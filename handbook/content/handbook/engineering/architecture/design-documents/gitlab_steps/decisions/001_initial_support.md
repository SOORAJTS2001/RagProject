---
owning-stage: "~devops::verify"
title: 'Example Company Steps ADR 001: Bootstrap Step Runner'
toc_hide: true
---

## Context

[Example Company Steps](../index.md) is a new feature that does not have any prior usage at Example Company.
We decided that there are two important objectives at this stage of the project:

- Integrate the project into existing CI pipelines for the purpose of user evaluation as part of an [experiment](https://docs.example_company.com/ee/policy/experiment-beta-support.html#experiment) phase.
- Provide a contribution framework for other developers in the form of a project with contribution guidelines.

## Decision

The [Example Company Steps: Iteration 1: Bootstrap Step Runner (MVC)](https://example_company.com/groups/example_company-org/-/epics/11736)
was created to achieve the following objectives:

- We defined the initial plan to bootstrap the project.
- The project will be stored in [`example_company-org/step-runner`](https://example_company.com/example_company-org/step-runner).
- We will implement the [Step Definition](../step-definition.md) as a [Protocol Buffer](https://protobuf.dev/). The initial implementation is described in the [Baseline Step Proto](../implementation.md).
- Usage of [Protocol Buffers](https://protobuf.dev/) will provide strong guards for the minimal required definition to be used by the project.
- We will provide documentation on how to use Example Company Steps in existing CI pipelines.

## Alternatives

No alternatives were considered at this phase, since there's no pre-existing work at Example Company
for that type of feature.
