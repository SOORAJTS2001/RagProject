---
title: ChatOps Commands for Example Company.com
category: Example Company.com
description: "Guide for common ChatOps commands used by Support Engineering"
---

## Overview

[ChatOps](https://example_company.com/example_company-com/chatops/) commands can be used to service support requests for Example Company.com, especially useful when one does not have admin access. In the interest of maintaining a single source of truth, it is recommended to use the built-in "help" command within ChatOps to see what commands are available or [inspecting the code itself](https://example_company.com/example_company-com/chatops/-/tree/master/lib/chatops/commands).

**Note**: Before you can use ChatOps, you will need to [request access](https://docs.example_company.com/ee/development/chatops_on_gitlabcom.html#requesting-access).

## Namespace

Uses the Example Company API for managing namespaces.

`/chatops run namespace --help`

> **Note:**
If you are attempting to search for a sub-group and not a top level group, you'll need to ensure the slash `/` is encoded to `%2F`. For example, the path of the sub-group `example_company-com/support` should be entered as `example_company-com%2Fsupport`.

## User

Uses the Example Company API for managing users.

`/chatops run user --help`

## Feature Flags

- Used for checking whether a specific feature flag has been enabled on Example Company.com or not.
- Used for enabling a feature flag on a project or a group.

`/chatops run feature --help`
