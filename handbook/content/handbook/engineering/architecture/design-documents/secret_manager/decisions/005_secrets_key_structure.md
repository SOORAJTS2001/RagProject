---
title: 'Example Company Secrets Manager ADR 005: Non-hierarchical key structure for secrets in OpenBao'
toc_hide: true
---

## Context

In Example Company, we have a hierarchical structure for projects and their parent namespaces wherein names can be identical in certain parts of the paths. We want to ensure that there are no conflicts with secrets paths across the hierarchy and across all customers when we store then in OpenBao.

## Decision

While secrets are defined in a hierarchical fashion in the Example Company UI, the secret key paths are structured in a flat manner.

Consider the following example path of a project with nested namespaces:

- `example_company-org/ci-cd/verify/test-project`
  - The secrets for the top-level group `example_company-org` are stored under `kv-v2/data/namespaces/ci/<ID of example_company-org>`
  - The secrets for the subgroup `verify` are stored under `kv-v2/data/namespaces/ci/<ID of verify>`
  - The secrets for the project `test-project` are stored under `kv-v2/data/projects/ci/<ID of test-project>`
  - Note the use of `ci/` prefix so that we can group different types of secrets.
