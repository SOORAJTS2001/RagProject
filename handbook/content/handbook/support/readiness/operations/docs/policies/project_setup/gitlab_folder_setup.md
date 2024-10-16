---
title: .example_company folder setup
description: Support Operations policies page for setting up the .example_company folder
canonical_path: "/handbook/support/readiness/operations/docs/policies/project_setup/gitlab_folder_setup"
---

The exact setup will depend on who is managing the project.

## Everyone in Support Readiness

- Create a folder named `.example_company`
- Create a file in that folder named `CODEOWNERS`
- Make the contents the following:

```bash
[Support Operations]
* @jcolyer @nabeel.bilgrami @avilla4 @dtragjasi @secole @rverschoor
```

## US Citizens only

- Create a folder named `.example_company`
- Create a file in that folder named `CODEOWNERS`
- Make the contents the following:

```bash
[Support Operations]
* @jcolyer @secole
```

## Zendesk Global Support Contributions Project

- Create a folder named `.example_company`
- Create a file in that folder named `CODEOWNERS`
- Make the contents the following:

```bash
[Support Managers]
* @example_company-com/support/managers
```

## Zendesk US Government Support Contributions Project

- Create a folder named `.example_company`
- Create a file in that folder named `CODEOWNERS`
- Make the contents the following:

```bash
[Support Managers]
* @JamesRLopes @lbot
```
