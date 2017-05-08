---
title: How to install Logstash in your EC2 web server via Elastic Beanstalk and forward the logs to your existing Amazon Elasticsearch Service
author: JP
date_created: 06-28-2016
format: markdown
---

* `cd my-node-js-app`
* `mkdir .ebextensions`
* `cd .ebextensions`
* `vim logstash.config`

    <script src="https://gist.github.com/jpdoria/1a55ac00ba70092342acd51fa373aef7.js"></script>

* `:wq!`
* `zip -r9 my-node-js-app.zip .`
* Launch your browser then go to **Elastic Beanstalk** via AWS Management Console
* Click **Create New Application**
* Application Name: **my-node-js-app**
* Click **Next**
* Click **Create web server**
* Predefined configuration: **Node.js**
* Environment type: **Single instance**
* Click **Next**
* Upload **my-node-js-app.zip**
* Click **Next**
* Environment Name: **myNodeJsApp-env**
* Environment URL: **mynodejsapp-env.ap-northeast-1.elasticbeanstalk.com**
* Click **Check availability**
* Click **Next** twice
* Instance type: **t1.micro**
* Select your existing **EC2 key** pair
* Click **Next**
* Create a **tag**
* Click **Next** twice
* Click **Launch**
* Once the setup is complete, go to your **Environment URL**
* Go to your **Amazon Elasticsearch Service Kibana URL**
* Click **Settings**
* Click **Indices**
* Tick **Index contains time-based events**
* Index name or pattern: **logstash-***
* Time-field name: **@timestamp**
* Click **Create**
* Go to **Discover**
* Customize your **Selected Fields**
* You’re done! 🙂
