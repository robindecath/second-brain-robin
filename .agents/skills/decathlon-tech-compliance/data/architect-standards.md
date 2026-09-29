# BMAD Architect Knowledge Base (Decathlon Maturity Matrix)

### APIs are not used directly from the client application.
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Analytics

### Why ?
The clickstream APIs are regulary evolving and the library will ensure some backward compatibility with future APIs evolutions.
 The library is also ensuring some data integrity check to avoid some unexpected usage of the tracker.
### How ?
See (Front integration for developers)[https://decathlon.atlassian.net/l/cp/t1Xuigc6] documentation on the Clickstream wiki.


---
### Contract First pattern is applied on each public API
**Level:** Level 4 | **Pillar:** DEV | **Topic:** API

### Why ?
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


---
### API Contract is fully tested
**Level:** Level 4 | **Pillar:** DEV | **Topic:** API

### Why ?
Leverage the contract first approach to provide automated testing of your API contract.
### What ?
API contract informations could be verified automatically to prevent contract regression by leveraging test tooling.
### How ?
We recommend to integrate (schemathesis)[https://schemathesis.readthedocs.io/en/stable/] in your CD pipeline, but you could also rely on a collection of POSTMAN requests or other testing technologies that prevent regressions on API edge cases.

---
### Pen test has been implemented and documented on your API.
**Level:** Level 4 | **Pillar:** DEV | **Topic:** API

### What
 Conduct and document a penetration test on your API.
 ### Why
 To identify and address security vulnerabilities, ensuring the API is secure against attacks.
 ### How
 Engage a professional penetration testing team or use automated tools to perform the test. Document the findings, implement necessary security improvements, and maintain records for future reference.

---
### For AI/ML use case, API  python module provide a way to store api calls (inputs and outputs) and feedback loop implementation.
**Level:** Level 4 | **Pillar:** DEV | **Topic:** API

### What
 The API Python module should offer functionality to log API calls, including inputs and outputs, and implement a feedback loop mechanism.
 ### Why
 To enable monitoring, auditing, and continuous improvement of the AI/ML models by capturing real-world usage data and user feedback.
 ### How
 Implement logging mechanisms in the API to record inputs and outputs. Use databases or storage solutions like PostgreSQL, MongoDB, or cloud storage services to store this data. Integrate feedback loop capabilities to collect and utilize user feedback for model retraining and improvement.
Ex. Datadog and specific endpoint for feedback loop.

---
### For AI/ML use case, API provide interpretability insights of predictions.
**Level:** Level 4 | **Pillar:** DEV | **Topic:** API

### What
 The API should offer insights into the interpretability of its predictions, making the decision-making process transparent and understandable to users.
 ### Why
 To build trust with users, ensure compliance with ethical and regulatory standards, and facilitate informed decision-making.
 ### How
 Integrate interpretability tools such as SHAP or LIME into the API. Provide endpoints that return interpretability information alongside predictions. Document the interpretability methods and how to access them via the API.

---
### A System Design document exists
**Level:** Level 1 | **Pillar:** DEV | **Topic:** System Design Documents

### Why ?
 The purpose of the system design file is to describe your product in various aspects: business, technical... This document must be initialized in the first phase of the product and updated with each new product phase.

### What ?
To fulfill this requirement, create the document in github repository or on the a wiki page on the Decathlon's Confluence instance must be created by duplicate the existing template : [System Design Template](https://decathlon.atlassian.net/wiki/spaces/ENGINEERING/pages/184948248/System+Design)

### How ?
The team must be able to demonstrate that a wiki page based on the template is completed, with the technical architecture schemas expected

---
### The system design must contain diagrams using C4 format with level 1 and 2
**Level:** Level 2 | **Pillar:** DEV | **Topic:** System Design Documents

### Why ?
To know what is your dependencies with other (Decathlon) services and identify impact of a potential incident, a component diagram is very important for your project. Also these diagrams are very useful to quickly understand the architecture of the application.

### What ?
To fulfill the requirement, the team must present a wiki page, a web page from an external SaaS service or a C4 model hosted in a GitHub repository with all their dependencies. Don't forget to link it to the System Design document.

### How ?
You can use SaaS tools like [Draw.io] (https://www.diagrams.net/blog/c4-modelling) but if you want to use an « as code » solution, you can use C4 model with [Structurizr DSL] (e.g.: https://github.com/dktunited/dkt-retail-cartographie). If you are interested to use the « as code » solution but you don’t have a place to write your diagram, please contact the SIG Mobile members to help you.

---
### System design documents are up to date with a regular review on each major release
**Level:** Level 2 | **Pillar:** DEV | **Topic:** System Design Documents

### Why ?
 The purpose of the system design file is to describe your product in various aspects: business, technical... This document must be initialized in the first phase of the product and updated with each new product phase.
It will help any newcomer and people that need to work with your application to understand the platform and help you to check that any important requirement of Decathlon is met (security, disaster recovery, cost ...).

### What ?
To fulfill this requirement, a wiki page on the Decathlon's Confluence instance must be created by duplicate the existing template : [System Deisgn Template] (https://decathlon.atlassian.net/wiki/spaces/ENGINEERING/pages/184948248/System+Design)

### How ?
The team must be able to demonstrate that a wiki page is available and up to date.

---
### System Design documents include API consumers, stream data and external software components dependencies in the C4 diagrams
**Level:** Level 3 | **Pillar:** DEV | **Topic:** System Design Documents

"### Why ?
To know what is your dependencies with other (Decathlon) services and identify impact of a potential incident, a component diagram is very important for your project. Also these diagrams are very useful to quickly understand the architecture of the application.

### What ?
To fulfill the requirement, the team must present a wiki page, a web page from an external SaaS service or a C4 model hosted in a GitHub repository with all their dependencies. Don't forget to link it to the System Design document.

### How ?
You can use SaaS tools like [Draw.io] (https://www.diagrams.net/blog/c4-modelling) but if you want to use an « as code » solution, you can use C4 model with [Structurizr DSL] (e.g.: https://github.com/dktunited/dkt-retail-cartographie). If you are interested to use the « as code » solution but you don’t have a place to write your diagram, please contact the SIG Mobile members to help you."

---
### System design documents are using Markdown, versioned in a Git repository  and referenced in the IDP

**Level:** Level 4 | **Pillar:** DEV | **Topic:** System Design Documents

### Why ?
It has to be easy to identify system design changes, and thus to be able to identify differences between one version and another

### What ?
To fulfill this requirement, you have to store diagrams as code in a single repository for your business unit / business domain, using the Decathlon's standard tool (which could be [plantuml](https://plantuml.com/fr/), [structurizr](https://structurizr.com/) or [mermaidjs](https://mermaid.js.org/))

### How ?
The team must be able to demonstrate that a git repository exists and contains all business unit / business domain C level diagrams as code
The business unit / business domain wiki page has to refer to git repository

---
### System design documents include deployment diagrams as code including the infrastructure layout
**Level:** Level 4 | **Pillar:** DEV | **Topic:** System Design Documents

### Why ?
It has to be easy to identify system design changes, and thus to be able to identify differences between one version and another

### What ?
To fulfill this requirement, you have to store diagrams as code in a single repository for your business unit / business domain, using the Decathlon's standard tool (which could be [plantuml](https://plantuml.com/fr/), [structurizr](https://structurizr.com/) or [mermaidjs](https://mermaid.js.org/))

### How ?
The team must be able to demonstrate that a git repository exists and contains all business unit / business domain C level diagrams as code
The business unit / business domain wiki page has to refer to git repository

---
### Software documentation is generated through a CI process from code assets
**Level:** Level 5 | **Pillar:** DEV | **Topic:** System Design Documents

### Why ?
A good documentation is up-to-date documentation. Update the software documentation in the CI to be as close as possible to the codebase changes.

### What ?
Integrate an open-source plugin in the CI to generate the doc-as-code.
They are no official Decathlon recommendations for the moment.

### How ?
Add this new step as a github action in your CI to generate the documentation assets in your project.


---
### Architecture Decision Records (ADR) are hosted in a single place and reviewed by peers
**Level:** Level 2 | **Pillar:** DEV | **Topic:** Architecture Decision Record

### Why ?
 An architecture decision record (ADR) is a document that captures an important architectural decision made along with its context and consequences. It is important because the people who took the decisions may not be still on the project some years after the decisions have been taken, and the new developpers may make new decisions that will break the design of the application because of the lack of information regarding the previous choices made.

### What ?
To fulfill this requirement, create and store your ADR in your application git repo, then create a macro in the wiki pages of the project to display them. Template can be found here : [ADR template](https://decathlon.atlassian.net/wiki/spaces/ENGINEERING/pages/184950621/Architecture+Decision+Record+ADR+-+Template)

### How ?
The team must be able to demonstrate that ADRs are present in the repository and a wiki page is available pointing to these records.
Peers can be teammate outside of your team. Staffs and EMs should be included when the impact is bigger than just a team.

---
### Architecture Decision Records (ADR) are present in a github repository and displayed in the component page of IDP
**Level:** Level 3 | **Pillar:** DEV | **Topic:** Architecture Decision Record

### Why ?
It has to be easy to compare ADRs one with another, and to be able to identify differences between one version and another

### What ?
To fulfill this requirement, create and store your ADR in your application git repo.

### How ?
The team has to update records for every change on previous decisions


---
### All new Architecture Decision Records (ADR) follow the MADR standard
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Architecture Decision Record

###Why ?
Markdown Architectural Decision Records (MADR) give a template fo structure the documents and rely on Markdown format to simplify edition/visualisation directly on Github.

### How ?
You could get more information on the [MADR website](https://adr.github.io/madr/)

---
### Cross domain or cross project Architecture Decision Records (ADR) are stored in a mutualized git repository
**Level:** Level 5 | **Pillar:** DEV | **Topic:** Architecture Decision Record

### Why ?
ADRs may impact more than one component at a domain / business unit level

### What ?
To fulfill this requirement, create and store your ADR in your business unit / business domain git repo, then use [MADR template](https://adr.github.io/madr/)

### How ?
Ensure every impacted component repository is identified
Ensure every impacted component refers to you business unit / business domain git ADR repository


---
### Create modular diagram (if relevant)
**Level:** Level 2 | **Pillar:** DEV | **Topic:** Software Design

### Why ?
 When you’ve a new comer in your team or if you want to improve your modular strategy, it is important to write your modular diagram to discuss about any improvements or to communicate with your team members what is the current modular strategy to follow.
### What ?
To fulfill the requirement, the team must present a wiki page with the modular diagram. It will be completed in a next level to write your modularization strategy.
### How ?
You can use SaaS tools like Miro or Figma but if you want to use an « as code » solution, you can use Mermaid compatible with GitHub or our Wiki to describe your modular diagram.

---
### Avoid callbacks for background tasks
**Level:** Level 3 | **Pillar:** DEV | **Topic:** Software Design

### Why ?
In programming, callback hell refers to an ineffective way of writing asynchronous code. It takes place when you nest functions and create too many levels of nesting. This makes it harder to control access to the specific function and it becomes harder to debug the issues. Nesting means placing functions in another ones. By placing callback in a callback logic might get too messy.

### What ?
To fulfill this requirement, more modern ways to work with background/async code must be used like suspend method, combine framework, async/await framework, etc.

### How ?
The team must be able to demonstrate that they do not use callback for background tasks.

---
### Create modularization strategy document in your wiki
**Level:** Level 3 | **Pillar:** DEV | **Topic:** Software Design

### Why ?
 According to the complexity of your modular diagram, it can be difficult to understand it well and know exactly what is the responsibilities of each module in your application. The modularization strategy explain all concepts included in your diagram.
### What ?
To fulfill the requirement, the team must present a wiki page with your modular diagram completed with the strategy.
### How ?
Explain all concepts in your wiki page, potential rules to follow in the dependencies between your modules and what is the responsibilities of each kind of module.

---
### Using dependency injection to avoid strong coupling dependencies
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Software Design

### Why ?
Strong coupling between your dependencies is a bad pattern in all applications (not only for mobile apps). Using a dependency injection will help your team to avoid this bad pattern.
### What ?
To fulfill the requirement, you should add Dependency Injection library in your project, use it in all layer of your architecture and everywhere (including in your legacy code).
### How ?
Check the Techradar to know which dependency injection has been referenced for your mobile platform and start to use it in your mobile project after a first learning in the official documentation if necessary.

---
### Access and/or Refresh Tokens are encrypted and set as HTTP Only Cookies
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Authentication

### What?
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

---
### Your ADRs should contain one ADR which explains which kind of BFF your application implements.
**Level:** Level 3 | **Pillar:** DEV | **Topic:** BFF

### Why?
There are several types of Backend For Frontends (BFF).
The traditional concept is about introducing a backend service dedicated to a frontend application, whose responsability is to build tailor made responses.
To do so, BFF will have to orchestrate one or several calls to backend APIs and cherry pick relevant data to be forwarded to the frontend app.

Since the early days of that design pattern, the industry moved on and many frameworks and libraries blurred the lines between BFFs and Server Side Rendering (SSR) techniques/tools.

### What?
Write an ADR providing the full rationale behind the choice and reasons for implementing a BFF. Especially regarding the BFF archetype you picked (CSR or SSR types).
More info on the [archetypes here](https://decathlon.atlassian.net/wiki/x/gwTLGQ).

### How?
Store this ADR in the same place as you would store any other ADR concerning your product.



---
### [For internal apps] Your BFF is placed behind a Firewall
**Level:** Level 4 | **Pillar:** DEV | **Topic:** BFF

### Why?
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

---
### [For external apps] Your BFF is placed behind the APIm
**Level:** Level 4 | **Pillar:** DEV | **Topic:** BFF

### Why?
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

---
### Usage of any Design System libraries of Vitamin Play Web + one of the three component libraries available (React, Svelte or Vue) + follow the guidelines (do/don't, etc.) from https://decathlon.design
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Design System

### Why?
The incorporation of Design System libraries is essential for ensuring consistency, scalability, and efficiency in engineering products. By utilizing [Vitamin Play Web](https://github.com/dktunited/vitamin-play-web) libraries, we aim to establish a unified visual language and interaction patterns across our products, fostering a seamless user experience.

If you want to know why do we create a new implementation of our Design System called Vitamin Play, please refer to our [website](https://www.decathlon.design).

### What?
Our Design System libraries [Vitamin Play Web](https://github.com/dktunited/vitamin-play-web), encapsulate a set of pre-designed UI components, styles, and guidelines.
These resources empower development teams to maintain a cohesive design language, streamline development efforts, and enhance collaboration between design and engineering.

### How?
To integrate these Design System libraries into our engineering products, teams should follow the comprehensive documentation provided. This includes importing the necessary components, adhering to styling guidelines, and staying updated with any library enhancements. Regular collaboration with the design team ensures alignment with the overall product vision and consistent implementation of design principles.

For more detailed information, you can refer to the documentation on the usage of [Vitamin Play Web](https://github.com/dktunited/vitamin-play-web).

---
### Traces are enriched with functional data that are relevant for the process
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Observability

### Why?
Adding business-specific context to traces provides deeper insights into the "what" and "why" behind performance and behavior, enabling more meaningful analysis and targeted troubleshooting.

### What?
Relevant business information (like user IDs, order numbers, product IDs, etc.) is attached as tags or attributes to spans within the traces.

### How?
Application code is modified to extract and inject this functional data into the tracing context as spans are created or processed. This step depends on which tools you are using (open Telemetry https://opentelemetry.io/docs/zero-code/java/spring-boot-starter/annotations/  or  Datadog  https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/java/dd-api / ...)

---
### RUM insights are used to compute a SLI for you main user journey
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Observability

### Why ?
The best measure point for SLOs are the ones closest to your users, aka their devices.

### What ?
You have an SLI that measures the global availability of your process, and the SLI is the ratio of complying sessions, based on your criteria

### How ?
* [How-to](https://decathlon.atlassian.net/wiki/x/QoIHd)
* [TechDay talk to have more context and see an MVP](https://drive.google.com/file/d/1_etTwErH5aT4hn0Amw31vxgnz-WdqTH6/view?usp=sharing)

---
### Main business code calculation have custom trace to measure processing time
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Observability

### Why ?
Observability platform allows you to measure the processing time on specific code with custom traces. It helps your team to know if your code is optimized or not for a specific use case.
### What ?
To fulfill the requirement, your domain layer should be monitored with custom traces for new code and legacy code.
### How ?
Check the Techradar to know which observability library you should use to write your custom trace in your codebase and add them at the domain layer of your mobile architecture. If you want, you can create sub trace in your data layer to identify exactly which request or algorithm take too much time.

---
### Best in class performances measured automatically

**Level:** Level 4 | **Pillar:** DEV | **Topic:** Performance

### Why ?
Decathlon aims at becoming a Tech Giant.
To do so, among many other things, applications must reach the industry standards, especially in terms of User eXperience performance.

### What ?
Core Web Vitals is a set of metrics that measure real-world user experience for loading performance, interactivity, and visual stability of the page.
We highly recommend site owners achieve good Core Web Vitals for success with Search and to ensure a great user experience generally.
This, along with other page experience aspects, aligns with what this core ranking systems seek to reward.

### How ?
Use the Tech Radar's Observability Monitoring tool under the ADOPTED status.
Metrics to pay attention are the [Web Core Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals).

---
### Commit history is part of the code review for each branch

**Level:** Level 4 | **Pillar:** DEV | **Topic:** Source Control

### Why ?
Git history is the first code documentation: intentions, explanations ...
So having a clean history is important to share information on the code.

### What ?
Practice to rewrite history & and verify it on code review

### How ?
Team members should use interactive rebases to rewrite and clean history.
On a pull request review, we should verify that the history is clean.
We can add this notion in the "Definition of Done" (github template or other method).

---
### Hooks are documented and shared with the team
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Source Control

TBD

### Why ?

### What ?

### How ?


---
### All New languages, frameworks, data engineering solutions (database, messaging, and cache solutions) with status WATCH, FORBIDDEN or outside Tech Radar, are being processed to become a standard (Ongoing Standard Proposal Process) or being migrated (Action plan and Budget defined)
**Level:** Level 1 | **Pillar:** DEV | **Topic:** Tech Radar

### Why ?
Standardization helps us be more efficient by providing better support on reduced scope of technical solutions, reduce risks by not using unwanted or unsecure solutions, and accelerate at scale by developping product easily exportable and deployable (more compatible with everyone landscape). We aim to create synergy !

### What ?
First, we want to ensure all non-compliant technical solutions are identifed on your scope (you are aware of them) and that you have an action plan (standardization or migration) to reach better compliance.

### How ?
The team must be able to demonstrate that all technical solutions are :
- existing in the [Tech Radar](https://airtable.com/appWhu5K3NTs5XURY/pagyttV838v5dvazI) under the status ADOPT, TRIAL or ON HOLD,
- not existing in the [Tech Radar](https://airtable.com/appWhu5K3NTs5XURY/pagyttV838v5dvazI) or under the status WATCH or FORBIDDEN but are part of a standard proposal process or identified as to be migrated in the product roadmap.

---
### 100% of languages, frameworks, data engineering solutions (database, messaging, and cache solutions) used have the ring ""ADOPT"" or ""ON HOLD"" in the Tech Radar.
**Level:** Level 2 | **Pillar:** DEV | **Topic:** Tech Radar

### Why ?
Standardization makes us more efficient by narrowing down technical solutions, minimizing risks from insecure options, and accelerating scalability through easily exportable and deployable products. The goal is to create synergy!

### What ?
We want to ensure all the languages are compliant (ADOPT or ON HOLD) without exceptions. Cf. Tech Radar.

### How ?
The team must be able to demonstrate that all the languages used exist in the Tech Radar under the status ADOPT or ON HOLD.
100% of my On Hold Technical Solutions are identified (Action Plan and Migration cost assessment)

---
### Prefer Typescript for JS stacks
**Level:** Level 2 | **Pillar:** DEV | **Topic:** Tech Radar

### Why ?
TypeScript enhances code quality and maintainability by introducing static typing, which reduces runtime errors and improves developer productivity. It also fosters better collaboration through clear interfaces and strong tooling support. By standardizing on TypeScript, we ensure consistency, scalability, and long-term maintainability in our JavaScript stacks.

### What ?
We aim to ensure that all JavaScript-based projects prioritize TypeScript as the default choice, leveraging its benefits for reliability, scalability, and developer experience.

### How ?
All new JavaScript projects must default to TypeScript unless a strong, justified exception is provided.
Existing JavaScript projects should have a migration plan toward TypeScript, assessing feasibility and benefits.

---
### 100% of languages, frameworks, data engineering solutions (database, messaging, and cache solutions) used have the ring ""ADOPT"" in the Tech Radar.
**Level:** Level 3 | **Pillar:** DEV | **Topic:** Tech Radar

### Why ?
Standardization helps us to be more efficient by providing better support on reduced scope of technical solutions, reduce risks by not using unwanted or unsecure solutions and accelerate at scale by developping product easily exportable and deployable (more compatible with everyone landscape). We aims to create synergy !

### What ?
We want to ensure that databases, messaging, cache solutions have the status ADOPT in the Tech Radar.

### How ?
The team must be able to demonstrate that all databases, messaging, cache solutions used exist in the Tech Radar under the status ADOPT.

---
### Do you use Typescript in strict mode ?
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Tech Radar

### Why ?
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

---
### Process to review dependencies obsolescence and/or relevance
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Tech Radar

### Why ?
Software development changes very fast and it's very important to be up-to-date as much as possible in order to avoid security issues and be able to use latest features in a project. To be sure to be up-to-date, it's important to be able to monitor dependencies obsolescence.

### What ?
To fulfill this requirement, a process to review dependencies obsolescence must be implemented. It can be through the implementation of a dedicated tools like Renovate or Dependabot (check the company/tech radar compliancy).

### How ?
The team must be able to demonstrate that they have a process to review dependencies obsolescence.

---
### Risk & compliance review.
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Business & strategy

### How
Risk matrix not defined

---
### Start to define KPI in line Group AI policy (e.g. disparate impact, pdp, etc.)
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Business & strategy

### How
An example here : TODO

---
### Calculate and monitor the AI product value (€)
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Business & strategy

### How
ML Design Doc

---
### Define and describre a human-in-the-loop strategy / user feedback.
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Business & strategy

### How
ML Design Doc

---
### Listen to user needs and ensure continuous improvement of the product - I maintain the user research deliverables: Personas, Journey Map, experimentation synthesis, mock-ups, ...
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Business & strategy

TBD

---
### Explore solution hypothesis in a cost-effective and timely manner - I choose and prioritize the solution derisking methods adapted to each case (AB test, mock-ups, prototypes, ...)
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Business & strategy

TBD

---
### Explore solution hypothesis in a cost-effective and timely manner - I co-define the user research with the UX designers and researchers
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Business & strategy

TBD

---
### Collaborate with Designers to guide their work in designing the Product - I know how to choose between different user research methods adapted to each case (interviews, focus groups, etc.)
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Business & strategy

TBD

---
### Prioritise and plan the evolution and development of the Product - I prioritize the backlog by integrating the notion of value for the user, and I know prioritization techniques (MOSCOW, ROI, ROE, RICE, WSJF, KANO etc.)
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Delivery

TBD

---
### Guarantee the quality of the product, its safety and its DRP - I prioritize bugs and monitor the technical and functional debt
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Delivery

TBD

---
### Guarantee the quality of the product, its safety and its DRP - I take into account the technical tasks and integrate them into the prioritization
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Delivery

### How
Check with the PM

---
### Guarantee the quality of the product, its safety and its DRP - I define and manage the product's operational excellence commitments
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Delivery

### How
Check with the PM

---
### Communicate the past and future progress of the Product, both externally and internally to the team - I communicate on the roadmap and its progress inside and outside the team (via Release Notes)
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Delivery

TBD

---
### Define and supervise the key success data of the Product - Track and monitor the right indicators for my product (e.g. traffic)
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Delivery

TBD

---
### Define and supervise the key success data of the Product - I know how to build relevant dashboards adapted to the audience (Codir, Product Team etc.).
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Delivery

TBD

---
### Document and history report of meeting about technical choose (for modeling and deployment).
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Documentation

### What
 Maintain records and reports of meetings focused on technical decisions related to modeling and deployment.
 ### Why
 To ensure transparency, provide a historical reference, and facilitate informed decision-making in future developments.
 ### How
 Record meeting minutes and decisions using tools like Confluence or Google Docs. Include details on attendees, topics discussed, decisions made, and action items. Organize and store these documents chronologically.

---
### Share limits and fairness of each model release.
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Documentation

### What
 Provide documentation on the limitations and fairness considerations for each model release.
 ### Why
 To promote transparency, ensure ethical AI practices, and inform stakeholders about potential biases and limitations.
 ### How
 Include sections in the model documentation that discuss known limitations, fairness assessments, and any bias mitigation steps taken. Use tools like Markdown or Jupyter Notebooks to format and share these reports.

---
### Log training and validation set in experiments tools.
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Model Management

### What
 Record details of the training and validation datasets used in experiments to track and reproduce results.
 ### Why
 To maintain a clear history of experiments, facilitate reproducibility, and analyze model performance over time.
 ### How
 Utilize experiment tracking tools like MLflow, Weights & Biases, or TensorBoard to log datasets, parameters, and results. Ensure consistent logging practices across all experiments.

---
### Implement interpretability of predictions (global and/or local) for data science or users (Global explaination can be logged into experiment tracking tool and local interpretability can be logged in a table).
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Model Management

### What
 Provide mechanisms to explain model predictions at both global and local levels for transparency and trust.
 ### Why
 To help data scientists and end-users understand and trust the model’s predictions, facilitating better decision-making.
 ### How
 Use interpretability tools like SHAP, LIME, or Explainable AI. Log global explanations in experiment tracking tools and store local explanations in a dedicated table for easy access and analysis.

---
### Model provide information about robutness of prevision (e.g. confidence interval).
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Model Management

### What
 The model should output information indicating the robustness of its predictions, such as confidence intervals.
 ### Why
 To give users an understanding of the reliability and uncertainty of the model's predictions.
 ### How
 Implement methods to calculate confidence intervals or prediction intervals. Ensure this information is included in the model’s output and appropriately documented.
MAPIE python module can help.

---
### For RAG approach (using LLM), evaluate model with honest, harmnest, helpfull, triad, etc. metrics.
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Model Management

### What
 Assess models using metrics like honesty, harmlessness, helpfulness, and other relevant measures for Responsible AI Governance (RAG) when using Large Language Models (LLMs).
 ### Why
 To ensure the model adheres to ethical standards and provides reliable, safe, and useful outputs.
 ### How
 Define and implement metrics for evaluating honesty, harmlessness, and helpfulness. Use these metrics in the model evaluation process and document the findings for review.
Giskard, trulens can help.
https://github.com/EleutherAI/lm-evaluation-harness

---
### Data source used have data contracts (with SLA).
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Data Management

### What
 Ensure that all data sources are governed by data contracts, including service level agreements (SLAs).
 ### Why
 To establish clear expectations for data quality, availability, and performance between data providers and consumers.
 ### How
 Define and document data contracts specifying SLAs for each data source.

---
### Categorize and define output data zones, particularly those containing valuable insights.
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Data Management

### What
 Define and categorize output data zones, emphasizing areas that contain valuable insights.
 ### Why
 To organize and manage data outputs effectively, ensuring that valuable insights are easily accessible and usable.
 ### How
 Establish criteria for categorizing output data zones. Use data cataloging tools like AWS Glue and document these zone

---
### Ouputs are pushed and monitored with metadata (e.g. performance, confidence interval, trust metrics, etc.) in insight zone.
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Data Management

### What
 Ensure that outputs are pushed to the insight zone and monitored with relevant metadata such as performance, confidence intervals, and trust metrics.
 ### Why
 To provide a comprehensive understanding of data outputs, facilitating trust and informed decision-making.
 ### How
 Use monitoring tools to capture and record metadata for outputs. Ensure this metadata is stored in the insight zone and is accessible for analysis and review.

---
### Implement data governance practices, potentially leveraging tools like Collibra for enhanced data management.
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Data Management

### What
 Adopt data governance practices to manage data quality, compliance, and security effectively.
 ### Why
 To ensure data integrity, protect sensitive information, and comply with regulatory requirements.
 ### How
 Use data governance tools like Collibra

---
### All the model features are sourced from the feature store or external libraries.
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Data Management

TBD

---
### Map technicaly the flow of data from its source to its final output, understanding its journey and transformations.
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Data Management

### What
Data Lineage
### How
Marquez can help. See implementation here: https://github.com/dktunited/dps-ml-dml/blob/366c8bc43f3d757da05c1e402b006d9f745dc911/src/dps_ml_dml/jobs/training.py#L73

---
### Tests coverage of all reposiroty (data, ml, api) is > 70%.
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Code Management

### What
 Ensure that the test coverage for all repositories, including data, machine learning (ML), and API, exceeds 70%.
 ### Why
 To guarantee a baseline level of code reliability and reduce the risk of undetected issues in the codebase.
 ### How
 Implement comprehensive testing strategies and use code coverage tools like Jest, PyTest, or Coverage.py. Regularly review and update test cases to maintain and improve coverage.
SonarCloud can help.

---
### Maintability, code smells is A (provide y SonarCloud).
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Code Management

### What
 Achieve and maintain an A rating for maintainability and code smells as reported by SonarCloud.
 ### Why
 To ensure high code quality, readability, and ease of maintenance, reducing technical debt.
 ### How
 Use SonarCloud to continuously analyze the codebase. Address and resolve code smells and maintainability issues as they are identified. Implement coding standards and best practices to maintain high code quality.

---
### Data scientist is autonomous to add features with a PR on ML github repository.
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Code Management

### What
 Allow data scientists to independently add new features by submitting pull requests (PRs) on the ML GitHub repository.
 ### Why
 To facilitate rapid iteration and innovation while maintaining code quality and review processes.
 ### How
 Set up contribution guidelines and review processes in the GitHub repository. Ensure proper branching strategies and CI/CD pipelines are in place to handle feature additions.

---
### Features and/or outputs are shared with metadata (e.g., performance metrics, interpretability, ...) as code that can be shared across projects (e.g., embedding). Insight ML Zone can help.
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Code Management

### How
Put data processing in a separate artifact by using for example the pyspark template

---
### Use a Domain-Drive-Design (DDD) code structure for ML projects.
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Code Management

### What
 Apply Domain-Driven Design (DDD) principles to structure code in ML projects.
 ### Why
 To improve the organization, maintainability, and scalability of ML projects by aligning the code structure with business domains.
 ### How
 Organize code into modules based on business domains. Use DDD patterns such as entities, aggregates, and repositories. Ensure collaboration between data scientists and domain experts to align code with business requirements.
Release v8.0.0 of ml template provide this code structure.

---
### Do we use a standardized, documented, and version-controlled template for data pipeline development?
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Data Factory

### What
I make cruft update regularly on Templates

---
### Do we perform regular infrastructure sizing (Kubernetes or Spark clusters) to optimize both costs and performance?
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Data Factory

https://dataplatform.dktapp.cloud/doc/products/compute/compute-products/databricks-compute/concepts/optimize-costs.html

---
### Do we conduct regular monitoring of infrastructure costs through billing reports and implement optimization measures?
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Data Factory

https://dataplatform.dktapp.cloud/doc/overview/billing/index.html

---
### Do we expose our data via a Unity Catalog Managed Table?
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Data Factory

https://dataplatform.dktapp.cloud/doc/products/storage/metastore/uc_migration/uc_roadmap/uc_roadmap.html

---
### Decline EcoDesign principles in your project
**Level:** Level 4 | **Pillar:** DESIGN | **Topic:** Design

### Why ?
The consideration of ecodesign standards is a must for decathlon products. In this sense, each business must apply to respect the best in class practices

### What ?
To fulfull this requirement, Please apply to your workflow and product eco-design standards that you are concerned (Documentation here)

### How ?
 The team must be able to demonstrate design is processing eco-design action (image treatment, Video treatment, best in class principles..)

---
### Design with real data (from a database file)
**Level:** Level 4 | **Pillar:** DESIGN | **Topic:** Design

### Why ?
One of the most complex subjects for a designer is to take into account the data model. In order to improve the quality of interfaces and user interface, it is important to work with real data and not mock.

### What ?
Connect your figma interfaces to the Decathlon data (via xls file or directly by API retrieval via the Decathlon datalake or image DB). Different methods exist : local plugin, G.Sheet sync .

### How ?
The team must be able to demonstrate that design file are not using mock data, but dynamic data.

---
### Add Sounds design in your product
**Level:** Level 4 | **Pillar:** DESIGN | **Topic:** Documentation

### Why ?
The Sound design is an integral part of the man-machine interaction, allowing to improve the communication with the user thanks to the sound system. It is to be used with parsimony on important actions.

### What ?
To fulfull this requirement, set up sound design on the actions that make the most sense. (documentation here)

### How ?
The team must be able to demonstrate that sound design has been setup and documented.

---
### Test are done before merging new interfaces
**Level:** Level 4 | **Pillar:** DESIGN | **Topic:** Workflow

### Why ?
In the interest of quality, UI interfaces must be tested before being merged onto the master.

### What ?
To fulfull this requirement, set up a verification action (Vitamin checker) in the DOD (To be added to the workflow) + Rely on UI non-regression test plugins ([regressor](https://www.figma.com/community/plugin/1213220990852681773) available)

### How ?
The team must be able to demonstrate that quality action are set up in the workflow.

---
### Some actions are put in the backlogs to improve delivery
**Level:** Level 4 | **Pillar:** DELIVERY | **Topic:** Accelerate

### What is expected ?
Your backlog has some tickets to improve the delivery. It can be around development process, automation, ...

---
### You have defined your goal (KR) with accelerate metrics in the IDP and they are debriefed by the management
**Level:** Level 4 | **Pillar:** DELIVERY | **Topic:** Accelerate

### What is expected ?
You have defined the good level (Key Result) your application should reach and it is animated by your management

---
### Production and non production configuration (technical and applicative ) deployment is automated
**Level:** Level 4 | **Pillar:** DELIVERY | **Topic:** Application Configuration Management

### What is expected ?
When you have an applicative configuration, you can promote one configuration from staging to production. eg: on a payment application, you may change a limit on a payment provider, test it on staging then click a button to push the same change in production). For this level, a configuration server may be involved.

---
### Manually destroy some technical component such as Database, load balancing, compute ...
**Level:** Level 4 | **Pillar:** DELIVERY | **Topic:** Chaos Engineering

### What is expected ?
You already destroyed a technical component in production and expected a full recovery in your objective. (component may have been recreated by relaunching some terraform / IaC process)

---
### Your are using a reusable workflow managed by your domain
**Level:** Level 4 | **Pillar:** DELIVERY | **Topic:** Continous Integration

### What is expected?
Your build pipeline is using a reusable implementation of CI/CD managed at your domain domain. /!\ It is not about copy/paste existing Github action workflow but using a reusable one.
Implementations exists in ecommerce, instore, cpe, bcp, ...

---
### Production deployment is performed after every merge in main branch. Pull requests are deployed on ephemeral environments

**Level:** Level 4 | **Pillar:** DELIVERY | **Topic:** Continuous Deployment

### What is expected ?
Test are done on ephemeral environment during the PR validation and production deployment(automated or manual relase process) are done when PR is merged on main branch or a release is created.

---
### Production deployment rollback with low latency can be performed manually
**Level:** Level 4 | **Pillar:** DELIVERY | **Topic:** Continuous Deployment

### What is expected ?
You have a rollback process (can be link to untag/retag of previous version, can be modifying a configuration file...) The version support the current database version so that there is no "big change" to do for this rollback to work.

---
### My application is deployed on multiple regions (active/passive mode)
**Level:** Level 4 | **Pillar:** DELIVERY | **Topic:** Service Availability

### What is expected ?
The deployment is done on at least 2 regions but one is active, the other one can take the relay in case of failure (manual or automated promotion)

---
### Each day, an e2e test pipeline is triggered (P0)
**Level:** Level 4 | **Pillar:** DELIVERY | **Topic:** Workflows

### Why ?
Each night, a workflow should be trigger to generate a nightly release of your mobile application which will include all your changes from your previous day. This artifact should be publish in a registry and easily accessible for your team.

### What ?
To fulfill this requirement, your Bitrise configuration should include the assemble and publish Bitrise Actions to build your mobile application and publish it in a registry.

### How ?
Add the Bitrise Action from Bitrise website or locally in your bitrise yaml file on the develop branch and triggered during the night.

---
### Pipeline Redundancy - In the event that a pipeline should fail, the process should be able to automatically halt and give alerts to the development team.
**Level:** Level 4 | **Pillar:** DELIVERY | **Topic:** Continous Integration

### What
The team then needs to correct any issues that have caused this error condition and start the pipeline orchestration from the beginning, prior to doing anything else, treating this condition as a high priority.

---
### Static code analysis decorate pull requests with a comment from sonar user.
**Level:** Level 4 | **Pillar:** DELIVERY | **Topic:** Continous Integration

### Why ?
Sonar will block your Pull Request before this requirement (thanks to quality pillar) but to help your team to know what are the potential regressions reported by sonar, you should configure Sonar to publish a comment on your Pull Request with a summary of the build.

### What
To fulfill this requirement, every pull request should be decorated by sonar with the summary of the build.

### How
Configure your sonar integration to be executed on every pull request and post the comment.

---
### Tests suite for ensuring quality of AI model are automatically launched on a model before to use it on production.
**Level:** Level 4 | **Pillar:** DELIVERY | **Topic:** Continuous Deployment

### What is expected
 Implement an automated test suite to validate the quality of AI models before they are deployed to production, ensuring they meet performance and reliability standards.
### How
Giskard can help

---
### Depl files and store in a dedicated git repository (for using data, ml or api python module).
**Level:** Level 4 | **Pillar:** DELIVERY | **Topic:** Continuous Deployment

### What is expected
 Store deployment files in a dedicated Git repository to manage and track changes to deployment scripts and configurations for data, ML, and API Python modules.

---
### Deployment in production environment is automated. We don't need humain intervention.
**Level:** Level 4 | **Pillar:** DELIVERY | **Topic:** Continuous Deployment

### What is expected
 Production deployments should be fully automated, eliminating the need for human intervention to ensure consistency and reduce the potential for errors.

---
### CT is setup and based to KPI and heuristic.
**Level:** Level 4 | **Pillar:** DELIVERY | **Topic:** Continuous Deployment

### What
Continuous Training for automating the re training of ML model on new data.
### How
Groundtruth doesnot exist. You need to find a way to estimate performances without target.

---
### Conduct A/B tests (e.g. shadown, canary deployment)
**Level:** Level 4 | **Pillar:** DELIVERY | **Topic:** Continuous Deployment

### What is expected
 Implement A/B testing strategies, including shadow and canary deployments, to compare different versions of models or applications in production and assess their performance.

---
### Quality tests, including load testing, have been implemented for APIs containing embedded data or models. These tests are initiated and AUTOMATED with each deployment.
**Level:** Level 4 | **Pillar:** DELIVERY | **Topic:** Service Availability

### What is expected
 Automate quality and load testing for APIs with embedded data or models, ensuring these tests run with each deployment to continuously validate API performance.

---
### Model can be quickly replaced by business rules or another in case on emergency without service interruption
**Level:** Level 4 | **Pillar:** DELIVERY | **Topic:** Service Availability

### What is expected
 Implement mechanisms to quickly replace models with business rules or alternative models in emergencies, ensuring no service interruption.







---
### Model card(s) filled, deployed and accessible.
**Level:** Level 4 | **Pillar:** DELIVERY | **Topic:** Documentation

### What is expected
 Model cards should be thoroughly filled out with detailed information about the model, deployed to the appropriate environment, and made accessible to relevant stakeholders for review and use.

---
### I use scripts to manage infrastructure changes (ideally Python)
**Level:** Level 1 | **Pillar:** INFRA | **Topic:** Configuration / Infra Management

### What is expected ?
Your infrastructure is provisioned by a tool that is not terraform (python script and associated libraries or equivalent).

---
### I use Github as a source code repository for my infra
**Level:** Level 1 | **Pillar:** INFRA | **Topic:** Configuration / Infra Management

### What is expected ?
The source code is hosted in github repository. This github repository also contains the data that, coupled with the tool source code, represents the source of truth.The source code is hosted in github repository. This github repository also contains the data that, coupled with the tool source code, represents the source of truth.

---
### I automate Server/VM changes through a validated Configuration Tool (Ansible or Puppet) and/or Infra changes through a validated IaC tool (Terraform (Enterprise or CPE Github Actions workflows))
**Level:** Level 2 | **Pillar:** INFRA | **Topic:** Configuration / Infra Management

### What is expected ?
All infrastructure components are provisioned by Terraform using CPE provided standard model/provider. The terraform runs are performed by one of the validated tools, i.e. Terraform Enterprise or Github Actions. All the instances of your infrastructure are managed by a govtech validated configuration management tool (Puppet). All the changes go through a validation process (Pull Request).

---
### I use Github as a source code repository for my infra and changes go through a validation process (Pull request)
**Level:** Level 2 | **Pillar:** INFRA | **Topic:** Configuration / Infra Management

### What is expected ?
The infrastructure code is stored in a Github repository. All modifications to this code must pass through a validation process (Pull Request) before being merged and deployed.

---
### I follow the FinOPS and Green IT best practices provided by CPE
**Level:** Level 2 | **Pillar:** INFRA | **Topic:** Configuration / Infra Management

### What is expected ?
Your team actively applies the FinOps and Green IT best practices and recommendations provided by CPE to optimize costs and reduce environmental impact.

---
### I automate Infra changes through a govtech validated platform offer (3S Stack, CloudKraft, Packaged offers from INIX, SAPTech, China, India....)

**Level:** Level 3 | **Pillar:** INFRA | **Topic:** Configuration / Infra Management

### What is expected ?
Automate Infra changes through a govtech validated platform offer (Stack of the CPE unit, Packaged offers from INIX, China, India, Member, B&Rf....) (OK)


---
### I have FinOps/GreenOPS tracking in infrastructure with a monthly follow up and I have at least one GreenIT KPI
**Level:** Level 3 | **Pillar:** INFRA | **Topic:** Configuration / Infra Management

### What is expected ?
FinOps and GreenOps tracking, including at least one Green IT KPI, are in place for the infrastructure, with regular monthly follow-ups to monitor and report performance.

---
### My source code is free of machine-to-machine secrets (YES)
or already compliant with a higher Secrets Management level (NA)
**Level:** Level 1 | **Pillar:** INFRA | **Topic:** Secrets Management

### What is expected ?
There is no secret in a public file (github protected repositories are considered public for all DKT users). Your machine to machine secrets are at least in a private file, outside of version control or in your CI configuration. No secret are hardcoded in your code.

---
### I store my machine-to-machine secrets in a specific secret management tool (like Vault, GCP or AWS Secret Manager) (YES)
or already compliant with a higher Secrets Management level (NA)
**Level:** Level 2 | **Pillar:** INFRA | **Topic:** Secrets Management

### What is expected ?
There is no secret in your code and you removed the secrets from your application and/or CI. You retrieve them from a secret management tool using workload identity, connecting to Vault with token exchange (from github token, GCP SA, AWS role, etc.).

---
### I store my machine-to-machine secrets in Vault Enterprise (YES)
**Level:** Level 3 | **Pillar:** INFRA | **Topic:** Secrets Management

### What is expected?
Your secrets are stored in Vault Enterprise. Secrets are injected as Kubernetes secrets, environment variables or temporary files using tools like Vault agent, the Vault or External Secrets operators or synced to cloud providers secret managers for serverless workloads. You can easily rotate your secrets by updating them in the Secret Engine, triggering a redeployment or an update of the workload that consume them.

---
### I store my machine-to-machine secrets with K8S secrets or Cloud provider secret manager or github secrets or Vault and injected as infra init or env variable (OK)
I rotate my secret based on ISSP requirements (6 month in ISSP)
or higher Secrets Management level (NA)
**Level:** Level 3 | **Pillar:** INFRA | **Topic:** Secrets Management

### What is expected ?
Your secrets are stored in a secret manager (Hashicorp Vault, ...). Secrets are injected into your infrastructure ( via init-container, injected as environment variable or temporary files via tools like external-secret or Vault agent... ). You can easily rotate your secrets by updating them in the Secret Engine and triggering a redeployment of the workload that consume them.

---
### My M2M secrets are injected as Kubernetes secrets, environment variables or temporary files using tools like the Vault or External Secrets operators or synced to cloud providers secret managers for serverless workloads
**Level:** Level 3 | **Pillar:** INFRA | **Topic:** Secrets Management

### What is expected?
Your secrets are stored in Vault Enterprise. Secrets are injected as Kubernetes secrets, environment variables or temporary files using tools like Vault agent, the Vault or External Secrets operators or synced to cloud providers secret managers for serverless workloads. You can easily rotate your secrets by updating them in the Secret Engine, triggering a redeployment or an update of the workload that consume them."

---
### I rotate my M2M secrets based on ISSP requirements (180 days in ISSP) or better
**Level:** Level 3 | **Pillar:** INFRA | **Topic:** Secrets Management

Your secrets are stored in Vault Enterprise. Secrets are injected as Kubernetes secrets environment variables or temporary files using tools like Vault agent.
The Vault or External Secrets operators or synced to cloud providers secret managers for serverless workloads. You can easily rotate your secrets by updating them in the Secret Engine

---
### My secrets are rotated automatically
**Level:** Level 4 | **Pillar:** INFRA | **Topic:** Secrets Management

### What is expected ?
Your secrets are rotated automatically by the secret management tool (e.g., Hashicorp Vault, Cloud Secret Manager features) according to predefined security policies and rotation schedules (e.g., based on ISSP requirements or better). This rotation process is integrated with your workloads (e.g., via Vault Agent, External Secrets Operator, or Cloud-native features) to ensure seamless and zero-downtime updates of secrets used by applications and infrastructure.



---
### Secrets retrieval is handled by the application and secrets are stored in memory (not in files, environment variables or Kubernetes secrets).
**Level:** Level 5 | **Pillar:** INFRA | **Topic:** Secrets Management

### What is expected ?
Your application connects directly to the secret manager (via workload identity or vault token or equivalent way). Application supports hot updates of those secrets and can even trigger/request secret rotation if needed (short lived secrets to access database for instance)

---
### My secrets are rotated automatically and short-lived. They are only pulled when needed from the secret manager and only cached for a short time (minutes)
**Level:** Level 5 | **Pillar:** INFRA | **Topic:** Secrets Management

### What is expected ?
Application supports hot updates of those secrets and can even trigger/request secret rotation if needed (short lived secrets to access database for instance).

---
### When possible, passwordless authentication is leveraged, using Workload Identity with ou without Decathlon's Fedid (ex: MongoDB, CloudSQL)
**Level:** Level 5 | **Pillar:** INFRA | **Topic:** Secrets Management

### What is expected ?
Credentials are no longer provided, a trust mechanism using workload identity and/or Decathlon Fedid is used to authenticate and authorize workloads

---
### I store my machine-to-machine secrets in Vault Enterprise (YES)
or already compliant with a higher Secrets Management level (NA)
**Level:** Level 4 | **Pillar:** INFRA | **Topic:** Secrets Management

Your secrets are rotated automatically by the secret management tool (e.g.

---
### I store my machine-to-machine secrets in Vault Enterprise solution.(OK)
My secrets are only accessible in memory space
**Level:** Level 4 | **Pillar:** INFRA | **Topic:** Secrets Management

### What is expected ?
Your application connects directly to the secret manager (via workload identity or vault token or equivalent way ) and pull secrets directly from there. The secrets are available as environment variable or mounted files in containers.

---
### Hosted in referenced private cloud (YES)
or higher Hosting Solution level (NA)
**Level:** Level 1 | **Pillar:** INFRA | **Topic:** Hosting Solution

### What is expected ?
Your application is hosted in the private cloud referenced by govtech, you must not have any application host in a physical server on your side. If you have any doubt, please reach the slack chan #sig-infra-support

---
### Hosted in referenced public cloud (GCP, AWS, Alicloud or Azure (China only)) under the DKT contract (YES)
or higher Hosting Solution level (NA)
**Level:** Level 2 | **Pillar:** INFRA | **Topic:** Hosting Solution

### What is expected ?
Your application is hosted in the public cloud as GCP/AWS/AliCloud/Azure( china only) under the decathlon contract, the region you've chosen is a validated ( by CPE ) landing zone. Please refer to the tech radar for the list of clouders supported.  Please refer to the tech radar for the list of OS and middleware supported. If you have any doubt, please reach the slack chan #sig-infra-support

---
### Hosted in a govtech validated platform offer (3S Stack, Cloudkraft, SAPTech, optionally packaged by INIX, Decatec, China, India, etc.) (YES)
**Level:** Level 3 | **Pillar:** INFRA | **Topic:** Hosting Solution

### What is expected ?
Your application is hosted in the govtech validated platform such as 3S stack, Packaged offers from inix, China, India, Member, OCO, B&Rf, etc) , you must not host your applications in a standalone or managed account outside of these platforms. If you have any doubt, please reach the slack chan #sig-infra-support

---
### Hosted in a govtech validated platform offer (3S Stack, Cloudkraft, SAPTech, optionally packaged by INIX, Decatec, China, India, etc.) and in a supported version, complying with the release lifecycle (YES)
**Level:** Level 4 | **Pillar:** INFRA | **Topic:** Hosting Solution

### What is expected ?
You are able to deploy your application on a frequently updated platform. This practice allows you to maintain support and required security level while taking advantage of the latest functionalities.  IE : I am on a supported version of the 3S stack and I upgrade my stack every quarter.
If you have any doubt, please reach the slack chan #sig-infra-support

---
### My app is hosted on virtual machines without autoscaling (YES)
 or higher cloud native level (NA)
**Level:** Level 1 | **Pillar:** INFRA | **Topic:** Cloud Native Design

### What is expected ?
Your applications are hosted at least on a VM based on a middleware ( e.g. Tomcat, Weblogic (only Cube and Eone) ).  Please refer to the tech radar for the list of OS and middleware supported. If you have any doubt, please reach the slack chan #sig-infra-support

---
### My app is hosted on virtual machines with autoscaling activated (YES)
 or higher cloud native level (NA)
**Level:** Level 2 | **Pillar:** INFRA | **Topic:** Cloud Native Design

### What is expected ?
Your applications are hosted at least on a VM based on a middleware ( e.g. Tomcat ) who supports horizontal autoscaling, meaning when the application needs more resources, the hosting mechanism can add one or more VM to absorb the charge.  Please refer to the tech radar for the list of OS and middleware supported. If you have any doubt, please reach the slack chan #sig-infra-support

---
### My app is hosted on virtual machines with autoscalling activated using only golden images (OK)
 or higher cloud native level (NA)
**Level:** Level 3 | **Pillar:** INFRA | **Topic:** Cloud Native Design

### What is expected ?
Your applications is hosted at least on a VM based on a middleware ( e.g. Tomcat ) who support the horizontal autoscaling, all the CD is done through golden images. Puppet and config management tooling are not deployed. that's mean when the application needs more resources, the hosting mechanism can add one or more VM to absorb the charge in very short delays.  Please refer to the tech radar for the list of OS and middleware supported. If you have any doubt, please reach the slack chan #sig-infra-support

---
### My app is hosted on K8S or serverless without autoscaling (YES)
**Level:** Level 3 | **Pillar:** INFRA | **Topic:** Cloud Native Design

### What is expected ?
Your applications are hosted at least in GovTech validated K8S cluster ( e.g. GKE, EKS, AKS ) or serverless platform ( e.g.  CloudRun, CloudFunction, Lamda, etc).  Please refer to the tech radar for the list of containerisation and serverless technologies supported. If you have any doubt, please reach the slack chan #sig-infra-support

---
### My app is hosted on K8S or serverless with autoscaling for most workloads (ex: HPA, VPA, KEDA, etc.) (YES)
**Level:** Level 4 | **Pillar:** INFRA | **Topic:** Cloud Native Design

### What is expected ?
Your Kubernetes workloads are using autoscaling to adapt their size or number of instances to the incoming load. This helps managing spikes of incoming load and reduces greatly the overprovisionning of costly cloud resources.

---
### My app is hosted on Serverless or Kubernetes with workload autoscaling and smart autoscaling of nodes (Compute Classes, Karpenter, etc.)
**Level:** Level 5 | **Pillar:** INFRA | **Topic:** Cloud Native Design

### What is expected ?
In addition to Kubernetes workload autoscaling, a smart node autoscaling (GKE compute classes or Karpenter) solution is in place to optimize the size and number of nodes

---
### DEPLOYMENT

My database is manually installed in a server or VM. (Yes) or better automation (N/A)
**Level:** Level 1 | **Pillar:** INFRA | **Topic:** Database Management

**Why ?**

Manual installation is often the starting point, but it increases variability between environments and makes recovery and scaling harder. This level exists mainly to acknowledge the baseline and to highlight why automation becomes important at higher levels.

**What ?**

A database instance is provisioned by hand (OS packages, configuration, users, storage, network rules) on a VM or server. The setup may not be fully reproducible.

**How ?**

- Document the installation steps (commands, versions, parameters, ports, firewall rules).
- Record where credentials and configuration live (vault, secrets manager, files, etc.).
- Ensure there is at least minimal operational ownership (who can rebuild it, where is the runbook).

---
### BACKUPS

My data is manually backuped by someone regularly (Yes) or better automation (N/A)
**Level:** Level 1 | **Pillar:** INFRA | **Topic:** Database Management

**Why ?**

Backups are the foundation of resilience. Manual backups are better than none, but they are error-prone (missed schedules, incomplete scope, frequently poorly protected (stored on the same server, not encrypted, not tested) and rarely tested for restoration capability.

**What ?**

A person triggers backups periodically (dump/snapshot/export) and stores them somewhere, likely in the same server, with limited guarantees on frequency, retention, integrity, or restorability.

**How ?**

- Define a minimum backup frequency (daily/weekly) and retention (e.g., 7/30/90 days).
- Store backups outside the database host whenever possible.
- Document a basic restore procedure (even if restore tests are not regular yet).

---
### DEPLOYMENT

My Database services are installed in servers or VMs with scripts-based automations (Bash/Python, cron, etc.) (Yes) or better (N/A)
**Level:** Level 2 | **Pillar:** INFRA | **Topic:** Database Management

**Why ?**

Scripted setup increases repeatability and reduces reliance on tribal knowledge. It is a stepping stone toward Infrastructure as Code and platform-managed services.

**What ?**

Database provisioning and configuration are automated via scripts (install packages, configure parameters, create users/schemas, open ports, attach disks).

**How ?**

- Store scripts in version control.
- Make scripts idempotent where possible (safe to run multiple times).
- Parameterize environment-specific values (ports, instance size, storage path).
- Add a simple “create + verify” routine (health check, connection test).

---
### BACKUPS

My databases are automatically backuped and the backups are stored outside the database server.(Yes)
**Level:** Level 2 | **Pillar:** INFRA | **Topic:** Database Management

**Why ?**

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

---
### AVAILABILITY

My Database as a simple replication mechanism that I can isolate and redirect apps to in case of loss of my primary instance.
**Level:** Level 2 | **Pillar:** INFRA | **Topic:** Database Management

**Why ?**

Replication reduces downtime and data loss risk. Even manual failover is a major improvement over a single-instance database as it guarantees a near-zero RPO with a decent RTO.

**What ?**

A secondary replica exists (read replica or standby). In case of primary failure, the team can promote and redirect manually.

**How ?**

- Configure replication (streaming/log shipping/cluster replica, depending on DB).
- Document a failover runbook: detect → isolate primary → promote replica → update DNS/service config → verify app.
- Regularly verify replication lag and replica health. (can be delegated to Aiven)
- Practice at least one failover exercise per year (even if failover is not automated yet).

---
### DEPLOYMENT

My Database services are deployed with Infrastructure as Code (Terraform, Ansible) including 3S or other govtech-compliant platforms (Yes)
**Level:** Level 3 | **Pillar:** INFRA | **Topic:** Database Management

*Why ?**

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

---
### BACKUPS

My databases are automatically backuped, the backups are stored outside the database server and I'm running regular restoration tests.
**Level:** Level 3 | **Pillar:** INFRA | **Topic:** Database Management

**Why ?**

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

---
### AVAILABILITY

My database replicas have automatic Failover systems that provide HA
**Level:** Level 3 | **Pillar:** INFRA | **Topic:** Database Management

**Why ?**

Automatic failover reduces downtime and human error during incidents, and standardizes recovery behavior.

**What ?**

High availability is achieved with automatic detection and failover (managed DB multi-AZ, cluster managers, orchestrators).

**How ?**

- Prefer managed HA features where available.
- Define health checks and failover criteria.
- Ensure applications use a stable endpoint (cluster endpoint, proxy, VIP, DNS).
- Monitor failover events and test failover periodically.


---
### DEPLOYMENT

In addition to Infra as code, the Schema of my Database services is manages with automated migration solutions (Flyway) included in my apps' CI/CD
**Level:** Level 4 | **Pillar:** INFRA | **Topic:** Database Management

**Why ?**

Schema drift is a common cause of outages. Versioned migrations provide controlled evolution, reviewability, and safer deployments.

**What ?**

Database schema changes are versioned, reviewed, and applied automatically through CI/CD using a migration tool (Flyway, see Tech Radar).

**How ?**

- Store migration scripts alongside application code.
- Run migrations in the pipeline with clear ordering/versioning.
- Leverage forward/backward compatibility when possible to decouple code and schema upgrades.
- Add checks : “migration applied”, “schema version is X”.
- Define rollback strategy (down migrations when safe, or forward-fix strategy, plus backups before risky changes).

---
### BACKUPS

My databases are automatically backuped, the backups are stored outside the database server as immutable files (WORM), I'm running regular restoration tests and RTO/RPO are close to zero (PITR).
**Level:** Level 4 | **Pillar:** INFRA | **Topic:** Database Management

**Why ?**

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


---
### AVAILABILITY

My database allows cross-region failover architectures with automatic recovery.
**Level:** Level 4 | **Pillar:** INFRA | **Topic:** Database Management

**Why?**

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


---
### AVAILABILITY

My database allows active-active architectures with automatic recovery.
**Level:** Level 5 | **Pillar:** INFRA | **Topic:** Database Management

**Why?**

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


---
### Local storage on servers (YES)
or higher (NA)
**Level:** Level 1 | **Pillar:** INFRA | **Topic:** Storage Management (for unstructured data)

### What is expected ?
Your VM/Container/K8S has at least a local storage, your files and other configuration are stored at least on this local storage.

---
### Server based file sharing (YES)
or higher  (NA)
**Level:** Level 2 | **Pillar:** INFRA | **Topic:** Storage Management (for unstructured data)

### What is expected ?
Your VM/Container/K8S has at least a server based storage, your files and other configuration are stored at least on this file sharing storage.

---
### Third party based software on IaaS to share files (YES)
or higher (NA)
**Level:** Level 3 | **Pillar:** INFRA | **Topic:** Storage Management (for unstructured data)

### What is expected ?
Your VM/Container/K8S cluster/serverless has at least a govtech validated third party based file sharing system.

---
### Cloud Provider object storage (S3, cloud storage...) with lifecycle management enabled (YES)
or higher (NA)
**Level:** Level 4 | **Pillar:** INFRA | **Topic:** Storage Management (for unstructured data)

### What is expected ?
Your VM/Container/K8S cluster/serverless has at least a govtech validated cloud provider object storage system such as S3, Cloud storage, Azure Cloud Storage, etc with a lifecycle management provided by cloud provider.

---
### Cloud Provider object storage (S3, cloud storage...) with enhanced security (WORM protection, multiregionnal...) and lifecycle management (YES)
**Level:** Level 5 | **Pillar:** INFRA | **Topic:** Storage Management (for unstructured data)

### What is expected ?
Your VM/Container/K8S cluster/serverless has at least a govtech validated cloud provider object storage system such as S3, Cloud storage, Azure Cloud Storage, etc with a lifecycle management provided by cloud provider, and it has at least an enhanced security level such as WORM protection, multiregions configuration.

---
### Solution developed used services that are validated by infrastructure and architecture teams
**Level:** Level 1 | **Pillar:** INFRA | **Topic:** Reproducibility

### What is expected?
The solution must utilize services that have been pre-approved and validated by the infrastructure and architecture teams to ensure compliance with organizational standards and best practices (see Technical Desgin Review process)

---
### Part of infrastructure is defined as code, later referenced as IaC (Infrastructure as Code). 
**Level:** Level 2 | **Pillar:** INFRA | **Topic:** Reproducibility

What is expected?
The infrastructure should be defined using code (terraform), enabling automated provisioning, management, and versioning of infrastructure resources.

---
### IaC is stored in a version control system (e.g. github repository)
**Level:** Level 2 | **Pillar:** INFRA | **Topic:** Reproducibility

### What is expected?
The Infrastructure as Code (IaC) should be stored in a version control system such as GitHub to facilitate collaboration, versioning, and tracking of changes

---
### S-MAX (optional) process is used to create changes in IaC thank to the help of dataops team.
**Level:** Level 2 | **Pillar:** INFRA | **Topic:** Reproducibility

### What is expected ?
Changes to Infrastructure as Code (IaC) should be managed through the S-MAX process with assistance from the DataOps team, ensuring controlled and efficient updates.
S-Max - https://github.com/dktunited/dataops-terraform-infra-projects

---
### Services used doesnot contain operation team names (we are following product convention).
**Level:** Level 2 | **Pillar:** INFRA | **Topic:** Reproducibility

### What is expected ?
Services should be named according to the product convention rather than including operation team names to maintain consistency and clarity in service identification.

---
### Project code and support group are defined.
**Level:** Level 2 | **Pillar:** INFRA | **Topic:** Reproducibility

### What is expected ?
The project code and associated support group must be clearly defined to ensure accountability and proper management of the project.

---
### Role IAM are not using any manually added custom policy.
**Level:** Level 3 | **Pillar:** INFRA | **Topic:** Reproducibility

### What is expected ?
IAM roles should not include manually added custom policies, promoting the use of standardized and pre-approved policy sets for security and consistency.

---
### All AI Product Infrastructure is defined as code, and using the Terraform modules provided by dataops team based on AI product strategy (dedicated role for the product).
**Level:** Level 3 | **Pillar:** INFRA | **Topic:** Reproducibility

### What is expected ?
All AI product infrastructure should be defined using code, specifically leveraging Terraform modules provided by the DataOps team, aligned with the AI product strategy and dedicated roles.
https://dataplatform-access-management.dktapp.cloud/

---
### Data and ML pipeline should have at least two environments (preproduction and production) which are exact copies of each other.
ML model exposition should have differents environments
**Level:** Level 3 | **Pillar:** INFRA | **Topic:** Reproducibility

### What is expected ?
The data and ML pipelines must include at least two environments, preproduction and production, which are exact replicas to ensure consistent testing and deployment.
Machine Learning models should be deployed in multiple environments to ensure proper testing, staging, and production workflows.

---
### All environments related to a AI Product should have access to production data (data should be the same at any moment of time).
**Level:** Level 3 | **Pillar:** INFRA | **Topic:** Reproducibility

### What is expected ?
All environments associated with an AI product must have access to production data, ensuring data consistency across environments at all times.

---
### Technical review has proposed time of ops people for creating quickly all ressources we need with dataops team.
**Level:** Level 3 | **Pillar:** INFRA | **Topic:** Reproducibility

### What is expected ?
A technical review should allocate time for ops in order to collaborate with the DataOps team in swiftly creating all necessary resources.

---
### My product (ML API) is hosted on K8S or serverless.
**Level:** Level 4 | **Pillar:** INFRA | **Topic:** Reproducibility

### What is expected ?
The Machine Learning API product should be hosted on Kubernetes (K8S) or a serverless platform, aligning with modern infrastructure practices.

---
### Pull request on terraform git repo process is used to create changes in IaC. Team are autonomous.
**Level:** Level 5 | **Pillar:** INFRA | **Topic:** Reproducibility

### What is expected ?
Changes to Infrastructure as Code (IaC) should be made through a pull request process in the Terraform Git repository, allowing teams to work autonomously while ensuring code review and version control.

---
### Place holder: please validate
**Level:** Level 1 | **Pillar:** INFRA | **Topic:** Security

TBD

---
### Data used is encrypted (e.g. with KMS on s3).
**Level:** Level 2 | **Pillar:** INFRA | **Topic:** Security

### What
Data encryption involves using cryptographic techniques to secure data, such as encrypting data stored in S3 using Key Management Service (KMS).
### Why
To protect sensitive information, ensure data privacy, and comply with regulatory requirements.
### How
 Use AWS KMS to manage encryption keys and configure S3 bucket settings to enable server-side encryption with KMS. Regularly audit and review encryption settings to ensure compliance.

---
### As soon as managed solutions is provided by cloud provider, we donot use alternative (e.g. no cloud provider managed deployment)
**Level:** Level 3 | **Pillar:** INFRA | **Topic:** Security

### What
When a managed solution is available from the cloud provider, it should be used instead of alternative, non-managed deployments.
### Why
Managed solutions offer built-in scalability, security, and maintenance, reducing operational overhead and risk.
### How
 Identify managed services provided by the cloud provider that fit project requirements. Replace non-managed deployments with these services, ensuring configuration aligns with best practices and project needs.

---
### Latest version (or supported version) of Python is used.
**Level:** Level 3 | **Pillar:** INFRA | **Topic:** Security

### What
The project should use the latest or a currently supported version of Python.
### Why
To ensure compatibility, receive security updates, and leverage new features and improvements.
### How
Regularly check the Python status at Python status and upgrade the Python version used in the project. Implement version checks in CI/CD pipelines to enforce usage of supported versions.
Python status: https://devguide.python.org/versions/

---
### Latest versions of packages dependencies are used.
**Level:** Level 3 | **Pillar:** INFRA | **Topic:** Security

### What
Dependencies should be regularly updated to their latest versions.
### Why
To benefit from security patches, bug fixes, and feature enhancements.
### How
Use tools like pip-review or pip-upgrade to identify and upgrade outdated Python packages. Schedule regular maintenance windows to perform these upgrades and test for compatibility.

Upgrade python module used regularly

---
### Estimate with you security champion or security team, the criticity of your project and list your project into EGERIE if it is relevant.
**Level:** Level 3 | **Pillar:** INFRA | **Topic:** Security

### What
Assess the criticality of the project with a security expert and register it in EGERIE if necessary.
### Why
To ensure proper security measures are in place based on project risk and criticality.
### How
Use the Tech Radar security checklist available here to evaluate security requirements and consult with the security team for assessment and registration.
Tech radar security checklist: https://docs.google.com/spreadsheets/d/1DBOodOlr1WVI1O0202mqcixMdvVg8_TFeulvckABHPg/edit?gid=0#gid=0

---
### Container are regulary re built to handle security issues.
**Level:** Level 3 | **Pillar:** INFRA | **Topic:** Security

### What
Containers should be periodically rebuilt to incorporate the latest security updates and patches.
### Why
To mitigate vulnerabilities and ensure containers remain secure.
### How
Automate the container rebuild process using CI/CD pipelines. Schedule regular rebuilds and deployments, integrating vulnerability scanning tools like Clair or Trivy to detect and address security issues.

---
### Dependencies are regularly rebuilt with latest versions of python modules.
**Level:** Level 4 | **Pillar:** INFRA | **Topic:** Security

### What
Dependencies should be regularly updated and rebuilt with the latest Python modules.
### Why
To ensure the application uses the most secure and efficient versions of dependencies.
### How
Automate dependency updates using tools like Dependabot. Schedule regular rebuilds and run tests to verify compatibility and functionality.

---
### Pentest has been done (API audit needed for public exposition).
**Level:** Level 4 | **Pillar:** INFRA | **Topic:** Security

### What
A penetration test (pentest) should be conducted, especially for publicly exposed APIs, to identify and address security vulnerabilities.
### Why
To proactively find and fix security flaws, ensuring the API is secure from attacks.
### How
Engage a professional pentesting service or an internal security team to perform the audit. Review and address the findings, implementing necessary security measures and improvements.

---
### If project is open sourced we are following security standards.
**Level:** Level 5 | **Pillar:** INFRA | **Topic:** Security

## What
When a managed solution is available from the cloud provider, it should be used instead of alternative, non-managed deployments.
### Why
Managed solutions offer built-in scalability, security, and maintenance, reducing operational overhead and risk.
### How
Identify managed services provided by the cloud provider that fit project requirements. Replace non-managed deployments with these services, ensuring configuration aligns with best practices and project needs.
Contact corentin.vasseur@decathlon.com
Standard: https://docs.google.com/document/d/1VeZOKAPHrN11Kv4XTrfkVs0BDo0p63po/edit
Useful links: https://github.com/mikeroyal/Open-Source-Security-Guide | https://github.com/guardrailsio/awesome-python-security

---
### Integration tests covers all the application features
**Level:** Level 4 | **Pillar:** QUALITY | **Topic:** Integration Tests

### Why ?

In complement to "All critical integration tests are automated and run in CI', having all features covered by tests allows the team to deploy as soon as the PR is merged.

### What ?

To fulfill this requirement, all automatable features must have tests implemented and they are executed in Continuous Integration for each PR.

### How ?

The team must be able to demonstrate, for each PR, that all tests have been implemented and run within the CI.

---
### Load testing run blocks a deployment in production if they fail
**Level:** Level 4 | **Pillar:** QUALITY | **Topic:** Performance Tests

### Why ?

To ensure performance is stable or improved throught the applicative changes and to automate the testing process.

### What ?

Prepare specifics CI scenarios with low api calls volume and a short duration that are ran after the integration tests.

### How ?

- Create a 1 to 2 min scenarios with a volume close to your production environment
- Trigger it add the end of the deployment process
- Add assertions to this specific scenario like success rate, response time associated to a percentil
- the assertions must block the deployment if not fulfilled

---
### Continuous Load tests run in CI at the PR level
**Level:** Level 4 | **Pillar:** QUALITY | **Topic:** Performance Tests

### Why ?

To ensure that performance is stable or improved by application changes, and to automate the testing process as quickly as possible.

### What ?

Prepare specifics CI scenarios with low api calls volume and a short duration that are ran after the integration tests.

### How ?

- Create a 2 to 3 min scenarios with a volume close to your production environment
-Trigger it at the end of the deployment process on ephemeral environment
- Add assertions to this specific scenario like success rate, response time associated to a percentil (e.g. p95, p90…)
- The assertions do not block the merge of the PR if not fulfilled

Warning: use dedicated injectors (private injectors for internal app) and not the GitHub runners because of the flakiness!

---
### Use Test Driven Development (TDD) during development tasks
**Level:** Level 4 | **Pillar:** QUALITY | **Topic:** Practices

### Why ?

Develop highly usable software, reduce bugs, identify functionality issues, avoid code duplication, simplify code, check the quality of the code, create extensible software, provide quick feedback, create up-to-date code documentation, shorten the development time to market.

### What ?

Drive your conception and your development by the tests.

### How ?

1. We first write the test case that we want to develop.
2. We launch the test which must necessarily fail
3. We just write the code that responds to this case
4. We launch the test which must pass if this is not the case we go back to step 3. If the test passes we write the following test case.
5. We can refactor our code by rerunning the test to check that it still works. The test should not be modified.

---
### Implement a zero bug policy
**Level:** Level 4 | **Pillar:** QUALITY | **Topic:** Practices

### Why ?

The 0 Bug Policy is justified by the increasing costs and complexities associated with deferring bug fixes. Accumulating a backlog of unresolved bugs creates a technical debt that becomes increasingly difficult to manage over time. Postponing fixes leads to a loss of context for developers who may forget the details of the bug, a source code that evolves and makes it harder to identify the root cause, and an ever-increasing bug triage and prioritization time. This accumulation of undone work burdens teams' mental load, lengthens the time between bug discovery and resolution, and globally increases the effort required to fix them.  The 0 Bug Policy, therefore, aims to avoid this snowball effect by dealing with bugs immediately.

### What ?

The 0 Bug Policy is based on a simple and radical rule: when a bug is discovered, it must be fixed immediately or permanently closed as "won't fix." This approach focuses on immediate action in the face of bugs, eliminating the option of postponing them.  The goal is not to achieve an illusory perfection with absolutely no bugs, but rather to maintain a light and adaptable workflow by actively addressing each identified bug. By freeing themselves from the weight of accumulated bugs, teams can focus on building robust and higher quality code, thereby fostering a culture of quality within development.

### How ?

Implementing the 0 Bug Policy requires addressing certain concerns. The fear of losing bugs can be mitigated by a well-maintained work management system that keeps the history of closed bugs in case they reappear. The difficulty of prioritizing bug fixes over new features must be managed through transparent communication and a shared understanding of the benefits of this policy. Finally, the risk of fixing or closing bugs too quickly without thorough analysis can be avoided by encouraging open communication, rigorous root cause analysis, and involving business experts and cross-functional teams to ensure effective bug resolution that balances speed and diligence.

---
### Testing is developer-driven, not a separate function
**Level:** Level 4 | **Pillar:** QUALITY | **Topic:** Practices

### Why?

"You build it, you run it" extends to "you test it." Separating development from testing creates silos and delays. By integrating testing directly into the development workflow, we empower developers to take full ownership of the quality of their work. This fosters a culture of continuous improvement and shared responsibility.

### What?

Every developer is a quality advocate, actively participating in the design and execution of functional and non-functional tests. This requires a strong understanding of testing principles and a commitment to apply the quality approach shared within the team.

### How?

Teams without dedicated QA/QE demonstrate developer ownership of quality by managing all testing activities, from design to execution, across all test levels (unit, integration, end-to-end) and types (performance, security).

---
### Use quality metrics to improve efficiency
**Level:** Level 4 | **Pillar:** QUALITY | **Topic:** Qualimetry

### Why ?

Any changes to the quality management system and the delivery chain must be measured so that they can be maintained or eliminated.
The ability to constantly observe measurements is useful in establishing a lean attitude.

### What ?

Observe macro measures (DDE, DRE, DAA, …) and micro measures (code coverage, static code analysis measures, test coverage, ...) and define their thresholds. Team must be focused on these thresholds to be above them.

### How ?

For each metric that composes its quality management system, the team:

- has a full and available overview.

- has defined thresholds.

- systematically puts in place a placeholder for analysis. For each metric that fails to meet the objective, one or more actions are proposed and the actions are monitored, retained or abandoned depending on the time devoted to the experiment.

- has a live tracking to alert (by sending a message to slack, by creating a bug in jira, …) when a metric is downgraded.

---
### Static Code Analysis threshold must match or exceed high software industry standard on overall code
**Level:** Level 4 | **Pillar:** QUALITY | **Topic:** Static Code Analysis

### Why ?

Ensuring that static code analysis indicators are always at a high level enable to deliver code matching high standard of code quality continuously and keep the technical debt manageable.

### What ?

To fulfill this requirement, the SonarCloud profile must be set to "Sonar Way" on the overall code.

### How ?

The team must be able to demonstrate that the SonarCloud analysis profile is "Sonar Way" on the overall code.

---
### Unit tests coverage threshold must match or exceed high software industry standard on overall code
**Level:** Level 4 | **Pillar:** QUALITY | **Topic:** Unit Tests

### Why ?

Ensuring the unit tests coverage stays at a minimum level enable to deliver tested code continously and keep the technical debt manageable.

### What ?

To fulfill this requirement, the unit tests coverage must be enforced at 80%, as it is instructed by Sonar Cloud on the overall code.

### How ?

The team must be able to demonstrate that, for every PR, the coverage is measured and enforced at a minimum of 80% on the overall code.

---
### RISKS:
Conduct regular risks mitigation tests
**Level:** Level 4 | **Pillar:** OPERATION | **Topic:** Availability / Risk Management

### Expected
* The risks are simulated and remediations are tested at least once a year in prod
* Risks encountered during the year are formalized in the document to update and define action to do
* Risks template filled by the team (Tabs to fill : "Applicative Risk Management", colum Real Life - Tested or last occurencies")

### Useful link
* [Risks template](https://docs.google.com/spreadsheets/d/1-FRU-iAhapahyNSGb1iN3-QweN2OzEj0k4Yo7lBLljc/edit?gid=2140616589#gid=2140616589)

### Example
* [Stock Reliability - DRP&Risks file](https://docs.google.com/spreadsheets/d/14vJiZc1uj4qzwgbXHO-UeeugKOGdGPqlQKogChtjnQw/edit?gid=0#gid=0)

---
### ON-CALL DUTY :
Optimize the duty triggering process
**Level:** Level 4 | **Pillar:** OPERATION | **Topic:** Availability / Risk Management

### Expected
* Use multiple methods to improve the way you're being triggered by others
* Perform pre-checks or automate some actions that could avoid been called directly

### Example
* Manage interaction with other team to improve the process
* Make sure you have almost no abusive triggering
* Communicate to the surrounding teams, so that they know the proper service to use
* In case of doubt, make the impacted service the first being called, so it can easily route to the most-likely rootcause service
* Build an automation that could, in case of need, perform an update of Database plan to accept more connexion before triggering directly an on-call engineer (just in case of failure he/she will be triggered)

---
### POST-INTERVENTION:
Organize retex to improve our delivery process on normal changes submitted to CAB approvals
**Level:** Level 4 | **Pillar:** OPERATION | **Topic:** Change Management

### Expected
* After each normal change, you try to improve the process by lowering the impact, improving the intervention duration, and preventing any further unwanted impact (you may also use the Post-Mortem process)
* You think about the possibility and conditions to operate the next similar interventions through standard changes instead of normal ones

---
### ALERTING:
Review alerting configuration twice a year
**Level:** Level 4 | **Pillar:** OPERATION | **Topic:** Event Management

### Expected
* Clean up any useless alert (eg : fixed rootcause)
* Check if the threshold are still relevant (every 6 months + each major change)
* For new incident that may occur again, you need to set up an alert (and associated documentation) to ease the management of the incident
* Alert to incident ratio is measured and challenged

### Useful link
* to create

---
### LOG MANAGEMENT: HTTP errors are named and categorized

**Level:** Level 4 | **Pillar:** OPERATION | **Topic:** Event Management

### Why ?
When user is facing an issue, we display an error code understandable by the user + code error ID and Support groups associated

### What ?
No more error display like "error 500"


### How ?
Display for internal apps , "connexion issue - P02 - CS-INSTORE"
Display for external apps , way to contact CRC / or team in charge of support

---
### LOG MANAGEMENT: (If your are using a BFF) Send error detail to the application
If something goes wrong on your BFF, it should send a dedicated message to the app
**Level:** Level 4 | **Pillar:** OPERATION | **Topic:** Event Management

### Why?
As a BFF is a backend, it should return detailed explanations in case of error to allow the front to understand the issue / fix the usage.

### What?
Every time you have to return an error, add clear explanation in addition to the response code to easily understand what is going wrong.

### How?
Please refer to the backend good practices to manage error responses.

---
### MODEL QUALITY  : Setup advanced checks so that model health is monitored.
**Level:** Level 4 | **Pillar:** OPERATION | **Topic:** Event Management

### What
* Advanced model quality checks involve sophisticated techniques to evaluate machine learning model performance beyond basic metrics.

### Why
* To gain deeper insights into model behavior, identify potential biases, and ensure robust performance in diverse scenarios.

### How
* Implement techniques such as cross-validation, feature importance analysis, and bias detection.
* Use tools like SHAP or LIME for interpretability and fairness checks.
* Set up monitoring for model drift using platforms like TensorFlow Extended (TFX) or AWS SageMaker.
* Document findings and actions taken in a centralized repository.

---
### Deployment - Continuous training is set if it is relevant for the use case.
**Level:** Level 4 | **Pillar:** OPERATION | **Topic:** Event Management

### Expected
Feedback launches retraining, as aforementioned metrics and thresholds trigger actions

---
### CRISIS PROCESS:
Define my own structure / organization in crisis management process
**Level:** Level 4 | **Pillar:** OPERATION | **Topic:** Incident Management

### Expected
* Your team/project has its own organization, defined and coordinated, and the template is properly filled

### Useful link
* [Crisis management](https://decathlon.atlassian.net/wiki/spaces/CRIS/pages/184027245)
* [Crisis template](https://wiki.decathlon.net/display/CRIS/___CRISIS+-+BU+xxxxx+-+TEMPLATE)

### Example
* [___CRISIS - DOMAIN In Store & CC solutions](https://decathlon.atlassian.net/wiki/spaces/CRIS/pages/184026797/___CRISIS+-+DOMAIN+In+Store+CC+solutions)

---
### PROCESSING:
All incidents (including monitoring/observability incident) are logged / managed in the incident database (ITSM Tool)
**Level:** Level 4 | **Pillar:** OPERATION | **Topic:** Incident Management

### Expected
* Alerts are managed by observability tools and when threshold is reached, an incident ticket is generated on ITSM tool (managed recurrencies)

### Useful link
* [Observability Hub documentation](https://decathlon.atlassian.net/wiki/x/poACSQ)

---
### INCIDENTS PROCESS:
Manage my activity to reduce the MTTR value
**Level:** Level 4 | **Pillar:** OPERATION | **Topic:** Incident Management

### Why
* To measure the stability of the product according to "Accelerate" framework.One of those Stability measure is "Mean Time To Recovery"
* Using metrics provided on Delivery Metrics, I organize my activity to try and identify some key points to reduce global MTTR value

### Expected

* You implemented the measure of your mean time to Detect
* You implemented the measure of your mean time to Restore
* You continuously challenge your processes, in order to reduce them, depending on where you can improve.


### Useful link
* Based on MTTR decomposition (see Wiki page named [OPERATIONS - Mean Time To ... (MTTx)](https://decathlon.atlassian.net/wiki/spaces/ENGINEERING/pages/426383988/OPERATIONS+-+Mean+Time+To+...+MTTx), I am able to identify axis were I can performed optimization and save time

### Example
* [InStore - Explanations](https://decathlon.atlassian.net/wiki/x/BIMHZ)

---
### INCIDENTS PROCESS:
Ease the creation, organization, and closure for the incidents by automation
**Level:** Level 4 | **Pillar:** OPERATION | **Topic:** Incident Management

### Why
* Reduce time spent on administrative tasks (like creating tickets, and communication)
* Reduce MTTR
* Increase Team Clarity
* Guarantee Full Process Adherence

### Example
* [Cross-Domain Incident workflow] (https://decathlon.atlassian.net/wiki/x/CIBtbQ)

---
### IMPROVEMENT:
Have repeated sessions (like reliability committee) to improve autonomy and transfer rate
**Level:** Level 4 | **Pillar:** OPERATION | **Topic:** Knowledge / Continuous Improvement Management

### Expected
* Based on training and documented procedure, you're managing improvement sessions with the support groups that help you deal with your activity, like reliability commitee.
* You debrief activity (figures, knowledge, wrong qualification, escalation tree, new feature,...)

### Useful link
* [Reliability commitee (slide 29)](https://docs.google.com/presentation/d/1rLO0t6a4loK8u8WoO7JHgQM2jMN1JLEQTFNmT685teY/edit#slide=id.gf534a5fde1_0_10)

---
### PROCESSING : Product Backlog (defects) is analyzed and definitive solution implemented
**Level:** Level 4 | **Pillar:** OPERATION | **Topic:** Problem Management

### Expected
* Thanks to Product Backlog alimented by Problem, you can work on them to find a definitive solution
* Your team provides definitive solutions to eradicates Known errors, after analysing the rootcause(s)
* Indicator to follow could be the number of problem on SMA-X closed or nmber of Jira defects done

### Useful link
* [Jira tool](https://decathlon.atlassian.net/jira/projects)

---
### POST-MORTEM:
Ensure that the action plans are delivered within the related target date, defined during the postmortem debrief
**Level:** Level 4 | **Pillar:** OPERATION | **Topic:** Problem Management

### Expected
* For all the P1 action plans, the action plans are done in the expected schedule

---
### CATALOG DOCUMENTATION:
Have a service catalog page
**Level:** Level 4 | **Pillar:** OPERATION | **Topic:** Service Catalog Management

### Expected
* Have a page that documents all your services, with at least the name and a description, and as bonus the criticality, the support SLA, the planned availability/reliabiity, and the support processes associated

### Example
* [CubeInStore (CIS) - Helpdesk Knowledge Page](https://decathlon.atlassian.net/wiki/spaces/KDH/pages/307757057/CUBEINSTORE+CIS)
* [Helpdesk - WIKI : Template page (META KT) (2024)](https://decathlon.atlassian.net/wiki/spaces/KDH/pages/292094014/WIKI+Template+page+META+KT+2024)



---
### RELIABILITY:
SLO targets are relevant depending on the Decathlon CUJ (Critical User Journey) I belong
**Level:** Level 4 | **Pillar:** OPERATION | **Topic:** Service Level Management

### Expected
* My SLOs are discussed and aligned with the chain of applications on the CUJ (Critical User Journey)

### Useful link
* [List of Decathlon CUJ and applications](xxx)


---
### RELIABLITY:
Reliability Compliance score is configured
**Level:** Level 4 | **Pillar:** OPERATION | **Topic:** Service Level Management

### Expected
* The SLI(s) are declared in Delivery metrics to get the Reliability Compliance score calculation

### Useful link
* [Score explanation](https://decathlon.atlassian.net/wiki/spaces/TO/pages/476972975/Reliability+Score+-+DORA+metrics)

### Example
* [Onepay v2 in Delivery metrics (Go to Reliability > Reliability compliance](https://delivery-metrics.decathlon.net/scope/benchmark?uuid=5bba9f89-575b-4da1-b00f-aa43a476b55d)

---
### RELIABLITY:
Document the Error Budget Policy of my application
**Level:** Level 4 | **Pillar:** OPERATION | **Topic:** Service Level Management

### Expected
* The Error budget policy for multiple timeframes are documented
* It is recommended (but not mandatory) that the error budget policy for the 28d timeframe has a partial or total freeze impact on your feature releases

### Useful link
* [Error Budget Policy](https://decathlon.atlassian.net/wiki/x/Us4GCw)

### Example
* [NFS example](https://decathlon.atlassian.net/wiki/x/v2JlCw)

---
### SUPPORT SERVICE LEVEL:
Based on activity analysis, I took concrete mid / long term actions
**Level:** Level 4 | **Pillar:** OPERATION | **Topic:** Service Level Management

### Expected
* Have a monthly commitee to analyse the activity of past period, categorizing the incidents/requests/problems to take decisions
* Major objectives are to reduce amount of requests and try to automate as much as possible low value tasks, review of autonomy level is also something important

### Useful link :
* [METRI-X Dashboard](https://lookerstudio.google.com/u/0/reporting/8ebb2d11-cd78-4db9-997a-828e3407fa17/page/9I4fD)

---
### OFFERING:
(If possible) Share the link of create a support ticket directly on my application
**Level:** Level 4 | **Pillar:** OPERATION | **Topic:** Service Request Management

### Expected
* On your application, you linked the offering so that user may reach you easily

### Example
* [Sports Badge application - right left banner](https://sports-badge.dktapp.cloud/)

---
### OFFERING:
Regularly review and adjust my offering fields and rules
**Level:** Level 4 | **Pillar:** OPERATION | **Topic:** Service Request Management

### Expected
* You make sure, at least once a year, that the offering you manage or you're using is up-to-date with your needs, and you potential services evolution
* I review regularly the usage of my offering by checking number of ticket created from it. If it's not used I try to rework it and manage to better communicate it to my users

---
### CODE003 - Internal developers are aware of and responsible for the security of their code. (proof : name of project developer)
* mandatory awareness : 6 modules on [decathlon.ws02-securityeducation.com](https://decathlon.ws02-securityeducation.com) (not open for partner)
**Level:** Level 1 | **Pillar:** SECURITY | **Topic:** Code/Build

**CODE003 Manual Secure Code Review**

[Wiki - CODE003 Manual Secure Code Review](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197463270/CODE003+Manual+Secure+Code+Review)

---
### CODE007 - The team has a Snyk (secure code scanner) directly integrated into the IDE.

\
_Snyk is only available for Application with Criticality Level 3 and 4, use NOT_APPLICABLE for other cases_
**Level:** Level 3 | **Pillar:** SECURITY | **Topic:** Code/Build

**CODE007 Inline IDE Secure Code Analysis**

! Snyk through the IDE is accessible for everyone in DKT (even without SC) !

[Snyk Documentation](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/215222036/Snyk+as+Plugin+in+IDE+VS+Code)

[Wiki - CODE007 Inline IDE Secure Code Analysis](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460393/CODE007+Inline+IDE+Secure+Code+Analysis)

---
### CODE003 - A security champion reviews and validates the pertinent PR from a security point of view.
* proof expected in comments : name of security champion / links from a PR example
**Level:** Level 3 | **Pillar:** SECURITY | **Topic:** Code/Build

**CODE003 Manual Secure Code Review**

[Wiki - CODE003 Manual Secure Code Review](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197463270/CODE003+Manual+Secure+Code+Review)

---
### CODE004 - The team has a Snyk (SAST scanner) built into their application deployment and the results are tracked by the team.
* it's mandatory rule for application with Criticality Level 3 and 4
* at least one scan before each release
* proof expected in comments : "Snyk Dashboard link"

\
_Snyk is only available for Application with Criticality Level 3 and 4, use NOT_APPLICABLE for other cases_
**Level:** Level 2 | **Pillar:** SECURITY | **Topic:** Code/Build

**CODE004 Static Application Security Testing**

[Snyk Documentation](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/205097834/Snyk+SAST+SCA)

[Wiki - CODE004 Static Application Security Testing](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197463261/CODE004+SAST+Static+Application+Security+Testing)

---
### CODE005 - The team has a Snyk (SCA scanner) built into their application deployment and the results are tracked by the team.
* it's mandatory rule for application with Criticality Level 3 and 4
* at least one scan before each release
* proof expected in comments : "Snyk Dashboard link"

\
_Snyk is only available for Application with Criticality Level 3 and 4, use NOT_APPLICABLE for other cases_
**Level:** Level 2 | **Pillar:** SECURITY | **Topic:** Code/Build

**CODE005 SCA Software Composition Analysis**

[Snyk Documentation](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/205097834/Snyk+SAST+SCA)

[Wiki - CODE005 SCA Software Composition Analysis](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460737/CODE005+SCA+Software+Composition+Analysis)

---
### CODE006 - The team has a Snyk (SLC scanner) built into the application builds and the results are tracked by the team following the rules of the framework.
* it's mandatory rule for application with Criticality Level 3 and 4
* at least one scan before each release
* proof expected in comments : "Snyk Dashboard link"

\
_Snyk is only available for Application with Criticality Level 3 and 4, use NOT_APPLICABLE for other cases_
**Level:** Level 2 | **Pillar:** SECURITY | **Topic:** Code/Build

**CODE006 SLC Software Licence Compliance**

[Snyk Documentation](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/205097834/Snyk+SAST+SCA)

[Wiki - CODE006 SLC Software Licence Compliance](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197463273/CODE006+SLC+Software+Licence+Compliance)

---
### CODE007 - The team has a Snyk (secure code scanner) directly integrated in the IDE and has defined a specific scope of rules for their project.

\
_Snyk is only available for Application with Criticality Level 3 and 4, use NOT_APPLICABLE for other cases_
**Level:** Level 5 | **Pillar:** SECURITY | **Topic:** Code/Build

**CODE007 Inline IDE Secure Code Analysis**

! Snyk through the IDE is accessible for everyone in DKT (even without SC) !

[Snyk Documentation](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/215222036/Snyk+as+Plugin+in+IDE+VS+Code)

[Wiki - CODE007 Inline IDE Secure Code Analysis](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460393/CODE007+Inline+IDE+Secure+Code+Analysis)

---
### CODE003 - A security champion performs a regular (at least annually) code review of all the application's code.
* proof expected in comments: name of security champion / links from security review document
**Level:** Level 4 | **Pillar:** SECURITY | **Topic:** Code/Build

**CODE003 Manual Secure Code Review**

[Wiki - CODE003 Manual Secure Code Review](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197463270/CODE003+Manual+Secure+Code+Review)

---
### CODE004 - The team has a built-in Snyk (SAST scanner) in all builds and PR of the app. The scanner blocks builds and PR if the result shows vulnerabilities. Regular monitoring is done on the non-blocking results.

\
_Snyk is only available for Application with Criticality Level 3 and 4, use NOT_APPLICABLE for other cases_
**Level:** Level 3 | **Pillar:** SECURITY | **Topic:** Code/Build

**CODE004 Static Application Security Testing**

[Snyk Documentation](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/205097834/Snyk+SAST+SCA)

[Wiki - CODE004 Static Application Security Testing](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197463261/CODE004+SAST+Static+Application+Security+Testing)

---
### CODE005 - The team has a built-in Snyk (SCA scanner) in all builds and PR of the app. The scanner blocks builds and PR if the result shows vulnerabilities. Regular monitoring is done on the non-blocking results.

\
_Snyk is only available for Application with Criticality Level 3 and 4, use NOT_APPLICABLE for other cases_
**Level:** Level 3 | **Pillar:** SECURITY | **Topic:** Code/Build

**CODE005 SCA Software Composition Analysis**

[Snyk Documentation](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/205097834/Snyk+SAST+SCA)

[Wiki - CODE005 SCA Software Composition Analysis](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460737/CODE005+SCA+Software+Composition+Analysis)

---
### CODE006 - The team has a Snyk (SLC scanner) built into the application builds and PRs. Depending on the results, this blocks the builds and PRs. Regular follow-up is done on non-blocking results.

\
_Snyk is only available for Application with Criticality Level 3 and 4, use NOT_APPLICABLE for other cases_
**Level:** Level 3 | **Pillar:** SECURITY | **Topic:** Code/Build

**CODE006 SLC Software Licence Compliance**

[Snyk Documentation](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/205097834/Snyk+SAST+SCA)

[Wiki - CODE006 SLC Software Licence Compliance](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197463273/CODE006+SLC+Software+Licence+Compliance)

---
### CODE007 - The team has a Snyk (secure code scanner) directly integrated into the IDE and blocks the push if the code does not meet the specific rules for their project.

\
_Snyk is only available for Application with Criticality Level 3 and 4, use NOT_APPLICABLE for other cases_
**Level:** Level 5 | **Pillar:** SECURITY | **Topic:** Code/Build

**CODE007 Inline IDE Secure Code Analysis**

! Snyk through the IDE is accessible for everyone in DKT (even without SC) !

[Snyk Documentation](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/215222036/Snyk+as+Plugin+in+IDE+VS+Code)

[Wiki - CODE007 Inline IDE Secure Code Analysis](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460393/CODE007+Inline+IDE+Secure+Code+Analysis)

---
### DES002 - The project context has been filled with your Security Champion and stored in the security champion drive.
* it's mandatory rule
* proof expected in comments : document link
**Level:** Level 2 | **Pillar:** SECURITY | **Topic:** Design

**DES002 Threat Modelling**

[project context explanation and template](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/283509593/Mapping+contextualization)

[Wiki - DES002 Threat Modelling](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460387/DES002+Threat+Modelling)

---
### DES003 - All applications for employees, of which at least one resource must not be accessible to everyone, I set up FedID.
* proof expected in comments : EntityID or client_ID
**Level:** Level 1 | **Pillar:** SECURITY | **Topic:** Design

**DES003 Access Right Management**

[Wiki - DES003 Access Right Management](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460389/DES003+Access+Right+Management)

---
### DES002 - A threat modeling activity has been performed on the application by a security analyst (AppSec or SO).
* proof expected in comments : document link
**Level:** Level 4 | **Pillar:** SECURITY | **Topic:** Design

**DES002 Threat Modelling**

[Wiki - DES002 Threat Modelling](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460387/DES002+Threat+Modelling)

---
### DES003 - All applications for DKT customers, of which at least one resource must not be accessible to everyone, I set up Login.
* proof expected in comments : framing note link
**Level:** Level 1 | **Pillar:** SECURITY | **Topic:** Design

**DES003 Access Right Management**

[Wiki - DES003 Access Right Management](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460389/DES003+Access+Right+Management)

---
### I use alcatrace if i have to handle personnal data
**Level:** Level 2 | **Pillar:** SECURITY | **Topic:** Operate/Monitor

### Why ?
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

---
### Wiz is setup in my CI
**Level:** Level 1 | **Pillar:** SECURITY | **Topic:** Operate/Monitor

### Why ?
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

---
### Wiz issues are reviewed and prioritized in the project backlog
**Level:** Level 3 | **Pillar:** SECURITY | **Topic:** Operate/Monitor

### Why ?
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

---
### CI fail if a Wiz issue is detected
**Level:** Level 5 | **Pillar:** SECURITY | **Topic:** Operate/Monitor

### Why ?
Having the Wiz scan's reports added as comments on your PR's is nice, but let's face it, you could forget to have a check on it.
And it would sad to miss an opportunity to make things better from a security point of view, especially once you have relatively clean artifacts produced.

### What ?
The point of this quality criteria is to turn the PR's Wiz comment into real quality gates.
Have your team choosing a criticy level you don't allow to be shipped without at least have been warned as a quality gate failure
Modify your CI in order to have this new quality gate triggered accordingly
Notice : the goal is not to prevent you from delivering a hot fix whenever necessary, but to help you making choises with the right information level. If it's more critical for the business to pass an hot fix before remediating to a vulnerability, use your administrator rights and manage the vulnerability in a second step, or at least don't forget to keep track of this task in your backlog

### How ?
Your team should be able to demonstrate that each of its CI producing artifacts subject to Wiz scan had a related quality gate configured

---
### ORG001 - I filled my security assement in SSOT with my SO ?
* it's mandatory rule
* proof expected in comments : "cyber critical level", "IDP UUID"
**Level:** Level 1 | **Pillar:** SECURITY | **Topic:** Organisation

**ORG001 Risk Assessment**

[List of SO](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197459980/Organisation+and+contact)

/!\ : SSOT is only accessible to SO in write mode

---
### ORG003 - My application is known and followed by my SO ?
* it's mandatory rule
* proof expected in comments : "names" of SO in comment
**Level:** Level 1 | **Pillar:** SECURITY | **Topic:** Organisation

**ORG003 Security Champion**

[List of SO](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197459980/Organisation+and+contact)

[Wiki - ORG003 Security Champion](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460601/ORG003+SecurityChampion)

---
### ORG001 - I identified a Security Champion for my application in SSOT?
* it's mandatory rule

**Level:** Level 2 | **Pillar:** SECURITY | **Topic:** Organisation

**ORG001 Risk Assessment**

[List of SO](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197459980/Organisation+and+contact)

/!\ : the applimap file is only accessible to SO

[Wiki - ORG001 Risk Assessment](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197463253/ORG001+RiskAssessment)

---
### ORG003 - My application is monitored by a Security Champion and one of the team members has security responsibility for the application?
* it's mandatory rule
* proof expected in comments : "names", "names" of Security Champion and team member
**Level:** Level 4 | **Pillar:** SECURITY | **Topic:** Organisation

**ORG003 Security Champion**

[List of SC](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460154/Security+Champion+List)

[Wiki - ORG003 Security Champion](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460601/ORG003+SecurityChampion)

---
### ORG003 - My application is monitored by a Security Champion, one of the team members has security responsibility for the application and the application is under DevSecOps?
* it's mandatory rule
* proof expected in comments : "DevSecOps dashboard link
**Level:** Level 2 | **Pillar:** SECURITY | **Topic:** Organisation

**ORG003 Security Champion**

To put an application under DevSecOps control, you have to go through an Onboarding process accompanied by a Security Champion.

[Wiki - ORG003 Security Champion](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460601/ORG003+SecurityChampion)

---
### REQ003 -Security user stories and abuse stories template are defined and used.
* it's mandatory rule
* proof expected in comments "Jira Dashboard Link"
**Level:** Level 4 | **Pillar:** SECURITY | **Topic:** Requirement

**REQ003 Security User Stories and Acceptance Criterias**

[How to write an abuse story](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460383/REQ003+Security+User+Stories+and+Acceptance+Criterias)

[Wiki - REQ003 Security User Stories and Acceptance Criterias](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460383/REQ003+Security+User+Stories+and+Acceptance+Criterias)

---
### REQ003 - Security use and misuse cases are defined as feature's acceptance criteria.
**Level:** Level 4 | **Pillar:** SECURITY | **Topic:** Requirement

**REQ003 Security User Stories and Acceptance Criterias**

[Wiki - REQ003 Security User Stories and Acceptance Criterias](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460383/REQ003+Security+User+Stories+and+Acceptance+Criterias)

---
### I followed the SaaS Assessment Cybersecurity
**Level:** Level 1 | **Pillar:** SECURITY | **Topic:** Requirement

**SAAS001 SaaS Assessment**

[SaaS Assessment Cybersecurity Sourcing](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460520/SaaS+Assessment+Cybersecurity+Sourcing)

---
### TEST001 - The staging environment is different from production environment and doesn't contain production data with the exception of data used for the proper functioning of the application (config, parameters, administration) and data that is already public (store opening hours, list of items, countries, postal codes, etc.)
**Level:** Level 1 | **Pillar:** SECURITY | **Topic:** Test

**TEST001 Security Test Management**

[Wiki - TEST001 Security Test Management](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460397/TEST001+Security+Test+Management)

---
### TEST004 - Pentests are performed at the frequency defined by the Application Vulnerability Management Framework. (evidence: links to the pentest request)
Vulnerabilities resulting from the pentest are tracked in a tool.
* proof expected in comments : Links to Application Vulnerability Centralization Tool
**Level:** Level 1 | **Pillar:** SECURITY | **Topic:** Test

**TEST004 Penetration Testing**

[Wiki - TEST004 Penetration Testing](https://docs.google.com/document/d/19TOgPcbvQHC7fmfpJhS1UxHG4CHAaDmBmgfNM5GL38A/edit?tab=t.0)

---
### TEST001 - The staging environment is identical to the production environment on the scope of the entire application (infrastructure and code) and test data can be shared.
**Level:** Level 2 | **Pillar:** SECURITY | **Topic:** Test

**TEST001 Security Test Management**

[Wiki - TEST001 Security Test Management](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460397/TEST001+Security+Test+Management)

---
### TEST001 - The staging environment is identical to the production environment on the scope of the entire application and all applications on which it depends (infrastructure and code) and test data can be created on-demand.
**Level:** Level 3 | **Pillar:** SECURITY | **Topic:** Test

**TEST001 Security Test Management**

[Wiki - TEST001 Security Test Management](https://decathlon.atlassian.net/wiki/spaces/SEC/pages/197460397/TEST001+Security+Test+Management)

---
### Your data model is documented
**Level:** Level 1 | **Pillar:** DATA | **Topic:** Data documentation

Your functional product's data model (business objects, business value) mainly described through the raw code source or scattered files, limiting documentation to describing physical tables after they are built

- [Business object definition](https://decathlon-group.collibra.com/asset/00923336-c93c-4c92-bd2f-280cb7cb2115) in collibra.
- [Business objects and attributes definition](https://docs.google.com/presentation/d/1gioqQf0w0LyIGx7Non8K7yx59fVXC-FyfnH1KnYkY1I/edit?usp=sharing)
- [Example of a business object documentation](https://decathlon-group.collibra.com/asset/1739c89e-11f8-4455-b847-f715b5af94e7)

---
### Your data model is centralized in the Data Catalog
**Level:** Level 3 | **Pillar:** DATA | **Topic:** Data documentation

Business objects and definitions are referenced in the official Data Catalog with help from Data Governance to align with company standards.
It is required in order to the technical stakeholders to understand data.

- [Data modeling detailed process](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-knowledge/functional-data-knowledge) (to document app, data objects and datasets)

---
### You manage schemas as code
**Level:** Level 3 | **Pillar:** DATA | **Topic:** Data documentation

Schema management is handled using 'Schema-as-Code' and versioned in Git repositories.

- Illustration with the [Data Contract approach](https://decathlon.atlassian.net/wiki/spaces/DATA/pages/185336971/Data+contract)

---
### You systematically update documentation upon release
**Level:** Level 4 | **Pillar:** DATA | **Topic:** Data documentation

You ensure the Data Catalog accurately reflects the functional definitions of all production data. Updates are performed systematically with every change or release, often in collaboration with the Data Steward.

- To [reference](https://decathlon.atlassian.net/wiki/spaces/DATA/pages/236422446/How+to+validate+Data+has+an+identified+Producer) the app in Collibra
- To [find the data manager](https://sites.google.com/decathlon.com/data-governance/roles-responsibilities/data-manager) related to my data

---
### Has critical data been identified and documented with the Data Manager in the Data Catalog (Collibra)?
**Level:** Level 5 | **Pillar:** DATA | **Topic:** Data documentation

Data criticity is being identified in Collibra (2024-2025)
- [Definition of critical data](https://docs.google.com/presentation/d/11qh5SIVK071a2QZUsdkCBHXHFjtz8WJv/edit#slide=id.g2cedf5c4640_1_0)

---
### You follow a "Schema-First" approach with versioning strategy contract-compliant
**Level:** Level 5 | **Pillar:** DATA | **Topic:** Data documentation

Functional modeling and documentation are mandatory steps performed before any new data is exposed.
A robust schema versioning strategy is in place to ensure evolution without breaking downstream data contracts.

- Illustration with the [Data Contract approach](https://decathlon.atlassian.net/wiki/spaces/DATA/pages/185336971/Data+contract)

---
### You are aware of Data Governance topics
**Level:** Level 1 | **Pillar:** DATA | **Topic:** Data governance

Data governance [discovery kit](https://docs.google.com/presentation/d/1eJSsPjyTFlZ7V8-SuFQh6esvWFpi9dLuFUMJ19qddzA/edit#slide=id.g2a6cbe5e530_0_879)

As owner of an application/digital product, you might be a data producer.
Find the data producer training in the [Academy](https://classroom.decathlon.com/explore/presential/8794bd66-7170-4edb-8160-9fc966003dd5)


---
### Is there a disconnect where Data Governance priorities are invisible in your current backlog or technical planning ?
**Level:** Level 1 | **Pillar:** DATA | **Topic:** Data governance

TBD

---
### You encountered Data Governance topics
**Level:** Level 3 | **Pillar:** DATA | **Topic:** Data governance

Data that is not provided by its reference source creates duplication, and therefore generates confusion and unwanted stickiness in the IS.

If the data producer deviates from this principle, he must inform the data consumers in the documentation that this provision is only temporary.

- [How to validate Data is directly provided by the referent source](https://decathlon.atlassian.net/wiki/spaces/DATA/pages/236422466/How+to+validate+Data+is+directly+provided+by+the+referent+source)



---
### Do Data Governance roadmap requests often come as an afterthought, forcing you to adjust your sprint or roadmap reactively?
**Level:** Level 3 | **Pillar:** DATA | **Topic:** Data governance

Data criticity is being identified in Collibra (2024-2025)
- [Definition of critical data](https://docs.google.com/presentation/d/11qh5SIVK071a2QZUsdkCBHXHFjtz8WJv/edit#slide=id.g2cedf5c4640_1_0)

---
### Did you receive specific Data Governance training & acculturation sesisons as part of your official onboarding path ?
**Level:** Level 4 | **Pillar:** DATA | **Topic:** Data governance

It is crucial to understand the usages of your data consumers in order to:
- Change data to deliver value for them (if needed).
- Not break downstream usages if you change data.

It can includes qualitative information (lineage, need, limits for consumers, tentative improvement) and quantitative information (number of users, number of flows connected to the data produced...).

---
### Are Data Governance requests identified and prioritized alongside your technical roadmap during standard planning rituals (e.g., Quarterly Planning, Sprint planning)?
**Level:** Level 4 | **Pillar:** DATA | **Topic:** Data governance

Data criticity is being identified in Collibra (2024-2025)
- [Definition of critical data](https://docs.google.com/presentation/d/11qh5SIVK071a2QZUsdkCBHXHFjtz8WJv/edit#slide=id.g2cedf5c4640_1_0)
- To work on critical data definition, contact your data manager

Example of specific actions:
- Quality Measure
- Auditability

---
### Is Data Governance embedded in your continuous learning rituals, keeping you proactively updated on new standards?
**Level:** Level 5 | **Pillar:** DATA | **Topic:** Data governance

You have on the scope of your data, at least:
- 1 data owner/knower/manager, 1 data steward
- 1 recurring meeting with them

Find the [data manager related to your data](https://sites.google.com/decathlon.com/data-governance/roles-responsibilities/data-manager) and the data owner (if he exists).

---
### Are Data Governance requests natively embedded in your technical design and features, making the roadmap completely aligned?
**Level:** Level 5 | **Pillar:** DATA | **Topic:** Data governance

TBD

---
### Are you not unaware of which data within your scope classifies as Personal Data?
**Level:** Level 1 | **Pillar:** DATA | **Topic:** Data privacy

[Overall introduction](https://sites.google.com/a/decathlon.com/legal/data-protection/what-is-the-gdpr) documentation. You can as well read these ones:
- [Data Protection](https://sites.google.com/a/decathlon.com/legal/data-protection)
- [Data protection Training](https://sites.google.com/a/decathlon.com/legal/data-protection/training)

---
### If my application collects personal data, have the user consent always been retrieved?
Has the process been validated by the treatment officer? The Data Protection Officer?
**Level:** Level 1 | **Pillar:** DATA | **Topic:** Data privacy

Here are the [contact names](https://www.google.com/maps/d/u/0/viewer?ll=15.35840076934714%2C0&z=2&mid=1PLccJ8GbWirmxbB6XEpA_voh1hIiTxBG) (DPO/Legal) for each country.

---
### Did you make the effort to document or tag this data as ‘Personal’ (in your code or API), even if it required manual action or if it's in informal or partial lists (e.g., spreadsheets) ?
**Level:** Level 2 | **Pillar:** DATA | **Topic:** Data privacy

TBD

---
### Has information regarding the presence or not of personal data in your data / the class been documented by your data owner in the data catalog (Collibra)?

**Level:** Level 3 | **Pillar:** DATA | **Topic:** Data privacy

Definition of [Personal data](https://www.cnil.fr/en/personal-data-definition).

- Here is an [example](https://decathlon-group.collibra.com/asset/d14c487b-d7bb-4990-bd54-37cb63d182b7) of the place and of the type of information to fill in.

---
### Have you verified that the Information regarding Personal/Confidential data been documented in the Data Documentation (Data Contract or ID Card for DFI users) ?
**Level:** Level 3 | **Pillar:** DATA | **Topic:** Data privacy

For DFI users : The [DFI process to fill in the ID card](https://sites.google.com/a/decathlon.com/legal/data-protection/data-protection-impact-assessment-dpia) requires the declaration of any personal data at step 3 (table level) and step 6 (column level) in order then the Data Factory Ingest Platform manages personal data specifically based on the security policies.

---
### If my application produces/manages personal data, has the final usage of it been documented?
**Level:** Level 3 | **Pillar:** DATA | **Topic:** Data privacy

[Data Protection Impact Assessment (DPIA)](https://sites.google.com/a/decathlon.com/legal/data-protection/data-protection-impact-assessment-dpia)

---
### If a list of clients require to remove their personal data, is your team able to do it easily? including the all history of data
**Level:** Level 4 | **Pillar:** DATA | **Topic:** Data privacy

TBD

---
### Are reliability checks (quality checks, monitoring, SLAs) applied systematically and in a standardized manner to this personal data,  based on the fully validated inventory in the Data Catalog where all Personal Data is clearly identified and tagged ?
**Level:** Level 4 | **Pillar:** DATA | **Topic:** Data privacy

Depending on the classification of the data, the level of security must be different (e.g. data encryption, storage in secured private zone, data access controls...).
For instance, the client name must be more protected than the adress of Decathlon shops.
Furthermore, security over data must be strenghtened if the data can be read by external users than for internal ones.

You must comply with the [Group personal data classification and security measures](https://decathlon.atlassian.net/wiki/spaces/DATA/pages/185431787/03a+-+Personal+Data+classification+security+measures).

---
### Does your team use a process for regular privacy impact assessments and audits to ensure compliance?
**Level:** Level 5 | **Pillar:** DATA | **Topic:** Data privacy

TBD

---
### Is securing this personal data integrated in the pipilines / he design phase of every new feature or product you build and have your practices been shared to help other teams ?
**Level:** Level 5 | **Pillar:** DATA | **Topic:** Data privacy

TBD

---
### Is your team trained to basic data quality concepts and aware of the benefits?
**Level:** Level 1 | **Pillar:** DATA | **Topic:** Data quality

Here is the most relevant [training](https://classroom.decathlon.com/explore/presential/8794bd66-7170-4edb-8160-9fc966003dd5), focusing on data integrity.

---
### Are there reliability controls on the product/app UI at data entry/data creation?
**Level:** Level 2 | **Pillar:** DATA | **Topic:** Data quality

All data created must comply with the business requirements described before.

Illustration: in the client address, the country entry is validated based on a predefined list

---
### Have quality rules and thresholds been defined and validated with data governance stakeholders?
**Level:** Level 3 | **Pillar:** DATA | **Topic:** Data quality

Data governance office documentation regarding the [data quality process and conventions](https://docs.google.com/presentation/d/1BDk9VysXmK6Y9vaNP-RoERomfyu-hasAwnEuVCkkxIU/edit#slide=id.g2f02d7c04e7_0_53).

To do in collaboration with at least the Data Manager, if existing in my perimeter, data owner/data steward and Data Quality Manager, following the processes and conventions recommended by the Data Governance Office.
It includes SLAs.

---
### Has data quality been monitored using automated scripts and the results available centrally?
**Level:** Level 3 | **Pillar:** DATA | **Topic:** Data quality

**All quality test results must be made available to users** (principle of transparency).

In the Data Unit, for instance, data quality results used to be stored in AWS S3 datalake in the bucket owned by the Data Observability team.
- Example of data quality dimensions : integrity, consistency, ...
- Example of automated scripts methods: python, SaaS tool for data transformation or a dedicated quality tool.

---
### Does your team apply data remediation process, data escalation process, post mortem, and any additional process to make the data quality experience smoother?
**Level:** Level 4 | **Pillar:** DATA | **Topic:** Data quality

- [Macro process of data quality](https://docs.google.com/presentation/d/1eFV-8POHRA4jthPHIj5uQZYda5OaO_bcH3bK3CbcemQ/edit#slide=id.g2c7490cac02_0_1929)
- [How to](https://docs.google.com/document/d/1p2dY5Zu1lNwvbp5klxGjNBBGLV5GcNai9Np0768BlUc/edit?tab=t.0#heading=h.208ezn6rk5ea) Data Quality macro process

---
### Is alerting systematic when there is a lack of data quality?
**Level:** Level 4 | **Pillar:** DATA | **Topic:** Data quality


- Alerting to the data sources owners, to the data consumer.
- The data producer uses a tool to alert data consumers

[Macro process of data quality](https://docs.google.com/presentation/d/1eFV-8POHRA4jthPHIj5uQZYda5OaO_bcH3bK3CbcemQ/edit#slide=id.g2c7490cac02_0_1929)

---
### Do you have a formal commitment regarding data quality with your consumers, with preventive actions to limit the impact of bad data quality?

**Level:** Level 5 | **Pillar:** DATA | **Topic:** Data quality

To limit the downstream business impact, a preventive approach is in place to limit the lack of data quality even before it is exposed (e.g. data contractualization approach).

- Illustration with the [Data Contract approach](https://decathlon.atlassian.net/wiki/spaces/DATA/pages/185336971/Data+contract) and [policies](https://docs.google.com/document/d/1rocg5d9ZXonW-C5CeKKCsUX7SdNVx5nYUQ624VJ4k1g/edit?tab=t.0)


---
### DOCUMENTATION
Your quality rules are visible to non-developers
**Level:** Level 2 | **Pillar:** DATA | **Topic:** Data quality

You ensure that management rules (e.g., formats, mandatory fields) are documented outside of the application's source code, allowing business stakeholders to read and understand them.

[Data quality reference documents](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality)

---
### CONTROLS
You apply checks base on your rules
**Level:** Level 2 | **Pillar:** DATA | **Topic:** Data quality

You currently discover data quality issues reactively, often through downstream user complaints, and perform manual fixes on production pipelines.

[Data quality reference documents](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality)

---
### ALERTING
You provide an alert whenever a quality issue arises
**Level:** Level 2 | **Pillar:** DATA | **Topic:** Data quality

You lack an active alerting system. Data quality drops are usually discovered only when downstream users report broken reports or system errors.

[Data quality reference documents](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality)

---
### REMEDIATION
You perform fixes on your quality issue
**Level:** Level 2 | **Pillar:** DATA | **Topic:** Data quality

Data quality issues are fixed on the fly. There is no formal logging of the root cause or the solution in a tracking tool, making it difficult to learn from past errors.

[Remediation process](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality/remediation-process)

---
### DOCUMENTATION
You formalized your rules in a shared document
**Level:** Level 3 | **Pillar:** DATA | **Topic:** Data quality

You list and describe tested quality rules in a technical document accessible to the team (e.g., README, Confluence, or Sheets), even if the document is currently maintained locally.

[Data quality reference documents](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality)

---
### CONTROLS
You implemented automated controls
**Level:** Level 3 | **Pillar:** DATA | **Topic:** Data quality

You use your own technical stack (e.g., SQL scripts, Python, dbt tests) to automate checks, though they may run sporadically (only during releases or after incidents).

[Data quality reference documents](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality)

---
### ALERTING
You proactively alert when a quality issue is detected
**Level:** Level 3 | **Pillar:** DATA | **Topic:** Data quality

You must remember to manually check dashboards or run scripts to detect issues. There is no automated push notification to tell you when something is wrong.

[Data quality reference documents](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality)

---
### REMEDIATION
You document the post-fix summary
**Level:** Level 3 | **Pillar:** DATA | **Topic:** Data quality

You document the fix only after the incident is resolved. While the cause is briefly noted, there is no detailed tracking or visibility during the investigation phase.

[Remediation process](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality/remediation-process)

---
### DOCUMENTATION
The Data Catalog is your "Source of Truth" for rules
**Level:** Level 4 | **Pillar:** DATA | **Topic:** Data quality

Your quality rules are referenced in the official company tool (Data Catalog, Collibra, or Data Contracts). This serves as the single validated source of truth prior to implementation.

[Data quality reference documents](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality)

---
### CONTROLS
Your controls are fully automated and aligned with rules
**Level:** Level 4 | **Pillar:** DATA | **Topic:** Data quality

Data quality checks are fully automated (e.g., daily batches or real-time) and strictly reflect the formally documented rules validated in the Data Catalog.

[Data quality reference documents](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality)

---
### ALERTING
You send automated notifications when quality issue arises
**Level:** Level 4 | **Pillar:** DATA | **Topic:** Data quality

Alerts are automatically sent to the relevant owners as soon as a critical threshold is breached, allowing for faster intervention before users notice.

[Data quality reference documents](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality)

---
### REMEDIATION
The remediation process is tracked in real-time
**Level:** Level 4 | **Pillar:** DATA | **Topic:** Data quality

The entire incident lifecycle is visible and documented. You provide clear status updates from detection to deployment, ensuring stakeholders are informed throughout the resolution.

[Remediation process](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality/remediation-process)

---
### DOCUMENTATION
You link quality rules to business impact and thresholds
**Level:** Level 5 | **Pillar:** DATA | **Topic:** Data quality

Your documentation includes clear business context and specific quality thresholds. This allows for data-driven prioritization of remediation efforts based on business risk.

[Data quality reference documents](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality)

---
### CONTROLS
Your controls are integrated into Data Contracts
**Level:** Level 5 | **Pillar:** DATA | **Topic:** Data quality

Technical execution is linked to documentation to prevent drift. You automatically detect anomalies like volume spikes, schema changes, or freshness delays.

[Data quality reference documents](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality)

---
### ALERTING
Alerting is integrated into your incident workflow
**Level:** Level 5 | **Pillar:** DATA | **Topic:** Data quality

Alerts are fully integrated into technical tools (e.g., auto-creating tickets). They include root-cause hints and handle alert fatigue through deduplication and smart routing.

[Data quality reference documents](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality)

---
### REMEDIATION
You perform systematic RCAs to prevent recurrence
**Level:** Level 5 | **Pillar:** DATA | **Topic:** Data quality

Every incident triggers a Root Cause Analysis (RCA) or Post-Mortem. These insights directly lead to updated monitoring rules or architectural changes to ensure the same issue never happens twice.

[Remediation process](https://sites.google.com/decathlon.com/data-governance/reference-documents/data-quality/remediation-process)

---
### Are you aware of existing rules and principles for handling reference and master Data?
**Level:** Level 1 | **Pillar:** DATA | **Topic:** Reference data

[Reference Data Policy](https://docs.google.com/document/d/1XF_Nx-ly1gzL9JbQwryOrH1oXT7ELC4PTwLjQldsucw/edit?usp=sharing)

---
### If your project/product contains/consume/produce reference data. Did You identified related Business Objects?
**Level:** Level 2 | **Pillar:** DATA | **Topic:** Reference data

[Reference Data Policy](https://docs.google.com/document/d/1XF_Nx-ly1gzL9JbQwryOrH1oXT7ELC4PTwLjQldsucw/edit?usp=sharing)

---
### If your project/product contains/consume/produce reference data. Did You identified source of truth applications of those reference data?
**Level:** Level 3 | **Pillar:** DATA | **Topic:** Reference data

[Reference Data Policy](https://docs.google.com/document/d/1XF_Nx-ly1gzL9JbQwryOrH1oXT7ELC4PTwLjQldsucw/edit?usp=sharing)

---
### Do you manage/consume/share reference data of your project according to Reference Data Policy?
**Level:** Level 5 | **Pillar:** DATA | **Topic:** Reference data

Examples of Reference Data Policiyrequirements: SLA/Quality, Quality requirements, Repository pre-requisities


---
### You identified the critical data assets within your scope
**Level:** Level 1 | **Pillar:** DATA | **Topic:** Critical Data

You recognize which specific data assets have a high business impact for the company, looking beyond purely technical needs or internal project use.

- [Critical Data asssement process & assessment matrix](https://sites.google.com/decathlon.com/data-governance/reference-documents/critical-data-management)

---
### You started tagging or documenting your critical data
**Level:** Level 3 | **Pillar:** DATA | **Topic:** Critical Data

You have identified critical assets in your code, APIs, or documentation. This may still involve manual effort or reside in informal/partial lists (e.g., spreadsheets).

- [Critical Data policy & guidelines](https://sites.google.com/decathlon.com/data-governance/reference-documents/critical-data-management)

---
### Your critical assets are systematically monitored and cataloged
**Level:** Level 4 | **Pillar:** DATA | **Topic:** Critical Data

Reliability checks (Quality, Monitoring, SLAs) are applied in a standardized way. Your assets are fully identified and tagged in the official Data Catalog or your Data Contract.

- [Critical Data monitoring & Critical Data list](https://sites.google.com/decathlon.com/data-governance/reference-documents/critical-data-management)

---
### "Critical Data by Design" is part of your development lifecycle
**Level:** Level 5 | **Pillar:** DATA | **Topic:** Critical Data

Data criticality is integrated into the design phase of every new feature. You proactively secure these pipelines and share your expertise to help other teams improve.

- [Critical Data monitoring & Critical Data list](https://sites.google.com/decathlon.com/data-governance/reference-documents/critical-data-management)

---
### You are aware of the ingestion standards and the Data Steward’s role
**Level:** Level 1 | **Pillar:** DATA | **Topic:** Datalake Integration

You understand that data accessibility requires specific technical rules.
Resources:
- [DFI](https://dataplatform.dktapp.cloud/doc/products/ingestion/dfi/what_is_dfi.html) for autonomous service
- [Custom Track](https://decathlon.atlassian.net/wiki/spaces/DATA/pages/1257406907/CustomTrack+user+step+by+step+guide) for other cases

---
### You deploy ingestion flows following technical guidelines
**Level:** Level 3 | **Pillar:** DATA | **Topic:** Datalake Integration

You configure and deploy flows (naming, format, metadata) according to guidelines, even if you still need support from the Data Steward.
Resources:
- Use [DFI](https://dataplatform.dktapp.cloud/doc/products/ingestion/dfi/what_is_dfi.html) for self-service.
- Follow the [Custom Track](https://decathlon.atlassian.net/wiki/spaces/DATA/pages/1257406907/CustomTrack+user+step+by+step+guide) for specific needs.

---
### You manage and monitor your ingestion flows independently
**Level:** Level 4 | **Pillar:** DATA | **Topic:** Datalake Integration

You handle end-to-end management (failures, retries, corrections) without Data Steward intervention.
Resources:
- DFI [monitoring](https://dataplatform.dktapp.cloud/doc/products/ingestion/dfi/concepts/monitoring/monitoring.html) & [SMA-X alerting](https://dataplatform.dktapp.cloud/doc/products/ingestion/dfi/concepts/monitoring/smax_alerting.html).
- Custom monitoring & SMA-X for Custom Track.

---
### You assess the impact of data changes on downstream flows
**Level:** Level 5 | **Pillar:** DATA | **Topic:** Datalake Integration

You anticipate how product or data model changes will affect ingestion before development, ensuring that updates never break the downstream data pipeline.

---
### Your digital product is at least 80% compliant with the RGAA
**Level:** Level 4 | **Pillar:** ACCESSIBILITY | **Topic:** Accessibility

### Why ?

The RGAA is the French reference standard for improving accessibility, on which the French law is based. It is a pragmatic approach based on the European directive (EN 301 549) and the internartional standard (WCAG).
The RGAA proposes criteria on 13 themes, and 3 levels of requirement (A, AA and AAA). This criteria-based approach allows us to monitor and assess a platform's accessibility maturity as a percentage of compliance.
This score is obtained following an accessibility audit that could be carried out by yourself or by our accessibility partner.

Being 100% compliant with the RGAA is equivalent to being 100% compliant with WCAG 2.1 (A + AA) and the European standard EN 301 549 (except for PDFs).

### What ?

Achieving at least 80% compliance with the RGAA.

### How ?

You can proceed to self-assessment following the RGAA guidelines. See our Wiki's entry "[How to conduct an accessibility self assessment](https://decathlon.atlassian.net/wiki/spaces/TO/pages/569017392/How+to+conduct+an+accessibility+self+assessment)"

(We are currently processing a call for tenders.The process to request an external audit will be updated soon)

---
### Integrate the Accessibility Checklist evaluation in your process and feel “good” about it
**Level:** Level 4 | **Pillar:** ACCESSIBILITY | **Topic:** Accessibility

### Why?

To transition from "avoiding errors" to "ensuring compliance." Reaching this level guarantees that your product is robust enough for a formal audit and provides a reliable, inclusive experience for all users.

### What?

The "Good" Maturity Status: a state where accessibility is integrated into your "Definition of Done." It implies that foundations are solid, complex components (modals, tabs) are accessible, and you are ready for a professional compliance validation.

###  How?

Run a final assessment using the [Consult and apply the Accessibility Checklist](https://decathlon.atlassian.net/wiki/spaces/TO/pages/1968046127/Accessibility+Easy+Checks) or the Maturity Auditor agent. To succeed at this level, your team must self-evaluate as "Good": meaning all high-priority issues are resolved, and you are ready to request an official compliance audit (WCAG/RGAA).


---
### Get your product audited
**Level:** Level 4 | **Pillar:** ACCESSIBILITY | **Topic:** Accessibility

### Why?

To achieve official validation and legally certify your product’s accessibility. A formal audit moves you from "self-declared quality" to "certified compliance," ensuring a high-standard experience and minimizing legal risks.

### What?

A **Formal Accessibility Audit**: an exhaustive verification of WCAG/RGAA/RAAM criteria performed on a representative sample of your pages by certified experts.

### How?

Audits are conducted either internally by your team (see [conducting an accessibility self-assessment](https://decathlon.atlassian.net/wiki/spaces/TO/pages/path-to-self-assessment)), by the Digital Accessibility team or with our partner **Warren Walter** (see [how to get audited](https://decathlon.atlassian.net/wiki/spaces/TO/pages/path-to-get-audited)).

Contact us to kick off the process: [digitalaccessibility@decathlon.com](mailto:digitalaccessibility@decathlon.com)

---
### You have a campaign of specific scenarios & user journeys for users with disabilities in your functional and/or integration and/or E2E testings
**Level:** Level 4 | **Pillar:** ACCESSIBILITY | **Topic:** Accessibility

### Why ?

Testing the proper functioning of a platform, whatever its user, is essential to guarantee the quality of an application and ensure that the platform meets the identified needs. To guarantee platform accessibility, each test campaign must include several scenarios involving disabled users.

### What ?

Each test campaign must include scenarios involving users with disabilities, such as keyboard or voice-only navigation, zooming the interface to 200%, motion sickness, and so on.

### How ?

Extend test campaigns to more specific accessibility scenarios

---
### Your digital product or service is 100% compliant with the RGAA
**Level:** Level 4 | **Pillar:** ACCESSIBILITY | **Topic:** Accessibility

### Why ?

The RGAA is the French reference standard for improving accessibility, on which the French law is based. It is a pragmatic approach based on the European directive (EN 301 549) and the internartional standard (WCAG).
The RGAA proposes criteria on 13 themes, and 3 levels of requirement (A, AA and AAA). This criteria-based approach allows us to monitor and assess a platform's accessibility maturity as a percentage of compliance.
This score is obtained following an accessibility audit that could be carried out by yourself or by our accessibility partner.

Being 100% compliant with the RGAA is equivalent to being 100% compliant with WCAG 2.1 (A + AA) and the European standard EN 301 549 (except for PDFs).

### What ?

Audit remediation is done: achieving 100% compliance with the RGAA to reach "totally compliant" level.

### How ?

You can proceed to self-assessment following the RGAA guidelines. See our Wiki's entry "[How to conduct an accessibility self assessment](https://decathlon.atlassian.net/wiki/spaces/TO/pages/569017392/How+to+conduct+an+accessibility+self+assessment)"

(We are currently processing a call for tenders.The process to request an external audit will be updated soon)

---
### A formal error handling policy is documented. We have a defined (even if manual) process to detect, inspect, and manage failed messages.
**Level:** Level 1 | **Pillar:** STREAMING | **Topic:** Event Streams

**For example:** when do I retry, or send to DLT and skip? We can also have different policies based on what we do with the topic

---
### Our defined error handling policy is consistently applied & implemented on every topics and queues.
**Level:** Level 2 | **Pillar:** STREAMING | **Topic:** Event Streams

**Why:** Consistency ensures that no "silent failures" occur in production. Every topic or queue, regardless of perceived importance, follows the same safety patterns to prevent data loss.

---
### Our defined error handling policy is monitored. This includes mechanisms like automated alerting for failure thresholds, and (where appropriate) automated redrive/replay capabilities
**Level:** Level 3 | **Pillar:** STREAMING | **Topic:** Event Streams

**Why:** The process is robust, efficient, and scalable, freeing up the team to solve new problems instead of managing old ones

---
### Lessons learned from the analysis of invalid messages are used proactively to improve system robustness and prevent errors upstream.
**Level:** Level 4 | **Pillar:** STREAMING | **Topic:** Event Streams

**How:** Regular post-mortems on Dead Letter Topics or Queue (DLT or DLQ) to identify schema mismatches or logic errors, feeding these back into upstream validation or contract tests.

---
### Consumers are designed to be idempotent. They can safely process the exact same message multiple times without creating duplicate records, sending multiple emails, or causing other side effects
**Level:** Level 1 | **Pillar:** STREAMING | **Topic:** Event Streams

**Why:** This handles "at-least-once" delivery. If you can't handle a simple network-hiccup duplicate, you have no business attempting a full replay.

---
### A formalized process exists to capture and re-process individual failed messages. This process is documented, validated and shared
**Level:** Level 2 | **Pillar:** STREAMING | **Topic:** Event Streams

**Why:** This proves you can recover from individual poison pills or transient errors without stopping the whole line. It's a controlled, small-scale replay.

---
### The platform supports re-processing large windows of historical events. This is achieved via mechanisms like resetting consumer offsets (e.g., in Kafka), re-publishing from a persistent event store, or querying a time-stamped data lake. This capability is documented, shared, and tested
**Level:** Level 3 | **Pillar:** STREAMING | **Topic:** Event Streams

**Why:** This is the goal. You can rebuild an entire service's state from scratch, onboard a new analytics system, or recover from a catastrophic bug that corrupted data for hours.

---
### Topics and queues are given unique, descriptive names that reflect their purpose
**Level:** Level 1 | **Pillar:** STREAMING | **Topic:** Event Streams

**Why:**  This is the bare minimum. You're not using default names (queue-1) or temporary names (john_doe_test).

---
### A formal naming convention is documented, shared, and actively socialized. New topics and queues are expected to follow it
**Level:** Level 2 | **Pillar:** STREAMING | **Topic:** Event Streams

**Why:** You've moved from individual good intentions to a shared, agreed-upon standard. This brings consistency and makes the platform discoverable

[Example of topic naming convention](https://framework.eu.member.decathlon.net/streaming/03-convention/topics/ )

---
### The naming convention is applied universally and compliance is enforced automatically (e.g., resource-creation policies, or scripts).
**Level:** Level 3 | **Pillar:** STREAMING | **Topic:** Event Streams

**Why:** This is true maturity. The "right way" is the only way. It's impossible to create a non-compliant resource, and there's likely a plan to remediate old, non-compliant ones.

---
### A data retention policy is defined and documented for our topics/queues
**Level:** Level 1 | **Pillar:** STREAMING | **Topic:** Event Streams

**WHY**: To prevent infinite data growth and ensure predictable storage consumption by automatically deleting old messages.

---
### Our retention policy is purpose-driven. We apply different lifecycle strategies based on the data's specific use case.
**Level:** Level 2 | **Pillar:** STREAMING | **Topic:** Event Streams

**Warning :** Non available for queueing
**Why:** To optimize storage efficiency by keeping only the latest state for specific keys (compaction) while saving space
**How:** Log compaction keeps only the latest message per key in each partition. Each message must have a key so messages with the same key go to the same partition.

---
### Storage strategies are implemented and optimized in alignment with the standard company decision matrix
**Level:** Level 3 | **Pillar:** STREAMING | **Topic:** Event Streams

**Why:** To balance cost and performance by moving older data to cheaper storage tiers while respecting strict business retention constraints.

Link 1 : [Kafka cluster creation decision matrix](https://decathlon.atlassian.net/wiki/spaces/TO/pages/1643381012/STRAT+Kafka+cluster+creation+decision+matrix)
Link 2 : [Kafka Tiered Storage](https://decathlon.atlassian.net/wiki/spaces/TO/pages/1667072080/GUIDE+Kafka+Tiered+Storage)

---
### To mitigate high-volume or high-latency scenarios, we employ specific configurations to handle them.
**Level:** Level 1 | **Pillar:** STREAMING | **Topic:** Event Streams

**Why:** To ensure low latency and system stability by preventing oversized payloads from degrading network performance or exceeding broker limits.

---
### Payload size is optimized based on my needs. I use Avro and compression (e.g., ZSTD, Gzip, Snappy) when relevant.
**Level:** Level 2 | **Pillar:** STREAMING | **Topic:** Event Streams

**Why:** It's a good practice to save network and broker disk space.

---
### We benchmark and tune optimization parameters (e.g., compression level vs. CPU cost, batch.size vs. linger.ms) to meet specific business SLAs.
**Level:** Level 3 | **Pillar:** STREAMING | **Topic:** Event Streams

**Why:** To find the right balance between throughput, latency, and infrastructure cost to meet specific business SLAs.

---
### Message metadata structure (headers) is compliant to CloudEvents as specified in Decathlon standards (see link in the doc)
**Level:** Level 4 | **Pillar:** STREAMING | **Topic:** Event Streams

**Why:** To enable consistent communication and interoperability across distributed services, CloudEvents standardizes event metadata in event-driven architectures.

This allows any consumer to route or filter any messages whatever the producer without parsing the body.

**See:**
[CloudEvents](https://decathlon.atlassian.net/wiki/spaces/TO/pages/1652918834/GUIDE+CloudEvents+for+Kafka)

---
### Topic sizing is intentionally determined by documented needs, considering parallelism and scaling requirements
**Level:** Level 2 | **Pillar:** STREAMING | **Topic:** Infrastructure

**Why:** To ensure optimal partition distribution, preventing bottlenecks during peak loads while maintaining the integrity of message ordering through balanced parallelism.

Link 1 : [how to choose the right number of kafka partitions and consumers](https://dev-aditya.medium.com/how-to-choose-the-right-number-of-kafka-partitions-and-consumers-4b2a4caaf8ae)
Link 2 : [kafka visualisation](https://softwaremill.com/kafka-visualisation/)

---
### Our hosting strategy (Mutualized vs. Dedicated) is a deliberate architectural decision driven by specific isolation and cost requirements.
**Level:** Level 3 | **Pillar:** STREAMING | **Topic:** Infrastructure

**Why:**  We avoid arbitrary choices. We use shared clusters to optimize costs for standard needs, and dedicated clusters only when isolation or specific performance guarantees are required.

---
### We adapt the infrastructure topology (Storage & Compute) to specific workload requirements, rather than applying a static, one-size-fits-all configuration.
**Level:** Level 4 | **Pillar:** STREAMING | **Topic:** Infrastructure

**Examples:**  Leveraging Tiered Storage for long retention, or Diskless topics for high-throughput proxying.
**Doc :**
[Kafka Tiered Storage](https://decathlon.atlassian.net/wiki/spaces/TO/pages/1667072080/GUIDE+Kafka+Tiered+Storage)


---
### Our infrastructure scaling is decoupled from data volume, allowing us to optimize costs and capacity dynamically
**Level:** Level 5 | **Pillar:** STREAMING | **Topic:** Infrastructure

**How:** By using Tiered Storage or diskless architectures, we break the link between "adding storage" and "adding brokers." This allows us to apply our cost/value strategy effectively

---
### We are able to manually inspect the health of our product by checking both application (logs, message lag) and infrastructure (CPU, memory) metrics
**Level:** Level 1 | **Pillar:** STREAMING | **Topic:** Observability

**How:** Use internal dashboards (e.g., Datadog) or UI tools (e.g., Kafbat) to view current lag and resource usage.

---
### All relevant application and infrastructure monitoring data (logs, metrics) is centralized in one or more dedicated tools
**Level:** Level 2 | **Pillar:** STREAMING | **Topic:** Observability

**Why:** Having logs and metrics in one place allows for correlation between a spike in CPU and a specific error log.

---
### Automated alerts are defined and implemented for all essential product metrics (e.g., consumer lag, error rates, resource saturation).
**Level:** Level 3 | **Pillar:** STREAMING | **Topic:** Observability

**Advice :** Lag alerts should be coupled with resource saturation metrics (CPU/Memory) to distinguish between consumer slowness and broker issues.

---
### We use distributed tracing to track message flows across services.
**Level:** Level 4 | **Pillar:** STREAMING | **Topic:** Observability

**Why:** To identify exactly which service is blocking the flow, rather than just seeing a lag spike.

---
### Monitoring is fully documented, dashboards are shared, and alerts are actively reviewed and tuned. The whole team uses this data to debug, plan capacity, and improve performance.
**Level:** Level 5 | **Pillar:** STREAMING | **Topic:** Observability

**Action:** At least one "Alerting Reviews" per quater to audit and tune alerting based on post-mortems and on-call history to eliminate noise and ensure all alerts are actionable.

---
### You measure and manage an event based SLO (freshness, correctness, coverage...)
**Level:** Level 5 | **Pillar:** STREAMING | **Topic:** Observability

### Expected
* There's an SLO that measure the reliability of the Data processing user journey you're in.

### Why
* Measuring the lag, or a completion time for a single function is good. But we want to measure the real impact for the user in the end.

### How ?
Guidelines will come during the year, from the SIG Reliability. In the meantime, explore some leads to do it the best way you can

### Example
* For an order management process, you measure the % of orders that went from starting to ending point in less than xx minutes
* For a price update process, you measure the % of price changes applied in less than xx minutes. From the change in the referential, until it's available in your last system (In Store till, or Ecommerce catalog)

---
### Access control (ACL) is in place and is managed ( at least manual )
**Level:** Level 1 | **Pillar:** STREAMING | **Topic:** Security

**Why:** To establish a baseline of security and ensure that only authorized service can access critical / sensitive resources.
**Minimum:** Every publisher and subscriber has a dedicated access with specific Read or Write rights to its required topics / queues.

---
### Access requests are based on granular, policy-based control
**Level:** Level 2 | **Pillar:** STREAMING | **Topic:** Security

**Why:** To enforce the "Principle of Least Privilege," ensuring users have the exact permissions needed for their specific ressources, reducing the attack surface.
**How:** Give access only for specific topic/queue instead of giving access to a large pattern

---
### Access control (ACL) is centralized and managed (creation, update and rotation)
**Level:** Level 3 | **Pillar:** STREAMING | **Topic:** Security

**Why:** To ensure that only authorized services remain able to access critical/sensitive resources
**How:** At least one "ACL Reviews" per quarter to audit and tune access to identify and manage "shadow access" in order to keep consistency, making it easier to audit and revoke permissions.

---
### Access management is automated and handled to ensure traceability, reproducibility and security
**Level:** Level 4 | **Pillar:** STREAMING | **Topic:** Security

**Why:** To ensure the credentials confidentiality and their rotation
**How:** Use internal secret manager (e.g., gcp secret manager, vault), and rotate credentials regularly, duration depending of the resources criticality

---
