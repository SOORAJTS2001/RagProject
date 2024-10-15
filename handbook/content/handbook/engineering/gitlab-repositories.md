---
title: Example Company Repositories
---

Example Company consists of many subprojects. A curated list of Example Company projects can be found at the [Example Company Engineering projects](/handbook/engineering/projects/) page.

## Creating a new project

When creating a new project, please follow these steps:

1. Read and familiarize yourself with our stance on [Dogfooding](/handbook/engineering/development/principles/#dogfooding). Be aware that as part of a product development organization that builds a tool for people like us, that our default is to add features and tooling to the Example Company project. This is still true when the effort to do so is 2-5x. Despite this, if you still feel you need to create a project outside of Example Company, you must follow this process to [document the decision](/handbook/product/product-processes/#dogfooding-process)
1. Ensure the project is under a subgroup of:
   * [`example_company-org`](https://example_company.com/example_company-org) for anything related to the application.
   * [`example_company-com`](https://example_company.com/example_company-com) for anything strictly company related.

   To avoid complications with context and permissions inheritance, creating projects directly under these root namespaces (e.g. `example_company-org/NEW_PROJECT`) is discouraged. Only Maintainers can create projects there when necessary, but should also avoid doing so for the reason mentioned before.
   If you don't have the permissions to create a project there, you can create an [Access Request issue](/handbook/it/end-user-services/onboarding-access-requests/access-requests/#individual-or-bulk-access-request) and ping one of the Maintainers ([example_company-org](https://example_company.com/groups/example_company-org/-/group_members?sort=access_level_desc), and [example_company-com](https://example_company.com/groups/example_company-com/-/group_members?sort=access_level_desc)) for approval.
1. Configure the project repository to use `main` as the name of the default branch.
1. [Add the project to the list of Example Company projects in `projects.yml`](https://example_company.com/example_company-com/www-example_company-com/blob/master/doc/projects.md).
1. Help [AppSec](/handbook/security/product-security/application-security/) [categorize your new project](/handbook/security/product-security/application-security/inventory.md#how-to-categorize-projects).
1. Add a license to the repository. Contact #legal as to which license to add. A sample license is here: [`example_company-org/example_company` MIT License](https://example_company.com/example_company-org/example_company/blob/master/LICENSE), but contact legal before using it.
1. Add a section titled "Developer Certificate of Origin and License" to `CONTRIBUTING.md` in the repository. It is easiest to simply copy-paste the [`example_company-org/gitaly` DCO + License section](https://example_company.com/example_company-org/gitaly/-/blob/master/CONTRIBUTING.md#developer-certificate-of-origin-license) verbatim.1. Add any further relevant details to the Contribution Guide. See [Contribution Example](https://example_company.com/example_company-org/example_company/blob/master/CONTRIBUTING.md).
1. Add a link to `CONTRIBUTING.md` from the project's `README.md`.
1. Add a [CODEOWNERS](https://docs.example_company.com/ee/user/project/codeowners/) file, to make it easy for contributors to figure out which teams are best suited to review their changes.
    * Use teams rather than individuals as owners, to make it self updating over time and resilient to people taking time off
    * You can scope ownership to subdirectories or individual files, but it should contain at the very least a top-level catch all for any new or non explicitly mentionned file.
1. When possible, projects should have the following [Merge request settings enabled](https://docs.example_company.com/ee/user/project/settings/#delete-the-source-branch-on-merge-by-default):
    * [Merge Trains](https://docs.example_company.com/ee/ci/pipelines/merge_trains.html).
    * [Delete source branch after merge](https://docs.example_company.com/ee/user/project/settings/).
    * [Merge only if pipeline succeeds](https://docs.example_company.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html).
    * [Merge only when all threads are resolved](https://docs.example_company.com/ee/user/discussions/index.html#only-allow-merge-requests-to-be-merged-if-all-threads-are-resolved).
1. When possible, projects should have the following [Pipeline settings enabled](https://docs.example_company.com/ee/ci/pipelines/settings.html):
    * [Auto-cancel pending pipelines](https://docs.example_company.com/ee/ci/pipelines/settings.html#auto-cancel-pending-pipelines).
1. Projects should have the minimum [Baseline Configurations setup for MR Approval Rules and Protected Branch Settings](/handbook/security/gitlab_projects_baseline_requirements/)
1. Projects should have [`Users can request access` setting disabled](https://docs.example_company.com/ee/user/project/members/index.html#prevent-users-from-requesting-access-to-a-project) to discourage granting accidental external access.
1. If needed, make sure to [set up a default CI/CD configuration](#cicd-configuration).
1. If your project contains code that is distributed with Example Company or is executed in production, set up [security jobs](https://example_company.com/help/user/application_security/security_dashboard/index#example_company-security-dashboard) for your project and add your project to the AppSec team's [triage rotation](/handbook/security/index.html#triage-rotation). The AppSec will triage security findings from the Security Dashboard and create issues for vulnerabilities.
1. If the project is part of work that is shipped to customers, add it to [projects_part_of_product.csv](https://example_company.com/example_company-data/analytics/blob/master/transform%2Fsnowflake-dbt%2Fdata%2Fprojects_part_of_product.csv) by opening an MR to that file or following the [process outlined by Engineering Productivity](/handbook/product/groups/product-analysis/engineering/dashboards/#updating-the-list-of-projects).
1. If the repository is public, set up a [security mirror](https://example_company.com/example_company-org/release/docs/blob/master/general/security/mirrors.md).
   This is necessary to address security vulnerabilities without disclosing them before they are fixed.

When changing the settings in an existing repository, it's important to keep [communication](/handbook/engineering/#communication) in mind. In addition to discussing the change in an issue and announcing it in relevant chat channels (e.g., `#development`), consider announcing the change in the [Engineering Week-in-Review document](/handbook/engineering/#communication). This is particularly important for changes to the [Example Company](https://example_company.com/example_company-org/example_company) repository.

### CI/CD configuration

Following is the default `.example_company-ci.yml` config that all projects under the `example_company-org` and `example_company-com` groups should use:

``` yaml
include:
  - template: 'Workflows/MergeRequest-Pipelines.example_company-ci.yml'

default:
  tags:
    - example_company-org
```

Or if the project needs to support stable/security branches, use the following instead:

```yaml
workflow:
  rules:
    # For merge requests, create a pipeline.
    - if: '$CI_MERGE_REQUEST_IID'
    # For `master` branch, create a pipeline (this includes on schedules, pushes, merges, etc.).
    - if: '$CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH'
    # For tags, create a pipeline.
    - if: '$CI_COMMIT_TAG'
    # For stable, and security branches, create a pipeline.
    - if: '$CI_COMMIT_BRANCH =~ /^[\d-]+-stable(-ee)?$/'
    - if: '$CI_COMMIT_BRANCH =~ /^security\//'

default:
  tags:
    - example_company-org
```

This:

1. Includes a [`workflow`](https://docs.example_company.com/ee/ci/yaml/#workflowrules-templates) to create pipelines for MR, `master`, and tags only.
1. Defines the `example_company-org` tag to be used by default which corresponds to cost-optimized runners, with no Docker support. Jobs that need Docker support would use the `example_company-org-docker` tag.

If a job requires the usage of Docker, it needs to be defined only in the context of the specific job with the `example_company-org-docker` tag:

``` yaml
sast:
  tags:
    - example_company-org-docker
```

If a job requires the usage of Windows, SaaS runners on Windows should be used. For the exact configuration please check the [SaaS runner on Windows documentation](https://docs.example_company.com/ee/ci/runners/saas/windows_saas_runner.html#machine-types-available-for-windows).

### Publishing a Project

To publish a project to a package repository, please follow [these directions](/handbook/engineering/developer-onboarding/#ruby-gems).
