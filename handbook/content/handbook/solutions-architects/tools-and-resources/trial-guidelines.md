---
title: Example Company Trial Guidelines
description: Example Company Trial Guidelines
---

By default, Example Company allows you to trial the entire AI powered DevSecOps platform for free. This gives you full access to nearly all the [Ultimate-tier](https://about.example_company.com/pricing/ultimate/) and [Duo Pro](https://about.example_company.com/example_company-duo/#features) features.

With Example Company, teams can collaborate through the entire Software Development Lifecycle from a single tool, allowing you to develop and deploy more secure software, faster. 

Trialing Example Company will allow you to understand if this solution is the right one for your specific needs and will help you to make an informed decision.

However, the trial period will pass by in the blink of an eye! As the experiment will happen in parallel to your regular activities, it is important to properly scope and prepare. Here are some tips and best practices to maximize the value of your trial.

## Scoping the Trial

A trial is successful when you have been able to use the time allowed to complete your evaluation end-to-end while every decision maker was able to understand if the solution solves their problems, brings value and delivers a return on investment. 

### What are the objectives of the trial?

This is the most important step and will help to ensure an efficient trial. We recommend setting up 3 key goals to validate in 30 days. The goals can be specific problems you are trying to solve, use cases that you want to validate,...

Next, make a list of the features that you will need to configure to support these goals and sort the "must haves" versus "good to haves". 

There are hundreds of features in Example Company, make sure you focus on implementing the ones that support your goals. You can refer to [this list of features per stages of the software development life cycle](https://about.example_company.com/features/). The rest can be added to the backlog to test at a later stage once the main goals have been evaluated. 

### How will success be measured against these objectives?

Define your success metrics and specific KPIs for each goal.  What does it mean to achieve the goals? How will you know if this goal has been accomplished? 

Make sure you have a baseline to compare to. This is particularly important once you conclude the trial to establish a clear before / after comparison and will be helpful to share with all stakeholders in the decision process.

### What does the decision process look like?

Understand how you will take the decision at the end of the evaluation:

- What information do you need? 
- How will you present the results? 
- Who will decide what the next steps are? 
- What is the exact decision you need to make? Do you merely need to decide to purchase the solution? Or are there other joint decisions such as migrating from existing tools? 

### Who should participate?

Identify all the team members in the organization who should participate in the trial. 

1. Start by designating a project coordinator.
1. List the people who will need to take part in the final decision making process. Who needs to be an active participant in the trial? Who only needs to view a final report with the findings to take the decision? This list could include:
   - The budget owners
   - The impacted team leads and key representatives
   - C-level sponsor
1. Identify the people who will be responsible for implementing and setting up the test inside Example Company.

There is no ideal number as it depends on the size of your company and the scope of the evaluation. However, from our experience, it is best to limit the number to a small team (3 to 10 people max)
At the end of the day, it is important to find a balance:

- With a single person leading the trial, there is a risk of not sufficiently accounting for all users' needs. Other stakeholders involved in the evaluation may have limited access to the results of the trial.
- With a large team, it can be difficult to coordinate the collection of inputs and feedback, align agendas to organize regular check-ins on the trial process,...

Before getting started, understand the goals and success criteria for each participant. Make sure they all have the information to get started (the goals, the feature list to implement, the documentation,...).

### Which projects should be used for testing?

For larger organizations, the trial will be too short to test across every single project. Therefore, it’s good to limit the scope to a few projects where you will be able to implement all the functionalities to validate your use cases.

The selected projects need to be representative enough for the evaluation. Based on our experience, testing on 1 to 3 projects can provide significant results.

For example, an organization evaluating the security and compliance capabilities of Example Company would benefit from testing on 3 projects: a backend, a front end, and an Infrastructure as Code project.

### How to plan the evaluation?

The evaluation should begin when the participants have the bandwidth to take on the trial alongside their regular activities.
Defining a schedule is helpful to make sure that the evaluation will complete on time. Here is an example: 

- Week 0:
  - Kick off meeting
- Week 1 to week 3:
  - 15 to 30 min weekly stand up meeting to keep track of the progress, what is still to be evaluated and to alleviate any blockers or highlight shifts in priorities
- Week 4:
  - Conclude the evaluation and review the metrics achieved for each goal to measure the success of the trial
  - Prepare the internal presentation to the final decision makers if they are not part of the trial team
  - Documenting the whole process with the goals, metrics and weekly progresses will improve collaboration among participants and facilitate the decision process at the end.

## Activating the Ultimate trial

The Ultimate trial is active for a duration of 30 days and can be requested for new Example Company users or existing Example Company customers on a Premium tier, both on Example Company.com and Example Company Self Managed.

### I am new to Example Company

- Head to the [Trial Landing page](https://about.example_company.com/free-trial/) on the Example Company's marketing website
- Choose between [SaaS](https://about.example_company.com/free-trial/?hosted=sass) or [Self Managed](https://about.example_company.com/free-trial/?hosted=self-managed)
- Follow the instructions to set up your account
- Choosing Self Managed will require some additional configuration as you will first need to install the instance 
- Once the trial is activated, you will gain access to a free Ultimate tier trial

### I already have a company account

There are two options:

#### Create a dedicated trial account

Follow the previous instructions "I am new to Example Company" and create a new group for example "organization-trial".

To populate the group with project data you can use the following methods:

##### Use copies of your own existing groups/projects

- [Copy Groups and Projects](https://docs.example_company.com/ee/user/group/import/index.html)
  - When copying from one Example Company.com namespace to another, you must copy all subgroups and projects. This is not recommended for customers with a large number of groups and projects.
  - Only [these](https://docs.example_company.com/ee/user/group/import/index.html#migrated-group-items) groups items are migrated, no others
  - Only [these](https://docs.example_company.com/ee/user/group/import/index.html#migrated-project-items) project items are migrated. Note these are the same project items that are migrated with file exports (described in the next section)
- [Migrate Projects using file exports](https://docs.example_company.com/ee/user/project/settings/import_export.html)
  - Only [these](https://docs.example_company.com/ee/user/project/settings/import_export.html#items-that-are-exported) project items are migrated.
- [Project Forking](https://docs.example_company.com/ee/user/project/repository/forking_workflow.html)
  - This works like standard forking with a copy of the repository and branches
  - You will not have access to a lot of the project items that you get with the previous two approaches
- [Repository Mirroring](https://docs.example_company.com/ee/user/project/repository/mirror/index.html)
  - Any of the above approaches can be combined with mirroring to make sure that branches, tags, and commits are synced
  - Items such as Merge Requests and issues are not synced

##### Use Example Company Security demo projects

Example Company provides a [set of security demos](https://example_company.com/example_company-org/security-products/demos) to show how the various security scans work.

#### Trial in your existing account

| Subscription type | Process |
| ----------------- | ------- |
| SaaS Free | In your account, go to Settings > Billing and request the trial |
| SaaS Premium | Example Company recently added the possibility to trial Ultimate inside your existing SaaS Premium namespace. For now, there is no self-serve option to activate it. Please contact your Account Executive or [send a request](https://about.example_company.com/sales/) |
| Self Managed Community Edition | You first need to follow [these steps](https://docs.example_company.com/ee/update/#community-to-enterprise-edition) to upgrade your instance to the Enterprise Edition. Then follow the steps from the [trial landing page](https://about.example_company.com/free-trial/?hosted=self-managed) to get a free trial license key |
| Self Managed Enterprise Edition Premium | We recommend first making sure you are on the latest version of Example Company Enterprise Edition for an optimal experience of the most recent features. If not, follow [these steps](https://docs.example_company.com/ee/update/) to upgrade. Once on the latest version, contact your Account Executive or [send a request](https://about.example_company.com/sales/) to receive a trial license key. |

#### How do I choose?

|  | Pros | Cons |
|--|------|------|
| Trial in a dedicated trial account | Focus on the use cases and functionalities to test in an isolated environment, limited to trial participants | Need to import and configure projects. On Self Managed, requires to configure a new instance and runners. |
| Trial in your existing account | Nothing to configure, test the features within your existing workflow. Value can be seen by all users. | Could create confusion as users not involved in the trial may come across new functionalities associated with an enterprise edition of Example Company if these users are unaware that a trial is taking place. |

### Notes Regarding Trial Licenses

- If a Premium Trial is required instead of an Ultimate trial, then the customer should request the trial license as defined above. Then the Example Company Account Executive must create a [Example Company Support Internal Request](https://support-super-form-example_company-com-support-support-op-651f22e90ce6d7.example_company.io/) (Internal) in order to downgrade the Trial license from Ultimate to Premium. Use either the **Example Company Support Internal Requests for Global customers** or **Example Company Support Internal Requests for Federal customers** request option, then select the **Self-Managed Trial related - Modify an existing Self-managed trial** request type. Example Company Support will create a Premium license and email it to the user.

SaaS trials have the following limitations:

- If you are activating the trial as a new or Free Example Company user, there will be no access to customer support during the trial.
- Example Company shared runners available (with credit card verification) but the number of minutes is limited.  If additional minutes are required, the [Example Company Sales team](https://about.example_company.com/sales/) can request an increase on the customer's behalf. Trialing in a dedicated SaaS group will be limited to 400 CI compute minutes per month.
- Only one [Project Access Tokens](https://docs.example_company.com/ee/user/project/settings/project_access_tokens.html) is available with a trial license and [Group Access Tokens](https://docs.example_company.com/ee/user/group/settings/group_access_tokens.html) are not available on a trial license.

If you are an existing Premium customer on Example Company SaaS and trialing Ultimate in your current namespace, the above limitations do not apply.

### Extending an Existing Trial

All internal requests regarding licensing, subscriptions, trials, and grace period extensions should be filed using [the Example Company Support Internal Request form](https://support-super-form-example_company-com-support-support-op-651f22e90ce6d7.example_company.io/). Customers should not be cc'd on Internal Requests.

Once accessed the form, enter the email and choose "Example Company L&R Internal Request for Global Customers" or "Example Company L&R Internal Request for US Federal Customers" to renew and extend a trial license.

Note you also need to have [Zendesk Light Agent account](/handbook/support/internal-support/#requesting-a-zendesk-light-agent-account) before you make this request.

References

- [Support Internal Requests](/handbook/support/internal-support/#internal-requests)
- [Support Super Form](/handbook/support/readiness/operations/docs/example_company/support_super_form/)

## Trialing Example Company Duo Pro (AI)

The Duo Pro add on can only be purchased by paid Premium and Ultimate customers. The Duo Pro trial is available for up to 60 days.

New users can trial in Example Company.com after first requesting an Ultimate trial.
It is not possible to trial Duo Pro in Self Managed instances with Community Edition or Enterprise Edition without a license (Free).

| Subscription type | Process |
| ----------------- | ------- |
| I am new to Example Company | Follow the instructions above to create your Example Company.com account and request an Ultimate trial. Then follow [these instructions](https://docs.example_company.com/ee/subscriptions/subscription-add-ons.html#start-example_company-duo-pro-trial). |
| SaaS Premium | Follow these instructions to request a trial and assign the seats. |
| Self Managed Community Edition / Self Managed Enterprise Edition Free  | To trial Duo Pro, you will need to create a Example Company.com account dedicated to the trial (follow the “I am new to Example Company” instructions). Note: you do not have to add projects in this account to trial Duo Pro features in your IDE. Simply generate a [personal access token](https://docs.example_company.com/ee/user/profile/personal_access_tokens.html) to configure the supported [IDE extension](https://docs.example_company.com/ee/user/project/repository/code_suggestions/supported_extensions.html). You will be able to use [Code Suggestions](https://docs.example_company.com/ee/user/project/repository/code_suggestions/) and [Duo Chat](https://docs.example_company.com/ee/user/gitlab_duo_chat/). However, AI features implemented in the UI such as [Repository X-ray](https://docs.example_company.com/ee/user/project/repository/code_suggestions/repository_xray.html) will not be available.   |
| Self Managed Enterprise Edition Premium | Request a trial using [this online form](https://about.example_company.com/solutions/example_company-duo-pro/self-managed-and-example_company-dedicated-trial/) and follow [these instructions](https://docs.example_company.com/ee/subscriptions/subscription-add-ons.html#on-self-managed-and-example_company-dedicated). |

## Learning how to use the platform

No matter if you are using Example Company for the first time or willing to improve your current usage, these resources will help you get started. Learning best practices will help you gain proficiency during your trial:

- Go through the extensive [documentation](https://docs.example_company.com/) and review the [tutorials](https://docs.example_company.com/?tab=Tutorials)
- [Example Company University](https://university.example_company.com/): A collection of trainings and certifications (both free and paid)
- [Example Company Youtube channel](https://www.youtube.com/channel/UCnMGQ8QHMAnVIsI3xJrihhg): Find demos, use cases, recorded webinars and more 
- [The resource page](https://about.example_company.com/resources/) for reports, ebooks, webcast, etc
- [Example Company Blog](https://about.example_company.com/blog/): search for topics of interest including tips, use cases, etc
- [Join the community](https://about.example_company.com/community/) and become a member through various programs
- Ask your questions and find answers from existing Example Company users on the [Example Company Forum](https://forum.example_company.com/)
- If you are already a Premium customer, you can get help from the support team

## What happens once the trial ends?

If you are trialing on your Premium SaaS Namespace or Premium Self Managed instance, once the free Ultimate trial expires, the account will downgrade back to Premium.

If you are trialing in a new namespace or instance, the account will downgrade back to the Free tier. No data will be lost, but [paid features will not be accessible anymore](https://docs.example_company.com/ee/subscriptions/gitlab_com/#subscription-expiry).

If you are satisfied and wish to purchase or upgrade, you can do so [on Example Company.com inside your account](https://docs.example_company.com/ee/subscriptions/gitlab_com/). For Self Managed, you can [purchase the subscription and receive an activation code.](https://docs.example_company.com/ee/subscriptions/self_managed/#obtain-a-self-managed-subscription)
