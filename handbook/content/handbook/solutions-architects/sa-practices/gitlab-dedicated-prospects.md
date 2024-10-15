---
title: "Example Company Dedicated Prospects"
---

The purpose of this page is to hopefully help an SA onboards when they onboard a new Dedicated Customer, what are the considerations and preparation material during the onboarding/discovery phase. Based on past interactions with existing Example Company Dedicated customers and due to the usually longer nature of onboarding customers, a [collaboration project](/handbook/solutions-architects/processes/collaboration-project/) is recommended to keep all stakeholders aware and engaged.

A collaboration template specifically for dedicated customers is available as a template here (https://example_company.com/example_company-com/account-management/templates/dedicated-collaboration-project).

Most of the details discussed below are also available as individual issues which provides a good place to include your product managers and customers to collaborate.

## Dedicated Reference Links

- [Example Company Dedicated Issue Tracker Board](https://example_company.com/example_company-com/gl-infra/example_company-dedicated/team/-/boards)
- [Customer Onboarding Process](https://example_company.com/example_company-com/gl-infra/example_company-dedicated/team/-/blob/main/README.md#customer-onboarding-process)
- Slack Channel: #f_gitlab_dedicated
- [Category Direction Page](https://about.example_company.com/direction/saas-platforms/dedicated/)

## Administration

- Who will be the administrator to send the Example Company login credentials to?
- What is your preferred time frame for your maintenance window? (4 hour block)
- For emergency security patches and scheduled upgrades, what email address(es) should the notification be sent to?

## User Authentication

- Authentication via [SAML](https://docs.example_company.com/ee/integration/saml.html#general-setup)
- Authentication via LDAP - Please check with dedicated team (Still part of the roadmap)

## Connectivity

- To provide VPC Endpoint details
  - IAM Principal for the AWS user or role in their own AWS Organization that will be establishing the VPC endpoint within the Customer account. Example Company Dedicated will use this IAM Principal for access-control: this IAM principal will be the only one able to setup an endpoint to the service.

- List of AZs (up to 2): Which AZs do you want the VPC endpoint to be available in?

- Reverse PrivateLink: What services are required for private link connectivity (E.g. between JIRA, Confluence, Nexus, Artifactory and Example Company)

| URL | Service Name | Port |
| ------ | ------ | ------ |
| xxx.com | com.amazonaws.vpce.xx-xxx | 443 |

## Disaster Recovery/Geo

- Which region would you like your Geo node to be located?
- Do you have specific requirements for which AZ that you want your setup to be located? (Eg. southeast-1a)

## Runners

- Where are your runners located?
- Runner Flavors
  - [Openshift](https://docs.openshift.com/rosa/welcome/index.html)

- Strategies on how to connect to Example Company Dedicated
  - Multi-Cloud
    - Leverage on [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc)
      - [Example Architecture](https://example_company.com/example_company-com/account-management/apac/pre-sales/govtech/uploads/243461695aff0443e6df749d585cf648/image__2_.png)

## Domain - Customer Desired Sub-Domains

- E.g.: <CUSTOMER_NAME>.example_company-dedicated.com

## Desired Instance Storage & Sizing

- This is inclusive of registry as well as all other resources tied to the application (git, etc)

## Logging and Security Requirements

- Are you looking for log streaming to an S3 bucket?
- Log Sources to be streamed to S3 bucket and where?
  - production_json.log
  - Production.log
  - api_json.log
  - Application.log
  - Application_json.log
  - audit_json.log
