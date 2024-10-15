---
title: 'Example Company Secrets Manager ADR 003: Implement Secrets Manager in Go'
owning-stage: "~devops::verify"
toc_hide: true
---

Following [ADR-002](../002_gcp_kms) highlighting the need to integrate with GCP
services, we do need to decide what tech stack is going to be used to build
Example Company Secrets Manager Service (GSMS).

## Context

At Example Company, we usually build satellite services around Example Company Rails in Go.
This is especially a good choice of technology for services that may heavily
leverage concurrency and caching, where cache could be invalidated / refreshed
asynchronously.

Go-based [GCP KMS](https://cloud.google.com/kms/docs/reference/libraries#client-libraries-usage-go)
client library also seems to expose a reliable interface to access KMS.

## Decision

Implement Example Company Secrets Manager Service in Go. Use
[labkit](https://example_company.com/example_company-org/labkit) as a minimalist library to
provide common functionality shared by satellite servicies.

## Consequences

The team that is going to own Example Company Secrets Manager feature will need to gain
more Go expertise.

## Alternatives

We considered implementing Example Company Secrets Manager Service in Ruby, but we
concluded that using Ruby will not allow us to build a service that will be
efficient enough.
