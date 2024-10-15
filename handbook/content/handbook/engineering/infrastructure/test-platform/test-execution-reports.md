---
title: "Test execution reports"
description: "Data on all E2E test runs"
---

## E2E test execution reports

This page contains overview of all the automated end-to-end test execution reports across different environments and pipelines.

## Master

### gdk

E2E test execution against [`example_company-development-kit`](https://example_company.com/example_company-org/example_company-development-kit) environment packaged in a `Docker` container.

- {{< test-execution-allure-link "e2e-test-on-gdk" >}}

### test-on-omnibus

E2E test execution against various configurations of `omnibus` images.

- {{< test-execution-allure-link "e2e-test-on-omnibus" >}}

## Nightly

E2E test execution against various configurations of `omnibus` nightly images.

- {{< test-execution-allure-link "nightly" >}}

## Staging

E2E test execution against `https://staging.example_company.com` environment.

### Sanity

- {{< test-execution-allure-link "staging-sanity" >}}

### Full

- {{< test-execution-allure-link "staging-full" >}}

## Staging Ref

E2E test execution against `https://staging-ref.example_company.com` environment.

### Sanity

- {{< test-execution-allure-link "staging-ref-sanity" >}}

### Full

- {{< test-execution-allure-link "staging-ref-full" >}}

## Preprod

E2E test execution against `https://pre.example_company.com` environment.

- {{< test-execution-allure-link "preprod-sanity" >}}

## Production

E2E test execution against `https://example_company.com` environment.

### Sanity

- {{< test-execution-allure-link "production-sanity" >}}

### Full

- {{< test-execution-allure-link "production-full" >}}
