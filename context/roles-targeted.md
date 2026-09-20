# Target Roles & Case-Study Mapping

> **Context Specification for AI Agents**:
> Use this file to tailor output to specific role types. Only emphasize case studies and skills that match the target role. Cross-reference `context/portfolio.md` and `context/skills.json` for evidence.

---

## Primary Target Roles

| Role | Fit Summary | Lead With |
|------|-------------|-----------|
| **Technical Product Manager** | 9+ years full-cycle delivery across fintech, marketplaces, and mobile. Fluent in API design, squad coordination, and business–tech alignment. | `faciliteacoches.com`, Facilitea Checkouts, `bcnmarket`, Tiendeo Mobile App |
| **Solutions Architect** | Hands-on architecture of microservices, event-driven systems, and cloud pipelines with banking and high-scale integrations. | `faciliteacoches.com`, `bcnmarket`, `aws-ip-change-tracker` |
| **Product Manager (Fintech / Banking)** | Deep checkout, payment, loan, insurance, and risk integration experience in regulated environments. | Facilitea Checkouts, `faciliteacoches.com` |
| **Senior Python Developer / Engineer** | Expert Python with PyPI open-source, serverless pipelines, and applied computer vision. | `google-api-support`, `aws-ip-change-tracker`, `bibliodetect` |
| **Engineering Manager (hands-on)** | Cross-functional leadership with ability to design systems and review code. | `faciliteacoches.com`, `bcnmarket`, Tiendeo Mobile App |

---

## Case Study → Role Mapping

| Case Study | Best For Roles | Key Proof Points |
|------------|----------------|------------------|
| `faciliteacoches.com` | TPM, Solutions Architect, Fintech PM | Marketplace from zero to production; banking integrations (loans, cards, insurance, risk); dealer CRM sync |
| Facilitea Checkouts | Fintech PM, TPM, Solutions Architect | Current role; checkout/payment evolution in regulated banking; GlobalPayments |
| `bcnmarket / bonusconsum` | TPM, Solutions Architect, Platform PM | 500k+ transactions in 3 months; municipal scale; high-availability cloud architecture |
| `google-api-support` | Python Engineer, Developer Tools, Automation | PyPI package; Google Workspace API abstraction; pandas integration |
| `libripolis.com` / `bibliodetect` | Python Engineer, AI/ML Engineer (applied CV) | YOLOv8 + EasyOCR pipeline; community platform |
| `aws-ip-change-tracker` | Cloud Engineer, Solutions Architect, Backend | Event-driven AWS (Lambda, SNS, EventBridge); Postgres CIDR indexing |
| Tiendeo Mobile App | Mobile PM, Growth PM, TPM | End-to-end app rebuild; 4.5-star rating; geofencing & push notifications |
| Tiendeo Cashback (CV only) | Growth PM, Product PM | Feature launch driving retention and merchant conversion |
| Reporting Automation (CV only) | Data Engineer, Python Engineer | 80% reporting time reduction via Google Slides/Sheets automation |

---

## Role-Specific Talking Points

### For Technical Product Manager roles
- Emphasize cross-functional squad orchestration, user story mapping, BPMN process modeling, and API contract design.
- Highlight measurable delivery: municipal platform scale, marketplace launch, sustained app ratings.
- De-emphasize deep ML training or native mobile coding — frame as product leadership with technical depth.

### For Solutions Architect roles
- Emphasize event-driven architecture, microservices, database design (PostgreSQL CIDR, NoSQL), and integration patterns.
- Reference `aws-ip-change-tracker` for concrete serverless design decisions.
- De-emphasize pure product marketing or SEO work unless relevant.

### For Fintech / Banking roles
- Lead with Facilitea Checkouts (current) and `faciliteacoches.com` (banking integrations).
- Highlight: consumer financing, card payments, insurance engines, risk scoring, GlobalPayments, compliance alignment.
- Do not claim expertise in specific regulatory frameworks (PCI-DSS, PSD2) unless documented in `context/`.

### For Python / Backend Engineering roles
- Lead with `google-api-support` (PyPI), `aws-ip-change-tracker`, and `bibliodetect`.
- Emphasize: type hints, serverless patterns, database-native features, automation philosophy.
- Frame TPM experience as a differentiator for senior/staff roles requiring product sense.

---

## Work Preferences (Non-Personal)

| Preference | Value |
|------------|-------|
| **Timezone** | CET / CEST (Spain) |
| **Work mode** | Hybrid or remote-friendly |
| **Industries** | Fintech, digital platforms, marketplaces, cloud/SaaS, public-sector digital services |
| **Role level** | Senior IC (TPM, Architect, Staff Engineer) or hands-on leadership |

---

## Agent Instructions

1. Identify the closest target role from the table above before generating output.
2. Select 2–3 case studies from the mapping table — do not list all projects indiscriminately.
3. Consult `context/limitations.md` before claiming any technology not listed as verified evidence.
4. Tag each talking point as **Verified**, **Inferable**, or **Gap** per `prompts/job-application-agent.md`.
