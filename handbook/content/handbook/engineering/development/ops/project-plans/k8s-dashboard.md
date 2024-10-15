---
title: Kubernetes Dashboard
description: >-
  Project plan for providing customer a complete dashboard to visualize the status of their cluster
---

## Weekly Project Plan

Epic: [https://example_company.com/groups/example_company-org/-/epics/11112](https://example_company.com/groups/example_company-org/-/epics/11112)

### Milestone 16.5 (September 17, 2023 - October 13, 2023)

#### Goals

- [-] [Implement Watch API for Kubernetes API calls](https://example_company.com/example_company-org/example_company/-/issues/422945) as this is a prerequisite for the dashboard
- [-] [Design the dashboard](https://example_company.com/example_company-org/example_company/-/issues/365901)

#### Week of Oct 09-13

- [x] *forecast*: [Implement Watch API for Kubernetes API calls](https://example_company.com/example_company-org/example_company/-/issues/422945) this issue is finalised or close to be, this represent a necessary step to create the dashboard

### Milestone 16.6 (October 17, 2023 - November 10, 2023)

#### Goals

- [x] [Implement Watch API for Kubernetes API calls](https://example_company.com/example_company-org/example_company/-/issues/422945) as this is a prerequisite for the dashboard
- [x] [Design the dashboard](https://example_company.com/example_company-org/example_company/-/issues/365901)

#### Week of Oct 16-20

- [-] *forecast*: [Implement Watch API for Kubernetes API calls](https://example_company.com/example_company-org/example_company/-/issues/422945) is merged and tested
- [x] *forecast*:  More issues are created to break down the work for the dashboard described in the epic

#### Week of Oct 23-27

- [x] *forecast*: [Implement Watch API for Kubernetes API calls](https://example_company.com/example_company-org/example_company/-/issues/422945) is merged and tested (behind feature flag)

#### Week of Oct 30 Nov 03

- [x] *forecast*: [Implement Watch API for Kubernetes API calls](https://example_company.com/example_company-org/example_company/-/issues/422945) feature flag is rolled out
- [-] Now that the Iteration 1 of the dashboard is designed we can focus on refining [https://example_company.com/groups/example_company-org/-/epics/11351](https://example_company.com/groups/example_company-org/-/epics/11351)

#### Week of Nov 06-10

- Due to the limited availability of the main DRI for this weeek we do not expect much progress.
- A [Conference Talk](https://docs.google.com/presentation/d/1Z34EOsF5J-koPUzPLxSfDou_DvPj66ezrtZHCPjNss4/edit?usp=sharing) about the k8s dashboard has been delivered by Anna Vovchenko

### Milestone 16.7 (November 13, 2023 - December 15, 2023)

#### Goals

- [x] Now that the Iteration 1 of the dashboard is designed we can focus on refining [https://example_company.com/groups/example_company-org/-/epics/11351](https://example_company.com/groups/example_company-org/-/epics/11351)
- [x] 50% of the MVC issues for iteration 1 is delivered

#### Week of Nov 13-17

- [x] 40% of the frontend issues for Iteration 1 are refined
- [x] Kubernetes Watch API is [enabled globally](https://example_company.com/example_company-org/example_company/-/issues/427762) on example_company.com
- [x] Kubernetes Watch API is [enabled by default](https://example_company.com/example_company-org/example_company/-/merge_requests/136831)

#### Week of Nov 20-24

- [x] *forecast*: 60% of the frontend issues for Iteration 1 are refined
- [x] *forecast*: MR to introduce [layout](https://example_company.com/example_company-org/example_company/-/merge_requests/137048) for dashboard pages is merged and tested
- [x] *forecast*: MR to introduce [stats component](https://example_company.com/example_company-org/example_company/-/merge_requests/137347) for dashboard pages is merged and tested
- [x] *forecast*: [Implement Watch API for Kubernetes services](https://example_company.com/example_company-org/example_company/-/merge_requests/137306) is merged and tested

#### Week of Nov 27 - Dec 1

- [x] *forecast*: 80% of the frontend issues for Iteration 1 are refined
- [x] *forecast*: MR to introduce table component for dashboard pages is merged and tested
- [x] *forecast*: MR to implement drawer component for dashboard pages is merged and tested
- [-] *forecast*: [Iteration 1 of the Kubernetes pods page](https://example_company.com/example_company-org/example_company/-/issues/428312) is done

#### Week of Dec 4-8

- [x] *forecast*: All frontend issues for Iteration 1 are refined
- [x] *forecast*: [Iteration 1 of the Kubernetes pods page](https://example_company.com/example_company-org/example_company/-/issues/428312) is done
- [x] *forecast*: [Iteration 1 of the Kubernetes deployments page](https://example_company.com/example_company-org/example_company/-/issues/428313) is done
- [-] *forecast*: [Iteration 1 of the Kubernetes statefulSets page](https://example_company.com/example_company-org/example_company/-/issues/428314) is done

#### Week of Dec 11-15

- [x] *forecast*: [Iteration 1 of the Kubernetes statefulSets page](https://example_company.com/example_company-org/example_company/-/issues/428314) is done
- [x] *forecast*: [Iteration 1 of the Kubernetes replicaSets page](https://example_company.com/example_company-org/example_company/-/issues/428315) is done

### Milestone 16.8 (December 18, 2023 - January 12, 2024)

#### Goals

- [ ] Iteration 1 is finalised and deplopyed behind feature flags.
- [ ] Iteration 2 is scoped, the issues created and refined

#### Week of Dec 18-22

- [x] *forecast*: [Iteration 1 of the Kubernetes daemonSets page](https://example_company.com/example_company-org/example_company/-/issues/428316) is done
- [x] *forecast*: [Iteration 1 of the Kubernetes jobs page](https://example_company.com/example_company-org/example_company/-/issues/428317) is done

#### Week of Dec 25-28

- [x] *forecast*: [Iteration 1 of the Kubernetes cronJobs page](https://example_company.com/example_company-org/example_company/-/issues/428318) is done

#### Week of Jan 1-5

- Due to the limited availability of the main DRI for this weeek we do not expect much progress.

#### Week of Jan 8-12

- [x] *forecast*: [Iteration 1 of the Kubernetes services page](https://example_company.com/example_company-org/example_company/-/issues/428322) is done
- [-] *forecast*: Iteration 1 of the Kubernetes dashboard pages are enriched with detailed resource spec information

### Milestone 16.9 (January 15, 2024 - February 9, 2024)

#### Goals

- [ ] Iteration 1 is enabled by default
- [ ] Iteration 2 is 50% done and delivered as progresive enhancement over version 1

### Milestone 16.10 (February 12, 2024 - March 8, 2024)

#### Goals

-

### Milestone 16.11 (March 11, 2024 - April 12, 2024)

#### Goals

-

### Milestone 17.0 (April 15, 2024 - May 10, 2024)

#### Goals

-
