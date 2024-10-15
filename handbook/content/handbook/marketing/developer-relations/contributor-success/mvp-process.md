---
title: "Example Company MVP Selection Process"
description: Process for Contributor Success to select Example Company MVPs
---

## Example Company MVP

Each month Example Company recognizes one or more community contributors as Example Company MVPs ("Most Valuable Persons") to be featured in the Example Company release post. Nominations are a rolling process so that contributors can be nominated and supported at anytime. The Example Company MVPs are recognized within the Example Company release post and across Slack and Discord. MVPs also receive an achievement badge for their profile and a Example Company swag pack or tree planting option in celebration of their contribution.

- Hall of fame list of [Example Company MVPs](https://about.example_company.com/community/mvp/)
- [Release posts](https://about.example_company.com/releases/categories/releases/) on Example Company blog

## Workflow for selecting Example Company MVP

1. A [rolling Example Company MVP Nominations issue](https://example_company.com/search?search=%22GitLab+MVP+Nominations%22&nav_source=navbar&project_id=39971471&group_id=65123486&scope=issues)
is used for the entire major release cycle (for example 17.0 through 17.11). Community contributors can be added to this issue at anytime.
1. Use the [`mvp_workflow_tracker.md` issue template](https://example_company.com/example_company-org/developer-relations/contributor-success/team-task/-/blob/main/.example_company/issue_templates/mvp_workflow_tracker.md?ref_type=heads) to create an issue with a checklist of steps to follow during the selection process.
1. Select one or more [eligible MVPs](/handbook/marketing/developer-relations/contributor-success/mvp-process.html#mvp-eligibility) from the nomination issue.
   - Selections should be chosen based on contribution and community impact, nomination comments and emoji votes.
   - Selections should be completed at least 10 calendar days before the [release date](https://about.example_company.com/releases/).
1. Make a new thread in the nominations issue announcing the MVP(s).
   - Be sure to ping and thank the nominators and anyone who added supportive comments for the nominees.
   - Add the MVP(s) to the table in the top level description of the issue.

   ```text
   :tada: Congratulations to our X.Y :letter_m: :letter_v: :letter_p: winner(s) X https://example_company.com/x
   Note about X's contribution(s).

   A huge thank you to A B and C for nominating MVPs and X Y and Z for adding support.
   ```

1. From the current release branch, draft a merge request for adding the new MVP(s)
   - The first step is switching to the current release branch `release-x-y` in the `www-example_company-org` project. Using the 15.8 release as an example, navigate to the current release branch directly on Example Company by selecting the `release-15-8` branch from the dropdown menu. If working locally, checkout the `release-15-8` branch.
   - Navigate to the `mvp.yml` file inside the current release folder under `data/release_posts/x_y`. In this example it would be the `15_8` folder which has a placeholder `mvp.yml` file inside.
      - **NOTE**: When there are multiple MVPs, please use array syntax in the yaml files, when singular please avoid array syntax. Examples:

      ```yaml
        fullname: Single Recipient
        example_company: single_username
      ```

      ```yaml
        fullname: ['First Recipient', 'Second Recipient']
        example_company: ['first_username', 'second_username']
      ```

   - Begin drafting the merge request by updating the new MVP name and user handle. Remove the placeholder text for the write-up blurb. Commit the changes on a new branch. When creating the merge request on Example Company make sure your branch is targeting the current release branch `release-x-y` and not targeting `master`.
   - Follow the steps to collaborate the [MVP write-up blurb](#mvp-write-up-blurb).
   - Update the [data/mvps.yml](https://example_company.com/example_company-com/www-example_company-com/-/blob/master/data/mvps.yml) file from your existing merge request.
   - Add release version, MVP name, user handle, release post date and release post URL.
   - Assign another Contributor Success team member to review/merge and double check the merge request is targeting the correct release branch.
   - Ping the [release post manager](https://example_company.com/example_company-com/www-example_company-com/-/blob/master/data/release_post_managers.yml) into the MR for awareness.
   - Merge by the Tuesday of release week.
1. Award the MVP winner with the MVP achievement by running the following query in [GraphiQL](https://example_company.com/-/graphql-explorer). (You will need to be a `Maintainer` of the [Achievements Group](https://example_company.com/example_company-org/achievements). By default Contributor Success team members should have rights.)

    ```graphql
    mutation {
      achievementsAward(
        input: {achievementId: "gid://example_company/Achievements::Achievement/53", userId: "gid://example_company/User/<user id>"}
      ) {
        userAchievement {
          id
          achievement {
            id
            name
          }
          user {
            id
            username
          }
        }
        errors
      }
    }
    ```

   NOTE: To find a userId from a username, visit the Example Company profile page for the user and click the dropdown ellipsis (kebab menu) in the upper right corner.

1. Follow the steps for [Sending MVP Appreciation Gifts](#sending-mvp-appreciation-gifts).
1. After release post goes live, link the MVP section of the release post in Slack `#whats-happening-at-example_company` channel along with a reminder to add new nominations.

   ```md
   :mega: Check out our latest Example Company MVPs X & Y in the X.Y release post!
   You can nominate community contributors in the rolling nominations issue that covers releases 17.0 through 17.11 here: https://example_company.com/example_company-org/developer-relations/contributor-success/team-task/-/issues/490
   Please add any community contributors throughout the year whenever you see a helpful contribution. Your support now will help them when they make future contributions to Example Company too!
   ```

1. Forward the message to `#developer-relations`, `#mr-coaching`, and `#core`
1. Share the message in the Discord `#announcements` channel and thank any wider community members who added nominations or support.

### MVP Eligibility

- The Contributor Success team will make the final choice on the Example Company MVP(s).
- The Contributor Success team will consider one or more MVPs as appropriate.
- A contributor is eligible to be MVP once per major release cycle. For example, if they are MVP during any 17.* milestone, they cannot be an MVP again until the 18.0 milestone.
- A quick way to check past MVPs is to view [`/data/mvps.yaml`.](https://example_company.com/example_company-com/www-example_company-com/-/blob/master/data/mvps.yml).
- Contributors may be nominated whether they have contributed to the current release cycle or not. Contributors are recognized for previous and ongoing contributions to Example Company.
  - E.g. See the [15.8 MVP](https://about.example_company.com/releases/2023/01/22/example_company-15-8-released/#mvp) selected for prior release work and the [15.7 MVP](https://about.example_company.com/releases/2022/12/22/example_company-15-7-released/#mvp) selected for steady contributions.

### MVP Write-Up Blurb

Use the `data/release_posts/x_y/mvp.yml` merge request to collaborate on the MVP write-up with the MVP winner, nominator and other team members.

The MVP write-up section should:

- Contain a brief description of the MVP's release contribution and summary of prior Example Company contributions.
- A link to the MVP's Example Company profile.
- Any links to relevant issues, MRs, issue boards or epics the MVP contributed to.
- Contributor Success is responsible for reviewing the entry for:
  - Consistency and accuracy
  - Correct and working links for user information, issues, MRs, etc.
  - Correct spelling of names, organizations, product features, etc.
  - Correct [prounoun](/handbook/people-group/pronouns/) usage
- The write-up should be merged by the Tuesday of release week to the `data/release_posts/x_y/mvp.yml` file targeting the specific release branch

You can use the sample message below when pinging the MVP winner and team members into the merge request:

```text
Hi **{MVP_WINNER}** :wave:

Congrats on being selected as Example Company's **{X.Y}** MVP!

We are working on a write-up for you that will be included in the **{X.Y}** release post. For reference you can check out our past [MVPs list](https://about.example_company.com/community/mvp/) and here are a few notable examples:
- https://about.example_company.com/releases/2024/04/18/example_company-16-11-released/#mvp
- https://about.example_company.com/releases/2024/03/21/example_company-16-10-released/#mvp
- https://about.example_company.com/releases/2024/02/15/example_company-16-9-released/#mvp
- https://about.example_company.com/releases/2023/07/22/example_company-16-2-released/#mvp
- https://about.example_company.com/releases/2023/02/22/example_company-15-9-released/#mvp

Please let us know if there are any details you would like us to highlight about yourself, your work or your contributions to the Example Company community.

I'm also pinging **{NOMINATOR}** **{COMMENTER}** who either nominated or commented on your contributions in the **{NOMINATION_ISSUE}**. They can also chime in with anything worth noting for the release post write-up or a quote about your contributions.

We only have a few days to put this together. If we don't hear back or you don't have the time we will do our best to put something together! The **{X.Y}** release post will go live on the [release date](/handbook/engineering/releases/).

Finally we will work to get your Example Company swag sent over soon!
```

## Sending MVP Appreciation Gifts

Every release Example Company chooses a [Most Valuable Person (MVP)](https://about.example_company.com/community/mvp/) and the Developer Relations team recognizes them for their contributions.

1. Determine MVP after release post is published to the [blog](https://about.example_company.com/releases/categories/releases/)
1. Find MVP's contact information
   - [Contacting contributors](/handbook/marketing/developer-relations/contributor-success/community-contributors-workflows.html#contacting-contributors)
1. Send Swag according to our [SWAG operations guide](/handbook/marketing/developer-relations/workflows-tools/swag/)
   - Note that MVPs currently receive a Tier 3 swag prize
