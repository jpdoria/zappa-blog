---
title: EBS backup and restore script
author: JP
date_created: 05-08-2017
format: markdown
---

# Services With Automated Backups

These are the services that have automated backups by default:  

* Amazon RDS
* Amazon ElastiCache (Redis)
* Amazon RedShift

Unfortunately, Amazon EC2 is not one of them and that is why we need to create a custom script using AWS CLI or AWS SDK.

# Let's Dive A Little Deeper

## RDS

* For MySQL, you need InnoDB (transactional engine)
* There is a *performance hit* if Multi-AZ is not enabled
* Backups are taken against the standby instance to reduce I/O freezes and slow down if multi-AZ is enabled
* If you delete an instance, then *all* automated backups are automatically deleted
* However, manual DB snapshots will *not* be deleted.
* All snapshots are stored on S3
* When you do a restore, you can change the engine type (SQL Standard to SQL Enterprise for example), provided you have enough storage space
* Retention period: 1-35 days (default: 7 days)

## ElastiCache

* Available for Redis Cache Cluster only
* The entire cluster is snapshotted
* Snapshot will *degrade* performance
* Therefore only set your snapshot window during the least busy part of the day
* All snapshots are stored on S3

## RedShift

* Backups are stored on S3
* By default, Amazon RedShift enables automated backups of your data warehouse cluster with a 1-day retention period
* Amazon RedShift only backs up data that has changed so most snapshots only use up a small amount of your free backup storage (incremental)

## EC2

* No automated backups
* Backups *degrade* the performance, schedule these times wisely
* Snapshots are stored on S3
* Can create automated backups using either the AWS CLI or SDKs
* They are incremental
	* Snapshots only store incremental changes since last snapshot
	* Only charged for incremental storage
	* Each snapshot still contains the base snapshot data

# EBS Backup

## AWS IAM Role Setup

1. Go to **AWS Management Console** > **Identity and Access Management**
1. Go to **Roles** then click **Create new role** button
1. Select **AWS Lambda**
1. Skip Attach Policy by click **Next Step**
1. Give your Role a name
1. Go back to **Roles** page then **find** your new role
1. Click on your new role then go to **Permissions** > **Inline Policies** > Create a new one
1. Select **Custom Policy**
1. Give your policy a name
1. Copy the policy below and paste it there

    <script src="https://gist.github.com/jpdoria/9805232b575cf72f1673a0506adf29cb.js"></script>

1. Click **Validate Policy**
1. Click **Apply Policy**

## AWS Lambda Setup

1. On your laptop or desktop, [clone](https://github.com/jpdoria/ebs-snapshot-python.git) or [download](https://codeload.github.com/jpdoria/ebs-snapshot-python/zip/master) the code as zip then uncompress it
1. Change directory to the `ebs-snapshot-python` or `ebs-snapshot-python-master`
1. Open and edit `user_vars.py`

    <script src="https://gist.github.com/jpdoria/762a946b94c4d7234cf8fb859f06f22a.js"></script>

1. Save your changes in `user_vars.py`
1. Compress `ebs-snapshot.py` and `user_vars.py` into one file (e.g., ebs-snapshot.zip)
1. Open your browser then go to  **AWS Management Console** > **Lambda**
1. Click **Create a Lambda function** > select **Blank Function**
1. Skip Configure triggers by clicking **Next** button
1. Give your function a name and a description
1. Choose **Python 3.6** as runtime
1. Select **Upload a .ZIP file** in **Code entry type**
1. Click **Upload** button
1. Upload the **ebs-snapshot.zip** you created earlier in Step 5
1. Handler: **ebs-snapshot.main**
1. Role: choose the role you created in AWS IAM Role Setup
1. Click **Advanced settings** then set the **Memory (MB)**  to **128**
1. Set the **Timeout** to **5 minutes**
1. Click **Next** button
1. Click **Create function** button

## Amazon CloudWatch Events Setup

1. Go to **AWS Management Console** > **CloudWatch**
1. Go to **Events** > **Rules** > click **Create rule** button
1. Under **Event Source**, select **Schedule**
1. Change the default value of **Fixed rate of** to **1 Day**
1. Under **Targets**, click **Add Target**
1. Select the **ebs-snapshot** function
1. Click **Configure details** button
1. Give your rule a name and a description
1. Tick **State** box to enable the rule
1. Click **Create rule** button

# EBS Restore

## Configuration

You need to install [AWS CLI](http://docs.aws.amazon.com/cli/latest/userguide/installing.html) first then you can configure your account on your local machine using `aws configure`. If you want to use this script on EC2, make sure the instance has a role (best practice).

This is the IAM policy that you should use.

<script src="https://gist.github.com/jpdoria/ca2bfb03db70b2a6f0191b737e7137f9.js"></script>

## Installation

`pip install ebsrs`

## Usage

    mbpr:~ root# ebsrs
    usage: ebsrs [-h] -r REGION -i INSTANCE_ID [-v]
    ebsrs: error: the following arguments are required: -r/--region, -i/--instance-id
    mbpr:~ root# ebsrs --help
    usage: ebsrs [-h] -r REGION -i INSTANCE_ID [-v]

    EBS Restore Snapshot v0.1.0

    optional arguments:
    -h, --help            show this help message and exit
    -r REGION, --region REGION
                            AWS Region
    -i INSTANCE_ID, --instance-id INSTANCE_ID
                            Instance ID (i-1234567)
    -v, --version         Display version
    mbpr:~ root#

## Example

    mbpr:~ root# ebsrs -r ap-southeast-1 -i i-2f0b2aa1
    Region: ap-southeast-1
    InstanceId: i-2f0b2aa1
    Fetching root volume of i-2f0b2aa1...
    VolumeId: vol-0fd09c171ebdac8f5
    Fetching snapshots of vol-0fd09c171ebdac8f5...
    1)	snap-06591742121affdac
        2017-02-16 16:01:08+00:00

    2)	snap-01973940c534a685f
        2017-02-15 16:01:09+00:00

    3)	snap-04459a725001860b7
        2017-02-14 16:01:09+00:00

    Choose a snapshot [1-3]: 3
    Your choice is [3] snap-04459a725001860b7 - 2017-02-14 16:01:09+00:00
    Creating a new volume using snap-04459a725001860b7...
    NewVolumeId: vol-07e5a167e70b6f036
    NewVolumeStatus: available
    Stopping i-2f0b2aa1...
    InstanceStatus: stopped
    OldVolumeId: vol-0fd09c171ebdac8f5
    Detaching old volume from /dev/sda1...
    Old volume is now detached
    Attaching new volume to i-2f0b2aa1 [/dev/sda1]...
    New volume is now attached
    Starting i-2f0b2aa1...
    InstanceStatus: running
    Do you want to remove the old volume? [Y/N] y
    Removing old EBS volume (vol-0fd09c171ebdac8f5)...
    vol-0fd09c171ebdac8f5 has been removed.
    Task completed successfully
    mbpr:~ root#



# Links to GitHub Repositories

If you want to see the source code or contribute, please check the links below:

* [https://github.com/jpdoria/ebs-snapshot-python](https://github.com/jpdoria/ebs-snapshot-python)  
* [https://github.com/jpdoria/ebsrs](https://github.com/jpdoria/ebsrs)
