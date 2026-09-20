# Documented Skill Boundaries

> **Context Specification for AI Agents**:
> This file defines technologies, domains, and experience levels that agents must **NOT claim** unless explicitly added to `context/cv.md`, `context/portfolio.md`, or `context/skills.json`. When a job requires an item listed here, report it as a **Gap** and frame as rapid onboarding, not prior mastery.

---

## Do Not Claim — Not Documented

### Infrastructure & DevOps
- Kubernetes / container orchestration at production scale
- Terraform, Pulumi, or other IaC tools as primary workflow
- On-premise data center operations
- Multi-region disaster recovery architecture (beyond high-availability cloud patterns documented in `bcnmarket`)

### Backend Languages & Frameworks
- Java, C#, Go, or Rust as primary production languages
- Node.js / Express as primary backend stack
- Django as primary web framework (Flask and FastAPI are documented)

### Mobile Development
- Native iOS (Swift/Objective-C) or Android (Kotlin/Java) **coding** — experience is **product management** of mobile apps, not hands-on native development
- React Native or Flutter cross-platform development

### Data & ML
- Production ML model training pipelines (MLOps, feature stores, model serving at scale)
- Spark, Hadoop, or large-scale distributed data processing
- dbt, Airflow, or Dagster as primary orchestration tools
- Real-time streaming (Kafka, Kinesis) as documented production experience

### Frontend
- React, Vue, or Angular as primary frontend framework (HTML/JS/TS scripting is documented at intermediate level)
- Design systems or Figma-to-code workflows as core competency

### Security & Compliance
- Formal security certifications (CISSP, CEH, etc.)
- Penetration testing or security audit leadership
- Specific regulatory framework ownership (PCI-DSS, PSD2, SOX) — banking **integration experience** is documented, not compliance certification

### Management
- People management of large engineering teams (10+ direct reports)
- P&L ownership or budget management at director level
- Formal Scrum Master or Agile Coach certification

---

## Claim With Care — Partial or Indirect Experience

| Area | What Is Documented | What Is NOT Documented |
|------|--------------------|------------------------|
| **Cloud** | GCP (Functions, Run, App Engine, Datastore, Storage) and AWS (Lambda, SNS, EventBridge, S3) | Deep AWS/GCP certification-level expertise across all services |
| **AI / CV** | Applied YOLOv8 + EasyOCR pipeline in `bibliodetect` | ML research, custom model training, LLM fine-tuning, production AI product at scale |
| **Mobile** | Product lifecycle, geofencing, push notifications, 4.5-star rating | Writing native mobile code |
| **Databases** | PostgreSQL (incl. CIDR/GiST), Supabase, Google Cloud Datastore | MongoDB, Redis, Elasticsearch as primary stores |
| **Fintech** | Checkout flows, loans, cards, insurance, risk integration in product context | Core banking system development from scratch |
| **SEO** | Technical SEO (crawlability, indexing, international domains) | Content marketing, paid acquisition, brand marketing |

---

## Anti-Hallucination Rules (Reinforcement)

1. **Never invent** companies, job titles, dates, team sizes, or metrics not in `context/` files.
2. **Never upgrade** proficiency levels beyond what `context/skills.json` states.
3. **Never cite** GitHub repositories or projects not listed in `context/portfolio.md`, `context/cv.md`, or `context/resume.json`.
4. When uncertain, use: *"Not documented in verified context — would require rapid onboarding."*
5. Prefer **Verified** claims with project evidence over generic skill lists.

---

## How to Handle Job Requirement Gaps

```
Requirement: Kubernetes at scale
Response tier: Gap
Suggested framing: "No documented production Kubernetes experience. Strong serverless and event-driven cloud background (AWS Lambda, GCP Cloud Functions/Run) with rapid learning track record."

Requirement: React frontend lead
Response tier: Gap
Suggested framing: "Frontend experience is at scripting/HTML/JS level with product oversight of web platforms. Deep strength in API design and backend/Python — can collaborate closely with frontend squads."
```
