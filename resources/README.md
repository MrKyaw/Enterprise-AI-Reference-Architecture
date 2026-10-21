# Architect Career Competency Framework & Resources

**Last updated:** 2026-10-21

This page consolidates **all architect competencies, knowledge areas, hands-on skills, and learning resources** (URLs, YouTube, books, courses, tools) into a single reference. It accompanies the [Enterprise AI Reference Architecture](../README.md) repository and is designed to help architects at every level identify gaps and find the right learning material.

---

## 📋 Table of Contents

1. [Major Architect Roles & Competencies](#major-architect-roles--competencies)
2. [Core Knowledge Every Architect Should Have](#core-knowledge-every-architect-should-have)
3. [Hands-On Proficiency](#hands-on-proficiency)
4. [AI/ML Architect Specialization](#aiml-architect-specialization)
5. [Architecture Artifacts](#architecture-artifacts)
6. [Seniority Expectations](#seniority-expectations)
7. [Learning Resources (URLs, YouTube, Books, Courses)](#learning-resources)
8. [Tools & Technologies by Domain](#tools--technologies-by-domain)

---

## 1. Major Architect Roles & Competencies

<|end|> Architect Role | Essential Knowledge | Hands-On Skills |
|---|---|---|
| **Enterprise Architect** | Business capabilities, enterprise strategy, application portfolios, governance, TOGAF, architecture roadmaps | Capability mapping, ArchiMate, application rationalization, reference architectures |
| **Solution Architect** | End-to-end systems, integrations, APIs, scalability, reliability, cost | Design and build reference solutions, REST/gRPC APIs, microservices, cloud deployments |
| **Software Architect** | Design patterns, DDD, clean architecture, concurrency, distributed systems | Python, Java, C#, TypeScript, system refactoring, testing, performance profiling |
| **Cloud Architect** | AWS/Azure/GCP, networking, IAM, high availability, disaster recovery, FinOps | Terraform, Kubernetes, serverless, VPC/VNet, CI/CD, monitoring |
| **Data Architect** | Data modeling, warehouses, lakehouses, data governance, batch and streaming | SQL, PySpark, Kafka, Delta Lake, Databricks, ETL/ELT |
| **AI/ML Architect** | ML algorithms, model lifecycle, deep learning, evaluation, responsible AI | PyTorch, scikit-learn, MLflow, model serving, GPU optimization |
| **GenAI / Agentic AI Architect** | LLMs, RAG, agents, MCP, tool orchestration, evaluation, guardrails | LangGraph, LangChain, LlamaIndex, vector databases, FastAPI, agent deployment |
| **Security Architect** | Zero Trust, threat modeling, IAM, encryption, regulatory compliance | OAuth2/OIDC, Key Vault, KMS, SAST/DAST, security testing, policy-as-code |
| **Platform Architect** | Developer platforms, infrastructure abstraction, SRE, multi-tenancy | Kubernetes, GitOps, Terraform, observability, platform APIs |
| **Integration Architect** | Event-driven architecture, API management, enterprise integration patterns | Kafka, message queues, API gateways, schema registries, integration testing |
| **Infrastructure / Network Architect** | Networking, compute, storage, DNS, routing, resilience | Linux, networking diagnostics, IaC, load balancing, infrastructure automation |
| **Technical / Systems Architect** | Cross-system design, requirements engineering, hardware/software integration | Prototyping, performance testing, interface contracts, system integration |

### Key Distinction
The difference between architect roles is primarily the **scope of responsibility** and **depth of specialization**. An Enterprise Architect owns portfolio-level decisions; a Solution Architect owns a specific solution end-to-end; a Software Architect owns code-level structure and patterns.

---

## 2. Core Knowledge Every Architect Should Have

### System Design & Architecture
- Modular monoliths, microservices, distributed systems
- Synchronous vs. asynchronous communication
- Event-driven design, CAP trade-offs, consistency
- Caching, fault tolerance, domain-driven design (DDD)

### Software Engineering Fundamentals
- Algorithms, data structures, API design
- Concurrency, database transactions
- Secure coding, design patterns
- Unit/integration testing, code review

### Cloud, Infrastructure & Operations
- Networking, containers, Kubernetes
- CI/CD, infrastructure as code (IaC)
- Deployment strategies, disaster recovery
- Observability, SLOs, cost optimization (FinOps)

### Data & Integration
- Relational and NoSQL databases, schema design
- Streaming, data pipelines
- API contracts, event schemas, lineage
- Data quality and governance

### Security & Responsible Technology
- Threat modeling, least privilege
- Identity management, encryption, privacy
- Compliance, supply-chain security, risk management

### Business & Leadership
- Requirements discovery, stakeholder communication
- Architecture Decision Records (ADRs)
- Technical roadmaps, cost-benefit analysis
- Mentoring, delivery governance

---

## 3. Hands-On Proficiency

An architect does not need to be the strongest programmer in every technology. However, they should have sufficient implementation experience to distinguish an elegant diagram from a system that can actually work.

| Capability | Expected Hands-On Evidence |
|---|---|
| **Coding** | Implement a working service, review complex code, debug failures |
| **API Architecture** | Build REST/gRPC endpoints with authentication, validation, error handling |
| **Databases** | Design schemas, write complex SQL, tune queries, manage transactions |
| **Distributed Systems** | Implement retries, idempotency, queues, caching, and failure recovery |
| **Cloud Deployment** | Deploy a working application using containers and cloud services |
| **Infrastructure** | Create reproducible environments with Terraform or equivalent IaC |
| **Security** | Implement authentication, authorization, secrets management, audit logs |
| **Observability** | Instrument metrics, logs, traces, dashboards, and alerts |
| **Performance** | Benchmark latency, throughput, memory, cost, and scalability |
| **Architecture Documentation** | Produce C4 diagrams, ADRs, sequence diagrams, threat models |
| **Delivery** | Design CI/CD pipelines, test strategies, rollback and release procedures |

---

## 4. AI/ML Architect Specialization

For AI Solution Architects, Principal AI Architects, and Agentic AI Architects, the following additional knowledge becomes critical:

| Domain | Hands-On Requirements |
|---|---|
| **Classical ML** | Feature engineering, supervised/unsupervised learning, cross-validation, leakage prevention |
| **Deep Learning** | PyTorch, CNNs, Transformers, transfer learning, fine-tuning |
| **Foundation Models** | Tokenization, attention, pretraining concepts, LoRA/QLoRA, distillation |
| **Self-Supervised Learning** | Contrastive learning, masked modeling, DINO, JEPA |
| **Multimodal AI** | Vision-language models, multimodal embeddings, fusion strategies |
| **RAG** | Chunking, embeddings, hybrid retrieval, reranking, grounded evaluation |
| **Agentic AI** | Planning, tool calling, MCP, state management, multi-agent orchestration |
| **AI Evaluation** | Precision/recall, F1, calibration, retrieval metrics, LLM evaluations |
| **AI Security** | Prompt injection defense, tool permissions, data leakage prevention |
| **MLOps / LLMOps** | Model registry, experiment tracking, deployment, monitoring, drift |
| **AI Economics** | Token costs, GPU utilization, throughput, latency, model routing |
| **AI Governance** | Human oversight, auditability, model risk management, responsible AI |

> **Note:** For research-heavy positions (e.g., Applied Scientist II), the expectation goes deeper into independent experimental design, novel modeling methods, scientific validation, and publication-quality research — distinct from a conventional Solution Architect role.

---

## 5. Architecture Artifacts

Every senior architect should be able to produce and maintain these artifacts:

| Artifact | Purpose |
|---|---|
| **ADR (Architecture Decision Record)** | Explains the decision, alternatives, and trade-offs |
| **C4 Architecture Diagrams** | Context, containers, components, and code views |
| **Sequence & Data-Flow Diagrams** | Shows runtime interactions and information movement |
| **Threat Models** | Documents trust boundaries, attack paths, and mitigations |
| **Non-Functional Requirements (NFRs)** | Defines latency, availability, scalability, recovery, and security targets |
| **Performance & Cost Benchmarks** | Provides evidence that the architecture meets its targets |
| **Technical Roadmap** | Links current-state architecture to future-state capabilities |

---

## 6. Seniority Expectations

| Level | Main Responsibility | Typical Evidence |
|---|---|---|
| **Senior Engineer** | Implements complex components | Production code, tests, troubleshooting |
| **Technical Lead** | Leads a team's implementation | Code reviews, design decisions, mentoring |
| **Solution Architect** | Owns a solution end-to-end | Architecture, integrations, NFRs, deployment |
| **Lead / Principal Architect** | Owns architecture across multiple systems | Standards, reusable platforms, strategic trade-offs |
| **Enterprise Architect** | Aligns technology across the organization | Capability roadmaps, governance, portfolio decisions |
| **Chief / Distinguished Architect** | Sets long-term technology direction | Organization-wide architecture strategy and influence |

> **Note:** Titles vary considerably by company. A Principal Engineer at a major technology company may have greater architectural scope than an Enterprise Architect in a smaller organization.

---

## 7. Learning Resources

### 📚 Books

#### System Design & Architecture
- [Designing Data-Intensive Applications](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/) — Martin Kleppmann (O'Reilly)
- [Building Microservices](https://www.oreilly.com/library/view/building-microservices-2nd/9781492034018/) — Sam Newman (O'Reilly)
- [Software Architecture: The Hard Parts](https://www.oreilly.com/library/view/software-architecture-the/9781492086888/) — Neal Ford, Mark Richards, Pramod Sadalage, Zhamak Dehghani
- [Fundamentals of Software Architecture](https://www.oreilly.com/library/view/fundamentals-of-software/9781492043447/) — Mark Richards, Neal Ford
- [Domain-Driven Design](https://www.domainlanguage.com/ddd/) — Eric Evans
- [Clean Architecture](https://www.oreilly.com/library/view/clean-architecture-a/9780134494344/) — Robert C. Martin

#### Cloud & Infrastructure
- [Cloud Native Patterns](https://www.manning.com/books/cloud-native-patterns) — Cornelia Davis (Manning)
- [Kubernetes Up & Running](https://www.oreilly.com/library/view/kubernetes-up-and/9781492046523/) — Brendan Burns, Joe Beda, Kelsey Hightower
- [Terraform: Up & Running](https://www.terraformupandrunning.com/) — Yevgeniy Brikman
- [Site Reliability Engineering](https://sre.google/sre-book/table-of-contents/) — Google (Free online)

#### AI/ML & GenAI
- [Deep Learning](https://www.deeplearningbook.org/) — Ian Goodfellow, Yoshua Bengio, Aaron Courville (Free online)
- [Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/) — Aurélien Géron
- [Building LLMs for Production](https://www.oreilly.com/library/view/building-llms-for/9781098150952/) — Louis-François Bouchard, Louie Peters
- [Generative AI with LangChain](https://www.packtpub.com/product/generative-ai-with-langchain/9781835083468) — Ben Auffarth
- [Designing Machine Learning Systems](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) — Chip Huyen

#### Security
- [Threat Modeling: Designing for Security](https://www.oreilly.com/library/view/threat-modeling-designing/9781118809808/) — Adam Shostack
- [Zero Trust Networks](https://www.oreilly.com/library/view/zero-trust-networks/9781492031673/) — Evan Gilman, Doug Barth

#### Enterprise Architecture
- [TOGAF Standard](https://www.opengroup.org/togaf) — The Open Group
- [Enterprise Architecture as Strategy](https://hbr.org/product/enterprise-architecture-as-strategy/8588-HBK-ENG) — Jeanne W. Ross, Peter Weill, David C. Robertson
- [The Open Group Architecture Framework (TOGAF) 10](https://www.opengroup.org/togaf)

### 🎬 YouTube Channels & Playlists

#### System Design & Software Architecture
- [ByteByteGo](https://www.youtube.com/@ByteByteGo) — System design interviews, architecture patterns
- [ArjanCodes](https://www.youtube.com/@ArjanCodes) — Software architecture, Python, clean code
- [Fireship](https://www.youtube.com/@Fireship) — Quick tech explainers, architecture overviews
- [Engineering with Utsav](https://www.youtube.com/@EngineeringwithUtsav) — System design deep dives
- [Hussein Nasser](https://www.youtube.com/@HusseinNasser) — Backend engineering, networking, databases
- [Gaurav Sen](https://www.youtube.com/@gkcs) — System design, algorithms
- [CodeKarle](https://www.youtube.com/@CodeKarle) — System design interviews

#### AI/ML & GenAI
- [Andrej Karpathy](https://www.youtube.com/@AndrejKarpathy) — Deep learning, LLMs, neural networks
- [3Blue1Brown](https://www.youtube.com/@3blue1brown) — Neural networks, linear algebra, calculus (visual)
- [Yannic Kilcher](https://www.youtube.com/@YannicKilcher) — ML paper reviews, research
- [StatQuest with Josh Starmer](https://www.youtube.com/@statquest) — Statistics, ML concepts
- [AI Explained](https://www.youtube.com/@AIExplained) — LLMs, AI safety, evaluations
- [Two Minute Papers](https://www.youtube.com/@TwoMinutePapers) — Latest AI research summaries
- [LangChain](https://www.youtube.com/@LangChain) — RAG, agents, LangGraph tutorials
- [LlamaIndex](https://www.youtube.com/@LlamaIndex) — RAG, data frameworks for LLMs
- [DeepLearning.AI](https://www.youtube.com/@DeepLearningAI) — Andrew Ng's courses, short courses

#### Cloud & Infrastructure
- [TechWorld with Nana](https://www.youtube.com/@TechWorldwithNana) — DevOps, Kubernetes, Docker
- [That DevOps Guy](https://www.youtube.com/@MarcelDempers) — Kubernetes, cloud native
- [Cloud Guru](https://www.youtube.com/@ACloudGuru) — Cloud certifications, AWS/Azure/GCP
- [FreeCodeCamp](https://www.youtube.com/@freecodecamp) — Full courses on cloud, DevOps, programming

#### Security
- [LiveOverflow](https://www.youtube.com/@LiveOverflow) — Security, CTF, exploitation
- [John Hammond](https://www.youtube.com/@_JohnHammond) — Cybersecurity, malware analysis
- [NetworkChuck](https://www.youtube.com/@NetworkChuck) — Networking, security basics

### 🌐 Online Courses & Platforms

| Platform | Best For | Link |
|---|---|---|
| **Coursera** | University-level ML, cloud, architecture | https://www.coursera.org |
| **edX** | MIT/Stanford courses | https://www.edx.org |
| **Udacity** | Nanodegrees (AI, cloud, autonomous systems) | https://www.udacity.com |
| **Fast.ai** | Practical deep learning | https://www.fast.ai |
| **DeepLearning.AI** | Short courses on LLMs, RAG, agents | https://www.deeplearning.ai |
| **Pluralsight** | Cloud, DevOps, architecture paths | https://www.pluralsight.com |
| **A Cloud Guru** | AWS/Azure/GCP certifications | https://acloudguru.com |
| **KodeKloud** | Kubernetes, Docker, Terraform | https://kodekloud.com |
| **Exponent** | System design interviews | https://www.tryexponent.com |
| **ByteByteGo** | System design newsletter/courses | https://bytebytego.com |

### 📖 Key Online Resources

| Resource | Description | URL |
|---|---|---|
| **The System Design Primer** | Comprehensive system design study guide | https://github.com/donnemartin/system-design-primer |
| **AWS Architecture Center** | Reference architectures for AWS | https://aws.amazon.com/architecture/ |
| **Azure Architecture Center** | Reference architectures for Azure | https://learn.microsoft.com/en-us/azure/architecture/ |
| **GCP Architecture Framework** | Reference architectures for GCP | https://cloud.google.com/architecture |
| **CNCF Landscape** | Cloud native technology landscape | https://landscape.cncf.io/ |
| **OWASP Top 10** | Security vulnerabilities | https://owasp.org/www-project-top-ten/ |
| **The Open Group Architecture Framework** | TOGAF | https://www.opengroup.org/togaf |
| **ArchiMate Specification** | Enterprise architecture modeling | https://www.opengroup.org/archimate |
| **C4 Model** | Architecture diagramming | https://c4model.com/ |
| **Martin Fowler's Architecture Guide** | Architecture patterns and refactoring | https://martinfowler.com/architecture/ |
| **High Scalability** | Real-world architecture case studies | http://highscalability.com/ |
| **InfoQ** | Architecture and engineering articles | https://www.infoq.com/architecture-design/ |

---

## 8. Tools & Technologies by Domain

### System Design & Architecture
- **Diagrams:** C4 Model, Mermaid, PlantUML, Draw.io, Lucidchart, Excalidraw
- **Documentation:** Markdown, ADRs, Notion, Confluence, GitBook
- **Modeling:** ArchiMate, UML, TOGAF

### Software Development
- **Languages:** Python, Java, C#, TypeScript, Go, Rust
- **Frameworks:** FastAPI, Spring Boot, .NET, React, Angular, Node.js
- **Testing:** pytest, JUnit, Jest, Cypress, Playwright

### Cloud & Infrastructure
- **IaC:** Terraform, Pulumi, CloudFormation, Bicep
- **Containers:** Docker, Kubernetes, Helm, Kustomize
- **CI/CD:** GitHub Actions, GitLab CI, Jenkins, ArgoCD, Flux
- **Monitoring:** Prometheus, Grafana, Datadog, New Relic, ELK Stack

### Data Engineering
- **Databases:** PostgreSQL, MySQL, MongoDB, Redis, Cassandra, DynamoDB
- **Data Platforms:** Snowflake, Databricks, BigQuery, Redshift, Synapse
- **Streaming:** Kafka, RabbitMQ, Pulsar, Kinesis, Event Hubs
- **Processing:** Spark, Flink, Airflow, dbt, Prefect

### AI/ML & GenAI
- **ML Frameworks:** PyTorch, TensorFlow, scikit-learn, XGBoost
- **LLM Frameworks:** LangChain, LangGraph, LlamaIndex, Haystack
- **Vector Databases:** Pinecone, Weaviate, Qdrant, Milvus, pgvector
- **Model Serving:** vLLM, TGI, TorchServe, TensorFlow Serving, Triton
- **MLOps:** MLflow, Weights & Biases, Kubeflow, SageMaker
- **Evaluation:** RAGAS, TruLens, DeepEval, Promptfoo

### Security
- **Identity:** OAuth2/OIDC, Keycloak, Auth0, Azure AD
- **Secrets:** HashiCorp Vault, AWS Secrets Manager, Azure Key Vault
- **Scanning:** Snyk, SonarQube, Trivy, OWASP ZAP
- **Policy-as-Code:** Open Policy Agent (OPA), Kyverno, Sentinel

### Observability
- **Metrics:** Prometheus, Grafana, Datadog
- **Logs:** ELK Stack, Loki, Splunk
- **Traces:** Jaeger, Zipkin, OpenTelemetry, Tempo
- **APM:** New Relic, Datadog, Dynatrace, AppDynamics

---

## 📝 How to Use This Framework

1. **Self-Assessment:** Rate yourself on each competency area (1-5 scale)
2. **Identify Gaps:** Focus on areas where you're below level 3 (proficient)
3. **Choose Resources:** Use the links above to find targeted learning material
4. **Hands-On Practice:** Build something from each gap area
5. **Document:** Create ADRs, C4 diagrams, and threat models as evidence
6. **Review:** Re-assess quarterly as you progress

---

*This framework is part of the [Enterprise AI Reference Architecture](../README.md) repository. Contributions and updates welcome.*