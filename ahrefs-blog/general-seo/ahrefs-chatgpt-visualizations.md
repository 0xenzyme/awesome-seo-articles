---
title: "How to Visualize Ahrefs Data with ChatGPT"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "ahrefs-chatgpt-visualizations"
url: "https://ahrefs.com/blog/ahrefs-chatgpt-visualizations/"
canonical: "https://ahrefs.com/blog/ahrefs-chatgpt-visualizations/"
author: "Patrick Stox"
published: "2024-02-07T17:48:16+00:00"
updated: "2024-09-17T10:58:02+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "ai_search_topic"
  - "date_2024_watch"
fetched_at: "2026-06-12T11:11:24+00:00"
status_code: 200
html_hash: "b89c75b031f5557455a679b2490a84a676676df99463e5d70508659fd08b9ad3"
clean_word_count: 1708
clean_char_count: 10307
---
# How to Visualize Ahrefs Data with ChatGPT

SEOs have access to so much data that sometimes, it’s hard to know what to do with it all. I’ve been experimenting with visualizing Ahrefs data using GPT-4, so I thought I’d share the results with you all.

We’ve already launched some AI-enhanced features like search intent, but we made it even better by adding the traffic share for each intent. Check out [this write-up](https://ahrefs.com/blog/chatgpt-and-ahrefs/) from Si Quan for some more things we might add.

For the visualizations, you’ll need GPT-4. There’s an API, but you can also just use ChatGPT Plus for $20 a month. I’m hoping to bring many of these visuals to life within the tool, but these things take time and you can create them now. Let me know your favorites and any other use cases you find that you want to see us add!

IMPORTANT

For all these, export the data in UTF-8 format from the report indicated and run the prompt. Note that your results may differ a bit because of how LLMs work. You may need to ask for some adjustments to get exactly what you want.

## Find the biggest gaps between desktop and mobile rankings

![Scatterplot showing mobile and desktop rankings with labeled outliers](https://ahrefs.com/blog/wp-content/uploads/2024/02/scatterplot-showing-mobile-and-desktop-rankings-wi.png)

### Use case:

This allows you to see outliers. If you have some terms ranking better on Desktop vs Mobile, then you might want to look at mobile issues or [Core Web Vitals](https://ahrefs.com/blog/core-web-vitals/).

You can see both mobile issues and Core Web Vitals in Ahrefs’ [Site Audit](https://ahrefs.com/site-audit). You’ll need to run Site Audit as mobile and connect to [PageSpeed Insights](https://ahrefs.com/blog/pagespeed-insights/).

### Data source:

Download your desktop and mobile rankings from the Overview report in [Rank Tracker](https://ahrefs.com/rank-tracker) (remember to choose the UTF-8 format). Upload both files to ChatGPT.

### Prompt:

> Read these 2 files that contain desktop and mobile keyword rankings.
>
> Show me a scatter plot comparing the desktop and mobile positions for each keyword.
>
> Label ones that have the biggest gap between rankings.

## See a breakdown of branded and unbranded traffic & volume

### Use case:

See the breakdown of traffic and total volume by [branded and unbranded terms](https://ahrefs.com/blog/branded-search/). At a glance, I can see that the majority of our traffic comes from unbranded terms.

### Data source:

Download your keyword rankings from the Organic Keywords report in [Site Explorer](https://ahrefs.com/site-explorer) (make sure to select the UTF-8 file format) and upload the file to ChatGPT.

### Prompt:

> Label each keyword in the “Keyword” column as branded or unbranded. Then create a pie chart that shows the sum of “Current organic traffic” for both categories.
>
> Also create this chart with the sum of “Volume” for each.

## Show the change in volume for branded and unbranded keywords

### Use case:

See if you’re gaining or losing clicks for branded or unbranded terms between two dates. You need to have compare mode enabled for this to work.

### Data source:

Like the previous one, download your keyword rankings from the Organic Keywords report in [Site Explorer](https://ahrefs.com/site-explorer) and upload the file.

### Prompt:

> Label each keyword in the “Keyword” column as branded or unbranded.
>
> Create a visual that shows me how the organic traffic changed overall for branded and unbranded keywords based on the sum of the data for each in the “Organic traffic change” column.

## Find out when competing content was updated

### Use case:

See the last time competing content was updated. If competitors are updating their content a lot, it can indicate a more competitive market.

### Data source:

Enter a competitor’s website into [Content Explorer](https://ahrefs.com/content-explorer) and export the list of pages (choose UTF-8 as the export format). This can also be done with a keyword or topic.

### Prompt:

> Show me how many days since the content was updated.

## See how long links last

### Use case:

See how long backlinks were live on average. If you’re losing a lot of backlinks early, you may want to look into the reasons why. Read [our study on link rot](https://ahrefs.com/blog/link-rot-study/) to see many of the common reasons.

You can filter the Backlinks report for many of the common reasons why links are lost.

### Data source:

Export your link profile from the Backlinks report in Site Explorer (choose UTF-8 as the file format). Upload this to ChatGPT.

### Prompt:

> Read this file and give me a histogram to show the distribution of backlink lifespans.

## Look for seasonal patterns in link acquisition

### Use case:

See any seasonal patterns for your acquired links. Here, I see a big spike in the middle of 2022 and what seems to be a bit of a spike in November the last few years.

### Data source:

Like the previous one, export your link profile from the Backlinks report in Site Explorer. Upload this to ChatGPT.

### Prompt:

> Look for seasonal patterns in backlink acquisition.

If you’d prefer a heatmap like the one below, use this prompt instead:

> Analyze patterns in link acquisition (e.g., weekdays vs. weekends, monthly trends) using line charts or heatmaps to identify when most backlinks are acquired.

## Quickly see share of voice by tag & competitor

### Use case:

See which tag groups are strong or weak vs competitors. I can quickly see we dominate for things like link building, but we’re weak for the terms in our general marketing bucket, probably because we mostly focus on SEO.

### Data source:

Export the data from the Competitors - Tags report in Rank Tracker (use UTF-8 format).

### Prompt:

> Show me share of voice by tag and split it by competitor as well.

## Forecast time series data

### Use case:

Forecasting traffic or other metrics forward. This is great for [getting buy-in](https://ahrefs.com/blog/seo-buy-in/).

Sidenote.

This failed with larger datasets or multiple competitors, but you can always use my [SEO forecasting scripts](https://ahrefs.com/blog/seo-forecasting/) for this as well.

### Data source:

Export graph data from the Overview report in Site Explorer. You can choose any time-series graph you like (organic traffic, referring domains, etc.)

### Prompt:

> Forecast this time series data forward one year

## See the change in keyword rankings

Long story short on this one. I had a version that wasn’t as good as what [Marie Haynes came up with](https://twitter.com/Marie_Haynes/status/1722729038429450384), but I added to her visualization to make it even better.

### Use case:

The chart visualizes winners/losers for keyword rankings and shows me overall if I’m doing better or worse. From this image, I can see that more keywords overall are ranking worse, but overall rankings are up, so the positive ones moved up a lot more than the negative ones lost.

### Data source:

Download your keyword rankings from the Organic Keywords report in [Site Explorer](https://ahrefs.com/site-explorer) and upload the file.

### Prompt:

I used multiple prompts to get the final chart, but they might be able to be simplified into one.

> Show me a scatter plot that shows the changes from the previous position and the current position. Include changes to a lower position as green and changes to a higher position as red. Include a legend and trendline.
>
> Add a count for improved and worsened on the previous chart. Also show me on the chart on average, how much did rankings improve or decline
>
> Remove the averages as they are. I want the overall average change in ranking position as one number.
>
> Move the average to the right side of the chart so it’s readable

## Find anomalies in organic traffic

### Use case:

Find anomalies in time series data. In this case, most of the anomalies line up with major website changes and [Google algorithm updates](https://ahrefs.com/google-algorithm-updates).

### Data source:

Export organic traffic graph data from the Overview report in Site Explorer.

### Prompt:

> Identify anomalies in this traffic chart

## See share of voice changes by tag

![Share of voice between two time points for each tagged group of keywords

### Use case:

This tells me if certain tagged groups are doing better or worse between the dates.

### Data source:

Export data from the Tags report in Rank Tracker.

### Prompt:

> Show me share of voice over time by tag.

## See how traffic changed for each tag

### Use case:

See how traffic changed for each tag between two dates. We have a better view for this coming in Rank Tracker that will show the evolution over time.

### Data source:

Like the previous one, export data from the Tags report in Rank Tracker.

### Prompt:

> Show me how traffic is evolving for each tag.

## Find which groups of terms have the most potential for improvement

### Use case:

See which groups of terms have the most volume vs the clicks that they’re getting. High total volume and low clicks means you have a lot to work on.

### Data source:

Export keywords from the Overview report in Rank Tracker. (You can choose between desktop or mobile ranking data with the toggle).

### Prompt:

> Visualize search volume and clicks by tag.

## See which SERP features are most common

### Use case:

Shows common SERP features for you and competitors that you may want to target. If certain [schema markup](https://ahrefs.com/blog/schema-markup/) is required but you’re not using it, it can lead to an easy win.

You may also have an issue with your schema markup. Ahrefs’ Site Audit validates against both schema.org and Google standards.

### Data source:

Export the data from the Content Gap report in our Competitive Analysis tool.

### Prompt:

> Show me which SERP features are most common.

Sidenote.

I would probably adjust this prompt to split them out into individual features rather than feature groups.

## Final thoughts

I hope this has sparked some ideas for other SEOs out there. I want to see what you all will create.

Have a cool idea you want to share? Let me know on [X](https://twitter.com/patrickstox) or [LinkedIn](https://www.linkedin.com/in/patrickstox/).
