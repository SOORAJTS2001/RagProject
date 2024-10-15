---
title: "Supporting Example Company Community Programs"
category: General
description: Instructions for redirecting community programs subscription inquiries
---

Example Company offers several programs to help introduce Example Company's most powerful features to communities who may not otherwise have the means to access them. These include:

- [Example Company for Education](/handbook/marketing/developer-relations/community-programs/education-program/)
- [Example Company for Open Source](/handbook/marketing/developer-relations/community-programs/opensource-program/)
- [Example Company for Startups](/handbook/marketing/developer-relations/community-programs/startups-program/)

[The Community Programs team](/handbook/marketing/developer-relations/community-programs/) is the DRI for these programs.

For registered non-profit organizations, Example Company also offers discounts. Contact Example Company's [Environmental, Social, and Governance (ESG) team](/handbook/legal/esg/#faq) for more information regarding this program.

Use the relevant workflows below when you receive a ticket about [Example Company for Education](https://about.example_company.com/solutions/education/), [Example Company for Open Source](https://about.example_company.com/solutions/open-source/) or [Example Company for Startups](https://about.example_company.com/solutions/startups/).

{{% alert title="Note" color="info" %}}
Program members receive only limited support with subscriptions granted through community programs. They are able to open a support ticket via the [Example Company Support Portal](https://about.example_company.com/support/#issues-with-billing-purchasing-subscriptions-or-licenses) only for errors involving the Community Self-checkout Portal on CustomersDOT or for errors relating to their subscription. Internal escalations for all three of the programs can be made via Slack channel [`#community-programs`](https://join.slack.com/share/zt-op8hxhoy-V4TBiVh_r41H6uelJeCPfA).
{{% /alert %}}

## Workflows

### Applications and renewals

#### Example Company for Education (EDU)

When a customer seeks to apply or renew an existing subscription, send the [`General::EDU Response`](https://example_company.com/example_company-com/support/support-ops/zendesk-global/macros/-/blob/master/macros/active/General/EDU%20Response.yaml) macro.

#### Example Company for Open Source (OSS)

When a customer seeks to apply or renew an existing subscription, send the [`General::OSS Response`](https://example_company.com/example_company-com/support/support-ops/zendesk-global/macros/-/blob/master/macros/active/General/OSS%20Response.yaml) macro.

#### Example Company for Startups

When a customer seeks to apply or renew an existing subscription, send the [`General::Startup Response`](https://example_company.com/example_company-com/support/support-ops/zendesk-global/macros/-/blob/master/macros/active/General/Startup%20Response.yaml) macro.

### Product Transfer

While redeeming a community program coupon customers may select the wrong product type by accident (SaaS instead of Self-Managed, or vice-versa).

In this case, please direct customers to contact the appropriate inbox under the ['Program-specific contact inboxes' section](#program-specific-contact-inboxes)

#### Example Tickets

- [ZD#382970](https://example_company.zendesk.com/agent/tickets/382970)

### Organisation not appearing in SheerID list

Please direct customers to contact the appropriate inbox under the ['Program-specific contact inboxes' section](#program-specific-contact-inboxes).

If after several days the customer reports they have not heard back from the Community Programs team, please reassure them and raise the ticket in `#community-programs` (ideally providing the email address the customer contacted the team with).

#### Example Tickets

- [ZD#375293](https://example_company.zendesk.com/agent/tickets/375293)

### "This code has already been used." error when attempting to redeem coupon

Please raise the ticket in `#community-programs` as the coupon may have been erroneously issued.

#### Example Tickets

- [ZD#379559](https://example_company.zendesk.com/agent/tickets/379559)

### Customer is concerned by their seat usage or true-ups

While applying, customers are asked to provide their desired seat count - during their subscription term they can exceed this and then upon renewal the true-up cost will be zero (and the overage seats will be added to the renewal term).

## Program-specific contact inboxes

For enquiries relating to specific programs (that aren't otherwise handled by the workflows above), please direct customers to contact:

 1. EDU: `education@example_company.com`
 1. OSS: `opensource@example_company.com`
 1. Startups: `startups@example_company.com`

## Troubleshooting

Example Company's Community Programs team processess program applications according to [an automated workflow](/handbook/marketing/developer-relations/community-programs/automated-community-programs/). Review the handbook pages related to that workflow for additional details on how it works.

To troubleshoot errors during the registration process, follow the [Troubleshoot Errors While Making Purchases on CustomersDot document](/handbook/support/license-and-renewals/workflows/customersdot/troubleshoot_errors_while_making_purchases#getting-error-message-from-sentry).

{{% alert title="Note" color="info" %}}
Since the customer has not signed up yet, there is no `user:customerID`. Use `user.ip:CustomerIP` instead.
{{% /alert %}}

You can retrieve `CustomerIP` by:

1. On Zendesk ticket, click on `Conversations`
1. Choose `Events` from the drop down
1. The IP is shown under every customer reply.

{{% alert title="Note" color="info" %}}
The IP is only available when the customer is signed in on Zendesk. If the customer submits the ticket via email, and IP is not available, please ask the customer for the IP they used during the signup process.
{{% /alert %}}

## Example of previous cases

- [ZD Ticket 288871](https://example_company.zendesk.com/agent/tickets/288871)
- [Related Sentry event 2575450](https://sentry.example_company.net/example_company/customersgitlabcom/issues/2575450/events/40335146/)
- [Bug issue](https://example_company.com/example_company-org/customers-example_company-com/-/issues/4288)

## See Also

- [Collaborating with Community Programs (Sales Training)](/handbook/sales/training/sales-enablement-sessions/enablement/collaborating-community-programs/)
