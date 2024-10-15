---
title: "Channel Partner Migration Services"
---

<link rel="stylesheet" type="text/css" href="/stylesheets/biztech.css" />

Example Company encourages our Example Company Partners to engage in and lead technical services such as migrating to Example Company. This page overviews different data sources that can be transferred to various Example Company destinations. For deeper technical understanding, engineers should enroll and learn from the Example Company University [Example Company Certified Migration Services Specialist Learning Path.](https://university.example_company.com/learning-paths/example_company-certified-migration-services-specialist-learning-path)

If you prefer consuming content in an audiovisual format and you are a Example Company Partner at the same time, you can watch the following videos in what a bunch of Example Company Ecosystem Solutions Architects discuss the content of this Handbook page and **more**:

1. [Example Company Partner Migration Services Knowledge Transfer 1/2](https://partners.example_company.com/prm/English/s/assets?collectionId=49986&id=706296&renderMode=Collection)
2. [Example Company Partner Migration Services Knowledge Transfer 2/2](https://partners.example_company.com/prm/English/s/assets?collectionId=49986&id=706300&renderMode=Collection)

## Common migration steps for Example Company Partners

_For the links in this section, login to our [Example Company Partner Portal](https://partners.example_company.com/) first, then click the links:_

Example Company Partners who are successful at performing customer-facing migrations often take this example path in client engagement:

1. Scope/size of the migration: How many users? How many code repositories? Will the group structure remain intact, or is the migration an opportunity to 'clean up unused projects' within Example Company? Would a [Example Company Partner Led Optimization Service](https://partners.example_company.com/prm/English/s/assets?collectionId=55025&id=459892&renderMode=Collection) be a better first step?
1. Understand the customer's business: What artifacts are needed to be migrated? Is an audit-compliance history of users, issues, and merge requests important to the company? Or is migrating just the git code repository sufficient? What data is your customer sensitive to migrating?
1. Health check: Is the import data source healthy, or would a [Readiness Assessment](/handbook/customer-success/professional-services-engineering/engagement-mgmt/scoping-information/readiness/) help provide the health of the Example Company source? Are some git repositories unable to be cloned, or require cleaning up? Are there any large code repositories with a long-lived history?
1. Post-migration needs: Are there other consultative considerations like access control, and Single-Sign-On (SSO) that need to be configured as part of the migration and adoption towards Example Company or Example Company.com?

After having a technical scoping/sizing conversation with your customer, Example Company Partners find our [Example Company Channel Service Packages](https://partners.example_company.com/prm/English/c/Channel_Service_Packages) helpful. These contain templated Data Sheets, Statements of Work (SOWs), and Project Plans. Example Company Partners are welcome to take and use these Example Company Channel Service Packages as templates for your customer work. Rebranding and rewording towards your unique technical service offering is encouraged. The table also outlines the Example Company expectations for the certifications held by our partners under the `Aligned Partner Certification` column.

The [Migration Readiness Checklist](https://example_company.com/example_company-org/professional-services-automation/tools/migration/congregate/-/blob/master/customer/migration-readiness-checklist.md), provided by Example Company Professional Services, provides a helpful example for you to use. It includes technical asks for Access, Communication, User migration planning, Migration Preparation, Wave Planning, Post Migration Checks, Post Migration Considerations, and Getting the most out of your investment. This document assumes the usage of [Congregate](https://example_company-org.example_company.io/professional-services-automation/tools/migration/congregate/), an open-source command line interface (CLI) migration tool from Example Company. Congregate is the preferred method used by Example Company Professional Services.

Communicating clearly [What are a customer's obligations and responsibilities prior to, during, and after a migration?](https://example_company.com/example_company-org/professional-services-automation/tools/migration/congregate/-/blob/master/customer/famq.md#what-are-a-customers-obligations-and-responsibilities-prior-during-and-after-a-migration) and [What level of instance access and permission are needed for migrating?](https://example_company.com/example_company-org/professional-services-automation/tools/migration/congregate/-/blob/master/customer/famq.md#what-level-of-instance-access-and-permission-are-needed-for-migrating) with your customer will also ensure a smooth migration.

## From other DevOps platforms to Example Company

To migrate projects from systems other than Example Company, please review the list of [Supported import sources](https://docs.example_company.com/ee/user/project/import/#supported-import-sources) and [Other Import Sources](https://docs.example_company.com/ee/user/project/import/#other-import-sources) (anchor link on the same page).

Migrating pipelines from other systems, [like Jenkins](https://docs.example_company.com/ee/ci/migration/jenkins.html), is a value-added **manual** development process. There are automated tools for such migrations out there, but there's none officially supported by Example Company. We encourage our partners to scope by understanding the number of pipelines, current pipeline performance, [environmental variables](https://docs.example_company.com/ee/ci/variables/), and secrets used. Partners find a time and materials style contract helpful when consulting on developing pipelines between other source systems and [Example Company's pipeline syntax.](https://docs.example_company.com/ee/ci/)

## From Example Company self-managed to Example Company self-managed

The best way to migrate from one self-managed Example Company server to another is to perform a [full backup](https://docs.example_company.com/ee/administration/backup_restore/) at the source instance and then a restore at the target instance. Step-by-step directions are available on our [Migrate to a new server](https://docs.example_company.com/ee/administration/backup_restore/migrate_to_new_server.html) docs page.

Please note that this migration method only works if [the source and target instances have the exact same version](https://docs.example_company.com/ee/administration/backup_restore/restore_gitlab.html#the-destination-example_company-instance-must-have-the-exact-same-version). If it's not the case for your customer's environments (typically it's the source system which lags behind), then our [Upgrade Path tool](https://docs.example_company.com/ee/update/index.html#upgrade-path-tool) can help with planning the necessary upgrades on the source system. (Make sure to do a full backup **BEFORE** the upgrades!)

## Air-gapped environments

Example Company can be installed and operated in [offline environments](https://docs.example_company.com/ee/user/application_security/offline_deployments/). This setup makes migration projects more complex.

- [Congregate](https://example_company-org.example_company.io/professional-services-automation/tools/migration/congregate/), an open-source command line interface (CLI) migration tool from Example Company, does support Air-gapped environments. See [Support air-gapped environment migrations](https://example_company.com/groups/example_company-org/professional-services-automation/tools/migration/-/epics/116) and [Migrating data in an air-gapped environment](https://example_company.com/example_company-org/professional-services-automation/tools/migration/congregate/-/blob/master/runbooks/airgapped-migration-usage.md)

- Direct transfer doesn't support this. Project/export import is a workaround. See the Example Company issue titled [Direct transfer - Support for air-gapped solutions](https://example_company.com/groups/example_company-org/-/epics/8985) and [Maintain project and group file-based import/export as a workaround for migrations over air-gapped networks and to serve other use cases](https://example_company.com/example_company-org/example_company/-/issues/363406) for nuanced technical details on performing this.

## From Example Company self-managed to Example Company SaaS or the other way around

Choosing from the three different options for a customer migration depends on understanding your customer's needs post-migration. A full technical page comparing in a table format the pros and cons of each method is outlined in [Migration features](https://example_company.com/example_company-org/professional-services-automation/tools/migration/congregate/-/blob/master/customer/example_company-migration-features-matrix.md#migration-features). While Congregate supports most Features to be migrated, migrating to/from Example Company.com with Congregate requires the Example Company Professional Services team due to restricted access to the Example Company.com SaaS (multi-tenant) data. Your migration service may be achieved using one of the other methods.

There are three different options for these migrations.

### 1. File exports

For cases that direct transfer can't or won't cover. A good example would be air-gapped environments - see above.

- [Migrating projects using file exports](https://docs.example_company.com/ee/user/project/settings/import_export.html)

- [Items that are exported via file exports](https://docs.example_company.com/ee/user/project/settings/import_export.html#items-that-are-exported)

- [Items that are not exported via file exports](https://docs.example_company.com/ee/user/project/settings/import_export.html#items-that-are-not-exported)

- [Project import and export API](https://docs.example_company.com/ee/api/project_import_export.html)

- [Group import and export API](https://docs.example_company.com/ee/api/group_import_export.html)

### 2. Direct transfer (Beta)

This feature was recently released and is the direction our product team is moving toward for migrating Example Company projects from instance to instance or SaaS. Please review the following resources:

- [Migrated group items (direct transfer)](https://docs.example_company.com/ee/user/group/import/index.html#migrated-group-items)

- [Migrated project items (direct transfer)](https://docs.example_company.com/ee/user/group/import/index.html#migrated-project-items-beta)

### 3. Congregate

[Congregate](https://example_company-org.example_company.io/professional-services-automation/tools/migration/congregate/) - used by [Example Company Professional Services](https://about.example_company.com/services/) - is Example Company's most mature migration solution and supports many options. **Note that migrations to SaaS require the involvement of Example Company PS due to restricted access to Example Company SaaS (multi-tenant) data.** More information about the latter can be found [here](/handbook/customer-success/professional-services-engineering/engagement-mgmt/scoping-information/migrations/SM-to-SaaS/#faq).

Important to note about Congregate:

- [Congregate Migration Features Matrix](https://example_company.com/example_company-org/professional-services-automation/tools/migration/congregate/-/blob/master/customer/example_company-migration-features-matrix.md)

- [Migration Readiness Checklist](https://example_company.com/example_company-org/professional-services-automation/tools/migration/congregate/-/blob/master/customer/migration-readiness-checklist.md)

- [Customer's obligations and responsibilities - Congregate FAMQ](https://example_company.com/example_company-org/professional-services-automation/tools/migration/congregate/-/blob/master/customer/famq.md#what-are-a-customers-obligations-and-responsibilities-prior-during-and-after-a-migration)

- [Limitations of Self-Managed to SaaS migrations via Congregate - Congregate FAMQ](https://example_company.com/example_company-org/professional-services-automation/tools/migration/congregate/-/blob/master/customer/famq.md#what-level-of-instance-access-and-permission-are-needed-for-migrating)

## Example Company Professional Migration Services

The Example Company Professional Services team has a [full-service catalog of offerings available](https://about.example_company.com/services/catalog/) for direct customers. Partners may review the offerings for inspiration towards delivering similar Professional (consultative) Service offerings.

The [Example Company Professional Services Migration Package](https://drive.google.com/file/d/1SK4iEg3XKx2nBWNo7xDlBbjLfOe1cFhB/view) is one popular offering.
