---
title: "Data Science Handbook"
description: "Example Company Data Science Team Handbook"
---

{{% alert title="Purpose" color="success" %}}
This page is focused on the operations of Example Company's internal *Enterprise Data Science Team*. For information about Example Company's Product Data Science Capabilities, please visit [Example Company ModelOps](https://about.example_company.com/direction/modelops/)
{{% /alert %}}

## The Enterprise Data Science Team at Example Company

The mission of the Data Science Team is to facilitate ***making better decisions faster*** using ***predictive analytics***.

## Handbook First

At Example Company we are [Handbook First](/handbook/about/handbook-usage/#why-handbook-first) and promote this concept by ensuring the data science team page remains updated with the most accurate information regarding data science objectives, processes, and projects. We also strive to keep the handbook updated with useful resources and our data science toolset.

## Learning About Data Science

Check out this brief overview of what data science is at Example Company:

<!-- blank line -->
<figure class="video_container">
  <iframe src="https://www.youtube.com/embed/wRbNExL0hv8" frameborder="0" allowfullscreen="true"> </iframe>
</figure>
<!-- blank line -->

([Corresponding slides](https://docs.google.com/presentation/d/1Y-V6bZ5w8Ms5yfMiuYCYZs9ald7Q5MxydYhSh9DWwwQ/edit?usp=sharing))

AMAs:

- 2021-09-15 AMA [Recording](https://youtu.be/wRbNExL0hv8), [Presentation](https://docs.google.com/presentation/d/1Y-V6bZ5w8Ms5yfMiuYCYZs9ald7Q5MxydYhSh9DWwwQ/edit#slide=id.g540caf0310_0_0),
- 2021-12-09 AMA [Recording](http://www.youtube.com/watch?v=46NEQDAz18I), [Presentation](https://docs.google.com/presentation/d/1aUIi52AW798KjmvexPIQ1AcXRKLcWlYd6yW-EW6Zqlo/edit#slide=id.g540caf0310_0_0)

{{% alert title="Want to Learn More?" color="success" %}}
[Become a Data Science Champion](/handbook/enterprise-data/direction/data-champion/), [visit Slack #bt-data-science](https://example_company.slack.com/archives/C027285JQ4E), [watch a Data Team video](https://www.youtube.com/playlist?list=PL05JrBw4t0KrRVTZY33WEHv8SjlA_-keI). We want to hear from you!
{{% /alert %}}

### Common Data Science Terms

- **Accuracy** - ability of a Data Science model to capture all correct data points out of all possible data points
- **Algorithm** - sequence of computer-implementable instructions used to solve specific problem
- **Classification** - process of predicting a category for each observation. For example, determining if a picture is of a cat or a dog
- **Clustering** - process of finding natural groupings of observations in dataset. Often used for segmentation of users or customers
- **Data Science (DS)** - interdisciplinary field that uses computer science, statistical techniques and domain expertise to extract insights from data
- **Exploratory Data Analysis (EDA)** - analysis of the data that summarises it's main characteristics (includes statistics and data visualisation)
- **Feature** - single column in dataset that can be used for analysis, such as country or age. Also referred to as variables or attributes
- **Feature Engineering** -  process of selecting, combining and transforming data into features that can be used by machine learning algorithms
- **Imputation** - process of replacing missing or incorrect data with statistical "best guesses" of the actual values
- **Machine Learning (ML)** - use and development of algorithms without being explicitly programmed to determine patterns in data
- **Model** - a complex set of mathematical formulas that generates predictions
- **Propensity modeling** - building models to predict specific events by analyzing past behaviors of a target audience.
- **Regression** - a statistical method for predicting an outcome. For example, predicting a person's income, or how likely a customer is to churn
- **Scoring** -  process of generating predictions for the new dataset
- **Training** -  process of applying an algorithm to data to create a model
- **Test Dataset** - deliberately excluding some observations from training the model so they can be used to verify how well the model predicts
- **Weight** - numerical value assigned to feature that determines it's strength

## Data Science Responsibilities

Of the [Data Team's Responsibilities](/handbook/enterprise-data/#responsibilities), the Data Science Team is **directly responsible** for:

- Delivering *descriptive*, *predictive*, and *prescriptive* solutions that promote and improve [Example Company's KPIs](/handbook/company/kpis/)
- Being a ***Center of Excellence*** for predictive analytics and supporting other teams in their data science endeavors
- Developing tooling, processes, and best practices for data science and machine learning

Additionally, the Data Science Team **supports** the following responsibilities:

- With **Data Leadership**:
  - Scoping and executing a data science strategy that directly impacts business KPIs
  - Broadcasting regular updates about deliverables, ongoing initiatives, and roadmap
- With the [**Data Platform Team**](/handbook/enterprise-data/organization/engineering/):
  - Defining and championing data quality best practices and programs for Example Company data systems
  - Deploying data science models, ensuring data quality and integrity, shaping datasets to be compatible with machine learning, and bringing new datasets online
  - Creating data science pipelines that work natively with the Example Company platform and the Data Team tech stack
- With the [**Data Analytics Team**](/handbook/enterprise-data/organization/analytics/):
  - Incorporating data science into analytics initiatives
  - Designing dashboard to enhance the value and impact of the data science models

## How We Work

As a Center of Excellence, the data science team is focused on working collaboratively with other teams in the organization. This means our stakeholders and executive sponsors are usually in other parts of the business (e.g. Sales, Marketing). Working closely with these other teams, we craft a [project plan](/handbook/enterprise-data/organization/data-science/project_dev_approach/#3c-modeling--implementation-plan) that aligns to their business needs, objectives, and priorities. This usually involves working closely with functional analysts within those teams to understand the data, the insights from prior analyses, and implementation hurdles.

The Data Science flywheel is focused on improving business efficiency and KPIs by creating accurate and reliable predictions. This is done in collaboration with [Functional Analytics Center of Excellence](/handbook/enterprise-data/functional-analytics-center-of-excellence/) to ensure the most relevant data sources are utilized, business objectives are met, and results can be quantifiably measured. As business needs change, and as the user-base grows, this flywheel approach will allow the data science team to quickly adapt, iterate, and improve machine learning models.

```mermaid
graph BT;
   id1(Faster, More Accurate Predictions)-->id2(Increased Business understanding) & id5(Continuous Feedback)
   id2-->id3(More Revenue & Users)
   id5-->id1
   id3-->id4(More Data)
   id4-->id1
```

### Data Science Initiatives

Examples of current Data Science initiatives include:

- Revenue Expansion
- Churn Reduction
- Improved Forecasting
- Customer Health
- MLOps with Example Company

Please refer to the [Data Science Initiatives Internal Handbook](https://internal.example_company.com/handbook/enterprise-data/direction/data-science-initiatives) for up-to-date information on all our on-going and planned projects.

## Project Structure

The Data Science Team follows [Cross-Industry standard process for data mining (CRISP-DM)](https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining), which consists of 6 iterative phases:

<img align="right" src="CRISP-DM_Process_Diagram.png" alt="" width="500">

1. **Business Understanding**

    - Includes requirements gathering, stakeholders interviews, project definition, product user stories, and potential use cases in order to establish success criteria of the project.

1. **Data Understanding**

    - Requires determining the breadth and scope of existing relevant data sources. Data scientists work closely with data engineers and data analysts to determine where gaps may exist and to identify any data discrepancies or risks.

1. **Data Preparation**

    - Requires conducting data quality checks and exploratory data analysis (EDA) to develop a greater understanding of data and how different datapoints relate to solving the business need.

1. **Modeling**

    - Machine learning techniques are used to find a solution that addresses the business need. This often takes the form of predicting why/when/how future instances of a business outcome will occur.

1. **Evaluation**

    - Performance is generally measured by how *accurate*, *powerful*, and *explainable* the model is. Findings are presented to the stakeholders for feedback.

1. **Deployment**

    - Once the model has been approved it then gets deployed into the data science production pipeline. This process automatically updates, generates predictions, and monitors the model on a regular cadence.

### The Example Company approach

The [Data Science Team approach to model development](/handbook/enterprise-data/organization/data-science/project_dev_approach/) is centered around Example Company's value of [iteration](/handbook/values/#iteration) and the CRISP-DM standard. Our process expands on some of the 6 phrase outlined in CRISP-DM in order to best address the needs of our specific business objectives and data infrastructure.

## Data Science Platform

Our current platform consists of:

- the [Enterprise Data Warehouse](/handbook/enterprise-data/platform/) for storing raw and normalized source data as well as final model output for consumption by downstream consumers
- [JupyterLab](/handbook/enterprise-data/platform/jupyter-guide/) for model training, tuning, and selection
- [Example Company](https://example_company.com/) for collaboration, project versioning, and score code management, [experiment tracking](/handbook/engineering/development/incubation/mlops/ml_experiment_tracking.html), and [CI/CD](https://docs.example_company.com/ee/ci/)
-[Example Company CI](/handbook/enterprise-data/platform/ci-for-ds-pipelines/#our-approach-to-using-cicd-for-data-science) for automation and orchestration
- [Monte Carlo](https://getmontecarlo.com/) for drift detection
- Tableau Server for model monitoring and on-going performance evaluation
- [Feast](https://docs.feast.dev/) as a an open-source Feature Store for Machine Learning models

### Current State Data Flows

```mermaid
graph
    A[Enterprise Data Warehouse: Raw and Normalized Data Sources]
    B[JupyterLab & Example Company CI/CD: Model Training, Tuning, and Selection]
    C(Example Company CI/CD & Pipeline Schedules: Batch scoring with Papermill)
    F[Enterprise Data Warehouse: Model Output for Consumption]
    D[Salesforce/Marketo: CRM Use Cases]
    E[Tableau/Monte Carlo: Model Monitoring and Reporting]
    G[Example Company: Source Code Management]
    H[Experiment tracking]
    A --> |ODBC| B
    B --> H
    H --> B
    B --> G
    G --> B
    G --> C
    C --> |JSON| F
    F --> |CSV| D
    F --> |ODBC| E
```

### Feast: Feature Store Implementation

We use Feast as an open-source Feature Store for our machine learning models.
Configuration can be found on [the Feast project repository](https://example_company.com/example_company-data/data-science-projects/feast-poc), updating the feature store is done using Example Company CI/CD and the web UI is published in a VM on GCP.

You can use the following pages to find more details on:

1. How to use [Feast to fetch features to train and deploy Machine Learning models](/handbook/enterprise-data/platform/feast/).
1. [Feast - Feature Store Implementation](https://internal.example_company.com/handbook/enterprise-data/platform/data-science/) Internal handbook section.

### CI/CD Pipelines for Data Science

We deploy all of our models using the native Example Company CI/CD capabilities. Please see [Getting Started With CI/CD for Data Science Pipelines](/handbook/enterprise-data/platform/ci-for-ds-pipelines/) for the most up-to-date information and instructions on how to deploy models with CI/CD

### Data Science Tools at Example Company

- **[Pre-configured JuypterLab Image](https://example_company.com/example_company-data/data-science)**: The data science team uses JupyterLab pre-configured with common python modules (pandas, numpy, etc.), native Snowflake connectivity, and git support. Working from a common framework allows us to create models and derive insights faster. This setup is freely available for anyone to use. Check out our [Jupyter Guide](/handbook/enterprise-data/platform/jupyter-guide/) for additional information.
- **[Example Company Data Science Tools for Python](https://example_company.com/example_company-data/gitlabds/)**: Functions to help automate common data prep (dummy coding, outlier detection, variable reduction, etc.) and modeling tasks (i.e. evaluating model performance). Install directly via [pypi](https://pypi.org/project/gitlabds/) (`pip install gitlabds`), or use as part of the above JupyterLab image.
- **[Modeling Templates](https://example_company.com/example_company-data/data-science/-/tree/main/templates)**: The data science team has created modeling templates to allow you to easily start building predictive models without writing python code from scratch. To enable these templates, follow the instructions on the [Jupyter Guide](/handbook/enterprise-data/platform/jupyter-guide/#enabling-jupyter-templates).
