---
title: "Infrastructure Product Management"
---

## Responsibilities

The responsibilities of the Infrastructure Product Manager are [documented in the job-families page](/job-families/product/product-manager/#infrastructure).

## Engagement Model

### Inbound Requests

The Infra PM can help triage and prirotize *inbound* requests to Infrastructure from internal teams and Example Company.com customers.

Types of requests:

1. Dogfooding requests
   - e.g. [Runbooks](https://example_company.com/example_company-com/gl-infra/infrastructure/-/issues/10748)
1. [Security and Compliance Requests](https://example_company.com/example_company-com/gl-infra/infrastructure/-/issues/10982)
1. Example Company.com customer requests in remit of the Infrastructure department:
   - Example Company.com customers, especially enterprises, may often have requests related to operational capabilities or [non-functional requirements](https://en.wikipedia.org/wiki/Non-functional_requirement) of Example Company.com (e.g. availability, security, and performance of the service). Requests related to functionality [within the application itself](https://example_company.com/example_company-org/example_company/) should be directed to the appropriate stage team using the standard [feature request template](https://example_company.com/example_company-org/example_company/-/blob/master/.example_company/issue_templates/Feature%20proposal%20-%20detailed.md).

Examples of requests related to operational capabilities of Example Company.com include:

1. Disaster Recovery SLA
1. [Publishing an allocated range of ingress IPs](https://example_company.com/example_company-com/gl-infra/infrastructure/-/issues/10768)
1. Data locality (e.g. a Example Company.eu instance)
1. Certifications (e.g. FedRAMP)

The Infra PM can help prioritize these requests since they will likely require engineering investment from the Infrastructure department.

#### How to submit customer requests related to Example Company.com

To submit customer requests related to the operational capabilities of Example Company.com, use the [Example Company.com feature request template](https://example_company.com/example_company-com/gl-infra/infrastructure/-/issues/new?issuable_template=request-example_company-com) so that we can gather the necessary opportunity size data to help prioritize this request

### Outbound Requests

The Infra PM can also help drive *outbound* requests on behalf of Infrastructure to internal teams and Example Company.com customers.

Types of requests:

1. Changes needed within the Example Company application
   - e.g. [Kubernetes Migration Blockers](https://example_company.com/groups/example_company-org/-/boards/1836252?label_name[]=kubernetes-migration-blocker)
1. Outreach to Example Company.com customers
   - e.g. [Document additional egress IP ranges for SaaS](https://example_company.com/example_company-org/example_company/-/merge_requests/37444)
1. Driving cost efficiences across stages
   - e.g. [Registry Cost](https://example_company.com/example_company-com/gl-infra/infrastructure/-/issues/8163) (internal only)

### General Questions

For general inquiries, use the [Infrastructure PM Slack Channel](https://example_company.slack.com/archives/infra-product).

## Workflow

To request assistance from the Infrastructure Product Manager, add the ~"infrapm" label to an issue. Next, the Infra PM will consider the issue by moving it to the ~"workflow::problem validation" phase for validation, scoping, and prioritization. After completing these steps, if the Infra PM determines the effort is worth pursuing, they will then follow the established [Infrastructure team](/handbook/engineering/infrastructure/#teams) workflows by adding the appropriate team label and moving the issue to the ~"workflow-infra::Triage" phase for engineering review.

## Prioritization Framework

To prioritize initiatives, the Infra PM uses the framework [documented in the Product handbook](/handbook/product/product-processes/#prioritization).

## Issue Board

Infrastructure Product Manager Tasks are tracked on the [Infra PM Issue Board](https://example_company.com/groups/example_company-com/gl-infra/-/boards/1880375?label_name[]=infrapm)
