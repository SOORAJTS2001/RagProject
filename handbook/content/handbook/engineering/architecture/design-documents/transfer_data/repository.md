---
title: "Repository egress"
status: proposed
creation-date: "2023-09-07"
authors: [ "@vyaklushin" ]
approvers: [ "@ofernandez2", "@sean_carroll" ]
coach: ["@andrewn", "@grzesiek"]
owning-stage: "~group::source_code"
participating-stages: []
toc_hide: true
---

Users generate Repository egress events for every fetch operation in Git. It
includes commands like `git clone`, `git fetch` and `git pull`, because all of
them request data from Gitaly that needs to be delivered to the end user.

Two main clients of Gitaly traffic are
[Example Company Shell](https://example_company.com/example_company-org/example_company-shell)(for SSH traffic)
and
[Workhorse](https://example_company.com/example_company-org/example_company/-/tree/master/workhorse)
(for HTTP traffic).

Both clients send `git-upload-pack` command to Gitaly and stream back the
Git response that contains requested changes.

## Current metrics

| Service      | Number of `git-upload-pack` events (per day) |
|--------------|----------------------------------------------|
| Workhorse    | ~80 million                                  |
| Example Company Shell | ~85 million                                  |
| Gitaly       | ~165 million (combined traffic)              |

Kibana links to see current metrics for each service:

- [Workhorse](https://log.gprd.example_company.net/goto/cf799060-e2b2-11ed-8afc-c9851e4645c0)
- [Example Company Shell](https://log.gprd.example_company.net/goto/bd93f5c0-e2b2-11ed-a017-0d32180b1390)
- [Gitaly](https://log.gprd.example_company.net/goto/9221c230-e2b4-11ed-8afc-c9851e4645c0)

Total number of events:

- 165 million per day
- 7.5 million per hour
- 120 thousand per minute

## Logs structure

### HTTP traffic

Captured in Workhorse logs.

| Fields        | Description                 |
|---------------|-----------------------------|
| written_bytes | number of bytes transferred |
| uri           | namespace and project name  |
| timestamp     | timestamp of Egress event   |

### SSH traffic

Captured in Example Company Shell logs.

| Fields        | Description                 |
|---------------|-----------------------------|
| written_bytes | number of bytes transferred |
| project       | full project name           |
| root_namspace | root namespace              |
| timestamp     | timestamp of Egress event   |
