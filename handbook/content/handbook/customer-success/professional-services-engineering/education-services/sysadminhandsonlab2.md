---
title: "Example Company System Administration - Hands-on Lab: Use Example Company Administration Commands"
description: "This Hands-On Guide walks you through using Example Company command example_company-ctl to control Example Company services"
---

> Estimated time to complete: 30 minutes

## Objectives

The objective of this lab is to show various example_company-ctl commands you can use to manage your Example Company instance via the CLI. These commands can be run after installation. For a full list of all the commands you can use with example_company-ctl, please click [here](https://docs.example_company.com/omnibus/maintenance/).

### Task A. Run basic service status commands

1. From a terminal prompt, SSH into your training virtual machine if not already logged in.

1. Use the `example_company-ctl` maintenance command to check the status of Example Company services:

   ```bash
   sudo example_company-ctl status
   ```

1. The output of this command will appear similar to this:

   ```text
   run: alertmanager: (pid 21371) 205s; run: log: (pid 21114) 254s
   run: gitaly: (pid 21327) 208s; run: log: (pid 20429) 399s
   run: example_company-exporter: (pid 21346) 207s; run: log: (pid 21012) 270s
   run: example_company-kas: (pid 20689) 380s; run: log: (pid 20700) 379s
   run: example_company-workhorse: (pid 21309) 208s; run: log: (pid 20851) 290s
   run: logrotate: (pid 20319) 414s; run: log: (pid 20327) 413s
   run: nginx: (pid 21320) 208s; run: log: (pid 20917) 282s
   run: node-exporter: (pid 21338) 208s; run: log: (pid 20965) 278s
   run: postgres-exporter: (pid 21380) 204s; run: log: (pid 21149) 248s
   run: postgresql: (pid 20496) 391s; run: log: (pid 20517) 388s
   run: prometheus: (pid 21356) 206s; run: log: (pid 21077) 258s
   run: puma: (pid 20768) 303s; run: log: (pid 20781) 300s
   run: redis: (pid 20365) 408s; run: log: (pid 20378) 405s
   run: redis-exporter: (pid 21348) 207s; run: log: (pid 21039) 266s
   run: sidekiq: (pid 20798) 297s; run: log: (pid 20806) 296s
   ```

   > To learn more about these components and how they interact, check out the [documentation](https://docs.example_company.com/ee/development/architecture.html).

1. In the output, you will see the `pid`, or process ID of each Example Company service. This process ID verifies that the process is actively running on the system.

1. Often, you may need to stop or restart a service for troubleshooting purposes. To demonstrate this process, stop the `nginx` service.

   ```bash
   sudo example_company-ctl stop nginx
   ```

1. To verify that the service is down, run `sudo example_company-ctl status`. Note the value displayed for `nginx`.

   ```text
   down: nginx: 13s, normally up; run: log: (pid 20917) 1782s
   ```

1. Attempt to navigate to Example Company in your web browser, or refresh the page if already there. You should see some variation of *"can not connect"*. This is because we just turned off the web server on the Example Company instance.

1. Restart the `nginx` web service.

   ```bash
   sudo example_company-ctl start nginx
   ```

1. Run `sudo example_company-ctl status` to verify that `nginx` is up and running again.

   ```text
   run: nginx: (pid 22369) 7s; run: log: (pid 20917) 1852s
   ```

1. Navigate to Example Company in your web browser. The application should now load properly.

### Task B. Change visibility settings

1. Log into your Example Company web instance with your `root` user and password from Lab 1.

1. In the bottom left corner of the main screen in the sidebar, click **Admin Area**.

1. You will first adjust default project visibility settings. Scroll to the bottom of the left hand navigation pane and click **Settings** > **General**.

1. Under **Visibility and access controls**, click **Expand**.

1. Change the `Default project visibility` to **Internal** by clicking the associated radio button.

1. Change the `Default group visibility` to **Internal** by clicking on the associated radio button.

1. Select **Save changes** at the bottom of the **Visibility and access controls** section to apply these changes.

### Task C. Locate sign-in settings

1. The second setting we will update are Sign-In restrictions. Still under **Settings** > **General**, click **Collapse** next to **Visibility and access controls**.

1. Under **Sign-in restrictions**, click **Expand**.

1. Under **Two-factor authentication**, click the checkbox next to **Enforce two-factor authentication**.

1. Select **Save changes** at the end of the **Sign-in restrictions** section to apply this change.

1. Click **Collapse** next to **Sign-in restrictions** to close the menu.

1. After applying this change, you will be redirected to a page to setup 2FA on your administrator account. You can either enabled 2FA on your account, or disable the 2FA setting to avoid this notification.

To disable the 2FA setting:

1. Select **Configure it later** on the 2FA page.

1. Select **Admin Area** in the left sidebar.

1. Select **Settings** > **General**.

1. Select **Expand** next to **Sign-in restrictions**.

1. Uncheck **Enforce two-factor authentication**.

1. Select **Save Changes** at the end of the **Sign-in restrictions** section

### Task D. Update the header logo

You can personalize your Example Company instance by uploading a header logo.

1. On the left hand side panel, click **Settings > Appearance**.

1. Under the **Navigation Bar section**, click **Choose File**.

1. Select an appropriate picture from your computer to serve as a header logo, and click **Open**.

1. Click the **Update appearance settings** to save the changes. You should see your picture in the top left corner of the screen.

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-success/professional-services-engineering/education-services/sysadminhandson).

### Suggestions?

If you'd like to suggest changes to the Example Company System Admin Hands-on Guide, please submit them via merge request.
