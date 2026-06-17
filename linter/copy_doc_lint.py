#!/usr/bin/env python3
"""
Copy doc linter — deterministic pre-checks for Canonical copy docs.

Catches mechanical issues (character limits, banned words, product names,
punctuation, missing metadata, placeholders) so the LLM skill can focus
on judgment calls like tone and clarity.

Usage:
    python copy_doc_lint.py <path-to-copy-doc.md>
    python copy_doc_lint.py <path-to-copy-doc.md> --json
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class Finding:
    rule: str
    severity: str  # critical, needs-work, minor
    section: str
    message: str
    found: str = ""
    suggestion: str = ""
    line: int = 0


# ---------------------------------------------------------------------------
# Section parser
# ---------------------------------------------------------------------------

# Section markers used in Canonical copy doc templates
SECTION_MARKERS = [
    "HERO", "LOGO CLOUD", "DATA SPOTLIGHT", "TIERED LIST",
    "EQUAL HEIGHT ROW", "EQUAL HEIGHTS ROW", "OPTIONS/PRICING",
    "RESOURCES", "TEXT SPOTLIGHT", "QUOTE", "BLOG", "TABBED",
    "DIVIDED", "NEWSLETTER", "TABLE", "PRICING", "CTA BAND",
    "BASIC SECTION", "CUSTOMER STORIES",
]


def identify_section(line: str, prev_section: str) -> str:
    """Return the current section name based on markers in the line."""
    upper = line.strip().upper()

    # Check for explicit section markers (as standalone lines or inside template patterns)
    for marker in SECTION_MARKERS:
        # Match as standalone label or in backtick template markers
        if upper == marker or upper.startswith(marker + " "):
            return marker.title()
        if f"`{marker}" in upper and "PATTERN" in upper:
            return marker.title()

    # Check for METADATA TABLE or METADATA pattern
    if "METADATA" in upper and ("TABLE" in upper or "PATTERN" in upper):
        return "Metadata"

    # Check for visible page marker
    if "visible page starts here" in line.lower():
        return "Page Start"

    return prev_section


def parse_sections(lines: list[str]) -> list[tuple[str, int, str]]:
    """Return list of (section_name, line_number, line_text)."""
    result = []
    current_section = "Preamble"
    for i, line in enumerate(lines, 1):
        new_section = identify_section(line, current_section)
        if new_section != current_section:
            current_section = new_section
        result.append((current_section, i, line))
    return result


# ---------------------------------------------------------------------------
# Metadata parser
# ---------------------------------------------------------------------------

REQUIRED_METADATA = [
    "page title",
    "page description",
    "page url",
    "navigation",
    "page type",
]


def extract_metadata(lines: list[str]) -> dict[str, str]:
    """Extract metadata table key-value pairs from either doc format."""
    metadata = {}
    in_metadata = False
    for line in lines:
        upper = line.strip().upper()
        if "METADATA" in upper and ("TABLE" in upper or "PATTERN" in upper):
            in_metadata = True
            continue
        # End of metadata on next section marker or visible page marker
        if in_metadata and ("visible page starts here" in line.lower()
                           or any(line.strip().upper() == m for m in SECTION_MARKERS)
                           or any(line.strip().upper().startswith(m + " ") for m in SECTION_MARKERS)):
            break
        # Also end on template pattern markers for other sections
        if in_metadata and re.match(r'^\|\s*`[A-Z].*pattern', line, re.IGNORECASE):
            if "METADATA" not in line.upper():
                break
        if not in_metadata:
            continue

        # Split line into pipe-separated cells
        if '|' not in line:
            continue
        cells = line.split('|')
        # Clean each cell
        clean_cells = []
        for c in cells:
            cleaned = re.sub(r'[\\*`]', '', c).strip()
            clean_cells.append(cleaned)
        # Remove empty cells from leading/trailing pipes
        clean_cells = [c for c in clean_cells if c]

        # Skip separator/formatting rows
        if all(re.match(r'^[:|-]+$', c) or not c for c in clean_cells):
            continue
        if len(clean_cells) == 1 and clean_cells[0].lower() == 'separator':
            continue

        # Find key-value pair: first substantive cell is key, next is value
        key = None
        val = ""
        for i, cell in enumerate(clean_cells):
            if not cell or cell.lower() == 'separator' or re.match(r'^[:|-]+$', cell):
                continue
            if key is None:
                key = cell.lower()
            else:
                val = cell
                break

        if key:
            metadata[key] = val

    return metadata


def check_metadata_completeness(metadata: dict[str, str]) -> list[Finding]:
    """Check that required metadata fields are present and filled."""
    findings = []
    for req in REQUIRED_METADATA:
        found = False
        for key, val in metadata.items():
            if req in key:
                found = True
                if not val or val.isspace():
                    findings.append(Finding(
                        rule="metadata-completeness",
                        severity="critical",
                        section="Metadata",
                        message=f"Required metadata field is empty: {key}",
                        found=f"'{key}' has no value",
                    ))
                break
        if not found:
            findings.append(Finding(
                rule="metadata-completeness",
                severity="critical",
                section="Metadata",
                message=f"Required metadata field missing: {req}",
            ))
    return findings


# ---------------------------------------------------------------------------
# Character limit checks
# ---------------------------------------------------------------------------

CHAR_LIMITS = {
    "page title": 60,
    "page description": 160,
}


def check_metadata_char_limits(metadata: dict[str, str]) -> list[Finding]:
    """Check character limits on metadata fields."""
    findings = []
    for key, val in metadata.items():
        for limit_key, limit in CHAR_LIMITS.items():
            if limit_key in key and val:
                # Strip markdown formatting for counting
                clean = re.sub(r'[*_]', '', val).strip()
                if len(clean) > limit:
                    findings.append(Finding(
                        rule="character-limits",
                        severity="needs-work",
                        section="Metadata",
                        message=f"{key} is {len(clean)} characters (limit: {limit})",
                        found=clean,
                        suggestion=f"Trim to {limit} characters or fewer",
                    ))
    return findings


# ---------------------------------------------------------------------------
# Style guide: UK spelling variants
# ---------------------------------------------------------------------------

UK_TO_US = {
    r"\bdata\s+centres?\b": "data center(s)",
    r"\blicences?\b": "license(s)",
    r"\bdefences?\b": "defense(s)",
    r"\bprogrammes?\b": "program(s)",
    r"\bper\s+cent\b": "percent",
    r"\bsceptical\b": "skeptical",
    r"\bcatalogues?\b": "catalog(s)",
    r"\btravell(ing|ed)\b": "traveling/traveled",
    r"\b\w+ise\b(?<!\bexercise\b)(?<!\badvertise\b)(?<!\bsupervise\b)(?<!\bcomprise\b)(?<!\bsurprise\b)(?<!\bwise\b)(?<!\botherwise\b)(?<!\blikewise\b)": "-ize form",
    r"\b\w+our\b(?<!\byour\b)(?<!\bfour\b)(?<!\bpour\b)(?<!\bhour\b)(?<!\btour\b)(?<!\bcontour\b)": "-or form (check if UK -our spelling)",
    r"\bwhilst\b": "while",
}

# More targeted -ise words to avoid false positives
ISE_WORDS = [
    (r"\borganise[sd]?\b", "organize"),
    (r"\bvirtualise[sd]?\b", "virtualize"),
    (r"\boptimise[sd]?\b", "optimize"),
    (r"\bcustomise[sd]?\b", "customize"),
    (r"\brecogni[sz]e[sd]?\b", None),  # skip, both valid
    (r"\bminimise[sd]?\b", "minimize"),
    (r"\bmaximise[sd]?\b", "maximize"),
    (r"\butilise[sd]?\b", "utilize (or better: use)"),
    (r"\bcontainerise[sd]?\b", "containerize"),
    (r"\bmodernise[sd]?\b", "modernize"),
    (r"\bprioritise[sd]?\b", "prioritize"),
    (r"\bcharacteri[sz]e[sd]?\b", None),
    (r"\bauthorise[sd]?\b", "authorize"),
    (r"\bstandardise[sd]?\b", "standardize"),
    (r"\bspecialise[sd]?\b", "specialize"),
    (r"\bcentralise[sd]?\b", "centralize"),
]

# Simple UK spelling pairs (exact words)
UK_WORDS = {
    "colour": "color",
    "colours": "colors",
    "behaviour": "behavior",
    "behaviours": "behaviors",
    "favour": "favor",
    "favourable": "favorable",
    "favourite": "favorite",
    "labour": "labor",
    "honour": "honor",
    "centre": "center",
    "centres": "centers",
}


def check_uk_spelling(text: str, section: str, line_num: int) -> list[Finding]:
    """Flag UK spelling variants."""
    findings = []
    matched_spans: list[tuple[int, int]] = []

    lower = text.lower()

    # Check "data centre" first (compound phrase takes priority)
    for m in re.finditer(r"\bdata\s+centres?\b", text, re.IGNORECASE):
        matched_spans.append((m.start(), m.end()))
        findings.append(Finding(
            rule="uk-spelling",
            severity="needs-work",
            section=section,
            message=f'UK spelling "{m.group()}" — use "data center"',
            found=m.group(),
            suggestion="data center",
            line=line_num,
        ))

    # "per cent"
    for m in re.finditer(r"\bper\s+cent\b", text, re.IGNORECASE):
        findings.append(Finding(
            rule="uk-spelling",
            severity="needs-work",
            section=section,
            message='"per cent" — use "percent"',
            found=m.group(),
            suggestion="percent",
            line=line_num,
        ))

    # Check exact UK words, skipping spans already covered
    for uk, us in UK_WORDS.items():
        pattern = rf"\b{uk}\b"
        for m in re.finditer(pattern, lower):
            if any(s <= m.start() < e for s, e in matched_spans):
                continue
            findings.append(Finding(
                rule="uk-spelling",
                severity="needs-work",
                section=section,
                message=f'UK spelling "{m.group()}" — use US spelling "{us}"',
                found=m.group(),
                suggestion=us,
                line=line_num,
            ))

    # Check -ise words
    for pattern, replacement in ISE_WORDS:
        if replacement is None:
            continue
        for m in re.finditer(pattern, text, re.IGNORECASE):
            findings.append(Finding(
                rule="uk-spelling",
                severity="needs-work",
                section=section,
                message=f'UK spelling "{m.group()}" — use "{replacement}"',
                found=m.group(),
                suggestion=replacement,
                line=line_num,
            ))

    return findings


# ---------------------------------------------------------------------------
# Product name enforcement
# ---------------------------------------------------------------------------

PRODUCT_NAME_RULES = [
    # (pattern, message, suggestion, severity)
    (r"\bMicrocloud\b(?!\.)", "MicroCloud requires capital C", "MicroCloud", "needs-work"),
    (r"\bmicrocloud\b(?!\.)", "MicroCloud requires capital M and C (unless sentence-initial handled)", "MicroCloud", "needs-work"),
    (r"\bVMWare\b", "VMware — lowercase 'w', not 'W'", "VMware", "needs-work"),
    (r"\bVmware\b", "VMware — capital W after VM", "VMware", "needs-work"),
    (r"\bvmware\b", "VMware should be capitalized", "VMware", "needs-work"),
    (r"\bUbuntu\s+Linux\b", 'Never use "Ubuntu Linux" — just "Ubuntu"', "Ubuntu", "needs-work"),
    (r"\bUbuntu\s+Advantage\b", 'Legacy name — use "Ubuntu Pro"', "Ubuntu Pro", "needs-work"),
    (r"\bUA-I\b", 'Legacy name — use "Ubuntu Pro"', "Ubuntu Pro", "needs-work"),
    (r"\bUbuntu\s+Pro\s+Apps\b", 'Legacy name — use "Ubuntu Pro"', "Ubuntu Pro", "needs-work"),
    (r"\bUbuntu\s+Pro\s+Infrastructure\b", 'Legacy name — use "Ubuntu Pro"', "Ubuntu Pro", "needs-work"),
    (r"\bExtended\s+Security\s+Maintenance\b", 'Use "Expanded Security Maintenance"', "Expanded Security Maintenance", "needs-work"),
    (r"\bEnd\s+of\s+Life\b", 'Use "End of Standard Support"', "End of Standard Support", "needs-work"),
    (r"\bEoL\b", 'Use "End of Standard Support"', "End of Standard Support", "needs-work"),
    (r"\bUbuntu\s+server\b", "Ubuntu Server requires capital S", "Ubuntu Server", "needs-work"),
    (r"\bUbuntu\s+Phone\b", 'Use "Ubuntu on phones"', "Ubuntu on phones", "needs-work"),
    (r"(?<!\w)open-source(?!\w)", '"open source" — no hyphen', "open source", "needs-work"),
    (r"(?<!\w)opensource(?!\w)", '"open source" — two words', "open source", "needs-work"),
    (r"(?<![.A-Z])Open\s+Source(?!\s+(Initiative|Definition|Security))", '"open source" — lowercase mid-sentence', "open source", "needs-work"),
]


def check_product_names(text: str, section: str, line_num: int) -> list[Finding]:
    """Check product and brand name rules."""
    findings = []
    for pattern, message, suggestion, severity in PRODUCT_NAME_RULES:
        for m in re.finditer(pattern, text):
            findings.append(Finding(
                rule="product-names",
                severity=severity,
                section=section,
                message=message,
                found=m.group(),
                suggestion=suggestion,
                line=line_num,
            ))
    return findings


# ---------------------------------------------------------------------------
# Banned words and phrases
# ---------------------------------------------------------------------------

BANNED_PHRASES = [
    (r"\bthe ability to\b", "rephrase — e.g. 'can'"),
    (r"\bis able to\b", "rephrase — e.g. 'can'"),
    (r"\bnot only\b.*?\bbut also\b", "wordy — simplify"),
    (r"\bbare\s+metal\b", "avoid 'bare metal'"),
    (r"\b(eliminate|execute|terminate|kill)\b", "avoid violent/negative language"),
    (r"\bleverage\b", "use 'use' instead"),
    (r"\bgoing forward\b", "remove — adds nothing"),
    (r"\bin order to\b", "simplify to 'to'"),
    (r"\bform factor\b", "avoid 'form factor'"),
    (r"\bend\s+users?\b", "use 'user' instead"),
    (r"\bdisruptive\b", "avoid 'disruptive'"),
    (r"\bexplosive\b", "avoid 'explosive'"),
]

FLOWERY_WORDS = {
    "assist": "help",
    "alleviate": "ease",
    "ameliorate": "improve",
    "approximately": "about",
    "ascertain": "learn",
    "attempt": "try",
    "cease": "stop",
    "desist": "stop",
    "commence": "begin",
    "initiate": "begin",
    "facilitate": "help",
    "magnitude": "size",
    "necessitate": "need",
    "numerous": "many",
    "prior to": "before",
    "possesses": "has",
    "purchase": "buy",
    "regarding": "about",
    "subsequently": "later",
    "utilize": "use",
    "utilise": "use",
    "whilst": "while",
}


def check_banned_words(text: str, section: str, line_num: int) -> list[Finding]:
    """Flag banned words and flowery language."""
    findings = []

    for pattern, suggestion in BANNED_PHRASES:
        for m in re.finditer(pattern, text, re.IGNORECASE):
            findings.append(Finding(
                rule="banned-words",
                severity="needs-work",
                section=section,
                message=f'Avoid "{m.group()}" — {suggestion}',
                found=m.group(),
                suggestion=suggestion,
                line=line_num,
            ))

    lower = text.lower()
    for word, replacement in FLOWERY_WORDS.items():
        if " " in word:
            pattern = rf"\b{re.escape(word)}\b"
        else:
            pattern = rf"\b{re.escape(word)}\b"
        for m in re.finditer(pattern, lower):
            findings.append(Finding(
                rule="flowery-language",
                severity="needs-work",
                section=section,
                message=f'Prefer plain English: "{word}" → "{replacement}"',
                found=word,
                suggestion=replacement,
                line=line_num,
            ))

    return findings


# ---------------------------------------------------------------------------
# Punctuation checks
# ---------------------------------------------------------------------------

def check_punctuation(text: str, section: str, line_num: int) -> list[Finding]:
    """Check punctuation rules."""
    findings = []

    # Em dash used as sentence break (— or ---)
    if "—" in text:
        findings.append(Finding(
            rule="punctuation",
            severity="minor",
            section=section,
            message="Use en dash with spaces ( – ) not em dash (—)",
            found="—",
            suggestion=" – ",
            line=line_num,
        ))

    # Hyphen used as sentence break (space-hyphen-space, but not in lists)
    # Only flag " - " that looks like a sentence break, not list items
    for m in re.finditer(r'(?<=[a-zA-Z]) - (?=[a-zA-Z])', text):
        findings.append(Finding(
            rule="punctuation",
            severity="minor",
            section=section,
            message="Use en dash with spaces ( – ) not hyphen ( - ) for sentence breaks",
            found=" - ",
            suggestion=" – ",
            line=line_num,
        ))

    # Exclamation marks
    if "!" in text and not text.strip().startswith(("!", "[!", "#")):
        # Skip markdown image syntax ![]
        clean = re.sub(r'!\[', '', text)
        if "!" in clean:
            findings.append(Finding(
                rule="punctuation",
                severity="minor",
                section=section,
                message="No exclamation marks in webpage copy",
                found="!",
                line=line_num,
            ))

    return findings


# ---------------------------------------------------------------------------
# Link and CTA checks
# ---------------------------------------------------------------------------

BANNED_LINK_TEXT = [
    "click here",
    "read more",
    "see more",
    "find out more",
    "learn more",
]


def extract_links(text: str) -> list[tuple[str, str]]:
    """Extract (link_text, url) pairs from markdown."""
    return re.findall(r'\[([^\]]+)\]\(([^)]*)\)', text)


def extract_bare_ctas(text: str) -> list[str]:
    """Extract CTA-style bracket text without URLs: [Contact us]."""
    # Match [text] not followed by (url)
    return re.findall(r'\[([^\]]+)\](?!\()', text)


def check_links_and_ctas(text: str, section: str, line_num: int) -> list[Finding]:
    """Check link text and CTA rules."""
    findings = []

    links = extract_links(text)
    bare_ctas = extract_bare_ctas(text)

    # Check for banned link text (substring match for phrases like "Click here to...")
    for link_text, url in links:
        lt_lower = link_text.strip().lower()
        for banned in BANNED_LINK_TEXT:
            if lt_lower == banned or lt_lower.startswith(banned + " "):
                findings.append(Finding(
                    rule="link-text",
                    severity="needs-work",
                    section=section,
                    message=f'Avoid "{link_text}" as link text — use descriptive text',
                    found=link_text,
                    line=line_num,
                ))
                break

    # Check for empty link destinations
    for link_text, url in links:
        if not url.strip():
            findings.append(Finding(
                rule="cta-destination",
                severity="critical",
                section=section,
                message=f'Link/CTA "{link_text}" has an empty destination',
                found=f"[{link_text}]()",
                suggestion="Add the destination URL",
                line=line_num,
            ))

    # Check for Google Drive links
    for link_text, url in links:
        if "drive.google.com" in url:
            findings.append(Finding(
                rule="asset-hosting",
                severity="needs-work",
                section=section,
                message="Resource hosted on Google Drive — move to asset manager",
                found=f"[{link_text}]({url})",
                suggestion="Host on Canonical asset manager",
                line=line_num,
            ))

    # Check for author comments in brackets: [AUTHOR: ...], [NOTE: ...], [EDITOR: ...]
    for m in re.finditer(r'\[(AUTHOR|EDITOR|NOTE|REVIEW|COMMENT)\s*:([^\]]+)\]', text, re.IGNORECASE):
        findings.append(Finding(
            rule="open-comment",
            severity="needs-work",
            section=section,
            message=f"Unresolved author comment: [{m.group(1)}: ...]",
            found=m.group(0),
            line=line_num,
        ))

    # Check for bare CTAs with no destination
    for cta in bare_ctas:
        # Skip template markers, section labels, and image refs
        if cta.startswith(("col:", "ch:", "HERO", "LOGO", "image")) or cta.upper() == cta:
            continue
        # Skip if it's clearly a section marker
        if any(cta.upper().startswith(m) for m in SECTION_MARKERS):
            continue
        # Skip logos instruction
        if "standard logos" in cta.lower() or "use the" in cta.lower():
            continue
        # Skip labels/tags (typically short, lowercase descriptors in brackets)
        clean_cta = cta.strip().rstrip("\\")
        if re.match(r'^[a-z][a-z0-9 -]+$', clean_cta) and len(clean_cta) < 25:
            continue
        # Skip author/editor comments (handled above)
        if re.match(r'(AUTHOR|EDITOR|NOTE|REVIEW|COMMENT)\s*:', cta, re.IGNORECASE):
            continue
        findings.append(Finding(
            rule="cta-destination",
            severity="critical",
            section=section,
            message=f'CTA "{cta}" has no destination URL',
            found=f"[{cta}]",
            suggestion="Add the destination URL",
            line=line_num,
        ))

    return findings


def check_link_consistency(all_links: list[tuple[str, str, str]]) -> list[Finding]:
    """Check that links with the same text go to the same destination."""
    findings = []
    text_to_urls: dict[str, set[str]] = {}
    text_to_section: dict[str, str] = {}

    for link_text, url, section in all_links:
        key = link_text.strip().lower()
        if key not in text_to_urls:
            text_to_urls[key] = set()
            text_to_section[key] = section
        text_to_urls[key].add(url)

    for text, urls in text_to_urls.items():
        if len(urls) > 1:
            findings.append(Finding(
                rule="link-consistency",
                severity="needs-work",
                section=text_to_section[text],
                message=f'Link text "{text}" points to {len(urls)} different URLs',
                found=f'"{text}" → {", ".join(sorted(urls))}',
            ))

    return findings


def check_duplicate_ctas(all_ctas: list[tuple[str, str]]) -> list[Finding]:
    """Flag duplicate CTA labels on the same page."""
    findings = []
    seen: dict[str, list[str]] = {}

    for cta_text, section in all_ctas:
        key = cta_text.strip().lower()
        if key not in seen:
            seen[key] = []
        seen[key].append(section)

    for text, sections in seen.items():
        if len(sections) > 1:
            findings.append(Finding(
                rule="duplicate-cta",
                severity="needs-work",
                section=sections[0],
                message=f'CTA "{text}" appears {len(sections)} times on the page (in {", ".join(sections)})',
                found=text,
                suggestion="Use distinct CTA text for each instance",
            ))

    return findings


# ---------------------------------------------------------------------------
# Placeholder / TBD detection
# ---------------------------------------------------------------------------

PLACEHOLDER_PATTERNS = [
    r"\bTBD\b",
    r"\bTBC\b",
    r"\bTK\b",
    r"\bTODO\b",
    r"\b[Pp]laceholder\b",
    r"\bLorem\s+ipsum\b",
    r"\bXXX\b",
    r"\b\[TBD\]\b",
    r"\b\[TODO\]\b",
]


def check_placeholders(text: str, section: str, line_num: int) -> list[Finding]:
    """Flag placeholder and TBD markers."""
    findings = []
    for pattern in PLACEHOLDER_PATTERNS:
        for m in re.finditer(pattern, text):
            findings.append(Finding(
                rule="placeholder",
                severity="critical",
                section=section,
                message=f"Unresolved placeholder: {m.group()}",
                found=m.group(),
                line=line_num,
            ))
    return findings


# ---------------------------------------------------------------------------
# Heading level checks
# ---------------------------------------------------------------------------

def check_heading_levels(lines: list[str]) -> list[Finding]:
    """Check for skipped heading levels."""
    findings = []
    prev_level = 0
    for i, line in enumerate(lines, 1):
        m = re.match(r'^(#{1,6})\s', line)
        if m:
            level = len(m.group(1))
            if prev_level > 0 and level > prev_level + 1:
                findings.append(Finding(
                    rule="heading-levels",
                    severity="needs-work",
                    section="Structure",
                    message=f"Skipped heading level: H{prev_level} → H{level}",
                    found=line.strip(),
                    line=i,
                ))
            prev_level = level
    return findings


# ---------------------------------------------------------------------------
# Superlatives and absolute claims
# ---------------------------------------------------------------------------

SUPERLATIVES = [
    r"\bunique\b",
    r"\bfirst\b",
    r"\bonly\b",
    r"\bsole\b",
    r"\bfastest\b",
    r"\blargest\b",
    r"\bbest\b",
    r"\bmost\b",
    r"\bunprecedented\b",
    r"\bexceptional\b",
    r"\bbest[\s-]+in[\s-]+class\b",
    r"\bbest[\s-]+of[\s-]+breed\b",
    r"\bcutting[\s-]+edge\b",
    r"\bstate[\s-]+of[\s-]+the[\s-]+art\b",
    r"\blatest\s+and\s+greatest\b",
    r"\bone[\s-]+of[\s-]+a[\s-]+kind\b",
    r"\bgame[\s-]+chang",
    r"\brevolutionary\b",
    r"\bsmallest\b",
]

SECURITY_CLAIMS = [
    (r"\bsecure\s+open\s+source\b", "use 'trusted open source'"),
    (r"\bmost\s+secure\b", "use 'designed with security in mind'"),
    (r"\bsecurity[\s-]+guaranteed\b", "use 'security-maintained'"),
    (r"\balways\s+secure\b", "use 'security-maintained'"),
    (r"\bfully\s+secured\b", "use 'we help you secure...'"),
]


def check_claims(text: str, section: str, line_num: int) -> list[Finding]:
    """Flag superlatives and security/absolute claims."""
    findings = []

    for pattern, suggestion in SECURITY_CLAIMS:
        for m in re.finditer(pattern, text, re.IGNORECASE):
            findings.append(Finding(
                rule="security-claims",
                severity="critical",
                section=section,
                message=f'Unprovable security claim: "{m.group()}" — {suggestion}',
                found=m.group(),
                suggestion=suggestion,
                line=line_num,
            ))

    for pattern in SUPERLATIVES:
        for m in re.finditer(pattern, text, re.IGNORECASE):
            # Skip common false positives in template/meta text
            word = m.group().lower()
            if word == "first" and ("first mention" in text.lower()
                                    or "first ones" in text.lower()
                                    or "first time" in text.lower()):
                continue
            findings.append(Finding(
                rule="superlatives",
                severity="needs-work",
                section=section,
                message=f'Superlative "{m.group()}" — verify it is backed by evidence',
                found=m.group(),
                line=line_num,
            ))

    return findings


# ---------------------------------------------------------------------------
# Number formatting
# ---------------------------------------------------------------------------

def check_numbers(text: str, section: str, line_num: int) -> list[Finding]:
    """Check number formatting rules."""
    findings = []

    # Space between value and unit
    for m in re.finditer(r'\b(\d+)\s+(GB|MB|KB|TB|GHz|b)\b', text):
        findings.append(Finding(
            rule="number-formatting",
            severity="minor",
            section=section,
            message=f'No space between value and unit: "{m.group()}"',
            found=m.group(),
            suggestion=m.group(1) + m.group(2),
            line=line_num,
        ))

    # Commas in large numbers (flag 4+ digits without comma, but not years or URLs)
    for m in re.finditer(r'(?<!\d)(\d{4,})(?!\d|[-/])', text):
        num = m.group(1)
        # Skip years (1900-2099) and version-like numbers
        if re.match(r'^(19|20)\d{2}$', num):
            continue
        # Skip numbers inside URLs or link destinations
        start = m.start()
        preceding = text[:start]
        if re.search(r'https?://\S*$', preceding) or re.search(r'\]\([^)]*$', preceding):
            continue
        if "," not in num and int(num) >= 10000:
            formatted = f"{int(num):,}"
            findings.append(Finding(
                rule="number-formatting",
                severity="minor",
                section=section,
                message=f'Use commas in numbers over 999: "{num}" → "{formatted}"',
                found=num,
                suggestion=formatted,
                line=line_num,
            ))

    return findings


# ---------------------------------------------------------------------------
# Main lint runner
# ---------------------------------------------------------------------------

def lint_file(filepath: str) -> list[Finding]:
    """Run all checks on a copy doc file."""
    path = Path(filepath)
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    findings: list[Finding] = []
    all_links: list[tuple[str, str, str]] = []
    all_ctas: list[tuple[str, str]] = []

    # Parse sections
    sections = parse_sections(lines)

    # Extract and check metadata
    metadata = extract_metadata(lines)
    findings.extend(check_metadata_completeness(metadata))
    findings.extend(check_metadata_char_limits(metadata))

    # Check heading levels (both standalone and inside table cells)
    findings.extend(check_heading_levels(lines))

    # Line-by-line checks
    for section_name, line_num, line in sections:
        # Skip empty lines, table separators, and binary/encoded data
        if not line.strip() or re.match(r'^\|[\s:|-]+\|$', line):
            continue
        if len(line) > 1000 and not re.search(r'[a-z]{3,}\s+[a-z]{3,}', line[:200], re.IGNORECASE):
            continue

        # Skip base64 image reference lines for placeholder checks
        is_image_ref = line.strip().startswith("[image") and "base64" in line

        # Skip preamble/template instructions for superlative checks
        is_preamble = section_name == "Preamble"

        findings.extend(check_uk_spelling(line, section_name, line_num))
        findings.extend(check_product_names(line, section_name, line_num))
        findings.extend(check_banned_words(line, section_name, line_num))
        findings.extend(check_punctuation(line, section_name, line_num))
        findings.extend(check_links_and_ctas(line, section_name, line_num))
        if not is_image_ref:
            findings.extend(check_placeholders(line, section_name, line_num))
        if not is_preamble:
            findings.extend(check_claims(line, section_name, line_num))
        findings.extend(check_numbers(line, section_name, line_num))

        # Collect links and CTAs for cross-line checks
        for link_text, url in extract_links(line):
            all_links.append((link_text, url, section_name))
            all_ctas.append((link_text, section_name))
        for cta_text in extract_bare_ctas(line):
            clean = cta_text.strip().rstrip("\\")
            # Only track real CTAs, not template markers or image refs
            if clean.startswith(("col:", "ch:", "image")) or clean.upper() == clean:
                continue
            if re.match(r'^image\d+$', clean, re.IGNORECASE):
                continue
            all_ctas.append((clean, section_name))

    # Cross-line checks
    findings.extend(check_link_consistency(all_links))
    findings.extend(check_duplicate_ctas(all_ctas))

    return findings


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

SEVERITY_ORDER = {"critical": 0, "needs-work": 1, "minor": 2}
SEVERITY_ICONS = {"critical": "🔴", "needs-work": "🟡", "minor": "🔵"}


def format_findings(findings: list[Finding], filepath: str) -> str:
    """Format findings as a readable report."""
    if not findings:
        return "✅ No issues found."

    lines = []
    lines.append(f"# Copy doc lint report")
    lines.append(f"**File:** {filepath}")
    lines.append("")

    # Summary
    by_severity = {"critical": 0, "needs-work": 0, "minor": 0}
    for f in findings:
        by_severity[f.severity] = by_severity.get(f.severity, 0) + 1

    total = len(findings)
    lines.append(f"**{total} issues:** "
                 f"{by_severity['critical']} critical, "
                 f"{by_severity['needs-work']} needs work, "
                 f"{by_severity['minor']} minor")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Group by section, then severity
    section_order = []
    section_findings: dict[str, list[Finding]] = {}
    for f in findings:
        if f.section not in section_findings:
            section_order.append(f.section)
            section_findings[f.section] = []
        section_findings[f.section].append(f)

    for section in section_order:
        lines.append(f"## {section}")
        lines.append("")

        sfindings = sorted(section_findings[section],
                           key=lambda f: SEVERITY_ORDER.get(f.severity, 9))

        for f in sfindings:
            icon = SEVERITY_ICONS.get(f.severity, "❓")
            line_ref = f" (line {f.line})" if f.line else ""
            lines.append(f"- {icon} **[{f.rule}]** {f.message}{line_ref}")
            if f.found:
                lines.append(f"  - *Found:* `{f.found}`")
            if f.suggestion:
                lines.append(f"  - *Suggestion:* {f.suggestion}")

        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Lint a Canonical copy doc for mechanical issues"
    )
    parser.add_argument("file", help="Path to the markdown copy doc")
    parser.add_argument("--json", action="store_true",
                        help="Output findings as JSON")
    args = parser.parse_args()

    if not Path(args.file).exists():
        print(f"Error: file not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    findings = lint_file(args.file)

    if args.json:
        print(json.dumps([asdict(f) for f in findings], indent=2))
    else:
        print(format_findings(findings, args.file))

    # Exit with non-zero if critical issues found
    if any(f.severity == "critical" for f in findings):
        sys.exit(2)
    elif findings:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
