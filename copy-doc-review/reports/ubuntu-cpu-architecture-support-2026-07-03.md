# UX content audit report – copy doc

**Document:** ubuntu.com_hardware – Ubuntu Hardware (Ubuntu CPU architecture support)
**Date:** July 3, 2026
**Page type:** Landing page
**Target audience:** Architects

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs work | 🔵 Minor | ❓ Needs review | ⬜ N/A |
|---|---|---|---|---|---|---|
| UX quality check | 12 | 3 | 9 | 7 | 2 | 2 |

**Total issues:** 19 (three critical, nine needs work, seven minor) · **Needs review:** two · **N/A sections:** Forms and inputs – landing page; Completeness (interactive states) – static landing page

---

## Issues by page section

### Metadata

#### 🟡 Needs work
- **[Navigation]** – Navigation placement requires discussion. The doc proposes changes to the meganav ("Certified Hardware" → "Hardware support," add "Architectures" section) but notes this "Needs discussion with Richard Ferreira." This must be resolved before design can proceed.
  - *Found:* "Needs discussion with Richard Ferreira."
  - *Recommendation:* Finalize the navigation decision and update the doc with the agreed placement.

#### 🔵 Minor
- **[Completeness]** – The "Link to asset manager tag" field is empty.
  - *Found:* Empty cell.
  - *Recommendation:* Confirm whether this should be populated before handoff to design.

---

### Hero

#### 🔴 Critical
- **[CTAs]** – The hero has two CTAs with nearly identical meaning: a button labeled "Learn more" and a link labeled "Find out more about our supported architectures." Both are vague and effectively say the same thing.
  - *Found:* Button: "Learn more" / Link: "Find out more about our supported architectures >"
  - *Recommendation:* Differentiate the two CTAs. The button could be "Explore architectures" and the link could be "Read the supported architectures documentation >." Alternatively, remove one of them – two CTAs to the same destination is redundant.

#### 🟡 Needs work
- **[CTAs]** – "Learn more" is a generic CTA that the style guide explicitly flags. It does not describe what the user will learn.
  - *Found:* "Learn more" (hero button)
  - *Recommendation:* Use a specific action verb, such as "Explore architectures" or "Get started."

- **[CTAs]** – "Find out more" is equally vague and listed as a non-descriptive CTA in the style guide.
  - *Found:* "Find out more about our supported architectures >"
  - *Recommendation:* Consider: "Read the supported architectures documentation >" or "View all supported architectures >."

#### 🔵 Minor
- **[Accessibility]** – The hero image asset is hosted on Google Drive.
  - *Found:* Asset link points to `drive.google.com`.
  - *Recommendation:* Move to the Canonical asset manager before handoff.

---

### Section 1: "Our philosophy: why Ubuntu's multi-architecture support matters"

#### 🔴 Critical
- **[Character limits]** – The main paragraph is 969 characters, exceeding the 900-character limit for a basic section supporting paragraph.
  - *Found:* 969-character paragraph.
  - *Recommendation:* Trim by approximately 70 characters. The opening two sentences could be condensed.

#### 🟡 Needs work
- **[Character limits]** – The additional paragraph (in a `ch:250` slot) is 333 characters, exceeding the 250-character limit.
  - *Found:* 333-character paragraph in a 250-character slot.
  - *Recommendation:* Trim by approximately 83 characters.

- **[Character limits]** – Both CTA buttons exceed the 20-character limit. "Learn about Ubuntu Pro" is 22 characters and "Find Ubuntu Desktop for your platform" is 37 characters.
  - *Found:* Two oversized button CTAs (22 and 37 chars).
  - *Recommendation:* Shorten to fit within 20 characters. For example: "Get Ubuntu Pro" (14 chars) and "Get Ubuntu Desktop" (18 chars).

#### 🔵 Minor
- **[Accessibility]** – The section image asset is hosted on Google Drive.
  - *Found:* Asset link points to `drive.google.com`.
  - *Recommendation:* Move to the Canonical asset manager.

---

### Section 2: "Maximizing silicon performance through architecture variants"

#### 🔴 Critical
- **[Character limits]** – The main paragraph is 1,195 characters, significantly exceeding the 900-character limit.
  - *Found:* 1,195-character paragraph in a `ch:900` slot.
  - *Recommendation:* This paragraph contains two distinct topics (architecture variants generally, and AMD64v3 specifically). Consider splitting into two sections or trimming substantially.

#### 🟡 Needs work
- **[CTAs]** – The CTA link text is just "Learn more" – the descriptive part ("about AMD64v3") falls outside the link.
  - *Found:* "[Learn more](…) about AMD64v3"
  - *Recommendation:* Make the full phrase the link text: "[Learn more about AMD64v3 >](…)" or better: "[Explore the AMD64v3 variant >](…)."

#### 🔵 Minor
- **[Accessibility]** – The section image asset is hosted on Google Drive.
  - *Found:* Asset link points to `drive.google.com`.
  - *Recommendation:* Move to the Canonical asset manager.

---

### Section 3: "Architecture vs. certification"

#### 🟡 Needs work
- **[Character limits]** – The main paragraph is 1,062 characters, exceeding the 900-character limit.
  - *Found:* 1,062-character paragraph in a `ch:900` slot.
  - *Recommendation:* Trim by approximately 162 characters. The paragraph repeats "laptops, desktops, IoT devices, or servers" twice – consolidating would help.

- **[Character limits]** – Both CTA buttons exceed the 20-character limit. "Find certified hardware" is 23 characters and "Learn about the program" is 23 characters.
  - *Found:* Two oversized button CTAs (23 chars each).
  - *Recommendation:* Shorten to 20 characters or fewer. For example: "Find hardware" (13 chars) and "About the program" (17 chars). Alternatively, use these as CTA links (60-character limit) instead of buttons.

- **[Completeness]** – An empty CTA placeholder remains in the template: "CTA – 60 characters >."
  - *Found:* Unfilled CTA slot.
  - *Recommendation:* Either fill in the CTA text or remove the placeholder row.

#### 🔵 Minor
- **[Accessibility]** – The section image asset is hosted on Google Drive.
  - *Found:* Asset link points to `drive.google.com`.
  - *Recommendation:* Move to the Canonical asset manager.

- **[Links]** – The certified hardware catalog link uses `http://` instead of `https://`.
  - *Found:* `[certified hardware catalog](http://ubuntu.com/certified)`
  - *Recommendation:* Update to `https://ubuntu.com/certified`.

---

### Resources

#### 🟡 Needs work
- **[Accessibility]** – Two resource images have placeholder alt text `[ALT TEXT]` that has not been filled in.
  - *Found:* `[ALT TEXT]` in two resource rows.
  - *Recommendation:* Add descriptive alt text for each image.

- **[Accessibility]** – Two resource images have placeholder `[Asset link]` with no actual asset URL.
  - *Found:* `[Asset link]` (no URL) in two rows.
  - *Recommendation:* Add the asset manager URLs or source the images.

#### 🔵 Minor
- **[CTAs]** – "Contact Us!" in the resources section uses an exclamation mark. The style guide says no exclamation marks in webpage copy.
  - *Found:* "please [Contact Us!](…)"
  - *Recommendation:* Change to "Contact us" (lowercase "u," no exclamation mark).

---

### Brand and style compliance

#### 🟡 Needs work (style)
- **[A1 – UK spelling]** – Four UK spelling variants found in the copy:
  - "whilst" (section 2) → should be "while"
  - "optimised" (section 2) → should be "optimized"
  - "optimisations" (section 3) → should be "optimizations"
  - "catalogue" (section 3) → should be "catalog"

#### 🔵 Minor (style)
- **[A14 – Consistency]** – Section 3 uses both "catalogue" and "catalog" in the same paragraph. Beyond the UK/US spelling issue, the inconsistency itself should be resolved.
  - *Found:* "the certified hardware catalogue lists…" and "explore our certified hardware catalog"
  - *Recommendation:* Use "catalog" consistently throughout.

---

## ❓ Needs review

- **[Metadata]** – The suggested URL is `ubuntu.com/architecture`, but the doc title and content focus on "hardware" and "CPU architectures." Confirm whether this URL is final or whether something like `ubuntu.com/hardware/architectures` would better reflect the IA.
  - *Found:* `ubuntu.com/architecture`
  - *Question:* Is this the agreed-upon URL path?

- **[Section 3]** – The paragraph mentions "up to 15 years of security and stability updates" for certified hardware. Confirm whether this claim applies specifically to certified hardware or to Ubuntu Pro generally – conflating the two could be misleading.
  - *Found:* "certified devices receive up to 15 years of security and stability updates"
  - *Question:* Is this accurate for certified hardware specifically, or does it depend on an Ubuntu Pro subscription?

---

## ⬜ Not applicable

- **Forms and inputs** – N/A: this is a landing page with no form or interactive input.
- **Completeness (interactive states)** – N/A: this is a static landing page with no interactive flows.

---

## ✅ What looks good

- **Structure and hierarchy** – The page follows a clear narrative arc: hero → philosophy/why → technical capability (variants) → certification → resources. Logical and easy to follow.
- **Metadata** – Page title (31 chars) and page description (111 chars) are well within their character limits.
- **Hero** – Title (51 chars) and subtitle (36 chars) are within limits. The supporting paragraph (203 chars) is concise and within the 300-character limit. Hero image has proper alt text defined: "A CPU mounted on a circuit board."
- **Section images** – All section images have descriptive alt text annotations (e.g. "A selection of chips on a circuit board," "A person wearing gloves holding a computer chip," "A set of server racks with visible network cabling").
- **Active voice** – The doc predominantly uses active voice, reading well for the architect audience.
- **Serial comma** – Consistently used throughout (e.g. "the motherboard, chipset, storage, networking, and peripherals").
- **Product names** – "Ubuntu," "Ubuntu Pro," "MAAS," "MicroCloud," "Ubuntu LTS," and "Canonical Livepatch" are all correctly named and capitalized.
- **"open source"** – Not used in this doc, so no issues.
- **Tone** – Authoritative and technically precise without being condescending – well suited to the architect audience.
- **Headings** – All in sentence case as required by the style guide.
