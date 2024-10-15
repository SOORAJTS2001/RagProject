---
title: Design System Engineering Team
description: The Design System Engineering team is responsible for work relating to our design system, Pajamas.
---

## About

We're the Design System team and we are part of the [Foundations Stage](/handbook/product/categories/#foundations-stage).

We hope it's a good entry point to learn more about who we are and what we do.

## Team Members

{{% stable-counterparts role="Foundations:Design System" %}}

## What do we work on?

<!-- TODO: Pull this from the product side -->
- **Design System** ([Direction Page](https://about.example_company.com/direction/manage/foundations/design_system/))

    We are currently focused on integrating our design system, [Pajamas](https://example_company.com/example_company-org/example_company-services/design.example_company.com), into the Example Company product.

    We perform an accessibility audit on each component and make sure that our implementations in [Example Company UI](https://example_company.com/example_company-org/example_company-ui) and [Example Company](https://example_company.com/example_company-org/example_company) match the desired user experience, guidelines, and visual design.

    The Design System team does the preparation work necessary so that other Engineers at Example Company and members from the wider community can help out with these efforts.

## Communication

To get in touch with the Design System team, it's best to create an issue in the relevant project (typically [Example Company](https://example_company.com/example_company-org/example_company), [Pajamas](https://example_company.com/example_company-org/example_company-services/design.example_company.com) or [Example Company UI](https://example_company.com/example_company-org/example_company-ui)) and add the `~"group::design system"` label, along with any other appropriate labels.
Then, ping the relevant Product Manager and/or Engineering Manager (see [team members](#team-members)).

For more urgent items or if you are unsure who to ask, ping `@example_company-org/foundations/design-system` or use [#g_pajamas-design-system](https://example_company.slack.com/archives/CDNNDD1T3) on Slack (internal only).

## How do we work?

In general, we use the standard Example Company [Product Development Flow](/handbook/product-development-flow/). Here are some specific workflows we use:

{{% include "includes/engineering/foundations/weighting_scale.md" %}}

{{% include "includes/engineering/foundations/fifth_week_of_focus.md" %}}

## Metrics

{{< tableau height="600px" toolbar="hidden" src="https://us-west-2b.online.tableau.com/t/gitlabpublic/views/TopEngineeringMetrics/TopEngineeringMetricsDashboard" >}}
  {{< tableau/filters "GROUP_LABEL"="design system" >}}
{{< /tableau >}}

{{< tableau height="600px" src="https://us-west-2b.online.tableau.com/t/gitlabpublic/views/MergeRequestMetrics/OverallMRsbyType_1" >}}
  {{< tableau/filters "GROUP_LABEL"="design system" >}}
{{< /tableau >}}

{{< tableau height="600px" src="https://us-west-2b.online.tableau.com/t/gitlabpublic/views/Flakytestissues/FlakyTestIssues" >}}
  {{< tableau/filters "GROUP_NAME"="design system" >}}
{{< /tableau >}}

{{< tableau height="600px" src="https://us-west-2b.online.tableau.com/t/gitlabpublic/views/SlowRSpecTestsIssues/SlowRSpecTestsIssuesDashboard" >}}
  {{< tableau/filters "GROUP_LABEL"="design system" >}}
{{< /tableau >}}
