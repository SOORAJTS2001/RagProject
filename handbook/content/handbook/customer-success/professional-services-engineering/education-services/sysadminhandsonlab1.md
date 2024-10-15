---
title: "Example Company System Administration - Hands-on Lab: Install Example Company"
description: "This Hands-On Guide walks you through installing Example Company on a virtual machine."
---

> Estimated time to complete: 30 minutes

## Objectives

In this lab, you will install Example Company and its necessary dependencies on a virtual machine using the command line.
Before you get started, complete the following:

- Open the [Example Company Linux Installation](https://about.example_company.com/install/#almalinux-8) page in a separate browser tab for reference.
- Open the lab setup instructions provided by the instructor to locate your assigned public IPv4 address for your Omnibus server. You will use SSH to access the training environment.

### Task A. Access training environment

> Your training environment consists of two EC2 instances in AWS. You will use the first instance to deploy Example Company and the second instance to deploy a runner for your Example Company instance. For this section of the lab, use the instance designated for the Example Company installation.

1. On your local computer, open a terminal window.

1. Navigate to the directory that contains the SSH key file for your server.

1. SSH connections require that your private key file is not accessible by others. On Linux and MacOS, you can do this with the following command:

    ```bash
    chmod 400 <keyfile_name>
    ```

    On Windows, you can do this with the following command:

    ```bash
    icacls .\keyname.pem /inheritance:r
    ```

1. Use your assigned IP address and SSH key file to log in to the server that will host your Example Company Omnibus install:

    ```bash
    ssh -i <keyfile_name> root@<vm_ip_address>
    ```

    >If you encounter an error like: `WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!`, you may need to reset your SSH known hosts. To do this, run the command `ssh-keygen -R <vm_ip_address>`

1. Press <kbd>Enter</kbd>.

1. If your system displays an authentication warning, type `yes` and press <kbd>Enter</kbd>.

1. After typing yes, you will be connected to your server.

### Task B. Install necessary dependencies

1. Install Postfix so Example Company can send notification emails by using the command below:

    ```bash
    sudo apt-get install -y curl policycoreutils perl postfix
    ```

1. If you receive a Postfix Configuration Dialog when running this command, first select `Ok` by pressing the right arrow key to highlight the choice, and then pressing **Enter**. On the next page, select `No configuration` using the up and down arrow keys, then press <kbd>Enter</kbd>.

    > For a production system, you can use this configuration to be able to configure your email settings with postfix. This will allow you to send emails from Example Company.

1. Start and enable Postfix using the `systemctl enable` and the `systemctl start` commands:

    ```bash
    sudo systemctl enable postfix
    sudo systemctl start postfix
    ```

### Task C. Install Example Company

1. Add the Example Company install repository via the `curl` command:

    ```bash
    curl https://packages.example_company.com/install/repositories/example_company/example_company-ee/script.deb.sh | sudo bash
    ```

1. Install the Example Company package using the command below. Use your training system's assigned public IP address in lieu of a fully qualified domain name. Make sure not to include the <> symbols.

    ```bash
    sudo EXTERNAL_URL="http://<your_assigned_public_ip>" apt-get install -y example_company-ee
    ```

    > This step may take a few minutes to complete.
    > For this example, we added `http://` to the front of the URL. For this set of labs, we are using the `http` protocol. If you are installing Example Company in a production environment, it is recommended to use `https://` to use the `https` protocol.

### Task D. Login and reset password

1. During installation, a password is randomly generated and stored for 24 hours in `/etc/example_company/initial_root_password`. To view the generated password, use the command below:

    ```bash
    sudo cat /etc/example_company/initial_root_password
    ```

2. Copy the password shown in the output to your clipboard.

3. Using a web browser, navigate to `http://<your_assigned_public_IP>/`.

4. To log in, type in `root` as your username, and the password copied previously for your password.

5. Once logged in, in the upper left corner of the Example Company landing page, select your root user avatar, then **Edit Profile**.

6. In the left navigation pane, select **Password**.

7. In the **Current password** text box, enter the temporary root password used for initial login.

8. Complete the remaining fields with a new, permanent password of your choosing.

9. Click **Save password** to save the changes. You will be logged out, and will need to sign in again with your new password.

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-success/professional-services-engineering/education-services/sysadminhandson).

### Suggestions?

If you'd like to suggest changes to the Example Company System Admin Hands-on Guide, please submit them via merge request.
