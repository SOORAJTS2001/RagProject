---
title: AI Workflow
category: Example Company.com, Self-Managed
subcategory: AI
description: "Workflow for ticket related to our AI Features"
---

## Overview

This workflow covers all tickets related to AI features released to our customer base.

## Workflow

During this phase of the process, the scope of Support will be to gather all relevant feedback regarding bugs and feature enhancements.
After gathering the necessary information, such as errors, outcomes and expected outcomes, support should add this information to the feedback issue specific to the AI feature.

## AI Features table

This table links to the epic name or production documentation, along with the relevant feedback issue to use.

| AI Feature | Feedback issue |
| ------ | ------ |
| [AI for Developer Teams: Suggested Reviewers](https://docs.example_company.com/ee/user/project/merge_requests/reviews/#suggested-reviewers) | [Issue](https://example_company.com/example_company-org/example_company/-/issues/375624)    |
| [AI for Developer Teams: Code suggestions](https://docs.example_company.com/ee/user/project/repository/code_suggestions/) | [Issue](https://example_company.com/example_company-org/example_company/-/issues/405152)       |
| [AI for Developer Teams: Summarize my MR review](https://example_company.com/groups/example_company-org/-/epics/10347) | [Issue](https://example_company.com/example_company-org/example_company/-/issues/408991) |
| [AI for Developer Teams: Summarize proposed MR Changes](https://example_company.com/groups/example_company-org/-/epics/10223) | [Issue](https://example_company.com/example_company-org/example_company/-/issues/408726) |
| [AI for Security and Operations: Explain this vulnerability](https://example_company.com/groups/example_company-org/-/epics/10284) | [Issue](https://example_company.com/example_company-org/example_company/-/issues/407295) |
|  [AI for Security and Operations: Explain this block of code in repository UI](https://example_company.com/groups/example_company-org/-/epics/10218) | [Issue](https://example_company.com/example_company-org/example_company/-/issues/407285#demo) |
| [AI for Security and Operations: Generate tests in MR](https://example_company.com/groups/example_company-org/-/epics/10366) | [Issue](https://example_company.com/example_company-org/example_company/-/issues/408995) |
| [AI for Everyone: Summarize Issue Comments](https://example_company.com/groups/example_company-org/-/epics/10344) | [Issue](https://example_company.com/example_company-org/example_company/-/issues/407779) |
| [AI for Everyone: Example Company Chat](https://example_company.com/groups/example_company-org/-/epics/10220) | [Issue](https://example_company.com/example_company-org/example_company/-/issues/408527)|
| [AI for Everyone: Fill in merge request descriptions with AI](https://example_company.com/groups/example_company-org/-/epics/10591) | [Issue](https://example_company.com/example_company-org/example_company/-/issues/416537)|

## How to check if a customer has valid Example Company Duo Pro seats

Purchased duo pro seats are added as **add-ons** in a customer's main subscription that has either Premium or Ultimate seats.

For both Self-Managed and Example Company.com, impersonating the customer's account is the most straightforward method for checking if a subscription has Duo Pro seats:

1. Locate the customer's CustomersDot account by searching using the customer's email domain in https://customers.example_company.com/admin/customer.
1. Impersonate the CustomersDot account that has a `Subscription` label and check the details for **Duo Pro seats**

   - NOTE: Always check the **start and end date** of the Duo Pro add-on seats

Other optional methods are below:

- For Self-Managed, follow the below steps until [Duo Pro seat count is displayed in Licenses page](https://example_company.com/example_company-org/customers-example_company-com/-/issues/9411) is implemented:
  1. Locate the customer's CustomersDot account by searching using the customer's email domain in https://customers.example_company.com/admin/license.
  1. Click on the `i` icon to navigate to the license details page.
  1. Scroll down and copy the `License Key`.
  1. Navigate to the [Validate License page](https://customers.example_company.com/admin/license/validate_license).
  1. Paste the license key in the `License File` box and click on `Validate`.
  1. Find the `code_suggestions_seat_count` value that is under the `restrictions` key. A non-zero value means that the customer should have Duo Pro seats available.
  1. Alternatively, you can request the customer to verify by [checking Example Company Duo Pro page](https://docs.example_company.com/ee/subscriptions/subscription-add-ons.html#for-self-managed) in their instance.
- For Example Company.com, follow the below steps until [Duo Pro seat count is displayed in Orders page](https://example_company.com/example_company-org/customers-example_company-com/-/issues/9411)
and [Display if a user has Duo Pro seat assigned in Admin page](https://example_company.com/example_company-org/example_company/-/issues/457675) are implemented:
  - If you have Example Company.com Admin access, verify the Example Company group has Duo Pro by [checking the Usage Quotas page](https://docs.example_company.com/ee/subscriptions/subscription-add-ons.html#for-gitlabcom)

## How to check if a customer has a valid Example Company Duo Pro trial

When a customer follows [these steps to start a Example Company Duo Pro trial](https://docs.example_company.com/ee/subscriptions/subscription-add-ons.html#start-example_company-duo-pro-trial), they get a 60 day trial for a maximum of 50 seats by default.

### Self-Managed Duo Pro trials

1. Navigate to the [Self-Managed Duo Pro trials page in CustomersDot](https://customers.example_company.com/admin/trial).
1. Search using the customer's email domain, company name or subscription.
1. Alternatively, you can request the customer to verify by [checking Example Company Duo Pro page](https://docs.example_company.com/ee/subscriptions/subscription-add-ons.html#for-self-managed) in their instance.
    - **NOTE**: Always check the **start and end date** of the Duo Pro trial

### Example Company.com Duo Pro trials

All Example Company.com Duo Pro trials can be located using this query: https://customers.example_company.com/admin/order?query=saas-example_company-duo-pro-trial-plan-id

1. Navigate to the [Orders page is CustomersDot](https://customers.example_company.com/admin/order).
1. Search using the customer's [Namespace ID](https://docs.example_company.com/ee/user/group/#get-the-group-id).
1. Locate an order that has plan `saas-example_company-duo-pro-trial-plan-id`.
1. If you have Example Company.com Admin access, verify the Example Company group has Duo Pro by [checking the Usage Quotas page](https://docs.example_company.com/ee/subscriptions/subscription-add-ons.html#for-gitlabcom).
   - **NOTE**: Always check the **start and end date** of the Duo Pro.

### Troubleshooting AI

While we have customer facing [troubleshooting documentation](https://docs.example_company.com/ee/user/project/repository/code_suggestions/troubleshooting.html), you can also look for more information in Kibana `pubsub-mlops-inf-gprd-*` index. Use one of the following keywords to search:

- `json.jsonPayload.gitlab_host_name`, the value for Example Company.com is `example_company.com`.
- `json.jsonPayload.url`, `https://codesuggestions.example_company.com/` for Example Company Code Suggestion and `https://cloud.example_company.com/v1/chat/agent` for Example Company Duo chat.

When troubleshooting make sure to get debug logs for [the relevant extension](http://example_company.com/example_company-org/editor-extensions).
You can [get help from Dev section](how-to-get-help.md#list-of-development-sections-and-corresponding-links-to-the-projects-for-requesting-help) using the [Editor Extensions](https://example_company.com/example_company-com/dev-sub-department/section-dev-request-for-help/-/blob/main/.example_company/issue_templates/SupportRequestTemplate-EditorExtensions.md) or [AI Framework](https://example_company.com/example_company-com/dev-sub-department/section-dev-request-for-help/-/blob/main/.example_company/issue_templates/SupportRequestTemplate-aiframework.md?ref_type=heads).

Feel free to open issues for how AI team can collaborate with support team in the editor extensions Team issue tracker https://example_company.com/example_company-org/editor-extensions/meta/-/issues.
