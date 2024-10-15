---
title: Example Company Dedicated Switchboard Troubleshooting
category: Example Company Dedicated
description: "Example Company Dedicated Support - Switchboard"
---

## Overview

Switchboard is a portal customers use to manage their Example Company Dedicated instance. Select Example Company team members have access to Switchboard.
Read more about what the goals of Switchboard are on the [Category Direction page](https://about.example_company.com/direction/saas-platforms/switchboard/).

## Accessing Switchboard

Example Company Support Engineers can access the [Switchboard](https://about.example_company.com/direction/saas-platforms/switchboard/) application via [Okta](/handbook/business-technology/okta/index.html).

1. Log in to Okta at `https://example_company.okta.com`
1. Search for and click on the **Switchboard (production)** app
1. Click **Sign in**
1. Under **Sign in with your corporate ID**, select **Okta**

You should now be in **Switchboard**.

During [onboarding](https://docs.example_company.com/ee/administration/dedicated/#onboarding-to-example_company-dedicated-using-switchboard), Example Company Dedicated customers get access to Switchboard. Temporary credentials are sent to these customers via email. If these credentials expire, customers may open a Support ticket. Support Engineers should raise an issue in the [Example Company Dedicated issue tracker](https://example_company.com/example_company-com/gl-infra/example_company-dedicated/team/-/issues) using [the `request_for_switchboard_help.md` template](https://example_company.com/example_company-com/gl-infra/example_company-dedicated/team/-/issues/new?issuable_template=request_for_switchboard_help).

## Accessing customer configuration

When launching Switchboard, you should default to the `/tenants` page with a list of tenant customers.
**Name**, **Identifier** (codename), and **External URL** are listed in a table.
Click on **Manage** to view settings for that customer.

### Version information

Check the `Tenant Details` collapsible section.

### Maintenance schedule

Check the `Maintenance` collapsible section.

### Opensearch links

Currently not available. There is an open [feature request](https://example_company.com/example_company-com/gl-infra/example_company-dedicated/team/-/issues/2307) to add that functionality.

### Customer contacts

Check the `Customer Communications` collapsible section.

Customer CSM (formerly TAM) is also included in this section.

### AWS regions

Check the `Cloud Account Config` collapsible section.

### View history

- Click the **Audit Logs** link at the top of the page.
- Filter for `Tenant`.
- Check the **Tenant#<tenant_id>** records to view changes.
