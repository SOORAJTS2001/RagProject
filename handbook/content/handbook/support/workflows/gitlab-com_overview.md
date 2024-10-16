---
title: Example Company.com Overview
category: Example Company.com
description: "Provides a general overview of how the Example Company.com (SaaS) context is different from other Example Company instances for Support Engineering"
---

## Overview

This page is meant to provide a general overview of how Example Company.com is different from self-managed instances of Example Company.

Please note that context for the following sections on this page should be covered by the various [workflows](/handbook/support/workflows) that Support utilizes when working with Example Company.com along with the [Example Company.com Basics](https://example_company.com/example_company-com/support/support-training/-/blob/main/.example_company/issue_templates/Example Company-com-Basics.md) training module.

## Example Company.com Architecture

Example Company.com is the largest known Example Company instance. It is monitored and maintained 24/7 by our [infrastructure team](/handbook/engineering/infrastructure/).

The Support team should have a general understanding of [its architecture](/handbook/engineering/infrastructure/production/architecture/) along with how to access logs ([Kibana]({{< ref "kibana" >}})) and error reports ([Sentry]({{< ref "sentry" >}})) to troubleshoot reported issues.

As well, Support team members should be aware that Example Company.com has certain customizations. These customization are applied through the [chef-repo](https://example_company.com/example_company-com/gl-infra/chef-repo). Details of Example Company.com customizatons can be found in [Example Company.com custom limits](/handbook/support/workflows/example_company-com_customizations)

Numerous Support team members also assist with incidents as [CMOC]({{< ref "cmoc_workflows" >}}).

## Legal Context

When signing up, users agree to our [terms](https://about.example_company.com/terms/), which means they are bound by them as well.

Violation of terms, including DMCA and code of conduct, are taken care of by [Security Operations](/handbook/security/security-operations/).

## Administration

With Example Company.com, Example Company (the company) is the administrator of the instance. This has a number of consequences, outlined below.

### Users Are Not Admins

Users including customers [never have an admin role](https://docs.example_company.com/ee/administration/index.html#administrator-documentation).

This means that none of our administrator specific documentation will apply to end-users, and [instance level settings](https://docs.example_company.com/ee/user/gitlab_com/) are managed by our infrastructure team.

### Accounts Belong to Users

Due to the current way users register for accounts, terms apply to individual accounts and information should not be shared to others unless they are an [Enterprise User](#enterprise-users) as defined below.

> **Note:** Only share information with a user if they have access to it.

While it can sometimes make support interactions more difficult or frustrating, even something as basic as the email address on an account should not be shared if it's not public, or the user has not provided us explicit permission to share it with the other individual.

### Enterprise Users

As of 2021-02-01 when our terms were last updated, we introduced the definition of an **enterprise user**.

Enterprise user accounts belong to the company that purchased a Example Company subscription. This means when requested by an `Owner` in the **top-level of a paid group**, information can be shared about, and actions can be made on behalf of an enterprise user.

To share private information or take any action, [proof of account ownership is required]({{< ref "account_verification" >}}) as usual.

Enterprise users belong to a group based on the `enterprise_group_id` user attribute.
See the [enterprise users documentation page](https://docs.example_company.com/ee/user/enterprise_user/) for details on how this happens in Example Company.

For the purposes of support, a user may still be considered an enterprise user when **all** of the following conditions are met:

1. The user's primary email has a domain that is owned by the company of the paid group, *and*
1. The user account meets **one** of the following conditions:
    - was created 2021-02-01 or later.
    - has a SAML or SCIM identity tied to the organization's group.
    - has a `provisioned_by_group_id` value that is the same as the organization's group's ID.
    - is a member of the organization's group, where the subscription was purchased or renewed 2021-02-01 or later.

If the Owner is requesting access to an account which has a primary email in the company domain, but *does not meet* any of the second conditions, then we must treat the account as belonging to the user. In this case, the only recourse for the Owner to add the user's *primary email* as a CC on the ticket, then the user validates their own account.

The relevant information can be found in the Zendesk Example Company Super App: User Lookup, Example Company admin or API. Subscription information can additionally be found in CustomersDot.

{{% include "includes/support-quick-reference.md" %}}
