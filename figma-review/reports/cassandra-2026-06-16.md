# UX content audit report

**Figma file:** canonical.com data – Sites (node 4553:4538 – Apache Cassandra)
**Copy doc:** Not provided – exact match check skipped
**Date:** 2026-06-16
**Checks run:** UX quality check only

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor |
|---|---|---|---|---|
| UX quality check | 10 | 0 | 5 | 5 |

**Total issues:** 10 (zero critical, five needs work, five minor)

---

## Check 2: UX quality check

### Issues by page section

---

#### Navigation

##### 🟡 Needs Work
- **[Navigation]** – The sub-nav shows "Data" as a nav item alongside "Portfolio", "Services", and "Docs". An unresolved Figma comment questions why "Data" appears here, noting only the Canonical logo should link back to the Data landing page. This is a product page, not the Data hub – the "Data" nav item may confuse users about where they are.
  - *Found:* "Data | Portfolio | Services | Docs" | *Recommendation:* Remove the "Data" label from the sub-nav or confirm with designer that it is intentional

---

#### Hero

##### 🔵 Minor
- **[CTAs]** – Two CTAs: "Contact us" (primary) and "Give it a try" (secondary). Both are reasonably specific, but "Give it a try" is vague – try what? A download, a demo, a managed instance? A more specific label would set clearer expectations.
  - *Found:* "Give it a try" | *Recommendation:* Consider "Try Cassandra" or "Get started free" to clarify what happens next

---

#### Run Apache Cassandra across public and private clouds

##### ✅ Pass – clear heading, descriptive paragraph, relevant cloud/infrastructure logos (OpenStack, MicroCloud, VMware, AWS, Google Cloud, Microsoft Azure)

---

#### Our offering by the numbers (data spotlight)

##### 🟡 Needs Work
- **[Links]** – Three data spotlight cards with arrow links: "Contact us ›", "Check our automation ›", "Try it yourself ›". "Contact us" repeats the hero CTA. More importantly, the link text does not clearly connect to the data point above it – e.g. "1 million+ users / Served by our stack" leads to "Contact us ›", which is a generic action unrelated to the stat.
  - *Found:* "Contact us ›" under "1 million+ users" stat | *Recommendation:* Use link text that connects to the data point – e.g. "Explore our stack ›" or remove links from the data spotlight if they are not adding value

##### 🔵 Minor
- **[Tone & clarity]** – "~30 minutes / To get started" is good and specific, but the description "Get up and running quickly whether in your local lab environment or your live production infrastructure setup" is long for a data spotlight description (check character limit: max 100 characters).
  - *Found:* ~130 characters in description | *Recommendation:* Shorten to fit within 100-character limit – e.g. "Deploy to lab or production in under 30 minutes"

---

#### Apache Cassandra deployment options

##### 🟡 Needs Work
- **[CTAs]** – "Try it" under the Snap section is vague and undescriptive. It does not tell the user what will happen – will they install a snap, visit Snapcraft, or start a tutorial?
  - *Found:* "Try it" | *Recommendation:* Use a specific CTA like "Install the snap" or "Get the snap on Snapcraft"

- **[CTAs]** – "Check our software operator" is more descriptive but still passive. The word "check" does not convey a clear action.
  - *Found:* "Check our software operator" | *Recommendation:* Consider "Deploy with Juju" or "Use the Cassandra operator"

##### 🔵 Minor
- **[Structure & hierarchy]** – The two deployment options (Snap and Software operator) are presented as a simple two-row layout. With only two items, this works, but the descriptions are dense. The Software operator paragraph is notably longer than the Snap one.
  - *Found:* Two unequal-length descriptions | *Recommendation:* Balance paragraph lengths or add bullet points to the longer description

---

#### Popular Apache Cassandra use cases

##### 🟡 Needs Work
- **[Structure & hierarchy]** – The four use-case cards (Real-time analytics, Geo-distributed applications, Mission critical applications, Latency-sensitive applications) have long, dense paragraph descriptions. Each runs four to five lines with no formatting – hard to scan quickly.
  - *Found:* Four dense paragraph cards | *Recommendation:* Shorten to two to three lines each, or add a one-line summary before the detail paragraph

##### 🔵 Minor
- **[Tone & clarity]** – "Mission critical applications" – "mission critical" is typically hyphenated ("mission-critical") when used as a compound adjective.
  - *Found:* "Mission critical applications" | *Recommendation:* Use "Mission-critical applications"

---

#### Apache Cassandra support services

##### 🟡 Needs Work
- **[Links]** – The paragraph contains inline links with underlined text ("deployments", "Ubuntu Pro") but no clear indication of where they lead. Inline links in body copy should use descriptive text.
  - *Found:* "deployments" and "Ubuntu Pro" as inline links | *Recommendation:* Make link text more descriptive or add destinations – e.g. "managed deployments" or ensure URLs are specified in the copy doc

##### 🔵 Minor
- **[CTAs]** – "More details" is vague. More details about what? Paired with "Get in touch", a reviewer cannot tell the difference in destination.
  - *Found:* "More details" + "Get in touch" | *Recommendation:* Use a specific CTA like "See all services" or "View pricing"

---

#### Subscription-based / On-demand lists

##### ✅ Pass – clean two-column layout with clear category labels and bullet lists. "And much more" at the bottom of each is a common pattern.

---

#### Community and support

##### ✅ Pass – well-structured with clear category headings (Connect with the community, Contact us, Read more, Contribute). Links are descriptive: "Matrix chat", "Charmed Apache Cassandra", "Data backups", "How to choose a DBMS", etc.

---

#### Footer (trademark notice)

##### ✅ Pass – includes proper trademark attribution for Apache Cassandra. Standard Canonical footer.

---

### Designer annotations

Unresolved comments found on this node:

- **Node 4553:4538** – "@mattea qq, why is there a 'Data' nav item? same applies for the etcd page. This seems odd to me as only the CoC logo should have 'Data'" – Navigation question, unresolved (surfaced above).

---

## ✅ What looks good

- **Clear page structure** – logical flow from hero → cloud support → numbers → deployment options → use cases → services → community
- **Hero copy is strong** – "Enterprise support for Apache Cassandra" is clear and specific; the supporting paragraph covers automation, security maintenance, and SLA-backed support
- **Cloud logo strip** – immediately communicates multi-cloud support with recognizable logos
- **Data spotlight is effective** – "1 million+ users", "9+ automations", "~30 minutes" provide concrete proof points
- **Deployment options are clear** – two options (Snap vs Software operator) with distinct purposes
- **Community section** – well-organized with "Contribute" category including "Apache Cassandra snap" – good for the open-source audience
- **Trademark notice** – proper Apache Foundation attribution in the footer

---

## 🔲 Manual checks for reviewer

- [ ] **Live page compare** – open the live page and compare; confirm only the intended sections have changed
- [ ] **Keyboard navigation** – tab through the page to confirm correct focus order
- [ ] **Data spotlight links** – verify "Contact us ›", "Check our automation ›", "Try it yourself ›" link to the correct destinations
- [ ] **Deployment CTAs** – verify "Try it" and "Check our software operator" link to the correct destinations
- [ ] **Inline links in services section** – verify "deployments" and "Ubuntu Pro" link destinations
- [ ] **"More details" CTA** – confirm destination differs from "Get in touch"
- [ ] **Use case card images** – verify illustrations have appropriate alt text in the build
