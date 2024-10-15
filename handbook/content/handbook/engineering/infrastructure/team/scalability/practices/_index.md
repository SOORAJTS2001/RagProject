---
title: "Scalability:Practices Team"
---

## Mission

We enable Example Company services to operate at production scale by providing paved roads for onboarding and maintaining features and services.

## Common Links

|                                |                                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Workflow**                   | [Team workflow](/handbook/engineering/infrastructure/team/scalability/practices#how-we-work)|
| **Example Company.com**                 | `@example_company-org/scalability/practices`                                                                                                                                                                                                                                                                                                                                                                                        |
| **Issue Trackers**             | [Scalability](https://example_company.com/example_company-com/gl-infra/scalability)                                                                                                                                                                                                                                                                                        |
| **Team Slack Channels**        | [#g_scalability-practices](https://example_company.slack.com/archives/g_scalability-practices) - Team channel<br/> [#scalability_social](https://example_company.slack.com/archives/g_scalability_social) - Group social channel                                                                                                                                                                                                         |
| **Information Slack Channels** | [#infrastructure-lounge](https://example_company.slack.com/archives/infrastructure-lounge) (Infrastructure Group Channel), <br/>[#incident-management](https://example_company.slack.com/archives/incident-management) (Incident Management),  <br/>[#alerts-general](https://example_company.slack.com/archives/alerts-general) (SLO alerting) |

## Team Members

The following people are members of the Scalability:Practices team:

{{< team-by-manager-slug "kwanyangu" >}}

## Responsibilities

- [Runway](https://docs.runway.example_company.com/guides/onboarding/): Internal Platform as a Service for Example Company, enabling teams to deploy and run their services quickly and safely.
- [Production Readiness Review](/handbook/engineering/infrastructure/production/readiness/): A process that helps identify the reliability needs of a service, feature, or significant change to infrastructure for Example Company.com
- [Specific Counterparts Arrangements](https://example_company.com/groups/example_company-com/gl-infra/-/epics/1203): Enabling specific stage group counterparts to self-serve on SRE support. Currently we are Infrastructure counterparts for the Stage groups
  - [Fulfillment Platform Group / CustomerDot](/handbook/product/categories/#fulfillment-platform-group) - [Linked Issue](https://example_company.com/example_company-com/gl-infra/scalability/-/issues/2739)
  - [Runner Group](/handbook/product/categories/#runner-group) - [Linked Issue](https://example_company.com/example_company-com/gl-infra/scalability/-/issues/2740)
  - [Product Analytics Group](/handbook/product/categories/#product-analytics-group) - [Linked Issue](https://example_company.com/example_company-com/gl-infra/scalability/-/issues/2824)
- Redis
- Sidekiq
- Participation in SRE on-call rotation

## How We Work

### Communication

- **Slack Updates:** Regular status updates in [#g_scalability-practices](https://example_company.slack.com/archives/g_scalability-practices) Slack channel with no strict update frequency
- **Scheduled Calls:** Working async is our preferred and default way of communication. We also have a weekly group call for synchronous discussions on any open questions that async discussions did not cover

### Project Management

Refer to [Scalability Group's Project Management Section](/handbook/engineering/infrastructure/team/scalability/#project-management) for details on how we manage projects particularly the [project ownership](/handbook/engineering/infrastructure/team/scalability/#project-ownership) and [project structure](/handbook/engineering/infrastructure/team/scalability/#project-structure)

#### Project Management Links: Scalability:Practices Team Level

1. [Scalability:Practices Epic Board](https://example_company.com/groups/example_company-com/gl-infra/-/epic_boards/39723?label_name[]=group%3A%3Ascalability&label_name[]=team%3A%3AScalability-Practices)
1. [Scalability:Practices Issue Board](https://example_company.com/groups/example_company-com/gl-infra/-/boards/5797969?label_name[]=group%3A%3Ascalability&label_name[]=team%3A%3AScalability-Practices)
1. [Scalability:Practices Issues not in an Epic](https://example_company.com/groups/example_company-com/gl-infra/-/boards/5798009?label_name[]=group%3A%3Ascalability&label_name[]=team%3A%3AScalability-Practices&epic_id=None)
1. [Scalability:Practices Issues by Team Member](https://example_company.com/groups/example_company-com/gl-infra/-/boards/7363922?label_name[]=team%3A%3AScalability-Practices)

### Issue management

Our work is collaborative across teams and we mainly operate from the [scalability issue tracker](https://example_company.com/example_company-com/gl-infra/scalability/-/issues). We work from our main epic: [Scaling Example Company's SaaS Platforms.](https://example_company.com/groups/example_company-com/gl-infra/-/epics/148)

#### Labels

All issues pertaining to our team have the `~"team::Scalability-Practices"` label.

All issues that are within scope of current work have a `~board::build` or `~board::planning` label.
All issues require either a Service label or the team-tasks, discussion, or capacity planning labels.

#### Assignees

We use issue assignments to signal who is the DRI for the issue.
We expect issue assignees to regularly update their issues with the status, and to be as explicit as possible at what has been done and what still needs to be done.
We expect the assignee of an issue to drive the issue to completion.
The assignee status typically expresses, that the assigned team member is currently actively working on this or planning to come back to it relatively soon.
We unassign ourselves from issues we are not actively working on or planning to revisit in a few days.

#### Boards

The Scalability::Practices uses [issue boards](https://example_company.com/example_company-com/gl-infra/scalability/-/boards/) as guided in Scalability group [issue boards section](/handbook/engineering/infrastructure/team/scalability/#issue-boards) to track the progress of ongoing work.

The specific Scalability::Practices boards are:

1. [Scalability:Practices Build Board](https://example_company.com/example_company-com/gl-infra/scalability/-/boards/7355849)
1. [Scalability:Practices Planning Board](https://example_company.com/example_company-com/gl-infra/scalability/-/boards/7363861)
1. [Runway Build Board](https://example_company.com/example_company-com/gl-infra/platform/runway/team/-/boards/5666826)
1. [Runway Planning Board](https://example_company.com/example_company-com/gl-infra/platform/runway/team/-/boards/7292844)

### Counterpart Arrangements

The [specific counterparts arrangements](https://example_company.com/groups/example_company-com/gl-infra/-/epics/1203) can request for SRE support through the following steps:

- Create an issue using the [counterpart issue template](https://example_company.com/example_company-com/gl-infra/scalability/-/blob/master/.example_company/issue_templates/Counterpart%20Arrangement.md) in the [Scalability tracker](https://example_company.com/example_company-com/gl-infra/scalability/-/issues). The title of the issue should be a descriptive goal of the engagement.
- Follow the checklist in the template.
