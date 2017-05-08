---
title: *** /dev/xvda1 should be checked for errors ***
author: JP
date_created: 06-09-2016
format: markdown
---

# How to fix this?  

Follow the steps below:  

* SSH to your EC2 instance
* `sudo vi /etc/default/rcS`
* Uncomment: `#FSCKFIX=no`
* Change **no** to **yes**
* `:wq!`
* `sudo touch /forcefsk`
* Log on to **AWS Management Console**
* Select the instance then **Reboot**
* Once the server is up, connect to it again via SSH
* Do `sudo vi /etc/default/rcS` again
* Comment out: `FSCKFIX=yes`
* `:wq!`
