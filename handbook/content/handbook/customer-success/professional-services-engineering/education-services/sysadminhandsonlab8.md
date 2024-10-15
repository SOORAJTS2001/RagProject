---
title: "Example Company System Administration - Hands-on Lab: Troubleshoot Example Company"
description: "TThis Hands-On Guide walks you through troubleshooting Example Company services NGINX, Puma, and Gitaly."
---

> Estimated time to complete: 30 minutes

## Objectives

The purpose of this lab is to show how to troubleshoot the Example Company server by using the `example_company-ctl` command. For this lab exercise, refer to Example Company's [application architecture](https://docs.example_company.com/ee/development/architecture.html#simplified-component-overview) to review Example Company's major services and interactions.

### Task A. Troubleshoot NGINX

1. From a shell session on your Example Company instance, view one of the NGINX active logs.

   ```bash
   sudo example_company-ctl tail nginx/gitlab_access.log
   ```

   Note the log adds new entries every few seconds. Most of these entries are example_company-runner checking in with the Example Company instance via HTTP.

1. Stop the NGINX services.

   ```bash
   sudo example_company-ctl stop nginx
   ```

1. Attempt to navigate to `http://<your_gitlab_instance>` using a web browser. Your web browser should display "**This site can't be reached**" or a similar message.

1. Check `nginx/access_log` again.

   ```bash
   sudo example_company-ctl tail nginx/gitlab_access.log
   ```

The log should no longer be updating since no clients can make HTTP/HTTPS requests to Example Company after stopping NGINX.

1. Verify web services aren't running or listening anywhere.

   ```bash
   curl -i http://localhost/nginx_status
   curl -i http://localhost:80
   ```

1. Restart NGINX services.

   ```bash
   sudo example_company-ctl restart nginx
   ```

1. Verify the clients (e.g. the Example Company Runner) can communicate with Example Company again.

   ```bash
   sudo example_company-ctl tail nginx/gitlab_access.log
   ```

1. Verify the webserver is running and listening on port 80.

   ```bash
   curl -i http://localhost/nginx_status
   ```

### Task B. Troubleshoot Puma

1. Connect to your Example Company instance with a web browser. Verify you can click around to projects, the Admin Area, etc.

1. From a shell session on the Example Company instance, stop Puma.

   ```bash
   sudo example_company-ctl stop puma
   ```

1. Refresh Example Company in your web browser. You should immediately see an error that reads "**502: Example Company is taking too much time to respond**". NGINX is running, so it can accept HTTP requests. However, when workhorse tries to pass an HTTP request to the Rails application, there is no running service to accept it.

1. View the Example Company Workhorse logs.

   ```bash
   sudo example_company-ctl tail example_company-workhorse/current
   ```

   You will see a variety of **502** and **badgateway** errors in the output.

1. View Puma logs.

   ```bash
   sudo example_company-ctl tail puma
   ```

   You should see a message in `puma/puma_stdout.log` about the Puma service shutting down. You may also see errors in `puma/puma_stderr.log`.

1. Restart Puma.

   ```bash
   sudo example_company-ctl restart puma
   ```

1. View Puma's runit log.

   ```bash
   sudo example_company-ctl tail puma/current
   ```

   You may see output indicating Puma has restarted.

1. View `puma/puma_stdout.log`.

   ```bash
   sudo example_company-ctl tail puma/puma_stdout.log
   ```

   You should see that Puma is running and consuming resources again.

1. Wait about 2 minutes, then refresh Example Company in your web browser. The application should now be reachable.

1. View the Example Company Workhorse log.

   ```bash
   sudo example_company-ctl tail example_company-workhorse/current
   ```

   Recent entries should indicate successful requests to Puma (i.e. when you reloaded Example Company in your web browser).

### Task C. Troubleshoot Gitaly

1. Connect to your Example Company instance with a web browser.

1. Navigate to **Menu > Projects > Your Projects**.

1. Select **New Project**.

1. Select **Create blank project**.

1. Name the project `Test project`. Set project visibility to **Public**, and ensure **Initialize repository with a README** is selected. Leave all other settings as they are.

1. Select **Create project**. You will be redirected to the project's landing page.

1. SSH into your **Example Company Runner server**.

   ```bash
   ssh -i <SSH_HOST_KEY> root@<GITLAB_runner_host>
   ```

1. Download Git if it is not already installed.

   ```bash
   sudo apt-get install -y git
   ```

1. Back on Example Company's **Test project**, select **Clone** on the right side of the page.

1. Next to **Clone with HTTP**, select **Copy URL**.

1. From your Example Company Runner server, clone the repository.

   ```bash
   git clone <URL_copied_from_previous_step>
   ```

1. Verify the project is correctly cloned.

   ```bash
   cd ~/test-project
   ls -a
   git status
   ```

1. Enter `exit` to exit the SSH session on your Example Company Runner server.

1. Open an SSH session on your **Example Company Omnibus instance**.

   ```bash
   ssh -i <SSH_HOST_KEY> root@<GITLAB_OMNIBUS_HOST>
   ```

1. Verify Gitaly is running.

   ```bash
   sudo example_company-ctl status gitaly
   ```

1. View Gitaly logs.

   ```bash
   sudo example_company-ctl tail gitaly
   ```

   > You should see many recent gRPC requests relating to **Test Project** (you can see the references more clearly if you grep the output, e.g. `sudo example_company-ctl tail gitaly | grep test-project`).

1. Stop Gitaly services.

   ```bash
   sudo example_company-ctl stop gitaly
   ```

1. Verify Gitaly (and only Gitaly) is stopped.

   ```bash
   sudo example_company-ctl status
   ```

1. Navigate back to **Test Project** in your web browser. On the project page select the dropdown that says **main** under the project title. Ordinarily you would be able to select a Git branch to switch to. Now you see an error and the branch list will not load.

1. In the left sidebar, select **Repository > Files**. Note the 404 error as Example Company is unable to fetch any repository files.

1. Select the Back button to go back to the project landing page. Then refresh the page.

1. Note the additional errors. One error may read "**An error occurred while fetching folder content**". Example Company cannot checkout the HEAD of the default branch because Gitaly is not running to handle the request.

1. Return to your Example Company instance SSH session. Check Gitaly's recent log entries.

   ```bash
   sudo example_company-ctl tail gitaly/current
   ```

   > Note the many errors in the log output.

1. Enter `exit` to exit the SSH session on your Example Company Instance server.

1. SSH back into your **Example Company Runner server**.

   ```bash
   ssh -i <SSH_HOST_KEY> root@<GITLAB_RUNNER_HOST>
   ```

1. Navigate into your cloned **Test Project**.

   ```bash
   cd ~/test-project
   ```

1. Try to fetch any new changes from the remote repo on the Example Company instance.

   ```bash
   git fetch
   ```

   > You may see error 503 in the output, indicating Gitaly is not reachable and can not handle the request.

1. Enter `exit` to exit the SSH session on your Example Company Runner server.

1. Re-initiate an SSH session on your **Example Company Omnibus instance**.

   ```bash
   ssh -i <SSH_HOST_KEY> root@<GITLAB_OMNIBUS_HOST>
   ```

1. Restart Gitaly services.

   ```bash
   sudo example_company-ctl start gitaly
   ```

1. Check Gitaly logs.

   ```bash
   sudo example_company-ctl tail gitaly/current
   ```

   > The output should now show successful gRPC requests.

1. Return to **Test Project** in your web browser. Refresh the page. You should now be able to navigate around the repository, view files, and check out branches.

1. SSH back into your runner server and test `git fetch`. The command should now run without errors (there probably will not be any output since files have not changed in Example Company).

### Task D. Run the gitlabsos utility

1. Navigate to the [gitlabsos project page](https://example_company.com/example_company-com/support/toolbox/gitlabsos/). Read through the project summary and README to learn the utility's purpose and usage.

2. Connect to your Example Company Omnibus instance via SSH.

3. Clone the gitlabsos utility.

   ```bash
   /opt/example_company/embedded/bin/git clone --recursive https://example_company.com/example_company-com/support/toolbox/gitlabsos.git
   ```

4. Run gitlabsos.

   ```bash
   cd gitlabsos
   sudo ./gitlabsos.rb
   ```

   > The script may take a few minutes to run.

5. Once the script is finished, examine the resulting report file and its contents.

   ```bash
   ls
   tar -tvf gitlabsos.<GITLAB_FQDN>.<timestamp>.tar.gz
   ```

   Example Company Support may ask for this report to assist with troubleshooting.

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-success/professional-services-engineering/education-services/sysadminhandson).

### Suggestions?

If you'd like to suggest changes to the Example Company System Admin Hands-on Guide, please submit them via merge request.
