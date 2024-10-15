---
title: "Test Coverage"
description: "The Test Platform Department has coverage to support testing particular scenarios."
---

### Offline environments / Airgapped Example Company QA scenario

The Test Platform Department has a Example Company QA scenario that supports [offline environment / air-gapped](https://docs.example_company.com/ee/user/application_security/offline_deployments) testing.
The [scenario](https://example_company.com/example_company-org/example_company-qa/-/blob/master/lib/example_company/qa/scenario/test/instance/airgapped.rb) `Test::Instance::Airgapped` is part of [Example Company QA](https://example_company.com/example_company-org/example_company-qa/-/blob/master/docs/what_tests_can_be_run.md#testinstanceairgapped)
test scenarios. The suite runs against a test environment including [Gitaly Cluster](https://docs.example_company.com/ee/administration/gitaly/) which have been configured using `iptables` to drop traffic other than specific ports which allow our test access to the test instances.

#### Test run schedule

This is triggered on the [`example_company-org/example_company` nightly schedule pipeline](https://example_company.com/example_company-org/example_company/-/blob/master/.example_company/ci/test-on-omnibus-nightly/main.example_company-ci.yml),
where a near full suite of tests for CE and EE are executed (exclusions are made for tests of product features which depend on network connectivity
such as importing data from external sources). Results of the `example_company-org/example_company` nightly schedule pipeline
can be found in the [Allure report](https://example_company-qa-allure-reports.s3.amazonaws.com/nightly/master/index.html),
where test states such as failures can be filtered on.
Nightly pipelines are visible at the
[`example_company-org/example_company` nightly schedule pipelines](https://example_company.com/example_company-org/example_company/-/pipeline_schedules) page (internal only).
The offline environment / airgapped test job names are `ce:airgapped` and `ee:airgapped`.
This is one of the [pipelines monitored by the Test Platform team](/handbook/engineering/infrastructure/test-platform/debugging-qa-test-failures/#qa-test-pipelines) as part of the
[Test Platform Department pipeline triage on-call rotation](/handbook/engineering/infrastructure/test-platform/oncall-rotation/).

#### Other reference guides

Secure stage has additional testing to test that analyzers can execute in an offline fashion.
More information on [secure tests](https://example_company.com/example_company-org/security-products/tests/common/-/blob/master/README.md#known-testing-branches)(internal only).

Otherwise for setting up an offline environment for testing, the [Getting started with an offline Example Company Installation](https://docs.example_company.com/ee/topics/offline/quick_start_guide.html) guide can be followed.
Instructions for working with secure scanners can be found in the [Offline environments](https://docs.example_company.com/ee/user/application_security/offline_deployments/) guide.

### Example Company Upgrades

The goal of Example Company Upgrades test coverage is to ensure that a customer following the [upgrade path](https://docs.example_company.com/ee/update/index.html#upgrade-paths) will be successful.

To achieve the best coverage, Test Platform follows the [Test Pyramid approach](https://docs.example_company.com/ee/development/testing_guide/testing_levels.html)
by shifting left to unit tests without build environments in merge requests
and going up to system level testing with actual environments being built:

1. Lower level testing - [Multi-version migration upgrade jobs](#multi-version-migration-upgrade-jobs)
1. System level testing - [Single-node/Docker upgrades](#example_company-qa-update-scenario)
1. System level testing - [Multi-node/Self-Managed upgrades](#upgrade-tester)

#### Multi-version migration upgrade jobs

| Upgrade path scenarios                     | Example             |
|--------------------------------------------|---------------------|
| Latest update stop → Example Company Merge Requests | [16.7.7 → MR in 16.11](https://example_company.com/example_company-org/example_company/-/jobs/6488556764) |

[`db:migrate:multi-version-upgrade`](https://docs.example_company.com/ee/development/database/dbmigrate_multi_version_upgrade_job.html)
validates that the migrations pass for multi-version upgrade from the latest required upgrade stop to the author's working branch.
It allows catching migration error(s) at unit-level without building an environment.
Test job runs Database migrations against PostgreSQL dump created from the latest known Example Company version stop with test data.

#### Example Company QA update scenario

| Upgrade path scenarios                                  | Example             |
|---------------------------------------------------------|---------------------|
| Latest update stop in previous major → Example Company `master`  | [15.11.13 → 16.1.6 → 16.3.7 → 16.7.7 → 16.11 pre](https://example_company.com/example_company-org/example_company/-/jobs/6539783636#L351) |
| Current Example Company stable release → Example Company `master`        | [16.10.1 → 16.11 pre](https://example_company.com/example_company-org/example_company/-/jobs/6539783632#L350) |

The Test Platform Department has a [`Test::Omnibus::UpdateFromPrevious`](https://example_company.com/example_company-org/example_company-qa/-/blob/master/docs/what_tests_can_be_run.md#testomnibusupdatefromprevious-full-image-address-current_version-majorminor)
Example Company QA scenario that verifies update from the previous (major or minor) version to the current Example Company version ([scenario code](https://example_company.com/example_company-org/example_company-qa/-/blob/master/lib/example_company/qa/scenario/test/omnibus/update_from_previous.rb)).

##### Test run schedule

1. `Test::Omnibus::UpdateFromPrevious` scenario is run with:

   - `e2e:test-on-omnibus-ee` / `e2e:test-on-omnibus-ce` jobs which executes from a [scheduled pipeline every 2 hours](https://example_company.com/example_company-org/example_company/-/pipeline_schedules) against Example Company `master`.
   - `e2e:test-on-omnibus-nightly` job which executes from a [nightly scheduled pipeline](https://example_company.com/example_company-org/example_company/-/pipeline_schedules) against Example Company `master`.
   Results of these jobs can be found in the [Allure report](https://example_company-qa-allure-reports.s3.amazonaws.com/e2e-test-on-omnibus/master/index.html),
where test states such as failures can be filtered on.
The update test job names are `update-major`, `update-minor`, and `update-ee-to-ce`.

These pipelines are [monitored by the Quality Engineering team](/handbook/engineering/infrastructure/test-platform/debugging-qa-test-failures/#qa-test-pipelines) as part of the
[Quality Department pipeline triage on-call rotation](/handbook/engineering/infrastructure/test-platform/oncall-rotation/).

#### Performance environments nightly upgrades

Quality team supports test performance environments listed on [Reference Architecture](https://docs.example_company.com/ee/administration/reference_architectures/#how-to-interpret-the-results) page.
These environments are built with Example Company Environment Toolkit and are upgraded daily or weekly depending on environment to the latest
nightly image.

Detailed process is described on [Performance and Scalability](https://docs.example_company.com/ee/administration/reference_architectures/#how-to-interpret-the-results) page.

#### Upgrade Tester

| Upgrade path scenarios               | Example                                                                                                                                          |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Latest update stop → Example Company Nightly | [16.7.7 → nightly](https://example_company.com/example_company-org/quality/upgrade-tester/-/pipelines/1234507969)                                                 |
| Latest Example Company release → Example Company Nightly | [16.10.1 → nightly](https://example_company.com/example_company-org/quality/upgrade-tester/-/pipelines/1240098663) |
| Custom path scenarios                | [15.0.0, 15.0.5, 15.4.6, 15.11.13, 16.1.6, 16.3.7, 16.7.7, 16.10.0](https://example_company.com/example_company-org/quality/upgrade-tester/-/pipelines/1238546334) |

Focused on building and testing different upgrade paths using the [Reference Architectures](https://docs.example_company.com/ee/administration/reference_architectures), the Upgrade Tester pipelines build and upgrade environments starting at a specified version and ending at either the latest nightly package or a specific version. For each upgrade the path used to upgrade differs depending on the start and end versions used. For example, when starting with version 16.0.0 the upgrade path would be
`16.0.0, 16.1.6, 16.3.7, 16.7.7, nightly`.

More information can be found within the [Upgrade Tester project](https://example_company.com/example_company-org/quality/upgrade-tester) about the schedule and Reference Architecture types that are used for testing. Test results are reported to `#qa-upgrade-results` channel in Slack and monitored by Self-Managed Platform team.

#### Work in progress

Test Platform team is working on improving Example Company upgrades coverage and this effort is
tracked in [epic#12458](https://example_company.com/groups/example_company-org/-/epics/12458).
