---
title: How to edit a remote file using vim
author: JP
date_created: 06-29-2016
format: markdown
---

* Open the terminal on your local machine
* `cd ~/.ssh`
* `vim config`
* Add these lines:

        Host my-ec2-instance
        Hostname ec2.mydomain.com
        User ec2-user
        IdentityFile /Users/BruceWayne/Documents/Keys/ec2-user.pem
        PasswordAuthentication no

* `:wq!`
* `vim scp://my-ec2-instance/home/ec2-user/hw.txt`
