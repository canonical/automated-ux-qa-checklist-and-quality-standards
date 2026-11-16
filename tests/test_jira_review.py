import contextlib
import io
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import jira_review as review
import review as launcher


class JiraReviewTests(unittest.TestCase):
    def setUp(self):
        setting = patch("jira_review.REPORT_REPO", "example/UX-review-reports")
        setting.start()
        self.addCleanup(setting.stop)

    @patch("jira_review.REPORT_REPO", "")
    @patch("jira_review.run_command")
    def test_missing_report_destination_fails_before_github_access(self, command):
        with self.assertRaisesRegex(review.ReviewError, "your own private repository"):
            review.publish(Path("unused.md"), "UX-1")
        command.assert_not_called()

    @patch("jira_review.jira_request")
    def test_jira_comment_contains_clickable_report_link(self, request):
        url = "https://github.com/example/UX-review-reports/blob/main/report.md"
        review.post_link("https://team.atlassian.net", "user", "token", "UX-1", url)
        body = request.call_args.args[4]["body"]
        nodes = body["content"][0]["content"]
        self.assertIn({"type": "text", "text": url, "marks": [
            {"type": "link", "attrs": {"href": url}}
        ]}, nodes)

    @patch("review.ensure_venv_and_reexec")
    @patch("review.subprocess.run")
    def test_launcher_routes_jira_url(self, run, ensure_venv):
        run.return_value.returncode = 0
        url = "https://team.atlassian.net/browse/UX-1"
        with patch("sys.argv", ["review.py", url]):
            self.assertEqual(launcher.main(), 0)
        self.assertEqual(run.call_args.args[0][1:], [str(launcher.JIRA_REVIEW), url])

    @patch("review.ensure_venv_and_reexec")
    @patch("review.subprocess.run")
    def test_launcher_still_routes_pr_url_and_flags(self, run, ensure_venv):
        run.return_value.returncode = 0
        url = "https://github.com/canonical/example/pull/42"
        with patch("sys.argv", ["review.py", url, "--demo-only"]):
            self.assertEqual(launcher.main(), 0)
        self.assertEqual(run.call_args.args[0][1:], [str(launcher.RUN_REVIEW), url, "--demo-only"])

    @patch.dict(os.environ, {}, clear=True)
    def test_jira_credentials_use_existing_mcp_configuration(self):
        with tempfile.TemporaryDirectory() as tmp:
            config = Path(tmp) / ".copilot" / "mcp-config.json"
            config.parent.mkdir()
            config.write_text(json.dumps({"mcpServers": {"jira": {"env": {
                "ATLASSIAN_BASE_URL": "https://team.atlassian.net/",
                "ATLASSIAN_EMAIL": "user",
                "ATLASSIAN_API_TOKEN": "token",
            }}}}), encoding="utf-8")
            with patch("jira_review.Path.home", return_value=Path(tmp)):
                self.assertEqual(review.jira_credentials(), ("https://team.atlassian.net", "user", "token"))

    def test_ticket_must_match_configured_https_site(self):
        self.assertEqual(
            review.parse_ticket("https://team.atlassian.net/browse/UX-42?x=1", "https://team.atlassian.net"),
            "UX-42",
        )
        for ticket in (
            "https://other.atlassian.net/browse/UX-42",
            "http://team.atlassian.net/browse/UX-42",
            "https://team.atlassian.net/browse/UX-42/extra",
        ):
            with self.subTest(ticket=ticket), self.assertRaises(review.ReviewError):
                review.parse_ticket(ticket, "https://team.atlassian.net")

    def test_extracts_nested_links_and_rejects_spoofed_hosts(self):
        data = {"description": [
            {"attrs": {"href": "https://www.figma.com/design/ABC/name?node-id=1-2"}},
            {"text": "Doc: https://docs.google.com/document/d/123/edit)."},
            {"text": "https://figma.com.evil.example/design/ABC/name"},
            {"text": "https://www.figma.com:bad/design/ABC/name"},
        ]}
        figma, docs = review.extract_links(data)
        self.assertEqual(figma, ["https://www.figma.com/design/ABC/name?node-id=1-2"])
        self.assertEqual(docs, ["https://docs.google.com/document/d/123/edit"])

    @patch("jira_review.jira_request")
    def test_fetches_all_comment_pages_and_remote_links(self, request):
        request.side_effect = [
            {"fields": {}},
            [{"object": {"url": "https://www.figma.com/file/ABC/a?node-id=1-2"}}],
            {"comments": [{"body": "first"}], "total": 2},
            {"comments": [{"body": "https://docs.google.com/document/d/doc/edit"}], "total": 2},
        ]
        figma, docs = review.get_ticket_links("https://team.atlassian.net", "x", "y", "UX-1")
        self.assertEqual(len(figma), 1)
        self.assertEqual(len(docs), 1)
        self.assertIn("startAt=1", request.call_args.args[3])

    @patch("jira_review.run_command")
    def test_public_repo_is_never_written(self, command):
        command.return_value = json.dumps({"visibility": "PUBLIC"})
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "report.md"
            path.write_text("test", encoding="utf-8")
            with self.assertRaises(review.ReviewError):
                review.publish(path, "UX-1")
        self.assertEqual(command.call_count, 1)

    @patch("jira_review.run_command")
    def test_publish_returns_immutable_commit_link(self, command):
        sha = "a" * 40
        command.side_effect = [
            json.dumps({"visibility": "PRIVATE", "defaultBranchRef": {"name": "main"}}),
            json.dumps({"commit": {"sha": sha}}),
        ]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "report.md"
            path.write_text("report", encoding="utf-8")
            url = review.publish(path, "UX-1")
        self.assertIn(f"/blob/{sha}/figma-reviews/ux-1-", url)
        self.assertEqual(json.loads(command.call_args.kwargs["input_text"])["branch"], "main")

    @patch("jira_review.figma_server_registered", return_value=True)
    @patch("jira_review.subprocess.run")
    def test_incomplete_report_is_not_accepted(self, run, registered):
        run.return_value.returncode = 0
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "report.md"
            path.write_text("Only UX quality", encoding="utf-8")
            with self.assertRaises(review.ReviewError):
                review.run_review("https://figma.com/design/abc/x?node-id=1-2",
                                  "https://docs.google.com/document/d/123/edit",
                                  Path(tmp) / "doc.md", path, False)

    @patch("jira_review.figma_server_registered", return_value=True)
    @patch("jira_review.subprocess.run")
    def test_complete_report_records_unapproved_copy(self, run, registered):
        run.return_value.returncode = 0
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "report.md"
            path.write_text("Exact copy match\nUX quality\nBrand & style", encoding="utf-8")
            review.run_review("https://figma.com/design/abc/x?node-id=1-2",
                              "https://docs.google.com/document/d/123/edit",
                              Path(tmp) / "doc.md", path, False)
            content = path.read_text(encoding="utf-8")
        self.assertIn("not confirmed as approved", content)
        self.assertIn("https://docs.google.com/document/d/123/edit", content)

    @patch("jira_review.figma_server_registered", return_value=True)
    @patch("jira_review.subprocess.run")
    def test_explicit_model_is_forwarded_to_copilot(self, run, registered):
        run.return_value.returncode = 0
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "report.md"
            path.write_text("Exact copy match\nUX quality\nBrand & style", encoding="utf-8")
            review.run_review("https://figma.com/design/abc/x?node-id=1-2",
                              "https://docs.google.com/document/d/123/edit",
                              Path(tmp) / "doc.md", path, False, "auto")
        command = run.call_args.args[0]
        self.assertEqual(command[command.index("--model") + 1], "auto")

    @patch.dict(os.environ, {"ATLASSIAN_BASE_URL": "https://team.atlassian.net",
                             "ATLASSIAN_EMAIL": "user", "ATLASSIAN_API_TOKEN": "token"})
    @patch("jira_review.post_link")
    @patch("jira_review.publish", return_value="https://github.com/private/report")
    @patch("jira_review.run_review")
    @patch("jira_review.run_command")
    @patch("jira_review.get_ticket_links")
    @patch("builtins.input", side_effect=["y", "n"])
    def test_full_flow_publishes_then_comments(self, user_input, links, command, run, publish, post):
        links.return_value = (["https://figma.com/design/abc/x?node-id=1-2"],
                              ["https://docs.google.com/document/d/123/edit"])

        def export(args):
            Path(args[-1]).write_text("copy", encoding="utf-8")
            return ""

        command.side_effect = export
        with patch("sys.argv", ["jira_review.py", "https://team.atlassian.net/browse/UX-1"]):
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(review.main(), 0)
        self.assertFalse(run.call_args.args[-2])
        self.assertIsNone(run.call_args.args[-1])
        post.assert_called_once_with("https://team.atlassian.net", "user", "token", "UX-1",
                                     "https://github.com/private/report")
        publish.assert_called_once()

    @patch.dict(os.environ, {"ATLASSIAN_BASE_URL": "https://team.atlassian.net",
                             "ATLASSIAN_EMAIL": "user", "ATLASSIAN_API_TOKEN": "token"})
    @patch("jira_review.post_link")
    @patch("jira_review.publish")
    @patch("jira_review.run_review")
    @patch("jira_review.run_command", side_effect=review.ReviewError("export failed"))
    @patch("jira_review.get_ticket_links")
    @patch("builtins.input", side_effect=["y", "y"])
    def test_fetch_failure_never_publishes_or_comments(self, user_input, links, command, run, publish, post):
        links.return_value = (["https://figma.com/design/abc/x?node-id=1-2"],
                              ["https://docs.google.com/document/d/123/edit"])
        with patch("sys.argv", ["jira_review.py", "https://team.atlassian.net/browse/UX-1"]):
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(review.main(), 1)
        run.assert_not_called()
        publish.assert_not_called()
        post.assert_not_called()


if __name__ == "__main__":
    unittest.main()
