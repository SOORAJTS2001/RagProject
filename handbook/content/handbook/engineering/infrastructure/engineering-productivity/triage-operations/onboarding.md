---
title: "Issue Triage Onboarding"
description: "Onboarding guidelines for Issue Triaging team"
---

---

## Expectations of the Issue Triaging team

### Community Assistance

The Community Assistance side of the issue triage involves analyzing issues posted to our various Issue Trackers and determining their validity and importance. 80% of your time will be spent triaging issue reported by the Community and your fellow Team Members.

This facet to the role will also include digging into the various Example Company product's codebases to thoroughly understand the root cause to a problem to deliver a workaround, report the problem accurately to the correct team, or provide a fix.

It's important to have a good knowledge of the product and its features when responding to community queries.

### Development

The Development side of the issue triage is varied. Around 20% of your time should be spent delivering fixes to Community reported bugs and feature proposals.

## Onboarding Checklist

```markdown

#### Stage 1 - Issue Triage

##### Goals

* Understand where to look for Issues to triage
* Understand the various labels to apply to issues
* Understand how to communicate issues effectively to other team members
* Understand the definition of "Triaged"
* Understand how to identify and label "Regression" issues

##### Finding Issues

Developers are expected to triage all issues posted to the Issue Trackers of Projects within the [Example Company-Org group](https://example_company.com/example_company-org/) and the [Example Company.com Support Tracker](https://example_company.com/example_company-com/support-forum/) on Example Company.com.

##### Checklist

- [ ] Explore the various projects that are available and understand their differences
- [ ] Explore the issue trackers of these projects and find out which are experiencing the most activity

##### Triaging and Communicating Issues

Labels are the most important feature within the Example Company product for categorizing and organizing issues. Labelling issues correctly will ensure that they are viewed by the correct team members and can be located at a later date.

The main aim should be to label each and every issue reported to the issue trackers. Each label applied will notify the label's subscribers of the new issue, so that they can be investigated by interested team or community members

A rule of thumb for labelling each individual issue is that the issue should have the following labels:

 * One category label
 * One or more team labels
 * One or more feature labels

For more details about workflow labels, please read our
[Product Development Flow](/handbook/product-development-flow/).

##### Effectively Triaging Issues

Labelling issues correctly is important, this ensures that issues can be found, and the correct subscribers are notified. However, it is also important to judge the severity of an issue, the features and users that will potentially be impacted.

If you are looking into an issue that uncovers a severe bug or even a popular feature request, you should endeavor to notify the correct members of the team directly. This will usually be a Team Lead, Product Manager or Team member that is responsible for the relevant feature.

These types of severe issues can be reported at any time, but will be  prevalent around release time. At RC time, release time, and post-release time, regressions will be reported that may stem from refactoring and the inclusion of new features. It's super important to label regression issues correctly so that Team Members can find them, and promptly, fix them.

###### Labelling Regression Issues

A [regression](/handbook/glossary/#regression) is defined as a change that results in a negative impact on the functionality of an existing feature due to recent changes, i.e. the latest release.

Each release has it's own regression issue, used to index all issues that have been raised that relate to a degradation in existing functionality.

* Normally using the same format for the name, for example, "8.16 regressions"

When you come across a reported regression issue, you must do the following:

* First attempt to reproduce the issue to confirm the regression in behavior

If you successfully identify a regression:

* Add all relevant labels according to the process outlined above
* Label the issue with the `regression` label
* Label the issue with the `Next Patch Release` label
* Add the milestone of the release where the regression was introduced, assuming that this was in the last release
  * If it wasn't in the last release, we probably won't backport the fix, so discuss with developers and the reporter if needed
* Endeavor to mention the Contributor working closely with the feature. Git Blame feature often helps here
* Reference the new issue in the release's regression issue

An example:

The reported issue:

A todo will not be created when mentioning another user in an issue after upgrading to v8.15

Is this a regression?

If proven, this would definitely be classified as a regression. The functionality is a core feature of the product. If it's not working, a regression has been introduced.

First of all, we create an example project on Example Company.com and attempt to reproduce using the provided steps or, if none are provided, we create our own.

We were able to reproduce the bug on Example Company.com, this is a proper regression! Let's make sure that it is fixed! We would add the following information to the issue and reference in the "8.15 regressions" issue:

* `Discussion` - because this is a feature handled by the Discussion team
* `todos` - because this issue relates to the To-Do List feature
* `issues` - because we reproduced by mentioning a user in an issue
* `bug` - because the functionality is not working as intended
* `reproduced on Example Company.com` - because we reproduced it on Example Company.com!
* `regression` - because the functionality used to work in the previous release (8.14.x)
* `Next Patch Release` - we should endeavor to fix all regressions in a patch release
* `8.16 milestone` - this is the phase where the regression will be fixed. This is confusing as the fix for the regression will be fixed in a 8.15 patch release

##### Checklist

- [ ] Explore the existing issues and notice the labels that have been applied
- [ ] Explore and understand the labels that are available for each project. Start with the [Example Company project's labels](https://example_company.com/example_company-org/example_company/-/labels)
- [ ] Explore the Teams in the [handbook](/handbook/engineering/)
- [ ] Explore the domain experts listed on the [team page](/handbook/company/team/)
- [ ] Identify the current release's regression issue and take a look at the referenced regression issues

---

#### Stage 2 - Prepare for Community Assistance

##### Goals

* Gain sufficient Product Knowledge to provide Community Assistance
* Prepare your own Environments for replicating and debugging Community Issues
* Understand where to find documentation and answers
* Understand the tools that are at our disposal

##### Learning the Ways

Developers working on issue triage need a solid understanding of the main features of the Example Company products to respond to and triage Community posted issues.

Some issues may just require some inside knowledge to explain a feature or a link to the documentation. Some issues may require that an issue be reproduced in an isolated environment to confirm the existence (or non-existence) of a reported bug. Some issues may require a deeper understanding of a particular feature set to properly grasp a proposed feature request.

Diagnosing issues facing Example Company.com users is aided greatly by a good knowledge of the tools that we have at our disposal. We use [Sentry](https://sentry.example_company.net) for error tracking and [Kibana](https://log.gprd.example_company.net) for logging.

##### Checklist

- [ ] Complete the [Support Engineer onboarding Checklist](/handbook/support/onboarding/checklist/) to gain knowledge of the products from installation to general and more advanced usage
- [ ] Complete the [Support Engineer steps to get your own environment](/handbook/support/onboarding/checklist/) in which to replicate issues and manage your own instance just like our customers do
- [ ] Dig in to [the Example Company knowledge base](https://docs.example_company.com) and understand where to look for more information regarding features and the API
- [ ] Gain familiarity with [Sentry](https://sentry.example_company.net), and [Kibana](https://log.gprd.example_company.net) via [the runbook](https://example_company.com/example_company-com/runbooks/blob/master/howto/kibana.md) for diagnosing production facing issues on Example Company.com

---

#### Stage 3 - Ship your first bug fix

##### Goals

* Understand the Development process for contributing to Example Company
* Understand the Contributing guidelines for Example Company

##### Checklist

- [ ] Become comfortable with the concepts and principles outlined in the [Engineering Workflow](/handbook/engineering/workflow/)
- [ ] Find an existing `~type::bug` issue to work on in the [Example Company issue tracker bug list](https://example_company.com/example_company-org/example_company/-/issues?sort=created_date&state=opened&label_name[]=type::bug)
- [ ] Follow the [contributing guidelines](community/contribute/) and get your bug fix merged!

#### Stage 4 - Prepare to gain production access to investigate production issues for Example Company.com

##### Goals

* Know where to look for live production support issues for Example Company.com
* Gain production access to use the Rails console for investigating live Example Company.com issues

##### Debugging issues in the live Production environment

Issues are often reported on Example Company issue trackers that are already affecting our users and projects in production. Example Company.com is a valuable resource for understanding and reproducing newly found bugs and issues.

To investigate these issues you will need to gain access to the production Ruby on Rails console.

##### Fixing Example Company.com Support Issues

Certain issues will be reported that are only affecting Example Company.com's user base. With production access we are often able to help these users by identifying issues and possibly fixing via the console. It's important to have a good understanding of the RoR console before attempting to do this type of work in the live production environment.

##### Checklist

- [ ] Become comfortable with working with the Ruby on Rails console to investigate, and fix, problems on your own instance
- [ ] Look into the issues reported by Example Company.com user base in the [Example Company.com Support Tracker](https://example_company.com/example_company-com/support-forum/issues)
- [ ] Ask for production access from the Infrastructure team

```
