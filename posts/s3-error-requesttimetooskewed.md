---
title: S3 Error: RequestTimeTooSkewed
author: JP
date_created: 07-07-2016
format: markdown
---

# Error Message

    [root@eng1_srva sql]# aws s3 ls s3://mys3bucket9999/

    An error occurred (RequestTimeTooSkewed) when calling the ListObjects operation: The difference between the request time and the current time is too large.
    [root@eng1_srva sql]#

# How to fix this?

* `yum install -y ntp`
* `vim /etc/ntpd.conf`
* Comment out lines with **x.centos.pool.ntp.org** (lines 22-25)
* Add the following:
    * **server 0.amazon.pool.ntp.org iburst**
    * **server 1.amazon.pool.ntp.org iburst**
    * **server 2.amazon.pool.ntp.org iburst**
    * **server 3.amazon.pool.ntp.org iburst**
* `:wq!`
* `service ntpd restart`
* Compare times: `curl -v --silent http://s3.amazonaws.com 2>&1 | grep Date; date -u`
