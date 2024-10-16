---
title: Remove Validation
description: "Workflow to remove validation on a Example Company.com user account"
category: Example Company.com
subcategory: Accounts
---

## Overview

This workflow covers how to remove validation for a Example Company.com user account. All free users [created after May 17, 2021](https://about.example_company.com/blog/2021/05/17/prevent-crypto-mining-abuse/) require a credit or debit card validation to use shared runners on Example Company.com.

> Credit card validation *is not* connected to a customers.example_company.com account or Zuora subscription.

## Workflow

You must ensure the customer is aware that removal of validation will result in their Example Company.com account being unable to use shared runners until they provide a credit or debit card for validation.

1. Complete the [account ownership verification workflow]({{< ref "account_verification#workflow" >}}) to verify the account owner and that you have received their permission to proceed. Please use the [standard data classification definition](https://internal.example_company.com/handbook/support/#data-classification). The peer review is not mandatory for these cases.
1. Sign into your admin account and locate the customer's user account.
1. Under the account tab, click `Edit`.
    1. Uncheck the "Validate user account" box.
    1. Add an [Admin Note]({{< ref "admin_note" >}}).
    1. Save your changes.
1. Send the following message to the user:

```text
Hi,

We have now processed this request. Your credit card validation has been removed and your credit card details have been deleted from your Example Company.com account.

Regards,
```
