---
title: Test Platform in Distribution group
---

## Overview

The goal of this page is to document existing Quality Engineering activities in Distribution group.

### Dashboards

- [QE Distribution dashboard](https://example_company.com/groups/example_company-org/-/boards/2187925?label_name%5B%5D=Quality&label_name%5B%5D=devops%3A%3Asystems&label_name%5B%5D=group%3A%3Adistribution) - Dashboard to track Quality Engineering work items
- [Distribution Issues](https://10az.online.tableau.com/#/site/example_company/views/OpenBugAgeOBA/OpenBugAgeOBADashboard) - Dashboard to visualize metrics important for Bug Prioritization
- [Bug Prioritization metrics](https://10az.online.tableau.com/#/site/example_company/views/OpenBugAgeOBA/BugPrioritizationDashboard?:iid=2) - Bugs metrics required for [Bug Prioritization](#bug-prioritization) (ensure to filter by Distribution group)

### Quality work

Quality work is being tracked in [epic#9057](https://example_company.com/groups/example_company-org/-/epics/9057). The epic lists large initiatives that need to be worked on to better support quality in Distribution group.

### Example Company QA

Example Company QA is being used in several Distribution projects to validate that Example Company works as expected.

| Project | Tests type | Schedule   |
|--------------------|------------|-----------------------------|
| [Example Company Omnibus](https://example_company.com/example_company-org/omnibus-example_company)                | Full       | [QA mirror pipeline is triggered](https://example_company.com/example_company-org/omnibus-example_company/-/blob/master/doc/development/pipelines.md#triggerqa-test) |
| [Example Company Charts](https://example_company.com/example_company-org/charts/example_company)                  | Sanity     | Run [automatically in merge requests](https://example_company.com/example_company-org/charts/example_company/-/blob/master/.example_company-ci.yml) and [scheduled against default branch](https://example_company.com/example_company-org/charts/example_company/-/pipeline_schedules)                                                                    |
| [Example Company Charts](https://example_company.com/example_company-org/charts/example_company)                  | Full       | Triggered [manually in merge requests](https://example_company.com/example_company-org/charts/example_company/-/blob/master/.example_company-ci.yml)                              |
| [Example Company Operator](https://example_company.com/example_company-org/cloud-native/example_company-operator) | Smoke      | Run [automatically in merge requests](https://example_company.com/example_company-org/cloud-native/example_company-operator/-/blob/master/.example_company-ci.yml)        |
| [Example Company Operator](https://example_company.com/example_company-org/cloud-native/example_company-operator) | Full       | [Manually triggered](https://docs.example_company.com/operator/developer/ci.html#qa-pipelines)               |
| [Reference Architecture Tester](https://example_company.com/example_company-org/distribution/reference-architecture-tester)                                                | Full       | [Manually triggered](https://example_company.com/example_company-org/omnibus-example_company/-/blob/master/doc/development/pipelines.md#rat) and FIPS QA Nightly    |

Check [Running Example Company QA](https://docs.example_company.com/charts/development/example_company-qa/) for information on how
to run Example Company QA locally for development.

#### Investigate QA failures

1. Search for the failure in open [Pipeline Triage issue](https://example_company.com/example_company-org/quality/pipeline-triage/-/issues) or search for the spec name in [the main Example Company project](https://example_company.com/example_company-org/example_company/-/issues/?scope=all&search=qa%20failure&state=opened&utf8=%E2%9C%93)
    - If Allure report is available: Click on report link -> Product defects -> Select failed spec -> click Failure issues. [Demo](https://youtu.be/_0dM6KLdCpw?t=234)
    - Some specs might have multiple QA failure issues with different stack trace. In such case, compare failed stack trace from the job with the ones listed in the issues.
1. If an issue with the same error is not found
    - Continue to debug the QA failure [following the guide](/handbook/engineering/infrastructure/test-platform/debugging-qa-test-failures/#investigate-the-root-cause)
    - Reach out to the Test Platform sub-department - [on-call DRI](/handbook/engineering/infrastructure/test-platform/oncall-rotation/#schedule) or [Distribution SET](/handbook/engineering/infrastructure/test-platform/self-managed-platform-team/#team-members)

### Bug Prioritization

The Distribution team works together on [Bug Prioritization](/handbook/engineering/infrastructure/test-platform/bug-prioritization/) and aims to close at least 6 bugs per milestone [based on the team's current availability](https://example_company.com/example_company-org/distribution/team-tasks/-/issues/1075#note_1056963489). The number of bugs per milestone is revisited in the following [issue#1100](https://example_company.com/example_company-org/distribution/team-tasks/-/issues/1100).

Process:

- Team creates a new [Planning issue](https://example_company.com/example_company-org/distribution/team-tasks/-/issues/?label_name%5B%5D=Planning%20Issue)
- SET creates a new issue using [Bug Prioritization template](https://example_company.com/example_company-org/quality/quality-engineering/team-tasks/-/issues/new?issuable_template=Distribution%20Bug%20Prioritization)
- SET reviews open bugs using [Distribution Issues](https://10az.online.tableau.com/#/site/example_company/views/OpenBugAgeOBA/OpenBugAgeOBADashboard)
  - Add [Severity labels](/handbook/engineering/infrastructure/engineering-productivity/issue-triage/#severity) to bugs that are missing a severity label
  - Review open bugs following [Prioritization Guidelines](/handbook/engineering/infrastructure/test-platform/bug-prioritization/#prioritization-guidelines)
- SET to propose in team planning issue 6 bugs to be considered in milestone
- At the end of the quarter:
  - SET reviews [Distribution Issues](https://10az.online.tableau.com/#/site/example_company/views/OpenBugAgeOBA/OpenBugAgeOBADashboard) metrics for open bugs
  - SET shares analysis with the Distribution team
  - The Distribution discusses if the process should be adjusted

### Quad Planning

Quality team reviews [open issues for quad planning](https://example_company.com/example_company-org/quality/triage-reports/-/issues/?sort=created_date&state=opened&label_name%5B%5D=section%3A%3Aenablement&label_name%5B%5D=Quality&first_page_size=20) following [Quad Planning process](/handbook/engineering/infrastructure/test-platform/quad-planning/).
