---
title: Going Serverless!
author: JP
date_created: 04-26-2017
format: markdown
---

So my blog is now back online and it's now *serverless* - hosted using [Amazon API Gateway](https://aws.amazon.com/api-gateway/) and [AWS Lambda](https://aws.amazon.com/lambda/).

One of the reasons why I changed my setup is the cost. I used to run my WordPress blog on an EC2 instance that was running 24/7. My blog has a low traffic so the instance was not overutilized and I think I was paying around $9 per month. Imagine that!

I had to refresh my Python and learned Flask though and Zappa too which is pretty easy and it was worth it!

# What is Serverless Computing?

From [AWS](https://aws.amazon.com/serverless/):

> Serverless computing allows you to build and run applications and services without thinking about servers. With serverless computing, your application still runs on servers, but all the server management is done by AWS. At the core of serverless computing is AWS Lambda, which lets you run your code without provisioning or managing servers. With Lambda, you can run code for virtually any type of application or backend service, and it takes care of everything required to run and scale your code with high availability.

## Pricing (us-east-1)

### Old Setup

#### Amazon EC2

* t2.micro - $0.012 per hour
* Instance was running 24/7
* Around $9 per month

### New Setup

#### AWS Certificate Manager

SSL/TLS certificates provisioned through AWS Certificate Manager are free. You pay only for the AWS resources you create to run your application.

#### Amazon API Gateway

* API Calls - $3.50 per million API calls received, plus the cost of data transfer out, in gigabytes
* Data Transfer - $0.09/GB for the first 10 TB

#### AWS Lambda

* First 1 million requests per month are free
* $0.20 per 1 million requests thereafter ($0.0000002 per request)
* Duration is calculated from the time your code begins executing until it returns or otherwise terminates, rounded up to the nearest 100ms. The price depends on the amount of memory you allocate to your function. You are charged $0.00001667 for every GB-second used.
* Free Tier
    * 1,000,000 free requests per month
    * Up to 3.2 million seconds of compute time per month

Again, my blog has a very low traffic so it is impossible to reach a million API calls or requests in a month. It's way cheaper than hosting on Amazon EC2, Amazon Lightsail, DigitalOcean or Heroku - and in most cases, it's completely *free*.

# Diagram

Here's the high level diagram:

![alt text](https://cdn.lazyadm.in/aws-sa.png "Serverless Architecture")
