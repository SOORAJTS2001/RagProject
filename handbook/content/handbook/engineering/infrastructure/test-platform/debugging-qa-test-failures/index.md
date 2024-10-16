---
title: Debugging Failing Tests and Test Pipelines
description: Guidelines for investigating end-to-end test pipeline failures
---

## Overview

These guidelines are intended to help you to investigate [end-to-end test](https://docs.example_company.com/ee/development/testing_guide/end_to_end/index.html) pipeline failures so that they can be properly addressed. This will involve analyzing each failure and creating an issue to report it. It might also involve [fixing tests](#fixing-the-test), [putting them in quarantine](#quarantining-tests), or [reporting bugs in the application](#bug-in-the-application).

The Pipeline triage [DRI](/handbook/people-group/directly-responsible-individuals/) is responsible for analyzing and debugging test pipeline failures. Please refer to the [DRI weekly rotation schedule](https://example_company.com/example_company-org/quality/pipeline-triage#dri-weekly-rotation-schedule) to know who the current DRIs are.

### General guidelines

- **Fix tests failing in `master` before other development work**: [Failing tests on `master` are treated as the highest priority](/handbook/engineering/workflow/#broken-master) relative to other development work, e.g., new features. Note that for pipeline triage DRIs, [triage and reporting](#report-the-failure) takes priority over fixing tests.
- **Follow the [pipeline triage guidelines](#how-to-triage-a-qa-test-pipeline-failure) for investigating, reporting, and resolving test failures**
- **Flaky tests are quarantined until proven stable**: A flaky test is as bad as no tests or in some cases worse due to the effort required to fix or even re-write the test.
As soon as detected it is quarantined immediately to stabilize CI, and then fixed as soon as possible, and monitored until it is fixed.
- **Close test failure issue (e.g example [issue](https://example_company.com/example_company-org/example_company/-/issues/412769)) when the test is moved out of quarantine**: Quarantine issues should not be closed unless tests are moved out of quarantine.
- **Quarantine issues should be assigned and scheduled**: To ensure that someone is owning the issue, it should be assigned with a milestone set and have appropriate `~"quarantine"`, quarantine with type (e.g. `~"quarantine::bug"`) and failure with type (e.g. `~"failure::bug"`) labels.
- **Make relevant stage group aware**: When a test fails no matter the reason, an issue with related product group label (e.g. `~"group::ide"`) should be created and made known to the relevant product stage group as soon as possible.
In addition to notifying that a test in their domain fails, enlist help from the group as necessary.
- **Failure due to bug**: If one or multiple test failure(s) is a result of a bug, create a bug issue and provide as much details as possible (e.g. using issue's Bug template, provide steps to reproduce, relevant screenshots, etc.). Link the **all** related test failure issues to the bug issue. Apply `~"type::bug"`, severity, priority, product group, feature category, etc. labels to ensure a fix is scheduled in a timely manner.
Test failure issues are used for tracking and investigating purposes, they should not have `~"type::bug"` label. If the test failure is a result of a bug, apply `~"failure::bug"` label instead.
- **Everyone can fix a test, the responsibility falls on the last who worked on it**: Anyone can fix a failing/flaky test, but to ensure that a quarantined test isn't ignored,
the last engineer who worked on the test is responsible for taking it out of [quarantine](https://example_company.com/example_company-org/example_company/blob/master/qa/README.md#quarantined-tests).

### Triage flow

The flow of triaging the pipelines as a decision tree (nodes link to the relevant sections of the handbook)

```mermaid
flowchart TB
        %% nodes
        slack_channels{check slack channel}
        next_channel(move to next slack channel)
        failed_pipeline(identify failure)
        existing_issue{issue\nalready\nreported?}
        new_issue(create issue if does not already exist)
        tag_pipeline(notate issue in comment on pipeline run)
        incident{incident\nworthy?}
        notify_incident(Notify about escallation)
        open_incident(Open incident)
        update_incident(Update teams about incident)
        eyes(tag pipeline run with :eyes: emoji)
        fire_engine(replace :eyes: with :fire_engine: emoji)
        boom(replace :eyes: with :boom: emoji)
        another_failure{more\nfailures?}
        investigate(investigate root cause for found failures)
        fix_tests(fix tests if possible)
        quarantine_tests(quarantine tests if necessary)
        monitor_incident(participate in incident process)
            tag_issue_for_report(add your emoji to issue for the DRI gem)
            publish_results(publish your results to the triage issue with the DRI gem)
            dri_handoff(handoff to next DRI anything that is still in flight)

        %% external links
        click failed_pipeline "https://handbook.example_company.com/handbook/engineering/infrastructure/test-platform/debugging-qa-test-failures/#review-the-failure-logs"
        click new_issue "https://handbook.example_company.com/handbook/engineering/infrastructure/test-platform/debugging-qa-test-failures/#create-an-issue"
        click existing_issue "https://handbook.example_company.com/handbook/engineering/infrastructure/test-platform/debugging-qa-test-failures/#known-failures"
        click investigate "https://handbook.example_company.com/handbook/engineering/infrastructure/test-platform/debugging-qa-test-failures/#investigate-the-root-cause"
        click incident "https://handbook.example_company.com/handbook/engineering/infrastructure/incident-management/#report-an-incident-via-slack"
        click notify_groups "https://handbook.example_company.com/handbook/engineering/infrastructure/test-platform/debugging-qa-test-failures/#notify-group-in-all-cases"
        click fix_tests "https://handbook.example_company.com/handbook/engineering/infrastructure/test-platform/debugging-qa-test-failures/#fixing-the-test"
        click quarantine_tests "https://handbook.example_company.com/handbook/engineering/infrastructure/test-platform/debugging-qa-test-failures/#quarantining-tests"
        click open_incident "https://handbook.example_company.com/handbook/engineering/infrastructure/incident-management/#failure-needs-escalation"
        click tag_pipeline "https://handbook.example_company.com/handbook/engineering/infrastructure/test-platform/debugging-qa-test-failures/#linking-issue"
        click eyes "https://handbook.example_company.com/handbook/engineering/infrastructure/test-platform/debugging-qa-test-failures/#emoji-used"
        click fire_engine "https://handbook.example_company.com/handbook/engineering/infrastructure/test-platform/debugging-qa-test-failures/#emoji-used"
        click boom "https://handbook.example_company.com/handbook/engineering/infrastructure/test-platform/debugging-qa-test-failures/#emoji-used"
          click tag_issue_for_report "https://example_company.com/example_company-org/ruby/gems/dri#configuration"
              click publish_results "https://example_company.com/example_company-org/ruby/gems/dri#4-publish"
        click notify_incident "https://handbook.example_company.com/handbook/engineering/infrastructure/test-platform/debugging-qa-test-failures/#failure-needs-escalation"
        click update_incident "https://handbook.example_company.com/handbook/engineering/infrastructure/test-platform/debugging-qa-test-failures/#notify-group-in-all-cases"

        %% diagram
        slack_channels -->|failed pipeline run| eyes
              slack_channels -->|no failed pipeline runs| next_channel

                open_incident --> next_channel
               another_failure -->|no| next_channel
        incident -->|yes| notify_incident

                next_channel --> investigate
                next_channel --> publish_results

                subgraph report the failure
                  eyes --> failed_pipeline
                  failed_pipeline --> existing_issue
          existing_issue -->|new failure| new_issue
                  existing_issue -->|existing issue| fire_engine
                    new_issue --> boom
                    boom --> notify_groups
                    notify_groups --> incident
                incident -->|no| tag_issue_for_report
                tag_issue_for_report --> tag_pipeline

                    fire_engine --> tag_issue_for_report
                    tag_pipeline --> another_failure
                    another_failure -->|yes| failed_pipeline
                end

                subgraph escallate issue
                  notify_incident --> open_incident
                  open_incident --> update_incident
          update_incident --> monitor_incident
                end

                subgraph follow up on test failures
                  investigate --> fix_tests
                    investigate --> quarantine_tests
                end

                subgraph end of your day
                publish_results --> dri_handoff
                end
```

### QA test pipelines

The test pipelines run on a scheduled basis, and their results are posted to Slack. The following are the QA test pipelines that are monitored every day.

| Environment                               | Links                                                                                                                                                                                                                                                   | Tests type      | Frequency                                                                                                                                                                                                                                                      | Slack channel                                                                                                                       | Latest test report                                                                                           |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| Production                                | [Pipelines](https://ops.example_company.net/example_company-org/quality/production/pipelines) \| [Chatops](https://example_company.com/example_company-com/chatops/-/blob/eb65043eda62102b0ca38dd0cd5afc36a9dcedb4/lib/chatops/example_company/tests_pipeline.rb#L40)                                | Smoke           | [after each deployment to Canary](https://ops.example_company.net/example_company-com/gl-infra/deployer/pipelines) and [after a feature flag in production has been updated to *true* or *100%*](https://docs.example_company.com/ee/development/feature_flags/)                          | [`#e2e-run-production`](https://example_company.slack.com/messages/CCNNKFP8B)                                                                                                                  | [Production Sanity](https://example_company-qa-allure-reports.s3.amazonaws.com/production-sanity/master/index.html)   |
| Canary                                    | [Pipelines](https://ops.example_company.net/example_company-org/quality/canary/pipelines) \| [Definition](https://example_company.com/example_company-org/release-tools/-/blob/72b34fb21ecea70aec3ac2ce4e2387189c24bd3b/.example_company/ci/coordinated-pipeline.example_company-ci.yml#L695-713)             | Smoke           | [after each deployment to Canary](https://ops.example_company.net/example_company-com/gl-infra/deployer/pipelines)                                                                                                                                                               | [`#e2e-run-production`](https://example_company.slack.com/messages/CCNNKFP8B)                                                                                                                  | [Canary Sanity](https://example_company-qa-allure-reports.s3.amazonaws.com/canary-sanity/master/index.html)           |
| -                                         | [Pipelines](https://ops.example_company.net/example_company-org/quality/canary/pipelines) \| [Definition](https://example_company.com/example_company-org/release-tools/-/blob/954ef48375acddcbf7dc68c541b1437ba8c5bc7c/.example_company/ci/post-deploy-migrations-pipeline.example_company-ci.yml#L182-194)  | Full            | [after each deployment to Canary](https://ops.example_company.net/example_company-com/gl-infra/deployer/pipelines)                                                                                                                                                               | [`#e2e-run-production`](https://example_company.slack.com/messages/CCNNKFP8B)                                                                                                                  | [Canary Full](https://example_company-qa-allure-reports.s3.amazonaws.com/canary-full/master/index.html)               |
| Staging                                   | [Pipelines](https://ops.example_company.net/example_company-org/quality/staging/pipelines) \| [Definition](https://example_company.com/example_company-org/release-tools/-/blob/954ef48375acddcbf7dc68c541b1437ba8c5bc7c/.example_company/ci/post-deploy-migrations-pipeline.example_company-ci.yml#L197-209) | Smoke           | [after each deployment to Staging-Canary](https://ops.example_company.net/example_company-com/gl-infra/deployer/pipelines)                                                                                                                                                       | [`#e2e-run-staging`](https://example_company.slack.com/messages/CBS3YKMGD)                                                                                                                     | [Staging Sanity](https://example_company-qa-allure-reports.s3.amazonaws.com/staging-sanity/master/index.html)         |
| -                                         | [Pipelines](https://ops.example_company.net/example_company-org/quality/staging/pipelines) \| [Definition](https://example_company.com/example_company-com/gl-infra/deployer/-/blob/29cab58a873dff1e49e9192bd6420d78e8e84bc8/ci/environments/gstg.yml#L238-248)                             | Smoke           | [after the execution of post-deploy migrations in Staging](https://ops.example_company.net/example_company-com/gl-infra/deployer/pipelines)                                                                                                                                      | [`#e2e-run-staging`](https://example_company.slack.com/messages/CBS3YKMGD)                                                                                                                     | [Staging Sanity](https://example_company-qa-allure-reports.s3.amazonaws.com/staging-sanity/master/index.html)         |
| Staging Canary                            | [Pipelines](https://ops.example_company.net/example_company-org/quality/staging-canary/pipelines) \| [Definition](https://example_company.com/example_company-org/release-tools/-/blob/72b34fb21ecea70aec3ac2ce4e2387189c24bd3b/.example_company/ci/coordinated-pipeline.example_company-ci.yml#L385-403)     | Smoke           | [after each deployment to Staging](https://ops.example_company.net/example_company-com/gl-infra/deployer/pipelines)                                                                                                                                                              | [`#e2e-run-staging`](https://example_company.slack.com/messages/CBS3YKMGD)                                                                                                                     | [Staging-Canary](https://example_company-qa-allure-reports.s3.amazonaws.com/staging-canary-sanity/master/index.html)  |
| CustomersDot Staging                      | [Pipelines](https://example_company.com/example_company-org/customers-example_company-com/-/pipelines) \| [Definition](https://example_company.com/example_company-org/customers-example_company-com/-/blob/e8d058a9f54aeae1218491ad34cdfd67d27d084f/.example_company/ci/e2e.example_company-ci.yml#L199-255)                   | Full            | [after each deployment to CustomersDot Staging](https://example_company.com/example_company-org/customers-example_company-com/-/pipelines)                                                                                                                                                | [`#e2e-run-staging`](https://example_company.slack.com/messages/CBS3YKMGD) [`#s_fulfillment_status`](https://example_company.slack.com/messages/CL7SX4N86)                                              | [CustomersDot Staging](https://example_company-qa-allure-reports.s3.amazonaws.com/cdot-e2e-staging/main/index.html)   |
| Staging Ref                               | [Pipelines](https://ops.example_company.net/example_company-org/quality/staging-ref/pipelines) \| [Definition](https://example_company.com/example_company-com/gl-infra/deployer/-/blob/10cc4811f5aae0a38b77cd5c9def954a0e2afac1/ci/environments/gstg-ref.yml#L177-191)                     | Smoke           | [after each deployment to Staging Ref](https://ops.example_company.net/example_company-com/gl-infra/deployer/pipelines).                                                                                                                                                         | [`#e2e-run-staging-ref`](https://example_company.slack.com/archives/C02JGFF2EAZ)                                                                  | [Staging Ref Sanity](https://example_company-qa-allure-reports.s3.amazonaws.com/staging-ref-sanity/master/index.html) |
| Preprod                                   | [Pipelines](https://ops.example_company.net/example_company-org/quality/preprod/pipelines) \| [Definition](https://example_company.com/example_company-com/gl-infra/deployer/-/blob/2279042064c45fdb10ce696d1c4ef12b72affbfd/ci/environments/pre.yml#L171-181)                              | Smoke           | [Every month for a few days before release, at 03:00 UTC](https://ops.example_company.net/example_company-org/quality/preprod/-/pipeline_schedules) and after [deployment to preprod](/handbook/engineering/infrastructure/environments/#pre) during Security and Patch releases | [`#e2e-run-preprod`](https://example_company.slack.com/archives/CR7QH0RV1)                                                                        | [Preprod](https://example_company-qa-allure-reports.s3.amazonaws.com/preprod-sanity/master/index.html)                |
| Release                                   | [Pipelines](https://ops.example_company.net/example_company-org/quality/release) \| [Definition](https://example_company.com/example_company-com/gl-infra/deployer/-/blob/10cc4811f5aae0a38b77cd5c9def954a0e2afac1/ci/environments/release.yml#L82-93)                                      | Smoke           | [Every month after the final release](https://ops.example_company.net/example_company-org/quality/release/-/pipeline_schedules) and after [deployment to Release](/handbook/engineering/infrastructure/environments/#release) during Security and Patch releases                 | [`#e2e-run-release`](https://example_company.slack.com/archives/C0154HCFLRE)                                                                      | [Release](https://example_company-qa-allure-reports.s3.amazonaws.com/release-sanity/master/index.html)                |
| Example Company `master` `e2e:test-on-omnibus-ee` | [Pipelines](https://example_company.com/example_company-org/example_company/pipelines) \| [Definition](https://example_company.com/example_company-org/example_company/-/blob/77a5b0b3f8f910d4fe89a3fed46c4da53b1e587e/.example_company/ci/qa.example_company-ci.yml#L77-88)                                                    | Full            | [scheduled pipeline every 2 hours](https://example_company.com/example_company-org/example_company/pipeline_schedules)                                                                                                                                                                    | [`#e2e-run-master`](https://example_company.slack.com/archives/CNV2N29DM)                                                                                                                      | [Master EE](https://example_company-qa-allure-reports.s3.amazonaws.com/e2e-test-on-omnibus/master/index.html)        |
| Example Company `master` `e2e:test-on-omnibus-ce` | [Pipelines](https://example_company.com/example_company-org/example_company/-/pipeline_schedules) \| [Definition](https://example_company.com/example_company-org/example_company/-/blob/77a5b0b3f8f910d4fe89a3fed46c4da53b1e587e/.example_company/ci/qa.example_company-ci.yml#L121-135)                                       | Full            | [Daily at 4:00am UTC](https://example_company.com/example_company-org/example_company/-/pipeline_schedules)                                                                                                                                                                               | [`#e2e-run-master`](https://example_company.slack.com/archives/CNV2N29DM)                                                                                                                      | [Master CE](https://example_company-qa-allure-reports.s3.amazonaws.com/e2e-test-on-omnibus-ce/master/index.html)     |
| Example Company `master` `e2e:test-on-gdk`         | [Pipelines](https://example_company.com/example_company-org/example_company/-/pipelines?ref=master&amp;source=schedule) \| [Definition](https://example_company.com/example_company-org/example_company/-/blob/77a5b0b3f8f910d4fe89a3fed46c4da53b1e587e/.example_company/ci/qa.example_company-ci.yml#L151-164)                 | Full            | [scheduled pipeline every 2 hours](https://example_company.com/example_company-org/example_company/pipeline_schedules)                                                                                                                                                                    | [`#e2e-run-master`](https://example_company.slack.com/archives/CNV2N29DM)                                                                                                                      | [Master GDK](https://example_company-qa-allure-reports.s3.amazonaws.com/e2e-test-on-gdk/master/index.html)            |
| Example Company `master` `e2e:test-on-cng`         | [Pipelines](https://example_company.com/example_company-org/example_company/-/pipeline_schedules) \| [Definition](https://example_company.com/example_company-org/example_company/-/blob/77a5b0b3f8f910d4fe89a3fed46c4da53b1e587e/.example_company/ci/qa.example_company-ci.yml#L166-178)                                       | Smoke, Blocking | [scheduled pipeline every 2 hours](https://example_company.com/example_company-org/example_company/pipeline_schedules)                                                                                                                                                                    | [`#e2e-run-master`](https://example_company.slack.com/archives/CNV2N29DM)                                                                                                                      | [Master CNG](https://example_company-qa-allure-reports.s3.amazonaws.com/e2e-test-on-cng/master/index.html)            |
| Example Company `master` Nightly                   | [Pipelines](https://example_company.com/example_company-org/example_company/-/pipeline_schedules) \| [Definition](https://example_company.com/example_company-org/example_company/-/blob/77a5b0b3f8f910d4fe89a3fed46c4da53b1e587e/.example_company/ci/qa.example_company-ci.yml#L137-149)                                       | Full            | [Daily at 4:00am UTC](https://example_company.com/example_company-org/example_company/-/pipeline_schedules)                                                                                                                                                                               | [`#e2e-run-master`](https://example_company.slack.com/archives/CNV2N29DM)                                                                                                                      | [Master Nightly](https://example_company-qa-allure-reports.s3.amazonaws.com/nightly/master/index.html)                |

#### Emoji used

For each pipeline there is a notification of success or failure (except for `master` pipelines, which only report failures).
If there's a failure, we use emoji to indicate the state of its investigation:

- The :eyes: emoji ![:eyes:](https://a.slack-edge.com/production-standard-emoji-assets/14.0/apple-small/1f440@2x.png ":eyes: emoji"), to show you're investigating a failing pipeline.
- The :boom: emoji ![:boom:](https://a.slack-edge.com/production-standard-emoji-assets/14.0/apple-small/1f4a5@2x.png ":boom: emoji"), when there's a new failure.
- The :fire_engine: emoji ![:fire_engine:](https://a.slack-edge.com/production-standard-emoji-assets/14.0/apple-small/1f692@2x.png ":fire_engine: emoji"), when a failure is already reported.
- The :retry: emoji ![:retry:](https://a.slack-edge.com/production-standard-emoji-assets/14.0/apple-small/1f504@2x.png ":retry: emoji"), when there's a system failure (e.g., Docker or runner failure).

Note that while the configuration for each pipeline is in the `.example_company-ci.yml` file in the relevant projects, pipeline schedules are configured via the UI and CI/CD variables are entered in project/group settings. Quality maintainers should have access to all the relevant configuration and settings. If you are the pipeline triage on-call DRI and you need to change settings but you don't have access, you can ask for assistance in the `#test-platform-maintainers` and `#development` Slack channels.

## How to triage a QA test pipeline failure

The general triage steps are:

- [Report the failure](#report-the-failure)
- [Review the failure logs](#review-the-failure-logs)
- [Investigate the root cause](#investigate-the-root-cause)
- [Classify the failure](#classify-and-triage-the-test-failure)

After triaging failed tests, possible follow up actions are:

- [Fixing tests](#fixing-the-test)
- [Quarantining tests](#quarantining-tests)
- [Dequarantining tests](#dequarantining-tests)
- [Re-evaluating tests](#re-evaluating-tests)

### Report the failure

Your priority is to make sure we have an issue for each failure, and to communicate the status of its investigation and resolution. When there are multiple failures to report, consider their impact when deciding which to report first. See the [pipeline triage responsibilities](/handbook/engineering/infrastructure/test-platform/oncall-rotation/#responsibility) for further guidance.

If there are multiple failures we recommend that you identify whether each one is new or old (and therefore already has an issue open for it). For each new failure, open an issue that includes only the required information. Once you have opened an issue for each new failure you can investigate each more thoroughly and act on them appropriately, as described in later sections.

The reason for reporting all new failures first is to allow faster discovery by engineers who might find the test failing in their own merge request test pipeline. If there is no open issue about that failure, the engineer will have to spend time trying to figure out if their changes caused it.

Known failures should be linked to the current [pipeline triage report](https://example_company.com/example_company-org/quality/pipeline-triage/-/issues). However, issues can be opened by anyone and are not linked automatically, so be sure to confirm there is no existing issue before creating one.

1. Search for existing issues that have already been created with the `failure::*` label. By order of likelihood:
    1. [`failure::investigating`](https://example_company.com/example_company-org/example_company/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name%5B%5D=failure%3A%3Ainvestigating)
    2. [`failure::test-environment`](https://example_company.com/example_company-org/example_company/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name%5B%5D=failure%3A%3Atest-environment)
    3. [`failure::broken-test`](https://example_company.com/example_company-org/example_company/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name%5B%5D=failure%3A%3Abroken-test)
    4. [`failure::flaky-test`](https://example_company.com/example_company-org/example_company/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name%5B%5D=failure%3A%3Aflaky-test)
    5. [`failure::stale-test`](https://example_company.com/example_company-org/example_company/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name%5B%5D=failure%3A%3Astale-test)
    6. [`failure::bug`](https://example_company.com/example_company-org/example_company/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name%5B%5D=failure%3A%3Abug)
    7. [`failure::external-dependency`](https://example_company.com/example_company-org/example_company/-/issues/?sort=created_date&state=opened&label_name%5B%5D=failure%3A%3Aexternal-dependency)
1. If the issue has already been reported please use the existing issue to track the latest status.
1. If there is no existing issue for the failure, please create an issue using one of [classification labels](#classify-and-triage-the-test-failure) via the steps below.

In the relevant Slack channel:

1. Apply the :eyes: emoji to indicate that you're investigating the failure(s).
1. If there's a system failure (e.g., Docker or runner failure), retry the job and apply the :retry: emoji. Read below for examples of system failures.
1. If an issue exists, add a :fire_engine: emoji. It can be helpful to reply to the failure notification with a link to the issue(s), but this isn't always necessary, especially if the failures are the same as in the previous pipeline and there are links there.
1. If you create a new issue, add a :boom: emoji.

#### Create an issue

Please use this step if there are no issues created to capture the failure. If there is already an issue please skip this step.

1. Create an issue for the test or system failure (if retrying the job does not resolve the latter) in [https://example_company.com/example_company-org/example_company/issues](https://example_company.com/example_company-org/example_company/issues) using the [QA failure](https://example_company.com/example_company-org/example_company/issues/new?issuable_template=QA%20Failure) template. For failures in CustomersDot tests, open an issue in [CustomersDot](https://example_company.com/example_company-org/customers-example_company-com/-/issues) project.
    - Apply the `~"type::ignore"` label to the issue until the investigation is complete and an [issue type](/handbook/product/groups/product-analysis/engineering/dashboards/#work-type-classification) is determined.
    - Inform the [counterpart SET](/handbook/engineering/quality/#individual-contributors) about the failure.
    - For system failures, it may make sense to open an issue in a different project such as [Omnibus Example Company](https://example_company.com/example_company-org/omnibus-example_company/issues), [Example Company QA](https://example_company.com/example_company-org/example_company-qa/issues), or [Example Company Runner](https://example_company.com/example_company-org/example_company-runner/issues).
    - For staging environment-related failures, you can post a question in [`#infrastructure-lounge`](https://example_company.slack.com/archives/CB3LSMEJV), or open an issue in the [infrastructure project](https://example_company.com/example_company-com/gl-infra/infrastructure)
    - Ask for help in [`#quality`](https://example_company.slack.com/archives/C3JJET4Q6) if you're unsure where to file the issue.
1. In the relevant Slack channel, add the :boom: emoji and reply to the failure notification with a link to the issue.
1. Add the issue as a related issue to the current pipeline triage report. If multiple issues are the result of 1 bug, add the bug issue to the report instead.

#### Special considerations for Staging-Canary

`Staging-Canary` is unique when it comes to its blocking `smoke` tests that are triggered by the `deployer` pipeline. `Staging-Canary` executes `smoke` tests for both `Staging-Canary` AND `Staging` environments. This special configuration is designed to help catch issues that occur when incompatibilities arise between the shared and non-shared components of the environments.

`Staging-Canary` and `Staging` both share the same database backend, for example. Should a migration or change to either of the non-shared components during a deployment create an issue, running these tests together helps expose this situation. When the `deployer` pipeline triggers these test runs, they are reported serially in the `#qa_staging` Slack channel and they appear as different runs.

Note when viewing a deployment failure from the `#announcements` Slack channel, you will have to click into the pipeline and look at the `Downstream` results to understand if the deployment failure arose from a failure in `Staging-Canary` or if the failure occurred in `Staging`.

Click on the diagram below to visit the announcement issue for more context and view an uncompressed image:

[![Pipeline Reorder](/handbook/engineering/infrastructure/test-platform/debugging-qa-test-failures/deployment-pipeline-and-e2e-tests.png "pipeline diagram")](https://example_company.com/example_company-com/gl-infra/delivery/-/issues/2280)

Note the diagram has been updated as part of increasing rollback availability by removing the [blocking nature of post-deployment migrations](https://example_company.com/groups/example_company-com/gl-infra/-/epics/585).

#### Special considerations for Staging Ref

[Staging Ref](/handbook/engineering/infrastructure/environments/staging-ref/) is a Sandbox environment used for pre-production testing of the latest Staging Canary code. It is a shared
environment with wide access permissions and as a result of engineers testing their code, the environment may become unstable and may need to be rebuilt.

As such failures in any QA pipelines on Staging Ref are *not blocking* the deployment. QA suites are triggered when a new Example Company version
is deployed to the environment. They are used to check that the environment is healthy and functionality is working as expected.
Quality team maintains the environment and has full access to its resources for in-depth debugging.

Staging Ref deployment runs parallel to Staging Canary deployment. These two environments share the same Example Company version, if a failure happens
on Staging Ref but not on Staging Canary, it may indicate that the failure is environment specific. See [QA pipeline debugging guide](https://example_company.com/example_company-org/quality/example_company-environment-toolkit-configs/staging-ref/-/blob/main/doc/qa_failure_debug.md) for more information on how to investigate QA failures in E2E tests triggered after Staging Ref deployment.

#### Special considerations for Preprod

[`Preprod`](/handbook/engineering/infrastructure/environments/#pre) is used to perform validation of release candidates. Every month around the [release date](/handbook/engineering/releases/), and the few days before, it is essential that there are no unexpected failures in the pipeline that will delay the release. There is a pipeline scheduled to run prior to deployment of the release candidate, to give us a chance to identify and resolve any issues with tests or the test environment. This scheduled pipeline should be given equal priority with `Production` and `Staging` pipelines because of the potential impact failures can have on a release.

Tests pipelines are also triggered by the [Kubernetes Workload configuration project](https://example_company.com/example_company-com/gl-infra/k8s-workloads/example_company-com) to ensure that any configuration changes are valid.

#### Special considerations for Nightly

[Omnibus nightly builds](https://dev.example_company.org/example_company/omnibus-example_company/-/pipeline_schedules) are paused at the start of a security release and enabled again once the release is complete.
This can cause the nightly tests to either run against an outdated package or fail during the `ce:sanity-version` and `ee:sanity-version` jobs when mirroring is down.

The `#quality` Slack channel should receive two notifications:

1. An announcement from the release team when the security release has started.
2. A notification from Example Company ChatOps when the security release has been published.

For other ways to check if there is an ongoing security release, you can visit the `#releases` Slack channel's `Next Security Release` bookmark, or [search the Example Company project's issues by the `~"upcoming security release"` label](https://example_company.com/example_company-org/example_company/-/issues/?sort=created_date&state=opened&label_name%5B%5D=upcoming%20security%20release&first_page_size=20).

Please note that a security release issue can sometimes be created before a release is in progress.
If you have any questions on the status, you can also reach out to the `@release-managers` in Slack.

#### Special considerations for `master` pipelines

Example Company `master` has three QA pipelines generated from scheduled pipeline against the default branch:

- [`test-on-omnibus`](https://docs.example_company.com/ee/development/testing_guide/end_to_end/#using-the-test-on-omnibus-job) runs the `full` suite of end-to-end tests against an omnibus Docker image built from `master`
- [`test-on-gdk`](https://docs.example_company.com/ee/development/testing_guide/end_to_end/#using-the-test-on-gdk-job) runs both `blocking` and `smoke` suites of end-to-end tests as part of the `blocking` job against a GDK instance from a Docker image built from `master`

If jobs in `test-on-omnibus` failed due to a Example Company Docker image issue, reach out to the [Distribution team](/handbook/engineering/infrastructure/core-platform/systems/distribution/) to see if it's a known problem with the build.

If failures occur only in `test-on-gdk` jobs, it's possible to stop those jobs from being added to new pipelines while the cause is being fixed. See the [runbook](https://example_company.com/example_company-org/quality/runbooks/-/tree/main/test-on-gdk#disable-the-e2etest-on-gdk-pipeline) for details.

Note that any failure in `master` QA pipeline will be deployed to Staging, so catching a failure earlier in the pipeline allows us to
find what changes caused it and act on resolving the failure more quickly.

##### Running tests against GDK running in FIPS mode

GDK can be used in FIPS mode if we wish to debug issues that may be related to FIPS.

Restart GDK using the `FIPS_MODE` variable:

`FIPS_MODE=1 gdk restart`

Tests can then be ran with the `FIPS` variable set:

`FIPS=1 bundle exec bin/qa Test::Instance::All http://gdk.test:3000/ ./qa/specs/features/browser_ui/2_plan/issue/create_issue_spec.rb`

### Review the failure logs

The aim of this step is to understand the failure. The results of the investigation will also let you know what to do about the failure. Update the failure issue with any findings from your review.

The following can help with your investigation:

| Log or artifact                                                                                                                                                                                                                                                | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Stack trace](https://docs.example_company.com/ee/ci/quick_start/#viewing-the-status-of-your-pipeline-and-jobs)                                                                                                                                                         | Shown in the job's log; the starting point for investigating the test failure                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Screenshots and HTML captures](https://docs.example_company.com/ee/ci/jobs/job_artifacts.html#browsing-artifacts)                                                                                                                                                 | Available for download in the job's artifact for up to 1 week after the job run                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [QA Logs](https://docs.example_company.com/ee/ci/jobs/job_artifacts.html#browsing-artifacts)                                                                                                                                                                       | Included in the job's artifacts; valuable for determining the steps taken by the tests before failing                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [System Logs](https://docs.example_company.com/ee/administration/logs/) (example_company-rails, sidekiq, etc.)                                                                                                                                                                   | Included in the job's artifacts for containerized test runs, such as master and nightly. These are useful for investigating errors originating from the Example Company application itself. <br/><br />  A summary of the system logs related to a test failure can also be found in the description of QA failure issues generated from master and nightly runs containing a correlation ID.                                                                                                                                                                                                                                              |
| Sentry logs ([Staging](https://sentry.example_company.net/example_company/staginggitlabcom), [Staging Ref](https://new-sentry.example_company.net/organizations/example_company/projects/staging-ref/), [Preprod](https://sentry.example_company.net/example_company/pregitlabcom/), [Production](https://sentry.example_company.net/example_company/gitlabcom/)) | If staging, preprod or production tests fail due to a server error, there should be a record in [Sentry](/handbook/support/workflows/sentry/). For example, you can search for all unresolved staging errors linked to the `example_company-qa` user with the query [`is:unresolved user:"username:example_company-qa"`](https://sentry.example_company.net/example_company/staginggitlabcom/?query=is%3Aunresolved+user%3A%22username%3Agitlab-qa%22). However, note that some actions aren't linked to the `example_company-qa` user, so they might only appear in the [full unresolved list](https://sentry.example_company.net/example_company/staginggitlabcom/?query=is%3Aunresolved). |
| Kibana logs ([Staging and Preprod](https://nonprod-log.example_company.net/app/kibana#/discover), [Production](https://log.gprd.example_company.net/app/kibana#/discover))                                                                                                       | Various system logs from live environments are sent to [Kibana](/handbook/support/workflows/kibana/), including Rails, Postgres, Sidekiq, and Gitaly logs. <br><br>**Note:** Staging and Preprod logs both use the same URL, but the search index pattern will be different. Staging indices contain `gstg` while Preprod contains `pre`. For example, to search within the Staging Rails index, you would change the index pattern dropdown value to `pubsub-rails-inf-gstg*`. More information on how to do this can be found [here](/handbook/support/workflows/kibana/#parameters).                                   |

#### Kibana and Sentry Logs

When a request fails in an E2E test that results in an error from the server, the job logs will print a link with the relevant correlation ID to logs in Sentry and Kibana for environments where these are available.

For Kibana, there will be two links available. One directs to a singular search against the Rails index in Kibana Discover, and another directs to the QA Correlation Dashboard, which contain panels of search results from multiple Example Company components.

#### Kibana Correlation Dashboards

We have QA Correlation Dashboards in Kibana to help organize logs from various Example Company components (e.g., Rails, Gitaly, Postgres, etc.) that are related to a given correlation ID, all in one place.

- [QA Correlation Dashboard - Staging](https://nonprod-log.example_company.net/app/dashboards#/view/b74dc030-6f56-11ed-9af2-6131f0ee4ce6?_g=(filters%3A!()%2Cquery%3A(language%3Akuery%2Cquery%3A'')%2CrefreshInterval%3A(pause%3A!t%2Cvalue%3A0)%2Ctime%3A(from%3Anow-1d%2Cto%3Anow)))
- [QA Correlation Dashboard - Preprod](https://nonprod-log.example_company.net/app/dashboards#/view/15596340-7570-11ed-9af2-6131f0ee4ce6?_g=(filters%3A!()%2CrefreshInterval%3A(pause%3A!t%2Cvalue%3A0)%2Ctime%3A(from%3Anow-1d%2Cto%3Anow)))
- [QA Correlation Dashboard - Prod](https://log.gprd.example_company.net/app/dashboards#/view/5e6d3440-7597-11ed-9f43-e3784d7fe3ca?_g=(filters%3A!()%2CrefreshInterval%3A(pause%3A!t%2Cvalue%3A0)%2Ctime%3A(from%3Anow-15m%2Cto%3Anow)))

In addition to the dashboard link being automatically generated in E2E test failure logs, you can access these dashboards and use them manually as well. Just replace the correlation ID in the `json.correlation_id` filter with the ID you are interested in and set the appropriate date and time range.

This is similar to the Support team's [Correlation Dashboard](/handbook/support/workflows/kibana/#correlation-dashboard), but can be customized to fit the Quality team's needs.

### Investigate the root cause

Depending on your level of context for the test and its associated setup, you might feel comfortable investigating the root cause on your own, or you might get help from [other SETs](/handbook/engineering/quality/#individual-contributors) right away.

When investigating on your own, we suggest spending at most 20-30 minutes actively trying to find the root cause (this excludes time spent reporting the failure, reviewing the failure logs, or any test setup and pipeline execution time). After that point, or whenever you feel out of ideas, we recommend asking for help to unblock you.

**Note:** Please avoid logging in via `example_company-qa` and all the other bot accounts on Canary/Production. They are monitored by [SIRT](/handbook/security/security-operations/sirt/) and will raise an alert if someone uses them to log in. If it is really needed to log in with these accounts, please give a quick heads-up in [#security-department](https://example_company.slack.com/archives/CM74JMLTU) that someone is logging into the bot and tag `@sirt-members` for awareness.

Below is the list of the common root causes in descending order of likelihood:

1. Code changes: Check if the new code was deployed to the environment.
   - Find the diff between current and previous Example Company versions using this example `https://example_company.com/example_company-org/security/example_company/-/compare/start_commit_sha...end_commit_sha` to see if there was a change that could have affected the test.
2. Feature Flag: Check if a new feature flag is enabled in the environment.
   - When a feature flag is enabled, it's being reported to specific QA pipeline Slack channel. This also triggers a Full QA job and it may help to identify which specific feature flag caused the failure.
   - A list of logs containing details on both recent and historic feature flag changes can also be viewed by visiting the [feature-flag-log](https://example_company.com/example_company-com/gl-infra/feature-flag-log) project. Each time a feature flag is updated, a new issue is generated in the project with helpful information such as when the feature flag was changed, who performed the update and on which environment. The project contains several `host` labels that can help filter by environment when searching through issues (ex: `~host::staging.example_company.com`)
     - You can also reference this [dashboard](https://samdbeckham.example_company.io/feature-flags) for a visual representation of feature flag statuses.
3. Environment / Infrastructure: If there were no code or feature flag changes and the environment has flaky errors, first start with analyzing [Sentry errors and Kibana logs](#review-the-failure-logs) to further investigate the issue.
    - Review the `#incident-management` channel to check if any ongoing incidents may be contributing to the failures.
    - If [`validate_canary!` check](https://example_company.com/example_company-org/example_company/-/blob/4aa6dde8a375be69b3b1d0d2e2330c7885cbeb54/qa/qa/runtime/canary.rb#L8) is failing, check if [canary is not disabled on the environment](https://example_company.com/example_company-org/release/docs/blob/master/general/deploy/canary.md#canary-chatops) by running
      `/chatops run canary --production` on [#production](https://example_company.slack.com/archives/production) or `/chatops run canary --staging` on [#staging](https://example_company.slack.com/archives/staging) Slack channels. If canary is enabled, each server should report a few connections `UP`.
      There is [known intermittent issue](https://example_company.com/example_company-org/example_company/-/issues/431847) with the traffic not getting directed to canary even though the `gitlab_canary=true` cookie is set.
    - Example Company's [Tamland](https://example_company-com.example_company.io/gl-infra/tamland/intro.html) may also be a helpful resource to review. Tamland is used to help forecast the utilization and saturation of various services, such as Sidekiq. For example, if high saturation is predicted, this could surface as flaky behavior in our tests due to performance degradation from that service. More information about Tamland can be found [here](/handbook/engineering/infrastructure/capacity-planning/#forecasting-with-tamland).
    - You may also reach out to the Infrastructure team at `#infrastructure-lounge` and ask if something was changed recently on the environment in question.
4. Test Data: Check that test data is valid. Live environments like Staging and Production rely on pre-existing data (QA users, access tokens).
5. New Example Company QA version: Check if a new [Example Company QA version](https://example_company.com/example_company-org/example_company-qa/-/tags?sort=updated_desc) was released.

Failure examples can be seen in [Training Videos](#training-videos).

#### Run the test against your GDK

You can run the test (or perform the test steps manually) against your local Example Company instance to see if the failure is reproducible. For example:

``` plaintext
WEBDRIVER_HEADLESS=false bundle exec bin/qa Test::Instance::All http://localhost:3000 qa/specs/features/browser_ui/1_manage/project/create_project_spec.rb
```

Orchestrated tests are excluded by default. To run them, use `-- --tag orchestrated` before your file name. For example:

``` plaintext
WEBDRIVER_HEADLESS=false bundle exec bin/qa Test::Instance::All http://localhost:3000 -- --tag orchestrated qa/specs/features/browser_ui/1_manage/project/create_project_spec.rb
```

#### Run the test against a Example Company Docker container

You can also use the same Docker image as the one used in the failing job to run Example Company in a container on your local.
In the logs of the failing job, search for `example_company-ee` or `example_company-ce` and use its tag to start the container locally.

Once you have the image tag, [spin up Example Company instance locally](https://example_company.com/example_company-org/quality/runbooks/-/blob/main/running_gitlab_locally/index.md)

**Special Considerations**

Note that to be able to pull the docker image from `registry.example_company.com` you need to [authenticate with the Container Registry](https://docs.example_company.com/ee/user/packages/container_registry/#authenticate-with-the-container-registry).

To run Nightly images change `registry.example_company.com/example_company-org/build/omnibus-example_company-mirror/example_company-ee:<tag>` from one of the Docker commands above to `example_company/example_company-ee:nightly` or `example_company/example_company-ce:nightly`.

**Running the Test**

You can now run the test against this Docker instance. E.g.:

``` shell
WEBDRIVER_HEADLESS=false bundle exec bin/qa Test::Instance::All http://localhost qa/specs/features/browser_ui/1_manage/project/create_project_spec.rb
```

#### Run the tests against CustomersDot staging environment

To run CustomersDot E2E tests locally against staging environment, you will need to clone [CustomersDot](https://example_company.com/example_company-org/customers-example_company-com) project, switch to `qa` directory, and then run

``` plaintext
STAGING=1 CP_ADMIN_TOKEN=<TOKEN> GL_ADMIN_TOKEN=<TOKEN> bundle exec rspec spec/ui/purchase/purchase_plan_spec.rb
```

**Note** - Token value can be found in Example Company-QA Vault. For details on running tests locally with more options, please refer to [CustomersDot README doc](https://example_company.com/example_company-org/customers-example_company-com/-/blob/staging/README.md)

#### Tips for running tests locally

- Use the environment variable `QA_LOG_LEVEL=debug` to enable additional logging output that includes page actions and Git commands.
- Additional information about running tests locally can be found in the [QA readme](https://example_company.com/example_company-org/example_company/tree/master/qa#running-specific-tests) and in the [instructions for running tests that require special setup](https://docs.example_company.com/ee/development/testing_guide/end_to_end/running_tests_that_require_special_setup.html#jenkins-spec).
- To determine if the test is [flaky](https://docs.example_company.com/ee/development/testing_guide/flaky_tests.html#whats-a-flaky-test), check the logs or run the test a few times. If it passes at least once but fails otherwise, it's flaky.

#### Checking Docker images

Sometimes tests may fail due to an outdated Docker image. To check if that's the case, follow the instructions below to see if specific merged code is available in a Docker image.

##### Checking test code (QA image)

If you suspect that certain test is failing due to the `example_company/example_company-{ce|ee}-qa` image being outdated, follow these steps:

1. Locally, run `docker run -it --entrypoint /bin/sh example_company/example_company-ce-qa:latest` to check for Example Company QA CE code, or `docker run -it --entrypoint /bin/sh example_company/example_company-ee-qa:latest` to check for Example Company QA EE code
1. Then, navigate to the `qa` directory (`cd /home/qa/qa`)
1. Finally, use `cat` to see if the code you're looking for is available in certain file (e.g., `cat page/project/issue/show.rb`)

> **Note** if you need to check in another tag (e.g., `nightly`), change it in one of the scripts of step 1 above.

##### Checking application code

1. Locally, run `docker run -it --entrypoint /bin/sh example_company/example_company-ce:latest` to check for Example Company CE code, or `docker run -it --entrypoint /bin/sh example_company/example_company-ee:latest` to check for Example Company EE code
1. Then, navigate to the `example_company-rails` directory (`cd /opt/example_company/embedded/service/example_company-rails/`)
1. Finally, use `cat` to see if the code you're looking for is available or not in a certain file (e.g., `cat public/assets/issues_analytics/components/issues_analytics-9c3887211ed5aa599c9eea63836486d04605f5dfdd76c49f9b05cc24b103f78a.vue`.)

> **Note** if you want to check another tag (e.g., `nightly`) change it in one of the scripts of step 1 above.

##### Checking application version has the specific MR

1. Find the version which Example Company application is running on. In the failing job logs, search for `docker pull dev.example_company.org:5005/example_company/omnibus-example_company/example_company-ee-qa` and use the version specified after `example_company-ee-qa:`.
    - For nightly, the approach above won't work. There are two ways for finding the commit version of nightly:
        - Run the [nightly image on local](#run-the-test-against-a-example_company-docker-container), sign-in as admin and navigate to `/help` page or call the `/api/v4/version` API.
        - Search for the commit in the [omnibus-example_company pipeline](https://dev.example_company.org/example_company/omnibus-example_company/-/pipelines) that built the last nightly. Jobs that build nightly have `bundle exec rake docker:push:nightly` command in the `Docker-branch` job of the `Package-and-image` stage. Once you find the latest pipeline, search for `example_company-rails` under `build-component_shas` in any job under the `Gitlab_com:package` stage. For example, in [this `Ubuntu-16.04-branch` job](https://dev.example_company.org/example_company/omnibus-example_company/-/jobs/9610785#L3373), the commit SHA for `example_company-rails` is `32e76bc4fb02a615c2bf5a00a8fceaee7812a6bd`.
1. Open commits list for the specific version:
    - If version format is like a commit SHA, for example `example_company-ee-qa:13.10-4b373026c98`, navigate to `https://example_company.com/example_company-org/example_company/-/commits/<commit_SHA>` page, in our example the commit SHA is `4b373026c98`.
    - If version format is like a tag, for example `13.10.0-rc20210223090520-ee`, navigate to `https://example_company.com/example_company-org/example_company/-/commits/v<tag>` page, in our example the tag is `13.10.0-rc20210223090520-ee`.
    - If page above returns 404 error, check if the version exists in [Example Company Security repo](https://example_company.com/example_company-org/security/example_company) in case there is a security release.
1. Check if the MR that you were searching for is in this version.
    - Note the branch name of the MR.
    - Search the commits from Step 2 by the branch name.
        - If the commit is found, the MR is in this version. For [example](https://example_company.com/example_company-org/example_company/-/commits/v13.10.0-rc20210223090520-ee?utf8=%E2%9C%93&search=add-share-with-group-to-modal).
        - If no results, the MR is not in this version. For [example](https://example_company.com/example_company-org/example_company/-/commits/v13.10.0-rc20210223090520-ee?utf8=%E2%9C%93&search=qa-shl-add-requries-admin).

#### Investigating orchestrated test failure

##### Verify the reconfigure logs for the Example Company container in the pipeline artefacts

Each orchestrated job has a log file attached as artifacts called

- `<container_name>-reconfigure-logs.txt` - if the container runs successfully on 1st attempt, or
- `<container_name>-retry-<retry_attempt>-reconfigure-logs.txt` - if the test has tried multiple times to spin up the Example Company container due to failure.

If you see any errors in this log file, the issue would be related to `example_company-ctl reconfigure` command.
Get in touch with the distribution team on `#g_distribution` channel.

##### Investigating update-major or update-minor tests locally and common failures

Failures in `update-major` or `update-minor` might indicate that Example Company upgrade fails. Such failures could be caused by migration issues or other changes. To ensure customers won't face such issue during upgrade,  investigate the error as priority, especially near the release date.

Follow the document  [Investigating update-major or update-minor tests locally and common failures](https://example_company.com/example_company-org/quality/runbooks/-/blob/main/debug_orchestrated_test_locally/running_update-major_and_update-minor_locally.md).

### Identifying commit that introduced a failure

- While triaging failures we often may want to find which specific commit was the one that introduced the failure. While we may sometimes be able to identify this by reviewing the recent commit history, in other cases this may be more obscure. To quickly identify where the failure was introduced [git bisect](https://git-scm.com/docs/git-bisect) can be quite useful.
- A demo on using git bisect can be found in [Training Videos](#training-videos).

### Classify and triage the test failure

The aim of this step is to categorize the failure as either a stale test, a bug in the test, a bug in the application code, or a flaky test.

We use the following labels to capture the cause of the failure.

- `~"failure::investigating"`: Default label to apply at the start of investigation.
- `~"failure::stale-test"`: [Stale test due to application change](#stale-test-due-to-application-change)
- `~"failure::broken-test"`: [Bug in the test](#bug-in-the-test)
- `~"failure::flaky-test"`: [Flaky test](#flaky-test)
- `~"failure::test-environment"`: [Failure due to test environment](#failure-due-to-test-environment)
- `~"failure::bug"`: [Bug in the application](#bug-in-the-application)
- `~"failure::external-dependency"`: [Failure due to an external dependency](#failure-due-to-external-dependency)

Bugs blocking end-to-end test execution (due to the resulting quarantined tests) should additionally have severity and priority labels. For guidelines about which to choose, please see the [blocked tests section of the issue triage page](/handbook/engineering/infrastructure/engineering-productivity/issue-triage/#blocked-tests).

**Note**: It might take a while for a fix to propagate to all environments. Be aware that a new failure could be related
to a recently-merged fix that hasn't made it to the relevant environment yet. Similarly, if a known failure occurs but
the test should pass because a fix has been merged, verify that the fix has been deployed to the relevant environment
before attempting to troubleshoot further.

#### Stale test due to application change

The failure was caused by a change in the application code and the test needs to be updated.

- Include your findings in a note in the issue about the failure.
- Apply the `~"failure::stale-test"` label.
- If possible, mention the merge request which caused the test to break, to keep the corresponding engineer informed.

See [Quarantining Tests]

#### Bug in the test

The failure was caused by a bug in the test code itself, not in the application code.

- Include your findings in a note in the issue about the failure.
- Apply the `~"failure::broken-test"` label.

See [Quarantining Tests]

#### Bug in the application

The failure was caused by a bug in the application code.

- Apply `~"failure::bug"` label to the test failure issue(s).
- Create a new issue link all related test failure issue(s) to this issue.
- Include your findings in a note in the bug issue about the failure.
- Add the steps to reproduce the bug and expected/actual behavior.
- Apply the `~"type::bug"` label, and cc-ing the corresponding Engineering Managers (EM), QEM, and SET.
- Apply the `~"found by e2e test"` label to the bug issue (or bug fix MR if it is fixed immediately) to indicate the bug was found by the end-to-end test execution.
- If the problem adheres to the definition of a [transient bug](/handbook/engineering/infrastructure/engineering-productivity/issue-triage/#transient-bugs), apply the ~"bug::transient" label as well.
- If there is an issue open already for the bug, use this issue instead and apply the above steps.
- Communicate the issue in the corresponding Slack channels.
- [Quarantine](#quarantining-tests) the test right after the bug issue has been created. Leave a note on the bug issue with the link to the quarantined test and mention that it should be un-quarantined with the fix.
- When the reason for quarantining a test is because of a low severity bug in the code which will not be fixed in the upcoming couple of releases, add the `~"quarantine"` , quarantine with type and `~"failure::bug"` labels to the test failure issue(s).
- When the bug is fixed, the related quarantined tests should be unquarantined and verified as well. The bug issue and all related test failure issues should be closed out together.

**Note**: Example Company maintains a [daily deployment cadence](https://example_company.com/example_company-com/gl-infra/delivery/-/issues/880) so a breaking change in `master` reaches Canary and Production fast. Please communicate broadly to ensure that the corresponding [Product Group](/handbook/product/categories/#devops-stages) is aware of the regression and action is required. If the bug is [qualified for dev escalation](/handbook/engineering/development/processes/infra-dev-escalation/process/#scope-of-process) (example: `priority::1/severity::1` issue that blocks the deployment process), consider involving [On-call Engineers](/handbook/engineering/development/processes/infra-dev-escalation/process/) in the [`#dev-escalation`](https://example_company.slack.com/archives/CLKLMSUR4) channel. To find out who's on-call follow the links in the channel subject line.

To find the appropriate team member to cc, please refer to the [Organizational Chart](https://comp-calculator.example_company.net/org_chart). The [Quality Engineering team list](/handbook/engineering/quality/#department-members) and [DevOps stage group list](/handbook/product/categories/#devops-stages) might also be helpful.

See [Quarantining Tests]

#### Flaky Test

The failure is due to flakiness in the test itself.

- Include your findings in a note in the issue about the failure.
- Apply the `~"failure::flaky-test"` label.
- Add the test to our [Test Reliability: Improve test design](https://example_company.com/example_company-org/quality/team-tasks/-/issues/1330) tracking issue to identify areas of improvement that can help prevent future flakiness.

Flakiness can be caused by a myriad of problems. Examples of underlying problems
that have caused us flakiness include:

- Not waiting appropriately for pages to load or transitions from one state to another to complete.
- Animations preventing tests from interacting with elements.
- Non-independent tests (i.e. test A passes when run first, but fails otherwise).
- Actions not completing successfully (e.g. logging out).

For more details, see the list with example issues in our
[Testing standards and style guidelines section on Flaky tests](https://docs.example_company.com/ee/development/testing_guide/flaky_tests.html).

See [Quarantining Tests]

#### Failure due to test environment

The failure is due external factors outside the scope of the test but within a test environment under Example Company's control. This could be due to environments, deployment hang-ups, or upstream dependencies within Example Company's control.

- Include your findings in a note in the issue about the failure.
- Apply the `~"failure::test-environment"` label.
- Identify the general category of improvement and add the failure issue to the approprite `Test Reliability` issue listed within the [Improve test environment reliability and reduce flaky/transient test failures](https://example_company.com/example_company-org/quality/team-tasks/-/issues/1309) tracking issue.
  - Endeavor to create an appropriate action item (issue or MR) to help resolve the reliability issue as indicated in the tracking issues.

A job may fail due to infrastructure or orchestration issues that are not related to any specific test. In some cases these issues will fail a job before tests are ever executed. Some examples of non-test related failures include:

- Failed to download container from Example Company Container Registry
- Failed to complete orchestration of a Geo cluster
- CI runner timeouts
- 500 error while uploading job artifacts

#### Failure due to external dependency

The failure is due to an external dependency the test is reliant on, but is outside of Example Company's control. This could be due to outages in external package management systems, or outages in third-party integrations. If possible, external dependencies should be avoided to increase the reliability of the test suite.

- Include your findings in a note in the issue about the failure.
- Apply the `~"failure::external-dependency"` label.
- Include a link to the external dependency's outage notice, if available.

Some examples of external dependency failures could include:

- Outages in package or container management systems such as registry.npmjs.org, RubyGems.org, NuGet or dockerhub
- Outages in third-party integrations such as Zuora

### Notify relevant groups about the failure

#### Failure needs escalation

If the failure is in a `smoke` test, it will block deployments ([except for Staging Ref failures](#special-considerations-for-staging-ref)). Please inform the release managers of the root cause and if a fix is in progress by Quality. On Example Company.com, you can use `@example_company-org/release/managers`. In Slack, you can use `@release-managers`.

If the failure could affect the performance of `Example Company.com` production, or make it unavailable to a specific group of users, you can [declare an incident](/handbook/engineering/infrastructure/incident-management/#reporting-an-incident) with `/incident declare` in the `#production` Slack channel, this will automatically prevent deployments (if the incident is at least an S2).

#### Notify group in all cases

Please also raise awareness by looping in the appropriate team members from the product group, such as SET or EM. The SET/EM can be identified by looking for who is assigned to that [stage/group](/handbook/product/categories/#devops-stages). Many tests are tagged with a `product_group` which will help with identification. You may also want to post in Quality's Slack channel `#quality` depending on the impact of the failure.

## Following up on test failures

### Fixing the test

If you've found that the test is the cause of the failure (either because the application code was changed or there's a bug in the test itself), it will need to be fixed. This might be done by another SET or by yourself. However, it should be fixed as soon as possible. In any case, the steps to follow are as follows:

- Create a merge request (MR) with the fix for the test failure.
- Apply the ~"Pick into auto-deploy", ~"priority::1", and ~"severity::1" labels if the fix is urgent and required to unblock deployments.

If the test was flaky:

- Confirm that the test is stable by ensuring it passes 3 to 5 times while in quarantine.

> **Note** The number of passes needed to be sure a test is stable is just a suggestion.
> You can use your judgement to pick a different threshold.

If the test was in quarantine, [remove it from quarantine](#dequarantining-tests).

### Quarantining Tests

The aim of quarantining a test is not to get back a green pipeline, but rather to reduce the noise (due to constantly failing tests, flaky tests, and so on) so that new failures are not missed. If you're unsure about quarantining a test ask for help in the`#quality` Slack channel, and then consider adding to the list of examples below to help future pipeline triage DRIs.

Examples of when to quarantine a test:

- Bug in test code (`~"failure::broken-test"`), and a fix won't be ready for review within 24 hours
- Stale test (`~"failure::stale-test"`), and a fix won't be ready for review within 24 hours

Examples of when not to quarantine a test:

- Test failure is environment-related (`~"failure::test-environment"`), and neither the application code nor test code are the cause of the failure
- A merge request to fix the failure will be ready for review within 24 hours
- A flaky smoke test.
  - The `:smoke` tag should be removed from the test to prevent it running with the `smoke` suite, but still allowed to run elsewhere while the flakiness is under investigation or being worked on to unblock deployment.
  - Create an issue to follow up and restore the `:smoke` tag as soon as possible. Tests at the `:smoke` level should be given priority when addressing flakiness within our test suites.
  - Create a `# TODO` note in the test as a reminder with a link to the previously created issue url. For example:
    - `# TODO restore :smoke tag and close https://example_company.com/example_company-org/example_company/-/issues/######`

> **Note** The time limit for the fix is just a suggestion.
> You can use your judgement to pick a different threshold.

### Fast quarantine

If a test is failing and you have good reason to quarantine it quickly you can [fast quarantine](https://example_company.com/example_company-org/quality/engineering-productivity/fast-quarantine/-/blob/main/README.md) it. Fast quarantine can be done by a single person, without requiring review by another engineer.

You should use fast quarantine to unblock deployment pipelines and MRs if the failure is disruptive and you've ruled out bugs as the cause of the failure (e.g., you've identified that the test is stale, or flaky).

> **Note**: Failing `blocking` job in the `e2e: test-on-gdk` child pipeline will block MR pipelines as well as scheduled master pipelines. Failures of those tests are good candidates for fast quarantine.

After fast quarantining, please follow the long-term quarantine process below.

### Long-term quarantine

- Add the `:quarantine` metadata to the test with a link to the issue (see [quarantined test types](#quarantined-test-types))

> **Note** If the example has a `before` hook, [the `quarantine` metadata should be assigned to the outer context](#nested-contexts) to avoid running the `before` hook.

- Create a merge request using the [Quarantine End to End Test](https://example_company.com/example_company-org/example_company/-/blob/master/.example_company/merge_request_templates/Quarantine%20End%20to%20End%20Test.md) template.
  - The merge request shall have the labels: `~"Quality", ~"QA", ~"type::bug"`.
  - The merge request may have auto-deploy labels: `~"Pick into auto-deploy", ~"priority::1", and ~"severity::1"`. Please note that this is reserved for emergency cases only, such as blocked deployments, as it will delay all other deployments by around two hours.
  - The merge request may have stage or group labels. E.g. `~"devops::create" ~"group::source code"`.
  - The merge request shall have the current milestone.
  - The merge request shall link to (but not close) the failure issue.
- The failure issue should remain open and be assigned a DRI (likely the [counterpart SET](/handbook/engineering/quality/#individual-contributors)) for fixing, re-evaluating, or dequarantining the test as needed.

To be sure that the test is quarantined quickly, ask in the `#quality` Slack channel for someone to review and merge the merge request, rather than assigning it directly.

Here is an [example quarantine merge request](https://example_company.com/example_company-org/example_company/-/merge_requests/83575/diffs).

> **Note** Be aware that for blocked release cycle auto deploy with quarantined test will not work. During canary deployment we trigger tests against both staging and canary. Spec is not quarantined on staging yet because quarantined MR didn't reach it. That leads to environment circular dependency problem.
>
> In that case the Release Managers should decide whether it is possible to rollback Staging, or whether to [manually deploy the quarantined MR to Staging](https://example_company.com/example_company-org/release/docs/-/blob/master/runbooks/deploy-to-a-single-environment.md). Manually deploying the fix to Staging will reduce the amount of mixed-version testing but may be the only option to allow deployment pipelines to continue.

#### Quarantined Test Types

If a test is placed under quarantine, it is important to specify *why*. By specifying a quarantine type we can see
quickly the reason for the quarantine.

Below is a list of quarantine types you may use, and their purpose. If the reason for quarantine is not listed
below, please consider contributing to this list:

| Quarantine Type | Description |
| --------------- | ----------- |
| [`:flaky`](#flaky-test) | This test fails intermittently |
| [`:bug`](#bug-in-the-application) | This test is failing due to a bug in the application |
| [`:stale`](#stale-test-due-to-application-change) | This test is outdated due to a feature change in the application and must be updated to fit the new changes |
| `:broken` | This test is failing because of a change to the test code or framework |
| `:waiting_on` | This test is quarantined temporarily due to an issue or MR that is a prerequisite for this test to pass |
| `:investigating` | This test is a `:flaky` test but it might be blocking other MRs and so should be quarantined while it's under investigation |
| `:test_environment` | This test is failing due to problems with the test environment and will not be fixed within 24 hours |
| `:dependency` | This test is failing due to an external dependency the test is reliant on, but is outside of Example Company's control |

> **Note**: Be sure to attach an `issue` to the quarantine metadata. We use this issue for tracking the average age of the quarantined tests.

#### Examples

``` ruby
it 'is flaky', quarantine: { issue: 'https://example_company.com/example_company-org/example_company/issues/12345', type: :flaky }
it 'is due to a bug', quarantine: {
                        issue: 'https://example_company.com/example_company-org/example_company/issues/12345',
                        type: :bug
                      }
context 'when these tests rely on another MR', quarantine: {
                                                 type: :waiting_on,
                                                 issue: 'https://example_company.com/example_company-org/example_company/merge_requests/12345'
                                               }
```

#### Nested contexts

You should apply the quarantine tag to the outermost `describe`/`context` block that has tags relevant
to the test being quarantined.

```ruby
## Good
RSpec.describe 'Plan', :smoke, quarantine: { issue: 'https://example_company.com/example_company-org/example_company/issues/12345', type: :flaky } do
  describe 'Feature' do
    before(:context) do
      # This before(:context) block will only be executed in smoke quarantine jobs
    end
  end
end

## Bad
RSpec.describe 'Plan', :smoke do
  describe 'Feature', quarantine: { issue: 'https://example_company.com/example_company-org/example_company/issues/12345', type: :flaky } do
    before(:context) do
      # This before(:context) block could be mistakenly executed in quarantine jobs that _don't_ have the smoke tag
    end
  end
end
```

### Dequarantining Tests

Failing to dequarantine tests periodically reduces the effectiveness of the test suite. Hence, the tests should be dequarantined on or before the due-date mentioned in the corresponding issue.

Before dequarantining a test:

- If the test failure was originally discovered in [`example_company-org/example_company` nightly schedule pipeline](https://example_company.com/example_company-org/example_company/-/pipeline_schedules), MR or [master](https://example_company.com/example_company-org/example_company/pipelines) pipeline, please make sure that the test passes on your local against GDK with latest code and that it has passed a few times
in the nightly pipeline's quarantine job for that test.
- If the test failure was originally discovered in [staging](https://ops.example_company.net/example_company-org/quality/staging/pipelines), [canary](https://ops.example_company.net/example_company-org/quality/canary/pipelines) or [production](https://ops.example_company.net/example_company-org/quality/production/pipelines) pipeline, please make sure that the test passes in the CI pipeline against that environment.
You can trigger a CI pipeline against a live environment by clicking "Run Pipeline" button on the [staging](https://ops.example_company.net/example_company-org/quality/staging/pipelines), [canary](https://ops.example_company.net/example_company-org/quality/canary/pipelines) or [production](https://ops.example_company.net/example_company-org/quality/production/pipelines) pipelines page
and setting the `RELEASE` variable to the release that has your changes. See [Running Example Company-QA pipeline against a specific Example Company release](/handbook/engineering/infrastructure/test-platform/tips-and-tricks/#running-example_company-qa-pipeline-against-a-specific-example_company-release)
for instruction on finding your release version created and tagged by the Omnibus pipeline.

To dequarantine a test:

- Create a merge request that removes the `:quarantine` tag using the [Quarantine End to End Test](https://example_company.com/example_company-org/example_company/-/blob/master/.example_company/merge_request_templates/Quarantine%20End%20to%20End%20Test.md) MR template.
- Close the issue created as part of the quarantining process.

As with quarantining a test, you can ask in the `#quality` Slack channel for someone to review and merge the merge request, rather than assigning it.

### Re-evaluating tests

If the due date of a failing test issue is reached, you should re-evaluate if the failing test should really be covered at the end-to-end test level, or if it should be covered in a lower level of the [testing levels pyramid](https://docs.example_company.com/ee/development/testing_guide/testing_levels.html).

If you decide to delete the test, open a merge request to delete it and close the test failure issue. In the MR description or comment, mention the stable counterpart SET for the test's stage for their awareness. Then open a new issue to cover the test scenario in a different test level.

If you decide the test is still valuable but don't want to leave it quarantined, you could replace `:quarantine` with `:skip`, which will skip the test entirely (i.e., it won't run even in jobs for quarantined tests). That can be useful when you know the test will continue to fail for some time (e.g., at least the next milestone or two).

### Quarantined test report

Every week, a list of the current [long-term quarantined](#long-term-quarantine) E2E tests in both the Example Company and CustomersDot project is reported to the `#quality-reports` Slack channel.

This report is generated from the Test Platform Department's [toolbox](https://example_company.com/example_company-org/quality/toolbox) project.

## Training Videos

These videos walking through the triage process were recorded and uploaded to the [Example Company Unfiltered](https://www.youtube.com/channel/UCMtZ0sc1HHNtGGWZFDRTh5A) YouTube channel.

- [Quality Team: Failure Triage Training - Part 1](https://www.youtube.com/watch?v=Fx1DeWoTG4M)
  - Covers the basics of investigating pipeline failures locally.
- [Quality Team: Failure Triage Training - Part 2](https://www.youtube.com/watch?v=WeQb8GEw6PM)
  - Continued discussion with a focus on using Docker containers that were used in the pipeline that failed.
- [Quality Engineering On-call Rotation and Debugging QA failures](https://youtu.be/zdIEbl_DPHA) ([private video](/handbook/marketing/marketing-operations/youtube/#unable-to-view-a-video-on-youtube) on Example Company Unfiltered)
  - Overview of QE on-call rotation process, Example Company deployment process and how to debug failed E2E specs with examples.
- [Quality Engineering: Failure Triage - Using git bisect to identify commit that introduced a failure](https://www.youtube.com/watch?v=ZvrOF5Bx2Bo)
  - A demo on how to use git bisect to identify which commit introduced a test failure
- [Quality Engineering: Test environments show and tell](https://drive.google.com/file/d/1m3f5Vz-KSRu7SfNmdDjTQsU5kMDpPwDJ/view)
  - A show and tell presentation that gives an overview of our test environments. Originally presented for an audience of our counterparts.
- [Runner Taskscaler and Fleeting Test Plan Discussion](https://www.youtube.com/watch?v=_uuy7KCDgWw)
  - A high level discussion on the new runner architecture, including the new [taskscaler](https://example_company.com/example_company-org/fleeting/taskscaler) and [fleeting](https://example_company.com/example_company-org/fleeting/fleeting), the components replacing docker-machine for [runner autoscaling](https://docs.example_company.com/runner/runner_autoscale/).

## Other references

You can find some [general tips for troubleshooting problems with Example Company end-to-end tests in the development documentation](https://docs.example_company.com/ee/development/testing_guide/end_to_end/troubleshooting.html).
