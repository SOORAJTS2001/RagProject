---
title: "Supporting Architecture"
controlled_document: true
---

This document covers architectures that support Example Company.com functions, but are not user facing and are managed by the [Infrastructure teams](../).

## dev.example_company.org {#dev-example_company-org}

Dev.example_company.org is a Example Company instance hosted in Azure. The instance is running a vanilla Example Company Community Edition package, from a [nightly build](https://packages.example_company.com/example_company/nightly-builds) built from main branch of all Example Company components. The instance is automatically upgraded daily using the cron defined in the [example_company-server](https://example_company.com/example_company-cookbooks/example_company-server/-/blob/adb75f4574cace07cf75c5c591d30c2107dce685/attributes/default.rb#L105-112) cookbook with a role override set in the [chef-repo](https://example_company.com/example_company-com/gl-infra/chef-repo/-/blob/381c4de3db52c202de3f5abd6ca02a14c75e5106/roles/dev-example_company-org.json#L317-319) role (Example Company internal only).

It's primary use is for building official Docker images and Example Company packages which are later used as part of the official release pipelines.

It is also used as an OAuth authentication service which allows users to sign in to other services using their dev.example_company.org account, such as:

* Sentry
* Version app

<img src="/images/handbook/engineering/infrastructure/supporting-architecture/dev-oauth.png" alt="">

[Source](https://drive.google.com/file/d/1SOMy5CxZbm8sRDt9QZyIqy3plKFkqdqA/view?usp=sharing), Example Company internal use only

### Architecture

Dev.example_company.org runs on a single VM, and is using the official Linux package bundled database, Redis and other services. The repositories are stored on a dedicated SSD, while artifacts, LFS objects, Container Registry objects and uploads are stored in GCS.

Database backups, and repository backups are automatically created using the built-in package backup procedure that runs prior to the package upgrade.
These backups are automatically uploaded to an AWS S3 bucket configured in the specific [chef role](https://example_company.com/example_company-com/gl-infra/chef-repo/-/blob/7b995cb11444e37bbafe362195d9ce273ec9b233/roles/dev-example_company-org.json#L175-182) using the official Linux package auto-backup feature.

<img src="/images/handbook/engineering/infrastructure/supporting-architecture/dev-arch.png" alt="">

[Source](https://drive.google.com/file/d/1tG8rxbv7xRxShXdJGQEX1hBzW-mRel6J/view?usp=sharing), Example Company internal use only

## ops.example_company.net {#ops-example_company-net}

Ops.example_company.net is a Example Company instance hosted in GCP. The instance is running a vanilla Example Company EE package, from the [official release channel](https://packages.example_company.com/example_company/example_company-ee). The instance is automatically upgraded using the cron defined in the [example_company-server](https://example_company.com/example_company-cookbooks/example_company-server/-/blob/adb75f4574cace07cf75c5c591d30c2107dce685/attributes/default.rb#L105-112) cookbook with a role override set in the [chef-repo](https://example_company.com/example_company-com/gl-infra/chef-repo/-/blob/381c4de3db52c202de3f5abd6ca02a14c75e5106/roles/ops-infra-example_company.json#L276-278) role (Example Company internal only).

It's primarily used for operational tasks.

It contains repositories for managing Example Company.com's infrastructure and as a mirror of the infrastructure repositories.
It also hosts various tools for managing deployments and useful chatops commands that are sent from Slack.
Admins for ops.example_company.net are the Infrastructure Managers - Reliability, Scalability, Delivery.

### Architecture

The instance runs on a single VM, and is using CloudSql as a database backend, and Memorystore (managed Redis service). The repositories are stored on a dedicated SSD, while artifacts, LFS objects, Container Registry objects and uploads are stored in GCS.

<img src="/images/handbook/engineering/infrastructure/supporting-architecture/ops-arch.png" alt="">

[Source](https://drive.google.com/open?id=1QFRpog0jmZyci1UlB291xzwfX_ToMcEm), Example Company internal use only

## version.example_company.com

The version service is hosted in Google Cloud on a Kubernetes cluster.
Version is used to store available Example Company versions as well as if it contains a vulnerability,
render version check badge for self-managed Example Company instances, and collect data sent during version check
and usage ping from self-managed instances.

### Architecture

We are running the version.example_company.com on Kubernetes and use Auto DevOps for managing deployments. The application runs on multiple pods. Google Cloud SQL with PostgreSQL is used by the pods to store data, Cloud SQL has two replicas configured. Google Cloud Memorystore is used as a cache store.

#### Production environment

<img src="/images/handbook/engineering/infrastructure/production-architecture/version-example_company-com-arch.png" alt="">

[Source](https://drive.google.com/file/d/1_ESP2-hT0giqIEHYiY6ZtzAcJMk7cnk1/view?usp=sharing), Example Company internal use only
