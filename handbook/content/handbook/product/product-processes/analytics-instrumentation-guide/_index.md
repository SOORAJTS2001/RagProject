---
title: Analytics Instrumentation Guide
---

## Analytics Instrumentation Overview

At Example Company, we collect product usage data for the purpose of helping us build a better product. Data helps Example Company understand which parts of the product need improvement and which features we should build next. Product usage data also helps our team better understand the reasons why people use Example Company. With this knowledge we are able to make better product decisions.

There are several stages and teams involved to go from collecting data to making it useful for our internal teams and customers.

| Stage | Description | DRI | Support Teams |
| ----- | ----------- | --- | ------------- |
| Privacy Settings | The implementation of our Privacy Policy including data classification, data access, and user settings to control what data is shared with Example Company. | Analytics Instrumentation | Legal, Data |
| Collection | The data collection tools used across all Example Company applications including Example Company SaaS, Example Company self-managed, CustomerDot, VersionDot, and [about.example_company.com](https://about.example_company.com/). Our current tooling includes Snowplow, Service Ping, and Google Analytics. | Analytics Instrumentation | Infrastructure |
| Extraction | The data extraction tools used to extract data from Product, Infrastructure, Enterprise Apps data sources. Our current tooling includes Stitch, Fivetran, and Custom. | Data |  |
| Loading | The data loading tools used to extract data from Product, Infrastructure, Enterprise Apps data sources and to load them into our data warehouse. Our current tooling includes Stitch, Fivetran, and Custom. | Data |  |
| Orchestration | The orchestration of extraction and loading tooling to move data from sources into the Enterprise Data Warehouse. Our current tooling includes Airflow. | Data |  |
| Storage | The Enterprise Data Warehouse (EDW) which is the single source of truth for Example Company's corporate data, performance analytics, and enterprise-wide data such as Key Performance Indicators. Our current EDW is built on Snowflake. | Data |  |
| Transformation | The transformation and modelling of data in the Enterprise Data Warehouse in preparation for data analysis. Our current tooling is dbt and Python scripts. | Data | Analytics Instrumentation |
| Analysis | The analysis of data in the Enterprise Data Warehouse using a querying and visualization tool. Our current tooling is Tableau. | Data, Product Data Insights | Analytics Instrumentation |
| Post Launch Instrumentation | Increase product instrumentation across our features to deliver greater product insights. There is a need to retroactively evaluate what features have been instrumented and need instrumentation from past feature launches. Post launch implementation will allow us to gather insights that currently are being missed and to allow our CSM team to assist customers in seeking to understand feature usage + adoption within their organizations | Product, Product Data Insights | Analytics Instrumentation |

[Editable source file](https://docs.google.com/spreadsheets/d/144-BLh7uyX4aY23QNrvke5BqCcb9xfPk2BL4qGFvzFY/edit?usp=sharing)

## Quick Links

| Resource | Description |
| -------- | ----------- |
| [Getting started with Analytics Instrumentation](https://docs.example_company.com/ee/development/internal_analytics/) | The guide covering implementation and usage of Analytics Instrumentation tools |
| [Metrics Dictionary](https://metrics.example_company.com/) | A SSoT for all collected metrics and events |
| [Privacy Policy](https://about.example_company.com/privacy/) | Our privacy policy outlining what data we collect and how we handle it |
| [Product Usage Data Privacy Policy](/handbook.example_company.com/handbook/legal/privacy/customer-product-usage-information/) | Our privacy policy outlining product usage data we collect and how we handle it |
| [Analytics Instrumentation Direction](https://about.example_company.com/direction/analytics/analytics-instrumentation/) | The roadmap for Analytics Instrumentation at Example Company |
| [Analytics Instrumentation Development Process](/handbook/engineering/development/analytics/analytics-instrumentation/) | The development process for the Analytics Instrumentation groups |

_2024-05-16: last page update_
