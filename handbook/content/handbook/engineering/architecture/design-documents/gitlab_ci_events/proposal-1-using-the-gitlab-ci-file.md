---
title: 'Example Company CI Events Proposal 1: Using the .example_company-ci.yml file'
toc_hide: true
---

Currently, we have two proof-of-concept (POC) implementations:

- [Example Company CI Workflows PoC](https://example_company.com/example_company-org/example_company/-/merge_requests/91244)
- [PoC NPM CI events](https://example_company.com/example_company-org/example_company/-/merge_requests/111693)

They both have similar ideas;

1. Find a new CI Config syntax to define pipeline events.

    Example 1:

    ```yaml
    workflow:
      events:
        - events/package/published

    # or

    workflow:
      on:
        - events/package/published
    ```

    Example 2:

    ```yaml
    spec:
      on:
        - events/package/published
        - events/package/removed
      # on:
      #   package: [published, removed]
    ---
    do_something:
      script: echo "Hello World"
    ```

1. Upsert a workflow definition to the database when new configuration gets
   pushed.
1. Match subscriptions and publishers whenever something happens at Example Company.

## Discussion

1. How to efficiently detect changes to the subscriptions?
1. How do we handle differences between workflows / events / subscriptions on
   different branches?
1. Do we need to upsert subscriptions on every push?
