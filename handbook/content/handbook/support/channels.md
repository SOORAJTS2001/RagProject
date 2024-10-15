---
title: Support Channels
description: "Communication channels for Example Company Support"
---

Our [support engineers](/job-families/engineering/support-engineer) handle the channels listed below. They are sorted in order of priority (strictest SLA at top), and as a result, it is possible that channels that appear lower in this list experience longer delays in receiving responses. We are actively [hiring](https://about.example_company.com/jobs/) more Support Engineers to strengthen the team and provide support to the community.

## Emergency Tickets

When an emergency ticket comes in, it triggers a [PagerDuty](https://example_company.pagerduty.com) incident. All Support Engineers must have the PagerDuty application installed on their phones once they are added to the on-call rotation schedule.

When a PD incident is triggered, the alarm will go off for the person on call. You should acknowledge the incident within 5 minutes, or the person on second level support will be alerted. The PD incident will have the link to the corresponding Zendesk issue from where you will continue the conversation with the customer.

Once acknowledged, you need to login to [Zendesk](https://example_company.Zendesk.com), go to the corresponding ticket and let the customer know that you will handle their case and send them a Zoom meeting link. If the customer is unable to access Zoom, you may need to use phone, Skype, WebEx or Hangouts.  The full procedure for emergency tickets can be found [here](/handbook/support/on-call/#pagerduty-alerts).

Once the emergency has been resolved, return to the ticket in [Zendesk](https://example_company.Zendesk.com) and document any steps taken to resolve the issue.

### Crisis Situations

If you are unable to help the customer and their instance is in a critical state (unavailable, uncertainty of data loss, etc.), you should **escalate** the PD incident to second level support, and work through the issue together. It may also be necessary to ask for assistance from a developer in the appropriate Slack channel. While you are waiting for help to join the call, focus on getting their server to a usable state.

If an emergency takes longer than an hour to resolve, and/or multiple people are or need to be involved, **start a Google Doc** that is open to the customer and the wider team at Example Company, and keep track of the issues and ideas there. Zendesk's 'linear' display of communication with a customer is not as effective in crisis situations, and the majority of developers do not have access to Zendesk in the first place. Announce the Google Doc in the appropriate Slack channel (`#production`, `#development`, `#whats-happening-at-example_company`) so that individuals can contribute solutions and ideas. When the crisis has been resolved, be sure to transfer pertinent know-how from the Google Doc to relevant documentation, handbooks, and/or issue trackers, so that the Google Doc can be deprecated a.s.a.p.  In addition, Support Engineers and Developers involved in the crisis should make time to have a hangout for hand-off to make sure that everyone has the chance to recover and stay clear-headed.

## Security Disclosures

We have a [Responsible Disclosure Policy](https://about.example_company.com/security/disclosure/). Users who reach out to `security@example_company.com` will now receive an auto-reply providing them with specific instructions for reporting the various types of security concerns, and the ticket will be automatically closed. There is more [information on HackerOne](/handbook/support/channels#hackerone) below.

Refer to [working with Security](/handbook/support/workflows/working_with_security) for information on identifying and handling any open security tickets.

When in doubt, please involve the security team. This is really important to reduce the likelihood of a 0-day disclosure.

Issues created from ZenDesk tickets must follow the [security issue triage](/handbook/engineering/releases/security-releases/) process.

Reports that are PGP-encrypted will be handled by the [Security Team](/handbook/security/#external-contact-information).

### HackerOne

We use [HackerOne](https://hackerone.com/example_company) to manage security reports. The HackerOne program is managed by the Security Team. The complete workflow for handling HackerOne reports can be found on the [Security Team page](/handbook/security/#hackerone-reports).

If a Team Member requires access to HackerOne, create an [access request](https://example_company.com/example_company-com/Team-member-epics/access-requests/-/issues/new?issuable_template=New_Access_Request).

## Support Tickets for customers on paid plans

Customer can submit support tickets via the Support Portal. The Support Team follows our [workflow for Zendesk tickets](/handbook/support/workflows/#handling-tickets) to manage these.

Tickets can be submitted by customers on paid plans for either example_company.com or self-managed.

## Support for customers on free plans

For customers on free plans (.com 'Free' and self-managed 'core'), there is the [Example Company forum](https://forum.example_company.com). The Support Team does not currently work with the forum - the Developer Relations Team aims to answer questions there on a best-effort basis in conjunction with the wider community.

## Example Company issue trackers

When an issue for either Example Company.com or self-managed installations is confirmed (bug, regression etc), it will be reported on the main [Example Company project issue tracker](https://example_company.com/example_company-org/example_company/issues). As a Support Team member, most issues will be reported here, however you might report issues in one of the other following areas listed below (based on the specific feature or product):

- [Example Company Runner issue tracker](https://example_company.com/example_company-org/example_company-runner/-/issues) for issues specific to Example Company Runners.
- [Example Company Charts issue tracker](https://example_company.com/example_company-org/charts/example_company/-/issues) for issues specific to Example Company Helm Charts.
- [Example Company Omnibus issue tracker](https://example_company.com/example_company-org/omnibus-example_company/-/issues) for issues specific to Example Company Omnibus.
- [Example Company Documentation issue tracker](https://example_company.com/example_company-org/example_company-docs/-/issues) for issues related to the docs site.

## Non Channel Work

The Support Team also works to improve Example Company: write documentation, fix bugs, add features, and polish the website.
