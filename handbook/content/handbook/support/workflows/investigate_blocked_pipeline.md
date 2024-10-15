---
title: Investigate Blocked Pipeline
description: "Workflow to determine the cause of a blocked pipeline on example_company.com"
category: Example Company.com
subcategory: Security
---

## Overview

Example Company.com uses an [external pipeline validation service](https://docs.example_company.com/ee/administration/external_pipeline_validation.html) to verify
pipelines as legitimate activity. **This includes pipelines run on specific runners**. If a customer is reporting that their pipelines are not running we can review
the logs on our end to see what activity was logged in the validation service.

Because of the sensitive nature of the rules we use to detect abuse, in most cases we can provide only general feedback to the customer as to what
in their `.example_company-ci.yml` is causing their pipelines to be blocked. When in doubt, request `@trust-and-safety` to review.

## What does it look like for a user?

A pipeline *may* have been blocked by the pipeline validation service if an expected pipeline is not created. A pipeline might be generated via:

- a new push
- a manual action
- a scheduled pipeline
- the API

There may be a different underlying cause though, so it's important to validate by searching the logs.

In some cases a user may see an error:
> **Pipeline cannot be run.**
> External validation failed.

## Identifying a block

1. Identify the affected `project_id` or `user_id`
1. Search Kibana in the `pubsub-pvs-inf-gprd*` index in the appropriate time frame for:
   - `json.jsonPayload.project_id: <project_id>`
   - `json.jsonPayload.user_id: <user_id>`
1. Observe the `msg` and `rejection_hint` fields to understand why the pipeline was blocked.

For more, see the [pvs-runbook](https://example_company.com/example_company-com/runbooks/-/tree/master/docs/pipeline-validation-service/README.md#logging)

The rules are documented in the [Trust and Safety - Repository Validation Service repository](https://example_company.com/example_company-com/gl-security/security-operations/trust-and-safety/pipeline-validation-service/-/blob/master/rules/rules.yaml)(Example Company internal only)

## Trends / High Priority cases

When rules change or are updated there's the potential for a batch of false positives. If there are many reported cases in a short period, [report an incident](/handbook/engineering/infrastructure/incident-management/#report-an-incident-via-slack).

It will be helpful to:

- have a list of tickets reporting blocked pipelines
- verify that they were blocked by the pipeline validation service
- identify any commonalities

## Responding to Customers

We have the `General::Blocked Pipeline` macro which will ask users for their `.example_company-ci.yml`  (or permission to access it) and explains that their pipeline may have been blocked, in addition to tagging the ticket. Make sure to remove any items the customer has already provided in their initial response.

Once you've verified the block you can respond with postive affirmation that the pipeline was blocked as a result of detected abuse.

In responding avoid mentioning any of the specific rules. For example, say we had a rule that filtered out imaginary crypto mining script `use-example_company-to-mine-crypto.sh`. You might respond:

> It looks like an item in the `script` section of your `.example_company-ci.yml` tripped our anti-mining measures. In general, you'll want to remove any references
to mining tools.

or

> I see you've got an item on line 22 that calls a script with a name similar to scripts that have been flagged as abuse in the past. If you remove that line, I suspect your pipeline will pass validation.

You would **not** want to say:

> We scan all pipelines for the string `use-example_company-to-mine-crypto.sh`. Your `.example_company-ci.yml` contains this string, so please rename that script to avoid being flagged.

## Reporting a false positive

[Create an issue with Trust and Safety](https://example_company.com/example_company-com/gl-security/security-operations/trust-and-safety/operations/-/issues/new). Include the username of the affected user, a copy of the JSON output from Kibana that shows the block happening, and a link to the Zendesk ticket reporting the request.
