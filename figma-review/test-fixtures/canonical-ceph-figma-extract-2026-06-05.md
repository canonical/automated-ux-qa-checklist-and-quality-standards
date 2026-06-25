# Figma text extraction snapshot — canonical.com/ceph

**File:** canonical.com-ceph---Sites (`d3yDJFcSFPv8baDTWnk0jR`), node `1:5640`
**Extracted:** 2026-06-05 via Figma MCP (`get_metadata` + `get_design_context`, section by section)
**Why this file exists:** a live Figma file can change between runs, so this is a frozen
record of exactly what the MCP returned for this test run. Compare future runs against it.

> Notation: `→ URL` = link destination (href) present in the export. **`→ (no link)`** =
> text is styled as a link/button but has NO href in the Figma export. Empty image alt text
> is NOT recorded as a finding here — see the test log: the code export always emits
> `alt=""`, so it cannot verify alt text.

---

## Header (2:1620)
Shared nav component — not extracted (out of scope, same as copy doc).

## Hero (1:5643)
- h1: "Canonical Ceph"
- h2: "Open source software defined storage"
- body: "Scalable, multi-protocol storage, proven across numerous enterprise production environments, preferred for its on-demand public cloud-style storage provisioning. Deploy Ceph in minutes to support all on-premises workloads, including OpenStack, Kubernetes, and MicroCloud."
- CTA (primary): "Get in touch" → https://ubuntu.com/ceph#get-in-touch
- CTA (secondary): "Calculate your storage costs" → https://ubuntu.com/ceph/pricing-calculator
- hero image (no alt recorded)

## Data spotlight (1:6819)
- label: "Canonical Ceph: proven and trusted"
- "10+" / "Years"
- "1,000,000+" / "Downloads"
- "1 minute" / "To get started"

## Success stories with Canonical Ceph (1:7057)
- h2: "Success stories with Canonical Ceph"
- body: "Designed from the ground up for petabyte-scale deployments, Canonical Ceph software defined storage includes only open source components with highly automated operations to drive down total cost of ownership. If you do not have the in-house expertise to operate your own storage infrastructure, Canonical Ceph is also available as a managed service."
- link: "Learn more about Ceph support ›" → https://canonical.com/ceph/support
- body: "The Wellcome Sanger Institute initially opted for self-maintained Ceph storage, but as their capacity needs grew from 3 PB to over 20 PB, they turned to Canonical to resolve their scaling challenges. With the help of Canonical support, the Institute's latest Ceph rollout decreased from a month to just four days."
- link: "Learn how Wellcome Sanger achieved a cost-effective Ceph infrastructure ›" → https://pages.ubuntu.com/rs/066-EOV-335/images/Wellcome%20Sanger%20Institute%20Case%20Study.pdf

## Logo section (1:7792)
- label: "Notable Ceph users"
- body: "Ceph is used across a broad range of industries, from academic institutions, to telco, to cloud service providers (CSPs)."
- logos: CERN, Deutsche Telekom, Bloomberg, Cisco, DreamHost, DigitalOcean (4 more logos hidden in file: arm, mlflow, nec, rabobank)

## Canonical Ceph deployment and operations — Tiered list + Table (11:6611)
- h2: "Canonical Ceph deployment and operations"
- h5 "Deploying Ceph": "Canonical can help you to design and install your Ceph cluster, from hardware selection through to integration with the rest of your infrastructure."
- h5 "Operating Ceph": "Day-2 operations are straightforward, thanks to highly automated procedures for software version upgrades and hardware expansions, as well as managing hardware replacement. If you prefer to treat your storage as-a-service, [we offer Managed Ceph](http://ubuntu.com/ceph/managed) – a Ceph cluster fully managed by Canonical."  *(link uses http://, not https)*
- h5 "A choice of tooling": "The choice is yours: use your own operations framework, or take advantage of the benefits of deploying with Juju and Charms. Each Ubuntu LTS release ships with a version of Ceph that is supported for up to 15 years."
- h5 "Long Term Support (LTS)": "To maximize Ceph upgrade flexibility for customers, Ceph versions are regularly released and maintained through Ubuntu updates and security repositories, as well as the Ubuntu Cloud Archive. This maintains the balance between remaining at the forefront of innovation and providing long-term support predictability."
- h5 "Economic advantage": "Consolidate block, file, and object storage workloads into a single Ceph cluster to increase operational efficiency. Repatriate workloads from public clouds to cut costs. Discover [Ceph's cost benefits](https://ubuntu.com/blog/predict-compare-and-reduce-costs-with-our-s3-cost-calculator), and try our [Ceph pricing calculator](https://ubuntu.com/ceph/pricing-calculator) to learn how much you could save with Ceph."
- h5: "The Ubuntu and Ceph support cadence"
- table (cols: Ubuntu 20.04.x LTS Focal | 22.04.x LTS Jammy | 24.04.x LTS Noble | 26.04.x LTS Resolute):
  - Ceph Quincy 17.2.x | Ceph Reef 18.2.x | Ceph Squid 19.2.x | Ceph Tentacle 20.2.x *
  - Ceph Pacific 16.2.x | Ceph Quincy 17.2.x * | – | –
  - Ceph Octopus 15.2.x * | – | – | –
- footnote: "* Releases denoted with an asterisk are supported under the full LTS commitment."

## More choice for your infrastructure — Equal heights (11:4885)
- h2: "More choice for your infrastructure"
- body: "Across all shapes and sizes of infrastructure, Canonical Ceph provides all the benefits of upstream Ceph in easily deployable and security maintained packages."
- button: "Install now" → **(no link)**
- block 1 "Storage-as-a-Service": "Juju-orchestrated, snap-delivered private cloud storage. Model based operations make it easy to get started with Ceph, and even easier to scale and maintain." — link "Find out more on Charmhub ›" → **(no link)**
- block 2 "Ceph containers": "Deploy and manage Ceph using your own choice of tooling, like cephadm or Rook, with trusted OCI compliant container images from Canonical." — link "Find out more on GitHub ›" → **(no link)**
- block 3 "Training / Local dev": "Use the lightweight snap for small scale deployments, snaptraining, and local-development." — link "Find out more in the Snap Store ›" → **(no link)**

## Why choose Canonical Ceph? — Basic section (11:5767)
- h2: "Why choose Canonical Ceph?"
- body: "Canonical Ceph management tooling enables you to orchestrate the entire lifecycle of deployment, configuration, and operation of a Ceph cluster, no matter its size or complexity. Our tooling simplifies both installation automation and Day-2 operations orchestration, including monitoring, scaling, upgrades, and hardware maintenance – all while remaining interoperable with other infrastructure and application management solutions."
- h5: "Benefits of Canonical Ceph" (proper bulleted list):
  - Highly scalable, from Terabytes to Exabytes
  - Highly reliable, with no single point of failure
  - Protect your data with replication and erasure coding
  - Enable BCP/DR with remote replication
  - Highly secure client authentication and data at rest encryption
  - Compatible with Amazon S3 and OpenStack Swift APIs
  - Decrease CapEx by using commodity hardware
  - Decrease OpEx through failure detection, self-management, and self-healing
  - Configurable and optimizable for cost and performance

## Learn more about Canonical Ceph — Resources (11:7757)
- h2: "Learn more about Canonical Ceph"
- "Canonical Ceph for Enterprise" → https://www.brighttalk.com/webcast/6793/520582 — "A single Ceph cluster can address block, file, and object storage needs… In this webinar, we review the storage challenges faced by enterprises…"
- "Cloud storage cost optimization" → **(no link)** — "Calculating the total cost of ownership of cloud storage isn't straightforward… In this webinar, we break down the total cost of storing data in public clouds…"
- "Introduction to cloud-native storage" → https://ubuntu.com/engage/introduction-to-cloud-native-storage — "Moving away from hosted container solutions?…"
- "AI storage with Ceph" → https://ubuntu.com/engage/ai-storage-with-ceph — "Discover how AI impacts your storage systems…"

## The latest blogs about Ceph — Blog (11:8848)
- label: "The latest blogs about Ceph"
- 4 blog blocks, ALL identical placeholder content:
  - title (×4): "How to enable Real-time Ubuntu on your machine" → **(no link)**
  - body (×4): "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nec pulvinar nulla, non bibendum quam…"

## Footer (1:6234)
Shared component — not extracted (out of scope).
