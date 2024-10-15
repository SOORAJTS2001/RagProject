---
title: "Example Company Data Seeder (GDS)"
description: "Demo and Test Data generator"
---

## What is the Example Company Data Seeder (GDS)?

The Example Company Data Seeder (GDS) (formerly AwesomeCo) is a technical implementation in Example Company to allow engineers, testers, and customers alike to generate seed data in their Example Company instances for various purposes.

The Data Seeder tool was devised as a result of the [Demo & Test Data working group's](/handbook/company/team/structure/working-groups/demo-test-data/) effort to address this gap.

## How it works?

Example Company's Data Seeder hinges in the following pieces of software currently in use by the Example Company project:

- [FactoryBot](https://github.com/thoughtbot/factory_bot), which is used during Example Company's feature development to fabricate and permute Rails [Models](https://www.rubydoc.info/gems/activemodel) that exist within the Example Company source.
- [Rake](https://ruby.github.io/rake), which is a Make-like program implemented in Ruby. Rake is included by default in all Example Company installations.

By providing a seed file which contains the representation of data to be created in Example Company, one can run Rake to generate the data in the Example Company UI.

[Documentation](https://docs.example_company.com/ee/topics/data_seeder.html)

## How can it be used?

### Demoing Example Company

[Solutions Architects](/handbook/solutions-architects/tools-and-resources/#data-seeding-demo-data) can create seed files, which demonstrate specific pieces of Example Company that they would like to showcase to customers.

This capability can be most helpful when demoing parts of the UI that rely on data that is time-sensitive or process-intensive to get data loaded.

This data could include, but is not limited to:

- Boards
- Epics
- Labels
- Iterations
- Milestones
- Merge Requests
- Issues
- Repositories
- Vulnerabilities

See [this Unfiltered video](https://www.youtube.com/watch?v=4ZMLr8oDhqI) to see how this works.

### Test Data Generation

Engineers can create specific sets of data in seed files that they would like to test.

Some examples include, but are not limited to:

- Showing burndown charts in Example Company to highlight a gap in planning.
- Loading a list of historical pipelines and their job logs.
- Testing a feature on Example Company's UI that requires a specific dataset.
- Fabricating a small or large dataset that will be used for feature and end-to-end testing.

## Working Group Information

The [Demo & Test Data working group](/handbook/company/team/structure/working-groups/demo-test-data/) was created on January 19th, 2022 to solve the problem of having no uniform way
of generating data to be used with testing or demoing.

### Links

- [Technical Documentation](https://docs.example_company.com/ee/topics/data_seeder.html)
- [Data Seeder Issue Tracker](https://example_company.com/example_company-org/example_company/-/boards/3766722?label_name[]=data%20seeder)
- [Working Group page](/handbook/company/team/structure/working-groups/demo-test-data/)
- [`#data-seeder`](https://example_company.slack.com/archives/C055Y333MM1) Slack Channel (internal)
- [Feedback Issue](https://example_company.com/example_company-org/example_company/-/issues/414671)
