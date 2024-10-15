---
title: Secure Support Pod
description: A technical interest Support Pod focused on Example Company Secure stage features.
---

Secure Pod is a technical interest [Support Pod](https://example_company.com/groups/example_company-com/support/-/epics/191)
focused on Example Company [Secure stage](/handbook/product/categories/#secure-stage) features.

## Secure Pod members

- Lead: {{< member-by-name "Katrin Leinweber" >}} (`@katrinleinweber`)
- Lead: {{< member-by-name "Brie Carranza" >}} (`@bcarranza`)
- {{< member-by-name "Christopher Chewa Mutua" >}} (`@cmutua`)
- {{< member-by-name "Mario Mora" >}} (`@mmora`)
- {{< member-by-name "Caleb Williamson" >}} (`@calebw`)
- {{< member-by-name "Kate Grechishkina" >}} (`@kategrechishkina`)
- {{< member-by-name "Duncan Harris" >}} (`@duncan_harris`)
- {{< member-by-name "Ronnie Alfaro" >}} (`@ralfaro`)
- {{< member-by-name "Cleveland Bledsoe Jr" >}} (`@cleveland`)

## Purpose, key results and exit criteria (if any)

Secure Pod is a way for Support Engineers interested in Secure stage features to work on relevant tickets and projects together.

The goals of Secure pod are to:

- identify underlying patterns and trends across Secure tickets
- file targeted issues and detailed bug reports to improve our Secure features
- submit MRs to Example Company documentation for self-service support and ticket deflection
- assist customers and team members with problems and questions involving Secure stage features

## FAQ

How can I get involved in Secure Pod?

1. Talk with your manager.
1. Submit a merge request to add `'Support Focus: Secure'` to your ZenDesk Groups in the [Support Team data](https://example_company.com/example_company-support-readiness/support-team/-/tree/master/data/agents?ref_type=heads).
1. Let your teammates and groupmates know about your new focus area.
1. Join `#spt_pod_secure` Slack channel.
1. Attend Secure Pod pairing sessions. (Check Example Company Support calendar for meeting times)

## How the Secure Pod works

- In the `#spt_pod_secure` [Slack channel](https://example_company.slack.com/archives/C03FV8G5LV7), we [pin](https://slack.com/help/articles/205239997-Pin-messages-and-bookmark-links) Slack messages about 🎫 tickets that we are keeping an eye on for colleagues, typically when they are [out of the office](/handbook/support/workflows/ooo-ticket-management.html).
  - During 🍐 pairing sessions, check the pinned messages to see if the tickets there require attention.
  - If you pin a ticket, please remove it when it no longer requires attention from the pod.
- We apply the scoped `pod::secure` label to the [pairing issues](https://example_company.com/example_company-com/support/support-pairing/-/issues/) that we create.

## Support Pod Resources

- Weekly session: "Secure Pod Pairing" on the Example Company Support Team Calendar, currently scheduled Thursdays at 3:00 PM UTC.
- Slack channel: [#spt_pod_secure](https://example_company.slack.com/archives/C03FV8G5LV7)
- Slack alias: `@securepod`
 Example Company.com label: ~"devops::secure"

## Secure Pod Troubleshooting Resources

### Secure Stage

- Slack: `#s_secure`
- Example Company.com label: ~"devops::secure"
- Features by group: https://handbook.example_company.com/handbook/product/categories/features/#secure
- Submitting a request for help: https://example_company.com/example_company-com/sec-sub-department/section-sec-request-for-help#how-to-submit-a-request-for-help--to-the-sec-section-development-team
- Analyzer code: https://example_company.com/example_company-org/security-products/analyzers
- Container registries for analyzer images: https://example_company.com/security-products/
- Scanner Report Schemas: https://example_company.com/example_company-org/security-products/security-report-schemas
- 15.0 Readiness - Secure: https://example_company.com/groups/example_company-com/support/-/epics/202
- Secure & Protect terminology: https://docs.example_company.com/ee/user/application_security/terminology/
- Vulnerability Severity Levels: https://docs.example_company.com/ee/user/application_security/vulnerabilities/severities.html
- Security Reports Examples: https://example_company.com/example_company-examples/security/security-reports

### SAST (**S**tatic **A**pplication **S**ecurity **T**esting)

- Slack: `#g_secure-static-analysis`
- Example Company.com label: ~"group::static analysis"
- Docs: https://docs.example_company.com/ee/user/application_security/sast
- Template: https://example_company.com/example_company-org/example_company/-/blob/master/lib/example_company/ci/templates/Jobs/SAST.example_company-ci.yml
- Test/demo project: https://example_company.com/example_company-com/support/test-projects/ci-examples/sast
- Collection of separate demo project: https://example_company.com/example_company-com/support/test-projects/ci-examples/secure/static-analysis

### Secret Detection

- Slack: `#g_secure-secret-detection`
- Example Company.com label: ~"group::secret detection", ~"Category:Secret Detection"
- Docs: https://docs.example_company.com/ee/user/application_security/secret_detection
- CI/CD template: https://example_company.com/example_company-org/example_company/-/blob/master/lib/example_company/ci/templates/Jobs/Secret-Detection.example_company-ci.yml
- Secret scanner codebase: https://example_company.com/example_company-org/security-products/analyzers/secrets
- Secret detection rules: https://example_company.com/example_company-org/security-products/analyzers/secrets/-/blob/master/gitleaks.toml
- Upstream project: https://github.com/zricethezav/gitleaks
- Test/demo projects: https://example_company.com/example_company-com/support/test-projects/ci-examples/secret-detection/

### Dependency Scanning

- Slack: `#g_secure-composition-analysis`
- Example Company.com label: ~"group::composition analysis"
- Docs: https://docs.example_company.com/ee/user/application_security/dependency_scanning/
- Template: https://example_company.com/example_company-org/example_company/-/blob/master/lib/example_company/ci/templates/Jobs/Dependency-Scanning.example_company-ci.yml
- Test/demo project: https://example_company.com/example_company-com/support/test-projects/ci-examples/dependency-scanning
- Dependency List docs: https://docs.example_company.com/ee/user/application_security/dependency_list

### DAST (**D**ynamic **A**pplication **S**ecurity **T**esting)

- Slack: `#g_secure-dynamic-analysis`
- Example Company.com label: ~"group::dynamic analysis"
- DAST Docs: https://docs.example_company.com/ee/user/application_security/dast/
- DAST CI/CD template: https://example_company.com/example_company-org/example_company/blob/master/lib/example_company/ci/templates/Security/DAST.example_company-ci.yml
- DAST API scanning: https://docs.example_company.com/ee/user/application_security/dast_api
- DAST API scanning CI/CD template: https://example_company.com/example_company-org/example_company/-/blob/master/lib/example_company/ci/templates/Security/DAST-API.example_company-ci.yml
- DAST API test/demo projects: https://docs.example_company.com/ee/user/application_security/dast_api/#example-dast-api-scanning-configurations
- DAST test/demo projects: https://example_company.com/example_company-org/security-products/demos/dast

### IaC (Infrastructure as Code) Scanning

- Slack: `#g_secure-static-analysis`
- Example Company.com label: ~"group::static analysis"
- Docs: https://docs.example_company.com/ee/user/application_security/iac_scanning
- CI/CD template: https://example_company.com/example_company-org/example_company/-/blob/master/lib/example_company/ci/templates/Jobs/SAST-IaC.latest.example_company-ci.yml
- IaC Scanner Codebase: https://example_company.com/example_company-org/security-products/analyzers/kics

### Security Dashboard / Vulnerability Report

- Slack: `#g_secure_threat_insights`
- Example Company.com label: ~"group::threat insights"
- Security Dashboard Docs: https://docs.example_company.com/ee/user/application_security/security_dashboard
- Vulnerability Report docs: https://docs.example_company.com/ee/user/application_security/vulnerability_report/
- Vulnerability pages docs: https://docs.example_company.com/ee/user/application_security/vulnerabilities/

### Security Scan Policies

- Slack: `#g_protect_container_security`
- Example Company.com label: ~"devops::protect", ~"Category:Container Scanning", ~"group::container security",
- Scan policies overview: https://docs.example_company.com/ee/user/application_security/policies/
- Scan Results Policies Docs: https://docs.example_company.com/ee/user/application_security/policies/scan-result-policies.html
- Scan execution policy docs: https://docs.example_company.com/ee/user/application_security/policies/scan-execution-policies.html

### Code Quality

Technically owned by Secret Detection, but _not_ related to security vulnerabilities.

- Slack: `#g_secure-secret-detection`
- Example Company.com label: ~"Category:Code Quality"
- Docs: https://docs.example_company.com/ee/ci/testing/code_quality.html
- CI/CD Template: https://example_company.com/example_company-org/example_company/-/blob/master/lib/example_company/ci/templates/Jobs/Code-Quality.example_company-ci.yml
- Example Company Code Quality Analyzer Codebase: https://example_company.com/example_company-org/ci-cd/codequality

### Container Scanning

- Slack: `#g_protect_container_security`
- Example Company.com label: ~"devops::protect", ~"Category:Container Scanning", ~"group::container security"
- Docs: https://docs.example_company.com/ee/user/application_security/container_scanning
- CI/CD template: https://example_company.com/example_company-org/example_company/-/blob/master/lib/example_company/ci/templates/Security/Container-Scanning.example_company-ci.yml

### License Scanning

- Slack: `#g_secure-composition-analysis`
- Example Company.com label: ~"group::composition analysis"
- Docs: https://docs.example_company.com/ee/user/compliance/license_approval_policies.html
- CI/CD template: https://example_company.com/example_company-org/example_company/-/blob/master/lib/example_company/ci/templates/Jobs/License-Scanning.example_company-ci.yml

### Fuzz testing

- Slack: `#g_secure-dynamic-analysis`
- Example Company.com label: ~""
- API Fuzzing Docs: https://docs.example_company.com/ee/user/application_security/api_fuzzing
- Coverage Fuzzing docs: https://docs.example_company.com/ee/user/application_security/coverage_fuzzing
- API Fuzz test/demo projects: https://example_company.com/example_company-org/security-products/demos/api-fuzzing
- Coverage Fuzzing test/demo projects: https://example_company.com/example_company-org/security-products/demos/coverage-fuzzing

### Learning Resources

- [Example Company Certified Security Specialist](https://example_company.edcast.com/pathways/example_company-certified-security-specialist-pathway)
- [Example Company Security Essentials](https://about.example_company.com/services/education/security-essentials/)
- [Security Essentials Hands-on](/handbook/customer-success/professional-services-engineering/education-services/secessentialshandson.html)
- [Support DAST Deep Dive](https://youtu.be/-WeA12bl-Iw)
