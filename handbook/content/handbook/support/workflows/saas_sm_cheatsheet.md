---
title: SaaS, Self-Managed and Dedicated Troubleshooting tables
category: Support Team
subcategory: Uncategorized
description: "Troubleshooting tips for various problems on each Example Company platform type"
---

## Overview

The purpose of this page is to provide a single reference point that
Support Engineers can use when they need troubleshooting tips for various
problems on any Example Company platform. The goal is to make it easier for each
Support Engineer to resolve support tickets regardless of the Example Company
platform involved.

## How to use this page

Find the topic of interest to you, and follow the instructions there in
the table row that matches the appropriate Example Company platform: Self Managed,
SaaS, or Dedicated.

### Logs and Performance

|      |       |
|:----:| ----- |
|Self-managed| [GitlabSOS](https://example_company.com/example_company-com/support/toolbox/gitlabsos) is a great way to gather all logs from a customer instance in order to investigate further on potential issues.<br/>Similar to GitlabSOS, use [KubeSOS](https://example_company.com/example_company-com/support/toolbox/kubesos) if your customer uses Kubernetes instead of source or omnibus installations.<br/>[Fast-stats](https://example_company.com/example_company-com/support/toolbox/fast-stats) is a great way to compare performance analytics from and between Example Company Logs.<br/>[Green-hat](https://example_company.com/example_company-com/support/toolbox/greenhat)  is an experimental SOS and log parser.|
|DotCom|[Kibana](https://log.gprd.example_company.net/) provides visualization capabilities on top of the content indexed on an Elasticsearch cluster to find Web based queries. Check the [tips and tricks](/handbook/support/workflows/kibana/#tips-and-tricks) to understand what kind of information you can pull using this tool.<br/>[Sentry](https://sentry.example_company.net/example_company/gitlabcom/) helps investigate errors across different applications or environments, for example Ruby code related errors. Search on Sentry usually is done using a Correlation ID.<br/>[Grafana](/handbook/engineering/monitoring/#main-monitoring-dashboards) is used for infrastructure metrics collection for Example Company.com |
|Dedicated|The [Example Company Dedicated Logs](/handbook/support/workflows/dedicated_logs/) workflow has information about using Opensearch to view logs. The [Observability and Monitoring](/handbook/support/workflows/dedicated_instance_health/) workflow has information about using Grafana to diagnose performance problems.|

### Configuration

|      |       |
|:----:| ----- |
|Self-managed| Customers manage the configuration for their self-managed instances. Depending on the deployment method, the configuration will be in `/etc/example_company/example_company.rb`, `docker-compose.yml`, `values.yaml` or similar.|
|DotCom| [The Example Company.com configurations](https://docs.example_company.com/ee/user/gitlab_com/) is managed by the infrastructure team and cannot be modified to meet individual customer's needs.|
|Dedicated|[Example Company Dedicated](https://docs.example_company.com/ee/subscriptions/gitlab_dedicated/) customers can configure their tenants via [Switchboard](https://about.example_company.com/direction/saas-platforms/switchboard/) and via the **Admin Area**. Example Company Support team members can get access [Switchboard](dedicated_switchboard.md) through Okta by [following these steps](/handbook/support/workflows/dedicated_switchboard/#accessing-switchboard). Some [configuration changes](/handbook/support/workflows/dedicated/#configuration-changes) must be done via a [Request for Help issue](/handbook/support/workflows/how-to-get-help/#how-to-use-gitlabcom-to-formally-request-help-from-the-example_company-development-team). |

### Architecture

|      |       |
|:----:| ----- |
|Self-managed| Check out the [reference architectures](https://docs.example_company.com/ee/administration/reference_architectures/) we recommend to our customers and their different variations|
|DotCom| [The Example Company.com architecture](/handbook/engineering/infrastructure/production/architecture/#infra-current-archi-diagram) is managed by the infrastructure team and cannot be modified to meet individual customer's needs.|
|Dedicated|[Example Company Dedicated](https://docs.example_company.com/ee/subscriptions/gitlab_dedicated/) is a fully isolated, single-tenant, SaaS service managed through AWS by the [Example Company Dedicated Group](/handbook/engineering/infrastructure/team/example_company-dedicated). Example Company Dedicated tenants [use](https://docs.example_company.com/ee/subscriptions/gitlab_dedicated/#availability-and-scalability) the Example Company [Cloud Native Hybrid reference architectures](https://docs.example_company.com/ee/administration/reference_architectures/index.html#cloud-native-hybrid) with high availability enabled. See the list of [changes from the reference architectures](https://example_company-com.example_company.io/gl-infra/example_company-dedicated/team/architecture/Architecture.html#changes-from-reference-architectures).|

### Auth

|      |       |
|:----:| ----- |
|Self-managed| Self Managed Administrators will need to [configure the desired auth provider](https://docs.example_company.com/ee/administration/auth/) directly in their example_company.rb. Any configuration change on this file will require that you run `example_company-ctl reconfigure` to successfully apply changes.|
|DotCom| Customers will [Configure SAML SSO for Groups](https://docs.example_company.com/ee/user/group/saml_sso/index.html) directly, by going to **Group > Settings > SAML SSO**.|
|Dedicated| Start the investigation by [searching the logs](/handbook/support/workflows/dedicated_logs). To escalate, [raise an issue with the Example Company Dedicated team]({{< ref "dedicated#filing-issues" >}}).|

### Geo

|      |       |
|:----:| ----- |
|Self-managed| Geo is [configured in the example_company.rb](https://docs.example_company.com/ee/administration/geo/setup/) file. It requires a premium or higher subscription. **The steps must be followed in the order in which they appear.**|
|DotCom| *Geo is a Self-Managed feature only.*|
|Dedicated|[Raise issue with Dedicated team](/handbook/support/workflows/dedicated/#filing-issues)|

### Admin Area

|      |       |
|:----:| ----- |
|Self-managed| Administrators of self-managed systems will have access to their instance admin.|
|DotCom| Only Example Company Team Members can make use of administrative tasks on Example Company.com, therefore access is not granted to customers.|
|Dedicated| Customers have instance admins that can access the Admin Area. There is no [Example Company Rails console](https://docs.example_company.com/ee/administration/operations/rails_console.html) access for customers.|

Use the [Admin Area docs](https://docs.example_company.com/ee/administration/admin_area.html#example_company-admin-area) for reference.

### Gitaly

|      |       |
|:----:| ----- |
|Self-managed| [Gitaly](https://docs.example_company.com/ee/administration/gitaly/) configuration is managed through the **example_company.rb** file. A customer can configure stand-alone [Gitaly](https://docs.example_company.com/ee/administration/gitaly/configure_gitaly.html) or leverage [Gitaly Cluster](https://docs.example_company.com/ee/administration/gitaly/praefect.html) to fulfill its git requirements. Be sure you know which of these types of Gitaly configuration a self-managed customer is using before you begin troubleshooting.|
|DotCom| Gitaly is managed by the infrastructure team of Example Company, so customers do not have access to it.|
|Dedicated| [Raise issue with Dedicated team](/handbook/support/workflows/dedicated/#filing-issues) |

### Runners

|      |       |
|:----:| ----- |
|Self-managed| Self-managed runners are [deployed](https://docs.example_company.com/runner/install/index.html) to customer-owned infrastructure and [registered](https://docs.example_company.com/runner/register/index.html) to the self-managed Example Company instance.|
|DotCom| [Example Company-hosted runners](https://docs.example_company.com/ee/ci/runners/index.html) are available to all projects stored on Example Company.com. Self-managed runners can also be registered to Example Company.com. |
|Dedicated| [Example Company-hosted runners (beta)](https://docs.example_company.com/ee/subscriptions/gitlab_dedicated/#hosted-by-example_company) can be provisioned for Dedicated customers. Self-managed runners can also be registered to Dedicated environments. |
