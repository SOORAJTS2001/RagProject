---
title: 'Example Company CI Events Proposal 3: Using the .example_company/ci/events folder'
toc_hide: true
---

In this proposal we want to create separate files for each group of events. We
can define events in the following format:

```yaml
# .example_company/ci/events/package-published.yml

spec:
  events:
    - name: package/published
---
include:
  - local: .example_company-ci.yml
    with:
      event: $[[ example_company.event.name ]]
```

And in the `.example_company-ci.yml` file, we can use the input;

```yaml
# .example_company-ci.yml

spec:
  inputs:
    event:
      default: push
---
job1:
  script: echo "Hello World"

job2:
  script: echo "Hello World"

job-for-package-published:
  script: echo "Hello World"
  rules:
    - if: $[[ inputs.event ]] == "package/published"
```

When an event happens;

1. We'll enqueue a new job for the event.
1. The job will search for the event file in the `.example_company/ci/events` folder.
1. The job will run `Ci::CreatePipelineService` for the event file.

## Problems & Questions

1. For every defined event run, we need to enqueue a new job.
1. Every event-job will need to search for files.
1. This would be only for the project-scope events.
1. This will not work for Example Company.com scale.
