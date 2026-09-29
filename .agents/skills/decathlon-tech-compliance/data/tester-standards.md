# BMAD Tester Knowledge Base (Decathlon Maturity Matrix)

### Tracking elements are included in non regression tests.
**Level:** Level 3 | **Pillar:** DEV | **Topic:** Analytics

### Why ?
Tracking regression are very usual in front application, we should ensure that each application change are not impacting the reliability of the produced data.
### What ?
Each tracking event should be part of the front application test suite with dedicated tests of the datalayer variables and data integrity check.
### How ?
Automated unit test before each deployment. Tests should be implemented for each component for each use cases.

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
### Synthetic tests are in place.
**Level:** Level 1 | **Pillar:** DEV | **Topic:** Observability

### Why ?
Being blind is not acceptable. Having synthetic tests will permit to have a feedback on what's runnnig into your production.

### What ?
The goal is to simulate real users that will request your app. It should permit to see runtime errors that impact your users. The requests should have a minimum checks (at least on status code) to ensure the answered page is correct for your users.

### How?
- Use the Tech Radar's Observability Monitoring tool under the ADOPTED status.

---
### Supervize the value creation and budget control of the product - I can model & test, define and follow the business model of my products or features.
**Level:** Level 1 | **Pillar:** DEV | **Topic:** Business & strategy

### How
VAT (value assessemnt template can help): https://docs.google.com/spreadsheets/d/1BwHONrJiGUm4ha1-lret9YFe71VX0WyKDohB63378Is/edit?usp=drive_link

---
### Determine the pricing of offers (know different product pricing techniques / model and test pricing hypotheses)
**Level:** Level 3 | **Pillar:** DEV | **Topic:** Business & strategy

TBD

---
### Explore solution hypothesis in a cost-effective and timely manner - I choose and prioritize the solution derisking methods adapted to each case (AB test, mock-ups, prototypes, ...)
**Level:** Level 4 | **Pillar:** DEV | **Topic:** Business & strategy

TBD

---
### Choice of machine learning model is documented and justified (e.g. model tested, metrics used, etc.).
**Level:** Level 2 | **Pillar:** DEV | **Topic:** Documentation

### What
 Document the selection process for the machine learning model, including the models tested and the metrics used for evaluation.
 ### Why
 To provide a rationale for the chosen model, demonstrating that the selection was based on systematic testing and evaluation, which helps in building trust and understanding among stakeholders.
 ### How
 Create a detailed report or section in your documentation that lists all the models considered, the evaluation metrics used (e.g., accuracy, precision, recall, F1 score), and the results of the comparisons. Justify the final choice based on these results, and include visual comparisons like performance graphs or tables.
Slides, Notebooks or documented in Sphinx technical documentation, an example here:
https://fictional-adventure-woglmk1.pages.github.io/final_report.html

---
### Document possible improvment can be done but not tested or integrated in the system yet.
**Level:** Level 5 | **Pillar:** DEV | **Topic:** Documentation

### What
 List and describe potential improvements that have been identified but not yet tested or integrated.
 ### Why
 To keep track of enhancement ideas for future development and provide a roadmap for ongoing improvement.
 ### How
 Create a backlog or roadmap document using tools like Jira, or a shared document. Detail each potential improvement, including its expected benefits and any preliminary considerations.
Confluence and/or sphinx documentation

---
### Estimate performance of your model on train, validation, test sets with appropriate metrics.
**Level:** Level 1 | **Pillar:** DEV | **Topic:** Model Management

### What
 Evaluate the performance of the machine learning model on training, validation, and test sets using relevant metrics.
 ### Why
 To assess the model's accuracy, generalization ability, and potential overfitting, ensuring it meets performance expectations.
 ### How
 Split the dataset into training, validation, and test sets. Use metrics such as accuracy, precision, recall, F1 score, ROC-AUC, and others appropriate for the problem. Document the results and compare performance across different sets.

---
### Write tests suite (with business interlocutor) and automaticly execute it at each model release.
**Level:** Level 5 | **Pillar:** DEV | **Topic:** Model Management

### What
 Develop a comprehensive test suite in collaboration with business stakeholders and ensure it runs automatically with each model release.
 ### Why
 To validate model performance and ensure it meets business requirements and quality standards.
 ### How
 Define test cases covering various aspects of the model, including accuracy, performance, and business logic. Integrate automated testing into the CI/CD pipeline using tools like pytest or unittest.
MLflow evaluate and Giskard are good candidates

---
### Tests coverage of all reposiroty (data, ml, api) is > 60%.
**Level:** Level 3 | **Pillar:** DEV | **Topic:** Code Management

### What
 Achieve and maintain test coverage of over 60% for all repositories, including data, ML, and API components.
 ### Why
 To ensure a basic level of code reliability and identify potential issues early in the development process.
 ### How
 Implement a comprehensive testing strategy using frameworks like pytest. Regularly measure test coverage using tools like coverage.py and address gaps by adding necessary test cases.
SonarCloud can help.

---
### Conduct code testing using the pytest framework to validate the functionality of the code.
**Level:** Level 3 | **Pillar:** DEV | **Topic:** Code Management

### What
 Use the pytest framework to write and run tests, validating the code's functionality.
 ### Why
 To ensure code reliability and correctness, and to identify issues early in the development cycle.
 ### How
 Write unit tests, integration tests, and functional tests using pytest. Integrate pytest into the CI/CD pipeline to automate test execution. Regularly review and update tests to cover new features and changes.

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
### Tests coverage of all reposiroty (data, ml, api) is > 90%.
**Level:** Level 5 | **Pillar:** DEV | **Topic:** Code Management

### What
 Ensure that the test coverage for all repositories, including data, machine learning (ML), and API, exceeds 90%.
 ### Why
 To maximize code reliability and minimize the risk of undetected issues.
 ### How
 Implement thorough testing strategies and utilize code coverage tools to measure and improve coverage. Regularly review and update test cases to maintain high coverage.
SonarCloud can help.

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
### Chaos testing automation is setup
**Level:** Level 5 | **Pillar:** DELIVERY | **Topic:** Chaos Engineering

### What is expected ?
You have a running chaos testing tool set up on your infra, this tool breaks things randomly

---
### Your automated build contains the mandatory step (build, test, quality, security). Build are also triggered on every pull request. Pull requests cannot be merged without a success on the build

**Level:** Level 2 | **Pillar:** DELIVERY | **Topic:** Continous Integration

### What is expected ?
CI is composed with the steps described here: https://decathlon.atlassian.net/wiki/x/-K8GCw

---
### A staging environment exists. Tests can be run in this environment, other applications may use this staging for their own test.
**Level:** Level 1 | **Pillar:** DELIVERY | **Topic:** Continuous Deployment

TBD

---
### A pen testing campain is automated after each deployment
**Level:** Level 5 | **Pillar:** DELIVERY | **Topic:** Continuous Deployment

TBD

---
### Deploy an artifact on demand (publish on Bitrise Deployment, GAR or Firebase Distribution, TestFlight, Play Store or Apple Store)
**Level:** Level 2 | **Pillar:** DELIVERY | **Topic:** Workflows

### Why ?
Publish the app on stores

### What ?
Use bitrise account connection & workflow / pipeline

### How ?
https://devcenter.bitrise.io/en/deploying.html

---
### Testing artifact is generated after every pull requests (publish on Bitrise Deployment, GAR or Firebase Distribution, TestFlight)
**Level:** Level 3 | **Pillar:** DELIVERY | **Topic:** Workflows

### Why ?
Generate an artifact of your application for every pull requests accelerate the testing phase of your contribution.

### What ?
To fulfill this requirement, your Bitrise configuration should include the assemble Bitrise Action inside the Pull Request trigger.

### How ?
Add the Bitrise Action from Bitrise website or locally in your bitrise yaml file.

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
### Automation Deployment - this should be configured as the last step in the build process. Automation deployment tool of choice to be configured in CI environment to trigger with the latest artifact.
**Level:** Level 3 | **Pillar:** DELIVERY | **Topic:** Continous Integration

### What is expected
 Automated deployment should be the final step in the build process, using a deployment tool configured in the CI environment to deploy the latest artifact automatically.

---
### CI server should be configured in such a way to take only the latest changes (just the updates), rather than the entire repository for building the artifact.
**Level:** Level 5 | **Pillar:** DELIVERY | **Topic:** Continous Integration

### What is expected
 Configure the CI server to fetch only the latest changes instead of the entire repository to optimize build times and resource usage.

---
### A dev and staging environment exists for testing ml (or/and data) artifact (code) on data samples. Tests can be run in this environment, other applications may use this staging for their own test.
**Level:** Level 2 | **Pillar:** DELIVERY | **Topic:** Continuous Deployment

### What is expected
 Separate development and staging environments must be established for testing ML and data artifacts on sample data, providing a space for thorough testing before production deployment.

---
### A dev and staging environment exists for testing data ml or api artifact. Tests can be run in this environment, other applications may use this staging for their own test.
**Level:** Level 3 | **Pillar:** DELIVERY | **Topic:** Continuous Deployment

### What is expected
 Establish separate development and staging environments for testing data, ML, and API artifacts to ensure comprehensive testing and validation before production deployment.

---
### Tests suite for ensuring quality of AI model are automatically launched on a model before to use it on production.
**Level:** Level 4 | **Pillar:** DELIVERY | **Topic:** Continuous Deployment

### What is expected
 Implement an automated test suite to validate the quality of AI models before they are deployed to production, ensuring they meet performance and reliability standards.
### How
Giskard can help

---
### Conduct A/B tests (e.g. shadown, canary deployment)
**Level:** Level 4 | **Pillar:** DELIVERY | **Topic:** Continuous Deployment

### What is expected
 Implement A/B testing strategies, including shadow and canary deployments, to compare different versions of models or applications in production and assess their performance.

---
### Canary deployment can be done for testing several models in production and compare them.
**Level:** Level 5 | **Pillar:** DELIVERY | **Topic:** Continuous Deployment

### What is expected
 Implement canary deployments to test multiple models in production concurrently, allowing for comparison and selection of the best-performing model.

---
### Quality tests, including load testing, have been integrated for APIs with embedded data or models. These tests can be initiated MANUALLY.
**Level:** Level 3 | **Pillar:** DELIVERY | **Topic:** Service Availability

### What is expected
 Integrate quality and load testing for APIs containing embedded data or models, allowing these tests to be initiated manually to ensure performance under various conditions.
### How
See example implemented with Locust on Second Hand Pricing project

---
### Quality tests, including load testing, have been implemented for APIs containing embedded data or models. These tests are initiated and AUTOMATED with each deployment.
**Level:** Level 4 | **Pillar:** DELIVERY | **Topic:** Service Availability

### What is expected
 Automate quality and load testing for APIs with embedded data or models, ensuring these tests run with each deployment to continuously validate API performance.

---
### A strategy has been defined and documented for testing production model (ex. on staging environment).
**Level:** Level 3 | **Pillar:** DELIVERY | **Topic:** Documentation

Goals : compare models before to deploy version version in production (= model testing)

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
### Implement all integration tests automation best practices
**Level:** Level 2 | **Pillar:** QUALITY | **Topic:** Integration Tests

### Why ?

Automated tests are code. Like any code, if they are poorly written, they become technical debt. The goal is to write tests that are easy to understand, update, and run.

### What ?

To create maintainable tests, focus on three key principles:

- Clarity: The purpose of each test should be immediately obvious.
- Structure: Use established design patterns and a logical project structure to make tests reusable, robust, and easy to navigate.
- Readability: Write tests in a way that both technical and non-technical team members can understand the behavior being tested.

###  How ?

Check the SIG dedicated [page](https://decathlon.atlassian.net/wiki/x/GQC2b). The team must be able to justify its choices for each acording recommendation.

---
### All critical integration tests are automated and run in CI
**Level:** Level 2 | **Pillar:** QUALITY | **Topic:** Integration Tests

### Why ?

All critical integration tests must be reliable. Running them for every code modification in the CI will avoid regressions on business features and complex resolution throughout time.

### What ?

To fulfill this requirement, all features marked as P0 and automatable must have tests implemented and are executed in Continuous Integration (not necessarily in the PR).

### How ?

The team must be able to demonstrate that there are integration tests running within CI and that all critical tests have been implemented.

---
### Strengthen integration tests by mocking external APIs
**Level:** Level 2 | **Pillar:** QUALITY | **Topic:** Integration Tests

### Why ?
To ensure reliable integration tests, external API dependencies must be removed. Fluctuations in external API availability (server outages, deployments) lead to unpredictable test outcomes.

### What ?
Implement mocking for all external API calls within integration tests.

### How ?
The team must be able to share the mock (or stub) implementation in their integration tests.

---
### All features are covered by at least one integration test
**Level:** Level 3 | **Pillar:** QUALITY | **Topic:** Integration Tests

### Why

Applications often fails not because a single function broke, but because two healthy functions couldn't "talk" to each other correctly.

### What

"All features covered" means that for every function of the application, there is a test case that executes the entire path required to complete that action.


### How:

Team must. be able de demonstrate all features are covered according to the test plan. Achieving feature coverage requires a disciplined approach to the development lifecycle.

---
### Integration tests must block the PR merge if they fail
**Level:** Level 3 | **Pillar:** QUALITY | **Topic:** Integration Tests

### Why ?

Quality gates on integration tests execution prevent from pushing regression in production

### What ?

To fullfill this requirement, all PR with failed executions are not mergeable & main/master branches with failed executions is not deployed

### How ?

The team must be able to demonstrate that:

>- for every PR, when integration tests fails, it's not possible to merge.
>- for main/master branches, when integration tests fails, nothing is deployed (neither in preproduction nor in production)

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
### Implement consumer contract testing
**Level:** Level 5 | **Pillar:** QUALITY | **Topic:** Integration Tests

### Why ?

**It only applies for microservices managed in the Decathlon information system. Not applicable for external API or open API.**

Consumer driven contract testing allows to confidently deploy an application (consumer) that communicate with others (providers) by testing the contract between them. In Decathlon, this is applicable for almost every application. It provides, from the customer side, confidence to release without in isolation of the provider, who gets a reliable source of information about the usage of its data, useful when testing breaking changes.

### What ?

To fulfill this requirement, the must choose a Contract Testing framework (Pact.io, Spring Cloud) and implements at least one test.

### How ?

The team must demonstrate the contracts and test location on the application repository.
Pact.io is recommended to implement contract testing.

---
### Have a quality approach written and shared with teammates
**Level:** Level 1 | **Pillar:** QUALITY | **Topic:** Organization

### Why ?

Quality management need to be structured and organized. This document allows to explain that.

### What ?

Quality approach is a document written by the team which define the quality system management: process, methods and testing activities on the whole software cycle.

### How ?

Covers all areas of testing (ex: quadrants), and non-functional testing. Define methodologies (ex: example mapping...), practices (TDD, BDD...), role and responsabilities, quality gates, qualimetry, tools, testing frameworks ...

---
### Have a test repository to manage, organize and structure manual tests
**Level:** Level 1 | **Pillar:** QUALITY | **Topic:** Organization

### Why ?

Have a test cases referential which provide all informations to validate the product by functionnal testing.

### What ?

To fulfill this requirement, you have to describe with a good formalism (Dataset need, action and assertion or gherkin language) all functionals test cases in a central place.

### How ?

Use a dedicated tool for that like XRay or other provided in the Tech Radar.


---
### Manual testing based on functional requirements (User story and/or specifications)
**Level:** Level 1 | **Pillar:** QUALITY | **Topic:** Organization

Manual tests should be based on functional requirements ( User stories,  specs .. )

### Why ?

- To be aligned with business needs/project goals

- To be aligned with what exists on Production



### How?

- Acceptance criteria must be defined on User stories /Specs in order to derive and design test cases

- Tester/Team member  cannot design test cases if the expected behavior of the system/acceptance criteria is not defined

- Tester/Team member  must ask for more information if US/Spec are not clear or expected behaviors are not defined

### Best Practices :

- Tester/Team member can perform review ceremony with Spec/US owner :

        Goal : to review tests and ensure the alignment with business needs/project goals

- 3 amigos ceremony on Agile environment

        Goal : to create tests in collaboration with Tester/PM/DEV

---
### Enforce conventional commits in your pull requests to build an automated and understandable changelog
**Level:** Level 2 | **Pillar:** QUALITY | **Topic:** Organization

### Why ?

To facilitate the understanding of the commit history. It provides an easy set of rules for creating an explicit commit history. Usefull to follow code changes and build changelog.

### What ?

To fulfill this requirement, you have to put in place a tool to avoid to push commit not aligned with your convention. You cand find the convention commit specification [here](https://www.conventionalcommits.org/en).

### How ?

The team must be able to demonstrate that a semantic check is run for every PR and is required to merge it

---
### Every non-functional change (refactoring or technical architecture) must include a formal risk analysis.
**Level:** Level 3 | **Pillar:** QUALITY | **Topic:** Organization

### Why ?

Code changes made in a refactoring, clean code or architecture tasks can change the behavior of the product. It's important that the team could expose risks behind and carry out tests phases if needed, like exploratory testing phase.

### What ?

To fulfill this requirement, team can be able to trace and identity technical tasks in its application lifecycle management system (e.g JIRA) and trigger a discussion about the risk.

### How ?

Trace and identify all technical tasks, trigger a discussion about the risk before the development phase and if needed, made adding testing activities before the deployment in production.

---
### Load testing threshold are defined & published
**Level:** Level 2 | **Pillar:** QUALITY | **Topic:** Performance Tests

### Why ?

To ensure our applications not only perform well today, but are also ready to handle future growth and increased user demand. Clear load testing objectives, published and understood by all, are crucial for guiding development and operations.  Furthermore, anticipating future capacity needs allows us to proactively plan resources and avoid performance bottlenecks as our application evolves and our business scales.

### What ?

*   **Current Performance Thresholds:** These are quantifiable targets for key performance indicators (KPIs) under the existing load.  Examples include:
    *   Response time (e.g., 95th percentile)
    *   Number of concurrent users
    *   Requests per second
    *   Maximum user capacity
    *   Maximum acceptable latency
    *   (And for mobile applications, metrics like application size, download/install/launch times, battery/memory/CPU/network usage, etc. - as listed previously)
    These thresholds should ideally be linked to current application resources (RAM, CPU, replicas, autoscaling configuration, etc.) to understand the baseline performance.

*   **Capacity Plan:** This is a forward-looking plan outlining how we will ensure performance as our application scales.  It should include:
    *   **Projected future load:**  Estimates of anticipated increases in user traffic, data volume, or transaction rates over a defined period (e.g., 1 year, 2 years).  This should be linked to business forecasts and growth projections.
    *   **Scalability strategy:**  How we plan to scale our application infrastructure (resources, architecture) to meet the projected future load while maintaining performance within the defined thresholds.
    *   **Performance re-evaluation plan:** How and when we will re-assess performance thresholds and capacity plans as the application and business evolve.

### How ?

Document both **current performance thresholds** and the **capacity plan** in a centralized, easily accessible location such as:

*   A dedicated page in your team's wiki or documentation system.
*   A dedicated repository (e.g., in GitHub) for performance documentation.

This documentation should clearly outline:

*   The specific performance thresholds for each relevant metric.
*   The methodology used to measure and validate these thresholds.
*   The projected future load scenarios and assumptions.
*   The planned capacity scaling strategies.
*   The schedule for reviewing and updating the performance thresholds and capacity plan.

Regularly review and update this documentation to ensure it remains relevant and aligned with the evolving needs of the application and the business.

---
### Load testing run on non-production environment
**Level:** Level 3 | **Pillar:** QUALITY | **Topic:** Performance Tests

### Why ?

This is the first concrete step on the load testing fulfillment. It will help you to build a secure and pertinent load testing testing scenario.

### What ?

Thoses test should be launched on a dedicated preproduction environnement. The environnement itself should have the same ressources and data volume as the production environment to perform a more relevant test.

### How ?

Create your scenarios using a load testing testing framework such as Gatling, Jmeter, Taurus... and commit them on the applicative reposity or a dedicated repository.
Thoses tests should be launched from a server/pod (not your local computer).

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
### Continuous Load tests must block the PR merge if they fail
**Level:** Level 5 | **Pillar:** QUALITY | **Topic:** Performance Tests

### Why ?

To ensure that performance is stable or improved by application changes and to automate the testing process as quickly as possible.

### What ?

Prepare specifics CI scenarios with low api calls volume and a short duration that are ran after the integration tests.

### How ?

- Create a 2 to 3 min scenarios with a volume close to your production environment
- Trigger it at the end of the deployment process on ephemeral environment
- Add assertions to this specific scenario like success rate, response time associated to a percentil
- The assertions must block the merge of the PR if not fulfilled

---
### Bug are qualified and tracked in a tool
**Level:** Level 1 | **Pillar:** QUALITY | **Topic:** Practices

### Why ?

Centralize issue tracking for clear communication and efficient problem resolution.

Improve product quality through organized bug management and data-driven insights.

### What ?

A software tool that centralises and tracks defects making it easier to manage and resolve problems.

### How ?

The team must be able to show the tool with recorded defects. (e.g. Jira)

---
### Do exploratory testing sessions
**Level:** Level 1 | **Pillar:** QUALITY | **Topic:** Practices

### Why ?

**This criteria does not apply for API or other Backend Products**

To complement other testing methods in order to execute relevant test cases not previously imagined.

### What ?

To fulfill this requirement, you must organize sessions focused on the discovery, exploration and investigation of the digital product in all its functional, graphic and ergonomic aspects.

### How ?

It is necessary to frame exploratory tests, to define the perimeter of the test, to define limits. To do this, you can choose some best practices and method (Freestyle, Scenario-based mode or Concept of a test persona).

---
### Identify critical test cases and add to the test repository
**Level:** Level 1 | **Pillar:** QUALITY | **Topic:** Practices

### Why ?

Defining your product's critical scope allows you to focus testing efforts where they matter most.

### What ?

Identify and label the criticality of each test case and feature directly within your test repository. This repository is simply the approved tool your team uses to manage tests, such as Xray.
Here are suggested steps to define your critical test cases:
- Collaborate with stakeholders: define with the Product Manager, QA, and Engineering what’s “critical” for the product.
- Identify critical features: focus on features that are core to the user journey, high business impact, or frequently used.
- Select corresponding test cases: link or create test cases that validate these critical paths.

### How ?
Make your critical tests viewable with a single click. Use your tool's features, like tags or dedicated views, to create a shareable link to the list.

---
### Each critical tests cases are associated to product functionalities in your test management tool
**Level:** Level 1 | **Pillar:** QUALITY | **Topic:** Practices

### Why ?

To identify which test cases are linked with each features. In order to calculate coverage easily and create a traceability matrix.

### What ?

Features map have to be complete. Identify and label the criticality of each test case and feature directly within your test repository. This repository is simply the approved tool your team uses to manage tests, such as Xray.
Here are suggested steps to define your critical test cases:
- Collaborate with stakeholders: define with the Product Manager, QA, and Engineering what’s “critical” for the product.
- Identify critical features: focus on features that are core to the user journey, high business impact, or frequently used.
- Select corresponding test cases: link or create test cases that validate these critical paths.

### How ?

The team must be able to show this complete features map with at least one test per critical feature. Thanks to that, the overall test coverage can be computed.

---
### Have a way to get and score the perceived quality from users
**Level:** Level 1 | **Pillar:** QUALITY | **Topic:** Practices

### Why ?

The quality level of a product or service corresponds to the average perception level of its users.

### What ?

Obtain regular the quality perceived by your users.

### How ?

The team must be able to give a quality score based on user feedbacks. This could be a rating from the Google Play store or the Apple Store for mobile applications, a survey (ie: Google Form) sent to users for applications, the Net Promoter Score, Medallia...

---
### Make sure product needs are well described, testable and without any ambiguity according to a shift left approach
**Level:** Level 2 | **Pillar:** QUALITY | **Topic:** Practices

### Why ?

Allows the team to be in the best conditions in order to deliver as ***quickly*** as possible with a high level of quality, avoiding surprises, bugs, misunderstandings as soon as possible and so ***reduce cost overheads from the non quality***

### What ?

Key is to identify the rights channels or ressources (Business specifications, videos, prototypes, wireframes) to well described what the team has to do and make sure that you are able to design all tests (whatever the type of tests) linked to the needs. These tests have to be validated and understood by the whole team.

### How ?

##### Process

Your process ensure that no development can start if the need and tests on the need are not defined and validated and so, ***ready***.

It can be managed easily by a ***maturation process*** or a least a definition of ready (***DOR***).
A maturation workflow can be set in your application lifecycle management through a succession of steps. You can defined output criterias for each of these steps.

An example below of a maturation workflow with each step requierements. Of course, because it's an example, you must adapt it regarding your context.

>1. Backlog
Functional Specifications
Flows to complete the task
Business rules
Pre-conditions (dependencies, external APIs, connected user?, ...)
Expected behaviors (nominal cases & errors)
>
>2. UX/UI
Screenshots / wireframes (Figma)
Specifications Design / Front
Design failure/error case
>
>3. TECH ANALYSIS
Technical validation
Split into small tasks (Work in small batches)
Storybook: Yes? No?
Identify network calls that need to be mocked for testing
Validate the operation of external APIs and documentation provided
Identify new data to add to the Strapi data initialization script
>
>4. QUALITY
Acceptance criteria
Update TNR: Yes? No?
Create TNR: Yes? No?
Data set is needed: Yes? No?
Automation test: Yes? No?
>
>5. READY TO DEVELOP
Estimated
Validated by the team

##### Practices

Following the ***'Given-When-Then'*** format for requirements significantly enhances testability, ensuring clarity and streamlined verification.

An excellent way to make almost of all with only one practice is to use the Example mapping. Very usefull for frontend and app applications and can be used also for backend application.

>How to make Example Mapping:
>- The PM show and explain the need to the team and write it in a yellow card
>- There are some discusion about the need and all management rules must be written under the yellow card in blue cards
>- Behind each blue card, team must write examples to validate the rule. Write it on green cards.
>- A high number of red cards highlights the fact that several (sometimes crucial) points remain unresolved and will require further business feedback. Development then simply cannot begin.
>- Too many blue cards can reveal a need that is too bulky and needs to be divided into sub-functionalities.
>- Too many examples, although useful in some cases, can also show that we are probably mixing up several rules.

##### Summary

*You've understood there isn't a single way to do, but keep in mind the target : Take time to be ready increase how fast you deliver and how well you deliver*

---
### Review test suite during post-mortems
**Level:** Level 2 | **Pillar:** QUALITY | **Topic:** Practices

### Why ?

Post-mortems are crucial for analysing production incidents and implementing measures to prevent their repetition.

A thorough review of existing test cases (both manual and automated) during a post-mortem helps pinpoint gaps that allowed the defect to reach production.

### What ?

Before the post-mortem meeting, investigate whether any existing tests cover the defect that caused the incident.

If the post-mortem reveals a gap in test coverage, the action plan must include updates to the test case suite.

Not all post-mortems will necessitate changes to the test suite. Updates are only required when a coverage gap is identified.

This applies to all types of testing, including: - Functional testing - Non-functional testing (e.g., performance, security)

### How ?

The team must be able to share past post mortem records (usually in Confluence). These records should clearly document instances where test case suite coverage was analysed and/or updated.

---
### Engineering team is autonomous for test design and execution
**Level:** Level 3 | **Pillar:** QUALITY | **Topic:** Practices

### Why ?

You build it, you test it, you run it. Testing is not only the part of dedicated roles.
Testing activities, whatever their form, must be carried out by the whole team in order to have quality throughout the software cycle and also reduce test feedback loops during all stages of the development process.

### What ?

With or without QA/QE, the whole team handles organizing and improving testing efforts as much "as code" as possible

### How ?

All teammates participate in test design, test execution and shortening test feedback loops to address issues/changes  as quickly as possible.




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
### Measure the quality of the tests and relevance of the test strategy
**Level:** Level 5 | **Pillar:** QUALITY | **Topic:** Practices

Why?

To ensure that testing efforts are focused on the right areas, maximizing risk mitigation while maintaining delivery speed. Without measuring effectiveness, a test suite can become "technical debt" either wasting time on redundant tests or leaving critical business risks unaddressed.

What?

This involves analyzing the correlation between test execution and actual production quality. It covers:
- Test Pyramid Health: Maintaining the right balance between Unit, Integration/API, and E2E tests.
- Risk Alignment: Ensuring test coverage matches the most critical business functionalities.
- Detection Power: Evaluating the ability of the test suite to catch regressions before they reach the user.

How?

Key Metrics: Tracking the Defect (bugs found in production vs. testing), Test Flakiness, and Execution Time (feedback loop efficiency).
- Regular Audits: Periodically reviewing the test suite to prune obsolete, redundant, or brittle tests.
- Quality Analysis: Using techniques like Code Coverage or Mutation Testing to ensure tests are meaningful and not just "passing."
- Risk-Based Adaptation: Continuously adjusting the test depth based on the impact and probability of failure for new features.

---
### Track production defects
**Level:** Level 1 | **Pillar:** QUALITY | **Topic:** Qualimetry

### Why ?

Understanding the volume of user-impacting production defects enables the team to prioritize efforts, directly enhancing product quality.

### What ?

Only qualified bugs, whether reported by users through customer support or identified internally by the team, are included in the current production defect count.

“Qualified” as confirmed that the reported issue is a true defect in the software, and not a misunderstanding of how the software should work, or a user error.

### How ?

The team must be able to share the current number of opened bugs in production.

---
### Use production defect to prioritise tasks
**Level:** Level 2 | **Pillar:** QUALITY | **Topic:** Qualimetry

### Why?

To promote proactive resolution of production defects by integrating their count and impact into the task prioritization process, ensuring the team is aware of and addresses critical issues promptly.

### What?

When assigning tasks (e.g., during daily stand-ups, sprint planning), developers and the team must prioritize their work based on the production defect backlog.

### How?

The team must demonstrate how the production defect backlog is integrated into their task prioritization process. Acceptable forms of demonstration include documented processes (e.g., in Confluence), Jira activity showing defect prioritization, or custom visualizations (e.g., Jira swimlanes, dashboards) that highlight production defect status.

---
### Measure the functionality/feature coverage performed by the integration tests
**Level:** Level 3 | **Pillar:** QUALITY | **Topic:** Qualimetry

### Why ?

The traceability matrix makes it possible to establish, in the form of a table with two entries, the n-to-n relationships existing between various elements. Its main purpose is to synthesize the links between: Functional tests and specifications. The functionality coverage by the tests allow to know what are  functionnalities covered by functional tests. It's a important measure to evaluate the functional garantee provided to your users.

### What ?

The functionality coverage is the ratio between the total number of functionalities which have at least one functional test divided by the total number of the functionnalities. It's important that functionnalities found in the traceabilty matrix are representatives of the product. The depth of functionnality description is at the discretion of the teams.

### How ?

Build your traceability matrix in a tool, a sheet. Ensure that all functionnalities of your product are mentioned into. Put functionnalities in the row of the matrix, and put all functional tests in the column. As soon as a functional test cover a functionnality, put a cross or something like that to inform in the matrix the covering information. Count all functionnalities which are covered by at least one functional test and divide it by the total count of functionnalities. You obtain the functionality coverage.

---
### All results of your automated test execution are published automatically and available for the whole team
**Level:** Level 3 | **Pillar:** QUALITY | **Topic:** Qualimetry

### Why ?

Get quickly and easily informations about automated test results is important to improve developer experience and the test results management. So that improve the productivity of the team and the quality of the product.

### What ?

For each automated test execution, results must be published somewhere, in a place which is known and available for all teamates. For all tests activities before the merge request, results can be directly published in a central place as the pull request. For testing activities after merging, results can be published on a dedicated dashboard (Ex : ARA, mochawesome ...)

### How ?

About testing activities before merge request, CI/CD must published the output of testing activities inside the pull request or provide a link which redirect to a dedicated dashboard (Example: Sonar Cloud).
Integration should be handled from CI/CD code (example: github action steps) for testing activities before and after merge.

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
### Use quality metrics to improve efficiency
**Level:** Level 3 | **Pillar:** QUALITY | **Topic:** Qualimetry

/

---
### Perform static code analysis locally
**Level:** Level 1 | **Pillar:** QUALITY | **Topic:** Static Code Analysis

### Why ?

Static code analysis, as unit test, provides some indicators on an application code without building it. Such indicators on code are related to: - errors (that can lead to bugs) - quality (respect of best practices) - security (vulnerabilities).

### What ?

To fulfill this requirement, you must have a static code analysis tool implemented in your project, such as Sonarcloud and/or Linter.

### How ?

The team must be able to demonstrate a previous static code analysis.

---
### Static Code Analysis runs in CI
**Level:** Level 1 | **Pillar:** QUALITY | **Topic:** Static Code Analysis

### Why ?

Running Static Code Analysis in Continuous Integration ensure that such analysis are run frequently so that possible issues can be visible to the team.

### What ?
To fulfill this requirement, a "static code analysis" step must be implemented in Continuous Integration at the Pull Request level.

### How ?

The team must be able to demonstrate that static code analysis is run for every PR.

---
### Static Code Analysis must block the PR merge if it fails
**Level:** Level 2 | **Pillar:** QUALITY | **Topic:** Static Code Analysis

### Why ?

Make sure that any issue brought by static code analysis will never be merged and are fixed right away.

### What ?

To fulfill this requirement, the workflow that run static code analysis must be a required status check in the project default branch.

### How ?

The team must be able to demonstrate that static code analysis is a required status check for every PR.

---
### Static Code Analysis threshold must match high software industry standard on new code
**Level:** Level 3 | **Pillar:** QUALITY | **Topic:** Static Code Analysis

### Why ?

Ensuring that static code analysis indicators are always at a high level enable to deliver code matching high standard of code quality continuously and keep the technical debt manageable.

### What ?

To fulfill this requirement, the SonarCloud profile must be set to "Sonar Way".

### How ?

The team must be able to demonstrate that the SonarCloud analysis profile is "Sonar Way".

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
### Perform unit test locally
**Level:** Level 1 | **Pillar:** QUALITY | **Topic:** Unit Tests

### Why ?

It ensures code maintainability, provides documentation for developers and more importantly, detect possible bug at the earliest that will be easy to reproduce and thus, fix.

### What ?

To fulfill this requirement, a unit test framework must be implemented with one appropriate test as well.

### How ?

The team must be able to demonstrate the launch of their unit tests locally.

---
### Unit tests coverage must be measured
**Level:** Level 1 | **Pillar:** QUALITY | **Topic:** Unit Tests

### Why ?

Unit tests coverage is an indicator (not the only one) about the faith a team can have in their tests.

### What ?

To fulfill this requirement, the unit test coverage must be measurable easily.

### How ?

The team must be able to share the unit tests coverage measured by the framework or using SonarCloud

---
### Unit tests run in CI
**Level:** Level 1 | **Pillar:** QUALITY | **Topic:** Unit Tests

### Why ?

Running unit tests in Continuous Integration ensure that tests are run frequently so that any anomalies added to the code will be detected before going in production.

### What ?

To fulfill this requirement, a "unit test" step must be implemented in Continuous Integration at the Pull Request level.

### How ?

The team must be able to demonstrate that, for every PR, unit tests are run within CI.

---
### Unit tests must block the PR merge if they fail
**Level:** Level 2 | **Pillar:** QUALITY | **Topic:** Unit Tests

### Why ?

Make sure that any regression brought by unit tests will never be merged and are fixed right away.

### What ?

To fulfill this requirement, the workflow that run unit tests must be a required status check in your default branch.

### How ?

The team must be able to demonstrate that, for every PR, the workflow that run unit tests is a required status check.

---
### Unit tests coverage threshold must be enforced in CI
**Level:** Level 3 | **Pillar:** QUALITY | **Topic:** Unit Tests

### Why ?

Make sure that the unit tests coverage is kept at a certain level, thus the technical debt cannot grow any longer.

### What ?

To fulfill this requirement, the unit test coverage must be measured at the PR level and if it doesn't meet the criteria, the PR can't be merged.

### How ?

The team must be able to demonstrate that, for every PR, the workflow responsible for measuring the unit tests coverage is required a status check.

---
### Unit tests coverage threshold must match high software industry standard on new code
**Level:** Level 3 | **Pillar:** QUALITY | **Topic:** Unit Tests

### Why ?

Ensuring the unit tests coverage stays at a minimum level enable to deliver tested code continously and keep the technical debt manageable.

### What ?

To fulfill this requirement, the unit tests coverage must be enforced at 80%, as it is instructed by Sonar Cloud.

### How ?

The team must be able to demonstrate that, for every PR, the coverage is measured and enforced at a minimum of 80%.

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
### DISASTER RECOVERY PLAN :
Manual DRP test on my product is performed regularly based on tiering rank objectives
**Level:** Level 3 | **Pillar:** OPERATION | **Topic:** Availability / Risk Management

### Expected
* The DRP tasks are tested at least once a year in prod
* A document is available to check last test occurence performed and display all actions performed
* Last execution date is filled in [Cybersecurity tool](https://airtable.com/appfC2IUoOeLkhYb6/pagnsmMcCjUL1PFbF) ("Date of last DRP test")

### Useful link
* [Risks&DRP wiki](https://decathlon.atlassian.net/wiki/x/YjkGCw)


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
### RISKS:
Chaos testing automation is setup
**Level:** Level 5 | **Pillar:** OPERATION | **Topic:** Availability / Risk Management

### Expected
You have a running chaos testing tool set up on your infra, this tool breaks things randomly

---
### POST-INTERVENTION:
Post-intervention checks are done with an acceptance plan test which may involve end-users
**Level:** Level 2 | **Pillar:** OPERATION | **Topic:** Change Management

### Expected
* At the end of the intervention, you perform detailed checks to ensure that there is no major impact or regression
* These checks may require the involvement of end-users

### Usefull link
* [Sportycoins - Checklist MAJOR RELEASE](https://decathlon.atlassian.net/wiki/x/1E1mCw)
* [Stock Reliability - Post Intervention tests](https://decathlon.atlassian.net/wiki/spaces/XCOM/pages/631603452/Post+Migration+Tests)

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
### You use at least one library for automated accessibility testing in your CI
**Level:** Level 2 | **Pillar:** ACCESSIBILITY | **Topic:** Accessibility

### Why ?

Automated evaluation tools will rarely be silver bullets when it comes to assessing accessibility requirements, but they can help to gain perspective on the maturity of a project, and reveal blocking issues. Having such a tool in a CI can prevent developers from delivering unaccessible code.

### What ?

Implementing an automated accessibility testing tool in your CI. LightHouse is authorized to use in that purpose. You can also . We aim to propose other tools to do so in the future (axe-core).

### How ?

- Implement [LightHouse CI](https://github.com/GoogleChrome/lighthouse-ci) into your CI.
- Make sure accessibility issues are correctly raised by [SonarQube Cloud](https://sonarcloud.io/projects) when building your GitHub Pull Requests.
- Use plugins to find accessibility issues in your code like eslint-plugin-jsx-a11y, [axe-core](https://github.com/dequelabs/axe-core), etc.

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
### Your digital product or service is compliant with the relevant AAA criteria of the latest version WCAG
**Level:** Level 5 | **Pillar:** ACCESSIBILITY | **Topic:** Accessibility

### Why ?

Level AAA is the highest possible conformance level in WCAG, and as a result holds organisations to the highest standard of accessibility. At this level, the web page and content satisfy all Level A, Level AA, and Level AAA success criteria. Although level AAA may not be applicable or realistic for everyone to achieve, organisations should strive to meet as many of its criteria as possible.

### What ?

Meet the relevant AAA criteria. You can find a full list of all these criteria in the [W3C Quick reference tool](https://www.w3.org/WAI/WCAG22/quickref/?currentsidebar=%23col_customize&levels=a%2Caa) or inthe [French RGAA website (in french)](https://accessibilite.numerique.gouv.fr/ressources/criteres-aaa/)

### How ?

[Ask for an audit by following this documented process](https://decathlon.atlassian.net/wiki/spaces/TO/pages/568820448/How+to+get+audited)

---
### The platform supports re-processing large windows of historical events. This is achieved via mechanisms like resetting consumer offsets (e.g., in Kafka), re-publishing from a persistent event store, or querying a time-stamped data lake. This capability is documented, shared, and tested
**Level:** Level 3 | **Pillar:** STREAMING | **Topic:** Event Streams

**Why:** This is the goal. You can rebuild an entire service's state from scratch, onboard a new analytics system, or recover from a catastrophic bug that corrupted data for hours.

---
