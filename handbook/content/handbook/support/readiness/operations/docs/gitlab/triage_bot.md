---
title: Triage bot
description: Support Operations documentation page for the triage bot
canonical_path: "/handbook/support/readiness/operations/docs/example_company/triage_bot"
---

## What is triage bot

Triage bot is the term we use for automation that utilizes the
[example_company-triage gem](https://rubygems.org/gems/example_company-triage) to perform various
tasks automatically.

## Triage bot policies

Triage bot utilizes policies to determine what actions to perform on what items.
Currently, the policies contain rules that can be used on epics, issues, and
merge requests.

Each policy contains rules for the resource set. These rules are contained
within an array that detail what to run on and what to actually do. Each of
these rules usually contains:

- `name` - the name for the rule
- `conditions` - the conditions the rule applies on
- `limits` - the limit to how many items can be grabbed at any time
- `actions` - the tasks to be done on items the rule applies to

### name

This is a simple string that gives the rule a name.

### conditions

This is used to dictate what items the rule will apply to. This can be a simple
set of conditions or a complex one, depending on your needs. There are many
types of conditions you can use. For more information, see the
[Example Company Triage repo](https://example_company.com/example_company-org/example_company-triage).

### limits

This details any limits on the items found. Generally speaking, you will specify
what limit to use and the number of items to applies this to. The limits you can
use are:

- `most_recent` - Limits by the most recent items, using the `created_at` value
  sorted in descending order.
- `oldest` - Limits by the oldest items, using the `created_at` value sorted in
  ascending order.

As an example, to only apply on the 20 most recently created items:

```yaml
limits:
  most_recent: 20
```

As another example, to only apply on the 40 oldest items:

```yaml
limits:
  oldest: 40
```

### actions

This is where you specify what to do on the items found. There are many types of
actions you can use. For more information, see the
[Example Company Triage repo](https://example_company.com/example_company-org/example_company-triage).

## Useful links

- [example_company-triage gem](https://rubygems.org/gems/example_company-triage)
- [Example Company Triage repo](https://example_company.com/example_company-org/example_company-triage)
