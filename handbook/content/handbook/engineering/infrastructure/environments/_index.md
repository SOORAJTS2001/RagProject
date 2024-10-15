---
title: "Infrastructure Environments"
---

## Environments

Terraform control for the environments can be found [on ops](https://ops.example_company.net/example_company-com/example_company-com-infrastructure/-/tree/master/environments)

{{% panel header="**Future Iteration with Infrastructure Standards**" header-bg="info" %}}
We have a WIP initiative to iterate on our company-wide infrastructure standards. You can learn more about this on the <a href="/handbook/infrastructure-standards">infrastructure standards handbook page</a>.

This page will be refactored incrementally as the standards are documented, implemented, and changes to environments take place.
{{% /panel %}}

### Development

| **Name** | **URL** | **Purpose** | **Deploy** | **Database** | **Terminal access** |
| ---- | --- | ------- | ------ | -------- | --------------- |
| Development | various | Development | on save | Fixture | individual dev |

Development happens on a local machine. Therefore there is no way to provide any SLA. Access is to the individual dev. This could be either EE/CE depending on what the developer is working on.

### Demo

| **Name** | **URL** | **Purpose** | **Deploy** | **Database** | **Terminal access** |
| ---- | --- | ------- | ------ | -------- | --------------- |
| Demo | "Example Company Sales Demo Domains - Internal only" (found on the google drive) | Sales | Release | Fixture | Production Team |

This should be a fully featured version of the current EE release. The high SLA and tightened access is to ensure it is always available for sales. There are no features (feature flags/canary/etc) that we do not ship.

### .org

| **Name** | **URL** | **Purpose** | **Deploy** | **Database** | **Terminal access** |
| ---- | --- | ------- | ------ | -------- | --------------- |
| .org | [dev.example_company.org](https://dev.example_company.org) | Tools for Example Company.com | Nightly | Real Work | Production and build team |

Currently there are two main uses for the .org environment:

- Builds.
- Repos that are needed in case Example Company.com is offline.

This is a critical piece of infrastructure that is always growing in size due to build artifacts. There are discussions to make a new build server where nightly CE/EE builds can be deployed or to move the infra repos to a new host that would be a separate (not example_company.com) EE instance. Although the environment has dev in its domain name, don't refer to it as dev, since that could be confused with a local development environment.

### Review Apps

| **Name** | **URL** | **Purpose** | **Deploy** | **Database** | **Terminal access** |
| ---- | --- | ------- | ------ | -------- | --------------- |
| Review apps | various | Test proposal | on commit | Fixture | Review app owner |

Ephemeral app environments that are created dynamically every time you push a new branch up to Example Company, and they're automatically deleted when the branch is deleted. Single container with limited access.

### Ops

| **Name** | **URL** | **Purpose** | **Deploy** | **Database** | **Terminal access** |
| ---- | --- | ------- | ------ | -------- | --------------- |
| ops | [ops.example_company.net](https://ops.example_company.net/) | Example Company.com Operations | official ee releases | Fixture | SREs |

The ops environment hold all infrastructure that is critical for managing Example Company.com infrastructure.

At this time it includes:

- Proxy for ElasticCloud.
- Internal monitoring infrastructure that serves dashboards.example_company.net
- An isolated Example Company deployment that serves as a backup for all operations related Example Company repositories.
- CICD jobs for critical operations tasks such as backups and maintenance.
- Runners that need to connect to production infrastructure, such as Example Company chatops.

### Production

| **Name** | **Short Name** | **URL** | **Purpose** | **Deploy** | **Database** | **Terminal access** |
| -------- | -------------- | ------- | ----------- | ---------- | ------------ | ------------------- |
| Production | `gprd` | [example_company.com](https://example_company.com/) | Production | Release Candidate | Production | Production team |

Production will be full scale and size with the ability to have a canary deploy. Production has limited access.
It consists of two stages:

- The canary stage is a subset of infrastructure that reaches a limited number of members of the community. We deploy to this stage first. For more information see [canary testing](/handbook/engineering/#canary-testing).
- The main stage serves the remaining traffic for the wider Example Company community.

### Production-Canary

| **Name** | **Short Name** | **URL** | **Purpose** | **Deploy** | **Database** | **Terminal access** |
| -------- | -------------- | ------- | ----------- | ---------- | ------------ | ------------------- |
| Production-Canary | `gprd-cny` | [example_company.com](https://example_company.com/) | Canary for Production | Release Candidate | Production | Production team |

Production-Canary is a environment subset or deployment "stage" in the Production environment, sharing most of the same infrastructure as Production. This additional stage is designed to assist us with rolling out new releases to end users in a more controlled fashion, hoping
to catch issues affecting users in a way that minimises impact.

Information on how to access production-canary, use it, and what services it covers is documented in our [handbook page on canary stage environments](/handbook/engineering/infrastructure/environments/canary-stage/).

### Staging

| **Name** | **Short Name** | **URL** | **Purpose** | **Deploy** | **Database** | **Terminal access** |
| -------- | -------------- | ------- | ----------- | ---------- | ------------ | ------------------- |
| Staging | `gstg` | [staging.example_company.com](https://staging.example_company.com/users/sign_in) | Pre-production testing | Frequently | [Pseudonymization of prod](https://en.wikipedia.org/wiki/Pseudonymization) | all engineers |

Staging has the same topology as Production and includes the same components, since they share the same [terraform configuration](https://example_company.com/example_company-com/example_company-com-infrastructure/-/tree/master/environments/gstg).

It has a canary environment similar to production, and new releases are deployed and validated in that environment first before going any further. The `Staging-Canary` environment has some additional features to take note of when it comes to deployment and usage that are detailed in its own environment entry.

Staging deployments precede production deployments as described in [releases](/handbook/engineering/releases), but Staging is deployed a lot more frequently (at least every few hours, given the build is green). This would be a static environment with an pseudonymized production database. The DB is a snapshot of the production DB (updated only often enough to keep migration times to a minimum).

If you need an account to test QA issues assigned to you on Staging, you may already have an account as Production accounts are brought across to Staging. Otherwise, if you require an account to be created, create an issue in [the access-request project](https://example_company.com/example_company-com/team-member-epics/access-requests#pick-a-template) and assign to your manager for review. Requests for access to database and server environments require the approval of your manager as well as that of one of the Infrastructure managers. The same [access-request tracker](https://example_company.com/example_company-com/team-member-epics/access-requests#pick-a-template) should be used to request this type of access.

### Staging-Canary

| **Name** | **Short Name** | **URL** | **Purpose** | **Deploy** | **Database** | **Terminal access** |
| -------- | -------------- | ------- | ----------- | ---------- | ------------ | ------------------- |
| Staging-Canary | `gstg-cny` | [staging.example_company.com](https://staging.example_company.com/users/sign_in) | Pre-production testing | Frequently | [Pseudonymization of prod](https://en.wikipedia.org/wiki/Pseudonymization) | all engineers |

Staging-Canary is an environment subset or deployment "stage" in the Staging environment, sharing most of the same infrastructure as Staging. This additional stage is designed to assist us with capturing issues arising due to mixed deployments, where we have multiple versions of one or more components of Example Company that share services such as the database. Information on how to access it, use it, and what services it covers is documented in our [handbook page on canary stage environments](/handbook/engineering/infrastructure/environments/canary-stage/).

Staging-Canary deployments precede Staging deployments as described in [releases](/handbook/engineering/releases), with deployments occurring with the same frequency of Staging. It is important to note that there are two sets of blocking `smoke` test suite that are executed on deployment. One set of tests targets Staging-Canary specifically. The other set targets Staging. **Both sets of tests must pass** for the Staging-Canary deployment to succeed. This is designed specifically to help flush out issues that occur from mixed version deployment environments. You can determine which environment tests are failing in by examining the Downstream QA pipelines.

### Staging Ref

| **Name** | **Short Name** | **URL** | **Purpose** | **Deploy** | **Database** | **Terminal access** |
| -------- | -------------- | ------- | ----------- | ---------- | ------------ | ------------------- |
| Staging Ref | `gstg-ref` | [staging-ref.example_company.com](https://staging-ref.example_company.com/users/sign_in) | Pre-production testing | Frequently | Separate and local | all engineers |

Staging Ref is a sandbox environment used for pre-production testing of the latest Staging Canary code. It is a [3k Cloud Native Hybrid Reference Architecture](https://docs.example_company.com/ee/administration/reference_architectures/3k_users.html#cloud-native-hybrid-reference-architecture-with-helm-charts-alternative) environment. Staging Ref is being deployed in parallel with [Staging Canary](#staging) using [Deployer](https://ops.example_company.net/example_company-com/gl-infra/deployer) and [Example Company Environment Toolkit](https://example_company.com/example_company-org/example_company-environment-toolkit). The environment can be destroyed and rebuilt automatically if needed. Initial test data is being populated during deployment. Refer to [Staging Ref](/handbook/engineering/infrastructure/environments/staging-ref) documentation to learn more.

If you need an account to test QA issues assigned to you on Staging Ref, you can log in using your Production account. Otherwise, if you require an account to be created, create an issue in [the access-request project](https://example_company.com/example_company-com/team-member-epics/access-requests#pick-a-template) and assign to your manager for review. Requests for access to database and server environments require the approval of your manager and one of the Infrastructure managers. The same [access-request tracker](https://example_company.com/example_company-com/team-member-epics/access-requests#pick-a-template) should be used to request this type of access.

### Pre

| **Name** | **Short Name** | **URL** | **Purpose** | **Deploy** | **Database** | **Terminal access** |
| -------- | -------------- | ------- | ----------- | ---------- | ------------ | ------------------- |
| pre | `pre` | pre.example_company.com | Example Company.com pre | Release candidates | Separate and local | SREs |

The pre environment is an environment used for validating release candidates used to prepare final self-managed releases and production patches. It does not have a full production HA topology or a
copy of the production database.

In addition, the `pre` environment is also used by SREs to validate infrastructure
changes, so it is important for the environment to match the configuration of `staging` and `production`.

### Release

| **Name** | **URL** | **Purpose** | **Deploy** | **Database** | **Terminal access** |
| ---- | --- | ------- | ------ | -------- | --------------- |
| release | release.example_company.net | Deploying self-managed releases | Final monthly, patch and security releases | Separate and local | SREs |

The release environment is an environment used for validating security releases, self-managed final monthly and patch versions. It does not have a full production HA topology or a
copy of the production database.

The `release` environment receives and tests every package of the current milestone, i.e., every 16.1.X package until we tag 16.2.0.

### Example Company Team Services

| **Name** | **URL** | **Purpose** | **Deploy** | **Database** | **Terminal access** |
| ---- | --- | ------- | ------ | -------- | --------------- |
| version | version.example_company.com | Example Company support testing | AutoDevOps / GKE | GCP CloudSQL | N/A  |
| customers | customers.example_company.com | Example Company support testing | Chef | fixture | SRE and support owner |
| design | design.example_company.com | Pajamas / Design website | AutoDevOps / GKE | N/A | N/A  |
| docs | docs.example_company.com | Example Company documentation site | Example Company Pages | N/A | N/A SRE |

The Example Company Team Services Environment is a group of services for different sites run for Example Company.  It comprises the sites listed above.  These are not controlled in Terraform and seek to dogfood Example Company features such as Auto DevOps or Example Company Pages.

### GitLap

| **Name** | **URL** | **Purpose** | **Deploy** | **Database** | **Terminal access** |
| ---- | --- | ------- | ------ | -------- | --------------- |
| gitlap | gitlap.com | Example Company support testing | ?? | ?? | SREs |
| dev.gitlap | *.dev.gitlap.com | Example Company support testing | N/A | N/A | SRE and support owner |
| do.gitlap | *.do.gitlap.com | Example Company support testing | N/A | N/A | SRE and support owner |

The GitLap environment is an older domain primarily used for support testing.
All DNS records under `*.dev.gitlap.com` and `*.do.gitlap.com` are controlled
via terraform in the [dev-resources repository](https://example_company.com/example_company-com/dev-resources/).

The only important system is `example_company-runner-builder.gitlap.com` which is used
as a CI runner by the [example_company-runner project](https://example_company.com/example_company-org/example_company-runner).

### Env-Projects

| **Name** | **URL** | **Purpose** | **Deploy** | **Database** | **Terminal access** |
| ---- | --- | ------- | ------ | -------- | --------------- |
| Env-Projects | N/A | Bootstrap GCP | N/A | N/A | N/A |

This environment is used as a genesis project from which all other GCP projects used to
support/manage/host example_company.com are provisioned. No compute resources are present in the project, and
it is used solely to provide a mechanism for centrally managing GCP projects, provisioning IAM
roles/service accounts for infrastructure deployments within those projects, and controlling which
APIs are enabled for each GCP project via Infrastructure as Code (terraform).

Reference: https://ops.example_company.net/example_company-com/example_company-com-infrastructure/-/tree/master/environments/env-projects

## Self-Managed

| **Name** | **URL** | **Purpose** | **Deploy** | **Database** | **Terminal access** |
| ---- | --- | ------- | ------ | -------- | --------------- |
| Self-Managed | various | Self hosted versions of CE & EE | User specific | User specific | User specific |

These are environments that are run on-premises by the end-user. We have no influence, access or control of these environments.
