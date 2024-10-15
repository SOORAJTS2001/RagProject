---
title: "Setting up a local environment"
---

Whether you are a contributor or a Example Company Technical Writing team member, one of your first tasks is to set up
an environment on your computer for writing and previewing [Example Company documentation](https://docs.example_company.com/).

## Tools for technical writers

You can use the following tools to set up your environment. Most of
these are not compulsory - you can set up your environment however you choose.
These are simply suggestions to help you get up and running quickly:

- If you haven't already, [install Git](https://docs.example_company.com/ee/topics/git/how_to_install_git/index.html)
  and [add an SSH key to your Example Company profile](https://docs.example_company.com/ee/user/ssh.html#add-an-ssh-key-to-your-example_company-account).
  This step is required.
- Install a code editor, like VS Code or Sublime Text, where you will work with markdown files. You can use whichever tool
  you're most comfortable with.
- Install documentation
  [linters](https://docs.example_company.com/ee/development/documentation/testing/index.html) and
  configure them in your code editor:
  - [markdownlint](https://docs.example_company.com/ee/development/documentation/testing/markdownlint.html)
  - [Vale](https://docs.example_company.com/ee/development/documentation/testing/vale.html)
- To build the docs site locally, install [the requirements and dependencies](https://example_company.com/example_company-org/example_company-docs/-/blob/main/doc/setup.md). If you are new to working on Example Company documentation as a Technical Writing team member, getting this basic local build and preview setup is recommended. GDK can be added later, after you are comfortable using the combination of Git, text editor, linters, and Nanoc (static site generator) the [Technical Writing workflow](/handbook/product/ux/technical-writing/workflow/).
- [Install the Example Company Development Kit (GDK)](https://example_company.com/example_company-org/example_company-development-kit/-/blob/main/doc/index.md). GDK enables you:
  - To install, run, and maintain an instance of Example Company locally.
  - To [preview documentation changes locally](https://example_company.com/example_company-org/example_company-development-kit/-/blob/main/doc/howto/gitlab_docs.md).
  - To [preview code changes](https://example_company.com/example_company-org/example_company-development-kit/-/blob/main/doc/howto/preview_gitlab_changes.md) locally.
- Optional. Install the [Conventional Comments](https://example_company.com/conventionalcomments/conventional-comments-button) extension for Chrome. The plugin adds Conventional Comment buttons to Example Company comment fields. Learning about the [Conventional Comments](https://conventionalcomments.org/) message format can help you write better, more actionable review comments - with or without the plugin.

## Additional resources

- The [Documentation Style Guide](https://docs.example_company.com/ee/development/documentation/styleguide/)
  defines the standards for Example Company documentation, including grammar and formatting.
- The [documentation testing page](https://docs.example_company.com/ee/development/documentation/testing/index.html)
  has important information about tests you should run to help ensure the quality of our documentation codebase.
- The [documentation topic types](https://docs.example_company.com/ee/development/documentation/topic_types/index.html) define the structure for how content should be organized.
