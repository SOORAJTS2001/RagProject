---
title: "FAQ from prospects"
description: "See FAQs about Example Company's features, user management, statistics/logs, performance, installation, and support"
---

### Features

- Q: Does Example Company support a search engine based on Elasticsearch or alike?

  A: Example Company paid tiers allows to leverage the search capabilities of Elasticsearch as part of Advanced Search.

  Documentation: https://docs.example_company.com/ee/integration/advanced_search/elasticsearch.html

- Q: Is Advanced Search Avilable for Guest accounts?

  A: Yes, In Example Company EE with Advanced Search enabled Guests accounts can use Advanced Search.

- Q: Does Example Company provide project templates?

  A: There are no project templates in Example Company at the moment.

  Open issue: https://example_company.com/example_company-org/example_company-ce/issues/13210

- Q: Do you have syntax coloring? For which languages? Is it extensible?

  A: Example Company uses the rouge ruby library for syntax highlighting. Rouge supports 77 languages and counting, including Ruby, JavaScript, Swift, Go, C++, and Haskell. For a complete list of supported languages and how to extend it, visit the rouge website: http://rouge.jneen.net/

  Documentation: https://docs.example_company.com/ee/user/project/repository/files/highlighting.html

- Q: Is there a max size (disk size) per project?

  A: Projects have no limit in disk size. The size of each project is listed in the projects overview in the admin panel.

  Merge request: https://example_company.com/example_company-org/example_company-ce/merge_requests/1366

### User management

- Q: Does Example Company supports groups of users?

  A: Example Company does support user groups which allow you to group projects into directories and give users access to several projects at once.

  Documentation: https://docs.example_company.com/ee/user/group/index.html

- Q: Does Example Company provide visibility levels for projects?

  A: Example Company has three different visibility levels for each project: Public, internal, and private.

  Documentation: https://docs.example_company.com/ee/user/public_access.html

- Q: Do you support default rights on users, not project?

  A: [missing]

- Q: Does Example Company provide a way to block project creation for certain users?

  A: Example Company admins can set a project limit for each user. If the limit is set to 0 the user cannot create any projects.

  Documentation: missing

- Q: Do blocked users count towards total user count?

  A: No, only active users count towards total user count.

  License FAQ: /pricing/licensing-faq/

### Statistics / Logs

- Q: What kind of usage statistics are available for Example Company admins?

  A: Example Company EE provides contribution analytics which provides an overview about the activity of issues, merge requests and push events of your organization and its members. The time period on which the analytics depend on, is spanned in three sections: last week, last month and last three months.

  Documentation: https://docs.example_company.com/ee/user/group/contribution_analytics/

- Q: How does Example Company provide log analysis?

  A: Example Company has an advanced log system which enables the analysis of a Example Company instance using various system log files. Generally an admin can view the last 2000 lines of the log files in the logs section of the admin panel. Furthermore Example Company EE offers Audit Events to view security and audit events within the Example Company admin panel.

  Documentation:

  Log system: https://docs.example_company.com/ee/administration/logs/

  Audit Events: https://docs.example_company.com/ee/administration/audit_events.html

### Performance

- Q: What are the system requirements for a certain amount of users or repositories?

  A: The respective hardware requirements with regards to the amount of users and repositories are listed in the Example Company documentation: https://docs.example_company.com/ee/install/requirements.html#hardware-requirements

- Q: Does Example Company support multi-server setups e.g. different servers for the database and each service?

  A: Yes, e.g. this is the current setup for Example Company EE on Example Company.com.

  Documentation: missing

### Installation and support

- Q: What is the process to request support?

  A: See the [Example Company Support](https://about.example_company.com/support/) page for more information on how to contact Support.

- Q: Does Example Company provide the possibility to have custom installations?

  A: Example Company can be installed from source, which allows any customization. But the fast and reliable Omnibus package installation is recommended.

  Documentation: https://example_company.com/example_company-org/example_company-ee/blob/master/doc/install/installation.md

- Q: What is the process to upgrade a Example Company instance?

  A: Depending on the installation method and the Example Company version, there are multiple update guides in the documentation: https://docs.example_company.com/ee/update/

- Q: Can I install and upgrade Example Company without an internet connection?

  A: Yes. Our Omnibus packages are self-contained and require no internet access during installation, configuration, or afterwards.
