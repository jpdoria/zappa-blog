---
title: CloudBerry Managed Backup Service
author: JP
date_created: 05-05-2017
format: markdown
---

#  Objective

One of our clients needs a good backup solution to cloud for their servers that are located in their remote offices. They want it to be always available and durable.

When I heard the words: *always available* and *durable*, I immediately thought of [Amazon S3](https://aws.amazon.com/s3/) and the good thing about it is CloudBerry is built for cloud storage like Amazon S3.

For those who don't know what Amazon S3 is, it is basically a secure and durable place to store your data. It has durability of 99.999999999% (yes, 11 nines!) of objects and it is designed for 99.99% availability over a given year.

# Server Specs

I have no information about what type of CPU, how many gigs of RAM, and disk space, etc. They don't matter anyway. I only need the OS and they are using Centos 5.5 and 6.8.

# What is CloudBerry Managed Backup Service
CloudBerry Managed Backup Service is designed to meet the needs of managed service providers and enterprise IT departments, providing reliable backup with central management, and monitoring.

# Why CloudBerry Managed Backup

* It is built for the cloud
* Simple management and full control
* Fully customizable design
* Cross-platform cloud backup
* Easy to setup and sell
* Integration options / API

# Signing Up
Signing up is easy! You just have to go to CloudBerry Managed Backup [Sign Up Page](https://www.cloudberrylab.com/managed-backup.aspx) and fill out the form, then you will receive an email containing your temporary password and instructions for logging on to the console.

# Logging In

To view the console, you can go to [https://mbs.cloudberrylab.com](https://mbs.cloudberrylab.com).

![alt text](https://cdn.lazyadm.in/cloudberry-managed-backup-service/cmbs-console.png "CloudBerry Managed Backup Service Console")

# Setup

## Storage
Once you log in to the console you will have to go through the **Wizard**. Add your **Amazon S3** [account details](http://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys) and a bucket.

## Service Account Creation

From your dashboard, go to **Users** then **Users**.

![alt text](https://cdn.lazyadm.in/cloudberry-managed-backup-service/cmbs-dashboard.png "CloudBerry Managed Backup Service Dashboard")

Click the **Create User** button.

![alt text](https://cdn.lazyadm.in/cloudberry-managed-backup-service/cmbs-user-list.png "User List")

When you are in the **Add User** page, you need to provide some information about the service account.

Example:

* **First Name**: Backup
* **Last Name**: Administrator
* **Login/Email\***: backup@company.com
* **Initial Password\***: passw0rd2017!
* **Company**: company
* **Account**: Amazon S3 & Glacier
* **Bucket**: cbb-s3-bucket
* **Storage Limit**: company-storage-limit
* **User enabled**: Active
* **Licenses**: User activates paid licenses from the pool automatically

Once the account is created, you will then see it in the **User List**.

![alt text](https://cdn.lazyadm.in/cloudberry-managed-backup-service/cmbs-user-list-new.png "User List")

Please note that this account does not have a permission to log on to the console. If you need an account to access the console and manage your backups, you need to create an account in **Administrators** page.

## Build

First off, you need to get the latest version of the builds by going to **Downloads** then clicking the **Request Custom Build** button.

![alt text](https://cdn.lazyadm.in/cloudberry-managed-backup-service/cmbs-request-custom-build.png "Request Custom Build")

You will receive an email notification once the build is complete. So after checking your email, go back to the **Downloads** page then find **Backup for Red Hat, Fedora, CentOS, SUSE, Oracle Linux** then click the **Make public** button.

After clicking the button, you should see the build for Linux under **Custom Builds (available to end users)**. Right click on it then **Copy Link Address**.

![alt text](https://cdn.lazyadm.in/cloudberry-managed-backup-service/cmbs-request-custom-build-available-to-end-users.png "Custom Build (available to end users)")

## Installation

Now that you have the download link of the latest build for Linux, connect to your EC2 instance via SSH then download the agent using `cURL` or `wget`.

Commands:

* `curl -O <download url>`  
* `curl -o <new filename> <download url>`  
* `wget <download url>`  
* `wget <download url> -O <new filename>`

![alt text](https://cdn.lazyadm.in/cloudberry-managed-backup-service/cmbs-download-agent.png "Download Agent")

You can now install the package using `yum`. The command to use is `yum install <package name>`

![alt text](https://cdn.lazyadm.in/cloudberry-managed-backup-service/cmbs-agent-installation-1.png "Download Agent")
![alt text](https://cdn.lazyadm.in/cloudberry-managed-backup-service/cmbs-agent-installation-2.png "Download Agent")

The installation directory is `/opt/local/Online Backup`. There is a script in `bin` directory so you need to add that to your `PATH` if you want to run the `cbb` script from anywhere.

To add it, issue this command: `export PATH=$PATH:'/opt/local/Online Backup/bin'`.

![alt text](https://cdn.lazyadm.in/cloudberry-managed-backup-service/cmbs-path.png "Path")

Now you can add your CloudBerry Backup account by issuing this command: `cbb addAccount -e <email address> -p <account password> -ssl yes`.

![alt text](https://cdn.lazyadm.in/cloudberry-managed-backup-service/cmbs-add-account.png "cbb addAccount")

## Verification

To verify if installation is successful, open your browser again then go to **CloudBerry Managed Backup Service Console** then **RMM** then **Remote Management** and you will see that the server is now registered.

![alt text](https://cdn.lazyadm.in/cloudberry-managed-backup-service/cmbs-rmm.png "RMM")

# Backup

Now that the server is registered, you can now create a backup plan and create your first backup!

To do this, click the **cog icon** then select **Show Plans**.

![alt text](https://cdn.lazyadm.in/cloudberry-managed-backup-service/cmbs-cog.png "Show Plans")

Once you are in the **plan list**, click the **Create Backup Plan** button then **Backup Files Plan** then you will be redirected to the **Create Backup plan** page and you need to provide some information.

* **Plan Name** - name of your backup plan
* **Backup Source** - directories or files that you want to backup (e.g., /home/ec2-user)
* **Backup Storage** - backup storage (e.g., Amazon S3)
* **Advanced Filter** - options: backup empty folders and do not backup system and hidden files
* **Compression and Encryption Options** - compression, encryption, and s3 storage options
* **Retention Policy** - backup retention policy
* **Schedule Options** - backup schedule
* **Pre/Post Actions (*coming soon*)** - actions to execute before and after the backup
* **Notification** - receive notification email when backup completes (backup fails or all cases)

After you have created your first backup plan, click the **Start** button. The status of backup (**Last Result**) will be shown in the same page.

![alt text](https://cdn.lazyadm.in/cloudberry-managed-backup-service/cmbs-backup-success.png "Backup Success")

# Restoration
Let's try to restore the backup. While in the **plan list** page, click **Create Restore Plan** then **Restore Files Plan** then you will be redirected to the **Create Restore plan page** and you need to provide some information.

* **Plan Name** - name of your restore plan
* **Backup Type** - backup version
* **Restore Source** - storage where the backup is stored and list of directories and files available for restoration (e.g., /home/ec2-user)
* **Destination** - restore to original location or restore to a specific location, restore deleted files, overwrite existing files or restore only new files
* **Compression and Encryption Options** - decryption
* **Scheduled Options** - restoration schedule
* **Notification** - receive notification email when restoration completes (restoration fails or all cases)

After you have created your first restore plan, click the **Start** button. The status of restoration (**Last Result**) will be shown in the same page.

![alt text](https://cdn.lazyadm.in/cloudberry-managed-backup-service/cmbs-restore-success.png "Restoration Success")

# Consistency Check

Prior to backup, I created a text file in `/home/ec2-user` called `hello-world.txt` and the content is `ip-192-168-254-112`. Now let's check if the original file and restored file are identical using this command: `md5sum <filename>`. By the way, I chose not to restore the file to its original location. I restored it to `/tmp/restore`.

![alt text](https://cdn.lazyadm.in/cloudberry-managed-backup-service/cmbs-consistency-check.png "md5sum")

# Learn More

To learn more about CloudBerry Managed Backup Service, check the following links:

* [https://www.cloudberrylab.com/managed-backup.aspx](https://www.cloudberrylab.com/managed-backup.aspx)
* [https://www.cloudberrylab.com/backup-faq.aspx](https://www.cloudberrylab.com/backup-faq.aspx)
* [https://mspbackups.com/Admin/Help.aspx?c=Contents/help\_command\_line_interface.html](https://mspbackups.com/Admin/Help.aspx?c=Contents/help_command_line_interface.html)
* [https://mspbackups.com/v2.0/Help](https://mspbackups.com/v2.0/Help)
