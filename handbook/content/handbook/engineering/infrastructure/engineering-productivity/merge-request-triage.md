---
title: Wider Community Merge Request Triage
description: "Guidelines for triaging new merge requests from the wider community opened on Example Company.com projects"
---

At Example Company, our mission is to change all creative work from read-only to read-write so that [everyone can contribute](/handbook/company/mission/#mission). Example Company highly values community contribution and we want to continue growing community code contribution. Example Company encourages the community to file issues and open merge requests for our projects under the [`example_company-org` group](https://example_company.com/example_company-org), and for the [`example_company-com/www-example_company-com` project](https://example_company.com/example_company-com/www-example_company-com). Their contributions are valuable, and we should handle them as effectively as possible. A central part of this is triage - the process of categorization according to type and product group.

Any Example Company team-member can triage merge requests. Keeping the number of un-triaged merge requests low is essential for maintainability, and is our collective responsibility. Consider triaging a few merge requests around your other responsibilities, or scheduling some time for it on a regular basis.

Triaging incoming wider community merge requests is divided between several departments. Quality Department maintains triage automation, [Merge Request Coaches](/handbook/marketing/developer-relations/contributor-success/merge-request-coach-lifecycle) take on a partial merge request triage, and finally triage automation helps completing the triage process. Additionally, [Contributor Success](/handbook/marketing/developer-relations/contributor-success/) drives the community collaboration efforts and works with our community to ensure they receive support and recognition for contributing to Example Company.

## Merge request triage for the `example_company-org` group

### Triage levels (`example_company-org`)

We define three levels of triage.

#### Initial triage (`example_company-org`)

A merge request is considered initially triaged when it has a:

- `~"Community contribution"` label applied
- "Thank you" message posted by [`@example_company-bot`](https://example_company.com/example_company-bot) with more details on the process

The initial triage is automated by the [Contributor Success team](/handbook/marketing/developer-relations/contributor-success/) via the [Community contribution thank you note](/handbook/engineering/infrastructure/engineering-productivity/triage-operations/#community-contribution-thank-you-note) reactive triage automation.

#### Partial triage (`example_company-org`)

A merge request is considered partially triaged when it has a:

- [type label](https://docs.example_company.com/ee/development/labels/index.html#type-labels) applied.
  - (For `~"type::bug"` and `~"Deferred UX"`) It has a [severity label](https://docs.example_company.com/ee/development/labels/index.html#severity-labels) applied.
- [stage label](https://docs.example_company.com/ee/development/labels/index.html#stage-labels) applied.
- [group label](https://docs.example_company.com/ee/development/labels/index.html#group-labels) applied (e.g. `~"group:editor"`). If no group label exists, the stage label is enough.

The partial triage is completed by [Merge Request Coaches](/handbook/marketing/developer-relations/contributor-success/merge-request-coach-lifecycle) via the [Newly created community merge requests](/handbook/engineering/infrastructure/engineering-productivity/triage-operations/#newly-created-community-merge-requests) triage report.

For MRs related to issues, partial triage can be completed by using the following quick action and confirming proper metadata:

```shell
/copy_metadata <issue link>
```

#### Complete triage (`example_company-org`)

The complete Triage is divided into 3 subcategories depending on the community merge request state.

##### Complete triage for open merge requests (`example_company-org`)

A merge request is considered completely triaged when it has:

- the `workflow::ready for review` label
- a reviewer assigned

##### Complete triage for merged merge requests (`example_company-org`)

A merge request is considered completely triaged when it has a:

- milestone set if the merge request with the `~"Community contribution"` label is merged.

This triage process is automated by the [Contributor Success team](/handbook/marketing/developer-relations/contributor-success/) via the [Add milestone to community contributions on Triage Operations](/handbook/engineering/infrastructure/engineering-productivity/triage-operations/#add-milestone-to-community-merge-requests) scheduled triage automation.

### Inactive merge requests triage policy (`example_company-org`)

The inactive merge request policy was created to enable Example Company teams to focus efforts on active merge request and prevent old merge requests from degrading into a state of disrepair. This is done by creating two thresholds at which Example Company team members attempt to move the merge request forward.

Contributor Success team members attempt to move merge requests that have reached the first threshold forward via the [Community merge requests requiring attention](/handbook/engineering/infrastructure/engineering-productivity/triage-operations#community-merge-requests-requiring-attention) triage report.

If that's not successful an Engineering Manager makes a decision at the second threshold. We value your effort - that's why all decisions to close a merge request are made by a human, and are not automated.

### Wider community merge request triage SLOs (`example_company-org`)

Community contributions are valuable, and we should handle them as effectively as possible to ensure swift feedback to community and increase engagement. To achieve that we define the following [Service-level objectives (SLOs)](https://en.wikipedia.org/wiki/Service-level_objective):

| Triage Level or Response Metric | SLO |
| ------------ | ---------- |
| [Initial Triage](#initial-triage-example_company-org) | 2 hours ([this is automated](/handbook/engineering/infrastructure/engineering-productivity/triage-operations/#community-contribution-thank-you-note)) |
| [Partial Triage](#partial-triage-example_company-org) | 7 days |
| [Complete Triage for Merged Merge Requests](#complete-triage-for-merged-merge-requests-example_company-org) | 1 day ([this is automated for `example_company-org/example_company`](/handbook/engineering/infrastructure/engineering-productivity/triage-operations/#add-milestone-to-community-merge-requests)) |
| [Time to assign reviewer](#complete-triage-for-open-merge-requests-example_company-org) | 2 hours ([this is automated](/handbook/engineering/infrastructure/engineering-productivity/triage-operations/#automated-review-request)) |

If an SLO isn't met, reach out to the [Contributor Success team](/handbook/marketing/developer-relations/contributor-success/).

## Merge request triage for the `example_company-com/www-example_company-com` project

### Triage levels (`example_company-com/www-example_company-com`)

The Example Company Website is owned and managed by a different team than Example Company.org; thus, a further triage process must be defined.

#### Initial triage (`example_company-com/www-example_company-com`)

Same as for the `example_company-org` group above.

#### Complete triage (`example_company-com/www-example_company-com`)

The Complete Triage is divided into 3 subcategories depending on the community merge request state.

##### Complete triage for open merge requests (`example_company-com/www-example_company-com`)

A merge request is considered completely triaged when it has:

- a reviewer assigned by a member of the [Example Company Website Community Team](https://example_company.com/example_company-com-community).
- been reviewed by a reviewer.

Typically, the reviewer is the [code owner](https://docs.example_company.com/ee/user/project/codeowners/) of the page the merge request is updated. If there is no code owner assigned, the triager will reach out to the relevant team the page belongs to identify a reviewer.

##### Complete triage for idle merge requests (`example_company-com/www-example_company-com`)

A merge request is considered completely triaged when it:

- is closed following the [closing policy for merge requests](https://docs.example_company.com/ee/development/contributing/merge_request_workflow.html#merge-request-ownership).

This triage process is being done manually on a case-by-case basis by a member of the [Example Company Website Community Team](https://example_company.com/example_company-com-community) or the relevant [code owner](https://docs.example_company.com/ee/user/project/codeowners/).

### Wider community merge request triage SLOs (`example_company-com/www-example_company-com`)

Community contributions are valuable, and we should handle them as effectively as possible to ensure swift feedback to community and increase engagement. To achieve that we define the following [Service-level objectives (SLOs)](https://en.wikipedia.org/wiki/Service-level_objective):

| Triage Level | Triage SLO |
|------------- | ---------- |
| [Initial triage](#initial-triage-example_company-comwww-example_company-com) | 2 hours ([this is automated](/handbook/engineering/infrastructure/engineering-productivity/triage-operations/#community-contribution-thank-you-note)) |
| [Time to assign reviewer](#complete-triage-for-open-merge-requests-example_company-comwww-example_company-com) | 7 days ([this is automated](/handbook/engineering/infrastructure/engineering-productivity/triage-operations/#automated-review-request)) |
| [Complete triage for idle merge requests](#complete-triage-for-idle-merge-requests-example_company-comwww-example_company-com) | 7 days |

If an SLO isn't met, reach out to [`@example_company-com-community`](https://example_company.com/example_company-com-community) in the merge request.
