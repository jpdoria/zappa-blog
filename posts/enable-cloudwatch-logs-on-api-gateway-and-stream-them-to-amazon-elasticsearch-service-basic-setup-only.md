---
title: Enable CloudWatch Logs on API Gateway and stream them to Amazon Elasticsearch Service (Basic setup only)
author: JP
date_created: 06-21-2016
format: markdown
---

* Go to **IAM** > **Create New Role**
* Set Role Name: **cloudwatch_api**
* Select **Role Type**: **Amazon API Gateway** > **AmazonAPIGatewayPushToCloudWatchLogs**
* **Create Role**
* Select the new **cloudwatch_api** role
* Go to **Trust Relationships** > **Edit Trust Relationship**
* Use this policy:  

    <script src="https://gist.github.com/jpdoria/8b733447bb62d6a0dc0762d542bf39c6.js"></script>

* **Update Trust Policy**
* Copy the Role ARN: **arn:aws:iam::123456789012:role/cloudwatch_api**
* Go to **Amazon API Gateway** > **Settings**
* Paste the **Role ARN** in CloudWatch log role ARN box
* Click **Save**
* You must have an API deployed already (I used the PetStore API and deployed it to “dev” stage)
* Go to **APIs** > **Your API** > **Stages** > **Select a Stage** > **Stage Editor** > **Settings**
* Tick **Enable CloudWatch Logs**
* Log Level: **INFO**
* Tick **Log full requests/responses data**
* Click **Save Changes**
* To confirm if logging is enabled, you should see **/aws/apigateway/welcome** and **API-Gateway-Execution-Logs_12r3bn45r6/dev** when you go to **CloudWatch** > **Logs**
* Go to **Amazon Elasticsearch Service**
* Click **Get Started**
* Elasticsearch domain name: **cloudwatch-api-es**
* Click **Next**
* Instance count: **1**
* Instance type: **t2.micro.elasticsearch**
* Storage Type: **EBS**
* EBS volume type: **General Purpose (SSD)**
* EBS volume size: **10**
* Click **Next**
* Set the domain access policy to: **Allow open access to the domain**
* Click **Next**
* Click **Confirm and create**
* Setup takes about 10 minutes to complete
* Go back to **CloudWatch** > **Logs**
* Select **API-Gateway-Execution-Logs_12r3bn45r6/dev** > **Actions** > **Stream to Amazon Elasticsearch Service**
* Amazon ES cluster: **cloudwatch-api-es**
* Launch IAM Execution Role: **Create a new IAM role**
* Allow the new role **lambda_elasticsearch_execution**
* Click **Next**
* Log Format: **JSON**
* Click **Next** twice
* Click **Start Streaming**
* Now go back to **Amazon Elasticsearch Service** > **Dashboard** > **cloudwatch-api-es**
* Go to the Kibana URL: **search-cloudwatch-api-es-xxxxxxxxxxxxxxxxxxxxxxxxxx.ap-northeast-1.es.amazonaws.com/_plugin/kibana/**
* Kibana will load the codes
* Tick **Index contains time-based events**
* Tick **Use event times to create index names**
* Index pattern interval: **Daily**
* Index name or pattern: **[cwl]-YYYY.MM.DD**
* Time-field name: **@timestamp**
* Click **Create**
* Go to **Discover**
* Add **@log_stream** and **@message** to Selected Fields
* You’re done! 🙂
