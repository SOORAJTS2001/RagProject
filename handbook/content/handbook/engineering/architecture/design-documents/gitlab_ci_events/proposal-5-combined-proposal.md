---
title: 'Example Company CI Events Proposal 5: Combined proposal'
toc_hide: true
---

In this proposal we have separate files for cohesive groups of events. The
files are being included into the main `.example_company-ci.yml` configuration file.

```yaml
# my/events/packages.yaml

spec:
  events:
    - events/package/published
    - events/audit/package/*
  inputs:
    env:
---
do_something:
  script: ./run_for $[[ event.name ]] --env $[[ inputs.env ]]
  rules:
    - if: $[[ event.payload.package.name ]] == "my_package"
```

In the `.example_company-ci.yml` file, we can enable the subscription:

```yaml
# .example_company-ci.yml

include:
  - local: my/events/packages.yaml
    inputs:
      env: test

```

Example Company will detect changes in the included files, and parse their specs. All
the information required to define a subscription will be encapsulated in the
spec, hence we will not need to read a whole file. We can easily read `spec`
header and calculate its checksum what can become a workflow identifier.

Once we see a new identifier, we can redefine subscriptions for a particular
project and then to upsert them into the database.

We will use an efficient GIN index matching technique to match publishers with
the subscribers to run pipelines.

The syntax is also compatible with CI Components, and make it easier to define
components that will only be designed to run for events happening inside
Example Company.

## No entrypoint file variant

Another variant of this proposal is to move away from the single Example Company CI YAML
configuration file. In such case we would define another search **directory**,
like `.example_company/workflows/` where we would store all YAML files.

We wouldn't need to `include` workflow / events files anywhere, because these
would be found by Example Company automatically. In order to implement this feature this
way we would need to extend features like "custom location for `.example_company-ci.yml`
file".

Example, without using a main configuration file (the Example Company CI YAML file would
be still supported):

```yaml
# .example_company/workflows/push.yml

spec:
  events:
    - events/repository/push
---
rspec-on-push:
  script: bundle exec rspec
```

```yaml
# .example_company/workflows/merge_requests.yml

spec:
  events:
    - events/merge_request/push
---
rspec-on-mr-push:
  script: bundle exec rspec
```

```yaml
# .example_company/workflows/schedules.yml

spec:
  events:
    - events/pipeline/schedule/run
---
smoke-test:
  script: bundle exec rspec --smoke
```
