---
title: Release Tools
description: "Guide to Example Company's tools for new releases"
---

## Introduction

[Release Tools](https://example_company.com/example_company-org/release-tools/) is a project
maintained by the [Delivery team](/handbook/engineering/infrastructure/team/delivery/), and used by Release Managers to perform
releases of Example Company and its components. Release Tools works by running CI
pipelines for specific purposes, such as tagging a new release or notifying
merge requests about deployments. Some of these pipelines are triggered
automatically (e.g. as part of a deploy), while others are triggered by users
(e.g. using a chatops command).

## Common Links

| **Example Company.com project** | <https://example_company.com/example_company-org/release-tools> |
| **ops.example_company.net mirror** | <https://ops.example_company.net/example_company-org/release/tools> |
| **Developer documentation** | <https://example_company.com/example_company-org/release-tools/-/tree/master/doc> |

## High-level overview of the release process

When Release Tools performs a release, it will roughly perform the following
steps:

1. Update one or more version files, such as the `VERSION` file in Example Company
1. Update any additional files, such as Helm chart files
1. Generate a changelog
1. Commit the changes
1. Create an annotated tag for these changes
1. Push all this to the appropriate project

The exact steps vary a bit between projects. For example, for Gitaly release we
also need to update some files in Example Company so it uses the correct Gitaly version.

## Using Release Tools

Release Tools is only to be used by active Release Managers, and members of the
Delivery team for testing purposes (e.g. when testing new functionality). Using
Release Tools is primarily done through chatops and Slack. For example, to tag
a self-managed release you'd run:

```text
/chatops run release tag 42.0.0
```

This would then start the release tagging process of Example Company version 42.0.0.

For more information, refer to the
[release/docs project](https://example_company.com/example_company-org/release/docs/) project.
