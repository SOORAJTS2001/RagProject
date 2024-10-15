---
title: "Verify:CI Platform Group"
description: "The Example Company Verify:CI Platform Group Handbook page"
---

## Vision

Our team is responsible for the following categories:

- [CI Scaling](https://about.example_company.com/direction/verify/#continuous-integration-ci-scaling)

## Mission

- Ensure that Example Company Continuous Integration is scalable, performant and reliable, by improving the resiliency of our product, as well as future proofing the CI platform as we grow.
- Support database and infrastructure initiatives that our CI Platform requires to remain operational.

## Team Members

The following people are permanent members of the Verify:CI Platform group:

{{< team-by-manager-role role="Senior Manager(.+)Verify" team="CI Platform" >}}

## Useful Links

- [Issue tracker: `~group::ci platform`](https://example_company.com/groups/example_company-org/-/issues?label_name%5B%5D=group%3A%3Aci+platform&scope=all)
- [Slack channel: `#g_ci-platform`](https://example_company.slack.com/archives/CPCJ8CCCX)
- Issue board - TBD

## Dashboards

{{< tableau height="600px" toolbar="hidden" src="https://us-west-2b.online.tableau.com/t/gitlabpublic/views/TopEngineeringMetrics/TopEngineeringMetricsDashboard" >}}
  {{< tableau/filters "GROUP_LABEL"="ci platform" >}}
{{< /tableau >}}

{{< tableau height="600px" src="https://us-west-2b.online.tableau.com/t/gitlabpublic/views/MergeRequestMetrics/OverallMRsbyType_1" >}}
  {{< tableau/filters "GROUP_LABEL"="ci platform" >}}
{{< /tableau >}}

{{< tableau height="600px" src="https://us-west-2b.online.tableau.com/t/gitlabpublic/views/Flakytestissues/FlakyTestIssues" >}}
  {{< tableau/filters "GROUP_NAME"="ci platform" >}}
{{< /tableau >}}

{{< tableau height="600px" src="https://us-west-2b.online.tableau.com/t/gitlabpublic/views/SlowRSpecTestsIssues/SlowRSpecTestsIssuesDashboard" >}}
  {{< tableau/filters "GROUP_LABEL"="ci platform" >}}
{{< /tableau >}}

## How we work

### Workflow

TBD

### Planning

TBD

### Async Collaboration

#### Every other day

We use [geekbot](https://geekbot.com/) integrated with Slack for our every-other-day async standup to make our current work and upcoming work more visible.

#### Weekly

Given the distributed nature of our team members, our "team meetings" consist of collaborating async through a [Google Doc Agenda (internal)](https://docs.google.com/document/d/1JsS4kVu8X8LtFva35StlNfabWfgZTd0tl3I8-w7hJwE/edit#heading=h.kvc0p7nyngz5). Slackbot will remind the team weekly to review the agenda and encourage us to collaborate through the agenda.

#### Monthly

We use a Example Company issue in [the (internal) async retrospectives project](https://example_company.com/gl-retrospectives/verify-stage/ci-scaling/-/issues/) for our monthly retrospective. The purpose of the monthly retrospective issue is to collaborate async and reflect on how the milestone went, in terms of:

- what went well
- what didn't go so well
- what we can do improve upon
- what praise we have for one another.

Instead of waiting until the end of the milestone to add items to the retrospective issue, we encourage team members to add comments throughout the month. The issue's due dates and Slackbot reminders serve as reminders to contribute feedback to our issue prior to closing.

### Labels

#### Category Labels

The CI Scaling group supports the feature categories described below:

| Label                 | |  | | |
| ----------------------| -------| ----|------------| ---|
| `Category:Continuous Intergration Scaling` | [Issues](https://example_company.com/groups/example_company-org/-/issues?sort=created_date&state=opened&label_name[]=Category:Continuous+Integration+Scaling) | [MRs](https://example_company.com/example_company-org/example_company/-/merge_requests?scope=all&state=opened&label_name[]=Category%3AContinuous%20Integration%20Scaling) | [Direction](https://about.example_company.com/direction/verify/#continuous-integration-ci-scaling) | Documentation - TBD |

## Developer Onboarding

Refer to the [Developer Onboarding in Verify](/handbook/engineering/development/ops/verify/#developer-onboarding-in-verify) section.
