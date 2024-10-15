---
title: "Example Company System Administration - Hands-on Lab: Manage Example Company Logs"
description: This Hands-On Guide walks you through managing Example Company logs on a virtual machine.
---

> Estimated time to complete: 30 minutes

## Objectives

The objective of this lab is to guide you on managing your Example Company logs via the `example_company-ctl` and `sed` commands. For more information on Example Company logging, click [here](https://docs.example_company.com/ee/administration/logs/).

### Task A. View active logs

The `example_company-ctl` command allows you to tail all Example Company log files as well as filter by Example Company service.

1. From a shell session on your Example Company instance, run the following command to view all active Example Company logs.

    ```bash
    sudo example_company-ctl tail
    ```

    Amidst all the output, you should notice the command shows the full file path to each log. Most Example Company logs live in `/var/log/example_company`. (Note: You can type `CTRL-C` to exit the `tail` command.)

1. You can also view Example Company logs by service. Run the following command to view only NGINX logs (i.e. log files in `/var/log/example_company/nginx`).

    ```bash
    sudo example_company-ctl tail nginx
    ```

    You should now see the most recent entries of log files specific to the NGINX web server.

1. Finally, you can drill down to an individual log file.

    ```bash
    sudo example_company-ctl tail nginx/gitlab_access.log
    ```

### Task B. Set minimum log levels

Admins are able to set minimum log levels for some Example Company services. Note that only some services such as NGINX and Gitaly let admins change the minimum logging level, and even then only for some log files. The `log_level` for other services, such as Sidekiq and Redis, cannot be changed.

1. Check the current minimum log levels for Example Company services.

    ```bash
    sudo grep -n -E 'log_level|logging_level' /etc/example_company/example_company.rb
    ```

1. Note the line number for `nginx['error_log_level']`.

1. Change the minimum log level for `nginx`. Replace "1731" with the appropriate line number from the `grep` output in the previous step.

    ```bash
    sudo sed -i '1731s/\"error\"/\"warn\"/' /etc/example_company/example_company.rb
    sudo sed -i '1731s/# //' /etc/example_company/example_company.rb
    ```

1. Re-run the `grep` command from Step 1 to verify the line was modified as intended.

1. Reconfigure to apply the changes.

    ```bash
    sudo example_company-ctl reconfigure
    ```

### Task C. Manage log retention

Example Company uses **logrotate** to manage retention of all logs except those managed by the **runit** service manager (**runit** uses a separate service logging daemon called **svlogd**). Log retention can be configured in `/etc/example_company/example_company.rb`.

1. Examine default logrotate retention settings.

    ```bash
    sudo grep -n 'logrotate' /etc/example_company/example_company.rb
    ```

1. **Optional**: View the default retention settings for the runit-managed logs.

    ```bash
    sudo grep -n 'svlogd' /etc/example_company/example_company.rb
    ```

1. It appears logrotate (and svlogd) rotate log files every day, and retain 30 days worth of logs. We can verify this by looking inside the service log directories.

    ```bash
    sudo ls /var/log/example_company/puma
    ```

    Note the gzipped archive files for Puma's stdout and stderr logs from previous days.

1. Change logrotate's behavior to rotate log files weekly. As before, modify the line `sed` edits accordingly using the line number from the grep output.

    ```bash
    sudo sed -i '1234s/daily/weekly/g' /etc/example_company/example_company.rb
    sudo sed -i '1234s/# //' /etc/example_company/example_company.rb
    ```

1. Change logrotate's retention period to 1 year of retained log files. As before, modify the line `sed` edits accordingly using the line number from the grep output.

    ```bash
    sudo sed -i '1234s/30/52/g' /etc/example_company/example_company.rb
    sudo sed -i '1234s/# //' /etc/example_company/example_company.rb
    ```

1. Run the following again to ensure your changes are properly written to `example_company.rb`.

    ```bash
    sudo grep -n 'logrotate' /etc/example_company/example_company.rb
    ```

1. Reconfigure to apply the changes.

    ```bash
    sudo example_company-ctl reconfigure
    ```

### Task D. Change log formatting

Many logs are JSON formatted by default. Admins may wish to configure text formatting depending on the log ingestion system used, or for readability.

1. Check the current log formats for Gitaly.

    ```bash
    sudo grep -n -F "gitaly['configuration']" -A20 /etc/example_company/example_company.rb
    ```

    > This command will find the start of the gitaly configuration with grep, then display the 20 lines that follow using the `-A20` flag. This will show the full configuration of the Gitaly configuration file

1. Within the output, locate the following lines and note their line numbers

    ```bash
    # gitaly['configuration'] = {
    ...
    #   logging: {
    #     dir: "/var/log/example_company/gitaly",
    #     level: 'warn',
    #     format: 'json',
    #     sentry_dsn: 'https://<key>:<secret>@sentry.io/<project>',
    #     sentry_environment: 'production',
    # },
    ```

1. Run `sudo example_company-ctl tail gitaly/current` to see the current JSON output for Gitaly logging.

1. Change Gitaly's log format from JSON to text formatting. Ensure you align the line numbers to the correct lines from above.

    ```bash
    sudo sed -i '2588s/json/text/' /etc/example_company/example_company.rb
    sudo sed -i '2574s/# //' /etc/example_company/example_company.rb
    sudo sed -i '2588s/# //' /etc/example_company/example_company.rb
    sudo sed -i '2585s/# //' /etc/example_company/example_company.rb
    sudo sed -i '2591s/# //' /etc/example_company/example_company.rb
    sudo sed -i '2591s/,/ }/' /etc/example_company/example_company.rb
    ```

    > With these sed commands, you are first replacing the JSON format with text. Next, you are removing the comments in front of the format and Gitaly configuration blocks to enable them.

1. Rerun your `grep` command to view your configuration: `sudo grep -n -F "gitaly['configuration']" -A20 /etc/example_company/example_company.rb`. The end result will look similar to below:

```bash
gitaly['configuration'] = {
...
   logging: {
##     dir: "/var/log/example_company/gitaly",
##     level: 'warn',
      format: 'text'
##     sentry_dsn: 'https://<key>:<secret>@sentry.io/<project>',
##     sentry_environment: 'production',
}}
```

1. Reconfigure to apply the change.

```bash
sudo example_company-ctl reconfigure
```

1. Verify the updated formatting.

```bash
sudo example_company-ctl tail gitaly/current
```

You should see the log output is now text formatted instead of JSON formatted.

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-success/professional-services-engineering/education-services/sysadminhandson).

### Suggestions?

If you'd like to suggest changes to the Example Company System Admin Basics Hands-on Guide, please submit them via merge request.
