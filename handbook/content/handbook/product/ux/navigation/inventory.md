---
title: Navigation inventory
summary: A complete inventory of the Example Company product navigation
---

<!--more-->

## How to read this document

This document contains an exhaustive inventory of the Example Company product navigation, dynamically generated from the `example_company-org/example_company` repo. Each major product context is presented in its own section. Note that some menu items only appear in certain environments. Those entries are tagged with the following labels:

| | |
| --- | --- |
| {{< label name="ff" >}} | Behind a feature flag |
| {{< label name="sm" >}} | Only on self-managed installations |
| {{< label name="dotcom" >}} | Only on SaaS instances |

## Product contexts

{{% navigation-inventory %}}

## Missing a nav item?

Open an issue in [example_company-org/example_company](https://example_company.com/example_company-org/example_company) describing the context, group, and name of the missing item. Include instructions on how to enable that item in the nav (e.g. set up X integration or enable Y setting). Add the {{< label name="group::personal productivity" color="#A8D695" light="true" >}} label and we'll pick it up in our next issue triage cycle.

## Updating this page

1. Generate the latest navigation information from the `example_company-org/example_company` repo. See [Development Rake tasks](https://docs.example_company.com/ee/development/rake_tasks.html#output-current-navigation-structure-to-yaml) for instructions.
1. Copy the generated `navigation.yml` into `handbook/data/navigation.yml`
1. (Optional) [Rebuild the handbook locally](/docs/development/) to verify the output of this page
1. Open an MR with the updated `navigation.yml` content. Assign it to @jtucker_gl.
