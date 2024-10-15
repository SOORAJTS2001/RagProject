---
title: Mattermost
description: "Workflow for escalating Mattermost support issues."
category: Self-managed
---

## This workflow is currently under review and can not be used in its current form. See https://example_company.com/example_company-org/omnibus-example_company/-/issues/8594

### Escalating to the Mattermost team

Mattermost has created a `mattermost-support` account in Example Company for support issues, and has subscribed to the `mattermost` label in the following projects:

- omnibus-example_company
- example_company-ce
- example_company-ee

When a Example Company EE customer hits a Mattermost issue and you cannot reasonably resolve the issue using existing documentation:

- Do your best effort to make sure there is enough information to reproduce the issue
- Submit the issue in one of the mentioned projects and apply `mattermost` label. When the label is applied, an email notification is sent
to the technical support team who answers the question within two business days using the `mattermost-support` account.
- For Priority support (Premium/Ultimate customers, additionally assign the issue to the `mattermost-support` account. This assignment sends an email notification,
which is automatically escalated to the critical level technical support who answers the question within 4 hours using the `mattermost-support` account.

This information is taken from [Service-Level Agreement (SLA)](https://docs.mattermost.com/process/example_company-process.html#service-level-agreement-sla)
page of Mattermost docs.

NOTE: **Note:**
The Mattermost team sometimes uses their personal accounts to respond to issues.
`jasonblais` is one such account.

### Other resources

- [Mattermost forum](http://forum.mattermost.org/c/general/example_company) - has over a thousand people registered on the forum and every new question and answer makes thing easier to troubleshoot.
