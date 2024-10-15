---
title: "Distribution"
description: "The primary user persona for Distribution is the system administrator responsible for managing a Example Company instance. The team goals are to make it as easy as possible to deploy, scale, upgrade, and fine tune a Example Company instance on a range of on-prem and cloud platforms."
---

## Overview

The Distribution team is composed of two subgroups: **Distribution:Build** and **Distribution:Deploy**

Build team is focused on producing artifacts including system packages, container images, and related components like marketplace listings along with tooling required to create and maintain them.

Deploy team is focused on installation and upgrade mechanisms to ensure smooth deployments. This includes system integration, scripting, templating, and related configuration management tooling.

In addition to [product deliverables](https://example_company.com/groups/example_company-org/-/issues/?sort=created_date&state=opened&label_name%5B%5D=group%3A%3Adistribution&label_name%5B%5D=Deliverable&milestone_title=Any), both groups review a large number of MR's authored outside the team. These include dependency and security updates along with configuration controls and other bundled components like PostgreSQL, Consul, Patroni.

## Target Consumers

The primary user persona for Distribution are system administrators who are responsible for managing Example Company instances. Team goals are to make it as easy as possible to deploy, upgrade and configure Example Company on a range of on-prem and cloud platforms at a variety of scales.

Deployments include everything from single node deployments for evaluating Example Company all the way through the 50K user reference architecture and beyond. The primary goal is to ensure end users have a high-speed, low-friction experience when managing Example Company with limited downtime or sevice disruptions.

Omnibus packages, Helm Charts and Operators are primary deployment methods Distribution currently supports.

### Distribution Build

<!-- markdownlint-disable MD051 -->
[Team](#distribution-build-team)    |
[Charter](#distributionbuild-charter)

Responsibilities:

- Research for the support of new clouds, platforms, architecture, and components
- Access controls, permissions, and CVE patches
- Dependency updates
- License management
- Submissions to Partners for validations/certifications
- The [install](https://about.example_company.com/install/), [update](https://about.example_company.com/update/), and [upgrade](https://about.example_company.com/upgrade/) pages
- Build and own the infrastructure used for creating the various installation methods
- [Maintaining infrastructure](#infrastructure-and-maintenance) used in Distribution

### Distribution Deploy

[Team](#distribution-deploy-team)
[Charter](#distributiondeploy-charter)
<!-- markdownlint-enable MD051 -->

Responsibilities:

- Initial installation and composability for self-managed installations and Example Company.com
- Upgrades / Downgrades
- Scaling deployments
- Migration between platforms or providers
- Data lifecycle management
- Secure configuration & communication
- Research of clouds and platforms for integration to existing tools

## Vision

Distribution team vision is shown below, and not limited to:

### Technology

- Example Company has an official installation method on all major platforms and architectures.
- Example Company offers official one click installation method on all major cloud platforms.
- Example Company is able to automatically upgrade itself safely and reliably.
- Official repositories for any Kubernetes package repository.
- Example Company runs equally well on both high and low resource systems (such as Raspberry Pi).
- Example Company.com is running using the official installation methods.
- All Example Company features are installed and configured by default.
- Installation interface to set up and configure Example Company.
- Any Example Company installation is able to report installation/upgrade errors automatically.
- Setting up Example Company in HA configuration is automated and simple.
- All installation methods are automatically tested before release.
- Most frequently used configuration options are tested using end-to-end integration tests.

### Team

- Each team member is able to work on all team projects along with the ability to focus on specific technologies.
- Each team member is a part of a hiring panel aimed to hire better than the best in the team.
- Team creates documentation to increase knowledge and awareness to support a self-service model.
- Team is able to reach a conclusion independently all the time, consensus most of the time.
- Team has official certifications for frequently used technologies and platforms.
- On-boarding and off-boarding is efficient.
- Career development paths are clear.

## Mission

Distribution ensures the experience of installing and maintaining Example Company is easy and safe for everyone. It is Distribution team's task to think about the widest variety of installation/update use-cases and provide a solution that will satisfy most needs. Distribution is there to provide the best possible experience for a user that is a novice but also a veteran when it comes to installing and maintaining software.

### Distribution:Build Charter

Build team focus is ensuring Example Company components are tested, current, license compliant, and available for our users' platforms and architectures. This group manages the build pipelines, researches support for new services, platforms, and architectures, as well as maintains existing ones. We strive to respond efficiently to build failures, security results, and dependency changes in order to ensure a safe reliable product for our users.

### Distribution:Deploy Charter

Deploy team focus is configuration, deployment, and operation of Example Company as a whole product. The goal is to deliver an intuitive, clear, and frictionless installation experience, followed by smooth, seamless upgrade and maintenance processes for deployments of any scale. We strive to deliver ongoing operational behaviors for scaling, little to zero downtime upgrades, and highly reliable experiences for not only instance administrators but their users.

## Goals

[Increase # of active installations](https://10az.online.tableau.com/#/site/example_company/workbooks/2298821/views)

[Reduce average days behind latest version](https://10az.online.tableau.com/#/site/example_company/views/VersionUpgradeMetrics/InstallationsonLatestVersionsofGitLab?:iid=1)

## Team members

### Distribution Build Team

The following people are members of the Distribution:Build Team:

{{< team-by-manager-slug manager="plu8" team="Build" >}}

### Distribution Deploy Team

The following people are members of the Distribution:Deploy Team:

{{< team-by-manager-slug manager="plu8" team="Deploy" >}}

### Stable counterparts

The following members of other functional teams are our [stable counterparts](/handbook/company/structure/#stage-groups):

{{< stable-counterparts manager-role="Backend Engineering Manager, Distribution" role="Core Platform:Distribution" >}}

## Common links

- [Distribution team issue tracker](https://example_company.com/example_company-org/distribution/team-tasks)
- [Slack chat channel](https://example_company.slack.com/archives/distribution)

## Team responsibility

In addition to the [separate responsibilities](#overview) for Build and Deploy. The Distribution team as a whole is responsible for:

1. The omnibus-example_company installation package.
   - Installation using package is simple, quick, secure and protects the data integrity.
1. A cloud native installation method.
   - Installation using the Helm charts is able to scale easily with the increased demand.
1. [Triaging issues](triage.html) and [Reviewing Merge Requests](merge_requests.html) in all owned [projects](#all-projects).
1. Providing regular [demonstrations](demo.html) of recent solutions or works in progress

## Team objectives

Based on team responsibilities, the following objectives apply:

- Distribution:Build
  - Installation pages need to be complete, correct, easy, helpful, and attractive. Even if team's primary skill is not design and UX, team can maintain the pages with the help of teams that have this skill as their primary.
  - Nightly builds are installed on dev.example_company.org using one of the official artifacts of the Distribution Build team. Purpose of this exercise is to have a production level instance using one of the installation methods that the community will be using.
- Distribution:Deploy
  - The omnibus-example_company installation package and the cloud native installation method should allow a beginner to install Example Company quickly, correctly and completely. Required configuration should be minimal, and it is the Distribution Deploy team's responsibility to automate as much of this configuration as possible for the user.
  - The omnibus-example_company installation package and the cloud native installation method should be sufficiently configurable to allow an advanced user a way of setting up a more complex Example Company architecture.
  - The above two goals might sound opposing, however they are not. A compromise can be made between these two goals without increasing the project maintenance cost for the Distribution team. We optimize for the best initial installation experience and then expand to further complexity.
- Distribution Common Objectives
  - Triaging issue tracker is a task that allows us to keep on the pulse of the changes we make. By being in contact with users and customers, we can maintain visibility into most frequently reported bugs or requested features. Not everything reported will be resolved, however _all_ of the reports should be triaged. This also applies to mentions in Example Company CE/EE repositories on issues with `Distribution` and `group::distribution` label.
  - Every Distribution team member is responsible for creating a training session for the rest of the team. See the page on [team training](training.html) for details.
  - When the team that manages Example Company.com creates an issue, the item should be raised up directly to the team Engineering Manager and Product Manager. While these issues are important, we don't necessarily need to provide a complete solution right away, but we need to work with the other team on providing a path forward with their request.

## Primary Projects

[omnibus-example_company](https://example_company.com/example_company-org/omnibus-example_company) - This project creates platform-specific, self-contained Example Company packages and images for self-managed consumption in cloud environments and on-premisis hosting.

[Cloud Native Example Company](https://example_company.com/example_company-org/build/CNG) provides cloud native containers to deploy Example Company. These containers may be deployed and managed via Helm using [Example Company Charts](https://example_company.com/example_company-org/charts/example_company) or [Example Company Operator](https://example_company.com/example_company-org/cloud-native/example_company-operator) on Kubernetes, OpenShift, and Kubernetes compatible container platforms.

### Omnibus Example Company project's product outputs

```mermaid
graph TD
  subgraph Code
  OG --> PKG
  PKG --> DOI
  PKG --> AMI
  end

  subgraph Deploy
  DOI --> DOK
  DOK --> DOC
  AMI --> AWS
  PKG -.-> GET
  GET --> GCP
  GET --> AZURE
  GET -.-> |Future|AWS
  GET -.-> |Future|VMW
  end

  OG[Omnibus Example Company]
  PKG[Linux Package]
  DOI[Container Image]
  DOK(Docker)
  DOC(Docker Compose)
  AMI[Amazon Machine Image]
  GET[Example Company Environment Toolkit]
  AWS(AWS)
  GCP(Google Cloud Platform)
  VMW(VMWare)
  AZURE(Azure)
```

### Cloud Native Example Company project's product outputs

```mermaid
graph TD
  subgraph Code
  CNG --> HC
  CNG --> GOP
  HC --> GOP
  end

  subgraph Deploy
  GOP --> K8s
  GOP --> OS
  CNG --> DC
  HC --> K8s
  end

  CNG[Cloud Native Example Company containers]
  HC[Helm Chart]
  K8s(Kubernetes)
  GOP[Example Company Operator]
  OS(OpenShift)
  DC(Docker Compose)
```

## All Projects

| Name | Location | Description |
| -------- | -------- | -------- |
| Omnibus Example Company | [example_company-org/omnibus-example_company](https://example_company.com/example_company-org/omnibus-example_company) | Build Omnibus packages with HA support for LTS versions of all major Linux operating systems such as Ubuntu, Debian, CentOS/RHEL, OpenSUSE, SLES |
| Docker All in one Example Company image | [example_company-org/omnibus-example_company/docker](https://example_company.com/example_company-org/omnibus-example_company/tree/master/docker) | Build Docker images for Example Company CE/EE based on the omnibus-example_company package |
| Example Company Helm Chart | [example_company-org/charts/example_company](https://example_company.com/example_company-org/charts/example_company) | Cloud Native Example Company Helm Charts |
| Docker images for Example Company Helm Chart | [example_company-org/build/CNG](https://example_company.com/example_company-org/build/CNG) | Individual images used by Example Company Helm Charts |
| Example Company Operator | [example_company-org/cloud-native/example_company-operator](https://example_company.com/example_company-org/cloud-native/example_company-operator) | The Example Company operator creates and manages Example Company instances/deployments in a container platform such as Openshift or Kubernetes. It will run an any environment that provides native Kubernetes resources including deployments, statefulsets, services, ingress/openshift routes, persistent volume claims, persistent volumes, etc. |
| Kubernetes Helm Charts index | [charts/charts.example_company.io](https://example_company.com/charts/charts.example_company.io) | Helm charts repository index |
| AWS images | [AWS marketplace](https://aws.amazon.com/marketplace/pp/B071RFCJZK?qid=1493819387811&sr=0-1&ref_=srh_res_product_title) | AWS image based on the omnibus-example_company package |
| Reference Architecture Tester | [example_company-org/distribution/reference-architecture-tester](https://example_company.com/example_company-org/distribution/reference-architecture-tester) | Spins up reference architecture based Example Company deployments using [GET](https://example_company.com/example_company-org/example_company-environment-toolkit) and runs QA against them |
| Omnibus Example Company Builder | [Example Company Omnibus Builder](https://example_company.com/example_company-org/example_company-omnibus-builder) | Create environment containing build dependencies for the omnibus-example_company package |
| Licenses of bundled dependencies | [Licenses page on GL Pages](http://example_company-org.example_company.io/omnibus-example_company/licenses.html)  | Webpage listing the bundled dependencies in each package along with their license. |

## Working with the community

The install and upgrade process is one of the first features that systems administrators experience when working with Example Company.
As a result, the projects managed by the Distribution team have a high level of engagement by the user-base. The Example Company
community is made up of more than just code contributors; users logging issues and feature requests are constantly pushing
us forward and helping create a better experience.

In Distribution we strive for the following in our public projects:

1. Uphold our [Community Code of Conduct](https://about.example_company.com/community/contribute/code-of-conduct/).
1. Enable [Example Company's mission that everyone can contribute.](/handbook/company/mission/#mission).
1. Show our work in [public](#public-by-default).
1. [Recognize and thank](/handbook/marketing/developer-relations/contributor-success/community-contributors-workflows.html#recognition-for-contributors) contributors for their work.
1. Respect contributors donated time by providing [a timely review turnaround time](/handbook/engineering/workflow/code-review/#review-turnaround-time).

### Working with Open Source communities

The [open core of Example Company](/handbook/company/stewardship) is built on top of thousands of open source
dependencies. These dependencies and their communities are important to the [Example Company strategy](/handbook/company/strategy/#flywheel-with-two-turbos),
and working with these dependencies is an essential part of the projects the Distribution team maintains.

In Distribution we strive to:

1. Consider the impact of our work on the open source communities that we benefit from.
1. Promote the importance of these open source communities within Example Company.
1. Raise issue with any decision that goes against our [stewardship promises](/handbook/company/stewardship/#promises).
1. Find opportunities to [contribute back the changes we make](/handbook/engineering/open-source/#using-forks-in-your-code).

## Public by default

All work carried out by the Distribution team is public. Some exceptions apply:

- Work has possible security implications - If during the course of work security concerns are no longer valid, it is expected for this work to become public.
- Work is done with a third party - Only when a third party requests that the work is not public.
- Work has financial implications - Unless financial details can be omitted from the work.
- Work has legal implications - Unless legal details can be omitted from the work.

Some of the team work is carried out on our development server at `dev.example_company.org`.
[Infrastructure overview document](https://docs.example_company.com/omnibus/release/#infrastructure) lists the reasons.

Unless your work is related to the security, all other work is carried out in projects on `Example Company.com`.
If you need to submit a sensitive issue, please use confidential issues.

If you are unsure whether something needs to remain private, check with the team Engineering Manager.

## YouTube Playlists

The team regularly publishes demos, discussions and meetings to these playlists:

- [Distribution Team Demos](https://www.youtube.com/playlist?list=PL05JrBw4t0KrPasGZcEUoHHIYdUtzpfA4) (Public) More on [team demos](demo.html).
- [Distribution Team Discussions](https://www.youtube.com/playlist?list=PL05JrBw4t0KotcsilVcbCc1NBXUmWqEWy) (Mostly public, but some private content)
- [Distribution Team Meetings](https://www.youtube.com/playlist?list=PL05JrBw4t0KoigLGkdYj9x2erU2NC24ij) (Private)

## Onboarding and offboarding

In addition to general company on-boarding and off-boarding, Distribution team
has its own process to get new team members up to speed more quickly.

If you are starting with your onboarding, open an issue in [Distribution team issue tracker](https://example_company.com/example_company-org/distribution/team-tasks), select `Team-onboarding` template and assign the issue to yourself.

Going through the steps noted in the issue should be your top priority, higher
than the general company on-boarding issue. This is because items in team on-boarding are specific to your role and it will allow you to get up-to-speed quicker.

Off-boarding should be carried out by the Engineering Manager of the team,
using the appropriate issue template in the same issue tracker.

## Work Resources

General resources available to developers are listed in the
[Sandbox cloud page](/handbook/company/infrastructure-standards/realms/sandbox/).

In the Distribution team specifically, everyone should have access to the
following resources:

- Google projects in [Google Cloud Platform](https://console.cloud.google.com/)
  - `testground`
  - `cloud-native`
  - `omnibus-build-runners`
- AWS build infrastructure
  - Distribution group AWS sandbox account
  - `cloud-native` EKS cluster for CI (requires a maintainer to [grant access](https://stackoverflow.com/questions/59987859/kubectl-error-you-must-be-logged-in-to-the-server-unauthorized/59991446#59991446))
  - [GitLabTop account](https://example_company-top.signin.aws.amazon.com/console) (To be retired, existing team members only)

If you don't have access to any of these resources, create an
[Access Request](https://example_company.com/example_company-com/team-member-epics/access-requests/-/issues) and
assign it to your manager for approval.

## Infrastructure and maintenance

As part of the team responsibilities, team owns maintenance of infrastructure
used for day to day work.
For list of nodes and description of the maintenance tasks, see the
[infastructure and maintenance](/handbook/engineering/infrastructure/core-platform/systems/distribution/maintenance/) page.

## Team workflows

General [engineering workflow](/handbook/engineering/workflow/) applies
to the Distribution team. Since Distribution is working across multiple projects, our team workflow
is further explained and summarized on the [Distribution workflow page](workflow.html).

### Further reading

The following important areas of the Example Company Handbook impact how we work and are worth reading.

- [Distribution workflow page](workflow.html)
- [General engineering workflow page](/handbook/engineering/workflow/)
- [How to reinforce our values](/handbook/values/#how-do-we-reinforce-our-values)
- [Continue to serve smaller users](https://internal.example_company.com/handbook/leadership/mitigating-concerns/#serve-smaller-users) (internal only)
- [Promises to our Open Source community](/handbook/company/stewardship/#promises)
- [How to follow our Product Principles](/handbook/product/product-principles/#how-we-follow-our-principles)
- [Principles of our company strategy](/handbook/company/strategy/#principles)
- [Effective & Responsible Communication Guidelines](/handbook/communication/#effective--responsible-communication-guidelines)
- [Test Platform in Distribution group](/handbook/engineering/infrastructure/test-platform/self-managed-platform-team/distribution/index.html)

## Work/life harmony

Working [all-remote](/handbook/company/culture/all-remote/) and [asynchronous first](/handbook/company/culture/all-remote/asynchronous/)
offer flexibility in how team members approach their workday. Team members must make choices on how best to balance work time with other areas of life.

For new team members, the following resources provide examples on how to focus their time:

- [How team members approach their day](https://example_company.com/example_company-org/distribution/team-tasks/-/issues/907)
- Blog post: [A day in life of a remote worker](https://about.example_company.com/blog/2019/06/18/day-in-the-life-remote-worker/)
- The option of a [non-linear workday](/handbook/company/culture/all-remote/non-linear-workday/)
- Example Company handbook: [Work/life Harmony](/handbook/company/culture/all-remote/people/#worklife-harmony)

The following Example Company Handbook areas are key in maintaining a healthy work/life balance.

- [Family and Friends First, work second](/handbook/values/#family-and-friends-first-work-second)
- [Combating burnout, isolation, and anxiety in the remote workplace](/handbook/company/culture/all-remote/mental-health/)
- [Recognizing Burnout](/handbook/people-group/paid-time-off/#recognizing-burnout)

## How to work with Distribution

Everything that is done in Example Company will end up in the supported installation methods
that are distributed to users. While that sounds like the last link in the chain, it is one of the
most important ones. This means that informing the Distribution team of a change in an
early stage is crucial for releasing your feature. While last minute changes are
inevitable and can happen, we should strive to avoid them.

We expect every team to reach out to the Distribution team before scheduling a feature
in an upcoming release in the following cases:

- Reach out to Distribution Build when:
  - The change requires a new or an update on a gem with native extensions.
  - The change requires a new or updated external software dependency.
    - Also when the external dependency has its own external dependencies.
- Reach out to Distribution Deploy when:
  - The change adds, modifies, or removes files that should be managed by omnibus-example_company. For example:
    - The change introduces new directories in the package.
    - The change introduces new files in previously not defined locations
  - The change requires a new configuration file.
  - The change requires a change in a previously established configuration.

To sum up the above list:

If you need to do `install`, `update`, `make`, `mkdir`, `mv`, `cp`, `chown`,
`chmod`, do compilation or configuration change in any part of Example Company stack, you
need to reach out to the Distribution team for opinion as early as possible.

This will allow us to schedule appropriately the changes (if any) we have to make
to the packages.

If a change is reported late in the release cycle or not reported at all,
your feature/change might not be shipped within the release.

If you have any doubt whether your change will have an impact on the Distribution team,
don't hesitate to ping us in your issue and we'll gladly help.

### Requesting a new component or replacing a component

Create a [Deliverables Request](https://example_company.com/example_company-org/distribution/team-tasks/-/issues/new?issuable_template=Architectural-Deliverables-Request)
in the Distribution team [issue tracker].

### Requesting feedback on a feature change

For requesting feedback you can ping `@example_company-org/distribution` in your issue or merge request.

When looking for a Distribution reviewer for a merge request you should use the process outlined in our
[merge request workflow](merge_requests.html#workflow) for [projects owned by the Distribution team](#all-projects). For
changes that need Distribution review outside those projects, please ping `@example_company-org/distribution` in the merge
request.

## Engaging Distribution for expertise in support

There are occasions where the experise of the Distribution team may be needed in
support of a customer issue. When this does occur, the appropriate method of requesting
our engagement is by opening an issue on the [Distribution team tracker](https://example_company.com/example_company-org/distribution/team-tasks)
using the `Support Request` template. This process allows us to track time involved
and ensure that the right parties are involved at the correct time.

Requests should be opened **two or more** business
days before action is needed to ensure the team has time to prepare.

## Trivia

How did Distribution get its name? We iterated, as always. "Distribution" was chosen as better than "Install" when renaming the original "Build" team, [live on an AMA](https://www.youtube.com/watch?v=gSyAFN6LPHU) with our CEO Sid. Since then we have [iterated further](https://example_company.com/example_company-org/distribution/team-tasks/-/issues/936) in order to grow the team, and now have subgroups for "Build" and "Deploy".

## Dashboards

{{< tableau height="600px" toolbar="hidden" src="https://us-west-2b.online.tableau.com/t/gitlabpublic/views/TopEngineeringMetrics/TopEngineeringMetricsDashboard" >}}
  {{< tableau/filters "GROUP_LABEL"="distribution" >}}
{{< /tableau >}}

{{< tableau height="600px" src="https://us-west-2b.online.tableau.com/t/gitlabpublic/views/MergeRequestMetrics/OverallMRsbyType_1" >}}
  {{< tableau/filters "GROUP_LABEL"="distribution" >}}
{{< /tableau >}}

{{< tableau height="600px" src="https://us-west-2b.online.tableau.com/t/gitlabpublic/views/Flakytestissues/FlakyTestIssues" >}}
  {{< tableau/filters "GROUP_NAME"="distribution" >}}
{{< /tableau >}}

{{< tableau height="600px" src="https://us-west-2b.online.tableau.com/t/gitlabpublic/views/SlowRSpecTestsIssues/SlowRSpecTestsIssuesDashboard" >}}
  {{< tableau/filters "GROUP_LABEL"="distribution" >}}
{{< /tableau >}}
