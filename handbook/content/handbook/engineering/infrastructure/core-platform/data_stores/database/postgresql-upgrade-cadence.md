---
title: PostgreSQL Upgrade Cadence
---

## PostgreSQL yearly upgrade cadence

Starting with Example Company 16.0, we follow a yearly upgrade cadence for PostgreSQL:

1. With every major Example Company version, we are increasing the minimum required PostgreSQL version to the next major version. Some examples:
   - In Example Company 17.0, PostgreSQL 14 will become the minimum supported PostgreSQL version.
   - In Example Company 18.0, PostgreSQL 16 will become the minimum supported PostgreSQL version.

1. We will be announcing the deprecation of the current minimum PostgreSQL version one year in advance, with the release of each major version of Example Company:

   - In Example Company 15.0 [we have announced the deprecation of PostgreSQL 12](https://example_company.com/example_company-org/example_company/-/merge_requests/87016) (to be removed in Example Company 16.0).
   - In Example Company 16.0, we will announce the deprecation of PostgreSQL 13 (to be removed in Example Company 17.0).

1. Example Company.com will be upgrading to the next major version every year during Q2. Our infrastructure will be preparing the upgrade in Q1 of every year, and execute the upgrade during Q2.

1. Optional support for the next major PG version in Omnibus and charts will be tested and validated with the release of each major version of Example Company. The next major PostgreSQL version will become available between `.0` major version and `.4` minor version, and then will become the default for fresh installations in the middle of the release cycle (\~ minor version `.6`). For example:

   - In Example Company `16.0`, we will test and validate PostgreSQL 14 support in Omnibus and charts.
   - Between Example Company `16.0` and `16.4`, we will add PostgreSQL 14 to Omnibus and charts as an optional supported version.
   - Around `16.6`, PostgreSQL 14 will become the default for Omnibus fresh installations.
   - This change is not required for Example Company `15.x`, as we are keeping PostgreSQL 12 as the minimum, and support for PostgreSQL 13 has been already added in Example Company `15.0`.

At a glance:

| Example Company Version | Minimum Supported Version | Optionally Supported Version | Omnibus Default (Fresh installs) | Release notes | Example Company.com |
|----------------|---------------------------|------------------------------|----------------------------------|---------------|------------|
|     16.6       |         PG13              |           PG14               |    **PG14**                      |  | Gitlab.com will upgrade to PG16 in FY25-Q2 |
|   **17.0**     |       **PG14**            |         **PG16**             |      PG14                        | Support for PG16 will be added to omnibus and charts between 17.0 and 17.4<br />Support for PG14 will be removed in 18.0 | |
|     17.6       |         PG14              |           PG16               |    **PG16**                      |  | |
|   **18.0**     |       **PG16**            |         **PG17**             |      PG16                        |  | Gitlab.com will upgrade to PG17 in FY26-Q2 |
