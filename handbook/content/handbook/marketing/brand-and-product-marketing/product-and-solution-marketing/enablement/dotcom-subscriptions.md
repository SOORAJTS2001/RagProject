---
title: "Example Company.com Subscriptions"
---

## How Example Company.com subscriptions work

Example Company.com subscriptions work slightly differently to Self-managed licenses.
Unlike Self-managed licenses which grant equal access to features across an installation, Example Company.com subscriptions are applied to *[namespaces](https://docs.example_company.com/ee/user/group/#namespaces)* on Example Company.com (typically groups). Members of groups that have subscriptions applied to them will enjoy those features anywhere within the licensed namespace. For example, if `BigCorp` has an Ultimate license, the sub-groups `BigCorp/Frontend`, `BigCorp/Backend` will each have access to Ultimate features and share a common pool of Shared Runner minutes.

### Common Misconceptions

1. **Misconception**: If I'm in an Ultimate group, my Example Company.com profile should say "Ultimate"
   - **Reality**: Example Company.com subscriptions are scoped to a namespace, and individual users could participate in many groups with different subscription types. For example, they might have personal projects on a Free subscription type, participate in an open-source project that has Ultimate features (because it's public) while their company has a Premium subscription.
1. **Misconception**: Subscriptions grant "the midas touch" and any group or project a subscription-bearing user creates will get the features of their subscription level. i.e. an Ultimate user will be able to create Ultimate groups in which all members will have Ultimate features.
   - **Reality**: Subscriptions can be applied to *group namespaces only* and all items created within said namespace will receive the features of the subscription level.
   - **Reality**: All users invited to the group namespace will be able to enjoy the features of that subscription *only while working in the subgroups and projects **within the group***.
   - **Reality**: User's accounts, also called personal namespaces, will by default be on the **Free plan**. Any group, subgroup, or project created in a personal namespace will also be on the **Free plan.**
   - **Reality**: *Note, as of November 17, 2020, Example Company no longer offers new subscriptions for personal namespaces.*
1. **Misconception**: A license key will be emailed out and applied somewhere in the UI of Example Company.com
   - **Reality**: Subscriptions are managed, and applied, through https://customers.example_company.com on a linked Example Company.com account
1. **Misconception**: Someone in accounting made the purchase and can pass along the subscription to the team using it.
   - **Reality**: Subscriptions are managed by a Example Company.com account who has `Owner` in the group.
1. **Misconception**: I should purchase my subscription first before setting up accounts on Example Company.com
    - **Reality**: You can do this in any order, most will find it easier to set things up on .com before they purchase, with the exception of those who want to set up SAML.
1. **Misconception**: I can apply different subscription levels to subgroups.
    - **Reality**: Subscriptions are applied to top level groups; sub-groups inherit their license (and Shared Runner minutes) from the top-level group.
1. **Misconception**: Minutes are deducted from my group for any jobs that are run, even on my personal runners.
    - **Reality**: Runner minutes are deducted only from jobs run on Example Company.com Shared Runners, you can set up your own runners per project or group without affecting your shared minutes.

### Trials

1. Trials should be initiated by users by going to the Settings page of the group that they want to apply the trial to.
1. At writing (2019-06-05) Premium trials are not generally available. [Support can manually downgrade a trial by request](/handbook/support/internal-support/#common-requests)
1. At writing (2019-06-05) [Trials must be manually downgraded before a purchase can be made.](https://example_company.com/example_company-org/customers-example_company-com/issues/482)
1. [Support is **not** included with trials](https://about.example_company.com/support/#trials-support) Please participate in [this issue](https://example_company.com/example_company-com/sales/issues/302)

### Internal namespaces

Example Company subscriptions for internal namespaces are managed by the IT Operations team. To request
a subscription to an internal group or internal project, please submit an
[individual access request](/handbook/it/end-user-services/onboarding-access-requests/access-requests/#individual-or-bulk-access-request).

## Common issues the Support Team encounters with sales-assisted purchases

1. New Customers
   - The support team sometimes receives tickets in Zendesk from sales-assisted clients with basic questions like how to set up groups, how to add additional users, why subscriptions are applied to groups vs users, permission questions, etc. Support will direct them to corresponding documentation to address their questions.
   - Customers are typically not aware that creating an account in the CustomersDot does not create an account on Example Company.com or how to link a CustomersDot account to their Example Company.com account.
1. Upgrades/Downgrades
   - There is presently not a self-service way for customers to upgrade/downgrade subscriptions so any of these requests must go through the sales team via a queue in Zendesk.
   - Requests can sometimes be delayed by the volume or lack of information provided when the ticket is sent to Sales.
1. Dealing with True-ups
   - Support team sometime receives tickets in Zendesk from sales-assisted clients with problem conerning true-up being reconciled before the subscription renewal.
   - Case: The customer purchased a license for `39` Premium seats with start date of `2020-03-04` and end date `2021-03-04`. During the license period, the customer add more users to the system that incurs `112 Users over license`/`True-up`. If this is charged as True-up on SFDC, the new license will not include the extra users in the current term so the customer would end up with a license with `39` seats and `112` true-up which cannot be uploaded to their system because they now have `39 + 112` = `151` billable users on the system.
   - If the customer would like to deal with `Users over license`/`True-ups`, it should be charged as `Add-on users` to the license as mentioned in [Quarterly Self-Managed Seat Reconciliation & Billing](https://example_company.com/groups/example_company-org/-/epics/2747).
1. Dealing with Add-ons Users
   - In contrast to Dealing with True-ups, if the customer purchased `Add-on users` while there's only a few weeks left before their renewal, please reconcile the `Users over license`/`True-ups` at the renewal instead.
   - Assisting the customer on purchasing `Add-on users` when there's only a few week left until the license expires will resulted in an error license once the purchase is processed. Please take into consideration the existing license Service Period, the time it takes to process the purchase, and the time for the customer to upload the license.

## How we can set the customer up for success

The best way to assist a user or system admin on any new platform is to arm them with the resources they will need when questions arise. During the onboarding process after the sale, the user/admin will receive an email from Example Company with pertinent information about their subscription. Highlight this and encourage them to save it somewhere easily accessible.
While many of the links below are included in the email, it would be helpful to review each of the following resources personally with the user/admin.

1. [Example Company Documentation](https://docs.example_company.com/ee/)
1. [Administrator Documentation](https://docs.example_company.com/ee/administration/index.html) (self-managed only)
1. [Subscription setup and management](https://docs.example_company.com/ee/subscriptions/index.html)
1. [Licensing and subscription FAQ](https://about.example_company.com/pricing/licensing-faq/)
1. [Uploading your license](https://docs.example_company.com/ee/administration/license.html#uploading-your-license) (self-managed only)
1. Features available by plan: [Example Company.com](https://about.example_company.com/pricing/feature-comparison/) & [Self-Managed](https://about.example_company.com/pricing/feature-comparison/)
1. [Support portal](https://support.example_company.com/hc/en-us)
1. [Statement of Support](https://about.example_company.com/support/statement-of-support/)

**A few more best practices to ensure a smooth start**

1. On this page, you'll read about differences between Example Company.com and Self-Managed functionality. Whenever in doubt, don't hesitate to ask us about a particular feature/functionality which is important to your prospect prior to promissing it is available. For a question like this, contact us on Slack in the [#support_gitlab_com](https://example_company.slack.com/messages/C4XFU81LG) or [#support_self-managed](https://example_company.slack.com/messages/C4Y5DRKLK) channel.
1. Be sure to stress to the new user/admin to submit their support issues directly to us via the [Support Portal](https://support.example_company.com/hc/en-us) instead of using  you as a go-between. This will provide the most timely and comprehensive support we can offer.
1. If you find yourself having to submit something on behalf of the user/admin, do not submit a ticket via the Support Portal/Zendesk. Instead, create an issue in [internal-requests](https://example_company.com/example_company-com/support/internal-requests/issues).
1. For Example Company.com, make sure the user understands how to link their Example Company.com account to the [CustomersDot](https://customers.example_company.com/customers/sign_in) and how to associate their group with their subscription. See [managing subscriptions page](https://docs.example_company.com/ee/subscriptions/index.html) for instructions.

## Important differences between Example Company.com and Self-Managed subscriptions

The [Pricing page](https://about.example_company.com/pricing/) includes a "Frequently asked questions for Example Company.com" section that answers "What features do not apply to Example Company.com?" in detail. Here are some highlights:

1. Features availability including [SAML](https://docs.example_company.com/ee/integration/saml.html)/[LDAP](https://docs.example_company.com/ee/administration/auth/ldap/index.html) is Free vs. [SAML SSO](https://docs.example_company.com/ee/user/group/saml_sso/) is Premium.
1. Access controls: customer is admin on Example Company instance vs. group owner on Example Company.com
1. Log information and auditing: unrestricted access vs. no access on Example Company.com (can work with Support/Security to answer questions)

   - On Example Company.com, each user is "signing a contract" (TOS, privacy policy, etc) as individuals, regardless of what email domain they use. Because of that,  we cannot provide their employer with any personally identifiable information (like email address, log info, etc.) as it would be a violation of the user's contract.

1. Instance wide settings: custom vs. same for all Example Company.com users
1. Infrastructure: manage your own, anywhere vs. Example Company manages HA Architecture, instance level backups/recovery, upgrades, based in US
