---
title: "SEO Forecasting: The Art Of Getting Buy-In"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "seo-forecasting"
url: "https://ahrefs.com/blog/seo-forecasting/"
canonical: "https://ahrefs.com/blog/seo-forecasting/"
author: "Patrick Stox"
published: "2020-08-27T16:00:52+00:00"
updated: "2025-01-17T21:28:55+00:00"
categories:
  - "Enterprise SEO"
freshness_reasons: []
fetched_at: "2026-06-12T12:05:12+00:00"
status_code: 200
html_hash: "6c0db9e7d9572fca7b58aec644ecd9074385611921e32bcf7f51f0e8e1a27c96"
clean_word_count: 3883
clean_char_count: 23770
---
# SEO Forecasting: The Art Of Getting Buy-In

SEO forecasting is a process that uses historical data to predict a company’s future search engine optimization (SEO) results. When forecasting, you may use 1st party or 3rd party historical data such as traffic, traffic value, click-through rate (CTR), and search volume.

Most Ahrefs users will be familiar with our traffic graphs. They show the estimated search traffic for any website or page over time. Here’s the graph for [ahrefs.com](https://ahrefs.com):

Having historical data like this is useful for analyzing the past performance of a website or web page, but what about future performance? If you want to estimate the future organic traffic growth or decline, that’s where SEO forecasting can help. Take a look at this graph.

That blue line is the future traffic prediction for Ahrefs. The blue shaded area is the upper and lower uncertainty level. Put simply, there’s an 80% probability of our forecasted organic traffic being within that range.

Even better, this graph took all of two minutes to make using Ahrefs data and open-source scripts I made.

In this guide, I’ll show you how to create graphs like these to predict future performance for your website, pages, and even graphs of you vs competitors so you can [get more buy-in for SEO projects](https://ahrefs.com/blog/seo-buy-in/).

- [Why SEO forecasting is important](#why-forecasting-is-important)
- [Keyword-level forecasts](#keyword-level-forecasts)
- [First-party vs third-party data](#third-party-data)
- [SEO forecasting with third-party data: use cases](#forecasting-seo)
- [Adjusting script settings & details](#adjusting-scripts)
- [Advanced SEO forecasting](#advanced-seo-forecasting)

## Why SEO forecasting is important

The reasons why you’d want to do this vary depending on your situation.

**If you work in** [**enterprise SEO**](https://ahrefs.com/blog/enterprise-seo/), you’ll usually have to make projections once or twice a year of how much you’ll grow SEO and increase revenue. The company will also set [goals](https://ahrefs.com/blog/seo-goals/) for you and your team. If there’s a discrepancy between your estimates and company goals, you can use that to argue for more resources.

Say you project an uplift of 15% year over year (YoY) at the current effort and resource levels, but your target is 25%. Your expected impact doesn’t align with expectations. In this case, you can push for a lower target or more resources to meet the company’s goal.

Maybe you need additional budget for content to reach the goal, or funding for link building or internal linking. You can use an SEO forecast to argue for resources for projects that matter to you.

**If you’re at an agency**, SEO forecasting can help with sales or predict the future impact for a client. Most companies want to know when they will be a market leader or beat a particular competitor.

Suppose a forecast shows they lag behind their target at current effort levels. In that situation, it’s easy for a salesperson to justify an increased budget for projects, a shift in strategy, or additional hours that will allow them to close the gap or overtake competitors.

 Adding an SEO forecast to a sales pitch can help elevate your pitch above those of other agencies and justify your requested budget.

## **Keyword-level forecasts**

A typical formula for keyword level forecasts is:

Search volume x average click-through rate (CTR)

Unfortunately, that only accounts for the keywords you have entered and is usually focused on one keyword per page, when pages rank and get traffic from many terms.

 You also run into the issue of using generic CTR curve models which may not be representative of your site. We actually create a custom CTR curve using your Google Search Console (GSC) data in the GSC Overview report in [Rank Tracker](https://ahrefs.com/rank-tracker).

There are already a lot of pre-existing spreadsheets that help you make keyword forecasts from folks such as:

- [Tom Capper](https://www.brainlabsdigital.com/blog/seo-forecasting/)
- [Kevin Indig](https://www.kevin-indig.com/a-google-sheets-template-for-seo-traffic-forecasting/)
- [Adam Tanguay](https://searchengineland.com/seo-forecasting-template-389686)

If you want next-level forecasts, you could even forecast the future volume the keywords. We’ve provided this data for many of the keywords in Keywords Explorer.

An easier way than going through this exercise would be to just use the Traffic Potential metric that we have in tools like [Keywords Explorer](https://ahrefs.com/keywords-explorer). It takes into account all the keywords that you might rank for, not just one.

Traffic Potential shows the sum of organic traffic that the #1 ranking page for your target keyword receives from all the keywords that it ranks for. In other words, if you build a better page than the one that already exists, you are likely to get as much traffic or more than the current best page.

## First-party vs third-party data?

Most SEO forecasts use first-party data sources like [Google Analytics](https://ahrefs.com/blog/google-analytics-for-seo/) or [Google Search Console](https://ahrefs.com/blog/google-search-console/). If you want an accurate estimate for your website or page, this is absolutely the best data to use. If you need more granularity in your data or to predict seasonality, use one of these sources. Here’s a [tutorial from JR Oakes](https://locomotive.agency/technical-seo/website-traffic-prediction-with-google-colaboratory-and-facebook-prophet/) that will help.

The problem is that SEO isn’t a single-player game. What you need to know is how your site or page is likely to perform relative to the competition. If your competitors are likely to outpace your SEO performance, that will influence your strategy and where you devote resources. And the only way to get data on your competitors is to use third-party sources like Ahrefs.

You may wonder if you can reliably use third-party data for SEO forecasting. At Ahrefs, the way we calculate our average volume data does not see daily granularity or seasonality, but it is useful for finding patterns and forecasting trends. If you use monthly volume instead, this data does have the trend data included. We also re-calculate previous data and update our graphs to remove irregularities that would otherwise be caused by updates to our data or calculations.

## SEO forecasting with third-party data: use cases

Graphs like the one I showed at the beginning of the article usually require some knowledge of coding and modeling libraries. That’s why many companies and agencies don’t do SEO forecasting. They don’t have the necessary resources like a data analyst or data scientist on their payroll.

With this in mind, I spent some time creating a bunch of plug-and-play scripts that you can run for free in [Google Colab](https://colab.research.google.com/). Just choose what you want to forecast below. I’ve included a link to the script and instructions on how to use it under each section.

I’ve used model called Prophet for these, but there are many other forecasting models like SARIMA that could be used as well.

- [Predicting future traffic](#predicting-future-traffic)
- [Predicting future traffic value](#predicting-future-traffic-value)
- [Predicting future competitor traffic](#predicting-future-competitor-traffic)
- [Predicting future competitor traffic value](#predicting-future-competitor-traffic-value)
- [Predicting future competitor page traffic](#predicting-future-competitor-page-traffic)
- [Making performance predictions during a core update](#core-update-performance-predictions)

Sidenote.

You can still download the data from the Legacy Overview report for these. If you use the new Overview report, you will need to adjust the export to match the format below which has 1 column for the date and another for the organic traffic.

### Predicting future traffic

This script will forecast your future traffic one year from now. When I run this one for ahrefs.com, the trend (dark blue line) shows that one year from now, we will likely be up to 1.3 million monthly organic visits from our current level of 880,000.

Here’s how to predict organic traffic for your site:

#### 1. Download your data in Ahrefs

- Navigate to [Site Explorer](https://ahrefs.com/site-explorer) and enter the domain you want data for
- In Overview, go to the “Organic search” tab
- Find the “Organic traffic” chart and select the period you want (it defaults to “All time”)
- Click Export > CSV and save the file

#### 2. Make a copy of the notebook and open it

- Open the [Traffic Forecast Notebook](https://colab.research.google.com/drive/1oJ2gD5w3EyTc12O39GzKiNL8wAiNGsSz?usp=sharing)
- Click File > “Save a copy in Drive”
- It should open a new window with the notebook, but if not, then go to your Google Drive, find the file, and open it.

#### 3. Run the notebook and upload your file

- Click Runtime > “Run all”
- Upload your file by clicking “Choose Files,” selecting your downloaded file, and clicking Open.

### Predicting future traffic value

If you’re not familiar with Traffic Value, it’s what it would cost to buy your current level of organic traffic from Google Ads. Another way to think of it is how much money the target website or URL has saved by ranking for keywords organically instead of buying paid traffic.

This script will forecast your future traffic value one year from now. When I run this for ahrefs.com, the trend shows that one year from now, we will likely be at a Traffic value of $2.9 million, up from our current level of $1.9 million.

Here’s how to predict organic Traffic Value for your site:

#### 1. Download your data in Ahrefs

- Navigate to [Site Explorer](https://ahrefs.com/site-explorer) and enter the domain you want data for
- In Overview, go to the “Organic search” tab
- Find the “Traffic value” chart and select the period you want (it defaults to “All time”)
- Click Export > CSV and save the file

#### 2. Make a copy of the notebook and open it

- Open the [Traffic Value Forecasting Notebook](https://colab.research.google.com/drive/1_3VT4cTkoz8Yp3XSMTbUYr-7EWs0deC9?usp=sharing)
- Click File > “Save a copy in Drive”
- It should open a new window with the notebook, but if not, then go to your Google Drive, find the file, and open it.

#### 3. Run the notebook and upload your file

- Click Runtime > “Run all”
- Upload your file by clicking “Choose Files0,”, selecting your downloaded file, and clicking Open.

### Predicting future competitor traffic

This script will forecast not only your growth but also the growth of your competitors. Notice that in the next year, Ahrefs is projected to overtake Moz at current effort levels. If you’re not at the level you want to be or the position you want to be in versus competitors, then a change is required. Maybe that change is a new strategy, new projects, or additional resources to get more done and have more impact. This can help you justify further investment in SEO by estimating your position vs. competitors in the future.

Here’s how to predict traffic performance for your site vs. competitors:

#### 1. Download your data in Ahrefs

- Navigate to [Site Explorer](https://ahrefs.com/site-explorer) and enter the domain you want data for
- In Overview, go to the “Organic search” tab
- Find the “Organic traffic” chart and select  the period you want which defaults to “All time”
- Click Export > CSV and save the file
- Repeat for each website that you want to compare

#### 2. Make a copy of the notebook and open it

- Choose the number of competitors you want to compare.
- Open the correct Traffic Forecast Notebook below:
  - [5 Site Traffic Forecast Notebook](https://colab.research.google.com/drive/16MjFZUlqg95WJxRpeTdEUZHaTX5hBOb7?usp=sharing)
  - [4 Site Traffic Forecast Notebook](https://colab.research.google.com/drive/1rvAGScvmjbhibCQw1f0PJFT282yyMD1O?usp=sharing)
  - [3 Site Traffic Forecast Notebook](https://colab.research.google.com/drive/1Rx5HHGl4W5FBToGaZNeMO1PSMATPuBwE?usp=sharing)
  - [2 Site Traffic Forecast Notebook](https://colab.research.google.com/drive/1AbQurrsJeRuv_n6R-r3jeJG8qswNZUBh?usp=sharing)
- Click File > “Save a copy in Drive”
- It should open a new window with the notebook, but if not, then go to your Google Drive, find the file, and open it.

#### 3. Run the notebook and upload your file

- Click Runtime > “Run all”
- This time there are multiple upload boxes. For each competitor, upload your file by clicking “Choose Files,” selecting your downloaded file, and clicking Open.

### Predicting future competitor traffic value

This script will forecast your growth in Traffic Value and the growth in Traffic Value for your competitors. Notice that we expect no significant changes in the order of competitors in the next year at current effort levels. If someone wanted to break out and make a change, they would likely need a change in strategy or increase resources to have an impact. An estimate like this can help justify the need for change or funding. For instance, if I were lower on this chart and stagnating while competitors seem to be pulling ahead, I’d be making a case for more resources while also looking into what competitors are doing that I am not.

Here’s how to predict traffic value performance for your site vs. competitors:

#### 1. Download your data in Ahrefs

- Navigate to [Site Explorer](https://ahrefs.com/site-explorer) and enter the domain you want data for
- In Overview, go to the “Organic search” tab
- Find the “Traffic value” chart and select the period you want (it defaults to “All time”.)
- Click Export > CSV and save the file
- Repeat for each website that you want to compare

#### 2. Make a copy of the notebook and open it

- Choose the number of competitors you want to compare.
- Open the correct Traffic Value Forecast Notebook below:
  - [5 Site Traffic Value Forecasting Notebook](https://colab.research.google.com/drive/1lHMtQufL6uTsiy-fkIfc5WW9l2lqiO9i?usp=sharing)
  - [4 Site Traffic Value Forecasting Notebook](https://colab.research.google.com/drive/1RoOiz14evoAJPxbSIiWIUmhHcfFGalqk?usp=sharing)
  - [3 Site Traffic Value Forecasting Notebook](https://colab.research.google.com/drive/1E2bb_jz69u3UpQxa_na0yAajGVzB31Z1?usp=sharing)
  - [2 Site Traffic Value Forecasting Notebook](https://colab.research.google.com/drive/1KFnkYzQzvpTFw0Tj6pUAOFf9XcSK_Sxd?usp=sharing)
- Click File > “Save a copy in Drive”
- It should open a new window with the notebook, but if not, then go to your Google Drive, find the file, and open it.

#### 3. Run the notebook and upload your file

- Click Runtime > “Run all”
- This time there are multiple upload boxes. For each competitor, upload your file by clicking “Choose Files,” selecting your downloaded file, and clicking Open.

### Predicting future competitor page traffic

With this script, I’ve graphed the top pages’ traffic for searches about “Google search operators.” As Ahrefs, I’m reasonably confident that we don’t need to update this post anytime soon as we seem to have comprehensive coverage and a sizable lead in traffic vs. competitors. However, Spyfu appears to be coming on strong, and it looks like their page will surpass Moz and possibly Google in traffic in the next year. If I were Moz, this might be a sign I should do a re-write or add additional content to my page. The same for Google Guide, it looks like their traffic has stagnated compared to competitors, so it may be time for a [content refresh](https://ahrefs.com/blog/republishing-content/) if they care about this page. Do you see where I’m going with this?

SEO forecasting for pages can help you estimate your market position in the future. You can use this information to prioritize your content updates based on which pages are most at risk of falling behind competing pages.

Here’s how to predict traffic performance at the page level for your site vs. competitors:

#### 1. Download your data in Ahrefs

- Navigate to [Site Explorer](https://ahrefs.com/site-explorer) and enter the domain you want data for
- In Overview, go to the “Organic search” tab
- Find the “Organic traffic” chart and select the period you want (it defaults to “All time”)
- Click Export > CSV and save the file
- Repeat for each website that you want to compare

#### 2. Make a copy of the notebook and open it

- Choose the number of competitors you want to compare.
- Open the correct Traffic Forecast Notebook below:
  - [5 Page Traffic Forecast Notebook](https://colab.research.google.com/drive/1fmKejx0FdaCXpXGSwJIBx8u6JDSEM_pD?usp=sharing)
  - [4 Page Traffic Forecast Notebook](https://colab.research.google.com/drive/1sHSwYd-TswJB1zyvPERkE6Br0kr39bEA?usp=sharing)
  - [3 Page Traffic Forecast Notebook](https://colab.research.google.com/drive/1sFHEizbkNb2pt7drnHFGgsWGlRP05cnd?usp=sharing)
  - [2 Page Traffic Forecast Notebook](https://colab.research.google.com/drive/1-qJdDOSJk0q-8KJmJEpYI3S_NkXDotRf?usp=sharing)
- Click File > “Save a copy in Drive”
- It should open a new window with the notebook, but if not, then go to your Google Drive, find the file, and open it.

#### 3. Run the notebook and upload your file

- Click Runtime > “Run all”
- This time there are multiple upload boxes. For each competitor, upload your file by clicking “Choose Files,” selecting your downloaded file, and clicking Open.

### Making performance predictions during a core update

I think everyone wants to know how they will perform during an update, especially websites who’ve had issues in the past. I wanted to show how a traffic forecast can progress as new data is added.

For this, I’m going to use a website that historically has seen ups and downs during core updates, verywellhealth.com. Notice that many of their ups and downs occurred during core updates, including a decline in [the last major update](https://searchengineland.com/google-may-2020-core-update-is-done-rolling-out-334826) on May 4th.

For the animation below, I have a blue line for the actual data until July 30th. The red line has no data beyond the days displayed on the GIF. Even before the May 4th update, the model was predicting a decline. When I added the update on the 4th, it predicted an even steeper decline.

Each additional day of data changes the prediction slightly as it incorporates the new information. All of the models were expecting a steeper drop than what happened, but they also predicted a slight recovery. Each predicted model seems to reasonably accurately match the actual traffic by the end of July, nearly two months in the future.

For fun, below is the current SEO forecast for one year from now to see how it does. You’ll notice that based on the fitted trend, the model thinks the traffic at the time of writing should be a little higher than it is now (where the blue line ends), but the site is likely to see some significant declines in the future. It’s predicted that the website will lose roughly half it’s traffic in the next year alone. I guess we’ll see if that holds true.

## Adjusting script settings & details

By default I’ve made some assumptions in the scripts above including:

- Core updates until the time of writing (July 2020);
- A window of 14 days to measure the data after core updates;
- Predictions for 365 days.

Here are some things you may want to do differently that will impact your SEO forecast.

- [Add additional updates](#add-additional-updates)
- [Change the holiday period](#change-holiday-period)
- [Forecast longer or shorter periods](#forecast-longer-shorter-periods)
- [Change the period of your initial data](#change-initial-data-period)
- [Use only part of a website](#use-part-of-website)
- [Change the line colors](#change-line-colors)

### Add additional updates

While I have core updates in the table that start with the earliest Ahrefs data, you may want to add updates that have happened or add future updates to the scripts. You just need to add additional dates to the array in the section below. The format is YYYY-MM-DD.

### Change the holiday period

I set the period for holidays as 14 days to give time for Google updates to roll out and Ahrefs to update the database. While I think this is reasonable, your data may show faster or slower changes. Check after the updates how long it seems to take for your data to stabilize and adjust this time if you need to. You can find the holiday time period in the code as `upper_window` as shown below.

### Forecast longer or shorter periods

By default, I have the scripts set to predict 365 days into the future, or one year. You can easily change this if you need to make predictions for a different period like a few months, or even predict multiple years into the future. For each item where you’re making a prediction, there will be a section that includes `periods=##`. The number here is the number of days you want to predict, so update to get predictions for the period you want.

For instance, if I want to forecast for three years, I’d change `periods=365` to `periods=1095` and my forecast for future organic search traffic for ahrefs.com would be what is shown below.

### Change the period of your initial data

I generally use the full historical data to make predictions by downloading all the data from the organic search overview chart. If you want to use less data, you can either edit the downloaded .csv files or download data for a different period, such as one year.

You’ll notice that in the forecast below for ahrefs.com, the estimate in one year is higher. That’s because a lot of recent growth pulls the trend-line higher. Different periods will yield different forecasts.

### Use only part of a website

The script accepts any .csv file. You can use an entire website or filter to a particular section, such as the blog’s path. You can even filter and use traffic for specific pages.

### Change the line colors

If the colors on the graph don’t align with those of your brand, that’s easy to change.

First, find the line that corresponds with the website you want to change and update the color for it in the section shown below. Adjust the colors to represent the different websites or brands.

Next, re-run this cell. Click the play button, and the graph will update.

## **Advanced SEO forecasting**

Forecasts can be as simple or as complex as you want them to be. They’re educated guesses based on data. In my experience more complex forecasts take more time and effort to put together and aren’t necessarily better. Most of the time, the ROI of building complex forecasts is not there.

The SEO forecasts I showed take a simplistic view of the data. A lot can change on your website and your competitors’ websites, such as deleting or creating new pages that target new keywords. More advanced predictions may take into account things like changes in search volume, [SERP features](https://ahrefs.com/blog/serps/#serp-features), keywords you know you will target, CTR, etc.

We’re also taking into account both branded and non-branded traffic in the forecasts when you might want to look at that data separately. You may even need to combine this data with conversions, average order value, or come up with return on investment (ROI) numbers.

## **Final thoughts**

Forecasts are always going to have some amount of uncertainty because changes are continually happening. You or your competitors can make website changes, change overall strategy, or make additional investments. Any of these can change the trajectory of the data, so you may want to update your SEO forecasts periodically to take into account any recent trend changes. Have fun forecasting!

Have questions? Let me know on [Twitter](https://twitter.com/patrickstox).
