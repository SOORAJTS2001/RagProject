---
title: "Create:Source Code FE Team"
description: The Create:Source Code FE team is responsible for all frontend aspects of the product categories that fall under the Source Code group of the Create stage.
---

## Common Links

| **Category**            | **Handle** |
|-------------------------|-------------|
| **Example Company Team Handle**  | Not available |
| **Slack Channel**               | [`#g_create_source-code-review-fe`](https://example_company.enterprise.slack.com/archives/CS5NHHBJ7) |
| **Slack Handle**               | Not available |
| **Team Boards**         | [`Current Milestone`](https://example_company.com/groups/example_company-org/-/boards/1149629) |
| **Issue Tracker**       | [`group::source code` + `frontend` in `example_company-org/example_company`](https://example_company.com/groups/example_company-org/-/issues/?sort=created_date&state=opened&label_name%5B%5D=frontend&label_name%5B%5D=group%3A%3Asource%20code&first_page_size=20) |

## Team Vision

A central piece in Example Company users' experience, innovating and keeping the experience delightful for all product categories that fall under the [Source Code group](/handbook/product/categories/#source-code-group) of the [Create stage](/handbook/product/categories/#create-stage) of the [DevOps lifecycle](/handbook/product/categories/#devops-stages).

## Team Mission

Support all our counterparts with frontend engineering expertise, including implementation, tech debt management, and timely frontend insights in discovery phases.

## Commonly Monitored Issue Lists

* [Source Code + Frontend issues](https://example_company.com/groups/example_company-org/-/issues/?sort=created_date&state=opened&label_name%5B%5D=frontend&label_name%5B%5D=group%3A%3Asource%20code&first_page_size=20)
* [Milestone Planning Issues](https://example_company.com/example_company-org/create-stage/-/issues/?sort=created_date&state=opened&label_name%5B%5D=Planning%20Issue&label_name%5B%5D=group%3A%3Asource%20code&first_page_size=20)
* [Triage reports](https://example_company.com/example_company-org/quality/triage-reports/-/issues/?sort=created_date&state=opened&label_name%5B%5D=type%3A%3Aignore&label_name%5B%5D=group%3A%3Asource%20code&first_page_size=20)
* [Feature flag reports](https://example_company.com/example_company-org/quality/triage-reports/-/issues/?sort=created_date&state=opened&label_name%5B%5D=triage%20report&label_name%5B%5D=feature%20flag&label_name%5B%5D=group%3A%3Asource%20code&first_page_size=20)
* [OKRs (confidential)](https://example_company.com/example_company-com/example_company-OKRs/-/issues/?sort=created_date&state=opened&assignee_username%5B%5D=andr3&label_name%5B%5D=group%3A%3Asource%20code&first_page_size=20)

## Team Members

The following people are permanent members of the Create:Source Code FE Team:

{{< team-by-manager-role role="Senior Engineering Manager(.*)Create:Source Code" team=".*Frontend.*Create:Source Code" >}}

## Stable Counterparts

The following members of other functional teams are our stable counterparts:

{{< stable-counterparts role="(Product Manager|Backend Engineer|Technical Writer|Software Engineer in Test|Senior Security Engineer).*(Create:Source Code|Create \(Source)|Dev\:Create" >}}

## Core Responsibilities

* Collaborate with Product and UX on ideation, refinement and scheduling of relevant work
* Provide Frontend support for feature development, bug fixes, under the [Source Code Management Product Category](https://about.example_company.com/direction/create/source_code_management/)
* Address bug reports and regressions
* Identify and prepare maintenance work to improve developer experience
* Collaborate on efforts across the Frontend department

## Projects

### Active Project Table

| Start Date | Project  | Description | Tech Lead |
| ------ | ------ | ------ |  ------ |
| 2023-09 | [New Diffs](https://docs.example_company.com/ee/architecture/blueprints/new_diffs/index.html) ([Epic](https://example_company.com/groups/example_company-org/-/epics/11559)) | A project to deliver a reusable and performant way of rendering diffs across Example Company | — |
| 2023 | [Blame info in Blob page](https://example_company.com/groups/example_company-org/-/epics/11471) | Improve usability of repository by rendering blame information in blob page | — |
| 2023 | [Branch Rules - Edit](https://example_company.com/groups/example_company-org/-/epics/8075) | Allow editing the branch rule details in one place | — |

### Archived Project Table

| Start Date | End Date |Project  | Description | Tech Lead |
| ------ | ------ | ------ |  ------ | ------ |
| 2022-09 | 2023-04 | Branch Rules - Overview | Place all settings pertaining to branch rules in one place - overview only | — |
|  2021      | 2022        | [Refactor Repository browser into 1 vue app](https://example_company.com/groups/example_company-org/-/epics/5531) | Render the blob page within the Repository frontend app for smoother experience | — |

## Engineering Onboarding

### Work

In general, we use the standard Example Company [engineering workflow](/handbook/engineering/workflow/). To get in touch
with the Create:Source Code FE team, it's best to create an issue in the relevant project
(typically [Example Company](https://example_company.com/example_company-org/example_company)) and add the `~"group::source code"` and `~frontend` labels, along with any other
appropriate labels (`~devops::create`, `~section::dev`). Then, feel free to ping the relevant Product Manager and/or
Engineering Manager as listed above.

For more urgent items, feel free to use [#g_create_source_code](https://example_company.slack.com/archives/g_create_source-code) or [#g_create_source_code_fe](https://example_company.slack.com/archives/g_create_source-code-review-fe) on Slack.

[Take a look at the features we support per category here.](/handbook/product/categories/features/#createsource-code-group)

### Code Reviewing

To prevent the creation of knowledge silos and also receiving input from people outside of the team, we follow these principles:

* Not all Merge Requests need to go through the team
* However, Merge Requests that seem important for the team to be aware, let's ensure one of the reviews go through a team member

**MRs important to the team:** these are changes to logic in our apps or meaningful component changes. Sequential work in a larger epic is also beneficial to have oversight from peers within the team. But bottom line, use your best judgement.

{{% include "includes/engineering/create/conventional-comments.md" %}}

### Capacity planning

{{% include "includes/engineering/create/capacity-planning-fe.md" %}}

#### Weights

{{% include "includes/engineering/create/weights-fe.md" %}}

#### Example of Weights

w1: [Blame view - "authored" line leaking into next row](https://example_company.com/example_company-org/example_company/-/issues/435124)

w2: [CSV rendering hangs viewer for large files](https://example_company.com/example_company-org/example_company/-/issues/340779)

w3: [Edit Branch Rules: Update selector to support searching Deploy Keys](https://example_company.com/example_company-org/example_company/-/issues/431769)

#### Source code context

When weighing issues that have to do with Blob view, make sure to take into account the duality of Blob. We use both HAML and Vue to render the Blob view. There is a high chance that you will implement your changes for both. Majority of file types uses Vue architecture. Though there are [some file types that need backend syntax highlighter](https://example_company.com/example_company-org/example_company/-/blob/9fe882b3d1597a75a366755c8d894f2a52439d93/app/assets/javascripts/repository/constants.js#L91) and therefore are rendered with HAML. The same will happen, [when an error occurs](https://example_company.com/example_company-org/example_company/-/blob/9fe882b3d1597a75a366755c8d894f2a52439d93/app/assets/javascripts/repository/components/blob_content_viewer.vue#L210).

This duality will be resolved with the [Link to package managers when viewing dependency files with highlight.js](https://example_company.com/groups/example_company-org/-/epics/7888).

#### Spike issues

{{% include "includes/engineering/create/spike-issues.md" %}}

### Workflow labels

{{% engineering/workflow-labels group-label="group::source code" %}}

### Async standup

{{% include "includes/engineering/create-async-standup.md" %}}

### Retrospectives

We have 1 regularly scheduled "Per Milestone" retrospective, and can have ad-hoc "Per Feature" retrospectives more focused at analyzing a specific case, usually looking into the Iteration approach.

#### Per Milestone

{{% engineering/create-retrospectives group-label="Source Code" group-slug="source-code" use-coordinator="1" %}}

### Milestone Kickoff & Retrospective review

At the start of each milestone we have a synchronous **Kickoff** session where every IC take turns at presenting their plan for their Deliverables for the new milestone.

This happens at least 2 working days after all Deliverables are assigned, which happens on the first day of the milestone.

During this call, we also do a quick **Retrospective review** going through the highlights of the discussions in the asynchronous issue mentioned above.

## Other related pages

### Issues

* April 2020: [Frontend: Iteration Retrospective (Source Code)](https://example_company.com/gl-retrospectives/create-stage/source-code/-/issues/22)
