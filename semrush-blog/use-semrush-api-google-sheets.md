---
title: "How To Use the Semrush API in Google Sheets"
source: semrush-blog
content_type: "product_or_tool"
freshness_risk: "high"
slug: "use-semrush-api-google-sheets"
url: "https://www.semrush.com/blog/use-semrush-api-google-sheets/"
canonical: "https://www.semrush.com/blog/use-semrush-api-google-sheets/"
author: "Brian Jensen"
published: "2015-03-12T13:00:03+00:00"
updated: "2015-03-12T13:00:03+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "date_2015_very_old"
  - "product_or_tool_content"
schema_genre: "General SEO"
fetched_at: "2026-06-12T20:23:05+00:00"
status_code: 200
html_hash: "ab59cf44442934fb6c3d9d683d2bd1e050309b4af813a60d9505777010329022"
clean_word_count: 964
clean_char_count: 5737
---
# How To Use the Semrush API in Google Sheets

Semrush is my favorite competitive research tool that I use for everything from organic and paid keyword research to understanding market share in a specific region. A few months ago, I was working on a large project where it made sense to look beyond the Semrush interface and pull data directly from their servers via the Semrush API. The problem was that I’d never used an API before and wasn’t able to locate any resources for a noob like myself to get started.

As luck would have it, I work with some [pretty smart people](https://twitter.com/ethanlyon) who were able to point me in the right direction. Now that I understand the basics, I want to pay it forward and create a resource for others who use Semrush, but not familiar with using the API.

**What is an API?**

Let’s start at the top. An [application programming interface](http://en.wikipedia.org/wiki/Application_programming_interface) as defined by Wikipedia is “a set of routines, protocols, and tools for building software applications.” APIs allow different applications to communicate with databases and many of the social tools digital marketers use on a daily basis are built using APIs. The Semrush API allows users to pull data directly from their servers. It can make large scale analysis a breeze.

**Locating Your Semrush API Key**

Before we get started with examples, you’ll need to locate your API key and number of remaining credits which can be found by navigation to the [API documentation page](https://developer.semrush.com/api/).

![Find your SEMrush API key](https://static.semrush.com/blog/uploads/media/31/5f/315fe3ddfda0d323c1c1acf7e7f4acfd/api1.png)

**Using the Semrush API in Google Sheets**

I use Google Sheets frequently to create and collaboratively edit spreadsheets with other users. To provide you with an example of how to use the application and Semrush’s database via the API, let’s pretend I’m working on a keyword research project with a co-worker in which we’ll need search volume CPC, competition and total number of Google results for a list of keywords.

Semrush offers a wide variety of reports that include paid, organic, overview, domain, URL reports and more. We’ll be using the Keyword Overview report that will allow us to pull data for all the metrics I’ll need for my keyword research project. Let’s dissect the request example for this report to provide us with a better understanding of the data we’ll be pulling into our Google spreadsheet.

![Parts of the report request example](https://static.semrush.com/blog/uploads/media/71/33/71336a82a9b8583aa9cccc2e96f1f6ec/api2.png)

1. The specific type of report you’d like to request
2. Your API key number
3. The report’s columns
4. The phrase we are researching
5. The database that we’ll be pulling in data from

Now that we have our API key, the report we’d like to run and a new spreadsheet we’ve created in Google Sheets, it’s time to review a few spreadsheet functions that will make it possible to retrieve and organize the data.

**Meet IMPORTDATA**

Just like in Excel, Google Spreadsheets [supports a wide array of functions](https://support.google.com/docs/table/25273?hl=en). For this tutorial, we’ll be using IMPORTDATA to retrieve data from Semrush.

![Meet IMPORTDATA](https://static.semrush.com/blog/uploads/media/71/f0/71f015816add0bcc2f0093f3a75f1621/api4.png)

The syntax for the function is IMPORTDATA(url), and the value for url must be enclosed in quotes or reference a cell. The Keyword Overview report request example using IMPORTDATA would look similar to the following:

=IMPORTDATA("https://api.semrush.com/?type=phrase\_this&key=00000000000000000000& &export\_columns=Ph,Nq,Cp,Co,Nr&phrase=keyword&database=us")

Because we’re efficient and we’d like to be able to drag through multiple rows in our spreadsheet, we can replace “keyword” with the cell we’d like to reference in the request i.e. “&A1&”.

![Replace the keyword with the cell you'd like to reference](https://static.semrush.com/blog/uploads/media/02/e8/02e822a05a3c77ca2a6bf210d65d5967/api5.png)

**Using the TRANSPOSE Function**

By default, Semrush will populate your data vertically down rows. Using a [nested function](http://spreadsheets.about.com/od/excel2010functions/qt/091223-nesting-functions-excel.htm) with the transpose feature will populate your data horizontally across columns. Creating a nested function using TRANSPOSE and IMPORTDATA would look similar to the following request:

=transpose(importdata("https://api.semrush.com/?type=phrase\_this&key=00000000000000000000& &export\_columns=Ph,Nq,Cp,Co,Nr&phrase=keyword&database=us"))

**Using the SPLIT Function**

Another Google Sheets function that you may find useful for working with your data is Split. An easy way to think about this function is that Split to Google Sheets is basically what Text to Columns is to Excel. The definition provided in Google Sheets is that this function “will help you divide text around a specified character or string and places each fragment into a separate cell in the row.”

![The split function](https://static.semrush.com/blog/uploads/media/88/35/8835f4fab4ff529264c25115ecc8c16a/api6.png)

Similar to Excel, there are many ways to accomplish the same task in Google Sheets and a plethora of different ways to organize and format your data in a way that works best for you.

Try a few different reports on your own and experiment with adding or removing export columns to get the data you need for your project.

That’s it, easy right? With the help of the IMPORTDATA function, using the API in Google Sheets can be a major time saver. Please leave any insight or tips you’d like to contribute in the comments below!
