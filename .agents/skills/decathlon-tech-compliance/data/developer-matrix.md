# 💻 FULL DEVELOPMENT ACTIVE MATRIX (Decathlon)

> **INSTRUCTIONS POUR L'AGENT :**
> 1. Référentiel complet des exigences DEVELOPMENT SIG.
> 2. Chaque point doit être validé selon le Step BMAD indiqué.
> 3. En cas de non-conformité, l'agent doit lever une alerte ou proposer une remédiation.

---

### [#0-A000-CPTTIIMD-6735efe1] Tracking is implemented. Tracking events are sent to the collector.
- **Level:** Level 1 | **Topic:** Analytics
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
Avoid external tracking solution that are not compliant with local regulation or the product radar.
### What ?
For example, you can integrate the [Clickstream API and tools](https://decathlon.atlassian.net/l/cp/JmrN5cwg)
### How ?
Getting started with [Clickstream front integration for developers](https://decathlon.atlassian.net/l/cp/mDoUwFY0)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-A000-EDLVADFW-9f863adf] Variables for your tracking system are documented.
- **Level:** Level 2 | **Topic:** Analytics
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
Documentation should make easier to maintain and debug the tracking events and the data layer content for external tiers or new onbording developers.
### What ?
Each tc_vars properties should be documented with the input datasource, and typing/formating information of the values.
### How ?
Create a dedicated wiki page where the tc_vars properties are listed and documented.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-A000-TEEADLVA-57cbecd4] Tracking elements are included in non regression tests.
- **Level:** Level 3 | **Topic:** Analytics
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### Why ?
Tracking regression are very usual in front application, we should ensure that each application change are not impacting the reliability of the produced data.
### What ?
Each tracking event should be part of the front application test suite with dedicated tests of the datalayer variables and data integrity check.
### How ?
Automated unit test before each deployment. Tests should be implemented for each component for each use cases.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-A000-TROTCLPT-a8d967e5] APIs are not used directly from the client application.
- **Level:** Level 4 | **Topic:** Analytics
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### Why ?
The clickstream APIs are regulary evolving and the library will ensure some backward compatibility with future APIs evolutions.
 The library is also ensuring some data integrity check to avoid some unexpected usage of the tracker.
### How ?
See (Front integration for developers)[https://decathlon.atlassian.net/l/cp/t1Xuigc6] documentation on the Clickstream wiki.

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-A000-TEHIIBOT-99d3e822] Tracking error handling is implemented based on the application observability.
- **Level:** Level 3 | **Topic:** Analytics
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
To identify potential issue on front end related to the tracking integration.
### How ?
Use your observability system to log front application errors with dedicated categories for tracking.

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-A000-ASITDTWA-e78fc812] Alerting system inform the dev team when an event or a data layer variable is not correct.
- **Level:** Level 5 | **Topic:** Observability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
To reduce the mean time to detect (MTTD) and reduce the data loss.
### How ?
Use your observability system (Datadog is recommended) and configure alerting on tracking errors.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-A000-PAAROQPA-44f1043b] * Public API are registered on QuAPI portal
* API contracts (Swagger/OpenAPI) are part of the code base
* A depreciation policy is defined and followed, with all breaking changes logged and communicated
- **Level:** Level 3 | **Topic:** API
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
* All public APIs must be exposed by APIM gravity to guarantee security, reliability, centralization, life cycle. etc...
* API will move over the time, new versions or evolution will come. To ensure the quality of our API and avoid breaking changes all consumers must review the change.
* You must have a docAPI with your openapi/swagger, it will enable your consumers to obtain all the information on your API.

### What ?
To fulfill this requirement:
* all projects have to declare their API in the quality portal.
* you must communicate to your consumer all the change from your API through a release note for example. Do not forget to update our docAPI.
* your swagger must be uploaded to the repository in which your docAPI is located. We can use the [docAPI template](https://github.com/dktunited/apim-docapi-template). You should also tag deprecated endpoints, if you want more information follow [best-practices-for-deprecating-apis](https://swagger.io/blog/api-strategy/best-practices-for-deprecating-apis/).


### How ?
* Using the QuAPI Portal : [https://quapi.decathlon.net/register](https://quapi.decathlon.net/register)
* The team must be able to demonstrate that the strategic communication is applied when releases new API version.
* In QuAPI you must validate the first criteria of design (D01) and be able to demonstrate that the deprecated strategy is well implemented in your openapi/swagger.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-A00000-AMEAAA-03bb5fb0] Public API are registered on QuAPI portal
- **Level:** Level 1 | **Topic:** API
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
All public APIs must be exposed by APIM gravity to guarantee security, reliability, centralization, life cycle. etc...


### What ?
To fulfill this requirement, all projects have to declare their API in the quality portal.

### How ?
Using the QuAPI Portal : [https://quapi.decathlon.net/register](https://quapi.decathlon.net/register)

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-A000-ACARBC00] API changes must be logged and communicate to your consumers the breaking changes
- **Level:** Level 2 | **Topic:** API
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
API will move over the time, new versions or evolution will come. To ensure the quality of our API and avoid breaking changes all consumers must review the change.

### What ?
To fulfill this requirement, you must communicate to your consumer all the change from your API through a release note for example. Do not forget to update our docAPI.

### How ?
The team must be able to demonstrate that the strategic communication is applied when releases new API version.

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-A000-ACSAPOTC] * API contracts (Swagger/OpenAPI) are part of the code base
* Depreciation policy is described and respected for each public API
- **Level:** Level 3 | **Topic:** API
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
You must have a docAPI with your openapi/swagger, it will enable your consumers to obtain all the information on your API.
* Endpoints
* Versioning / Deprecating
* Inputs / Outputs
* Samples

### What ?
To fulfill this requirement, your swagger must be uploaded to the repository in which your docAPI is located. We can use the [docAPI template](https://github.com/dktunited/apim-docapi-template). You should also tag deprecated endpoints, if you want more information follow [best-practices-for-deprecating-apis](https://swagger.io/blog/api-strategy/best-practices-for-deprecating-apis/).

### How ?
In QuAPI you must validate the first criteria of design (D01) and be able to demonstrate that the deprecated strategy is well implemented in your openapi/swagger.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-A000-CFPIAOEP] Contract First pattern is applied on each public API
- **Level:** Level 4 | **Topic:** API
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
Contract First are a software development technique claims that openapi/swagger should be written first before writing any code. Advantages of this approach can be listed as:
* Reusability
* Separation of concerns
* Good and consistent communication between teams
* Easy documentation
* Consistent API models

### What ?
To fulfill this requirement, you must implement the contract first by using openapi generator plugin.

### How ?
The team must be able to demonstrate the implementation of the contract first through a dedicated solution.

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-A000-ACIFT000] API Contract is fully tested
- **Level:** Level 4 | **Topic:** API
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### Why ?
Leverage the contract first approach to provide automated testing of your API contract.
### What ?
API contract informations could be verified automatically to prevent contract regression by leveraging test tooling.
### How ?
We recommend to integrate (schemathesis)[https://schemathesis.readthedocs.io/en/stable/] in your CD pipeline, but you could also rely on a collection of POSTMAN requests or other testing technologies that prevent regressions on API edge cases.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-A000-PTHBIADO] Pen test has been implemented and documented on your API.
- **Level:** Level 4 | **Topic:** API
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
 Conduct and document a penetration test on your API.
 ### Why
 To identify and address security vulnerabilities, ensuring the API is secure against attacks.
 ### How
 Engage a professional penetration testing team or use automated tools to perform the test. Document the findings, implement necessary security improvements, and maintain records for future reference.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-A000-FAUCAPMP] For AI/ML use case, API  python module provide a way to store api calls (inputs and outputs) and feedback loop implementation.
- **Level:** Level 4 | **Topic:** API
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
 The API Python module should offer functionality to log API calls, including inputs and outputs, and implement a feedback loop mechanism.
 ### Why
 To enable monitoring, auditing, and continuous improvement of the AI/ML models by capturing real-world usage data and user feedback.
 ### How
 Implement logging mechanisms in the API to record inputs and outputs. Use databases or storage solutions like PostgreSQL, MongoDB, or cloud storage services to store this data. Integrate feedback loop capabilities to collect and utilize user feedback for model retraining and improvement.
Ex. Datadog and specific endpoint for feedback loop.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-A000-FAUCAPII] For AI/ML use case, API provide interpretability insights of predictions.
- **Level:** Level 4 | **Topic:** API
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 The API should offer insights into the interpretability of its predictions, making the decision-making process transparent and understandable to users.
 ### Why
 To build trust with users, ensure compliance with ethical and regulatory standards, and facilitate informed decision-making.
 ### How
 Integrate interpretability tools such as SHAP or LIME into the API. Provide endpoints that return interpretability information alongside predictions. Document the interpretability methods and how to access them via the API.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-A00000-CSAIYW-d2a40b60] A System Design document exists
- **Level:** Level 1 | **Topic:** System Design Documents
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
 The purpose of the system design file is to describe your product in various aspects: business, technical... This document must be initialized in the first phase of the product and updated with each new product phase.

### What ?
To fulfill this requirement, create the document in github repository or on the a wiki page on the Decathlon's Confluence instance must be created by duplicate the existing template : [System Design Template](https://decathlon.atlassian.net/wiki/spaces/ENGINEERING/pages/184948248/System+Design)

### How ?
The team must be able to demonstrate that a wiki page based on the template is completed, with the technical architecture schemas expected
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-A00000-CCDWOS-694a58ae] The system design must contain diagrams using C4 format with level 1 and 2
- **Level:** Level 2 | **Topic:** System Design Documents
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
To know what is your dependencies with other (Decathlon) services and identify impact of a potential incident, a component diagram is very important for your project. Also these diagrams are very useful to quickly understand the architecture of the application.

### What ?
To fulfill the requirement, the team must present a wiki page, a web page from an external SaaS service or a C4 model hosted in a GitHub repository with all their dependencies. Don't forget to link it to the System Design document.

### How ?
You can use SaaS tools like [Draw.io] (https://www.diagrams.net/blog/c4-modelling) but if you want to use an « as code » solution, you can use C4 model with [Structurizr DSL] (e.g.: https://github.com/dktunited/dkt-retail-cartographie). If you are interested to use the « as code » solution but you don’t have a place to write your diagram, please contact the SIG Mobile members to help you.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-A00000-SDUTD0-1ca55cf5] System design documents are up to date with a regular review on each major release
- **Level:** Level 2 | **Topic:** System Design Documents
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### Why ?
 The purpose of the system design file is to describe your product in various aspects: business, technical... This document must be initialized in the first phase of the product and updated with each new product phase.
It will help any newcomer and people that need to work with your application to understand the platform and help you to check that any important requirement of Decathlon is met (security, disaster recovery, cost ...).

### What ?
To fulfill this requirement, a wiki page on the Decathlon's Confluence instance must be created by duplicate the existing template : [System Deisgn Template] (https://decathlon.atlassian.net/wiki/spaces/ENGINEERING/pages/184948248/System+Design)

### How ?
The team must be able to demonstrate that a wiki page is available and up to date.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-A000-SDDIACAE-117652ad] System Design documents include API consumers, stream data and external software components dependencies in the C4 diagrams
- **Level:** Level 3 | **Topic:** System Design Documents
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** "### Why ?
To know what is your dependencies with other (Decathlon) services and identify impact of a potential incident, a component diagram is very important for your project. Also these diagrams are very useful to quickly understand the architecture of the application.

### What ?
To fulfill the requirement, the team must present a wiki page, a web page from an external SaaS service or a C4 model hosted in a GitHub repository with all their dependencies. Don't forget to link it to the System Design document.

### How ?
You can use SaaS tools like [Draw.io] (https://www.diagrams.net/blog/c4-modelling) but if you want to use an « as code » solution, you can use C4 model with [Structurizr DSL] (e.g.: https://github.com/dktunited/dkt-retail-cartographie). If you are interested to use the « as code » solution but you don’t have a place to write your diagram, please contact the SIG Mobile members to help you."
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-A000-SDDAAACA-f07f681c] System design documents are using Markdown, versioned in a Git repository  and referenced in the IDP

- **Level:** Level 4 | **Topic:** System Design Documents
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
It has to be easy to identify system design changes, and thus to be able to identify differences between one version and another

### What ?
To fulfill this requirement, you have to store diagrams as code in a single repository for your business unit / business domain, using the Decathlon's standard tool (which could be [plantuml](https://plantuml.com/fr/), [structurizr](https://structurizr.com/) or [mermaidjs](https://mermaid.js.org/))

### How ?
The team must be able to demonstrate that a git repository exists and contains all business unit / business domain C level diagrams as code
The business unit / business domain wiki page has to refer to git repository
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-SDD0-SDDIDDAC-3008ae89] System design documents include deployment diagrams as code including the infrastructure layout
- **Level:** Level 4 | **Topic:** System Design Documents
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
It has to be easy to identify system design changes, and thus to be able to identify differences between one version and another

### What ?
To fulfill this requirement, you have to store diagrams as code in a single repository for your business unit / business domain, using the Decathlon's standard tool (which could be [plantuml](https://plantuml.com/fr/), [structurizr](https://structurizr.com/) or [mermaidjs](https://mermaid.js.org/))

### How ?
The team must be able to demonstrate that a git repository exists and contains all business unit / business domain C level diagrams as code
The business unit / business domain wiki page has to refer to git repository
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-A000-SDIGTACP] Software documentation is generated through a CI process from code assets
- **Level:** Level 5 | **Topic:** System Design Documents
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
A good documentation is up-to-date documentation. Update the software documentation in the CI to be as close as possible to the codebase changes.

### What ?
Integrate an open-source plugin in the CI to generate the doc-as-code.
They are no official Decathlon recommendations for the moment.

### How ?
Add this new step as a github action in your CI to generate the documentation assets in your project.

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-A000-ADRAAFIA] Architecture Decision Records (ADR) are hosted in a single place and reviewed by peers
- **Level:** Level 2 | **Topic:** Architecture Decision Record
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
 An architecture decision record (ADR) is a document that captures an important architectural decision made along with its context and consequences. It is important because the people who took the decisions may not be still on the project some years after the decisions have been taken, and the new developpers may make new decisions that will break the design of the application because of the lack of information regarding the previous choices made.

### What ?
To fulfill this requirement, create and store your ADR in your application git repo, then create a macro in the wiki pages of the project to display them. Template can be found here : [ADR template](https://decathlon.atlassian.net/wiki/spaces/ENGINEERING/pages/184950621/Architecture+Decision+Record+ADR+-+Template)

### How ?
The team must be able to demonstrate that ADRs are present in the repository and a wiki page is available pointing to these records.
Peers can be teammate outside of your team. Staffs and EMs should be included when the impact is bigger than just a team.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-A000-ADRAFTMF-9ba07237] Architecture Decision Records (ADR) are present in a github repository and displayed in the component page of IDP
- **Level:** Level 3 | **Topic:** Architecture Decision Record
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
It has to be easy to compare ADRs one with another, and to be able to identify differences between one version and another

### What ?
To fulfill this requirement, create and store your ADR in your application git repo.

### How ?
The team has to update records for every change on previous decisions

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-A000-ANADRAFT-72f18d3a] All new Architecture Decision Records (ADR) follow the MADR standard
- **Level:** Level 4 | **Topic:** Architecture Decision Record
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ###Why ?
Markdown Architectural Decision Records (MADR) give a template fo structure the documents and rely on Markdown format to simplify edition/visualisation directly on Github.

### How ?
You could get more information on the [MADR website](https://adr.github.io/madr/)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-A000-ADRFABUA-31618acc] Cross domain or cross project Architecture Decision Records (ADR) are stored in a mutualized git repository
- **Level:** Level 5 | **Topic:** Architecture Decision Record
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
ADRs may impact more than one component at a domain / business unit level

### What ?
To fulfill this requirement, create and store your ADR in your business unit / business domain git repo, then use [MADR template](https://adr.github.io/madr/)

### How ?
Ensure every impacted component repository is identified
Ensure every impacted component refers to you business unit / business domain git ADR repository

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-A000-CMDIR000] Create modular diagram (if relevant)
- **Level:** Level 2 | **Topic:** Software Design
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
 When you’ve a new comer in your team or if you want to improve your modular strategy, it is important to write your modular diagram to discuss about any improvements or to communicate with your team members what is the current modular strategy to follow.
### What ?
To fulfill the requirement, the team must present a wiki page with the modular diagram. It will be completed in a next level to write your modularization strategy.
### How ?
You can use SaaS tools like Miro or Figma but if you want to use an « as code » solution, you can use Mermaid compatible with GitHub or our Wiki to describe your modular diagram.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-TR00-ACFBT000] Avoid callbacks for background tasks
- **Level:** Level 3 | **Topic:** Software Design
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
In programming, callback hell refers to an ineffective way of writing asynchronous code. It takes place when you nest functions and create too many levels of nesting. This makes it harder to control access to the specific function and it becomes harder to debug the issues. Nesting means placing functions in another ones. By placing callback in a callback logic might get too messy.

### What ?
To fulfill this requirement, more modern ways to work with background/async code must be used like suspend method, combine framework, async/await framework, etc.

### How ?
The team must be able to demonstrate that they do not use callback for background tasks.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-A000-CMSDIYW0] Create modularization strategy document in your wiki
- **Level:** Level 3 | **Topic:** Software Design
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
 According to the complexity of your modular diagram, it can be difficult to understand it well and know exactly what is the responsibilities of each module in your application. The modularization strategy explain all concepts included in your diagram.
### What ?
To fulfill the requirement, the team must present a wiki page with your modular diagram completed with the strategy.
### How ?
Explain all concepts in your wiki page, potential rules to follow in the dependencies between your modules and what is the responsibilities of each kind of module.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-TR00-UDITASCD] Using dependency injection to avoid strong coupling dependencies
- **Level:** Level 4 | **Topic:** Software Design
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### Why ?
Strong coupling between your dependencies is a bad pattern in all applications (not only for mobile apps). Using a dependency injection will help your team to avoid this bad pattern.
### What ?
To fulfill the requirement, you should add Dependency Injection library in your project, use it in all layer of your architecture and everywhere (including in your legacy code).
### How ?
Check the Techradar to know which dependency injection has been referenced for your mobile platform and start to use it in your mobile project after a first learning in the official documentation if necessary.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-A000-AARTAATJ-8921b1a3] Access and/or Refresh Tokens are accessible to JavaScript
- **Level:** Level 2 | **Topic:** Authentication
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What?
(Disclaimer: if you're implementing a new frontend application and are looking at the best practice, please consider implementing the level 2 and skip level 1).

One of the most widely used way of storing tokens is through APIs accessible by the JavaScript.
Applications that are storing tokens this way are exposed to Cross Site Scripting (XSS) attacks.

### Why?
If you use localStorage for persisting access tokens and an attacker manages to run foreign JavaScript code within your application, the attacker can exfiltrate any tokens and call APIs directly.
Moreover, XSS also allows attackers to manipulate data in the local storage of the application, meaning attackers can change the token.

Note that data in local storage is stored permanently, which means that any tokens stored there reside on the file system of the user’s device (laptop, computer, mobile or other) and are accessible to other applications even after the browser is closed.

### How?
The tokens are stored in one of the followings browser Web APIs:
- Web Storage API (LocalStorage, SessionStorage)
- IndexDB
- any other web APIs accessible to Javascript
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-A000-AARTASAH-0fb6db89] Access and/or Refresh Tokens are set as HTTP Only Cookies
- **Level:** Level 3 | **Topic:** Authentication
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What?
One of the most widely used way of storing tokens is through APIs accessible by the JavaScript.
Applications that are storing tokens this way are exposed to Cross Site Scripting (XSS) attacks.
Use Cookies to store your tokens instead, but bear in mind that they must be configured correctly to limit the number of security vulnerabilities.

### Why?
Cookies are pieces of data that are stored in the browser. By design, the browser adds cookies to every request to the server. Therefore, an application must use cookies with caution. If not configured carefully, a browser may append cookies with cross-site requests and allow for cross-site request forgery (CSRF) attacks.

Cookies have attributes that control their security properties. For example, the SameSite attribute can help to mitigate the risk of CSRF attacks. When a cookie has the SameSite attribute set to Strict, the browser adds it to requests that originate from and target the same site as the site of the cookie’s origin. The browser will not add cookies when requests are embedded in any third-party site, like via links.

You can set and retrieve cookies via JavaScript. However, when using JavaScript to read cookies, the application becomes vulnerable to XSS (in addition to CSRF). Therefore, the preferred option is to have a backend component that sets the cookie and marks it as HttpOnly. That flag mitigates leaking data through XSS attacks because it indicates to the browser that the cookie must not be available via JavaScript.

To prevent cookies from leaking via a man-in-the-middle attack, which may lead to session hijacking, cookies should only be sent over encrypted connections (HTTPS). To instruct the browser to only send cookies in HTTPS requests, a cookie must have the Secure attribute set.

### How?
Set the following properties when sending to the browser a cookie creation order:
SameSite=Strict
Secure
HttpOnly

`Set-Cookie:token=myvalue;SameSite=Strict;Secure;HttpOnly`
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-A000-AARTAEAS-2dd922c9] Access and/or Refresh Tokens are encrypted and set as HTTP Only Cookies
- **Level:** Level 4 | **Topic:** Authentication
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What?
Encrypt tokens and store them into the cookie storage with HTTPOnly and secure options enabled.

### Why?
Previous levels allow to limit man-in-the-middle and XSS vulnerabilities but don't limit the risks of replay attacks outside the application.
Indeed a leaked token can be injected into a wide range of services exposed by Decathlon.

For instance, a token leaked on a mobile app could be used to hit a completely different app.
And the way the authentication system is build (avoid SPOF by distributing its public key) makes this possible.
If the stolen token happens to have sufficient scope accreditations it could authenticate malicous api calls.

Encrypting a pair of Access and Refresh tokens allows to limit the impact to the service that delivered them.
Replay attacks injecting stolen tokens won't work on other services.

### How?
First encrypt the Access and Refresh tokens.
Then set the following properties when sending to the browser the cookie creation order:
SameSite=Strict
Secure
HttpOnly

`Set-Cookie:token=myvalue;SameSite=Strict;Secure;HttpOnly`
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-A000-AARTANET-a0355e9a] Access and Refresh Tokens are not exposed to the end user.
- **Level:** Level 5 | **Topic:** Authentication
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What?
Store the access and refresh tokens in a server-side memory storage and map the access token with a random session identifier stored in the cookie storage.

### Why?
The previous level still allows temporary session theft through the theft of the access token (encrypted or not) as the access token can't be revoked.
In order to prevent this vulnerability and to be fully compliant with the OAuth2 specification, access and refresh tokens must be kept confidential among the resource server (the API), the client (the front-end application) and the authorization server (FedID or Member).

### How?
First, store the access and refresh tokens in a server-side memory storage (like Redis) available to the BFF.
Create a session identifier (session ID) using a Cryptographically Secure Pseudorandom Number Generator (CSPRNG) like [crypto.randomBytes()](https://nodejs.org/api/crypto.html#crypto_crypto_randombytes_size_callback).
Map the session ID with the access and refresh tokens.
Set the following attributes when sending the cookie to the browser:
+ SameSite=Strict
+ Secure
+ HttpOnly
+ Max-Age=$(lifetime of the access token in seconds)
When sending requests from the BFF to an API, use the access token to authenticate the user against the API.
When the cookie expires, get a new access token with the current refresh token. If the refresh token is invalid, redirect the user to the login flow.
If the user disconnects themselves, delete the tokens and the session identifier from the server-side memory storage.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-B000-YPIAAEWK-fe68193e] Your ADRs should contain one ADR which explains which kind of BFF your application implements.
- **Level:** Level 3 | **Topic:** BFF
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why?
There are several types of Backend For Frontends (BFF).
The traditional concept is about introducing a backend service dedicated to a frontend application, whose responsability is to build tailor made responses.
To do so, BFF will have to orchestrate one or several calls to backend APIs and cherry pick relevant data to be forwarded to the frontend app.

Since the early days of that design pattern, the industry moved on and many frameworks and libraries blurred the lines between BFFs and Server Side Rendering (SSR) techniques/tools.

### What?
Write an ADR providing the full rationale behind the choice and reasons for implementing a BFF. Especially regarding the BFF archetype you picked (CSR or SSR types).
More info on the [archetypes here](https://decathlon.atlassian.net/wiki/x/gwTLGQ).

### How?
Store this ADR in the same place as you would store any other ADR concerning your product.


- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-B000-FIABIPBA-669f7417] [For internal apps] Your BFF is placed behind a Firewall
- **Level:** Level 4 | **Topic:** BFF
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### Why?
Exposing a service to the web represents a risk that must be mitigated.
In order to do so, protect your BFFs by placing the WAF in front of them.

### What?
WAFs' managed rules offer advanced zero-day vulnerability protections.
Core OWASP rules block familiar “Top 10” attack techniques.
Custom rulesets deliver tailored protections to block any threat.
WAF Machine Learning complements WAF rulesets by detecting bypasses and attack variations of RCE, XSS and SQLi attacks.
Exposed credential checks monitor and block use of stolen/exposed credentials for account takeover.
Sensitive data detection alerts on responses containing sensitive data.
WAF content scanning protects your web servers and enterprise network from malware by scanning files uploaded to your application in-transit.
Advanced rate limiting prevents abuse, DDoS, brute force attempts along with API-centric controls.
Flexible response options allow for blocking, logging, rate limiting or challenging.

### How?
Please consult the infra tech radar attached documentation under Firewall, CDN, WAF (Cloudflare in 2024).

### Who?
"Internal apps" are applications intended to be used by Decathlon teammates.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-B000-FEABIPBT-56a261a4] [For external apps] Your BFF is placed behind the APIm
- **Level:** Level 4 | **Topic:** BFF
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### Why?
- The Web Application Firewall (WAF) comes out of the box (Cloudflare in 2024)
- Prevents DDoS attacks
- Allows rate limiting (limits the blast radius effect)
- Handles TLS and ceritificates
- Canary deployment Active-active easier with the APIm
- Consumers Identification (BFF should be mutualized as soon as same logic has to be implemented 3 times or more, APIm helps spotting routes and data consumption)
- Multi-domain (without the APIm a new dedicated domain name must be found for each BFF resulting in accidental complexity in the frontend app aka handling CORS)

As long as your BFF acts only as a proxy (resend the traffic to another API) and those API check the JWT, then I did not enforced to put the BFF behind the Gateway, avoiding useless north/south internet roundtrip (~35ms latency).

But if your BFF evolves, the risk is to add business logic or to proxify calls to unsecure endpoints after you took the decision, opening a breach in the information system.

Having your BFF behind an APIM Gateway and with a correct security control is a way to ensure long term security. But at a cost of latencies and APIM traffic cost.

If you're using a server side rendering engine or any meta framework that uses the server ( eg: server actions, rendering etc ), this is not required.

### What?

Register your BFF into the APIm.
Route your traffic to the APIm.


### How?
Depending on the type of BFF used, 1 or 2 plans can be used:
1. A public plan for static resources (Server Side Rendered or Client Side Rendered HTML, CSS, JS bundles etc.)
2. A private plan for the BFF private API routes

For use cases where performances are mandatory, please consider the following points:
- The API Gateway adds 50 to 70 ms latency (North-South)
- If you witness more latency have a look at the North-South vs East-West traffic
Frontend application should hit the Gateway once, which will then route the query to the BFF.
From that point the BFF should query other data sources and APIs through the East-West Gateway (and microGateways).
It'll save a lot of time and latency not to go back on internet and keep local traffic local (aka intra cluster).

Please consult the Tech Radar's current API Management/Gateway solution for complete documentation.

### Who?
"External apps" are applications intended to be used by Decathlon customers.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-DS00-UOADSLVW-1a5e9639] Usage of any Design System libraries of Vitamin Play Web
- **Level:** Level 2 | **Topic:** Design System
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why?
The incorporation of Design System libraries is essential for ensuring consistency, scalability, and efficiency in engineering products. By utilizing [Vitamin Play Web](https://github.com/dktunited/vitamin-play-web) libraries, we aim to establish a unified visual language and interaction patterns across our products, fostering a seamless user experience.

If you want to know why do we create a new implementation of our Design System called Vitamin Play, please refer to our [website](https://www.decathlon.design).

### What?
Our Design System libraries [Vitamin Play Web](https://github.com/dktunited/vitamin-play-web), encapsulate a set of pre-designed UI components, styles, and guidelines.
These resources empower development teams to maintain a cohesive design language, streamline development efforts, and enhance collaboration between design and engineering.

### How?
To integrate these Design System libraries into our engineering products, teams should follow the comprehensive documentation provided. This includes importing the necessary components, adhering to styling guidelines, and staying updated with any library enhancements. Regular collaboration with the design team ensures alignment with the overall product vision and consistent implementation of design principles.

For more detailed information, you can refer to the documentation on the usage of [Vitamin Play Web](https://github.com/dktunited/vitamin-play-web).
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DS00-UOVPWLDS-200af8b8] Usage of any Design System libraries of Vitamin Play Web + one of the three component libraries available (React, Svelte or Vue)
- **Level:** Level 3 | **Topic:** Design System
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why?
The incorporation of Design System libraries is essential for ensuring consistency, scalability, and efficiency in engineering products. By utilizing [Vitamin Play Web](https://github.com/dktunited/vitamin-play-web) libraries, we aim to establish a unified visual language and interaction patterns across our products, fostering a seamless user experience.

If you want to know why do we create a new implementation of our Design System called Vitamin Play, please refer to our [website](https://www.decathlon.design).

### What?
Our Design System libraries [Vitamin Play Web](https://github.com/dktunited/vitamin-play-web), encapsulate a set of pre-designed UI components, styles, and guidelines.
These resources empower development teams to maintain a cohesive design language, streamline development efforts, and enhance collaboration between design and engineering.

### How?
To integrate these Design System libraries into our engineering products, teams should follow the comprehensive documentation provided. This includes importing the necessary components, adhering to styling guidelines, and staying updated with any library enhancements. Regular collaboration with the design team ensures alignment with the overall product vision and consistent implementation of design principles.

For more detailed information, you can refer to the documentation on the usage of [Vitamin Play Web](https://github.com/dktunited/vitamin-play-web).
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DS00-UOVPWLDS-200af8b8] Usage of any Design System libraries of Vitamin Play Web + one of the three component libraries available (React, Svelte or Vue) + follow the guidelines (do/don't, etc.) from https://decathlon.design
- **Level:** Level 4 | **Topic:** Design System
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why?
The incorporation of Design System libraries is essential for ensuring consistency, scalability, and efficiency in engineering products. By utilizing [Vitamin Play Web](https://github.com/dktunited/vitamin-play-web) libraries, we aim to establish a unified visual language and interaction patterns across our products, fostering a seamless user experience.

If you want to know why do we create a new implementation of our Design System called Vitamin Play, please refer to our [website](https://www.decathlon.design).

### What?
Our Design System libraries [Vitamin Play Web](https://github.com/dktunited/vitamin-play-web), encapsulate a set of pre-designed UI components, styles, and guidelines.
These resources empower development teams to maintain a cohesive design language, streamline development efforts, and enhance collaboration between design and engineering.

### How?
To integrate these Design System libraries into our engineering products, teams should follow the comprehensive documentation provided. This includes importing the necessary components, adhering to styling guidelines, and staying updated with any library enhancements. Regular collaboration with the design team ensures alignment with the overall product vision and consistent implementation of design principles.

For more detailed information, you can refer to the documentation on the usage of [Vitamin Play Web](https://github.com/dktunited/vitamin-play-web).
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-DS00-UOVPWLDS-200af8b8] Usage of Vitamin Play Web libraries (Design System) with an engineering adoption score > 40%
- **Level:** Level 5 | **Topic:** Design System
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why?
The incorporation of Design System libraries is essential for ensuring consistency, scalability, and efficiency in engineering products. By utilizing [Vitamin Play Web](https://github.com/dktunited/vitamin-play-web) libraries, we aim to establish a unified visual language and interaction patterns across our products, fostering a seamless user experience.

If you want to know why do we create a new implementation of our Design System called Vitamin Play, please refer to our [website](https://www.decathlon.design).

### What?
Our Design System libraries [Vitamin Play Web](https://github.com/dktunited/vitamin-play-web), encapsulate a set of pre-designed UI components, styles, and guidelines.
These resources empower development teams to maintain a cohesive design language, streamline development efforts, and enhance collaboration between design and engineering.

### How?
To integrate these Design System libraries into our engineering products, teams should follow the comprehensive documentation provided. This includes importing the necessary components, adhering to styling guidelines, and staying updated with any library enhancements. Regular collaboration with the design team ensures alignment with the overall product vision and consistent implementation of design principles.

For more detailed information, you can refer to the documentation on the usage of [Vitamin Play Web](https://github.com/dktunited/vitamin-play-web).
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-A00000-IHALCT-55b15faf] * Logs are stored in a single collector (Datadog, Google Cloud Logging, Splunk) without redondancy
* Logs retention is managed with relevance in all environnements (prod, staging ...), they are stored on cold storage if a longer retention policy if mandatory
- **Level:** Level 1 | **Topic:** Observability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
Logging is generate important FinOps cost and we should optimise the storage and indexation of the logs to enable troubleshooting capabilities in a single tool.

### What ?
Ensure that the application and infrastructure  logs are collected in a single log tool (Datadog, Google Cloud Logging, Splunk ...) and avoid multiple storage.

No matter the tool and the infrastructure considered, the team should have a single UI to use in order to access all of its components logs
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-Q000-SCMIYA00] Setup crash monitoring tool in your application
- **Level:** Level 1 | **Topic:** Observability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
>Crash monitoring is very important to understand the stability of an app which is deployed in production. It saves troubleshooting time by intelligently grouping crashes and highlighting the circumstances that lead up to them. According to the usage and the capabilities of the tool used, fatal and no fatal issues may be monitored. These tools allow software engineers to follow a very important KPIs for the stability of the app like:
* Crash-free users which is the percentage of users that have not experienced a crash in the given timeframe
* Crash-free sessions which is the percentage of total sessions that have not resulted in a crash in the given timeframe.

### What ?
To fulfill this requirement, a crash monitoring (such as Firebase Crashlytics) must be lived in the production binary and must monitor at least fatal issues.

### How ?
The team must be able to demonstrate that a crash monitoring tool has been implemented in the source code of the application and that data are correctly logged into a dedicated dashboard in order to be able to read some information like:
* stacktrace
* app version
* device details
* Crash-free user rate
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-O000-STSCTOHC-4a84b8cc] Setup telemetry SDK (dkt-otel) configured to observe http calls
- **Level:** Level 1 | **Topic:** Observability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
### Why ?

### What ?
Can be either Datadog Mobile SDK (if you need advanced features like RUM), Opentelemetry otherwise

### How ?

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-O000-STAIP000-b85134a9] Synthetic tests are in place.
- **Level:** Level 1 | **Topic:** Observability
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### Why ?
Being blind is not acceptable. Having synthetic tests will permit to have a feedback on what's runnnig into your production.

### What ?
The goal is to simulate real users that will request your app. It should permit to see runtime errors that impact your users. The requests should have a minimum checks (at least on status code) to ensure the answered page is correct for your users.

### How?
- Use the Tech Radar's Observability Monitoring tool under the ADOPTED status.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-O000-RUMIU000-c8c17a76] Real User Monitoring is used.
- **Level:** Level 2 | **Topic:** Observability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
To understand the user experience in real-time. Identify performance issues and frustrations.
Make data-driven decisions and foster a culture of continuous enhancement.

### What ?
- Error Stack Traces
- Metrics & Alerting
- Session replays
- Frustration events (Heatmaps)

### How?
- Use the Tech Radar's Observability Monitoring tool under the ADOPTED status.
- Integrate RUM scripts into applications and Collect and aggregate data with user consent.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-O000-TLIIIMCI-62d3a41d] Tracing library is implemented in my code, in addition to logs.
- **Level:** Level 2 | **Topic:** Observability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
To gain detailed visibility into the flow and performance of individual requests across your system, beyond what logs alone can offer for debugging and optimization.

### What?
Your codebase is instrumented with a library that automatically or manually creates and reports traces and spans, capturing the execution path and timing of operations.

### How?
You've integrated a tracing SDK (like OpenTelemetry or datadog agent) into your application code to generate and send trace data to a backend (datadog, ... ) for visualization and analysis.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-A00000-IHALRP-80388741] Logs retention is managed with relevance in all environnements (prod, staging ...), they are stored on cold storage if a longer retention policy if mandatory.

- **Level:** Level 2 | **Topic:** Observability
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### Why ?
It's twofolded :
On one hand, developpers can sometimes get wild regarding log production

No matter the relevency of such a practice, it can quickly lead to :
- at best a disk space exhaustion ... that most certainly an OPS will complain about sooner or later ;)
- at worst an expensive bill, whenever the log storage is externalized on a SAAS solution, like Datadog.

On the other hand, your logs can contains valuable informations. For example :
- in order to perform post mortem analysis
- to keep track of which IP accessed your web server when

In such a case you'll want to make certain that you keep track of a certain time frame of logs.

As you can see, if you don't make things clear, you can get caught between the hammer and the anvil !

### What ?
Addressing the retention problematic necessitate :
- To have your team clearly specify
    - which logic it wants to apply regarding its past, present and future log retention policy definition
    - which functional requirements and financial constraints should be taken into account to do so.
- Choose current log retention accordingly
- Apply this retention on the centralized tool it use

### How ?
- The team should pocess an up to date document that specify this policy
- It should be able to easily check that its actual log retention is configured accordingly
- For example, log storage is limited to 7 days (Datadog) or 30 days (Splunk and GCL)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-O000-TARM0000-38e6f549] Traces and retention management
- **Level:** Level 2 | **Topic:** Observability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why?
Efficiently managing the volume and lifespan of trace data is crucial for controlling storage costs and ensuring relevant information is available for analysis and troubleshooting.

### What?
You have policies and processes for determining the volume of traces that are ingested and indexed, to have to proper amount of traces vs the cost

### How?
This involves configuring retention periods in your observability tool (datadog, ...).
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-Q000-CCMTPLWC] Configure crash monitoring SDK to push logs for every crashs
- **Level:** Level 2 | **Topic:** Observability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
Pushing logs with your crashs give you more context and can help you to identify its root cause.
### What ?
To fulfill this requirement, configure a logger compatible with crash monitoring tools to centralized all your logs and implement the way to push your logs when you are in release mode.
### How ?
For Android, you can use library as Timber to log what you want and if your BuildConfig said that you are in release mode, use Crashlytics library to push your logs.
For iOS, you can directly use Crashlytics library where you want to push your log message but we recommend to develop an abstraction if you want to be compatible with multiple Crashlitics platforms and don’t push logs in debug mode.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-Q000-CCMTPCUS] Configure crash monitoring tool to push pertinent custom keys (user id, country, etc.) for every crash
- **Level:** Level 2 | **Topic:** Observability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
Pushing custom keys with your crashs give your more context about the device configuration, the users and the specific context of your app. But take care about GDPR rules and equivalents for other countries.
### What ?
To fulfill this requirement, you should reuse your implementation to publish your logs in Crashlytics platform but add your custom keys.
### How ?
For Android, in your Timber implementation to publish your logs, add your custom keys before the push.
For iOS, in your abstraction layer of Crashlytics platforms, add your custom keys before the push.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-Q000-SCRBBVDR] Split crash reports by build variants (debug, release, etc..)
- **Level:** Level 2 | **Topic:** Observability
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### Why ?
At the minimum, all mobile applications have two variants: Debug and Release. You shouldn’t publish your crashs to Crashlytics platform at the same place for all your variants to know if it is a crash in production or in development.
### What ?
Some mobile projects can have more than two variants: beta phase, TNR phase, QA phase, etc. It depends the project and feature teams. So it is important to know in which version come from your crash when you work on their resolution.
### How ?
Use a package id (Android) or bundle id (iOS) adapted to your variant to give this information to the Crashlytics platform. They will split your crashs for you according to this id if you pre-configured your Crashlytics platform first.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-O000-CTSTPPCK-1c7d786d] Configure telemetry SDK (dkt-otel) to push pertinent custom keys (user id, country, etc.)
- **Level:** Level 2 | **Topic:** Observability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
### Why ?

### What ?

### How ?

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-O000-CTSTPLAS-c9e0c2a5] Configure telemetry SDK (dkt-otel) to push logs as span attached to a trace
- **Level:** Level 2 | **Topic:** Observability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
### Why ?

### What ?

### How ?

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-O000-CTSTTPI0-08045630] Configure telemetry SDK (dkt-otel) to track performance issues
- **Level:** Level 2 | **Topic:** Observability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
### Why ?

### What ?

### How ?

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-O000-IYHABSTS-0604e0af] If you have a BFF, setup telemetry SDK configured to observe http request received
- **Level:** Level 2 | **Topic:** Observability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
### Why ?

### What ?

### How ?

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-O000-LLIRTEAW-ed2813dd] Log level is restricted to ERROR and WARN for dev/staging/production environments, DEBUG and INFO usages are deprecated and should be replaced by tracing/APM tools
- **Level:** Level 3 | **Topic:** Observability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
The Application Performance Management tools take the observability of your system one step beyond.
In a nutshell, they aim to gather in one place all information it can gather about it, and propose several advanced tools based on collected metrics, such as :
- end to end tracing of a user's action.
- AI powered monitoring & alerting of the health of the whole system
- support of your own SLI / SLO definition, in order to turn them into metrics and eventually alerts whenever they are not fullfiled
- time series & multidimentional oriented analysis dashboards, I.E. can relate thru time your logs, technical & functional metrics
- log centralization & searching
- etc

Although it comes at a (financial) cost, it can greatly enhance your capacity to quickly analyze any kind of trouble.

### What ?
- Choose your APM tool. Right now Datadog is available in Decathlon tech radar. You can also rely on OpenTelemetry as a standard format for traces.
- Choose on which system components to activate it.
- Have thoses system components instrumented with it
- Have your team trained in the use of your APM's UI : it can sometime get overwhelming the first time you see it ;)
- Configure your SLI / SLO
- Configure customized dashboards
- Configure alerts based on collected metrics.
- Have those alerts redirected to a dedicated Slack channel

### How ?
Your team must be able to demonstrate that :
- An APM tool is configred on key part of the system it's running
- Your Devs and / or Production Experts are familiar with the usage of the APM's UI
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-O000-LPIDWIU0] Log level usages is documented in the project dev guidelines
- **Level:** Level 2 | **Topic:** Observability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
Being able to address problems in criticity order is a smart move.
But doing so require first that each developpers in your team uses the same "criticity scale" definition !

### What ?
Your team should aggree on the way it want to define its logs criticity level scale, and write it down in a policy document.

You can get inspiration from [this Medium article](https://medium.com/@edouard.cattez/the-art-of-talkative-application-489f03bd89f4) for example, and adapt it to your team's functional specificites.

It will serve as a reminder for each team members, and as a guideline regarding log production for newcomers.

And, to a certain extent, you can also include in this document extra log related information, such as :
- which rules have to be applied regarding the choice of log level that has been activated in each of your environments : production / qualification / preproduction / pic / etc
- specify the various kind of logs your code can produce whenever you need to distinguish them. For exemple, access logs / code logs / alcatrace logs / logs enabling kpi & dashboard productions

### How ?
The team must be able to :
- present an up to date version of this document
- demonstrate that each of its developers knows this document & is familiar with the policy it describes
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-O000-AYDO0000-cb584c20] Are your dashboards optimized?
- **Level:** Level 3 | **Topic:** Observability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why?
A dashboard is a tool for visually tracking, analyzing, and displaying key performance metrics, which enable you to monitor the health of your infrastructure.


### What?
Dashboards are on a grid-based layout, which can include a variety of objects such as images, graphs, and logs.
They are commonly used as status boards or storytelling views which update in realtime, and can represent fixed points in the past. They are used for monitoring and debugging.

### How?
Timeboards have automatic layouts, and represent a single point in time—either fixed or real-time—across the entire dashboard. They are commonly used for troubleshooting, correlation, and general data exploration.

Screenboards are dashboards with free-form layouts which can include a variety of objects such as images, graphs, and logs. They are commonly used as status boards or storytelling views that update in real-time or represent fixed points in the past.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-Q000-0OECASTF] Configure crash monitoring tool to report controlled error as non fatal
- **Level:** Level 3 | **Topic:** Observability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
Crash are one of the most important thing to monitor for mobile applications and Crashlytics platform report them automatically but there are some cases where you catch by yourself errors and implement a deteriorated scenario for your usecase. These exceptions should be catch as non fatal error and publish to Crashlytics platform to investigate why you need to use the deteriorated scenario.
### What ?
To fulfill the requirement, all your try/catch inside your mobile application should publish the exception as non fatal error to the Crashlytics platform or should be tagged as an ignored exception.
### How ?
Improve your Crashlytics abstraction to handle non fatal error to catch this kind of exception.
Otherwise, name your exception variable "ignored" to inform team members that you want to ignore this specific exception and add a comment to explain why.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-O000-CTSTMRT0-91133045] Configure telemetry SDK (dkt-otel) to measure performance
- **Level:** Level 3 | **Topic:** Observability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
### Why ?

### What ?

### How ?

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-O000-CTSTRCEA-77382eb0] Configure telemetry SDK (dkt-otel) to report controlled error as event
- **Level:** Level 3 | **Topic:** Observability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
### Why ?

### What ?

### How ?

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-O000-TAEWFDTA-9c71d2a5] Traces are enriched with functional data that are relevant for the process
- **Level:** Level 4 | **Topic:** Observability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why?
Adding business-specific context to traces provides deeper insights into the "what" and "why" behind performance and behavior, enabling more meaningful analysis and targeted troubleshooting.

### What?
Relevant business information (like user IDs, order numbers, product IDs, etc.) is attached as tags or attributes to spans within the traces.

### How?
Application code is modified to extract and inject this functional data into the tracing context as spans are created or processed. This step depends on which tools you are using (open Telemetry https://opentelemetry.io/docs/zero-code/java/spring-boot-starter/annotations/  or  Datadog  https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/java/dd-api / ...)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-O000-RIAUTCAS-103af676] RUM insights are used to compute a SLI for you main user journey
- **Level:** Level 4 | **Topic:** Observability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
The best measure point for SLOs are the ones closest to your users, aka their devices.

### What ?
You have an SLI that measures the global availability of your process, and the SLI is the ratio of complying sessions, based on your criteria

### How ?
* [How-to](https://decathlon.atlassian.net/wiki/x/QoIHd)
* [TechDay talk to have more context and see an MVP](https://drive.google.com/file/d/1_etTwErH5aT4hn0Amw31vxgnz-WdqTH6/view?usp=sharing)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-Q000-MBCCHCTT] Main business code calculation have custom trace to measure processing time
- **Level:** Level 4 | **Topic:** Observability
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### Why ?
Observability platform allows you to measure the processing time on specific code with custom traces. It helps your team to know if your code is optimized or not for a specific use case.
### What ?
To fulfill the requirement, your domain layer should be monitored with custom traces for new code and legacy code.
### How ?
Check the Techradar to know which observability library you should use to write your custom trace in your codebase and add them at the domain layer of your mobile architecture. If you want, you can create sub trace in your data layer to identify exactly which request or algorithm take too much time.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-O000-ACDNCAMI-c3207a1a] Standard application logs are phased out in favor of natively instrumented traces (eg: OpenTelemetry). Manual instrumentation is limited to enriching traces with business attributes
- **Level:** Level 5 | **Topic:** Observability
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### Why ?
To achieve focused observability and streamlined troubleshooting by directly tracking request flow and performance through distributed tracing (APM), minimizing the noise and management overhead of traditional application logs.

### What ?
The application code intentionally omits manual instrumentation and standard logs, relying primarily on automatically generated or strategically placed traces and the analytical capabilities of an Application Performance Monitoring (APM) system for understanding application behavior and resolving issues.
Troubleshooting relies on distributed tracing and APM metadata rather than manual logs. Application-specific logs are strictly reserved for non-functional requirements (audit, security, compliance), while business context is injected directly into trace spans

### How ?
Your application use a tracing libraries and APM agents. You did configure them to capture request lifecycles and performance metrics, while explicitly avoiding the inclusion of general-purpose logging statements in the core codebase (with specific exceptions for critical audit trails).
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-P000-PAIP0000-fa1f1790] Performance assessment is performed
- **Level:** Level 1 | **Topic:** Performance
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
Minimum perfomance assessment is crucial for any frontend application to ensure optimal user experience. It improves application usability and satisfaction.

### What ?
Manually measure page load times, page rendering speed, and network efficiency.
Identify and resolve performance bottlenecks.

Metrics to pay attention are the [Web Core Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals).

### How ?
Use mannual ad hoc tooling like the devtools within your browser (no automatized included).
Follow techniques such as code minification, image compression, and caching strategies.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-P000-PAAIP000-4f51b953] Performance assessment automatized in Production
- **Level:** Level 2 | **Topic:** Performance
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
Ad hoc manual performance assessments are a good start but aren't enough.
Performance must be continuously assesed especially on production environments.

There are 2 main objectives here:
- Monitor and analyze the user experience quality
- Measure the impact of freshly released new features

### What ?
Gather frontend performance metrics in an automated fashion.

### How ?
Use the Tech Radar's Observability Monitoring tool under the ADOPTED status.

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-P000-PAAITC00-0d099896] Performance assessment automatized in the CI

- **Level:** Level 3 | **Topic:** Performance
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** Performance assessment automatized in the CI

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-P000-BICPMA00-dcd2e26e] Best in class performances measured automatically

- **Level:** Level 4 | **Topic:** Performance
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
Decathlon aims at becoming a Tech Giant.
To do so, among many other things, applications must reach the industry standards, especially in terms of User eXperience performance.

### What ?
Core Web Vitals is a set of metrics that measure real-world user experience for loading performance, interactivity, and visual stability of the page.
We highly recommend site owners achieve good Core Web Vitals for success with Search and to ensure a great user experience generally.
This, along with other page experience aspects, aligns with what this core ranking systems seek to reward.

### How ?
Use the Tech Radar's Observability Monitoring tool under the ADOPTED status.
Metrics to pay attention are the [Web Core Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals).
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-SC00-CRHODGOW-1bfaf981] * Code repository hosted on dktunited GitHub org with all requirements (topics, description, etc.).
* README file in the repository
* .gitignore file to skip all local build files
* Admin permissions on the repository are given to a team and not individually
* Every Pull Request triggers a code review
- **Level:** Level 1 | **Topic:** Source Control
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-SC00-NSSBPTTR] No Secrets should be pushed to the repo.
- **Level:** Level 1 | **Topic:** Source Control
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
Private keys shouldn't appear in the repo
### What
git-crypt is the recommended tool in the Tech Radar to encrypt secrets
### How
https://medium.com/@sumitkum/securing-your-secret-keys-with-git-crypt-b2fa6ffed1a6

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-SC00-SCWID000] * Source control workflow is documented
* Commit comments and branch naming are using a documented convention
* Source code formating is documented with a common IDE setup for the team
- **Level:** Level 2 | **Topic:** Source Control
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
* Sharing the git workflow between all members of a team helps to align the way work is done.
This concerns the technical management of the repository (e.g. creation of feature branches, merge in main etc.) but also the management of the product / project (e.g. after the creation of a tag, the version will go into production).
‍* Using conventions allows better collaboration across committers.
It also makes the most of git utilities: with normalized commits, it's easier to work with history and commands and automation are easiez (generate changelog ...)
* Sharing a configuration for format code is important to automatically respect the formatting conventions. It reduces discussions around conventions, in Pull request reviews ...

### What ?
* A documentation based on a diagram and/or explanations.
Ex: (https://www.atlassian.com/git/tutorials/comparing-workflows)[https://www.atlassian.com/git/tutorials/comparing-workflows]
* In a team, a convention for commit comments and branch naming must be defined.
* If you can, use an IDE agnostic tool like prettier, editorconfig etc. You can use an IDE specific configuration too.

### How ?
* Add documentation directly on repository (or if not possible in another medium), through, for instance, an ADR (Architecture Decision Record).
* Choose a convention and document it as an ADR in the repo or at least in the readme.
Ex: for commits, you can use [conventionnal commits](https://www.conventionalcommits.org/en/v1.0.0/) or a simpler way like just start with jira ticket number.
* Use and share configuration in repository. Document usage
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-SC00-CCABNAUA] Commit comments and branch naming are using a documented convention
- **Level:** Level 2 | **Topic:** Source Control
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
‍Using conventions allows better collaboration across committers.
It also makes the most of git utilities: with normalized commits, it's easier to work with history and commands and automation are easiez (generate changelog ...)

### What ?
In a team, a convention for commit comments and branch naming must be defined.

### How ?
Choose a convention and document it as an ADR in the repo or at least in the readme.
Ex: for commits, you can use [conventionnal commits](https://www.conventionalcommits.org/en/v1.0.0/) or a simpler way like just start with jira ticket number.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-SC00-SCFIDWAC] Source code formating is documented with a common IDE setup for the team
- **Level:** Level 3 | **Topic:** Source Control
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
Sharing a configuration for format code is important to automatically respect the formatting conventions. It reduces discussions around conventions, in Pull request reviews ...

### What ?
If you can, use an IDE agnostic tool like prettier, editorconfig etc.
You can use an IDE specific configuration too

### How ?
Use and share configuration in repository. Document usage
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-SC00-RNAGAFEP] Technical release notes are generated automatically for each production release
- **Level:** Level 3 | **Topic:** Source Control
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
Having defined release notes help your consumers/users (production leaders, OPS, ...) to know about when and what have been released in the past to communicate about technical changes.

### What ?
A generated release note.

### How ?
Generate a changelog, release note github ... via CI
Ex:
https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-SC00-PALISOTP] Code formatting is setup on the project and applied in the CI
- **Level:** Level 2 | **Topic:** Source Control
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
To ensures that the formatting is respected to prevent merge conflict and improve efficiency of code review.

### What ?
Formatting/linting the code automatically in CI.

### How ?
Configure the formatting / linting steps (depends on the language / technology used) in the repository and then configure the CI to run it.

### Examples
 * (Editor config plugin)[https://editorconfig.org/]

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-SC00-DYFSROP0] Do you follow Frontend SIG recommendation on Prettier?
- **Level:** Level 3 | **Topic:** Source Control
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
To ensures that the formatting is respected and is the same for all projects
### What ?
Formatting defined by SIG
### How ?
Follow https://decathlon.atlassian.net/wiki/spaces/TO/pages/1356824904/Prettier+configuration
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-SC00-CHIPOTCR] Commit history is part of the code review for each branch

- **Level:** Level 4 | **Topic:** Source Control
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### Why ?
Git history is the first code documentation: intentions, explanations ...
So having a clean history is important to share information on the code.

### What ?
Practice to rewrite history & and verify it on code review

### How ?
Team members should use interactive rebases to rewrite and clean history.
On a pull request review, we should verify that the history is clean.
We can add this notion in the "Definition of Done" (github template or other method).
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-SC00-HADASWTT-c756f803] Hooks are documented and shared with the team
- **Level:** Level 4 | **Topic:** Source Control
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD

### Why ?

### What ?

### How ?

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-T00000-OPFND0-588f0d99] * Onboarding process for new developers
* Development setup could be performed in less than 1 day included in the onboarding documentation
- **Level:** Level 1 | **Topic:** Team
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### Why ?
Onboarding process is necessary in order to reduce the amount of time an engineer will spend in the learning and adaptation bracket. The aims:
* Quicker integration in order to have software engineers that ship production code faster.
* Consistency in the produced code with the existing code practices of the team
* Reduce turnover (for internals): Software Engineers who have a great onboarding experience tend to stay with the company longer.

### What ?
To fulfill this requirement, an onboarding process must be defined for the project, through a dedicated documentation/platform, such as:
* Heyteam
* Wiki page / Checklist

### How ?
The team must be able to demonstrate that an onboarding process exists and can be applied
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-T00000-CFTEHT-81782d15] Contributing file to explain how to contribute to your project from external team
- **Level:** Level 3 | **Topic:** Team
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
A contributing file is a guideline to external contributers to know how to process to submit contribution to the project.

### What ?
To fulfill this requirement, the [CONTRIBUTING.md](http://contributing.md/) file should be filled in and at the root of the Github repository.
* Write code of conduct [template from Github](https://github.com/dktunited/mpe-documentation/blob/main/docs/contributing/code_of_conduct.md)
* Write [CONTRIBUTING.md](https://github.com/dktunited/mpe-documentation/tree/main/docs/contributing) should be in your root directory
* Add the licence : [License Decathlon](https://github.com/dktunited/.github/blob/main/LICENSE.md)

### How ?
The team must be able to demonstrate that a [CONTRIBUTING.md](https://github.com/dktunited/mpe-documentation/tree/main/docs/contributing) file exists in the repository and that all requirements are filled and up-to-date.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-T00000-NDMSUI-11df7a8e] Development setup could be performed in less than 1 day included in the onboarding documentation
- **Level:** Level 2 | **Topic:** Team
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### Why ?

The way a new developer starts to work with his new machine is a very important process. A development environment complex to set up can be very demotivating since a newcomer may be uncomfortable to ask for help repetitively, he/she probably will try to prove his capacities by being autonomous.
Also, in case the team occasionally needs to ask an expert about an issue with the application, the setup process should be easy and quick to avoid losing too much time with the step with no added value.

### What ?
To fulfill this requirement, an new operating development environment should be setup in less than 1 hour. For instance, these could be the steps for a typical project:
* install the tools/software: programmation language(s) in the correct version(s) (Java, JavaScript, Python...), building tools (Maven, npm...), other tools (docker...)
* configure accounts on services appropriately (Google Cloud Provider, Github...)
* get the code base (from github)
* automatically configure environment if needed, with scripts
* initialize a development app (database...)
* explanation on "How to test that the environment is correctly setup" (Postman collection with a key use case for an API, scenario for a front-end application...)

### How ?
The team must be able to provide documentation and scripts demonstrating that a new software engineering is able to start to an operating development environment in less than 1 hour.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-TR00-NTSWFOOT] All New languages, frameworks, data engineering solutions (database, messaging, and cache solutions) with status WATCH, FORBIDDEN or outside Tech Radar, are being processed to become a standard (Ongoing Standard Proposal Process) or being migrated (Action plan and Budget defined)
- **Level:** Level 1 | **Topic:** Tech Radar
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
Standardization helps us be more efficient by providing better support on reduced scope of technical solutions, reduce risks by not using unwanted or unsecure solutions, and accelerate at scale by developping product easily exportable and deployable (more compatible with everyone landscape). We aim to create synergy !

### What ?
First, we want to ensure all non-compliant technical solutions are identifed on your scope (you are aware of them) and that you have an action plan (standardization or migration) to reach better compliance.

### How ?
The team must be able to demonstrate that all technical solutions are :
- existing in the [Tech Radar](https://airtable.com/appWhu5K3NTs5XURY/pagyttV838v5dvazI) under the status ADOPT, TRIAL or ON HOLD,
- not existing in the [Tech Radar](https://airtable.com/appWhu5K3NTs5XURY/pagyttV838v5dvazI) or under the status WATCH or FORBIDDEN but are part of a standard proposal process or identified as to be migrated in the product roadmap.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-TR00-0OLUHTRA-f609126c] 100% of languages, frameworks, data engineering solutions (database, messaging, and cache solutions) used have the ring ""ADOPT"" or ""ON HOLD"" in the Tech Radar.
- **Level:** Level 2 | **Topic:** Tech Radar
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
Standardization makes us more efficient by narrowing down technical solutions, minimizing risks from insecure options, and accelerating scalability through easily exportable and deployable products. The goal is to create synergy!

### What ?
We want to ensure all the languages are compliant (ADOPT or ON HOLD) without exceptions. Cf. Tech Radar.

### How ?
The team must be able to demonstrate that all the languages used exist in the Tech Radar under the status ADOPT or ON HOLD.
100% of my On Hold Technical Solutions are identified (Action Plan and Migration cost assessment)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [1-TR00-DYUT0000] Prefer Typescript for JS stacks
- **Level:** Level 2 | **Topic:** Tech Radar
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
TypeScript enhances code quality and maintainability by introducing static typing, which reduces runtime errors and improves developer productivity. It also fosters better collaboration through clear interfaces and strong tooling support. By standardizing on TypeScript, we ensure consistency, scalability, and long-term maintainability in our JavaScript stacks.

### What ?
We aim to ensure that all JavaScript-based projects prioritize TypeScript as the default choice, leveraging its benefits for reliability, scalability, and developer experience.

### How ?
All new JavaScript projects must default to TypeScript unless a strong, justified exception is provided.
Existing JavaScript projects should have a migration plan toward TypeScript, assessing feasibility and benefits.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-TR00-0ODESDMA-8b5e0bd9] 100% of languages, frameworks, data engineering solutions (database, messaging, and cache solutions) used have the ring ""ADOPT"" in the Tech Radar.
- **Level:** Level 3 | **Topic:** Tech Radar
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
Standardization helps us to be more efficient by providing better support on reduced scope of technical solutions, reduce risks by not using unwanted or unsecure solutions and accelerate at scale by developping product easily exportable and deployable (more compatible with everyone landscape). We aims to create synergy !

### What ?
We want to ensure that databases, messaging, cache solutions have the status ADOPT in the Tech Radar.

### How ?
The team must be able to demonstrate that all databases, messaging, cache solutions used exist in the Tech Radar under the status ADOPT.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-TR00-DYUTISM0] Do you use Typescript in strict mode ?
- **Level:** Level 4 | **Topic:** Tech Radar
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### Why ?
The strict flag enables a wide range of type checking behavior that results in stronger guarantees of program correctness.
Turning this on is equivalent to enabling all of the strict mode family options.
You can then turn off individual strict mode family checks as needed.

Future versions of TypeScript may introduce additional stricter checking under this flag, so upgrades of TypeScript might result in new type errors in your program.
When appropriate and possible, a corresponding flag will be added to disable that behavior.

### What ?
The strict mode can either be set with the strict alias (CF: How section) or be incrementally added.
`strict` is an alias which represents the following list of flags:

allowUnreachableCode
allowUnusedLabels
alwaysStrict
exactOptionalPropertyTypes
noFallthroughCasesInSwitch
noImplicitAny
noImplicitOverride
noImplicitReturns
noImplicitThis
noPropertyAccessFromIndexSignature
noUncheckedIndexedAccess
noUnusedLocalsnoUnusedParameters
strictBindCallApply
strictFunctionTypes
strictNullChecks
strictPropertyInitialization
useUnknownInCatchVariables

### How ?
To enable the strict mode you have 2 options:
1 - [One Shot] In your project's tsconfig.json configuration file, set the compilerOptions `strict` value to true.
2 - [Iterative] In that same file manually add one at a time each options listed in the `What ?`section, compile your app with that new flag and fix any type error you might have.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-Q000-PTRDOAR0] Process to review dependencies obsolescence and/or relevance
- **Level:** Level 4 | **Topic:** Tech Radar
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### Why ?
Software development changes very fast and it's very important to be up-to-date as much as possible in order to avoid security issues and be able to use latest features in a project. To be sure to be up-to-date, it's important to be able to monitor dependencies obsolescence.

### What ?
To fulfill this requirement, a process to review dependencies obsolescence must be implemented. It can be through the implementation of a dedicated tools like Renovate or Dependabot (check the company/tech radar compliancy).

### How ?
The team must be able to demonstrate that they have a process to review dependencies obsolescence.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-R000-GSNBEWPI-22f64c65] Graceful shutdown (no bad events when pod is terminating / rollout)
- **Level:** Level 1 | **Topic:** Reliability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
To prevent data loss and service interruptions, for example: during pod termination or rollouts.

### What?
A controlled process allowing a graceful shutdown (no bad events when termination / rollout), for example: a pod to finish tasks and disconnect gracefully before termination.

### How ?
By using lifecycle hooks (e.g., preStop) and proper signal handling  (kill -1) within the application if it is not already managed by the framework.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-R000-RTPISOMA-7dbb0bf8] Relevant timeouts policy is set on my application, across components (APIM / app / partners)
- **Level:** Level 1 | **Topic:** Reliability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why ?
To prevent cascading failures, resource exhaustion, and ensure a responsive user experience by limiting the time components wait for each other.

### What?
Establishing appropriate time limits for requests and connections between all involved systems (APIM, application, partners).

### How ?
Configuring timeout settings within each component's configuration, considering expected response times and potential network latency.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-R000-HARRPCBM-a19be02d] Have a robust Retries policy / circuit breaker mechanism
- **Level:** Level 3 | **Topic:** Reliability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why?
To improve system resilience and availability by automatically recovering from transient failures and preventing cascading failures when downstream services are unavailable.

### What?
Implementing strategies to automatically re-attempt failed requests (retries) and stop sending requests to failing services for a period (circuit breaker).

### How?
 Utilizing libraries or frameworks that provide configurable retry policies (backoff, jitter) and circuit breaker patterns (open, closed, half-open states) within your application.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-R000-IIMWIRIY-a5cb3fe0] Implement idempotency mechanism whenever it’s relevant (if your clients use retries for example)
- **Level:** Level 3 | **Topic:** Reliability
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### Why ?
To prevent unintended side effects and data corruption when clients retry requests, ensuring an operation has the same effect no matter how many times it's executed.

### What ?
 Designing operations so that multiple identical requests produce the same outcome as a single request.

### How ?
One option may be to assign or use a natural (orderId, ...) unique identifiers to requests and checking if a request with the same ID has already been processed, returning the previous result instead of re-executing.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-R000-RTOTGJWT-88778f72] Relevant timeouts on the Global journey (with the other applications on the path)
- **Level:** Level 5 | **Topic:** Reliability
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why?
To prevent a single slow or unresponsive application in the chain from causing cascading delays or failures across the entire user flow.

### What?
Defining appropriate maximum wait times for interactions between all applications involved in a complete user journey.

### How ?
Configuring timeouts at each integration point, considering the expected performance of each application and potential network latency within the overall path.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-BS00-IOBAOCIM-3f67a1ee] Initiate or be aware of content in ML Design Doc Google doc.
- **Level:** Level 1 | **Topic:** Business & strategy
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
Guideline / checklist for machine learning systems; it is not meant to be exhaustive. The intent of the design doc is to help you think better about the problem, design and solution and get feedback. Adopt whichever sections—and add new sections—to meet this goal.
### How
https://docs.google.com/document/d/1cjuA6BsRIMGjsIHjRaiST28R5z2SFtzjerqj_gsjMk0/edit?usp=sharing
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-BS00-ETTPPIAR-86db0e05] Ensure that the project, product in AI Radar / AI Inventory as json or markdown file.
- **Level:** Level 1 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### How
https://github.com/dktunited/ai-radar/tree/main
The process is automated if you are using v8.1.0 of ml code template.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-BS00-DTOABMOT-436bd096] Describe the overview and business motivation of the project.
- **Level:** Level 1 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### How
See ML Design Doc.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-BS00-UTNDTPOC-96ae844f] Understand the need - Define the project: objectives, challenges, constraints, end users (planification)
- **Level:** Level 1 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### How
Involving stakeholders : individual interviews with requestiers, understanding the need in the organization and the project
### What
Business Analysis, Prroduct vision board, DSM Alignement
### Souce
https://docs.google.com/presentation/d/1odaNArmU7XlyoKRjNt_Ppwz7tZzgJ6tK63hzLsXNdi4/edit#slide=id.g1e96518207f_0_60
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-BS00-UTNUUNCC-9e7806ba] Understand the need - Understanding user needs, constraints, context
- **Level:** Level 1 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### How
Interveiw, focus group, observation, survey
### Deliverable
User research plan, interview, focus group, survey
### Souce ?
https://docs.google.com/presentation/d/1odaNArmU7XlyoKRjNt_Ppwz7tZzgJ6tK63hzLsXNdi4/edit#slide=id.g1e96518207f_0_60
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-BS00-STVCABCO-1cd16905] Supervize the value creation and budget control of the product - I can model & test, define and follow the business model of my products or features.
- **Level:** Level 1 | **Topic:** Business & strategy
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### How
VAT (value assessemnt template can help): https://docs.google.com/spreadsheets/d/1BwHONrJiGUm4ha1-lret9YFe71VX0WyKDohB63378Is/edit?usp=drive_link
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-BS00-DSMBG000-727344a5] Define sucess metrics (business goals).
- **Level:** Level 2 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### How
See ML Design Doc.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-BS00-DTMOTPSP-c812ad2b] Detail the methodology of the project (scientific part)
- **Level:** Level 2 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### How
See ML Design Doc.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-BS00-UTNIDUDQ-1f1578e3] Understand the need - Identify data, Understand data quality, understand complexity (volume, location gold, insight, etc.)
- **Level:** Level 2 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### How
Meeting with data owners and analytics engineer if necessary
### Deliverable
Metting + notes report
### Souce
https://docs.google.com/presentation/d/1odaNArmU7XlyoKRjNt_Ppwz7tZzgJ6tK63hzLsXNdi4/edit#slide=id.g1e96518207f_0_60
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-BS00-DDSU0000-77d05cbe] Descibe data sources used.
- **Level:** Level 2 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
Enumerate the required data, their functional domain, and storage location.
### How
Conluence and/or ML Design Doc
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-BS00-DTPTCDII-ffadc382] Design the product -Transforming collected data into ideas and design solutions
- **Level:** Level 2 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### How
Co-designing workshops
### Deliverable
Brainstorming, personnas, flow charts (tasks flow, user flow, wireframe, design flow), Experience map
### Souce
https://docs.google.com/presentation/d/1odaNArmU7XlyoKRjNt_Ppwz7tZzgJ6tK63hzLsXNdi4/edit#slide=id.g1e96518207f_0_60
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-BS00-DTPFTMRD-4881d3e3] Design the product - Find the most relevant data in order to create the best product. If necessary create the missing data
- **Level:** Level 2 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### How
Finding ressources, data modeling and preparation, data quality assessment
### Deliverables
Workshop with DE, AE an/or data orwner in order to get the data necessary for the end product
### Souce
https://docs.google.com/presentation/d/1odaNArmU7XlyoKRjNt_Ppwz7tZzgJ6tK63hzLsXNdi4/edit#slide=id.g1e96518207f_0_60
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-BS00-PRUOEAMM-332803be] Plan regular update of each AI Maturity Matrix pillars
- **Level:** Level 2 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### When
Every month or quarter.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-BS00-BBRIDFMP-07bd2d87] Budget (build, run, infra) definition for my project.
- **Level:** Level 2 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### How
Monitor infrastructure and ressources needed to estimate the ROI of the project.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-BS00-MIBOMEOP-7e82cb0c] Monitor infrastructure budget of my experimentation of project
- **Level:** Level 2 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### How
Report biling Tableau (FinOps).
https://prod-uk-a.online.tableau.com/#/site/dktunited/views/ReportBilling_17031560490270/ReportBilling?:iid=1
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-BS00-STVCABCO-924887c1] Supervize the value creation and budget control of the product - I make budget forecasts & negotiate budgets.
- **Level:** Level 2 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-BS00-LTUNAECI-c7fa01a0] Listen to user needs and ensure continuous improvement of the product - I organize and prioritize the user research backlog
- **Level:** Level 2 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-BS00-LTUNAECI-aef3b67d] Listen to user needs and ensure continuous improvement of the product - I synthesize the results of the experiments and deduce the solution choices
- **Level:** Level 2 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-BS00-DTPVASIP-b7f0e63b] Define the product vision and strategy - I provide transparency and communicate the Product vision to stakeholders (formalize the vision, Objectivey the impacts and communicate)
- **Level:** Level 2 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-BS00-DTPVASIK-6a6db9bf] Define the product vision and strategy - I know how to co-construct my KR at the quarter with my team, and I animate them regularly (on a weekly basis ideally)
- **Level:** Level 2 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-BS00-MTVATTPO-4a897256] Match the vision according to the positioning of the Product on the market - I perform competitive benchmarks
- **Level:** Level 2 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-BS00-DTSIEHLD-72fb5729] Describe the solution implementation (e.g. high level design, infrastructure, data privacy, monitoring, alerts, cost estimation)
- **Level:** Level 3 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### How
ML Design Doc / solution architecture / c4model. See example in AI Framework.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-BS00-ATDRTHBC-b48942f3] A technical design review (TDR) has been conducted and a clear architecture of the AI system is defined.
- **Level:** Level 3 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### How
Schedule TDR with data platform team.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-BS00-DTPDMOP0-7fc47a96] Desgin the product - Designing mockup of prototype.
- **Level:** Level 3 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### How to
Based on the previous work, build the prototype closest to the final product, knowing which approach to take MVP or not
### Deliverable
Prototype, Kickoff meeting, slides deck
### Souce ?
https://docs.google.com/presentation/d/1odaNArmU7XlyoKRjNt_Ppwz7tZzgJ6tK63hzLsXNdi4/edit#slide=id.g1e96518207f_0_60
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-BS00-DTPVASIC-552e3545] Define the product vision and strategy - I co-construct the vision of the Product with the different teams involved on an ongoing basis (modus operandi to be followed, types of workshops, participants to be invited, deliverables, feedback templates etc.)
- **Level:** Level 3 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-BS00-DTPVASID-769cd054] Define the product vision and strategy - I define the short, medium and long term steps in the service of the product vision (Outcome Based Product Roadmap)
- **Level:** Level 3 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-BS00-DTPVASIU-a79bfadd] Define the product vision and strategy - I use the Vision to adjust the strategic axes on a daily basis
- **Level:** Level 3 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-BS00-DTPVASIH-ee10ed8f] Define the product vision and strategy - I help the organization to translate its strategic objectives into SMART tactical objectives in the product roadmap
- **Level:** Level 3 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-BS00-MTVATTPO-2e9b290b] Match the vision according to the positioning of the Product on the market - I conduct the necessary market studies (launch, product pivot or major functionalities)
- **Level:** Level 3 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-BS00-MTVATTPO-baa67d4c] Match the vision according to the positioning of the Product on the market - I can identify my customer/user segments
- **Level:** Level 3 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-BS00-MTVATTPO-dc0e67a9] Match the vision according to the positioning of the Product on the market - I build new offers or new products
- **Level:** Level 3 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-BS00-DTPOOKDP-1682f1f7] Determine the pricing of offers (know different product pricing techniques / model and test pricing hypotheses)
- **Level:** Level 3 | **Topic:** Business & strategy
- **BMAD Step:** Step 05 - Testing
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-BS00-LTUNAECI-234c7647] Listen to user needs and ensure continuous improvement of the product - I segment the uses made of the product
- **Level:** Level 3 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-BS00-RCR00000-8c1b3fdd] Risk & compliance review.
- **Level:** Level 4 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### How
Risk matrix not defined
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-BS00-STDKILGA-8521fd60] Start to define KPI in line Group AI policy (e.g. disparate impact, pdp, etc.)
- **Level:** Level 4 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### How
An example here : TODO
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-BS00-CAMTAPV0-37e8a7a5] Calculate and monitor the AI product value (€)
- **Level:** Level 4 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### How
ML Design Doc
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-BS00-DADAHSUF-d801f278] Define and describre a human-in-the-loop strategy / user feedback.
- **Level:** Level 4 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### How
ML Design Doc
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-BS00-LTUNAECI-cc36a3ef] Listen to user needs and ensure continuous improvement of the product - I maintain the user research deliverables: Personas, Journey Map, experimentation synthesis, mock-ups, ...
- **Level:** Level 4 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-BS00-ESHIACAT-d743e848] Explore solution hypothesis in a cost-effective and timely manner - I choose and prioritize the solution derisking methods adapted to each case (AB test, mock-ups, prototypes, ...)
- **Level:** Level 4 | **Topic:** Business & strategy
- **BMAD Step:** Step 05 - Testing
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-BS00-ESHIACAT-e32d1264] Explore solution hypothesis in a cost-effective and timely manner - I co-define the user research with the UX designers and researchers
- **Level:** Level 4 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-BS00-CWDTGTWI-cec74a6d] Collaborate with Designers to guide their work in designing the Product - I know how to choose between different user research methods adapted to each case (interviews, focus groups, etc.)
- **Level:** Level 4 | **Topic:** Business & strategy
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-BS00-OAE00000-d00c0a9b] Ongoing audits (external)
- **Level:** Level 5 | **Topic:** Business & strategy
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### How
An example here : TODO
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-D000-PAPTEADO-f5896c8f] Prioritise and plan the evolution and development of the Product - I organize a backlog (Features, Epics, US, tasks etc.).
- **Level:** Level 1 | **Topic:** Delivery
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-D000-PAPTEADO-0647434a] Prioritise and plan the evolution and development of the Product - I organize a backlog taking into account roadmaps and release plans.
- **Level:** Level 2 | **Topic:** Delivery
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-D000-PAPTEADO-9027b4e6] Prioritise and plan the evolution and development of the Product - I can write a functional document for my features/products
- **Level:** Level 2 | **Topic:** Delivery
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-D000-PAPTEADO-c9ecd769] Prioritise and plan the evolution and development of the Product - I understand and know how to discuss technical choices
- **Level:** Level 2 | **Topic:** Delivery
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-D000-PAPTEADO-c31a3098] Prioritise and plan the evolution and development of the Product - I understand and know how to discuss costings
- **Level:** Level 2 | **Topic:** Delivery
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-D000-GTQOTPIS-002369eb] Guarantee the quality of the product, its safety and its DRP - I ensure the protection of my product's data
- **Level:** Level 2 | **Topic:** Delivery
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-D000-HAMSTEDD-a64156dc] Have a multi skills Team (e.g. DE, DS, MLE, Ops)
- **Level:** Level 3 | **Topic:** Delivery
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### How
See Role section in AI Framework (https://ai-framework.decathlon.net/)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-D000-PAPTEADO-978e24dc] Prioritise and plan the evolution and development of the Product - I plan future developments in the short term (6 weeks) and medium term (3 months)
- **Level:** Level 3 | **Topic:** Delivery
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-D000-PAPTEADO-a6a017ef] Prioritise and plan the evolution and development of the Product - I know how to frame the features and their desired impact
- **Level:** Level 3 | **Topic:** Delivery
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-D000-PAPTEADO-df32f719] Prioritise and plan the evolution and development of the Product -I lead the writing of user stories and guarantee their functional consistency
- **Level:** Level 3 | **Topic:** Delivery
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-D000-PAPTEADO-867221a4] Prioritise and plan the evolution and development of the Product - I ensure collaboration with other teams in order to manage dependencies and adhesions
- **Level:** Level 3 | **Topic:** Delivery
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-D000-GTQOTPIS-39076eae] Guarantee the quality of the product, its safety and its DRP - I systematically validate the quality of the delivered functionalities
- **Level:** Level 3 | **Topic:** Delivery
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-D000-CTPAFPOT-75dd8b39] Communicate the past and future progress of the Product, both externally and internally to the team - I maintain periodic Sprint Reviews open to stakeholders
- **Level:** Level 3 | **Topic:** Delivery
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-D000-CTPAFPOT-defb6f29] Communicate the past and future progress of the Product, both externally and internally to the team - I conduct a roadmapping, prioritization or storymapping workshop
- **Level:** Level 3 | **Topic:** Delivery
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### How
Product vision board
### Source
https://docs.google.com/presentation/d/1odaNArmU7XlyoKRjNt_Ppwz7tZzgJ6tK63hzLsXNdi4/edit#slide=id.g29164bcac97_1_159
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-D000-DASTKSDO-948275fc] Define and supervise the key success data of the Product - Define and implement team and product success metrics
- **Level:** Level 3 | **Topic:** Delivery
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-D000-PAPTEADO-5d844097] Prioritise and plan the evolution and development of the Product - I prioritize the backlog by integrating the notion of value for the user, and I know prioritization techniques (MOSCOW, ROI, ROE, RICE, WSJF, KANO etc.)
- **Level:** Level 4 | **Topic:** Delivery
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-D000-GTQOTPIS-7da6ea7f] Guarantee the quality of the product, its safety and its DRP - I prioritize bugs and monitor the technical and functional debt
- **Level:** Level 4 | **Topic:** Delivery
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-D000-GTQOTPIS-94d7212e] Guarantee the quality of the product, its safety and its DRP - I take into account the technical tasks and integrate them into the prioritization
- **Level:** Level 4 | **Topic:** Delivery
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### How
Check with the PM
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-D000-GTQOTPIS-e3100e26] Guarantee the quality of the product, its safety and its DRP - I define and manage the product's operational excellence commitments
- **Level:** Level 4 | **Topic:** Delivery
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### How
Check with the PM
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-D000-CTPAFPOT-7ec4cea1] Communicate the past and future progress of the Product, both externally and internally to the team - I communicate on the roadmap and its progress inside and outside the team (via Release Notes)
- **Level:** Level 4 | **Topic:** Delivery
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-D000-DASTKSDO-0d46ee5e] Define and supervise the key success data of the Product - Track and monitor the right indicators for my product (e.g. traffic)
- **Level:** Level 4 | **Topic:** Delivery
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-D000-DASTKSDO-d0af3dcc] Define and supervise the key success data of the Product - I know how to build relevant dashboards adapted to the audience (Codir, Product Team etc.).
- **Level:** Level 4 | **Topic:** Delivery
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-D000-DASTKSDO-54550bb7] Define and supervise the key success data of the Product - I have advanced Dataviz (mastery of dedicated tools).
- **Level:** Level 5 | **Topic:** Delivery
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-D000-KAIUEPIK-845354b4] Know and improve user engagement paths - I know how to calculate the LTV (Life time value) of my users
- **Level:** Level 5 | **Topic:** Delivery
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### How
Check with the PM
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-D000-KAIUEPIK-157cc20e] Know and improve user engagement paths - I know how to identify the parts of my engagement journey that need improvement
- **Level:** Level 5 | **Topic:** Delivery
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### How
Check with the PM
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-D000-DDWFAUIA-1b230947] Data definition (what features are used in an ML model and what these features mean) is documented.
- **Level:** Level 1 | **Topic:** Documentation
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
Established structured notations like "datasheets for datasets" are recommended here. Yes, with structured datasheets, including detailed information on: data handling, data collector, data collection method
### How
Sphinx documentation or github (in addition to confluence).
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-D000-CCDOTPGM-3888b023] Create comprehensive documentation outlining the project's goals, methodologies, and results.
- **Level:** Level 1 | **Topic:** Documentation
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Develop detailed documentation that covers the project's objectives, the methodologies employed, and the results achieved.
 ### Why
 To provide a clear and comprehensive understanding of the project for stakeholders, facilitate knowledge transfer, and ensure transparency.
 ### How
 Use tools like Markdown, Google Docs (cf. ML Design Doc), or Confluence to structure the documentation. Include sections for project goals, detailed methodologies (data gathering, analysis, modeling), and results (key findings, metrics, visualizations). Ensure that the documentation is well-organized and easy to navigate.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-D000-SOGAACDI-b64b43af] Steps of gathering, analyzing and cleaning data including motivation for each step should be documented (e.g. part of EDA)
- **Level:** Level 2 | **Topic:** Documentation
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Document the steps involved in data gathering, analysis, and cleaning, providing the rationale for each step.
 ### Why
 To ensure reproducibility, transparency, and to provide context for the data preparation process, which is crucial for understanding the foundation of the analysis and modeling efforts.
 ### How
 Use tools like Jupyter Notebooks or a shared documentation platform to describe each step of the data preparation process. Include motivations, methods used, and any challenges encountered. Use visual aids like charts and graphs to illustrate data cleaning and EDA processes.
Markdown file or Sphinx documentation in github repository
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-D000-COMLMIDA-fbcb92a5] Choice of machine learning model is documented and justified (e.g. model tested, metrics used, etc.).
- **Level:** Level 2 | **Topic:** Documentation
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
 Document the selection process for the machine learning model, including the models tested and the metrics used for evaluation.
 ### Why
 To provide a rationale for the chosen model, demonstrating that the selection was based on systematic testing and evaluation, which helps in building trust and understanding among stakeholders.
 ### How
 Create a detailed report or section in your documentation that lists all the models considered, the evaluation metrics used (e.g., accuracy, precision, recall, F1 score), and the results of the comparisons. Justify the final choice based on these results, and include visual comparisons like performance graphs or tables.
Slides, Notebooks or documented in Sphinx technical documentation, an example here:
https://fictional-adventure-woglmk1.pages.github.io/final_report.html
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-D000-DDP00000-c3457df5] Document data pipeline.
- **Level:** Level 3 | **Topic:** Documentation
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Provide comprehensive documentation for the data pipeline, detailing each stage of the process.
 ### Why
 To ensure clear understanding, facilitate maintenance, and enable efficient troubleshooting and updates.
 ### How
 Use documentation tools like Markdown, Sphinx
Draw a diagram of steps in the data pipeline and their dependencies. Describe what append in each steps. Solution architecture can help.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-D000-SRUODDOD-13cb3ec6] Schedule regularly update of data definition or define checklist at each release (what features are used in an ML model and what these features mean).
- **Level:** Level 3 | **Topic:** Documentation
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
 Regularly update data definitions and maintain a checklist for each release that includes details on the features used in an ML model and their meanings.
 ### Why
 To ensure data consistency, improve model transparency, and facilitate communication among team members.
 ### How
 Establish a schedule for reviewing and updating data definitions. Create a checklist template to document features, their descriptions, and any changes for each release. Store these documents in a shared repository like Confluence or GitHub.
Ritual meeting or check when module is release
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-D000-GDAOCDUT-e5dc011e] Generate detailed and organized code documentation using the documentation tool.
- **Level:** Level 3 | **Topic:** Documentation
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Produce detailed and well-organized documentation for the codebase using a documentation tool.
 ### Why
 To enhance code readability, facilitate onboarding of new developers, and improve overall project maintainability.
 ### How
 Use tools like Sphinx, or MkDocs to generate documentation. Ensure that comments and docstrings are comprehensive and up-to-date. Regularly update the documentation as the code evolves and publish it in a centralized location.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-D000-DADTOAOT-76079b88] Design and document the overall architecture of the AI solution to ensure clarity and maintainability.
- **Level:** Level 3 | **Topic:** Documentation
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Create and maintain documentation of the overall architecture of the AI solution, outlining its components and their interactions.
 ### Why
 To provide a clear blueprint of the system for developers, stakeholders, and maintenance teams, ensuring ease of understanding and modification.
 ### How
 Use architectural diagram tools like Draw.io to visualize the architecture. Document each component's purpose, interactions, and data flow. Store the documentation in an accessible repository.
Solution Architecture example.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-D000-DAHROMAT-91bce7d9] Document and history report of meeting about technical choose (for modeling and deployment).
- **Level:** Level 4 | **Topic:** Documentation
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Maintain records and reports of meetings focused on technical decisions related to modeling and deployment.
 ### Why
 To ensure transparency, provide a historical reference, and facilitate informed decision-making in future developments.
 ### How
 Record meeting minutes and decisions using tools like Confluence or Google Docs. Include details on attendees, topics discussed, decisions made, and action items. Organize and store these documents chronologically.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-D000-SLAFOEMR-cdca2c84] Share limits and fairness of each model release.
- **Level:** Level 4 | **Topic:** Documentation
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Provide documentation on the limitations and fairness considerations for each model release.
 ### Why
 To promote transparency, ensure ethical AI practices, and inform stakeholders about potential biases and limitations.
 ### How
 Include sections in the model documentation that discuss known limitations, fairness assessments, and any bias mitigation steps taken. Use tools like Markdown or Jupyter Notebooks to format and share these reports.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-D000-DPICBDBN-dc878681] Document possible improvment can be done but not tested or integrated in the system yet.
- **Level:** Level 5 | **Topic:** Documentation
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
 List and describe potential improvements that have been identified but not yet tested or integrated.
 ### Why
 To keep track of enhancement ideas for future development and provide a roadmap for ongoing improvement.
 ### How
 Create a backlog or roadmap document using tools like Jira, or a shared document. Detail each potential improvement, including its expected benefits and any preliminary considerations.
Confluence and/or sphinx documentation
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-D000-BRHBCAAE-8320f34a] Bias report has been conducted and available (ex. wiki or confluence).
- **Level:** Level 5 | **Topic:** Documentation
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Conduct and make available a bias report for the AI models.
 ### Why
 To identify, document, and address any biases in the models, ensuring ethical AI practices and building trust with users.
 ### How
 Perform bias analysis using tools like Fairness Indicators or Aequitas. Document the findings and mitigation steps in a report. Publish the report on platforms like Confluence or a project wiki for easy access.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-D000-AIWDATAS-ff449253] An interface with details about the AI system/application and the decision-making process is available and the AI application is globally interpretable.
- **Level:** Level 5 | **Topic:** Documentation
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 An interface should provide comprehensive details about the AI system, including its decision-making process, ensuring the application is globally interpretable.
 ### Why
 To enhance transparency, build trust with users, and ensure compliance with regulatory and ethical standards.
 ### How
 Develop a user-friendly interface that explains the AI system's functionality, decision-making criteria, and provides visualizations of how decisions are made. Use frameworks like LIME or SHAP to support interpretability.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-MM00-USMOCDSP-12cea5d0] Use standard methodology of common data science project (e.g. descriptive analysis, eda, modeling, iterative, etc.).
- **Level:** Level 1 | **Topic:** Model Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Follow standard methodologies for data science projects, including descriptive analysis, exploratory data analysis (EDA), modeling, and iterative development.
 ### Why
 To ensure a structured, systematic approach that improves the quality and reliability of data science projects.
 ### How
 Implement a project workflow that includes steps for data collection, cleaning, EDA, model selection, training, evaluation, and iteration. Use tools like Jupyter Notebooks for documentation and analysis.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-MM00-EPOYMOTV-0bd57d87] Estimate performance of your model on train, validation, test sets with appropriate metrics.
- **Level:** Level 1 | **Topic:** Model Management
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
 Evaluate the performance of the machine learning model on training, validation, and test sets using relevant metrics.
 ### Why
 To assess the model's accuracy, generalization ability, and potential overfitting, ensuring it meets performance expectations.
 ### How
 Split the dataset into training, validation, and test sets. Use metrics such as accuracy, precision, recall, F1 score, ROC-AUC, and others appropriate for the problem. Document the results and compare performance across different sets.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-MM00-DKPIKOMT-20799280] Determine key performance indicators (KPIs or metrics) to measure success.
- **Level:** Level 2 | **Topic:** Model Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Identify and define the key performance indicators (KPIs) or metrics that will be used to measure the success of the AI project.
 ### Why
 To provide clear, quantifiable goals that align with business objectives and allow for consistent performance tracking.
 ### How
 Work with stakeholders to determine relevant KPIs. These might include metrics like accuracy, precision, recall, F1 score for classification tasks, or RMSE, MAE for regression tasks. Ensure these metrics are documented and agreed upon by all parties.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-MM00-SAPBTMTE-67e9a7c2] Set a performance baseline to measure the effectiveness and improvements of machine learning models.
- **Level:** Level 2 | **Topic:** Model Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Establish a baseline performance metric that represents the minimum acceptable performance level for the machine learning model.
 ### Why
 To have a reference point for evaluating the effectiveness of new models and improvements over time.
 ### How
 Use simple models or historical data to set the baseline performance. Document the baseline metrics and use them to compare against the performance of new models or iterations.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-MM00-CTMSMLMB-cd2c9cd1] Choose the most suitable machine learning model based on the problem requirements and characteristics.
- **Level:** Level 2 | **Topic:** Model Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Select the machine learning model that best fits the specific requirements and characteristics of the problem at hand.
 ### Why
 To ensure the chosen model effectively addresses the problem, meets performance criteria, and is practical to implement.
 ### How
 Evaluate different models considering factors like data type, size, complexity, and computational resources. Use techniques such as cross-validation and grid search to compare models and select the one that performs best on the validation set.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-MM00-DAATOAPM-4fec3cc0] Document and assess the outcomes and performance metrics of the trained machine learning model.
- **Level:** Level 2 | **Topic:** Model Management
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
 Thoroughly document the outcomes and performance metrics of the trained machine learning model.
 ### Why
 To provide a clear record of model performance, facilitate reproducibility, and enable stakeholders to understand and evaluate the results.
 ### How
 Create detailed reports that include the model's performance metrics, evaluation results on train, validation, and test sets, and any observations or insights. Use tools like Jupyter Notebooks, Markdown, or dedicated documentation platforms to present this information.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-MM00-RAMECDLH-9f59070e] Record and monitor experiments, capturing details like hyperparameters and results for future reference.
- **Level:** Level 2 | **Topic:** Model Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why
Anything that wont make it into production should be recorded in a
knowledge repository so future projects dont waste time trying the
same thing.
### How
MLflow tracking or Sagemaker Experiments are good candidates.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-MM00-ARAMECDL-acafa23d] Automatically record and monitor experiments, capturing details like hyperparameters and results for future reference.
- **Level:** Level 3 | **Topic:** Model Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### Why
Anything that wont make it into production should be recorded in a
knowledge repository so future projects dont waste time trying the
same thing.
### How
MLflow tracking or Sagemaker Experiments are good candidates.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-MM00-DAMP0000-34fbddc9] Develop a model pipeline.
- **Level:** Level 3 | **Topic:** Model Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Create a structured sequence of processes and stages for building, training, validating, and deploying machine learning models.
 ### Why
 To ensure a systematic, reproducible, and efficient workflow for model development and deployment.
 ### How
 Use tools like Apache Airflow, Sagemaker, or MLflow to design and implement the pipeline. Define stages such as data preprocessing, feature engineering, model training, validation, and deployment.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-MM00-LTAVSIET-733e7ef6] Log training and validation set in experiments tools.
- **Level:** Level 4 | **Topic:** Model Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Record details of the training and validation datasets used in experiments to track and reproduce results.
 ### Why
 To maintain a clear history of experiments, facilitate reproducibility, and analyze model performance over time.
 ### How
 Utilize experiment tracking tools like MLflow, Weights & Biases, or TensorBoard to log datasets, parameters, and results. Ensure consistent logging practices across all experiments.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-MM00-IIOPGALF-59f5f92a] Implement interpretability of predictions (global and/or local) for data science or users (Global explaination can be logged into experiment tracking tool and local interpretability can be logged in a table).
- **Level:** Level 4 | **Topic:** Model Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Provide mechanisms to explain model predictions at both global and local levels for transparency and trust.
 ### Why
 To help data scientists and end-users understand and trust the model’s predictions, facilitating better decision-making.
 ### How
 Use interpretability tools like SHAP, LIME, or Explainable AI. Log global explanations in experiment tracking tools and store local explanations in a dedicated table for easy access and analysis.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-MM00-MPIAROPE-06b1254e] Model provide information about robutness of prevision (e.g. confidence interval).
- **Level:** Level 4 | **Topic:** Model Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 The model should output information indicating the robustness of its predictions, such as confidence intervals.
 ### Why
 To give users an understanding of the reliability and uncertainty of the model's predictions.
 ### How
 Implement methods to calculate confidence intervals or prediction intervals. Ensure this information is included in the model’s output and appropriately documented.
MAPIE python module can help.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-MM00-FRAULEMW-998bd744] For RAG approach (using LLM), evaluate model with honest, harmnest, helpfull, triad, etc. metrics.
- **Level:** Level 4 | **Topic:** Model Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Assess models using metrics like honesty, harmlessness, helpfulness, and other relevant measures for Responsible AI Governance (RAG) when using Large Language Models (LLMs).
 ### Why
 To ensure the model adheres to ethical standards and provides reliable, safe, and useful outputs.
 ### How
 Define and implement metrics for evaluating honesty, harmlessness, and helpfulness. Use these metrics in the model evaluation process and document the findings for review.
Giskard, trulens can help.
https://github.com/EleutherAI/lm-evaluation-harness
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-MM00-MBFIADAM-bef24d61] Mitigate bias find in a dataset and model.
- **Level:** Level 5 | **Topic:** Model Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Identify and reduce bias in datasets and models to ensure fairness and accuracy.
 ### Why
 To prevent biased outcomes and ensure equitable model performance across different groups.
 ### How
 Conduct bias detection using tools like Fairness Indicators or Aequitas. Implement techniques such as re-sampling, re-weighting, or adversarial debiasing to mitigate identified biases.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-MM00-SARASOMI-2ca87fa8] Setup and run a scan of models in order to detect potential vulnaribilities in the model.
- **Level:** Level 5 | **Topic:** Model Management
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
 Regularly scan models to detect and address potential security vulnerabilities.
 ### Why
 To ensure the model is secure and robust against adversarial attacks and other vulnerabilities.
 ### How
 Use tools like CleverHans or IBM Adversarial Robustness Toolbox to scan for vulnerabilities. Implement security measures and continuously monitor and update the model as needed.
MLflow evaluate and Giskard are good candidates
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-MM00-WTSWBIAA-5d6f7c2f] Write tests suite (with business interlocutor) and automaticly execute it at each model release.
- **Level:** Level 5 | **Topic:** Model Management
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
 Develop a comprehensive test suite in collaboration with business stakeholders and ensure it runs automatically with each model release.
 ### Why
 To validate model performance and ensure it meets business requirements and quality standards.
 ### How
 Define test cases covering various aspects of the model, including accuracy, performance, and business logic. Integrate automated testing into the CI/CD pipeline using tools like pytest or unittest.
MLflow evaluate and Giskard are good candidates
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-DM00-ICOAHEDU-50d588a2] In case of Ad Hoc experimentation, data used are stored and versionned properly.
- **Level:** Level 1 | **Topic:** Data Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Ensure that data used for ad hoc experimentation is stored and versioned correctly.
 ### Why
 To maintain reproducibility and traceability of experimental results.
 ### How
 Use data versioning tools like Delta (or DVC) to track and manage data used in experiments. Document and store data along with relevant metadata in a centralized repository.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-DM00-ADSUPTTD-c32b3a8c] All data sources used provide to the datalake (e.g. silver, gold or insight zone).
- **Level:** Level 2 | **Topic:** Data Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Integrate all data sources into the data lake, categorizing them into zones like silver, gold, or insight.
 ### Why
 To ensure centralized, organized, and accessible data management for analysis and processing.
 ### How
 Use ETL tools to ingest and categorize data into the appropriate zones within the data lake.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-DM00-UAGFEDIA-891600f7] Utilize AWS Glue for efficient data ingestion and collection processes.
- **Level:** Level 2 | **Topic:** Data Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DM00-DSAMWDVT-4356239e] Data source are monitored with data validation tools.
- **Level:** Level 3 | **Topic:** Data Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Continuously monitor data sources using data validation tools to ensure data quality and integrity.
 ### Why
 To detect and address data quality issues early, maintaining high data standards.
 ### How
 Implement data validation frameworks like Great Expectations or Deequ to monitor and validate data continuously. Set up alerts for any data quality issues detected.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DM00-DADP0000-56d2ef34] Develop a data pipeline.
- **Level:** Level 3 | **Topic:** Data Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Create a structured data pipeline to handle data ingestion, processing, and storage.
 ### Why
 To ensure efficient, scalable, and reliable data flow from source to destination.
 ### How
 Use data pipeline tools like Apache Airflow, Pyspark or DPT code template
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DM00-DACDZSQL-4e8593da] Define and categorize data zones, specifying quality levels for input data.
- **Level:** Level 3 | **Topic:** Data Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Establish and define data zones (e.g., bronze, silver, gold) with specified quality levels for input data.
 ### Why
 To organize data based on quality and processing stages, ensuring clarity and consistency.
 ### How
 Implement data governance practices to categorize data zones. Define criteria for each zone and use tools like AWS Glue Data Catalog for organization.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DM00-DPIGAAES-776ea2cd] Data profiling is generated and available (ex. sphinx documentation).
- **Level:** Level 3 | **Topic:** Data Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Generate and provide access to data profiling reports to understand the characteristics and quality of the data.
 ### Why
 To facilitate data exploration, quality assessment, and informed decision-making.
 ### How
 Use data profiling tools like Pandas Profiling or DataProfiler. Document the profiling results and make them accessible using tools like Sphinx for creating detailed documentation.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DM00-DSUHDCWS-a00fd203] Data source used have data contracts (with SLA).
- **Level:** Level 4 | **Topic:** Data Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Ensure that all data sources are governed by data contracts, including service level agreements (SLAs).
 ### Why
 To establish clear expectations for data quality, availability, and performance between data providers and consumers.
 ### How
 Define and document data contracts specifying SLAs for each data source.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DM00-CADODZPT-55c295ca] Categorize and define output data zones, particularly those containing valuable insights.
- **Level:** Level 4 | **Topic:** Data Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Define and categorize output data zones, emphasizing areas that contain valuable insights.
 ### Why
 To organize and manage data outputs effectively, ensuring that valuable insights are easily accessible and usable.
 ### How
 Establish criteria for categorizing output data zones. Use data cataloging tools like AWS Glue and document these zone
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DM00-OAPAMWME-e0a69b3e] Ouputs are pushed and monitored with metadata (e.g. performance, confidence interval, trust metrics, etc.) in insight zone.
- **Level:** Level 4 | **Topic:** Data Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Ensure that outputs are pushed to the insight zone and monitored with relevant metadata such as performance, confidence intervals, and trust metrics.
 ### Why
 To provide a comprehensive understanding of data outputs, facilitating trust and informed decision-making.
 ### How
 Use monitoring tools to capture and record metadata for outputs. Ensure this metadata is stored in the insight zone and is accessible for analysis and review.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DM00-IDGPPLTL-1d187e42] Implement data governance practices, potentially leveraging tools like Collibra for enhanced data management.
- **Level:** Level 4 | **Topic:** Data Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Adopt data governance practices to manage data quality, compliance, and security effectively.
 ### Why
 To ensure data integrity, protect sensitive information, and comply with regulatory requirements.
 ### How
 Use data governance tools like Collibra
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DM00-ATMFASFT-80aced5a] All the model features are sourced from the feature store or external libraries.
- **Level:** Level 4 | **Topic:** Data Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DM00-MTTFODFI-770ad8b4] Map technicaly the flow of data from its source to its final output, understanding its journey and transformations.
- **Level:** Level 4 | **Topic:** Data Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
Data Lineage
### How
Marquez can help. See implementation here: https://github.com/dktunited/dps-ml-dml/blob/366c8bc43f3d757da05c1e402b006d9f745dc911/src/dps_ml_dml/jobs/training.py#L73
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-CM00-CAAFBNDA-2e86a669] Create Ad-hoc analysis for business (notebooks documented) and push into a github repository.
- **Level:** Level 1 | **Topic:** Code Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-CM00-CDAMSDTE-0fdc0117] Clearly define and manage software dependencies to ensure consistent and reproducible environments.
- **Level:** Level 2 | **Topic:** Code Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
Dependency specification
### How
Poetry, pyenv (or requirements.txt)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-CM00-AASKCOTD-8304084c] Analyze and summarize key characteristics of the dataset through Exploratory Data Analysis (EDA).
- **Level:** Level 2 | **Topic:** Code Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** Exploratory Data Analysis (EDA) has been conducted / Notebook getstarted
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-CM00-TOTDAOPD-ec43e6d2] The offline training data and online prediction data is transformed with the same code
- **Level:** Level 3 | **Topic:** Code Management
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
 Ensure that the code used for transforming offline training data is the same as that used for online prediction data.
 ### Why
 To maintain consistency in data processing and ensure that the model performs similarly during both training and inference.
 ### How
 Develop a shared codebase or library for data transformation. Use version control to manage and synchronize changes. Validate the transformations using tests to ensure they produce the same results in both offline and online environments.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-CM00-DAAWTEDP-db3f127d] Develop an automated workflow that encompasses data preprocessing, model training, and evaluation.
- **Level:** Level 3 | **Topic:** Code Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Create an automated workflow to handle data preprocessing, model training, and evaluation processes.
 ### Why
 To improve efficiency, reproducibility, and reduce the potential for human error in the model development lifecycle.
 ### How
Create ML pipeline or use workflow orchestration tools like Apache Airflow or sagemaker to automate the steps. Define and schedule tasks for each stage of the process, ensuring proper dependencies and data flow between tasks.

- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-CM00-CTAUDTEP-42bc473a] Containerize the application using Docker to enhance portability and reproducibility across different environments.
- **Level:** Level 3 | **Topic:** Code Management
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
 Use Docker to containerize the application, ensuring it can run consistently across various environments.
 ### Why
 To enhance portability, reproducibility, and ease of deployment, minimizing environment-related issues.
 ### How
 Create a Dockerfile to define the application's environment. Build and test the Docker image locally. Use container orchestration tools like Kubernetes for managing deployments.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-CM00-PCCTPMOA-86a21521] Package code components to promote modularity, organization, and ease of development.
- **Level:** Level 3 | **Topic:** Code Management
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
 Organize the code into modular packages to improve structure and maintainability.
 ### Why
 To facilitate easier development, testing, and reuse of code components.
 ### How
 Define clear boundaries for different components and package them accordingly. Use tools like setuptools for Python to create and manage packages. Ensure proper documentation and versioning for each package.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-CM00-PASCTFCA-a0f9c110] Provide a standardized code template for consistency and efficiency in development practices.
- **Level:** Level 3 | **Topic:** Code Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Develop and distribute standardized code templates to be used across projects.
 ### Why
 To ensure consistency, improve development efficiency, and reduce onboarding time for new developers.
 ### How
 Create templates that include common structures, configurations, and best practices. Store these templates in a shared repository and encourage their use through documentation and training sessions.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-CM00-TCOARDMA-de430174] Tests coverage of all reposiroty (data, ml, api) is > 60%.
- **Level:** Level 3 | **Topic:** Code Management
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
 Achieve and maintain test coverage of over 60% for all repositories, including data, ML, and API components.
 ### Why
 To ensure a basic level of code reliability and identify potential issues early in the development process.
 ### How
 Implement a comprehensive testing strategy using frameworks like pytest. Regularly measure test coverage using tools like coverage.py and address gaps by adding necessary test cases.
SonarCloud can help.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-CM00-UAPODTFL-985b5173] Utilize a PySpark or DBT template for large-scale data processing to optimize efficiency and scalability.
- **Level:** Level 3 | **Topic:** Code Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Use PySpark or DBT templates for handling large-scale data processing tasks.
 ### Why
 To optimize efficiency, scalability, and maintainability in data processing workflows.
 ### How
 Develop standardized templates for common data processing tasks using PySpark or DBT. Ensure these templates are well-documented and reusable. Implement them in data pipelines to handle large datasets effectively.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-CM00-CFANPOPM-004a79db] Conf files are not part of python module.
- **Level:** Level 3 | **Topic:** Code Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Ensure that configuration files are separate from Python modules.
 ### Why
 To maintain a clear separation of code and configuration, making the codebase more modular and easier to manage.
 ### How
 Store configuration files in a dedicated directory or use environment variables. Load configurations at runtime using libraries like configparser See ML template
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-CM00-ECQSUTLM-e2c289e6] Enforce code quality standards using tools like mypy for type checking and linters for style enforcement.
- **Level:** Level 3 | **Topic:** Code Management
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
 Use tools like mypy for type checking and linters for enforcing code style standards.
 ### Why
 To ensure high code quality, readability, and maintainability.
 ### How
 Integrate mypy and linting tools (e.g., flake8, pylint) into the development workflow. Configure these tools in the CI/CD pipeline to enforce standards automatically. Provide training and documentation on their usage and benefits. Code quality (mypy, lint). See Ruff implementation in ML Template
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-CM00-VCUDVLIP-e154f895] Validate configurations using data validation library in Python to ensure robustness and prevent errors.
- **Level:** Level 3 | **Topic:** Code Management
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
 Use a data validation library in Python to validate configurations, ensuring they are robust and error-free.
 ### Why
 To catch configuration errors early and prevent runtime issues.
 ### How
 Implement validation checks using libraries
Configuration validation (pydantic) - cf. ML template
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-CM00-CCTUTPFT-a44652b4] Conduct code testing using the pytest framework to validate the functionality of the code.
- **Level:** Level 3 | **Topic:** Code Management
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
 Use the pytest framework to write and run tests, validating the code's functionality.
 ### Why
 To ensure code reliability and correctness, and to identify issues early in the development cycle.
 ### How
 Write unit tests, integration tests, and functional tests using pytest. Integrate pytest into the CI/CD pipeline to automate test execution. Regularly review and update tests to cover new features and changes.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-CM00-PRSSTIAA-03679aea] Perform regular security scans to identify and address potential vulnerabilities in the codebase.
- **Level:** Level 3 | **Topic:** Code Management
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
 Conduct regular security scans on the codebase to detect and mitigate vulnerabilities.
 ### Why
 To protect the application from security threats and ensure compliance with security standards.
 ### How
 Use security scanning tools like Snyk, Bandit, or OWASP Dependency-Check. Integrate these tools into the CI/CD pipeline for continuous monitoring. Review and address any identified vulnerabilities promptly.
Code security (scan with Giskard)
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-CM00-CASPFRCQ-a604fe2d] Create a SonarCloud project for reporting code quality.
- **Level:** Level 3 | **Topic:** Code Management
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
 Set up a SonarCloud project to monitor and report on code quality metrics.
 ### Why
 To maintain high code quality standards, identify code issues early, and track improvements over time.
 ### How
 Configure SonarCloud to analyze the codebase. Integrate it with the CI/CD pipeline for automated code quality checks. Review and act on the reports generated by SonarCloud to improve code quality.
ML template: https://github.com/dktunited/dps-ml-databricks-template
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-CM00-TCOARDMA-de430174] Tests coverage of all reposiroty (data, ml, api) is > 70%.
- **Level:** Level 4 | **Topic:** Code Management
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
 Ensure that the test coverage for all repositories, including data, machine learning (ML), and API, exceeds 70%.
 ### Why
 To guarantee a baseline level of code reliability and reduce the risk of undetected issues in the codebase.
 ### How
 Implement comprehensive testing strategies and use code coverage tools like Jest, PyTest, or Coverage.py. Regularly review and update test cases to maintain and improve coverage.
SonarCloud can help.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-CM00-MCSIAPYS-3604588b] Maintability, code smells is A (provide y SonarCloud).
- **Level:** Level 4 | **Topic:** Code Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Achieve and maintain an A rating for maintainability and code smells as reported by SonarCloud.
 ### Why
 To ensure high code quality, readability, and ease of maintenance, reducing technical debt.
 ### How
 Use SonarCloud to continuously analyze the codebase. Address and resolve code smells and maintainability issues as they are identified. Implement coding standards and best practices to maintain high code quality.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-CM00-DSIATAFW-7a984f14] Data scientist is autonomous to add features with a PR on ML github repository.
- **Level:** Level 4 | **Topic:** Code Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Allow data scientists to independently add new features by submitting pull requests (PRs) on the ML GitHub repository.
 ### Why
 To facilitate rapid iteration and innovation while maintaining code quality and review processes.
 ### How
 Set up contribution guidelines and review processes in the GitHub repository. Ensure proper branching strategies and CI/CD pipelines are in place to handle feature additions.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-CM00-FAOASWME-e40c8fb8] Features and/or outputs are shared with metadata (e.g., performance metrics, interpretability, ...) as code that can be shared across projects (e.g., embedding). Insight ML Zone can help.
- **Level:** Level 4 | **Topic:** Code Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### How
Put data processing in a separate artifact by using for example the pyspark template
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-CM00-UADDCSFM-d0bdaf24] Use a Domain-Drive-Design (DDD) code structure for ML projects.
- **Level:** Level 4 | **Topic:** Code Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Apply Domain-Driven Design (DDD) principles to structure code in ML projects.
 ### Why
 To improve the organization, maintainability, and scalability of ML projects by aligning the code structure with business domains.
 ### How
 Organize code into modules based on business domains. Use DDD patterns such as entities, aggregates, and repositories. Ensure collaboration between data scientists and domain experts to align code with business requirements.
Release v8.0.0 of ml template provide this code structure.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-CM00-TCOARDMA-de430174] Tests coverage of all reposiroty (data, ml, api) is > 90%.
- **Level:** Level 5 | **Topic:** Code Management
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
 Ensure that the test coverage for all repositories, including data, machine learning (ML), and API, exceeds 90%.
 ### Why
 To maximize code reliability and minimize the risk of undetected issues.
 ### How
 Implement thorough testing strategies and utilize code coverage tools to measure and improve coverage. Regularly review and update test cases to maintain high coverage.
SonarCloud can help.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-CM00-YCIPIAPG-3c8f0480] Your code is pushed into a public github repository and follow open source standard.
- **Level:** Level 5 | **Topic:** Code Management
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Publish your code in a public GitHub repository and adhere to open-source standards.
 ### Why
 To promote transparency, collaboration, and reuse of code within the open-source community.
 ### How
 Ensure the code follows best practices for open-source projects, including clear documentation, licensing, and contribution guidelines. Use tools like GitHub Actions for CI/CD and maintain a high standard of code quality.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-V000-PPV00000-de977cbb] Placeholder: please validate
- **Level:** Level 1 | **Topic:** Versionning
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-V000-MATDVOML-420b9e41] Manage and track different versions of machine learning models to facilitate collaboration and experimentation.
- **Level:** Level 2 | **Topic:** Versionning
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Implement a system for managing and tracking different versions of machine learning models.
 ### Why
 To enable collaborative work, ensure reproducibility, and facilitate experimentation with various model versions.
 ### How
 Use model versioning tools like MLflow to track and manage different versions. Document changes and maintain a model registry for easy access and reference.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-V000-IASTVATC-f2931060] Implement a system to version and track changes in outputs dataset for reproducibility and traceability.
- **Level:** Level 3 | **Topic:** Versionning
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
 Set up a system to version and track changes in output datasets.
 ### Why
 To ensure reproducibility and traceability of data transformations and model outputs.
 ### How
 Use data versioning tools like DVC or Delta Lake to manage versions of output datasets. Track changes and document metadata for each version to maintain a clear history.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-V000-MIMRHS00-ce8df8be] Models in model registry have signature.
- **Level:** Level 3 | **Topic:** Versionning
- **BMAD Step:** Step 05 - Testing
- **Constraint:** ### What
 Ensure that models stored in the model registry include a signature.
 ### Why
 To verify the integrity and authenticity of models, facilitating secure and reliable deployments.
 ### How
 Implement model signing processes using cryptographic techniques. Store and verify signatures in the model registry to ensure models have not been tampered with.
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [ #0-DF00-ITLSTORE-f33627fb] Is the legacy stack (Talend, Opcon, Redshift, etc.) removed from our pipeline?
- **Level:** Level 1 | **Topic:** Data Factory
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** https://dataplatform.dktapp.cloud/data-factory
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#0-DF00-DWEODITD-22f5ab45] Do we expose our data in the Datalake?
- **Level:** Level 1 | **Topic:** Data Factory
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** https://dataplatform.dktapp.cloud/doc/products/storage/zones/datalake_zones/datalake_zones.html
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-DF00-WPROLEAS-c6f0f30a] Do we exclusively use Modern Data Stack tools (e.g., dbt, Airflow, Spark on Databricks, etc.) for data integration and transformation?
- **Level:** Level 2 | **Topic:** Data Factory
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** https://dataplatform.dktapp.cloud/data-factory
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#1-DF00-DWNLULZO-d86eef49] Do we no longer use legacy zones (ods, cds) to expose our data?
- **Level:** Level 2 | **Topic:** Data Factory
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** https://dataplatform.dktapp.cloud/doc/products/storage/zones/datalake_zones/datalake_zones.html
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DF00-WUAOTFDL-a3c60882] Do we use development standards to build our data pipelines (template, shared libraries, etc.)?
- **Level:** Level 3 | **Topic:** Data Factory
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** https://dataplatform.dktapp.cloud/doc/products/compute/template-products/overview.html
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DF00-WLAMCDSI-8d9592ab] Do we only use validated languages (Python & SQL) to build our data pipelines?
- **Level:** Level 3 | **Topic:** Data Factory
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** TBD
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DF00-WUTMABSG-547ae65f] Do we exclusively use the Medallion architecture (Bronze, Silver, Gold, Insight) with defined data governance policies?
- **Level:** Level 3 | **Topic:** Data Factory
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** https://dataplatform.dktapp.cloud/doc/products/storage/zones/datalake_zones/datalake_zones.html
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DF00-WCAOTSAZ-731aeeb7] Do we consistently apply optimization techniques (such as z-ordering and vacuuming) to enhance the performance of our data tables?
- **Level:** Level 3 | **Topic:** Data Factory
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** https://dataplatform.dktapp.cloud/doc/products/compute/compute-products/databricks-compute/concepts/optimize-costs.html#use-sql-warehouse-for-sql-workloads
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#2-DF00-DWUUC000-5479af03] Do we use Unity Catalog?
- **Level:** Level 3 | **Topic:** Data Factory
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** https://dataplatform.dktapp.cloud/doc/products/storage/metastore/uc_migration/uc_roadmap/uc_roadmap.html
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DF00-WEASDAVT-a3845118] Do we use a standardized, documented, and version-controlled template for data pipeline development?
- **Level:** Level 4 | **Topic:** Data Factory
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
I make cruft update regularly on Templates
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DF00-WPRISKOS-d5ae2401] Do we perform regular infrastructure sizing (Kubernetes or Spark clusters) to optimize both costs and performance?
- **Level:** Level 4 | **Topic:** Data Factory
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** https://dataplatform.dktapp.cloud/doc/products/compute/compute-products/databricks-compute/concepts/optimize-costs.html
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DF00-WCRMOICT-26af0083] Do we conduct regular monitoring of infrastructure costs through billing reports and implement optimization measures?
- **Level:** Level 4 | **Topic:** Data Factory
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** https://dataplatform.dktapp.cloud/doc/overview/billing/index.html
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#3-DF00-DWEODVAU-0afee7df] Do we expose our data via a Unity Catalog Managed Table?
- **Level:** Level 4 | **Topic:** Data Factory
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** https://dataplatform.dktapp.cloud/doc/products/storage/metastore/uc_migration/uc_roadmap/uc_roadmap.html
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---

### [#4-DF00-WUAQOTTM-994ccb8d] Do we utilize advanced query optimization techniques to minimize data spills or distribution skews?
- **Level:** Level 5 | **Topic:** Data Factory
- **BMAD Step:** Step 04 - Implementation
- **Constraint:** ### What
Skew and spill | Databricks Documentation
- **Verification:** L'agent doit valider la présence d'une preuve d'implémentation spécifique à cette règle.
---
