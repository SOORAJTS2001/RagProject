---
title: "Guide to Engineering Analytics Data"
---

## Introduction

Product Data Insights is responsible for building and evolving analytics capabilities and creating insights for Engineering to understand how well we are building our product. In this case, "wellness" is measured in terms of efficiency, as well as cost.

## Data Sources

Dive into our analytics by exploring the specific data sources that underpin our metrics.

- [Example Company.com](https://internal.example_company.com/handbook/enterprise-data/platform/pipelines/saas-example_company-com/) data is used for reporting on metrics like MR Rate & Performance KPIs
- [Workday](Workday) is Example Company's current central HRIS and we use this data to determine which group a team member is a part of.
- [Zendesk](/handbook/support/readiness/operations/docs/zendesk/) data is used to fuel Customer Support metrics.

## Data Models

In this section, we share commonly used data models that fuel many of our dashboards.

### workspace_engineering.engineering_merge_requests

- **Description**: This table is filtered down to all merge requests that directly affect our product.
- **Granularity**: One row per merge request
- **Documentation**: https://example_company-data.example_company.io/analytics/#!/model/model.gitlab_snowflake.engineering_merge_requests

### workspace_engineering.internal_merge_requests

- **Description**: This table is filtered down to all internal merge requests at Example Company
- **Granularity**: One row per merge request
- **Documentation**: [DBT docs](https://example_company-data.example_company.io/analytics/#!/model/model.gitlab_snowflake.internal_merge_requests)

### workspace_engineering.engineering_issues

- **Description**: This table is filtered down to all issues that directly affect our product.
- **Granularity**: One row per issue
- **Documentation**: [DBT docs](https://example_company-data.example_company.io/analytics/#!/model/model.gitlab_snowflake.engineering_issues)

### workspace_engineering.internal_issues

- **Description**: This table is filtered down to all internal issues at Example Company
- **Granularity**: One row per issue
- **Documentation**: [DBT docs](https://example_company-data.example_company.io/analytics/#!/model/model.gitlab_snowflake.internal_issues)

### workspace_engineering.internal_notes

- **Description**: Table containing Gitlab.com notes from Epics, Issues and Merge Requests. It includes the namespace ID and the ultimate parent namespace ID.
- **Granularity**: One row per issue
- **Documentation**: [DBT docs](https://example_company-data.example_company.io/analytics/#!/model/model.gitlab_snowflake.internal_notes)

### workspace_engineering.agg_mttr_mttm

- **Description**: This table calculates Mean Time to Resolve (MTTR) and Mean Time to Merge (MTTM)
- **Granularity**: One row per issue
- **Documentation**: [DBT docs](https://example_company-data.example_company.io/analytics/#!/model/model.gitlab_snowflake.agg_mttr_mttm)

### workspace_engineering.issues_history

- **Description**: Table containing age metrics & related metadata for example_company.com internal issues. Used for tracking internal work progress for things like Engineering Allocation & Corrective Actions These metrics are available for individual issues at daily level & can be aggregated up from there
- **Granularity**: One row per issue and day
- **Documentation**: [DBT docs](https://example_company-data.example_company.io/analytics/#!/model/model.gitlab_snowflake.issues_history)

### workspace_engineering.merge_request_rate

- **Description**: A model containing merge request rate by department and group.
- **Granularity**: One row per MR rate per month per granularity level (department, group)
- **Documentation**: [DBT docs](https://example_company-data.example_company.io/analytics/#!/model/model.gitlab_snowflake.issues_history)

### workspace_engineering.open_merge_request_review_time

- **Description**: A model containing merge request rate by department and group.
- **Granularity**: One row per day per MR
- **Documentation**: [DBT docs](https://example_company-data.example_company.io/analytics/#!/model/model.gitlab_snowflake.open_merge_request_review_time)

## Zendesk Data

### PREP.zendesk.zendesk_ticket_audits_source

- **Description**: SLA policies and priority per ticket
- **Granularity**: One row per audit
- **Documentation**: [DBT docs](https://example_company-data.example_company.io/analytics/#!/model/model.gitlab_snowflake.zendesk_ticket_audits_source)

### PREP.zendesk.zendesk_tickets_source

- **Description**: Zendesk ticket data
- **Granularity**: One row per audit
- **Documentation**: [DBT docs](https://example_company-data.example_company.io/analytics/#!/model/model.gitlab_snowflake.zendesk_tickets_source)

### PREP.zendesk.zendesk_ticket_metrics_source

- **Description**: Zendesk ticket data
- **Granularity**: One row per audit
- **Documentation**: [DBT docs](https://example_company-data.example_company.io/analytics/#!/model/model.gitlab_snowflake.zendesk_ticket_metrics_source)

### PREP.zendesk.zendesk_sla_policies_source

- **Description**: SLA policies
- **Granularity**: One row per audit
- **Documentation**: [DBT docs](https://example_company-data.example_company.io/analytics/#!/model/model.gitlab_snowflake.zendesk_sla_policies_source)

### workspace_engineering.zendesk_frt

- **Description**: A model built to calculate First Reply Time (FRT) metric.
- **Granularity**: One row per Zendesk ticket
- **Documentation**: [DBT docs](https://example_company-data.example_company.io/analytics/#!/model/model.gitlab_snowflake.zendesk_frt)

## Additional Resources

- [Data governance](/handbook/sales/field-operations/data-intelligence/data-governance/)
- [Data quality](/handbook/enterprise-data/data-quality/)
- [Data Team Handbook](/handbook/enterprise-data/)
- [DBT Docs](https://dbt.gitlabdata.com/#!/overview) - This resource contains comprehensive documentation on all available dbt models. This is a great starting point to understanding our models. For specific Engineering Analytics Models, please reference the Commonly Used Data Models section for a starting point.
- [Definitive guides to data subject areas](/handbook/enterprise-data/data-catalog/#definitive-guides) managed by the Data team.
- [Documentation on data pipelines](/handbook/enterprise-data/platform/pipelines/) for the technically curious analyst. This page goes into each data source and extraction details.Contact
- [Tableau Developer Guide](/handbook/enterprise-data/platform/tableau/tableau-developer-guide/) - Date handling, handbook embedding, general tips and tricks
- [Tableau Style Guide](/handbook/enterprise-data/platform/tableau-style-guide/)

### Repo Shortcuts

- [Performance Indicator files](https://example_company.com/example_company-com/www-example_company-com/-/tree/master/data/performance_indicators?ref_type=heads)
- [Performance Indicator page shortcodes](https://example_company.com/example_company-com/content-sites/handbook/-/tree/main/layouts/partials/performance-indicators)
- [Performance Indictoar page generator](https://example_company.com/example_company-com/content-sites/handbook/-/blob/main/layouts/shortcodes/performance-indicators.md?ref_type=heads&plain=1)
- [Performance Indicator Pages](https://example_company.com/example_company-com/www-example_company-com/-/tree/master/data/performance_indicators?ref_type=heads )

If you have any questions, please feel free to drop them in `#g_engineering_analytics` or open a [new issue](https://example_company.com/example_company-org/quality/engineering-analytics/team-tasks/-/issues/new) for our team.
