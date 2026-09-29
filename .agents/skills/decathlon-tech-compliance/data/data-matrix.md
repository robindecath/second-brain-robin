# 📊 FULL DATA & STREAMING ACTIVE MATRIX (Decathlon)

> **INSTRUCTIONS POUR L'AGENT :**
> 1. Référentiel complet des exigences DATA & STREAMING SIG.
> 2. Chaque point doit être validé selon le Step BMAD indiqué.
> 3. En cas de non-conformité, l'agent doit lever une alerte ou proposer une remédiation.

---

### [#0-DD00-HBORTTAB-31037d3a] Your data model is documented
- **Level:** Level 1 | **Topic:** Data documentation
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** Your functional product's data model (business objects, business value) mainly described through the raw code source or scattered files, limiting documentation to describing physical tables after they are built

- [Business object definition](https://decathlon-group.collibra.com/asset/00923336-c93c-4c92-bd2f-280cb7cb2115) in collibra.
- [Business objects and attributes definition](https://docs.google.com/presentation/d/1gioqQf0w0LyIGx7Non8K7yx59fVXC-FyfnH1KnYkY1I/edit?usp=sharing)
- [Example of a business object documentation](https://decathlon-group.collibra.com/asset/1739c89e-11f8-4455-b847-f715b5af94e7)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DD00-HTDMBD00-16362b62] Your data model is centralized in the Data Catalog
- **Level:** Level 3 | **Topic:** Data documentation
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** Business objects and definitions are referenced in the official Data Catalog with help from Data Governance to align with company standards.
It is required in order to the technical stakeholders to understand data.

- [Data modeling detailed process](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-knowledge/functional-data-knowledge) (to document app, data objects and datasets)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DD00-YMSAC000-b8a18fea] You manage schemas as code
- **Level:** Level 3 | **Topic:** Data documentation
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** Schema management is handled using 'Schema-as-Code' and versioned in Git repositories.

- Illustration with the [Data Contract approach](https://decathlon.atlassian.net/wiki/spaces/DATA/pages/185336971/Data+contract)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DD00-HTABRAVW-39d3bf15] You systematically update documentation upon release
- **Level:** Level 4 | **Topic:** Data documentation
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** You ensure the Data Catalog accurately reflects the functional definitions of all production data. Updates are performed systematically with every change or release, often in collaboration with the Data Steward.

- To [reference](https://decathlon.atlassian.net/wiki/spaces/DATA/pages/236422446/How+to+validate+Data+has+an+identified+Producer) the app in Collibra
- To [find the data manager](https://sites.google.com/decathlon.com/data-governance/roles-responsibilities/data-manager) related to my data
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-DD00-HCDBIADW-40c8bf58] Has critical data been identified and documented with the Data Manager in the Data Catalog (Collibra)?
- **Level:** Level 5 | **Topic:** Data documentation
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** Data criticity is being identified in Collibra (2024-2025)
- [Definition of critical data](https://docs.google.com/presentation/d/11qh5SIVK071a2QZUsdkCBHXHFjtz8WJv/edit#slide=id.g2cedf5c4640_1_0)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-DD00-IDDIWDCD-d2e417c6] You follow a "Schema-First" approach with versioning strategy contract-compliant
- **Level:** Level 5 | **Topic:** Data documentation
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** Functional modeling and documentation are mandatory steps performed before any new data is exposed.
A robust schema versioning strategy is in place to ensure evolution without breaking downstream data contracts.

- Illustration with the [Data Contract approach](https://decathlon.atlassian.net/wiki/spaces/DATA/pages/185336971/Data+contract)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-DG00-ATPKSAAO-07e4422d] You are aware of Data Governance topics
- **Level:** Level 1 | **Topic:** Data governance
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** Data governance [discovery kit](https://docs.google.com/presentation/d/1eJSsPjyTFlZ7V8-SuFQh6esvWFpi9dLuFUMJ19qddzA/edit#slide=id.g2a6cbe5e530_0_879)

As owner of an application/digital product, you might be a data producer.
Find the data producer training in the [Academy](https://classroom.decathlon.com/explore/presential/8794bd66-7170-4edb-8160-9fc966003dd5)

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-DG00-ITADWDGP-ecebdf65] Is there a disconnect where Data Governance priorities are invisible in your current backlog or technical planning ?
- **Level:** Level 1 | **Topic:** Data governance
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-DG00-ITDOMPIF-47a69f88] You encountered Data Governance topics
- **Level:** Level 3 | **Topic:** Data governance
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** Data that is not provided by its reference source creates duplication, and therefore generates confusion and unwanted stickiness in the IS.

If the data producer deviates from this principle, he must inform the data consumers in the documentation that this provision is only temporary.

- [How to validate Data is directly provided by the referent source](https://decathlon.atlassian.net/wiki/spaces/DATA/pages/236422466/How+to+validate+Data+is+directly+provided+by+the+referent+source)


- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DG00-DYIYDMAW-e42d627c] Do Data Governance roadmap requests often come as an afterthought, forcing you to adjust your sprint or roadmap reactively?
- **Level:** Level 3 | **Topic:** Data governance
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** Data criticity is being identified in Collibra (2024-2025)
- [Definition of critical data](https://docs.google.com/presentation/d/11qh5SIVK071a2QZUsdkCBHXHFjtz8WJv/edit#slide=id.g2cedf5c4640_1_0)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DG00-DMTKTDCO-2448b2ad] Did you receive specific Data Governance training & acculturation sesisons as part of your official onboarding path ?
- **Level:** Level 4 | **Topic:** Data governance
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** It is crucial to understand the usages of your data consumers in order to:
- Change data to deliver value for them (if needed).
- Not break downstream usages if you change data.

It can includes qualitative information (lineage, need, limits for consumers, tentative improvement) and quantitative information (number of users, number of flows connected to the data produced...).
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DG00-DYATCDOY-e1adba99] Are Data Governance requests identified and prioritized alongside your technical roadmap during standard planning rituals (e.g., Quarterly Planning, Sprint planning)?
- **Level:** Level 4 | **Topic:** Data governance
- **BMAD Step:** Step 05 - Testing
- **Constraint:** Data criticity is being identified in Collibra (2024-2025)
- [Definition of critical data](https://docs.google.com/presentation/d/11qh5SIVK071a2QZUsdkCBHXHFjtz8WJv/edit#slide=id.g2cedf5c4640_1_0)
- To work on critical data definition, contact your data manager

Example of specific actions:
- Quality Measure
- Auditability
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-DG00-TPHIAODG-7d222964] Is Data Governance embedded in your continuous learning rituals, keeping you proactively updated on new standards?
- **Level:** Level 5 | **Topic:** Data governance
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** You have on the scope of your data, at least:
- 1 data owner/knower/manager, 1 data steward
- 1 recurring meeting with them

Find the [data manager related to your data](https://sites.google.com/decathlon.com/data-governance/roles-responsibilities/data-manager) and the data owner (if he exists).
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-DG00-ADGRNEIY-fb5957f1] Are Data Governance requests natively embedded in your technical design and features, making the roadmap completely aligned?
- **Level:** Level 5 | **Topic:** Data governance
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-DP00-TMSAAOTP-72e020bc] Are you not unaware of which data within your scope classifies as Personal Data?
- **Level:** Level 1 | **Topic:** Data privacy
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** [Overall introduction](https://sites.google.com/a/decathlon.com/legal/data-protection/what-is-the-gdpr) documentation. You can as well read these ones:
- [Data Protection](https://sites.google.com/a/decathlon.com/legal/data-protection)
- [Data protection Training](https://sites.google.com/a/decathlon.com/legal/data-protection/training)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-DP00-IMACPDHT-3a1d14db] If my application collects personal data, have the user consent always been retrieved?
Has the process been validated by the treatment officer? The Data Protection Officer?
- **Level:** Level 1 | **Topic:** Data privacy
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** Here are the [contact names](https://www.google.com/maps/d/u/0/viewer?ll=15.35840076934714%2C0&z=2&mid=1PLccJ8GbWirmxbB6XEpA_voh1hIiTxBG) (DPO/Legal) for each country.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-DP00-HIRTPONO-0974b742] Did you make the effort to document or tag this data as ‘Personal’ (in your code or API), even if it required manual action or if it's in informal or partial lists (e.g., spreadsheets) ?
- **Level:** Level 2 | **Topic:** Data privacy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DP00-FDIITDOI-f063e180] Has information regarding the presence or not of personal data in your data / the class been documented by your data owner in the data catalog (Collibra)?

- **Level:** Level 3 | **Topic:** Data privacy
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** Definition of [Personal data](https://www.cnil.fr/en/personal-data-definition).

- Here is an [example](https://decathlon-group.collibra.com/asset/d14c487b-d7bb-4990-bd54-37cb63d182b7) of the place and of the type of information to fill in.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DP00-FDIITDOY-ce51054c] Have you verified that the Information regarding Personal/Confidential data been documented in the Data Documentation (Data Contract or ID Card for DFI users) ?
- **Level:** Level 3 | **Topic:** Data privacy
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** For DFI users : The [DFI process to fill in the ID card](https://sites.google.com/a/decathlon.com/legal/data-protection/data-protection-impact-assessment-dpia) requires the declaration of any personal data at step 3 (table level) and step 6 (column level) in order then the Data Factory Ingest Platform manages personal data specifically based on the security policies.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DP00-IMAPPDHT-99a2fe6a] If my application produces/manages personal data, has the final usage of it been documented?
- **Level:** Level 3 | **Topic:** Data privacy
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** [Data Protection Impact Assessment (DPIA)](https://sites.google.com/a/decathlon.com/legal/data-protection/data-protection-impact-assessment-dpia)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DP00-IALOCRTR-a6692769] If a list of clients require to remove their personal data, is your team able to do it easily? including the all history of data
- **Level:** Level 4 | **Topic:** Data privacy
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DP00-DYAHTRSA-80e5d56b] Are reliability checks (quality checks, monitoring, SLAs) applied systematically and in a standardized manner to this personal data,  based on the fully validated inventory in the Data Catalog where all Personal Data is clearly identified and tagged ?
- **Level:** Level 4 | **Topic:** Data privacy
- **BMAD Step:** Step 05 - Testing
- **Constraint:** Depending on the classification of the data, the level of security must be different (e.g. data encryption, storage in secured private zone, data access controls...).
For instance, the client name must be more protected than the adress of Decathlon shops.
Furthermore, security over data must be strenghtened if the data can be read by external users than for internal ones.

You must comply with the [Group personal data classification and security measures](https://decathlon.atlassian.net/wiki/spaces/DATA/pages/185431787/03a+-+Personal+Data+classification+security+measures).
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-DP00-DYTUAPFR-9bd64a8b] Does your team use a process for regular privacy impact assessments and audits to ensure compliance?
- **Level:** Level 5 | **Topic:** Data privacy
- **BMAD Step:** Step 05 - Testing
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-DP00-ISTPDIIT-159f702f] Is securing this personal data integrated in the pipilines / he design phase of every new feature or product you build and have your practices been shared to help other teams ?
- **Level:** Level 5 | **Topic:** Data privacy
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-DQ00-IYTTTBDQ-a2e99cbb] Is your team trained to basic data quality concepts and aware of the benefits?
- **Level:** Level 1 | **Topic:** Data quality
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** Here is the most relevant [training](https://classroom.decathlon.com/explore/presential/8794bd66-7170-4edb-8160-9fc966003dd5), focusing on data integrity.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-DQ00-ATRCOTPU-87db90b6] Are there reliability controls on the product/app UI at data entry/data creation?
- **Level:** Level 2 | **Topic:** Data quality
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** All data created must comply with the business requirements described before.

Illustration: in the client address, the country entry is validated based on a predefined list
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DQ00-HQRATBDA-109ff5ce] Have quality rules and thresholds been defined and validated with data governance stakeholders?
- **Level:** Level 3 | **Topic:** Data quality
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** Data governance office documentation regarding the [data quality process and conventions](https://docs.google.com/presentation/d/1BDk9VysXmK6Y9vaNP-RoERomfyu-hasAwnEuVCkkxIU/edit#slide=id.g2f02d7c04e7_0_53).

To do in collaboration with at least the Data Manager, if existing in my perimeter, data owner/data steward and Data Quality Manager, following the processes and conventions recommended by the Data Governance Office.
It includes SLAs.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DQ00-HDQBMUAS-0a70fee4] Has data quality been monitored using automated scripts and the results available centrally?
- **Level:** Level 3 | **Topic:** Data quality
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **All quality test results must be made available to users** (principle of transparency).

In the Data Unit, for instance, data quality results used to be stored in AWS S3 datalake in the bucket owned by the Data Observability team.
- Example of data quality dimensions : integrity, consistency, ...
- Example of automated scripts methods: python, SaaS tool for data transformation or a dedicated quality tool.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DQ00-DYTADRPD-18a3a308] Does your team apply data remediation process, data escalation process, post mortem, and any additional process to make the data quality experience smoother?
- **Level:** Level 4 | **Topic:** Data quality
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** - [Macro process of data quality](https://docs.google.com/presentation/d/1eFV-8POHRA4jthPHIj5uQZYda5OaO_bcH3bK3CbcemQ/edit#slide=id.g2c7490cac02_0_1929)
- [How to](https://docs.google.com/document/d/1p2dY5Zu1lNwvbp5klxGjNBBGLV5GcNai9Np0768BlUc/edit?tab=t.0#heading=h.208ezn6rk5ea) Data Quality macro process
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DQ00-IASWTIAL-c1087006] Is alerting systematic when there is a lack of data quality?
- **Level:** Level 4 | **Topic:** Data quality
- **BMAD Step:** Step 03 - Architecture
- **Constraint:**
- Alerting to the data sources owners, to the data consumer.
- The data producer uses a tool to alert data consumers

[Macro process of data quality](https://docs.google.com/presentation/d/1eFV-8POHRA4jthPHIj5uQZYda5OaO_bcH3bK3CbcemQ/edit#slide=id.g2c7490cac02_0_1929)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-DQ00-DYHAFCRD-3cd26cfc] Do you have a formal commitment regarding data quality with your consumers, with preventive actions to limit the impact of bad data quality?

- **Level:** Level 5 | **Topic:** Data quality
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** To limit the downstream business impact, a preventive approach is in place to limit the lack of data quality even before it is exposed (e.g. data contractualization approach).

- Illustration with the [Data Contract approach](https://decathlon.atlassian.net/wiki/spaces/DATA/pages/185336971/Data+contract) and [policies](https://docs.google.com/document/d/1rocg5d9ZXonW-C5CeKKCsUX7SdNVx5nYUQ624VJ4k1g/edit?tab=t.0)

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-DQ00-DQRAVTN0-e89cfbc7] DOCUMENTATION
Your quality rules are visible to non-developers
- **Level:** Level 2 | **Topic:** Data quality
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** You ensure that management rules (e.g., formats, mandatory fields) are documented outside of the application's source code, allowing business stakeholders to read and understand them.

[Data quality reference documents](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-DQ00-CACBOYR0-d5da1404] CONTROLS
You apply checks base on your rules
- **Level:** Level 2 | **Topic:** Data quality
- **BMAD Step:** Step 05 - Testing
- **Constraint:** You currently discover data quality issues reactively, often through downstream user complaints, and perform manual fixes on production pipelines.

[Data quality reference documents](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-DQ00-APAAWAQI-bde21322] ALERTING
You provide an alert whenever a quality issue arises
- **Level:** Level 2 | **Topic:** Data quality
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** You lack an active alerting system. Data quality drops are usually discovered only when downstream users report broken reports or system errors.

[Data quality reference documents](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-DQ00-RPFOYQI0-45ceadf6] REMEDIATION
You perform fixes on your quality issue
- **Level:** Level 2 | **Topic:** Data quality
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** Data quality issues are fixed on the fly. There is no formal logging of the root cause or the solution in a tracking tool, making it difficult to learn from past errors.

[Remediation process](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality/remediation-process)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DQ00-DFYRIASD-67ed0320] DOCUMENTATION
You formalized your rules in a shared document
- **Level:** Level 3 | **Topic:** Data quality
- **BMAD Step:** Step 05 - Testing
- **Constraint:** You list and describe tested quality rules in a technical document accessible to the team (e.g., README, Confluence, or Sheets), even if the document is currently maintained locally.

[Data quality reference documents](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DQ00-CIAC0000-224c66f5] CONTROLS
You implemented automated controls
- **Level:** Level 3 | **Topic:** Data quality
- **BMAD Step:** Step 05 - Testing
- **Constraint:** You use your own technical stack (e.g., SQL scripts, Python, dbt tests) to automate checks, though they may run sporadically (only during releases or after incidents).

[Data quality reference documents](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DQ00-APAWAQII-3017dc0f] ALERTING
You proactively alert when a quality issue is detected
- **Level:** Level 3 | **Topic:** Data quality
- **BMAD Step:** Step 05 - Testing
- **Constraint:** You must remember to manually check dashboards or run scripts to detect issues. There is no automated push notification to tell you when something is wrong.

[Data quality reference documents](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DQ00-RDTPS000-0fc82be7] REMEDIATION
You document the post-fix summary
- **Level:** Level 3 | **Topic:** Data quality
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** You document the fix only after the incident is resolved. While the cause is briefly noted, there is no detailed tracking or visibility during the investigation phase.

[Remediation process](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality/remediation-process)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DQ00-DDCIYSOT-c56123a8] DOCUMENTATION
The Data Catalog is your "Source of Truth" for rules
- **Level:** Level 4 | **Topic:** Data quality
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** Your quality rules are referenced in the official company tool (Data Catalog, Collibra, or Data Contracts). This serves as the single validated source of truth prior to implementation.

[Data quality reference documents](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DQ00-CCAFAAAW-535132b0] CONTROLS
Your controls are fully automated and aligned with rules
- **Level:** Level 4 | **Topic:** Data quality
- **BMAD Step:** Step 05 - Testing
- **Constraint:** Data quality checks are fully automated (e.g., daily batches or real-time) and strictly reflect the formally documented rules validated in the Data Catalog.

[Data quality reference documents](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DQ00-ASANWQIA-deccfa53] ALERTING
You send automated notifications when quality issue arises
- **Level:** Level 4 | **Topic:** Data quality
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** Alerts are automatically sent to the relevant owners as soon as a critical threshold is breached, allowing for faster intervention before users notice.

[Data quality reference documents](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DQ00-RRPITIR0-8c648893] REMEDIATION
The remediation process is tracked in real-time
- **Level:** Level 4 | **Topic:** Data quality
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** The entire incident lifecycle is visible and documented. You provide clear status updates from detection to deployment, ensuring stakeholders are informed throughout the resolution.

[Remediation process](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality/remediation-process)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-DQ00-DLQRTBIA-4dffcda3] DOCUMENTATION
You link quality rules to business impact and thresholds
- **Level:** Level 5 | **Topic:** Data quality
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** Your documentation includes clear business context and specific quality thresholds. This allows for data-driven prioritization of remediation efforts based on business risk.

[Data quality reference documents](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-DQ00-CCAIIDC0-9bf6746a] CONTROLS
Your controls are integrated into Data Contracts
- **Level:** Level 5 | **Topic:** Data quality
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** Technical execution is linked to documentation to prevent drift. You automatically detect anomalies like volume spikes, schema changes, or freshness delays.

[Data quality reference documents](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-DQ00-AIIIYIW0-b2079c24] ALERTING
Alerting is integrated into your incident workflow
- **Level:** Level 5 | **Topic:** Data quality
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** Alerts are fully integrated into technical tools (e.g., auto-creating tickets). They include root-cause hints and handle alert fatigue through deduplication and smart routing.

[Data quality reference documents](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-DQ00-RPSRTPR0-2f9a79a4] REMEDIATION
You perform systematic RCAs to prevent recurrence
- **Level:** Level 5 | **Topic:** Data quality
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** Every incident triggers a Root Cause Analysis (RCA) or Post-Mortem. These insights directly lead to updated monitoring rules or architectural changes to ensure the same issue never happens twice.

[Remediation process](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality/remediation-process)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-RD00-AYAOERAP-90976c4a] Are you aware of existing rules and principles for handling reference and master Data?
- **Level:** Level 1 | **Topic:** Reference data
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** [Reference Data Policy](https://docs.google.com/document/d/1XF_Nx-ly1gzL9JbQwryOrH1oXT7ELC4PTwLjQldsucw/edit?usp=sharing)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-RD00-IYPCRDDY-d8f5ae50] If your project/product contains/consume/produce reference data. Did You identified related Business Objects?
- **Level:** Level 2 | **Topic:** Reference data
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** [Reference Data Policy](https://docs.google.com/document/d/1XF_Nx-ly1gzL9JbQwryOrH1oXT7ELC4PTwLjQldsucw/edit?usp=sharing)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-RD00-IYPCRDDY-b368a8bb] If your project/product contains/consume/produce reference data. Did You identified source of truth applications of those reference data?
- **Level:** Level 3 | **Topic:** Reference data
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** [Reference Data Policy](https://docs.google.com/document/d/1XF_Nx-ly1gzL9JbQwryOrH1oXT7ELC4PTwLjQldsucw/edit?usp=sharing)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-RD00-DYMRDOYP-cbf1a1c5] Do you manage/consume/share reference data of your project according to Reference Data Policy?
- **Level:** Level 5 | **Topic:** Reference data
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** Examples of Reference Data Policiyrequirements: SLA/Quality, Quality requirements, Repository pre-requisities

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-CD00-YITCDAWY-e3e58160] You identified the critical data assets within your scope
- **Level:** Level 1 | **Topic:** Critical Data
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** You recognize which specific data assets have a high business impact for the company, looking beyond purely technical needs or internal project use.

- [Critical Data asssement process & assessment matrix](https://sites.google.com/decathlon.com/data-governance/reference-documents/critical-data-management)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-CD00-YSTODYCD-0a483c88] You started tagging or documenting your critical data
- **Level:** Level 3 | **Topic:** Critical Data
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** You have identified critical assets in your code, APIs, or documentation. This may still involve manual effort or reside in informal/partial lists (e.g., spreadsheets).

- [Critical Data policy & guidelines](https://sites.google.com/decathlon.com/data-governance/reference-documents/critical-data-management)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-CD00-YCAASMAC-8af49983] Your critical assets are systematically monitored and cataloged
- **Level:** Level 4 | **Topic:** Critical Data
- **BMAD Step:** Step 05 - Testing
- **Constraint:** Reliability checks (Quality, Monitoring, SLAs) are applied in a standardized way. Your assets are fully identified and tagged in the official Data Catalog or your Data Contract.

- [Critical Data monitoring & Critical Data list](https://sites.google.com/decathlon.com/data-governance/reference-documents/critical-data-management)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-CD00-CDBDIPOY-74a8a60b] "Critical Data by Design" is part of your development lifecycle
- **Level:** Level 5 | **Topic:** Critical Data
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** Data criticality is integrated into the design phase of every new feature. You proactively secure these pipelines and share your expertise to help other teams improve.

- [Critical Data monitoring & Critical Data list](https://sites.google.com/decathlon.com/data-governance/reference-documents/critical-data-management)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-DI00-YAAOTISA-bc311d83] You are aware of the ingestion standards and the Data Steward’s role
- **Level:** Level 1 | **Topic:** Datalake Integration
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** You understand that data accessibility requires specific technical rules.
Resources:
- [DFI](https://dataplatform.dktapp.cloud/doc/products/ingestion/dfi/what_is_dfi.html) for autonomous service
- [Custom Track](https://decathlon.atlassian.net/wiki/spaces/DATA/pages/1257406907/CustomTrack+user+step+by+step+guide) for other cases
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DI00-YDIFFTG0-41f91d13] You deploy ingestion flows following technical guidelines
- **Level:** Level 3 | **Topic:** Datalake Integration
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** You configure and deploy flows (naming, format, metadata) according to guidelines, even if you still need support from the Data Steward.
Resources:
- Use [DFI](https://dataplatform.dktapp.cloud/doc/products/ingestion/dfi/what_is_dfi.html) for self-service.
- Follow the [Custom Track](https://decathlon.atlassian.net/wiki/spaces/DATA/pages/1257406907/CustomTrack+user+step+by+step+guide) for specific needs.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DI00-YMAMYIFI-9a6e3580] You manage and monitor your ingestion flows independently
- **Level:** Level 4 | **Topic:** Datalake Integration
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** You handle end-to-end management (failures, retries, corrections) without Data Steward intervention.
Resources:
- DFI [monitoring](https://dataplatform.dktapp.cloud/doc/products/ingestion/dfi/concepts/monitoring/monitoring.html) & [SMA-X alerting](https://dataplatform.dktapp.cloud/doc/products/ingestion/dfi/concepts/monitoring/smax_alerting.html).
- Custom monitoring & SMA-X for Custom Track.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-DI00-YATIODCO-76560103] You assess the impact of data changes on downstream flows
- **Level:** Level 5 | **Topic:** Datalake Integration
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** You anticipate how product or data model changes will affect ingestion before development, ensuring that updates never break the downstream data pipeline.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-ES00-AFEHPIDW-3db547a7] A formal error handling policy is documented. We have a defined (even if manual) process to detect, inspect, and manage failed messages.
- **Level:** Level 1 | **Topic:** Event Streams
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** **For example:** when do I retry, or send to DLT and skip? We can also have different policies based on what we do with the topic
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-ES00-ODEHPICA-f8c3899c] Our defined error handling policy is consistently applied & implemented on every topics and queues.
- **Level:** Level 2 | **Topic:** Event Streams
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** **Why:** Consistency ensures that no "silent failures" occur in production. Every topic or queue, regardless of perceived importance, follows the same safety patterns to prevent data loss.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-ES00-ODEHPIMT-3b7df757] Our defined error handling policy is monitored. This includes mechanisms like automated alerting for failure thresholds, and (where appropriate) automated redrive/replay capabilities
- **Level:** Level 3 | **Topic:** Event Streams
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** **Why:** The process is robust, efficient, and scalable, freeing up the team to solve new problems instead of managing old ones
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-ES00-LLFTAOIM-011dd41f] Lessons learned from the analysis of invalid messages are used proactively to improve system robustness and prevent errors upstream.
- **Level:** Level 4 | **Topic:** Event Streams
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **How:** Regular post-mortems on Dead Letter Topics or Queue (DLT or DLQ) to identify schema mismatches or logic errors, feeding these back into upstream validation or contract tests.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-ES00-CADTBITC-cae03c33] Consumers are designed to be idempotent. They can safely process the exact same message multiple times without creating duplicate records, sending multiple emails, or causing other side effects
- **Level:** Level 1 | **Topic:** Event Streams
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** **Why:** This handles "at-least-once" delivery. If you can't handle a simple network-hiccup duplicate, you have no business attempting a full replay.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-ES00-AFPETCAR-ee8b1d95] A formalized process exists to capture and re-process individual failed messages. This process is documented, validated and shared
- **Level:** Level 2 | **Topic:** Event Streams
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** **Why:** This proves you can recover from individual poison pills or transient errors without stopping the whole line. It's a controlled, small-scale replay.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-ES00-TPSRLWOH-0c218a6a] The platform supports re-processing large windows of historical events. This is achieved via mechanisms like resetting consumer offsets (e.g., in Kafka), re-publishing from a persistent event store, or querying a time-stamped data lake. This capability is documented, shared, and tested
- **Level:** Level 3 | **Topic:** Event Streams
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **Why:** This is the goal. You can rebuild an entire service's state from scratch, onboard a new analytics system, or recover from a catastrophic bug that corrupted data for hours.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-ES00-TAQAGUDN-431c3c19] Topics and queues are given unique, descriptive names that reflect their purpose
- **Level:** Level 1 | **Topic:** Event Streams
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **Why:**  This is the bare minimum. You're not using default names (queue-1) or temporary names (john_doe_test).
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-ES00-AFNCIDSA-a02b4b6f] A formal naming convention is documented, shared, and actively socialized. New topics and queues are expected to follow it
- **Level:** Level 2 | **Topic:** Event Streams
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** **Why:** You've moved from individual good intentions to a shared, agreed-upon standard. This brings consistency and makes the platform discoverable

[Example of topic naming convention](https://framework.eu.member.decathlon.net/streaming/03-convention/topics/ )
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-ES00-TNCIAUAC-4e386072] The naming convention is applied universally and compliance is enforced automatically (e.g., resource-creation policies, or scripts).
- **Level:** Level 3 | **Topic:** Event Streams
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** **Why:** This is true maturity. The "right way" is the only way. It's impossible to create a non-compliant resource, and there's likely a plan to remediate old, non-compliant ones.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-ES00-ADRPIDAD-9aefb6d0] A data retention policy is defined and documented for our topics/queues
- **Level:** Level 1 | **Topic:** Event Streams
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** **WHY**: To prevent infinite data growth and ensure predictable storage consumption by automatically deleting old messages.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-ES00-ORPIPWAD-af746079] Our retention policy is purpose-driven. We apply different lifecycle strategies based on the data's specific use case.
- **Level:** Level 2 | **Topic:** Event Streams
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **Warning :** Non available for queueing
**Why:** To optimize storage efficiency by keeping only the latest state for specific keys (compaction) while saving space
**How:** Log compaction keeps only the latest message per key in each partition. Each message must have a key so messages with the same key go to the same partition.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-ES00-SSAIAOIA-aff21ddb] Storage strategies are implemented and optimized in alignment with the standard company decision matrix
- **Level:** Level 3 | **Topic:** Event Streams
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** **Why:** To balance cost and performance by moving older data to cheaper storage tiers while respecting strict business retention constraints.

Link 1 : [Kafka cluster creation decision matrix](https://decathlon.atlassian.net/wiki/spaces/TO/pages/1643381012/STRAT+Kafka+cluster+creation+decision+matrix)
Link 2 : [Kafka Tiered Storage](https://decathlon.atlassian.net/wiki/spaces/TO/pages/1667072080/GUIDE+Kafka+Tiered+Storage)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-ES00-WMPSAABO-763919df] To mitigate high-volume or high-latency scenarios, we employ specific configurations to handle them.
- **Level:** Level 1 | **Topic:** Event Streams
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** **Why:** To ensure low latency and system stability by preventing oversized payloads from degrading network performance or exceeding broker limits.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-ES00-PSIOBOMN-e58aa589] Payload size is optimized based on my needs. I use Avro and compression (e.g., ZSTD, Gzip, Snappy) when relevant.
- **Level:** Level 2 | **Topic:** Event Streams
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** **Why:** It's a good practice to save network and broker disk space.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-ES00-WBATOPEC-1c84804e] We benchmark and tune optimization parameters (e.g., compression level vs. CPU cost, batch.size vs. linger.ms) to meet specific business SLAs.
- **Level:** Level 3 | **Topic:** Event Streams
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** **Why:** To find the right balance between throughput, latency, and infrastructure cost to meet specific business SLAs.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-ES00-MMSHICTC-1049fa61] Message metadata structure (headers) is compliant to CloudEvents as specified in Decathlon standards (see link in the doc)
- **Level:** Level 4 | **Topic:** Event Streams
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** **Why:** To enable consistent communication and interoperability across distributed services, CloudEvents standardizes event metadata in event-driven architectures.

This allows any consumer to route or filter any messages whatever the producer without parsing the body.

**See:**
[CloudEvents](https://decathlon.atlassian.net/wiki/spaces/TO/pages/1652918834/GUIDE+CloudEvents+for+Kafka)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-I000-TSIIDBDN-f0dfa980] Topic sizing is intentionally determined by documented needs, considering parallelism and scaling requirements
- **Level:** Level 2 | **Topic:** Infrastructure
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** **Why:** To ensure optimal partition distribution, preventing bottlenecks during peak loads while maintaining the integrity of message ordering through balanced parallelism.

Link 1 : [how to choose the right number of kafka partitions and consumers](https://dev-aditya.medium.com/how-to-choose-the-right-number-of-kafka-partitions-and-consumers-4b2a4caaf8ae)
Link 2 : [kafka visualisation](https://softwaremill.com/kafka-visualisation/)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-I000-OHSMVDIA-b154a19a] Our hosting strategy (Mutualized vs. Dedicated) is a deliberate architectural decision driven by specific isolation and cost requirements.
- **Level:** Level 3 | **Topic:** Infrastructure
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** **Why:**  We avoid arbitrary choices. We use shared clusters to optimize costs for standard needs, and dedicated clusters only when isolation or specific performance guarantees are required.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-I000-WATITSCT-3dc12f04] We adapt the infrastructure topology (Storage & Compute) to specific workload requirements, rather than applying a static, one-size-fits-all configuration.
- **Level:** Level 4 | **Topic:** Infrastructure
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** **Examples:**  Leveraging Tiered Storage for long retention, or Diskless topics for high-throughput proxying.
**Doc :**
[Kafka Tiered Storage](https://decathlon.atlassian.net/wiki/spaces/TO/pages/1667072080/GUIDE+Kafka+Tiered+Storage)

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-I000-OISIDFDV-04f490f6] Our infrastructure scaling is decoupled from data volume, allowing us to optimize costs and capacity dynamically
- **Level:** Level 5 | **Topic:** Infrastructure
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** **How:** By using Tiered Storage or diskless architectures, we break the link between "adding storage" and "adding brokers." This allows us to apply our cost/value strategy effectively
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-O000-WAATMITH-65500de2] We are able to manually inspect the health of our product by checking both application (logs, message lag) and infrastructure (CPU, memory) metrics
- **Level:** Level 1 | **Topic:** Observability
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **How:** Use internal dashboards (e.g., Datadog) or UI tools (e.g., Kafbat) to view current lag and resource usage.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-O000-ARAAIMDL-54e7e8a2] All relevant application and infrastructure monitoring data (logs, metrics) is centralized in one or more dedicated tools
- **Level:** Level 2 | **Topic:** Observability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** **Why:** Having logs and metrics in one place allows for correlation between a spike in CPU and a specific error log.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-O000-AAADAIFA-eb18eeaa] Automated alerts are defined and implemented for all essential product metrics (e.g., consumer lag, error rates, resource saturation).
- **Level:** Level 3 | **Topic:** Observability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** **Advice :** Lag alerts should be coupled with resource saturation metrics (CPU/Memory) to distinguish between consumer slowness and broker issues.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-O000-WUDTTTMF-43ef9b6e] We use distributed tracing to track message flows across services.
- **Level:** Level 4 | **Topic:** Observability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** **Why:** To identify exactly which service is blocking the flow, rather than just seeing a lag spike.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-O000-MIFDDASA-651e1999] Monitoring is fully documented, dashboards are shared, and alerts are actively reviewed and tuned. The whole team uses this data to debug, plan capacity, and improve performance.
- **Level:** Level 5 | **Topic:** Observability
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **Action:** At least one "Alerting Reviews" per quater to audit and tune alerting based on post-mortems and on-call history to eliminate noise and ensure all alerts are actionable.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-O000-YMAMAEBS-b3a9acb8] You measure and manage an event based SLO (freshness, correctness, coverage...)
- **Level:** Level 5 | **Topic:** Observability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Expected
* There's an SLO that measure the reliability of the Data processing user journey you're in.

### Why
* Measuring the lag, or a completion time for a single function is good. But we want to measure the real impact for the user in the end.

### How ?
Guidelines will come during the year, from the SIG Reliability. In the meantime, explore some leads to do it the best way you can

### Example
* For an order management process, you measure the % of orders that went from starting to ending point in less than xx minutes
* For a price update process, you measure the % of price changes applied in less than xx minutes. From the change in the referential, until it's available in your last system (In Store till, or Ecommerce catalog)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-S000-ACAIIPAI-0276972f] Access control (ACL) is in place and is managed ( at least manual )
- **Level:** Level 1 | **Topic:** Security
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** **Why:** To establish a baseline of security and ensure that only authorized service can access critical / sensitive resources.
**Minimum:** Every publisher and subscriber has a dedicated access with specific Read or Write rights to its required topics / queues.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-S000-ARABOGPC-c6d411f3] Access requests are based on granular, policy-based control
- **Level:** Level 2 | **Topic:** Security
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** **Why:** To enforce the "Principle of Least Privilege," ensuring users have the exact permissions needed for their specific ressources, reducing the attack surface.
**How:** Give access only for specific topic/queue instead of giving access to a large pattern
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-S000-ACAICAMC-0008cd4b] Access control (ACL) is centralized and managed (creation, update and rotation)
- **Level:** Level 3 | **Topic:** Security
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **Why:** To ensure that only authorized services remain able to access critical/sensitive resources
**How:** At least one "ACL Reviews" per quarter to audit and tune access to identify and manage "shadow access" in order to keep consistency, making it easier to audit and revoke permissions.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-S000-AMAIAAHT-7e80e2ce] Access management is automated and handled to ensure traceability, reproducibility and security
- **Level:** Level 4 | **Topic:** Security
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** **Why:** To ensure the credentials confidentiality and their rotation
**How:** Use internal secret manager (e.g., gcp secret manager, vault), and rotate credentials regularly, duration depending of the resources criticality
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---
