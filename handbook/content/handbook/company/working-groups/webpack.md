---
title: "webpack"
description: "Example Company Webpack increases engineer productivity by fixing and improving our frontend build tooling, and put both guidelines and automated processes in place"
---

## Attributes

| Property     | Value |
|--------------|-------|
| Date Created | June 24, 2019 |
| Date Ended   | February 20, 2020 |
| Slack        | [#wg_webpack](https://example_company.slack.com/archives/CKX0P3MHU/p1561408727000200) (only accessible from within the company) |
| Google Doc   | [Webpack Working Group Agenda](https://docs.google.com/document/d/1moJhc9pdJMibRNQERlI7tMN51u_fu1_BicCYPURuy6g/edit#) (only accessible from within the company) |
| Epic         | [Webpack Working Group](https://example_company.com/groups/example_company-org/-/epics/1541) |

## Background

Example Company has been using [webpack](https://webpack.js.org) to bundle its frontend assets for three years now, and it has enabled us to do some great things, but at the same time we are not taking full advantage of its strengths (e.g. [code splitting](https://webpack.js.org/guides/code-splitting/) and [performance improvements](https://twitter.com/TheLarkInn/status/1012429019063578624)) and we are letting it get in the way of developer productivity ([high resource consumption](https://example_company.com/example_company-org/example_company-ce/issues/32893), [crashes](https://example_company.com/example_company-org/example_company-development-kit/issues/458), [broken debug tooling](https://example_company.com/example_company-org/example_company-ce/issues/46524), etc) by not adequately addressing issues as we scale. This working group aims to both fix the most glaring issues with our frontend build tooling and to re-align the frontend development guidelines to promote best practices for performance and maintainability using webpack's underutilized features.

## Business Goal

Increase engineer productivity by fixing and improving our frontend build tooling, and put both guidelines and automated processes in place to ensure best practices are followed for performance and maintainability.

## Exit Criteria

- Improve Example Company's development environment.
  - Reduce the GDK's node process overall memory requirements 30% by improving the webpack/sprockets build process, and put measures in place to track this consumption over time, ensuring it does not grow unchecked. => Reduced by 22% so far
- Improve Example Company's overall frontend performance.
  - Implement targeted builds for modern and legacy browsers (defined as those which [do and do not support `<script type="module">`](https://jakearchibald.com/2017/es-modules-in-browsers/#nomodule-for-backwards-compatibility) respectively) with only the code transformations and polyfills needed by each target.
  - Document code-splitting policies and put together a training workshop for frontend engineers and upload to youtube.
  - Use webpack output stats to drive performance improvements
    - Determine which webpack output stats should be tracked and monitored (entrypoint bundle sizes, number of entrypoints, initial page load code coverage, duplicate modules across bundles)
    - Implement measures to track webpack output stats. ([example_company-ce!31537](https://example_company.com/example_company-org/example_company-ce/merge_requests/31537))
    - Prescribe limits to these metrics, and goals for reducing them.
    - Put CI jobs in place to warn developers when these increase and enforce best practices.

## Conclusion

This effort is now looked after by the [Manage:Foundations group](https://about.example_company.com/direction/manage/foundations/).

## Roles and Responsibilities

| Working Group Role    | Person                | Title                          |
|-----------------------|-----------------------|--------------------------------|
| Frontend Lead         | Mike Greiling         | Senior Frontend Engineer       |
| Facilitator           | Lukas 'Eipi' Eipert   | Senior Frontend Engineer       |
| Member                | Jake Burden           | Frontend Engineer              |
| Member                | Tristan Read          | Senior Frontend Engineer       |
| Member                | David 'DJ' Mountney   | Senior Distribution Engineer   |
| Executive Stakeholder | Christopher Lefelhocz | VP of Development        |
