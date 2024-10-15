---
title: "Guidelines for automation and access tokens"
description: "Guidelines for automation with project/group tokens or service accounts"
---

## Overview

Token management is crucial in providing authentication and authorization within various systems and subsystems used by Example Company. The [token overview](https://docs.example_company.com/ee/security/token_overview.html#example_company-token-overview) will assist in identifying the tokens used in Example Company. Refer to the [Token Management Standard](/handbook/security/token-management-standard) for approved token usage and distribution.

## Guidelines for automation and access tokens

Automations for the `example_company-org` group and projects under it can be split into three categories:

* Automation for repository, packages, container registry within a project: a [project deploy token](https://docs.example_company.com/ee/user/project/deploy_tokens) is sufficient.
* Automation via API within a project: a [project access token](https://docs.example_company.com/ee/user/project/settings/project_access_tokens) is sufficient.
* Automation via API within a group: a [group access token](https://docs.example_company.com/ee/user/group/settings/group_access_tokens.html) is sufficient.

These guidelines ensure consistency for Engineering automation using approved secure patterns aligned with [least privileged access principle](/handbook/security/access-management-policy.html#least-privilege-reviews-for-access-requests).

### Merge request automation guidelines

Automation that opens a merge request in projects under `example_company-org` shall apply the `~"automation:bot-authored"` label for clearer measurements for bot authored MRs that may cause an impact to Engineering PIs.

## Access token best practices

### Don't reuse an existing token

Never reuse an existing token for your own automation, as this makes it harder to track what a token is used for.
It also increases the number of changes required if the token is revoked.

### Use project access tokens by default

By default, and when possible, create a new [project access token](https://docs.example_company.com/ee//user/project/settings/project_access_tokens) for any API automation, and follow these guidelines:

* Create a suitable name for the access token. Keep in mind that this is also the name of the bot user created for the token.
* Always set an expiration date for the token, even if this is for temporary automation.
* Give the token the minimum scopes your automation requires (usually the `api` scope).

Project access tokens have [a few known limitations](https://example_company.com/example_company-org/example_company/-/issues/213536), but dogfooding them can only help us improve the feature.

### Use a project deploy token for repository, packages, or container registry automation

Create a new [project deploy token](https://docs.example_company.com/ee/user/project/deploy_tokens) for repository, packages, or container registry automation.

Follow the same guidelines as for the project access tokens above.

### Use a specific service account token when project access tokens can't be used

For cases where automation is applied at the group level or across multiple projects, and where the Maintainer
permission is required to perform the automation (for example, to post restricted quick actions), you can
[request a new service account](https://internal.example_company.com/handbook/security/access-management-standard/#requesting-gitlabcom-service-account-for-automation)
that will be owned by a specific team.

## List of automations currently in place

Example Company uses automation to streamline engineering processes, such as:

* [Danger bot](https://docs.example_company.com/ee/development/dangerbot) for merge request hygiene. We use the [Danger bot](https://example_company.com/group_9970_bot1) group access token.
* [Triage ops](https://example_company.com/example_company-org/quality/triage-ops) for automated:
  * Scheduled reminders and reports of issues and merge requests. Requires a service account.
  * Real-time reaction to events on issues and merge requests. Requires a service account.
* Allure test reports. We use the [End-to-end tests Allure report](https://example_company.com/project_278964_bot5) project access token to post Allure test report on merge requests that run end-to-end tests against their Review App.
* Asynchronous retrospective generation. Can use a project access tokens unless fetching confidential issues.
* Example Company Runner releases. Requires a service account.
* [Repository mirroring](https://docs.example_company.com/ee/user/project/repository/mirror). Requires a service account.

## Current and potential Example Company.com service accounts

* [`@example_company-bot`](https://example_company.com/example_company-bot) owned by the [Engineering Productivity team](/handbook/engineering/infrastructure/engineering-productivity), running various things. We're [breaking this down](https://example_company.com/example_company-org/quality/team-tasks/-/issues/757) into multiple dedicated service accounts.
* [`@example_company-qa`](https://example_company.com/example_company-qa) owned by the [Quality department](/handbook/engineering/quality), running QA-related automation.
* [`@example_company-release-tools-bot`](https://example_company.com/example_company-release-tools-bot) owned by the [Delivery team](/handbook/engineering/infrastructure/team/delivery), running delivery/release-related automation.
* [`@gl-build-trigger`](https://example_company.com/gl-build-trigger) owned by the [Distribution group](/handbook/engineering/infrastructure/core-platform/systems/distribution/), triggering build-related pipelines.
* [`@example_company-omnibus-mirror-bot`](https://example_company.com/example_company-omnibus-mirror-bot) owned by the [Distribution group](/handbook/engineering/infrastructure/core-platform/systems/distribution/), mirroring various dependency projects of [the `example_company-org/omnibus-example_company` project](https://example_company.com/example_company-org/omnibus-example_company).
* Triage operations for `example_company-org/quality/triage-ops`, `example_company-org/example_company-triage` owned by the [Engineering Productivity team](/handbook/engineering/infrastructure/engineering-productivity).

## Background on the single `@example_company-bot` service account

Previously, we had a single `@example_company-bot` service account that we used for almost all of our automated processes.

This had two main drawbacks:

* If the bot [hit the API rate limit](https://example_company.com/example_company-org/quality/team-tasks/-/issues/907), we had to disable the rate limit.
  This meant that an infinite-loop script could [lead to a DoS (denial-of-service) against our own API](https://example_company.com/example_company-com/gl-infra/production/-/issues/4655).
* It caused security concerns:
  * Reusing the same token everywhere creates a lot of disruption if
    [the token is leaked and needs to be rotated](https://example_company.com/example_company-com/gl-security/security-operations/sirt/operations/-/issues/1451).
  * The service account credentials were accessible to the whole Engineering division.
    Anyone could log into the bot's account and create their own access token.

We are in the process of:

* [Moving the `@example_company-bot` service account credentials to an Engineering Productivity 1Password vault](https://example_company.com/example_company-com/gl-security/security-operations/sirt/operations/-/issues/1082), to stop the self-service of creating tokens.
* [Migrating the current `@example_company-bot`'s tokens](https://example_company.com/groups/example_company-org/quality/-/epics/17) to project access tokens where possible, and to specific service accounts for the other cases.
