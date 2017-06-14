---
title: Build Your First Chatbot with Amazon Lex
author: JP
date_created: 06-14-2017
format: markdown
---

# What is Amazon Lex

Amazon Lex, released last April 19, 2017, is one of the secure managed services of AWS under Artificial Intelligence category that helps you build conversational interfaces into any application using voice and text.

With Amazon Lex, you can build chatbots that respond to messages and events to a Slack channel or SMS messages sent to Twilio SMS number or you can integrate your bots to Facebook Messenger.

The good thing about this is machine language expertise is not necessary to use this technology. You can specify the conversational flow and Amazon Lex will take care of speech recognition and natural language understanding functionality. And yes, Lex get more intelligent over time!

Cool, right? Let's go build our first text-based chatbot!

# Prerequisites

So, what do we need to build our first chatbot?

* Laptop/Desktop
* Terminal
* Your favorite code editor (I highly recommend [Visual Studio Code](https://code.visualstudio.com/)!)
* [AWS Account](https://aws.amazon.com/free)
* Make sure to configure your AWS account using [AWS CLI](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
* [Node.js v6.11.0](https://nodejs.org/en/)
* [Serverless Framework v1.15.3](https://serverless.com/)

# Amazon Lex Setup

## Bot

Let's begin!

1. Log on to your **AWS Management Console**
1. Choose a **Region**
1. Under **Artificial Intelligence**, click **Lex**
1. If you don't have existing bots, click **Getting Started**. Otherwise, click **Create**
1. Select **Custom bot**
1. Bot name: **name of your bot**
1. Output voice: **None. This is only a test based application.**
1. Session Timeout: **1 min**
1. IAM role: **AWSServiceRoleForLexBots**
1. Child-Directed? (Mandatory): **No**
1. Click **Create**

## Intents

To build a bot, you need to create a set of actions a.k.a **Intents** that you want your bot to fulfill. You can have multiple intents in a single bot. For example, **ProductInquiry**, **BazaarScheduleInquiry**, and **ThanksGoodbye**.

1. Click **Create Intent**
1. Click **Create new intent**
1. Name your new Intent (e.g., **ProductInquiry**)
1. Click **Add**
1. Repeat the same steps for **BazaarScheduleInquiry** and **ThanksGoodbye**
1. Don't forget to click **Save Intent**

## Utterances

**Utterances** are the spoken or typed phrases that invoke your intent. For example, "Hi" and "I would like to know the prices of your products".

1. Under **Sample utterances**, add the following for **ProductInquiry** intent:  
    - Hi  
    - Hello  
    - I would like to know the prices of your {product}
1. Do the same for **BazaarScheduleInquiry** but use the utterances below instead:
    - Can you give me the schedule
    - I would like to know the bazaar schedule
1. And for **ThanksGoodbye** intent, add the following:
    - Thanks
    - Goodbye
    - Thank you
1. Don't forget to click **Save Intent**

## Lambda initialization and validation

We can use AWS Lambda to validate the user input using the initialization and validation codeHook. This code gets executed at every turn of the conversation. This codehook can be used to set up session parameters, validate user input and customize responses.

This is the part where we write our code.

1. Fire up your terminal
1. `mkdir aws-lex-my-first-chatbot`
1. `cd aws-lex-my-first-chatbot`
1. `npm init`
1. Press **Enter** until **Is this ok?**, or provide a value
1. Type **yes**
1. `vim serverless.yml` then copy the code below then paste it to the new file (or do `sls create -t aws-nodejs` but still use the configuration below)

  <script src="https://gist.github.com/jpdoria/e9c20da835829660e34a611cce247107.js"></script>

9. `npm install serverless-plugin-optimize --save-dev`
1. `vim index.js` then copy the code below then paste it to the new file

    <script src="https://gist.github.com/jpdoria/2e66636954811c8f9365636a31d141c8.js"></script>

12. `vim lexDispatch.js` then copy the code below then paste it to the new file

    <script src="https://gist.github.com/jpdoria/d183bfd2cc481f1600ab2dc3af7cf016.js"></script>

13. `vim productInquiry.js` then copy the code below then paste it to the new file

    <script src="https://gist.github.com/jpdoria/7132e92e62deacc35c8017c334125eb7.js"></script>

14. `vim bazaarScheduleInquiry.js` then copy the code below then paste it to the new file

    <script src="https://gist.github.com/jpdoria/bfc26252f194dfa4db4806c39a03ff95.js"></script>

15. `vim goodbye.js` then copy the code below then paste it to the new file

    <script src="https://gist.github.com/jpdoria/b47c90c41826a73a4fe27f4e4196d1ed.js"></script>

16. `vim lexResponses.js` then copy the code below then paste it to the new file

    <script src="https://gist.github.com/jpdoria/a62c85653dfe77b2ac6b58e5a5d0a0ad.js"></script>

17. `sls deploy -v` to deploy the code to AWS Lambda
1. After the deployment, you'll see the complete name of the function and that is `aws-lex-my-first-chatbot-dev-validation`

Tip: to tail the invocation from CloudWatch Logs, do `sls logs -f validation -t`

## Slots

The input data required to fulfill the intent are called **Slots**. For example, "Hey there! Which of our products do you want to check: cookies, ready-to-serve gourmet sauces, or savories?"

### ProductInquiry Intent

1. While in **Editor** tab of your Bot, find the **Slot types** on the left pane
1. Click **+** icon
1. Slot type name: **product**
1. Description: **List of products**
1. Value:
    - Cookies
    - Sauces
    - Savories
6. Click **Add slot to intent**
1. Change **slotOne** to **product**
1. Click the **cog icon** beside **e.g. What city?** to update the prompt
1. Change **e.g. What city?** to **Hey there! Which of our products do you want to check: cookies, ready-to-serve gourmet sauces, or savories?**
1. Click **Save**
1. Don't forget to click **Save Intent**

Again, we only use slots if require the user to provide us the information he needs (e.g., available color of car, types of products, etc.). We don't need to set up slots for **BazaarScheduleInquiry** and **ThanksGoodbye**.

## Build

1. Once you have properly configured the bot, go ahead and build it by clicking **Build**
1. Lex will inform you that "You can start testing the Bot once the build completes successfully.", then click **Build**

## Test Bot

Open the **Test Bot** chatbox then test your bot.

## Publish

If you're happy with the result, you can now publish your bot to Facebook Messenger, Slack, or Twilio! 😊

# Pricing

## Text
Price per 1,000 requests: $0.75  
Free Tier* (requests per month): 10,000

## Speech
Price per 1,000 requests: $4.00  
Free Tier* (requests per month): 5,000

*Available for the first year upon sign-up to new Amazon Lex customers

# Learn More

To learn more about this awesome service of AWS, check the links below:

- [https://aws.amazon.com/lex/faqs/](https://aws.amazon.com/lex/faqs/)
- [http://docs.aws.amazon.com/lex/latest/dg/what-is.html](http://docs.aws.amazon.com/lex/latest/dg/what-is.html)
- [http://docs.aws.amazon.com/lex/latest/dg/lambda-input-response-format.html](http://docs.aws.amazon.com/lex/latest/dg/lambda-input-response-format.html)
