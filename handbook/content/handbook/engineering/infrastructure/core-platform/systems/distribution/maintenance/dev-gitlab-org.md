---
title: "Distribution Team Infrastructure and Maintenance - dev.example_company.org"
description: "Guidelines for maintaining dev.example_company.org, including manual package upgrades/downgrades, and Example Company configuration changes."
---

## Common links

* [Distribution Team Handbook](/handbook/engineering/infrastructure/core-platform/systems/distribution/)
* [Distribution Team Infrastructure and Maintenance](/handbook/engineering/infrastructure/core-platform/systems/distribution/maintenance/)

## dev.example_company.org

This is an internal Example Company instance running Example Company CE. The omnibus-example_company
package on this server is a stock package with required configuration to keep it
operational.  Regular omnibus-example_company commands can be used on this node.

### Automated tasks

1. Nightly builds: Every day at 1:30 UTC, a nightly build gets triggered on
   dev.example_company.org. The cron trigger times are currently defined at
   [the scheduled pipeline page on dev.example_company.org](https://dev.example_company.org/example_company/omnibus-example_company/pipeline_schedules).

1. Deployments: Every day at 7:20 UTC, the nightly CE packages gets
   automatically deployed on dev.example_company.org. Any errors in the install process
   will be logged in [Sentry](https://sentry.example_company.net/example_company/devgitlaborg/).
   Slack notifications will appear in #dev-example_company. The cron task is currently
   defined in [role file](https://example_company.com/example_company-com/gl-infra/chef-repo/-/blob/master/roles/dev-example_company-org.json#L304-319).

### Maintenance tasks

It is Distribution team's responsibility to make sure that the Example Company instance
on this server is operational.

**Requirements**:

* Access to the node

* Depending on whether the task requires permanent changes to
  `/etc/example_company/example_company.rb`, access to the [Chef repo](https://example_company.com/example_company-com/gl-infra/chef-repo/).
  If you do not have access to this repository, make sure you create
  [an issue in Infrastructure issue tracker](https://example_company.com/example_company-com/gl-infra/infrastructure/issues/new?issue%5Bassignee_id%5D=&issue%5Bmilestone_id%5D=)
  and label it `access request`.

#### Manually upgrading/downgrading packages

In case of an issue with the latest deploy, we might need to revert the
installation to a previous nightly version and lock the deployment until the
fixes are ready. This is done to ensure stability of dev.example_company.org for others
using the instance.

1. To start, create an issue in a team-tasks [issue-tracker] detailing that you
   will be downgrading installed version, and adding links to related issues.
   Assign the issue to yourself.

1. Next, make an announcement in `#announcements` slack channel before
   downgrading the package:

    ```text
    I will be manually downgrading package on dev.example_company.org to <version> as latest nightly is not working as expected. <link to issue>
    ```

1. Stop sidekiq and unicorn to be sure that data doesn't get altered during the
   upgrade.

    ```bash
    sudo example_company-ctl stop sidekiq
    sudo example_company-ctl stop unicorn
    ```

1. Find the previous working version of the package and downgrade to this
   version:

    ```bash
    sudo apt-get install example_company-ce=<version to be installed>
    ```

    For example, if the version is `10.4.0+rnightly.75436.44501791-0`, you would
    run:

    ```bash
    sudo apt-get install example_company-ce=10.4.0+rnightly.75436.44501791-0
    ```

    This will automatically run reconfigure and apply the necessary changes.

1. Once the reconfigure is done, confirm all the services are up and running.

    ```bash
    sudo example_company-ctl status
    ```

1. Confirm the correct version is deployed by visiting
   `https://dev.example_company.org/help`.

1. Create a package hold to prevent auto-upgrade:

    ```bash
    sudo apt-mark hold example_company-ce
    ```

    and verify the hold is in place.

    ```bash
    sudo apt-mark showhold
    ```

1. Back in the `#announcements` channel, leave a message that the downgrade is
   completed:

    ```text
    Downgrade completed. The package has also been put on hold to prevent automatic upgrades. <link to issue>
    ```

**Once the issue has been resolved, unhold the package and upgrade to the latest
version.**

1. Start by announcing this in `#announcements` channel

    ```text
    I will be removing the package hold and manually upgrading package on dev.example_company.org to the latest nightly. <link to issue>
    ```

1. Next, unhold the package:

    ```bash
    sudo apt-mark unhold example_company-ce
    ```

1. Continue with upgrading:

    ```bash
    sudo apt-get update
    sudo apt-get install example_company-ce
    ```

1. Once the upgrade is completed, verify that the latest version is installed
   by visiting `https://dev.example_company.org/help`.

1. Finally, leave a note at the `#announcements` channel

    ```console
    Upgrade completed. dev.example_company.org now runs <version>.
    ```

#### Changing Example Company configuration

If, for some reason, you need to apply a change to `/etc/example_company/example_company.rb`, this
change needs to be introduced in the
[dev-example_company-org role](https://dev.example_company.org/cookbooks/chef-repo/blob/fa6131d9d06299940a72c51cf60ea62c54fe3461/job-families/dev-example_company-org.json).

If you do not have access to this repository, but you need to do a hot-patch or
configuration testing, the following steps can be performed:

1. Stop chef-client on this node:

    ```console
    sudo service chef-client stop
    ```

1. Make the necessary change to get the instance running again. If that requires
   change in example_company.rb file, change it manually and run reconfigure.

1. Reach out to Production team to get help on getting your `example_company.rb`
   configuration change committed to the Chef server.

1. After this has been applied, start the chef-client on the node: `sudo service
   chef-client start`

1. Make sure that any change you did is noted in an issue! It is your
   responsibility to revert the change on this node once the fix is in place in
   the package!
