# ☁️ FULL INFRASTRUCTURE ACTIVE MATRIX (Decathlon)

> **INSTRUCTIONS POUR L'AGENT :**
> 1. Référentiel complet des exigences INFRASTRUCTURE SIG.
> 2. Chaque point doit être validé selon le Step BMAD indiqué.
> 3. En cas de non-conformité, l'agent doit lever une alerte ou proposer une remédiation.

---

### [#1-CIM000-STMICP-75b97ece] I use scripts to manage infrastructure changes (ideally Python)
- **Level:** Level 1 | **Topic:** Configuration / Infra Management
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
Your infrastructure is provisioned by a tool that is not terraform (python script and associated libraries or equivalent).
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-CIM0-IUGAASCR-9aaa0236] I use Github as a source code repository for my infra
- **Level:** Level 1 | **Topic:** Configuration / Infra Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What is expected ?
The source code is hosted in github repository. This github repository also contains the data that, coupled with the tool source code, represents the source of truth.The source code is hosted in github repository. This github repository also contains the data that, coupled with the tool source code, represents the source of truth.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-CIM000-AICTIT-2b1a6a3a] I automate Server/VM changes through a validated Configuration Tool (Ansible or Puppet) and/or Infra changes through a validated IaC tool (Terraform (Enterprise or CPE Github Actions workflows))
- **Level:** Level 2 | **Topic:** Configuration / Infra Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What is expected ?
All infrastructure components are provisioned by Terraform using CPE provided standard model/provider. The terraform runs are performed by one of the validated tools, i.e. Terraform Enterprise or Github Actions. All the instances of your infrastructure are managed by a govtech validated configuration management tool (Puppet). All the changes go through a validation process (Pull Request).
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-CIM0-IUGAASCR-41f5726c] I use Github as a source code repository for my infra and changes go through a validation process (Pull request)
- **Level:** Level 2 | **Topic:** Configuration / Infra Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What is expected ?
The infrastructure code is stored in a Github repository. All modifications to this code must pass through a validation process (Pull Request) before being merged and deployed.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-CIM0-IFTFAGIB-d73ac3d8] I follow the FinOPS and Green IT best practices provided by CPE
- **Level:** Level 2 | **Topic:** Configuration / Infra Management
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
Your team actively applies the FinOps and Green IT best practices and recommendations provided by CPE to optimize costs and reduce environmental impact.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-CIM0-AICTAGVP] I automate Infra changes through a govtech validated platform offer (3S Stack, CloudKraft, Packaged offers from INIX, SAPTech, China, India....)

- **Level:** Level 3 | **Topic:** Configuration / Infra Management
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
Automate Infra changes through a govtech validated platform offer (Stack of the CPE unit, Packaged offers from INIX, China, India, Member, B&Rf....) (OK)

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-CIM0-IHFTIIWA-73251758] I have FinOps/GreenOPS tracking in infrastructure with a monthly follow up and I have at least one GreenIT KPI
- **Level:** Level 3 | **Topic:** Configuration / Infra Management
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
FinOps and GreenOps tracking, including at least one Green IT KPI, are in place for the infrastructure, with regular monthly follow-ups to monitor and report performance.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-SM00-ISMMSIAP] My source code is free of machine-to-machine secrets (YES)
or already compliant with a higher Secrets Management level (NA)
- **Level:** Level 1 | **Topic:** Secrets Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What is expected ?
There is no secret in a public file (github protected repositories are considered public for all DKT users). Your machine to machine secrets are at least in a private file, outside of version control or in your CI configuration. No secret are hardcoded in your code.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-SM0000-ISMMSI-d1cae740] I store my machine-to-machine secrets in a specific secret management tool (like Vault, GCP or AWS Secret Manager) (YES)
or already compliant with a higher Secrets Management level (NA)
- **Level:** Level 2 | **Topic:** Secrets Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What is expected ?
There is no secret in your code and you removed the secrets from your application and/or CI. You retrieve them from a secret management tool using workload identity, connecting to Vault with token exchange (from github token, GCP SA, AWS role, etc.).
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-SM00-ISMMSIVE-6b825dc4] I store my machine-to-machine secrets in Vault Enterprise (YES)
- **Level:** Level 3 | **Topic:** Secrets Management
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected?
Your secrets are stored in Vault Enterprise. Secrets are injected as Kubernetes secrets, environment variables or temporary files using tools like Vault agent, the Vault or External Secrets operators or synced to cloud providers secret managers for serverless workloads. You can easily rotate your secrets by updating them in the Secret Engine, triggering a redeployment or an update of the workload that consume them.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-SM0000-ISMMSW-91a87c3d] I store my machine-to-machine secrets with K8S secrets or Cloud provider secret manager or github secrets or Vault and injected as infra init or env variable (OK)
I rotate my secret based on ISSP requirements (6 month in ISSP)
or higher Secrets Management level (NA)
- **Level:** Level 3 | **Topic:** Secrets Management
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
Your secrets are stored in a secret manager (Hashicorp Vault, ...). Secrets are injected into your infrastructure ( via init-container, injected as environment variable or temporary files via tools like external-secret or Vault agent... ). You can easily rotate your secrets by updating them in the Secret Engine and triggering a redeployment of the workload that consume them.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-SM00-MMSAIAKS-4f21987b] My M2M secrets are injected as Kubernetes secrets, environment variables or temporary files using tools like the Vault or External Secrets operators or synced to cloud providers secret managers for serverless workloads
- **Level:** Level 3 | **Topic:** Secrets Management
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected?
Your secrets are stored in Vault Enterprise. Secrets are injected as Kubernetes secrets, environment variables or temporary files using tools like Vault agent, the Vault or External Secrets operators or synced to cloud providers secret managers for serverless workloads. You can easily rotate your secrets by updating them in the Secret Engine, triggering a redeployment or an update of the workload that consume them."
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-SM00-IRMMSBOI-8db1a3e9] I rotate my M2M secrets based on ISSP requirements (180 days in ISSP) or better
- **Level:** Level 3 | **Topic:** Secrets Management
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** Your secrets are stored in Vault Enterprise. Secrets are injected as Kubernetes secrets environment variables or temporary files using tools like Vault agent.
The Vault or External Secrets operators or synced to cloud providers secret managers for serverless workloads. You can easily rotate your secrets by updating them in the Secret Engine
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-SM00-MSARA000-c99c6de0] My secrets are rotated automatically
- **Level:** Level 4 | **Topic:** Secrets Management
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
Your secrets are rotated automatically by the secret management tool (e.g., Hashicorp Vault, Cloud Secret Manager features) according to predefined security policies and rotation schedules (e.g., based on ISSP requirements or better). This rotation process is integrated with your workloads (e.g., via Vault Agent, External Secrets Operator, or Cloud-native features) to ensure seamless and zero-downtime updates of secrets used by applications and infrastructure.


- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-SM0000-MMSREF-35f523f5] Secrets retrieval is handled by the application and secrets are stored in memory (not in files, environment variables or Kubernetes secrets).
- **Level:** Level 5 | **Topic:** Secrets Management
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
Your application connects directly to the secret manager (via workload identity or vault token or equivalent way). Application supports hot updates of those secrets and can even trigger/request secret rotation if needed (short lived secrets to access database for instance)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-SM00-SRIHBTAA-c35b8267] My secrets are rotated automatically and short-lived. They are only pulled when needed from the secret manager and only cached for a short time (minutes)
- **Level:** Level 5 | **Topic:** Secrets Management
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
Application supports hot updates of those secrets and can even trigger/request secret rotation if needed (short lived secrets to access database for instance).
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-SM00-WPPAILUW-4739f2b2] When possible, passwordless authentication is leveraged, using Workload Identity with ou without Decathlon's Fedid (ex: MongoDB, CloudSQL)
- **Level:** Level 5 | **Topic:** Secrets Management
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
Credentials are no longer provided, a trust mechanism using workload identity and/or Decathlon Fedid is used to authenticate and authorize workloads
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-SM00-ISMMSIVE-7ebf69da] I store my machine-to-machine secrets in Vault Enterprise (YES)
or already compliant with a higher Secrets Management level (NA)
- **Level:** Level 4 | **Topic:** Secrets Management
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** Your secrets are rotated automatically by the secret management tool (e.g.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-SM0000-ISMMSI-d84857be] I store my machine-to-machine secrets in Vault Enterprise solution.(OK)
My secrets are only accessible in memory space
- **Level:** Level 4 | **Topic:** Secrets Management
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
Your application connects directly to the secret manager (via workload identity or vault token or equivalent way ) and pull secrets directly from there. The secrets are available as environment variable or mounted files in containers.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-HS0000-HIPCEN-3a76d78e] Hosted in referenced private cloud (YES)
or higher Hosting Solution level (NA)
- **Level:** Level 1 | **Topic:** Hosting Solution
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
Your application is hosted in the private cloud referenced by govtech, you must not have any application host in a physical server on your side. If you have any doubt, please reach the slack chan #sig-infra-support
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-HS0000-HIRPCG-949022f3] Hosted in referenced public cloud (GCP, AWS, Alicloud or Azure (China only)) under the DKT contract (YES)
or higher Hosting Solution level (NA)
- **Level:** Level 2 | **Topic:** Hosting Solution
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
Your application is hosted in the public cloud as GCP/AWS/AliCloud/Azure( china only) under the decathlon contract, the region you've chosen is a validated ( by CPE ) landing zone. Please refer to the tech radar for the list of clouders supported.  Please refer to the tech radar for the list of OS and middleware supported. If you have any doubt, please reach the slack chan #sig-infra-support
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-HS0000-HIRPCG-28937fb3] Hosted in a govtech validated platform offer (3S Stack, Cloudkraft, SAPTech, optionally packaged by INIX, Decatec, China, India, etc.) (YES)
- **Level:** Level 3 | **Topic:** Hosting Solution
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
Your application is hosted in the govtech validated platform such as 3S stack, Packaged offers from inix, China, India, Member, OCO, B&Rf, etc) , you must not host your applications in a standalone or managed account outside of these platforms. If you have any doubt, please reach the slack chan #sig-infra-support
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-HS00-TPIUIIAS-e981dedf] Hosted in a govtech validated platform offer (3S Stack, Cloudkraft, SAPTech, optionally packaged by INIX, Decatec, China, India, etc.) and in a supported version, complying with the release lifecycle (YES)
- **Level:** Level 4 | **Topic:** Hosting Solution
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What is expected ?
You are able to deploy your application on a frequently updated platform. This practice allows you to maintain support and required security level while taking advantage of the latest functionalities.  IE : I am on a supported version of the 3S stack and I upgrade my stack every quarter.
If you have any doubt, please reach the slack chan #sig-infra-support
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-CND0-MAIHOVMW] My app is hosted on virtual machines without autoscaling (YES)
 or higher cloud native level (NA)
- **Level:** Level 1 | **Topic:** Cloud Native Design
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
Your applications are hosted at least on a VM based on a middleware ( e.g. Tomcat, Weblogic (only Cube and Eone) ).  Please refer to the tech radar for the list of OS and middleware supported. If you have any doubt, please reach the slack chan #sig-infra-support
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-CND0-MAIHOVMW] My app is hosted on virtual machines with autoscaling activated (YES)
 or higher cloud native level (NA)
- **Level:** Level 2 | **Topic:** Cloud Native Design
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
Your applications are hosted at least on a VM based on a middleware ( e.g. Tomcat ) who supports horizontal autoscaling, meaning when the application needs more resources, the hosting mechanism can add one or more VM to absorb the charge.  Please refer to the tech radar for the list of OS and middleware supported. If you have any doubt, please reach the slack chan #sig-infra-support
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-CND0-MAIHOVMW-bf0acf39] My app is hosted on virtual machines with autoscalling activated using only golden images (OK)
 or higher cloud native level (NA)
- **Level:** Level 3 | **Topic:** Cloud Native Design
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What is expected ?
Your applications is hosted at least on a VM based on a middleware ( e.g. Tomcat ) who support the horizontal autoscaling, all the CD is done through golden images. Puppet and config management tooling are not deployed. that's mean when the application needs more resources, the hosting mechanism can add one or more VM to absorb the charge in very short delays.  Please refer to the tech radar for the list of OS and middleware supported. If you have any doubt, please reach the slack chan #sig-infra-support
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-CND0-MAIHOKOS] My app is hosted on K8S or serverless without autoscaling (YES)
- **Level:** Level 3 | **Topic:** Cloud Native Design
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
Your applications are hosted at least in GovTech validated K8S cluster ( e.g. GKE, EKS, AKS ) or serverless platform ( e.g.  CloudRun, CloudFunction, Lamda, etc).  Please refer to the tech radar for the list of containerisation and serverless technologies supported. If you have any doubt, please reach the slack chan #sig-infra-support
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-CND0-MAIHOKOS-c91600be] My app is hosted on K8S or serverless with autoscaling for most workloads (ex: HPA, VPA, KEDA, etc.) (YES)
- **Level:** Level 4 | **Topic:** Cloud Native Design
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
Your Kubernetes workloads are using autoscaling to adapt their size or number of instances to the incoming load. This helps managing spikes of incoming load and reduces greatly the overprovisionning of costly cloud resources.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-CND0-MAIHOSOK-8375cbf4] My app is hosted on Serverless or Kubernetes with workload autoscaling and smart autoscaling of nodes (Compute Classes, Karpenter, etc.)
- **Level:** Level 5 | **Topic:** Cloud Native Design
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
In addition to Kubernetes workload autoscaling, a smart node autoscaling (GKE compute classes or Karpenter) solution is in place to optimize the size and number of nodes
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-DM00-ISMODOAP] DEPLOYMENT

My database is manually installed in a server or VM. (Yes) or better automation (N/A)
- **Level:** Level 1 | **Topic:** Database Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** **Why ?**

Manual installation is often the starting point, but it increases variability between environments and makes recovery and scaling harder. This level exists mainly to acknowledge the baseline and to highlight why automation becomes important at higher levels.

**What ?**

A database instance is provisioned by hand (OS packages, configuration, users, storage, network rules) on a VM or server. The setup may not be fully reproducible.

**How ?**

- Document the installation steps (commands, versions, parameters, ports, firewall rules).
- Record where credentials and configuration live (vault, secrets manager, files, etc.).
- Ensure there is at least minimal operational ownership (who can rebuild it, where is the runbook).
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-DM00-BDIMBBSR-ea5f56eb] BACKUPS

My data is manually backuped by someone regularly (Yes) or better automation (N/A)
- **Level:** Level 1 | **Topic:** Database Management
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **Why ?**

Backups are the foundation of resilience. Manual backups are better than none, but they are error-prone (missed schedules, incomplete scope, frequently poorly protected (stored on the same server, not encrypted, not tested) and rarely tested for restoration capability.

**What ?**

A person triggers backups periodically (dump/snapshot/export) and stores them somewhere, likely in the same server, with limited guarantees on frequency, retention, integrity, or restorability.

**How ?**

- Define a minimum backup frequency (daily/weekly) and retention (e.g., 7/30/90 days).
- Store backups outside the database host whenever possible.
- Document a basic restore procedure (even if restore tests are not regular yet).
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-DM00-ISMODOAV] DEPLOYMENT

My Database services are installed in servers or VMs with scripts-based automations (Bash/Python, cron, etc.) (Yes) or better (N/A)
- **Level:** Level 2 | **Topic:** Database Management
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **Why ?**

Scripted setup increases repeatability and reduces reliance on tribal knowledge. It is a stepping stone toward Infrastructure as Code and platform-managed services.

**What ?**

Database provisioning and configuration are automated via scripts (install packages, configure parameters, create users/schemas, open ports, attach disks).

**How ?**

- Store scripts in version control.
- Make scripts idempotent where possible (safe to run multiple times).
- Parameterize environment-specific values (ports, instance size, storage path).
- Add a simple “create + verify” routine (health check, connection test).
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-DM00-BDAABATB-6cef12c8] BACKUPS

My databases are automatically backuped and the backups are stored outside the database server.(Yes)
- **Level:** Level 2 | **Topic:** Database Management
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** **Why ?**

Automation reduces missed backups and ensures backups survive host loss. External storage is essential for real disaster recovery.

**What ?**

Scheduled, automated backups run without human intervention, and backup artifacts are stored on separate infrastructure (object storage, backup server, managed backup service).

**How ?**

- Use native DB backup tooling or cloud/managed backup features.
- Send backups to external storage with access controls and encryption.
- Track backup job success/failure (notifications/alerts).
- Define retention rules (rotation / lifecycle policies).

<sub>GreenIT</sub>

**Why ?**

Automated retention policies reduce unnecessary storage footprint and cost.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-DM00-MDAASRMT-7937f5a9] AVAILABILITY

My Database as a simple replication mechanism that I can isolate and redirect apps to in case of loss of my primary instance.
- **Level:** Level 2 | **Topic:** Database Management
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **Why ?**

Replication reduces downtime and data loss risk. Even manual failover is a major improvement over a single-instance database as it guarantees a near-zero RPO with a decent RTO.

**What ?**

A secondary replica exists (read replica or standby). In case of primary failure, the team can promote and redirect manually.

**How ?**

- Configure replication (streaming/log shipping/cluster replica, depending on DB).
- Document a failover runbook: detect → isolate primary → promote replica → update DNS/service config → verify app.
- Regularly verify replication lag and replica health. (can be delegated to Aiven)
- Practice at least one failover exercise per year (even if failover is not automated yet).
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DM00-ISMDOAMS] DEPLOYMENT

My Database services are deployed with Infrastructure as Code (Terraform, Ansible) including 3S or other govtech-compliant platforms (Yes)
- **Level:** Level 3 | **Topic:** Database Management
- **BMAD Step:** Step 05 - Testing
- **Constraint:** *Why ?**

Infrastructure as Code (IaC) brings auditability, repeatability, and safer change management through peer review. It also supports compliance constraints (traceability, standard patterns, security guardrails).

**What ?**

Database infrastructure (networking, compute/storage, IAM, security groups, managed DB resources) is defined as code and deployed via pipelines.

**How ?**

Using Govtech platforms (like 3S or Standard terraform modules) simplifies this,  otherwise:
- Use Terraform/Ansible (or equivalent) to create the database services (usually on Aiven) and dependencies (IAM, network peerings, etc.)
- Enforce reviews on IaC changes (pull requests).
- Separate environments (dev/staging/prod) with distinct states/workspaces.
- Include compliance-required controls (encryption, logging, network segmentation).

<sub>GreenIT</sub>

**Why ?**

IaC enables optimizations like shutting down non-production services outside working hours, saving both money and carbon footprint.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DM00-BDAABTBA-d7850203] BACKUPS

My databases are automatically backuped, the backups are stored outside the database server and I'm running regular restoration tests.
- **Level:** Level 3 | **Topic:** Database Management
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **Why ?**

A backup you never restore is only a hope. Restoration tests validate backup integrity, procedures, RTO assumptions, and team readiness.
Automation ensures consistent and auditable behavior, creating confidence in integrity of backups.

**What ?**

Automated backups + external storage + periodic restore drills (full restore or partial restore to a test environment).
Note : Replication & HA architectures do not exempt from mandatory backuping all data.

**How ?**

- Schedule restore drills (yearly/quarterly).
- Restore into an isolated environment and validate:
  - DB starts correctly
  - critical tables exist
  - sample queries succeed
  - application can connect (optional)
- Track restore time and gaps; improve the runbook.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DM00-ADRHAFST-3f8a59e3] AVAILABILITY

My database replicas have automatic Failover systems that provide HA
- **Level:** Level 3 | **Topic:** Database Management
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **Why ?**

Automatic failover reduces downtime and human error during incidents, and standardizes recovery behavior.

**What ?**

High availability is achieved with automatic detection and failover (managed DB multi-AZ, cluster managers, orchestrators).

**How ?**

- Prefer managed HA features where available.
- Define health checks and failover criteria.
- Ensure applications use a stable endpoint (cluster endpoint, proxy, VIP, DNS).
- Monitor failover events and test failover periodically.

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DM00-ISMDOAMS] DEPLOYMENT

In addition to Infra as code, the Schema of my Database services is manages with automated migration solutions (Flyway) included in my apps' CI/CD
- **Level:** Level 4 | **Topic:** Database Management
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **Why ?**

Schema drift is a common cause of outages. Versioned migrations provide controlled evolution, reviewability, and safer deployments.

**What ?**

Database schema changes are versioned, reviewed, and applied automatically through CI/CD using a migration tool (Flyway, see Tech Radar).

**How ?**

- Store migration scripts alongside application code.
- Run migrations in the pipeline with clear ordering/versioning.
- Leverage forward/backward compatibility when possible to decouple code and schema upgrades.
- Add checks : “migration applied”, “schema version is X”.
- Define rollback strategy (down migrations when safe, or forward-fix strategy, plus backups before risky changes).
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DM00-MDAABTBA-22c38a4e] BACKUPS

My databases are automatically backuped, the backups are stored outside the database server as immutable files (WORM), I'm running regular restoration tests and RTO/RPO are close to zero (PITR).
- **Level:** Level 4 | **Topic:** Database Management
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **Why ?**

This level targets strong resilience and security: immutability protects against ransomware and operator mistakes; PITR minimizes data loss; restore drills validate recovery objectives.

**What ?**

Backups include:
- immutable storage (WORM / object lock)
- regular restore tests
- PITR (point-in-time recovery) enabled
- defined and measured RPO/RTO targets (aiming close to zero when required)

**How ?**

- Enable PITR / continuous archiving (WAL/binlog, depending on DB engine).
- Store backups in object storage with immutability and retention lock.
- Encrypt backups and manage keys properly.
- Measure and report achieved RPO/RTO during restore tests.

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DM00-MDAAHAWA-1434631c] AVAILABILITY

My database allows cross-region failover architectures with automatic recovery.
- **Level:** Level 4 | **Topic:** Database Management
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **Why?**

Cross-region failover provides the highest level of disaster recovery, ensuring business continuity and minimal data loss even after a major regional outage. Automatic recovery dramatically minimizes the Recovery Time Objective (RTO) and reduces the potential for human error during a crisis.

**What?**

This involves a primary instance in one region and a synchronized, ready-to-take-over standby instance in a different geographical region. The system includes automated health checks and a coordinated failover mechanism that redirects application traffic to the standby in case of a complete failure of the primary region.

**How?**
- Set up and maintain a synchronous or asynchronous replication stream to a second, separate region.
- Implement automated, region-aware health checks that trigger the failover process.
- Configure global traffic management (e.g., DNS, load balancer) to automatically redirect traffic to the healthy region after failover.
- Continuously test the failover and failback procedures.
- Ensure the application layer can gracefully handle the cross-region connection latency and brief outage during the switch.

<sub>CRITICALITY NOTE</sub>

Not all application criticality tiers or Service Level Objectives (SLOs) require this level of resilience. This architecture is typically reserved for applications with the highest RTO and RPO requirements (e.g., Tier 1).

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-HS0000-HICCSO-ff858145] AVAILABILITY

My database allows active-active architectures with automatic recovery.
- **Level:** Level 5 | **Topic:** Database Management
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **Why?**

Active-active architectures provide ultimate resilience by allowing both regions to handle traffic simultaneously, eliminating downtime during regional failures. It also provides significant performance gains by distributing the read and write load globally, but introduces substantial complexity, especially around data consistency.

**What?**

Multiple active nodes or clusters across different regions accept traffic concurrently. The system requires advanced, automated mechanisms for recovery, load balancing, and critically, conflict resolution to ensure data consistency (e.g., multi-master replication, distributed SQL). This is often not feasible or has severe trade-offs with traditional relational databases like PostgreSQL.

**How?**
- Choose a data technology and architecture inherently compatible with multi-region active-active deployment (e.g., distributed databases, specialized multi-region clusters).
- Define strict consistency requirements (e.g., strong vs. eventual consistency) and acceptable failure modes.
- Implement global routing/load balancing to intelligently distribute traffic to the nearest healthy instance.
- Develop and validate the automatic conflict resolution logic and recovery mechanism.
- Continuously test complex failure scenarios (e.g., network partition, partial cluster failure) to ensure data integrity and automatic recovery.

<sub>CRITICALITY NOTE</sub>

This is the highest resilience level and should only be considered for the most critical Tier 0/1 applications whose SLO dictates near-zero downtime and high concurrent regional load. For most applications, Level 4 is sufficient.

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-SMFU-LSOSOOHN] Local storage on servers (YES)
or higher (NA)
- **Level:** Level 1 | **Topic:** Storage Management (for unstructured data)
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What is expected ?
Your VM/Container/K8S has at least a local storage, your files and other configuration are stored at least on this local storage.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-SMFU-SBFSOOHN] Server based file sharing (YES)
or higher  (NA)
- **Level:** Level 2 | **Topic:** Storage Management (for unstructured data)
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What is expected ?
Your VM/Container/K8S has at least a server based storage, your files and other configuration are stored at least on this file sharing storage.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-SMFU-TPBSOITS] Third party based software on IaaS to share files (YES)
or higher (NA)
- **Level:** Level 3 | **Topic:** Storage Management (for unstructured data)
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
Your VM/Container/K8S cluster/serverless has at least a govtech validated third party based file sharing system.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-SMFU-CPOSSCSW] Cloud Provider object storage (S3, cloud storage...) with lifecycle management enabled (YES)
or higher (NA)
- **Level:** Level 4 | **Topic:** Storage Management (for unstructured data)
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
Your VM/Container/K8S cluster/serverless has at least a govtech validated cloud provider object storage system such as S3, Cloud storage, Azure Cloud Storage, etc with a lifecycle management provided by cloud provider.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-SMFU-CPOSSCSW] Cloud Provider object storage (S3, cloud storage...) with enhanced security (WORM protection, multiregionnal...) and lifecycle management (YES)
- **Level:** Level 5 | **Topic:** Storage Management (for unstructured data)
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What is expected ?
Your VM/Container/K8S cluster/serverless has at least a govtech validated cloud provider object storage system such as S3, Cloud storage, Azure Cloud Storage, etc with a lifecycle management provided by cloud provider, and it has at least an enhanced security level such as WORM protection, multiregions configuration.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-R000-SDUSTAVB-c79162a8] Solution developed used services that are validated by infrastructure and architecture teams
- **Level:** Level 1 | **Topic:** Reproducibility
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected?
The solution must utilize services that have been pre-approved and validated by the infrastructure and architecture teams to ensure compliance with organizational standards and best practices (see Technical Desgin Review process)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-R000-POIIDACL-df845130] Part of infrastructure is defined as code, later referenced as IaC (Infrastructure as Code). 
- **Level:** Level 2 | **Topic:** Reproducibility
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** What is expected?
The infrastructure should be defined using code (terraform), enabling automated provisioning, management, and versioning of infrastructure resources.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-R000-IISIAVCS-1067483e] IaC is stored in a version control system (e.g. github repository)
- **Level:** Level 2 | **Topic:** Reproducibility
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What is expected?
The Infrastructure as Code (IaC) should be stored in a version control system such as GitHub to facilitate collaboration, versioning, and tracking of changes
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-R000-SOPIUTCC-983eaab0] S-MAX (optional) process is used to create changes in IaC thank to the help of dataops team.
- **Level:** Level 2 | **Topic:** Reproducibility
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What is expected ?
Changes to Infrastructure as Code (IaC) should be managed through the S-MAX process with assistance from the DataOps team, ensuring controlled and efficient updates.
S-Max - https://github.com/dktunited/dataops-terraform-infra-projects
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-R000-SUDCOTNW-109fa2cb] Services used doesnot contain operation team names (we are following product convention).
- **Level:** Level 2 | **Topic:** Reproducibility
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
Services should be named according to the product convention rather than including operation team names to maintain consistency and clarity in service identification.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-R000-PCASGAD0-77d48a70] Project code and support group are defined.
- **Level:** Level 2 | **Topic:** Reproducibility
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What is expected ?
The project code and associated support group must be clearly defined to ensure accountability and proper management of the project.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-R000-RIANUAMA-b2656eb0] Role IAM are not using any manually added custom policy.
- **Level:** Level 3 | **Topic:** Reproducibility
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
IAM roles should not include manually added custom policies, promoting the use of standardized and pre-approved policy sets for security and consistency.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-R000-AAPIIDAC-3b9d5812] All AI Product Infrastructure is defined as code, and using the Terraform modules provided by dataops team based on AI product strategy (dedicated role for the product).
- **Level:** Level 3 | **Topic:** Reproducibility
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
All AI product infrastructure should be defined using code, specifically leveraging Terraform modules provided by the DataOps team, aligned with the AI product strategy and dedicated roles.
https://dataplatform-access-management.dktapp.cloud/
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-R000-DAMPSHAL-4abcea22] Data and ML pipeline should have at least two environments (preproduction and production) which are exact copies of each other.
ML model exposition should have differents environments
- **Level:** Level 3 | **Topic:** Reproducibility
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What is expected ?
The data and ML pipelines must include at least two environments, preproduction and production, which are exact replicas to ensure consistent testing and deployment.
Machine Learning models should be deployed in multiple environments to ensure proper testing, staging, and production workflows.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-R000-AERTAAPS-7fa7677d] All environments related to a AI Product should have access to production data (data should be the same at any moment of time).
- **Level:** Level 3 | **Topic:** Reproducibility
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
All environments associated with an AI product must have access to production data, ensuring data consistency across environments at all times.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-R000-TRHPTOOP-c5dc25f2] Technical review has proposed time of ops people for creating quickly all ressources we need with dataops team.
- **Level:** Level 3 | **Topic:** Reproducibility
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
A technical review should allocate time for ops in order to collaborate with the DataOps team in swiftly creating all necessary resources.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-R000-MPMAIHOK-dff5b136] My product (ML API) is hosted on K8S or serverless.
- **Level:** Level 4 | **Topic:** Reproducibility
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What is expected ?
The Machine Learning API product should be hosted on Kubernetes (K8S) or a serverless platform, aligning with modern infrastructure practices.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-R000-PROTGRPI-313d52fe] Pull request on terraform git repo process is used to create changes in IaC. Team are autonomous.
- **Level:** Level 5 | **Topic:** Reproducibility
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What is expected ?
Changes to Infrastructure as Code (IaC) should be made through a pull request process in the Terraform Git repository, allowing teams to work autonomously while ensuring code review and version control.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-S000-PHPV0000-bf91045a] Place holder: please validate
- **Level:** Level 1 | **Topic:** Security
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-S000-DUIEEWKO-b1663ca7] Data used is encrypted (e.g. with KMS on s3).
- **Level:** Level 2 | **Topic:** Security
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
Data encryption involves using cryptographic techniques to secure data, such as encrypting data stored in S3 using Key Management Service (KMS).
### Why
To protect sensitive information, ensure data privacy, and comply with regulatory requirements.
### How
 Use AWS KMS to manage encryption keys and configure S3 bucket settings to enable server-side encryption with KMS. Regularly audit and review encryption settings to ensure compliance.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-S000-ASAMSIPB-e3fba747] As soon as managed solutions is provided by cloud provider, we donot use alternative (e.g. no cloud provider managed deployment)
- **Level:** Level 3 | **Topic:** Security
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ### What
When a managed solution is available from the cloud provider, it should be used instead of alternative, non-managed deployments.
### Why
Managed solutions offer built-in scalability, security, and maintenance, reducing operational overhead and risk.
### How
 Identify managed services provided by the cloud provider that fit project requirements. Replace non-managed deployments with these services, ensuring configuration aligns with best practices and project needs.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-S000-LVOSVOPI-290700ba] Latest version (or supported version) of Python is used.
- **Level:** Level 3 | **Topic:** Security
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
The project should use the latest or a currently supported version of Python.
### Why
To ensure compatibility, receive security updates, and leverage new features and improvements.
### How
Regularly check the Python status at Python status and upgrade the Python version used in the project. Implement version checks in CI/CD pipelines to enforce usage of supported versions.
Python status: https://devguide.python.org/versions/
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-S000-LVOPDAU0-57a78e4f] Latest versions of packages dependencies are used.
- **Level:** Level 3 | **Topic:** Security
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
Dependencies should be regularly updated to their latest versions.
### Why
To benefit from security patches, bug fixes, and feature enhancements.
### How
Use tools like pip-review or pip-upgrade to identify and upgrade outdated Python packages. Schedule regular maintenance windows to perform these upgrades and test for compatibility.

Upgrade python module used regularly
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-S000-EWYSCOST-8bd45f59] Estimate with you security champion or security team, the criticity of your project and list your project into EGERIE if it is relevant.
- **Level:** Level 3 | **Topic:** Security
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
Assess the criticality of the project with a security expert and register it in EGERIE if necessary.
### Why
To ensure proper security measures are in place based on project risk and criticality.
### How
Use the Tech Radar security checklist available here to evaluate security requirements and consult with the security team for assessment and registration.
Tech radar security checklist: https://docs.google.com/spreadsheets/d/1DBOodOlr1WVI1O0202mqcixMdvVg8_TFeulvckABHPg/edit?gid=0#gid=0
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-S000-CARRBTHS-f4943f71] Container are regulary re built to handle security issues.
- **Level:** Level 3 | **Topic:** Security
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
Containers should be periodically rebuilt to incorporate the latest security updates and patches.
### Why
To mitigate vulnerabilities and ensure containers remain secure.
### How
Automate the container rebuild process using CI/CD pipelines. Schedule regular rebuilds and deployments, integrating vulnerability scanning tools like Clair or Trivy to detect and address security issues.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-S000-DARRWLVO-66b0db6f] Dependencies are regularly rebuilt with latest versions of python modules.
- **Level:** Level 4 | **Topic:** Security
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
Dependencies should be regularly updated and rebuilt with the latest Python modules.
### Why
To ensure the application uses the most secure and efficient versions of dependencies.
### How
Automate dependency updates using tools like Dependabot. Schedule regular rebuilds and run tests to verify compatibility and functionality.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-S000-PHBDAANF-b7bd10a9] Pentest has been done (API audit needed for public exposition).
- **Level:** Level 4 | **Topic:** Security
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
A penetration test (pentest) should be conducted, especially for publicly exposed APIs, to identify and address security vulnerabilities.
### Why
To proactively find and fix security flaws, ensuring the API is secure from attacks.
### How
Engage a professional pentesting service or an internal security team to perform the audit. Review and address the findings, implementing necessary security measures and improvements.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-S000-IPIOSWAF-83bb3c21] If project is open sourced we are following security standards.
- **Level:** Level 5 | **Topic:** Security
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** ## What
When a managed solution is available from the cloud provider, it should be used instead of alternative, non-managed deployments.
### Why
Managed solutions offer built-in scalability, security, and maintenance, reducing operational overhead and risk.
### How
Identify managed services provided by the cloud provider that fit project requirements. Replace non-managed deployments with these services, ensuring configuration aligns with best practices and project needs.
Contact corentin.vasseur@decathlon.com
Standard: https://docs.google.com/document/d/1VeZOKAPHrN11Kv4XTrfkVs0BDo0p63po/edit
Useful links: https://github.com/mikeroyal/Open-Source-Security-Guide | https://github.com/guardrailsio/awesome-python-security
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---
