---
title: Handling flagged licensing provisioning failures
description: "How to handle flagged licensing provisioning failures"
category: Example Company Self-Managed licenses
---

The [Provision tracking system](https://example_company.com/groups/example_company-org/-/epics/8300) provides a means of monitoring provision failures via a failure alerting system in the Slack channel `#provision_failures` so that the Fulfillment Product Team and the L&R Support Team can be made aware quickly when a failure occurs and act upon it.

## Workflow for handling Provisioning failures

1. The Fulfillment Team will monitor the Slack channel for provisioning failures. The following link provides information on the [Provision Failure Monitoring process](https://example_company.com/example_company-org/customers-example_company-com/-/blob/123966423b08392b13675cec9249484dd2faf377/doc/provision_tracking_system/failure_monitoring.md#provision-failures-monitoring) from the Provisioning team perspective.
1. If the Fulfillment Team is unable to resolve a failed provision then they will request help from L&R Support via [the internal request form](https://support-super-form-example_company-com-support-support-op-651f22e90ce6d7.example_company.io/). Use the **Example Company Support Internal Requests for Global customers** request option, and **Report a provision failure** for the internal request type. The criteria for submission are:
   - If Fulfillment requires L&R Support intervention to fix something for the customer, OR
   - The root cause of the issue is already fixed or being fixed, so it's not going to be an ongoing failure case
1. In such situations the Support Engineer should [open a ticket on behalf of the customer](/handbook/support/workflows/working-on-tickets#8-how-can-i-open-a-new-ticket-on-behalf-of-a-customer) to inform them of the issue and offer them a solution or workaround if one is available. The Support Engineer can communicate if required with the Provisioning submitter via the raised Zendesk ticket.
1. If required, the Support Engineer can also submit a new bug issue, update (requesting higher prioritization or feedback) an existing issue or create a new feature request as outlined in the Example Company handbook section [Managing Product Issues](/handbook/support/license-and-renewals/workflows/managing_product_issues/)
