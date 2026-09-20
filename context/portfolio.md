# Portfolio & Engineering Case Studies: Víctor Pérez Berruezo

> **Context Specification for AI Agents**:
> This document details real-world software products, technical architectures, and open-source libraries led or engineered by Víctor Pérez Berruezo (`vperezb`). Each case study follows a structured format (*Context/Problem*, *Solution & Architecture*, *Tech Stack*, *Key Capabilities*, *Impact & Outcomes*) designed for automated ingestion, technical interview prep, and capability verification.

---

## 1. `faciliteacoches.com` — Enterprise Car Marketplace & Integrated Fintech Ecosystem

- **Company / Context**: CaixaBank Tech (Facilitea)
- **Live Platform**: [faciliteacoches.com](https://faciliteacoches.com/)
- **Role**: IT Project Manager / Technical Solutions Architect
- **Domain**: Fintech, Automotive Marketplaces, Banking Services Integration

### Context & Problem
CaixaBank sought to create a comprehensive digital car marketplace enabling customers to browse verified dealership vehicle stock, obtain instant financing, calculate insurance quotes, and execute transactions online within a unified, secure banking environment.

### Solution & Architecture
Víctor led the technical discovery, architecture design, and cross-functional delivery from inception:
- **Cross-Functional Orchestration**: Coordinated operations, UX/UI, business stakeholders, and engineering squads across multiple agile sprints.
- **Microservices & API Architecture**: Designed RESTful APIs and asynchronous event-driven communications between frontend portals, dealer CRMs, and core banking backends.
- **Fintech & Banking Integrations**:
  - Integrated automated consumer credit / loan evaluation workflows and instant calculation engines.
  - Connected payment gateways and card processing systems (GlobalPayments solutions).
  - Integrated automated vehicle insurance calculation and risk assessment pipelines.
- **Inventory & CRM Synchronization**: Architected real-time and batch synchronization channels connecting independent automotive dealer CRMs with the central catalog.

### Tech Stack & Methodologies
`Microservices`, `REST APIs`, `Event-Driven Architecture`, `Fintech / Banking Integrations (Loans, Cards, Insurance, Risk)`, `PostgreSQL / NoSQL`, `BPMN Process Modeling`, `Scrum & Kanban`.

### Key Outcomes & Impact
- Successfully launched `faciliteacoches.com` as CaixaBank's flagship automotive marketplace.
- Reduced friction between vehicle discovery and loan origination, shortening credit approval latency for end customers.

### Individual Contribution
- **Owned**: Technical discovery, API/event architecture design, banking integration strategy, and cross-functional delivery coordination.
- **Team delivery**: Frontend portals, dealer CRM integration, engineering squad implementation, and UX/operations alignment.

---

## 2. Facilitea Checkouts — Banking Checkout & Payment Platform Evolution

- **Company / Context**: CaixaBank Tech (Facilitea)
- **Role**: IT Project Manager — Checkouts
- **Domain**: Fintech, Payment Processing, Banking Compliance, Checkout UX

### Context & Problem
The Facilitea platform requires continuous evolution of checkout and payment flows to support new commercial products, maintain integration with core banking infrastructure, and meet strict security and regulatory standards across multiple payment channels.

### Solution & Architecture
- Lead technical analysis, architectural design, and phased delivery of checkout and payment solution improvements within the Facilitea ecosystem.
- Ensure end-to-end system integration and architectural consistency between frontend checkout experiences, payment gateways, and core banking backends.
- Align technical decisions with banking security standards, compliance requirements, and commercial business needs across cross-functional squads.

### Tech Stack & Methodologies
`Checkout Flows`, `Payment Gateway Integration`, `GlobalPayments`, `Banking Security Standards`, `API Design`, `Cross-Functional Squad Coordination`, `BPMN Process Modeling`, `Scrum & Kanban`.

### Key Outcomes & Impact
- Owns the technical direction of checkout evolution within a regulated banking environment.
- Bridges product, engineering, and banking infrastructure teams to deliver compliant, integrated payment experiences.

### Individual Contribution
- **Owned**: Technical analysis, checkout architecture design, integration alignment, and cross-squad coordination for payment solution evolution.
- **Team delivery**: Implementation across engineering squads, UX, operations, and banking infrastructure stakeholders.

---

## 3. `bcnmarket / bonusconsum` — Municipal E-Commerce & Consumption Stimulus Platform

- **Company / Context**: Tiendeo.com & Barcelona City Council (Ajuntament de Barcelona)
- **Reference**: [Ajuntament de Barcelona Press Release](https://ajuntament.barcelona.cat/premsa/2021/10/04/barcelona-llanca-280-000-bonus-consum-per-potenciar-el-consum-local-a-traves-de-bcnmarket-barcelona/)
- **Role**: Senior Web Product Manager & Technical Lead
- **Domain**: High-Scale Digital Platforms, E-Commerce, Public Sector

### Context & Problem
During economic recovery initiatives, the Barcelona City Council required a scalable marketplace and digital voucher platform (*Bonus Consum*) to distribute subsidized shopping vouchers directly to citizens to spend in local brick-and-mortar retail shops.

### Solution & Architecture
- Led the end-to-end product delivery from conceptual design to city-wide launch within a strict 1-year timeline.
- Designed a scalable, cloud-based platform architecture capable of withstanding extreme traffic surges when voucher releases went live to hundreds of thousands of concurrent citizens.
- Integrated barcode/QR redemption mechanisms, merchant validation backoffices, and real-time transaction reconciliation.

### Tech Stack
`Cloud Platforms (GCP / AWS)`, `High-Availability Architecture`, `Python / Flask`, `Microservices`, `REST APIs`, `QR / Barcode Redemption`, `BPMN`.

### Key Outcomes & Impact
- Processed **500,000+ consumer transactions within 3 months** during peak municipal consumption campaigns.
- Maintained high availability with no reported downtime during voucher release windows; platform monitoring showed sub-second response times under peak load.
- Economic impact documented by the [Barcelona City Council press release](https://ajuntament.barcelona.cat/premsa/2021/10/04/barcelona-llanca-280-000-bonus-consum-per-potenciar-el-consum-local-a-traves-de-bcnmarket-barcelona/) (280,000 vouchers distributed to stimulate local commerce).

### Individual Contribution
- **Owned**: End-to-end product delivery, scalable cloud architecture design, and cross-functional coordination from concept to city-wide launch.
- **Team delivery**: Engineering implementation, merchant onboarding, and municipal stakeholder alignment.

---

## 4. `google-api-support` — Open-Source Python Library for Google Workspace Automation

- **Repository**: [github.com/vperezb/google-api-support](https://github.com/vperezb/google-api-support)
- **Distribution**: PyPI (`pip install google-api-support`)
- **Primary Domain**: API Integration, Automation, Developer Tooling
- **Status**: Production / Open Source

### Context & Problem
Interacting with official Google Workspace APIs (Sheets, Slides, Drive, Cloud Storage) using raw client libraries involves substantial boilerplate: managing credential flows, building batch update JSON payloads, and writing repetitive helper routines across distinct scripts.

### Solution & Architecture
Designed and published an open-source Python wrapper library abstracting Google API mechanics into idiomatic Python methods with native `pandas` DataFrame integration:
- **Google Sheets Wrapper**: Bidirectional sync (`DataFrame` to sheet, sheet to `DataFrame`), dynamic spreadsheet creation, tab manipulation.
- **Google Slides Engine**: Programmatic presentation generation, template text replacement, slide note extraction, and batch shape/image transformation.
- **Google Drive Management**: Hierarchical folder traversal (by path or ID) and automated file copy/move/upload/download routines.
- **Cloud Storage**: File upload routines returning signed public/private asset URLs.
- **Authentication**: Streamlined Service Account credentials handling (`GOOGLE_APPLICATION_CREDENTIALS` & OAuth2 flows).

### Tech Stack
`Python 3.8+`, `pandas`, `google-api-python-client`, `google-auth`, `oauth2client`, `httplib2`, `PyPI`.

### Key Outcomes & Impact
- Published on PyPI with open community adoption, saving engineering teams hundreds of hours of repetitive boilerplate code.

---

## 5. `libripolis.com` & `bibliodetect` — Book Lending Platform & AI Vision Recognition

- **Web Platform**: [libripolis.com](https://es.libripolis.com/)
- **Core AI Package**: [github.com/vperezb/bibliodetect](https://github.com/vperezb/bibliodetect)
- **Primary Domain**: Community Platforms, Computer Vision, Deep Learning & Multilingual OCR

### Context & Problem
Physical book sharing between friends and communities is plagued by forgotten loans, lost copies, and tedious manual catalog entry of book titles and authors.

### Solution & Architecture
- **Platform Layer (`libripolis.com`)**: Web application enabling users to track book collections, manage lending circles, and log borrow/return transactions seamlessly.
- **AI Vision Engine (`bibliodetect`)**: Decoupled deep learning Python package that extracts titles and authors directly from bookshelf photos:
  - **YOLOv8 (Ultralytics)** detects individual book boundaries within cluttered visual environments.
  - **OpenCV** extracts and standardizes cropped book spine regions.
  - **EasyOCR (PyTorch)** performs multilingual OCR (English, Spanish, French, etc.) to transcribe spine text into clean, structured data payloads.

### Tech Stack
`Python 3.10+`, `YOLOv8 (Ultralytics)`, `PyTorch`, `EasyOCR`, `OpenCV`, `Web App Development`, `Cursor / Copilot`.

### Key Outcomes & Impact
- Replaced manual 1-by-1 book typing with single-shot image cataloging, enabling rapid digital onboarding of physical libraries.

---

## 6. `aws-ip-change-tracker` — High-Reliability Event-Driven Cloud Network Sync

- **Repository**: [github.com/vperezb/aws-ip-change-tracker](https://github.com/vperezb/aws-ip-change-tracker)
- **Primary Domain**: Cloud Infrastructure, Event-Driven Architectures, Networking & Data Pipelines

### Context & Problem
AWS continuously modifies global IP address ranges across services (EC2, CloudFront, S3, Route53). Organizations require an accurate, immutable audit log of network prefix additions and removals without continuous API polling.

### Solution & Architecture
Built a dual-mode hybrid ingestion pipeline combining push and pull strategies:
1. **Real-time Reactive Ingestion (Push)**: AWS SNS topic subscriber (`AmazonIpSpaceChanged`) triggering an AWS Lambda function immediately upon prefix changes.
2. **Scheduled Audit Sweep (Pull)**: EventBridge rule running every 48 hours to perform a full global set difference, preventing drift or data loss from transient cloud provider hiccups.
3. **State Verification & Efficiency**: Evaluates AWS `syncToken` before write operations to prevent duplicate compute spend.
4. **Optimized Persistence**: Supabase (PostgreSQL) using native Postgres `CIDR` data types with GiST indexing (`inet_ops`) for instantaneous IP-in-range queries. Changes are committed atomically.

### Tech Stack
`Python`, `AWS Lambda`, `AWS SNS`, `AWS EventBridge`, `Supabase (PostgreSQL)`, `Postgres CIDR & GiST indexing`, `SQL`.

---

## 7. `Tiendeo Mobile App` Lifecycle Overhaul

- **Platform**: [Tiendeo Mobile App (iOS & Android)](https://play.google.com/store/apps/details?id=com.geomobile.tiendeo&hl=ca)
- **Role**: Junior Product Manager — Mobile APPs (1y 8mo)
- **Domain**: Native Mobile Apps, Geofencing, User Engagement

### Context & Problem
Tiendeo's flagship mobile application needed a complete architectural and UX overhaul to support modern geofenced promotional alerts, improved catalog reading experiences, and higher store ratings.

### Solution & Architecture
- Managed the end-to-end app rebuild from initial scoping through agile sprints to production deployment on Google Play and Apple App Store.
- Implemented **Firebase Cloud Messaging**, **Geofencing**, and **DeepLink** routing for localized push alerts when users approached relevant retail partner stores.
- Established rigorous user feedback collection mechanisms and continuous release triage.

### Key Outcomes & Impact
- Maintained a sustained **4.5-star user rating** across both iOS and Android stores post-launch (product served Tiendeo's global user base).

### Individual Contribution
- **Owned**: Product lifecycle, sprint planning, user story definition, release triage, and feedback loops.
- **Team delivery**: Native iOS/Android engineering, UX design, and Firebase/geofencing implementation.

---

## 8. Technical Writing & Community Knowledge Sharing

- **Medium**: [medium.com/@victor.perez.berruezo](https://medium.com/@victor.perez.berruezo) (Tiendeo Tech contributor)
- **Stack Overflow**: [stackoverflow.com/users/6109224/vperezb](https://stackoverflow.com/users/6109224/vperezb)
- **Focus Areas**:
  - Practical Python data pipelines (SQL to `pandas` DataFrame conversion).
  - AWS S3 bucket interaction and automation patterns.
  - Google Slides API automation for dynamic corporate presentation decks.
  - Developer productivity: SSH configuration, Jupyter with TensorFlow/Keras, QR code tracking systems.
