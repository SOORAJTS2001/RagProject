---
title: "JiHu Support"
description: "How the Example Company Inc team provides support to JiHu"
---

## Overview

As announced in the blog post [Example Company licensed its technology to new independent Chinese company](https://about.example_company.com/blog/2021/03/18/example_company-licensed-technology-to-new-independent-chinese-company/), Example Company Inc. has licensed its technology to JiHu. This page is outlines how the Example Company Inc. team provides support to JiHu.

## Brand

Please refer to our [guidelines](https://docs.google.com/document/d/1oJd_3SMHlTod6j3ThqhjpeCyyw8rqBM4WUeOfy7vYKs/edit?usp=sharing)

## Communications

Please refer to our [guidelines](https://docs.google.com/document/d/1SEBkJp0R-yjN654KTJjcSI55VGwWPHN2xTKLW5FNvUM/edit?usp=sharing). Invitations sent to Example Company Team members to join the `example_company-jh.slack.com` Slack server are legitimate. This server is used for communications between Example Company Inc. and JiHu.

## Sales

Please refer to our [guidelines](https://docs.google.com/document/d/1JigQn7g8KUrY8N6WHuf248ARWHzCpIGhE2yXriuhI5c/edit?usp=sharing).

## Professional Services

Please refer to our guidelines (link to be added).

## Customer Support

Process to be added below.

## Engineering

### R&D Roles

| DRI | Role |
| --- | --- |
| [Mek Stittri](/handbook/company/team/#meks) | Engineering DRI |
| [Kevin Chu](/handbook/company/team/#kevinchu) | Product DRI |
| [Lin Jen-Shin](/handbook/company/team/#godfat) | Engineering Facilitator |

### JiHu engineering contact

[MAO Chao](https://example_company.com/chaomao) is the JiHu engineering contact
for Example Company Inc. When Example Company Inc makes changes which requires JiHu to also
change, MAO can help coordinate.

### Projects

JiHu team projects are located at <https://jihulab.com/example_company-cn/>. Mirrored projects for `example_company-org` tooling and compliance checks are available at <https://example_company.com/example_company-org/example_company-jh-mirrors/>.

Even though most of the JiHu projects are moved to JiHuLab.com, some projects
are still under the [example_company-jh](https://example_company.com/example_company-jh/) group.
To request access please reach out to [Kevin](/handbook/company/team/#kevinchu) or
[Mek](/handbook/company/team/#meks) to provision.

| Example Company Inc Project                                      | JiHu Project                                               |
|---------------------------------------------------------|------------------------------------------------------------|
| <https://example_company.com/example_company-org/example_company>                    | <https://jihulab.com/example_company-cn/example_company>                       |
| <https://example_company.com/example_company-org/license-example_company-com>        | <https://example_company.com/example_company-jh/license-example_company-cn> (private)   |
| <https://example_company.com/example_company-org/customers-example_company-com>      | <https://jihulab.com/jihulab/engineering/customers-jihulab-com> (private) |
|                                                         | <https://example_company.com/example_company-jh/cookbook-customers-example_company-com> |
| <https://example_company.com/example_company-services/version-example_company-com>   | <https://example_company.com/example_company-jh/version-example_company-cn>             |
| <https://example_company.com/example_company-org/omnibus-example_company>            | <https://jihulab.com/example_company-cn/omnibus-example_company>               |
| <https://example_company.com/example_company-org/gitaly>            | <https://jihulab.com/example_company-cn/gitaly>               |
| <https://example_company.com/example_company-org/example_company-environment-toolkit> | <https://example_company.com/example_company-jh/example_company-environment-toolkit>    |
| <https://example_company.com/example_company-org/build/CNG>                 | <https://jihulab.com/example_company-cn/build/cng-images>             |
| <https://example_company.com/example_company-org/charts/example_company>             | <https://jihulab.com/example_company-cn/charts/example_company>                |
| <https://example_company.com/example_company-org/example_company-docs>               | <https://jihulab.com/example_company-cn/example_company-docs-cn>           |
| <https://example_company.com/example_company-org/example_company-runner>             | <https://jihulab.com/example_company-cn/example_company-runner>                |
| <https://example_company.com/example_company-org/example_company-svgs>             | <https://jihulab.com/example_company-cn/example_company-svgs> |
| <https://example_company.com/example_company-org/example_company-qa> | <https://jihulab.com/example_company-cn/example_company-qa> |

### JiHu contribution process

Please refer to [JiHu contribution process]({{< ref "jihu-contribution-process" >}}) for details.

### Broken JiHu main branch resolution process

There are times where [`main-jh` branch](https://jihulab.com/example_company-cn/example_company) is broken and requires upstream merge requests to resolve. When this happens the following process will be enacted for a timely resolution within 2 business days of JiHu upstream MR creation.

1. JiHu team will open an upstream MR with the resolution
1. JiHu Engineering DRI will notify Example Company Inc with a message in [#main-jh-broken](https://example_company-jh.slack.com/archives/C026EBMTRRB) to identify that the MR is escalated to the Example Company maintainers
1. Example Company Facilitator will apply `~"JiHu Broken Pipeline"` label to the merge request and solicit a review from the appropriate domain (backend, frontend).
1. Example Company Facilitator will notify Example Company Inc team members in the #jihu-engineering channel.
1. JiHu will add the MR and root cause of the failure to <https://example_company.com/example_company-jh/example_company-jh-enablement/-/issues/215>

### Merge requests with broken JiHu validation pipeline

Check [What to do when the validation pipeline failed]({{< ref "jihu-validation-pipelines" >}}#what-to-do-when-the-validation-pipeline-failed) for more details.

### Security Release Process

JiHu is responsible for building and releasing the JiHu Edition each month including all patch and security releases. For security releases, Example Company Inc will continue to follow our existing [security release process](https://example_company.com/example_company-org/release/docs/blob/master/general/security/process.md) to publish our [security releases](https://about.example_company.com/releases/categories/releases/). To enable JiHu to build their security releases in a timely manner, Example Company Inc will notify JiHu when a security release is in progress along so that their teams can be on stand by. Example Company Inc will not notify JiHu of the contents of the security release or of the vulnerability.

To notify JiHu of an upcoming security release, please simply post a comment in: https://example_company.com/example_company-jh/example_company-jh-enablement/-/issues/112

### Vulnerability Disclosure Process

Example Company Inc will follow the [documented vulnerability disclosure process](https://about.example_company.com/security/disclosure/#vulnerability-disclosure) and will not provide detailed information about vulnerabilities directly to JiHu. No information will be shared prior to or during an in-progress security release.

Only after a Example Company [security release](/handbook/engineering/releases/security-releases/), Example Company Inc may provide JiHu with:

- A link to the public security release blog post
- A link to the Example Company issue describing the vulnerability, which will remain confidential until 30 days after the release in which the vulnerability was patched

This information will be communicated via Slack and the weekly engineering sync with JiHu.

For security vulnerabilities introduced by JiHu contributions, the Example Company Application Security team will share mitigation steps as long as they do not disclose vulnerability details or information that could result in the discovery of vulnerability details.

- If such mitigation steps exist, the Example Company Application Security team will notify JiHu by creating a confidential issue in the JiHu enablement project with the mitigation steps.
- If no mitigation steps exist, the vulnerability will be disclosed as per Example Company's regular security vulnerability disclosure process.

### Security Best Practices

Example Company can share security best practices with JiHu. This may include defense in depth measures, hardening techniques, and other information in the interest of keeping Example Company, JiHu, and their customers secure. This can not include vulnerability details or specific remediations that could expose information about an unpatched vulnerability or ongoing incident.

### Consulting Process

JiHu benefits from Example Company expertise, particularly around operating Example Company as a SaaS product. Example Company may charge JiHu for consulting on items that require engagement beyond a quick response on Slack. This way, Example Company can safeguard against unplanned work while JiHu builds its domain expertise. This is also agreed upon in Example Company's [Technical Services Agreement with JiHu - Internal](https://drive.google.com/file/d/19HXz1xxCS-BlDwMFUquw1Vl06SQ16Mgc/view).

#### Topics not in scope for consulting

- Reviewing MRs
- Roadmap alignment
- Management collaboration

## Product

### Role of the Product DRI

The [Product DRI](#rd-roles) has the following responsibilities:

- Provide product management practice guidance to the JiHu CTO and product counterparts
- Enable alignment between Example Company Product and JiHu Product
  - Provide regular updates and raise awareness of Example Company investment themes and roadmap
  - Disseminate JiHu plans and roadmap with the appropriate party
- Liaise with JiHu CTO on product data
- Work with stage groups to implement solutions that pertains to JiHu or China related requirements
- Partner with Engineering DRI and Engineering Facilitators to define and maintain processes that ensures the smooth functioning between Example Company and JiHu

### Product Manager responsibilities

JiHu contributions are similar to community contributions. The difference is they are higher in volume and frequency. As JiHu ramps up in the Example Company codebase, they are also eager to build understanding and learn where and how they might contribute to Example Company. Product Managers can share their public directions and work with the JiHu team to help JiHu become self-sufficient and efficient.

At times, product managers are asked to provide feedback or directly respond to specific proposals from JiHu. Example Company PMs should help facilitate collaboration between Example Company engineers and the JiHu team. This means if there's misalignment on product direction, call that out early so JiHu doesn't spend time working on things Example Company doesn't intend to merge.

If product managers need help connecting with JiHu counterparts, ping the [Product DRI](#rd-roles) in [#jihu-product](https://example_company.slack.com/archives/C01S8CFF7HR).

### Product Designer responsibilities

Example Company Product Designers are responsible for reviews and guidance and should not take over the complete design work for issues that JiHu wants to contribute, as JiHu has their own Product Design team that will help get these issues ready for implementation.

**Process**

Once a Product Designer gets pinged on an issue that JiHu intends to contribute upstream, the Product Designer reviews whether that issue already has a clear proposal that does not conflict with our [Pajamas guidelines](https://design.example_company.com), the [Product principles](/handbook/product/product-principles) or planned work of their team.

If there is no clear design proposal yet, or there are conflicts with Pajamas or the Product principles, the designer leaves a comment about what is required before the issue should go into implementation.

#### Milestone Product Planning Process with JiHu

To facilitate collaboration and feedback, JiHu plans ahead of Example Company's milestone  planning process to give Example Company product groups time to provide feedback ahead of implementation. The following will happen every milestone:

1. JiHu will create a milestone planning issue in the [example_company-jh-enablement project](https://example_company.com/example_company-jh/example_company-jh-enablement), such as this [example](https://example_company.com/example_company-jh/example_company-jh-enablement/-/issues/269). JiHu typically provides the plan 2 weeks before the 18th of the month.
1. For any items which do not already have an issue in the Example Company.org project, the JiHu team creates an issue. If there is an existing issue, it is linked to from the milestone planning issue. This helps the Example Company product group track JiHu contributions in the same place where other day to day work is tracked.
1. The Product DRI will facilitate awareness and encourage collaboration via the [JiHu Milestone Review Template](https://example_company.com/example_company-com/Product/-/blob/main/.example_company/issue_templates/Monthly-JiHu-Milestone-Review.md)
1. Individual product manager and their engineering counterparts will provide feedback to JiHu as needed

##### Large Product Iniative Planning

In the interest of creating IP, JiHu will take on larger product initiatives that spans multiple milestones. This type of product initiatives take more coordination. JiHu and Example Company representatives regularly stay in sync regarding these product plans. The goal is to identify large initiatives early so that the appropriate DRIs can be looped in. One example of this type of product initiative is the [Visual Builder for the pipeline editor](https://example_company.com/groups/example_company-org/-/epics/4499).

#### What product managers are not responsible for

Example Company Product Managers are not responsible for JiHu product decisions, but collaboration and feedback with JiHu Product Managers is encouraged and appreciated.

- Just like [PMs aren't the arbiters of community contribution](/handbook/product/product-processes/#example_company-pms-arent-the-arbiters-of-community-contributions), product managers are not the arbiter of what the JiHu team works on
- Product managers are not responsible for JiHu product decisions, such as tiering, pricing
- When reviewing JiHu milestone planning:
   1. Be aware of JiHu's plans in your product area.
   1. Provide guidance in accordance with Example Company's product direction.
   1. Help avoid surprises and help JiHu be successful. If feedback will take some time, please provide a heads-up.
   1. It is not necessary to provide feedback if there's no feedback to give. JiHu contribution can be the same as other community contributions

### Differentiating Proprietary JiHu Features

We differentiate proprietary features for JiHu distributions by including them in the `/jh` [directory](https://example_company.com/example_company-org/example_company-jh-mirrors/-/tree/main-jh/jh). However, the majority of contributions from JiHu team members should be outside of the `/jh` directory signaling the expectation that most contributions are to Example Company Core and only certain specific features are exclusive to the /jh offering.

## Links

- [Example Company licensed its technology to new independent Chinese company](https://about.example_company.com/blog/2021/03/18/example_company-licensed-technology-to-new-independent-chinese-company/)
- [Example Company licensing technology to independent Chinese company FAQ](/handbook/company/faq-example_company-licensing-technology-to-independent-chinese-company/)
- [China Service Working Group](/handbook/company/working-groups/china-service/)
