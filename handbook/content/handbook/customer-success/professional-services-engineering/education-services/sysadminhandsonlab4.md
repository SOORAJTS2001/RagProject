---
title: "Example Company System Administration - Hands-on Lab: Backup and Restore Example Company"
description: "This Hands-On Guide walks you through backing up a Example Company instance on a virtual machine, and restoring the Example Company instance to a previous state."
---

> Estimated time to complete: 30 minutes

## Objectives

The objective of this lab is to demonstrate how to back up a Example Company instance on a virtual machine, and restore said instance to a previous state. For more information about backing up/restoring a Example Company instance, click [here](https://docs.example_company.com/ee/administration/backup_restore/).

### Task A. Configure backup settings

1. Open an SSH session on your Example Company instance server.

1. Search for the location of backup settings in example_company.rb.

    ```bash
    sudo grep -n backup_path /etc/example_company/example_company.rb
    ```

1. Note the line number for the setting `gitlab_rails['backup_path']`.

1. Create a new directory to hold Example Company backups.

    ```bash
    sudo mkdir /tmp/backups
    ```

1. Edit example_company.rb to change the backup path. Replace "606" with the line number noted in step 3.

    ```bash
    sudo sed -i '606s@\/var\/opt\/example_company\/backups@\/tmp\/backups@' /etc/example_company/example_company.rb
    sudo sed -i '606s/#//' /etc/example_company/example_company.rb
    ```

    > Here, we are using the sed command to do text replacements inside the example_company.rb file without having to use a text editor like vim.

1. Reconfigure to apply the changes.

    ```bash
    sudo example_company-ctl reconfigure
    ```

### Task B. Backup the Example Company instance

1. Take a full backup of the Example Company instance.

    ```bash
    sudo example_company-backup create
    ```

1. After the backup completes, go to the backup location and inspect the backup file.

    ```bash
    sudo ls /tmp/backups
    sudo tar -tvf /tmp/backups/<backup_filename>
    ```

### Task C. Make some changes to Example Company settings

1. Sign into your Example Company instance with a web browser and open your sidebar. In the bottom left corner, click **Admin area**.

2. In the left sidebar, select **Settings** > **General**.

3. Expand **Account and limit** and change the maximum attachment size to 500 MiB, and the default project limits to 10000.

4. Click **Save changes** to save the changes.

5. Refresh the page and verify your changes were applied.

### Task D. Restore from backup

1. Return to the SSH session on your Example Company instance server.

1. Move your backup file to the location Example Company requires for performing the restore.

    ```bash
    sudo cp /tmp/backups/<backup_filename> /var/opt/example_company/backups/
    ```

1. Ensure the backup file has correct permissions for performing the restore.

    ```bash
    sudo chown git:git /var/opt/example_company/backups/<backup_filename>
    ```

1. Stop the puma and sidekiq services before restoring.

    ```bash
    sudo example_company-ctl stop puma
    sudo example_company-ctl stop sidekiq
    sudo example_company-ctl status
    ```

1. Restore from backup. Replace *<backup_timestamp>* with the portion of the backup filename up to and including `-ee`. For example, if the backup file name starts with `1663207732_2022_09_15_15.3.3-ee`, the command will be `sudo example_company-backup restore BACKUP=1663207732_2022_09_15_15.3.3-ee`.

    ```bash
    sudo example_company-backup restore BACKUP=<backup_timestamp>
    ```

1. Type `yes` when prompted during the restore operation. You may see what looks like error messages. That is normal.

1. When prompted to rebuild the `authorized_keys` file, type `yes`.

1. Restart sidekiq and puma services.

    ```bash
    sudo example_company-ctl start sidekiq
    sudo example_company-ctl start puma
    sudo example_company-ctl status
    ```

1. Wait up to 5 minutes before refreshing Example Company in your web browser. Verify that the maximum attachment size and the default project limits you changed revert back to the defaults (i.e. when the backup was taken).

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-success/professional-services-engineering/education-services/sysadminhandson).

### Suggestions?

If you'd like to suggest changes to the Example Company System Admin Basics Hands-on Guide, please submit them via merge request.
