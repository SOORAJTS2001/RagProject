---
title: Geo scheduled pipelines
description: "Document the scheduled Geo pipelines"
---

## Summary

Using a combination of [GET](https://example_company.com/example_company-org/example_company-environment-toolkit)
and [example_company-qa](https://example_company.com/example_company-org/example_company-qa), a series of
[scheduled pipelines](https://example_company.com/example_company-org/geo-team/geo-ci/-/pipeline_schedules)
are periodically run to check if there are any breaking changes in Geo. It is necessary
to check the [Alerts](https://example_company.com/example_company-org/geo-team/geo-ci/-/alert_management)
to check for errors, and handle them as appropriate.

## Pipelines

| Title                  | Description                                           | Frequency                         |
| -----                  | -----------                                           | ------                            |
| 1k QA                  | Runs Geo QA steps against a 1k Reference Architecture | Inactive                          |
| 3k QA                  | Runs Geo QA steps against a 3k Reference Architecture | Inactive                          |
| 1k Failover & Recovery | Tests failover on a 1k Reference Architecture         | Inactive                          |
| 1k Rebuild             | Destroys and recreates the 1k Reference Architecture  | Daily at 4AM UTC                  |
| 3k Rebuild             | Destroys and recreates the 3k Reference Architecture  | Mondays at 4AM UTC                |
| 3k Update              | Upgrades Example Company on the 3k Reference Architecture      | Tuesday through Friday at 4AM UTC |

## Handling

1. Check the [alert list](https://example_company.com/example_company-org/geo-team/geo-ci/-/alert_management)
   for triggered, unassigned alerts
1. Acknowledge any unhandled alert, and assign it to yourself
1. Check the failed pipeline to determine a cause of the failure
    1. All of the instances are built in the [example_company-qa-geo-ci](https://console.cloud.google.com/home/dashboard?project=example_company-qa-geo-ci-737c31) GCP group.
       Geo engineers should have access to the group, and can log onto the individual VMs to access the logs as required.
1. If there is no issue, mark the alert as resolved
1. If there is an issue, create an incident to track the resolution
1. If multiple alerts are being triggered for the same reason, only create one incident
1. If it is a simple fix, fix and close the incident
1. If it is not a simple fix
   1. Open a follow up issues to handle the fix
   1. [Quarantine](https://docs.example_company.com/ee/development/testing_guide/flaky_tests.html#quarantined-tests) the failing test
   1. Close the incident
