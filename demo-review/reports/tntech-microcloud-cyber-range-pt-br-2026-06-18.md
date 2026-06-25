# UX content audit report – live page

**URL:** https://canonical-com-2633.demos.haus/case-study/tntech-microcloud-cyber-range-pt-br
**Date:** 2026-06-18
**Copy doc:** Tennessee Tech Uni Microcloud case study (LATAM portuguese)
**Note:** Static HTML was captured successfully. Interactive modal states and client-side validation were not exercised.

---

## Summary

| Check | ✅ Pass | 🔴 Critical | 🟡 Needs Work | 🔵 Minor |
|---|---|---|---|---|
| UX quality check | 10 | 1 | 2 | 2 |
| Copy doc match | 8 | 0 | 1 | 1 |

**Total issues:** 7 (1 critical, 3 needs work, 3 minor)

---

## Issues by page section

### Hero

#### 🔵 Minor
- **[Accessibility]** – The Tennessee Tech logo in the hero has an empty alt attribute.
  - *Found:* `alt=""` on the partner logo image | *Recommendation:* Add a short alt such as "Tennessee Tech University logo," or keep it decorative only if the team has explicitly decided the logo adds no information.

### Main content

#### 🔵 Minor
- **[Mobile Considerations]** – Several body sections are very dense and should be checked carefully at small breakpoints.
  - *Found:* Long paragraphs in "Construindo a infraestrutura de cibersegurança do amanhã," "Desafio," "Solução," and "Resultados" | *Recommendation:* Review line length, paragraph spacing, and scanability on mobile so the copy stays readable without feeling wall-like.

### Resultados

#### 🔵 Minor
- **[Copy doc match]** – The source copy links "Ubuntu Pro," but the demo shows it as plain text.
  - *Found:* Demo text "Ubuntu Pro" with no in-section link | *Recommendation:* Restore the link if the copy doc remains the source of truth for this section.

### CTA

#### 🟡 Needs Work
- **[Copy doc match]** – The CTA destination does not match the source copy doc.
  - *Found:* Demo CTA goes to `https://canonical.com/microcloud/contact-us` | *Recommendation:* Confirm whether the intended target is the copy doc link destination `https://canonical.com/microcloud/what-is-microcloud#get-in-touch` and align them.

### Contact modal

#### 🔴 Critical
- **[Forms & Inputs]** – The first textarea in the contact modal does not have a reliable field label attached to the control.
  - *Found:* The field under "What would you like to discuss?" renders as an unlabeled `<textarea id="comments">` with no usable associated label | *Recommendation:* Add a proper visible label or bind the prompt to the textarea with `label` or `aria-labelledby` so assistive technology announces the field correctly.

#### 🟡 Needs Work
- **[Copy doc match]** – The modal content switches from Portuguese into English, which breaks the localized experience.
  - *Found:* "Contact Canonical," "Contact the Canonical team to learn more about our products and services," "First name:","Country:","I agree to receive information..." | *Recommendation:* Localize the full modal, including helper copy, field labels, consent text, and success or error messaging, into Brazilian Portuguese.

- **[CTAs]** – The submit action is generic and does not tell the user what will happen.
  - *Found:* "Submit" | *Recommendation:* Use a specific, localized action label such as "Enviar mensagem" or equivalent.

---

## ✅ What looks good

- The visible case study section order matches the copy doc from hero through CTA.
- Core body copy in "Sobre," "Destaques," "Construindo...," "Desafio," "Solução," and "Resultados" matches the source copy closely.
- All four Travis Lee quotes present in the copy doc are also present on the demo.
- Headings are descriptive and follow a clear hierarchy through the article content.
- The page includes breadcrumbs, which helps users understand where they are.
- The main CTA text is specific enough to communicate the next step.
- Required fields in the contact form appear to be visibly marked.

---

## 🔲 Manual checks for reviewer

- [ ] **Responsive behavior** – resize the browser or use device emulation to check layout and readability at mobile, tablet, and desktop breakpoints
- [ ] **Keyboard navigation** – tab through the page to confirm correct focus order, visible focus indicators, and accessible labels on interactive elements
- [ ] **Authenticated states** – log in and check any copy that only appears after authentication
- [ ] **JS-rendered content** – interact with the page to trigger dynamic states
