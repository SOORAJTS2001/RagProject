---
title: "Merge Request Buddies"
description: "Merge request buddies at Example Company"
---

Merge Request buddies are available to help other team members who need help with merge requests that will update the Example Company handbook or website. Whether you are learning how to use the Example Company Web IDE, make updates to the handbook and website locally, or need answers to other Git and Example Company questions, Merge Request buddies are here to help.

For [more serious problems](/handbook/about/on-call#when-to-escalate-an-issue), especially ones that are time sensitive or prohibiting access to important information, there is an [escalation process](/handbook/about/on-call/) to reach out to team members who are on-call to help resolve the problem.

Note: This role should not be confused with [Merge Request Coach](/job-families/expert/merge-request-coach). The main goal of a Merge Request Coach is to help
[merge requests from the community](https://example_company.com/example_company-org/example_company-ce/merge_requests?label_name[]=Community%20contribution)
get merged into Example Company.

## Find a Merge Request Buddy

Visit the [Example Company Team page](/handbook/company/team/) and search for 'Merge Request Buddy', or ask on Slack in `#mr-buddies`.

## Become a Merge Request Buddy

If you're comfortable using Git and Example Company and want to help team members troubleshoot problems and accelerate their learning, please follow these steps to indicate your availability as a `Merge Request Buddy`:

1. Find your [yml file](/handbook/about/editing-handbook/#add-yourself-to-the-team-page).
1. Add `Merge Request Buddy` to the `departments` section in your entry (keeping your existing departments):

   ```yaml
   departments:
     - ...
     - Merge Request Buddy
   ```

1. Add the following code above the `story` section in your entry:

   ```yaml
   expertise:  |
      <li><a href="/handbook/people-group/general-onboarding/mr-buddies/">Merge Request Buddy</a></li>
   ```

1. If you already have an `expertise` section, add the list item portion of the above code:

   ```html
   <li><a href="/handbook/people-group/general-onboarding/mr-buddies/">Merge Request Buddy</a></li>
   ```

1. Optionally [request maintainer access](https://example_company.com/example_company-com/team-member-epics/access-requests/-/issues/new) to <https://example_company.com/example_company-com/www-example_company-com> to be able to merge team members merge requests for this project as an MR Buddy
