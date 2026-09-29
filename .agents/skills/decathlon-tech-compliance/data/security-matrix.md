# 🛡️ FULL SECURITY ACTIVE MATRIX (Decathlon)

> **INSTRUCTIONS POUR L'AGENT :**
> 1. Référentiel complet des exigences SECURITY SIG.
> 2. Chaque point doit être validé selon le Step BMAD indiqué.
> 3. En cas de non-conformité, l'agent doit lever une alerte ou proposer une remédiation.

---

### [#1-CODE003-ManualSecureCodeReview] CODE003 - Internal developers are aware of and responsible for the security of their code. (proof : name of project developer)
* mandatory awareness : 6 modules on [decathlon.ws02-securityeducation.com](https://decathlon.ws02-securityeducation.com) (not open for partner)
- **Level:** Level 1 | **Topic:** Code/Build
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** **CODE003 Manual Secure Code Review**

[Wiki - CODE003 Manual Secure Code Review](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197463270/CODE003+Manual+Secure+Code+Review)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-CODE007-InlineIDESecureCodeAnalysis] CODE007 - The team has a Snyk (secure code scanner) directly integrated into the IDE.

\
_Snyk is only available for Application with Criticality Level 3 and 4, use NOT_APPLICABLE for other cases_
- **Level:** Level 3 | **Topic:** Code/Build
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **CODE007 Inline IDE Secure Code Analysis**

! Snyk through the IDE is accessible for everyone in DKT (even without SC) !

[Snyk Documentation](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/215222036/Snyk+as+Plugin+in+IDE+VS+Code)

[Wiki - CODE007 Inline IDE Secure Code Analysis](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460393/CODE007+Inline+IDE+Secure+Code+Analysis)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-CODE003-ManualSecureCodeReview] CODE003 - A security champion reviews and validates the pertinent PR from a security point of view.
* proof expected in comments : name of security champion / links from a PR example
- **Level:** Level 3 | **Topic:** Code/Build
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** **CODE003 Manual Secure Code Review**

[Wiki - CODE003 Manual Secure Code Review](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197463270/CODE003+Manual+Secure+Code+Review)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-CODE004-SAST] CODE004 - The team has a Snyk (SAST scanner) built into their application deployment and the results are tracked by the team.
* it's mandatory rule for application with Criticality Level 3 and 4
* at least one scan before each release
* proof expected in comments : "Snyk Dashboard link"

\
_Snyk is only available for Application with Criticality Level 3 and 4, use NOT_APPLICABLE for other cases_
- **Level:** Level 2 | **Topic:** Code/Build
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **CODE004 Static Application Security Testing**

[Snyk Documentation](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/205097834/Snyk+SAST+SCA)

[Wiki - CODE004 Static Application Security Testing](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197463261/CODE004+SAST+Static+Application+Security+Testing)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-CODE005-SCA] CODE005 - The team has a Snyk (SCA scanner) built into their application deployment and the results are tracked by the team.
* it's mandatory rule for application with Criticality Level 3 and 4
* at least one scan before each release
* proof expected in comments : "Snyk Dashboard link"

\
_Snyk is only available for Application with Criticality Level 3 and 4, use NOT_APPLICABLE for other cases_
- **Level:** Level 2 | **Topic:** Code/Build
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **CODE005 SCA Software Composition Analysis**

[Snyk Documentation](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/205097834/Snyk+SAST+SCA)

[Wiki - CODE005 SCA Software Composition Analysis](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460737/CODE005+SCA+Software+Composition+Analysis)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-CODE006-SLC] CODE006 - The team has a Snyk (SLC scanner) built into the application builds and the results are tracked by the team following the rules of the framework.
* it's mandatory rule for application with Criticality Level 3 and 4
* at least one scan before each release
* proof expected in comments : "Snyk Dashboard link"

\
_Snyk is only available for Application with Criticality Level 3 and 4, use NOT_APPLICABLE for other cases_
- **Level:** Level 2 | **Topic:** Code/Build
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **CODE006 SLC Software Licence Compliance**

[Snyk Documentation](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/205097834/Snyk+SAST+SCA)

[Wiki - CODE006 SLC Software Licence Compliance](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197463273/CODE006+SLC+Software+Licence+Compliance)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-CODE007-InlineIDESecureCodeAnalysis] CODE007 - The team has a Snyk (secure code scanner) directly integrated in the IDE and has defined a specific scope of rules for their project.

\
_Snyk is only available for Application with Criticality Level 3 and 4, use NOT_APPLICABLE for other cases_
- **Level:** Level 5 | **Topic:** Code/Build
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **CODE007 Inline IDE Secure Code Analysis**

! Snyk through the IDE is accessible for everyone in DKT (even without SC) !

[Snyk Documentation](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/215222036/Snyk+as+Plugin+in+IDE+VS+Code)

[Wiki - CODE007 Inline IDE Secure Code Analysis](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460393/CODE007+Inline+IDE+Secure+Code+Analysis)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-CODE003-ManualSecureCodeReview] CODE003 - A security champion performs a regular (at least annually) code review of all the application's code.
* proof expected in comments: name of security champion / links from security review document
- **Level:** Level 4 | **Topic:** Code/Build
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** **CODE003 Manual Secure Code Review**

[Wiki - CODE003 Manual Secure Code Review](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197463270/CODE003+Manual+Secure+Code+Review)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-CODE004-SAST] CODE004 - The team has a built-in Snyk (SAST scanner) in all builds and PR of the app. The scanner blocks builds and PR if the result shows vulnerabilities. Regular monitoring is done on the non-blocking results.

\
_Snyk is only available for Application with Criticality Level 3 and 4, use NOT_APPLICABLE for other cases_
- **Level:** Level 3 | **Topic:** Code/Build
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **CODE004 Static Application Security Testing**

[Snyk Documentation](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/205097834/Snyk+SAST+SCA)

[Wiki - CODE004 Static Application Security Testing](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197463261/CODE004+SAST+Static+Application+Security+Testing)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-CODE005-SCA] CODE005 - The team has a built-in Snyk (SCA scanner) in all builds and PR of the app. The scanner blocks builds and PR if the result shows vulnerabilities. Regular monitoring is done on the non-blocking results.

\
_Snyk is only available for Application with Criticality Level 3 and 4, use NOT_APPLICABLE for other cases_
- **Level:** Level 3 | **Topic:** Code/Build
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **CODE005 SCA Software Composition Analysis**

[Snyk Documentation](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/205097834/Snyk+SAST+SCA)

[Wiki - CODE005 SCA Software Composition Analysis](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460737/CODE005+SCA+Software+Composition+Analysis)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-CODE006-SLC] CODE006 - The team has a Snyk (SLC scanner) built into the application builds and PRs. Depending on the results, this blocks the builds and PRs. Regular follow-up is done on non-blocking results.

\
_Snyk is only available for Application with Criticality Level 3 and 4, use NOT_APPLICABLE for other cases_
- **Level:** Level 3 | **Topic:** Code/Build
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **CODE006 SLC Software Licence Compliance**

[Snyk Documentation](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/205097834/Snyk+SAST+SCA)

[Wiki - CODE006 SLC Software Licence Compliance](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197463273/CODE006+SLC+Software+Licence+Compliance)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-CODE007-InlineIDESecureCodeAnalysis] CODE007 - The team has a Snyk (secure code scanner) directly integrated into the IDE and blocks the push if the code does not meet the specific rules for their project.

\
_Snyk is only available for Application with Criticality Level 3 and 4, use NOT_APPLICABLE for other cases_
- **Level:** Level 5 | **Topic:** Code/Build
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **CODE007 Inline IDE Secure Code Analysis**

! Snyk through the IDE is accessible for everyone in DKT (even without SC) !

[Snyk Documentation](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/215222036/Snyk+as+Plugin+in+IDE+VS+Code)

[Wiki - CODE007 Inline IDE Secure Code Analysis](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460393/CODE007+Inline+IDE+Secure+Code+Analysis)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-DES002-ThreatModelling] DES002 - The project context has been filled with your Security Champion and stored in the security champion drive.
* it's mandatory rule
* proof expected in comments : document link
- **Level:** Level 2 | **Topic:** Design
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** **DES002 Threat Modelling**

[project context explanation and template](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/283509593/Mapping+contextualization)

[Wiki - DES002 Threat Modelling](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460387/DES002+Threat+Modelling)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-DES003-AccessRightManagement] DES003 - All applications for employees, of which at least one resource must not be accessible to everyone, I set up FedID.
* proof expected in comments : EntityID or client_ID
- **Level:** Level 1 | **Topic:** Design
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** **DES003 Access Right Management**

[Wiki - DES003 Access Right Management](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460389/DES003+Access+Right+Management)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DES002-ThreatModelling] DES002 - A threat modeling activity has been performed on the application by a security analyst (AppSec or SO).
* proof expected in comments : document link
- **Level:** Level 4 | **Topic:** Design
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** **DES002 Threat Modelling**

[Wiki - DES002 Threat Modelling](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460387/DES002+Threat+Modelling)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DES003-AccessRightManagement] DES003 - All applications for DKT customers, of which at least one resource must not be accessible to everyone, I set up Login.
* proof expected in comments : framing note link
- **Level:** Level 1 | **Topic:** Design
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** **DES003 Access Right Management**

[Wiki - DES003 Access Right Management](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460389/DES003+Access+Right+Management)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-OPR004-ApplicationSecurityLogging] I use alcatrace if i have to handle personnal data
- **Level:** Level 2 | **Topic:** Operate/Monitor
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### Why ?
Data protection is a matter that is getting more and more sensitive nowdays, especially whenever it concerne people's informations.
Likewise RGPD in Europe, many countries have their own regulation.
Check the following sites for further details : [CNIL (fr)](https://www.cnil.fr/fr/la-protection-des-donnees-dans-le-monde) & [UNCTAD (en)](https://unctad.org/page/data-protection-and-privacy-legislation-worldwide#:~:text=137%20out%20of%20194%20countries,in%20only%2048%20per%20cent.)
If we want to make business in those countries we need to conform with those reglementations, else we would risk huge fines that could jeopardize our business model.

Alcatrace is a Decathlon's IT project that aim to address in a centralized place many of those data protection problematics.

### What ?
In a nutshell, fullfiling this requirement takes to send a log to Alcatrace each time a Personal Data is created, modified or deleted in any components of software.

You can find futher details regarding this project on the following Decathlon's Wiki pages and / or sites :
- [The Alcatrace wiki page](https://wiki.decathlon.net/display/SEC/SOC+-+ALCATRACE)
- [The XCommerce's security team digest about Alcatrace](https://wiki.decathlon.net/display/XCOM/Alcatrace)
- [The Alcatrace site](https://sites.google.com/oxylane.com/alcatrace/accueil)

### How ?
The team must be able to demonstrate that all its software components comply with Alcatrace requirements
At best, all Personal Data CRUD manipulation will be managed in a dedicated component, in order to centralize and automatize the log sending to Alcatrace, and ease the auditing of this criteria
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-REL002-SecureArtifactManagement] Wiz is setup in my CI
- **Level:** Level 1 | **Topic:** Operate/Monitor
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### Why ?
Knowledge is power.
Being able to solve your vulnerabilities require first to know to which ones you are exposed.

### What ?
Altough there is a shift left trend on that matter, a first good place to monitor that is in your CI.
Add this extra Wiz check step after each ones that produce an artifact !
This will enable your team to be proactive on that matter, and to fix troubles before a Sec Ops ask for it for ASAP :)
Notice that Dependabot is a good sidekick to adding a Wiz step in your CI, but it can't replace it because Wiz scan performed in your CI are also a way to feed our Security teams with metrics.

### How ?
Wiz ship scanners that can be applied on produced artifacts.
For example a CI producing Docker images can use [this Dktunied Github Action](https://github.com/dktunited/.github/blob/main/actions/Wiz/action.yml) in order to have a vulerability report added to your Pull Requests
To estimate that your team reached this maturity level, it must to able to show that each of its PR's artifacts are subject to a Vulnerability scan
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-REL002-SecureArtifactManagement] Wiz issues are reviewed and prioritized in the project backlog
- **Level:** Level 3 | **Topic:** Operate/Monitor
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### Why ?
Checking your vulnerabilities at CI time is good first step, but far far from been enough :
A vulnerability can be discovered month after your last CI run produced and delivered an artifact in production
This is the main reason why having yout team animating itself on a regular basis regarding its artifacts' vulnerabilities is a must have.

### What ?
Choose the metric you'll rely on to animate your review.
Right now it's , but it can evolve : stay up to date with the last official way to check it !
Choose an adapted review frequency and perform it
Analyse each reported troubles, with the help of your Sec Ops if necessary, and decide :
- if they are relevant (some false positives can sneak in)
- how to remediate them
- have a deadline recorded if you decide to fix it
- create the corresponding tasks in your backlog
- if you think it's not worth fixing it, make a CAB to validate your choice with your Sec Ops.

### How ?
Your team should be able to present its review minutes, including in each of them the references to metrics that have been considered, which decisions have been made, why, and the references to either the corresponding JIRA or CAB
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-REL002-SecureArtifactManagement] CI fail if a Wiz issue is detected
- **Level:** Level 5 | **Topic:** Operate/Monitor
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### Why ?
Having the Wiz scan's reports added as comments on your PR's is nice, but let's face it, you could forget to have a check on it.
And it would sad to miss an opportunity to make things better from a security point of view, especially once you have relatively clean artifacts produced.

### What ?
The point of this quality criteria is to turn the PR's Wiz comment into real quality gates.
Have your team choosing a criticy level you don't allow to be shipped without at least have been warned as a quality gate failure
Modify your CI in order to have this new quality gate triggered accordingly
Notice : the goal is not to prevent you from delivering a hot fix whenever necessary, but to help you making choises with the right information level. If it's more critical for the business to pass an hot fix before remediating to a vulnerability, use your administrator rights and manage the vulnerability in a second step, or at least don't forget to keep track of this task in your backlog

### How ?
Your team should be able to demonstrate that each of its CI producing artifacts subject to Wiz scan had a related quality gate configured
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-ORG001-RiskAssessment] ORG001 - I filled my security assement in SSOT with my SO ?
* it's mandatory rule
* proof expected in comments : "cyber critical level", "IDP UUID"
- **Level:** Level 1 | **Topic:** Organisation
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** **ORG001 Risk Assessment**

[List of SO](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197459980/Organisation+and+contact)

/!\ : SSOT is only accessible to SO in write mode
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-ORG003-SecurityChampion] ORG003 - My application is known and followed by my SO ?
* it's mandatory rule
* proof expected in comments : "names" of SO in comment
- **Level:** Level 1 | **Topic:** Organisation
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** **ORG003 Security Champion**

[List of SO](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197459980/Organisation+and+contact)

[Wiki - ORG003 Security Champion](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460601/ORG003+SecurityChampion)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-ORG001-RiskAssessment] ORG001 - I identified a Security Champion for my application in SSOT?
* it's mandatory rule

- **Level:** Level 2 | **Topic:** Organisation
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** **ORG001 Risk Assessment**

[List of SO](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197459980/Organisation+and+contact)

/!\ : the applimap file is only accessible to SO

[Wiki - ORG001 Risk Assessment](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197463253/ORG001+RiskAssessment)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-ORG003-SecurityChampion] ORG003 - My application is monitored by a Security Champion and one of the team members has security responsibility for the application?
* it's mandatory rule
* proof expected in comments : "names", "names" of Security Champion and team member
- **Level:** Level 4 | **Topic:** Organisation
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** **ORG003 Security Champion**

[List of SC](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460154/Security+Champion+List)

[Wiki - ORG003 Security Champion](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460601/ORG003+SecurityChampion)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-ORG003-SecurityChampion] ORG003 - My application is monitored by a Security Champion, one of the team members has security responsibility for the application and the application is under DevSecOps?
* it's mandatory rule
* proof expected in comments : "DevSecOps dashboard link
- **Level:** Level 2 | **Topic:** Organisation
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** **ORG003 Security Champion**

To put an application under DevSecOps control, you have to go through an Onboarding process accompanied by a Security Champion.

[Wiki - ORG003 Security Champion](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460601/ORG003+SecurityChampion)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-REQ003-SecurityUserStoriesandAcceptanceCriterias] REQ003 -Security user stories and abuse stories template are defined and used.
* it's mandatory rule
* proof expected in comments "Jira Dashboard Link"
- **Level:** Level 4 | **Topic:** Requirement
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** **REQ003 Security User Stories and Acceptance Criterias**

[How to write an abuse story](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460383/REQ003+Security+User+Stories+and+Acceptance+Criterias)

[Wiki - REQ003 Security User Stories and Acceptance Criterias](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460383/REQ003+Security+User+Stories+and+Acceptance+Criterias)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-REQ003-SecurityUserStoriesandAcceptanceCriterias] REQ003 - Security use and misuse cases are defined as feature's acceptance criteria.
- **Level:** Level 4 | **Topic:** Requirement
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** **REQ003 Security User Stories and Acceptance Criterias**

[Wiki - REQ003 Security User Stories and Acceptance Criterias](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460383/REQ003+Security+User+Stories+and+Acceptance+Criterias)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-SAAS001-SaaSAssessment] I followed the SaaS Assessment Cybersecurity
- **Level:** Level 1 | **Topic:** Requirement
- **BMAD Step:** Step 03 - Architecture
- **Constraint:** **SAAS001 SaaS Assessment**

[SaaS Assessment Cybersecurity Sourcing](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460520/SaaS+Assessment+Cybersecurity+Sourcing)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-TEST001-SecurityTestManagement] TEST001 - The staging environment is different from production environment and doesn't contain production data with the exception of data used for the proper functioning of the application (config, parameters, administration) and data that is already public (store opening hours, list of items, countries, postal codes, etc.)
- **Level:** Level 1 | **Topic:** Test
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **TEST001 Security Test Management**

[Wiki - TEST001 Security Test Management](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460397/TEST001+Security+Test+Management)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-TEST004-PenetrationTesting] TEST004 - Pentests are performed at the frequency defined by the Application Vulnerability Management Framework. (evidence: links to the pentest request)
Vulnerabilities resulting from the pentest are tracked in a tool.
* proof expected in comments : Links to Application Vulnerability Centralization Tool
- **Level:** Level 1 | **Topic:** Test
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **TEST004 Penetration Testing**

[Wiki - TEST004 Penetration Testing](https://docs.google.com/document/d/19TOgPcbvQHC7fmfpJhS1UxHG4CHAaDmBmgfNM5GL38A/edit?tab=t.0)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-TEST001-SecurityTestManagement] TEST001 - The staging environment is identical to the production environment on the scope of the entire application (infrastructure and code) and test data can be shared.
- **Level:** Level 2 | **Topic:** Test
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **TEST001 Security Test Management**

[Wiki - TEST001 Security Test Management](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460397/TEST001+Security+Test+Management)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-TEST001-SecurityTestManagement] TEST001 - The staging environment is identical to the production environment on the scope of the entire application and all applications on which it depends (infrastructure and code) and test data can be created on-demand.
- **Level:** Level 3 | **Topic:** Test
- **BMAD Step:** Step 05 - Testing
- **Constraint:** **TEST001 Security Test Management**

[Wiki - TEST001 Security Test Management](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460397/TEST001+Security+Test+Management)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---
