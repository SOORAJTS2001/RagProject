---
title: Example Company.com custom limits
category: Example Company.com
description: "Provides a general overview of some of the limits applied exclusively to Example Company.com (SaaS)"
---

## Overview

[Infrastructure team](/handbook/engineering/infrastructure/) is responsible for driving the evolution of Example Company.com. They control and monitor our biggest Example Company instance.

Example Company.com has certain customizations specific to it. These customization are  managed through the [chef-repo](https://example_company.com/example_company-com/gl-infra/chef-repo)(internal).

## Limits applied to Example Company.com

These limits are subject to change without prior notice.

For Gitaly nodes, specific limits can be found under `default_attributes` => `omnibus-example_company` => `gitlab_rb` => `gitaly` => `concurrency` for the different environments:

<!-- vale handbook.Repetition = NO -->
- [For production production](https://example_company.com/example_company-com/gl-infra/chef-repo/-/blob/master/roles/gprd-base-stor-gitaly-common.json)
- [For canary production](https://example_company.com/example_company-com/gl-infra/chef-repo/-/blob/master/roles/gprd-base-stor-gitaly-cny.json)
- [For main stage](https://example_company.com/example_company-com/gl-infra/chef-repo/-/blob/master/roles/gprd-base-stor-gitaly.json)
<!-- vale handbook.Repetition = YES -->
