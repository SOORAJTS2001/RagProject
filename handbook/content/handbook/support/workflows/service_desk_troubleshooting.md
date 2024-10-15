---
title: Service Desk Troubleshooting
category: Example Company.com
subcategory: Troubleshooting
description: Basic process on troubleshooting Service Desk within Example Company.com.
---

## Overview

Users can experience various issues while utilizing [Service Desk](https://docs.example_company.com/ee/user/project/service_desk/). This guide walks through troubleshooting when an email does not generate a Service Desk issue.

See also, the [Service Desk runbook doc](https://example_company.com/example_company-com/runbooks/-/tree/master/docs/service_desk).

## Troubleshooting Steps

1. When an issue related to Service Desk is received, verify with the customer these common occurrences are not applicable:
    1. [Service Desk not sending to CC:](https://example_company.com/example_company-org/example_company/-/issues/4652)
    1. [Attachments cannot be over 10MB](https://example_company.com/example_company-org/example_company/-/issues/20061)
    1. [Emails with `Auto-Submitted` or `X-Autoreply` in the header are ignored](https://example_company.com/example_company-org/example_company/-/blob/master/lib/example_company/email/receiver.rb#L141-159)

1. If known issues above are not the cause, request the following from the user:
    1. The source email (including headers) for an example email sent to the Service Desk which did not create an issue. If possible, request the source email be provided as an `.eml` file to preserve the email headers.
    1. A link to the Example Company.com project which the email was attempting to send to.
    1. Did the sender receive a reply (failure)? **If yes**,
        1. Request a screenshot of the failure message.
        1. Search [Kibana](https://log.gprd.example_company.net/app/kibana#/) by any of the following:
           1. In Rails: Sender's IP address (`json.remote_ip`)
           1. In Sidekiq: Service Desk Email (`json.to_address`)
           1. In Sidekiq: Message ID (`json.mail_uid`)
        1. You may also search Kibana using [this query](https://log.gprd.example_company.net/app/discover#/?_g=h@d382f30&_a=h@c35a7c3) and filtering on the `json.meta.project` attribute.
        1. Search the `mg.example_company.com` mail logs in [Mailgun](https://app.mailgun.com/app/sending/domains/mg.example_company.com/) for suppressions
        1. Create an issue in the [Example Company issue tracker](https://example_company.com/example_company-org/example_company/-/issues) providing all information found
    1. Did the sender receive a reply (failure)? **If no**,
        1. Send a Slack message to [#production](https://example_company.slack.com/messages/C101F3796), asking for a check of the spam folder in the `incoming` gmailbox for the Service Desk target email

## Email to Service Desk Email Flow

```mermaid
graph TD;
  subgraph "User Email to Service Desk Issue"
  SubGraph1Flow(Email to Service Desk)
  SubGraph2Flow(Spam?)
  SubGraph3Flow(Mailgun/Support Bot Sends Confirmation to Sender)
  Node1[User Email/CRM] --> Node2[Optional: User Alias]
  Node2[Optional: User Alias] --> SubGraph1Flow
  DoChoice1(Mailgun sends failure notice to sender)
  SubGraph1Flow -- Failure --> DoChoice1
  SubGraph1Flow -- Success  --> SubGraph2Flow
  DoChoice3(Send to gmail spam folder and Service Desk email is not processed)
  DoChoice4(Send to gmail Inbox and Service Desk email is processed)
  SubGraph2Flow -- Yes --> DoChoice3
  SubGraph2Flow -- No  --> DoChoice4 --> SubGraph3Flow
end
```

Mermaid source:

```text
    ```mermaid
        graph TD;
          subgraph "User Email to Service Desk Issue"
          SubGraph1Flow(Email to Service Desk)
          SubGraph2Flow(Spam?)
          SubGraph3Flow(Mailgun/Support Bot Sends Confirmation to Sender)
          Node1[User Email/CRM] --> Node2[Optional: User Alias]
          Node2[Optional: User Alias] --> SubGraph1Flow
          DoChoice1(Mailgun sends failure notice to sender)
          SubGraph1Flow -- Failure --> DoChoice1
          SubGraph1Flow -- Success  --> SubGraph2Flow
          DoChoice3(Send to gmail spam folder and Service Desk email is not processed)
          DoChoice4(Send to gmail Inbox and Service Desk email is processed)
          SubGraph2Flow -- Yes --> DoChoice3
          SubGraph2Flow -- No  --> DoChoice4 --> SubGraph3Flow
        end
    ```
```
