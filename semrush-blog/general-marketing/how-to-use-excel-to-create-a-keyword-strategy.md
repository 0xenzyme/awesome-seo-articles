---
title: "How To Use Excel To Create a Keyword Strategy"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "how-to-use-excel-to-create-a-keyword-strategy"
url: "https://www.semrush.com/blog/how-to-use-excel-to-create-a-keyword-strategy/"
canonical: "https://www.semrush.com/blog/how-to-use-excel-to-create-a-keyword-strategy/"
author: "Sergio Aicardi"
published: "2014-06-19T14:30:39+00:00"
updated: "2014-06-19T14:30:39+00:00"
categories:
  - "General Marketing"
freshness_reasons:
  - "date_2014_very_old"
schema_genre: "General Marketing"
fetched_at: "2026-06-12T16:49:49+00:00"
status_code: 200
html_hash: "16a3524f14fe05f010909f8706d467abcc229b64e1892a320301b20fddeee639"
clean_word_count: 1257
clean_char_count: 7375
---
# How To Use Excel To Create a Keyword Strategy

Everyone knows keywords are a big part of SEO, but I feel most people don’t really appreciate the work that goes behind setting up a strategy that is based on keyword performance.

Maybe it’s because most people don’t understand what measures are taken to create large SEM campaigns with thousands of keywords that need to be strategically selected. When dealing with large pay per click campaigns in AdWords, using the right keywords means everything.

Since there are great tools out there like Semrush and Google Analytics, we can get great keyword data from our competitors or our websites that we manage easily. But managing that data can be tricky at times (especially with ecommerce data). As a member of a PPC management company, it’s important that I am efficient and strategic when selecting keywords for our clients.

I wanted to share some of the ways I use Excel to create a keyword strategy very quickly using simple concatenation in a not-so-simple way.

## Introduction to simple concatenation

[Concatenation](http://office.microsoft.com/en-us/excel-help/concatenate-function-HP010062562.aspx) is a computer programming term which means “to join two charter strings end-to-end.” In Excel, concatenation is a function used to join strings from different cells together. To show you an example, the cells from column A, B and C are joined together using simple concatenation.

![concatenation-ABC](https://static.semrush.com/blog/uploads/media/f5/9c/f59c405547b45476d419fc5b69b18776/concatenation-abc-e1403113331895.png)

*Notice that spaces were also included in the concatenation formula, which needs to be done if you want there to be spaces between your character strings.*

It’s worthy to note that you only need to fill in the formula in cell D2 and then click and drag the formula down to the last row with data instead of manually entering the formula for each cell in column D. Excel will automatically change the numbers in each cell for you, so the formula is adjusted for each row to show the data in the correct order as it was showed in the first cell.

## Using concatenation to build bulk keyword lists for highly targeted ad groups

Over the years I’ve used Excel to streamline the setup of new AdWords campaigns. Being that a lot of our clients are local, service-based business owners, I decided to build a tool using simple concatenation to generate keywords I know convert well based on my research with Semrush, Google Analytics, Google AdWords and other tools that show actionable data pertaining to keywords.

When I started working with this tool, it started as a simple spreadsheet much like the one above, actually. Now the workbook contains several sheets that are all starting to communicate with each other.

Over time, the tool evolves because I am finding new ways to add to it. The tool is a great asset. We recently created a campaign with a conversion rate that is over 35% consistently since launch. We also have an average quality score that is over 9/10 because of the fact that we created such laser-targeted ad groups that were both location-specific and service-specific (a case study of the campaign can be viewed [here](http://themiamiseocompany.com/case-studies/ppc-case-studies/)). Below is a snapshot of the tool which I will describe further in the next few paragraphs.

To explain from left to right (top to bottom): What you are looking at is a tool that creates several keyword ideas very quickly by filling in just a few cells. First, we specify the location details in column B followed by the type of service, service variations and buying variations.

**Service variations** are basically different types of services that are grouped into a category of service. For example, this client is a pest control company owner. One of his services is termite control. A variation of that would be “eco-friendly termite control” or “24 hour termite control.”

With **buying variations**, we are simply applying tags to the keywords we feel would imply the searcher is ready to make a purchase or one that needs service immediately and isn’t just doing research or shopping around. A buying variation for a termite control ad group might be “local termite control” or “affordable termite control.”

Using concatenation you can create tons of keyword variations, and that’s exactly what I have done with the PPC campaign for this client who is now doing great. The ad groups are made up of keywords that are all extremely relevant to one another and lead visitors to landing pages that were optimized for the same list of keywords. The content is well-tailored to the keywords I generated with this tool, and so was the ad copy.

All of these factors contributed toward the keywords having a very high quality score within AdWords, and allowed the client to get the top ranking position while spending less. Let’s take a look at the formula that was used to generate the keyword in cell E30.

## Optimizing your Excel tools

Let’s take a look at some of the other pages that are automatically filled using simple concatenation when you fill out the location cells, service variations and buying variations. Keep in mind that the sheet already created all of the keywords in column E and Y from the first sheet in the previous snapshot, which saves time in itself using a few simple concatenation commands. What’s great about concatenation is that you can pull data from other sheets in your workbook, which we will show in the next few screenshots.

I have a separate labeled sheet called “Long Tail Variations.” This provides long tail variations and the URL extension that is recommended for a high chance at ranking organically or to simply have an intelligent URL structure, as shown in the screenshot below. It also creates a copy of the keywords with the first letter capitalized using the Proper function, which can be handy if you want to use those keywords as paragraph headers or titles for your landing pages. Additionally, I added another column that ads a broad match modifier to each keyword.

The entire workbook has sheets like these to allow me to quickly and easily access keywords that are closely themed to each other for ad group creation and more. Recently, I used concatenation to set up ad copies automatically, which I’ve added to this workbook!

## Limitless possibilities with SEM data in Excel

Most people have no idea that Excel is capable of doing some pretty amazing things. I’ve been working with our programmer recently to plan the development of our project management solution. This will communicate with several tools like Semrush via API directly in Excel. Simple changes on a bulk level can save you invaluable time, and give you that edge as a member of any company that relies on Excel as a tool in the workspace.

When I find myself doing something I’ve done before, I usually think to myself, “Can I use Excel to automate this?” The answer is usually, *yes*; it just takes time to figure out the right functions or formulas to do it.

The one takeaway I have from conversing with Excel gurus is that you can never learn enough. I enjoy sharing my experiences and tips, and I hope this blog post encourages you to try and create your own tools in Excel! Until next time, please feel free to leave questions or comments below!
