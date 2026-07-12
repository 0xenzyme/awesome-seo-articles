---
title: "The Guide to Finding Keywords You Ranked or Lost After a Google Algorithm Update"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "high"
slug: "guide-finding-keywords-ranked-lost-google-algorithm-update"
url: "https://www.semrush.com/blog/guide-finding-keywords-ranked-lost-google-algorithm-update/"
canonical: "https://www.semrush.com/blog/guide-finding-keywords-ranked-lost-google-algorithm-update/"
author: "Brett Elliott"
published: "2018-08-15T07:00:00+00:00"
updated: "2020-12-29T09:13:00+00:00"
categories:
  - "Keyword Research"
freshness_reasons:
  - "date_2020_very_old"
  - "time_sensitive_title"
schema_genre: "Keyword Research"
fetched_at: "2026-06-12T16:07:41+00:00"
status_code: 200
html_hash: "09c988a0374e304013e1d453aee9b1e53148cac52c6a02e581256dc5ee6dfd43"
clean_word_count: 1909
clean_char_count: 10817
---
# The Guide to Finding Keywords You Ranked or Lost After a Google Algorithm Update

## Picture this:

It's 8:30 AM, you are enjoying a hot coffee and open Twitter. You see SEO chatter about a core algorithm update. Curious and wary, you open Google Analytics and traffic has dropped. You frown. You open your keyword tracking tool. Your frown deepens. Everything looks fine in your rank tracking tool. You are not sure which keywords on which pages dropped, and you need to have some answers before your 10:00 AM client call. What to do?

That is what this guide is for. As long as you have Google Analytics, Google Search Console, and Semrush you can get creative and [discover keywords](https://www.semrush.com/blog/keyword-research-guide-for-seo/) that you lost after the latest update. You may also want to see which keywords are driving increases, and you can use this same process for that as well.

The first thing we need to do is find out which pages experienced large gains or drops. For this we are going to use the *All Pages* report in Google Analytics.

1. Login to Google Analytics
 2. Go to Behavior > Site Content > All Pages
 3. Set your segment to Organic Traffic
 4. Set your date range to only look at the period of time since the algorithm update affected your traffic

If your business is seasonal, then you want to set a comparison in the date range to compare traffic year over year. If you don't have seasonal traffic, then you want to compare it to the previous week.

![Google Analytics all pages report](https://static.semrush.com/blog/uploads/media/00/84/00841f8a0047116eb3b20cb3c26c4cd7/organic-entrances.png)

Notice that we are not focused on sessions or pageviews. We have set our segment to only look at organic traffic, so we are focused on entrances. [Entrances](https://support.google.com/analytics/answer/2956047?hl=en) is the number of times visitors entered your site through a specified page or set of pages; this means that these specific pages are the ones that experienced a change in rankings, good or bad because the traffic entering that page from search changed. We are not using sessions or pageviews because a person can land on a homepage from organic, then visit other pages on the site and increase organic sessions, even though they did not land on that page from Google.

Sort your table by organic entrances in descending order so you can see your top performers. Depending on your site, this might mean that you need to change the default 10 rows to something a little larger. You can go up to 5000 rows, but we are mostly looking for the largest drops or gains and many websites get the majority of their traffic from the top 25 or 50 pages on their site. Find the page you want to examine and copy the URL.

![google analytics all pages report organic entrances](https://static.semrush.com/blog/uploads/media/25/fa/25faeab96ed066a1d1a1329f8f52614d/organic-entrances-increase.png)

I definitely want to know what keywords are driving this sudden large increase in my traffic, so I am headed to Semrush. Go to the Dashboard and open your website or enter in the search bar. Select Organic Rankings, then Positions. Scroll down to the bottom, open the advanced filters, and set your filters to match what I have in the image below and hit apply.

![SEMRush filters](https://static.semrush.com/blog/uploads/media/92/51/9251514d53be14bf4a11a8db87392190/semrush-filters.png)

This will give you all the keywords within Semrush's index that your webpage was ranking for, and is a pretty nice list, but we need to export it in Excel because we want to see some before/after rankings. Once it is exported, you will notice that column "last updated" was converted to a timestamp. We need to fix that so select the cell next to the timestamp (on mine this is cell N2) and enter this formula:

=(((M2/60)/60)/24)+DATE(1970,1,1)

The M2 is referencing the timestamped cell, so if you delete columns, just make sure you update the reference. Right click the highlighted cells, select **Format Cells**, go to the **Number** tab, choose **Date** in the left-hand sidebar, and then choose the **date type**. Hit OK, and you now have regular dates.

Add in a name for the column like "Last Checked," then select row 1, click Data in the ribbon up top and set a Filter. You are then going to open up the "Last Checked" filter and *deselect* all the dates since the update impacted your site. In my case, this removed all keyword rankings that Semrush collected after August 2nd since my site was not impacted until August 3rd.

Now you have a list of all the keywords within Semrush's index that you were ranking for before the algorithm update. Copy those keywords and paste into a new tab. Delete all columns except **keyword**, **position**, **search volume**, and **date last checked**, then name the tab PRE ALGO. These are the keywords you will later enter into a position tracking tool to get your new rankings so you can compare drops or increases from before and after the algorithm update.

Now reopen your filter, and reverse the filter so you are only looking at rankings that Semrush collected *after* the update. Copy/paste those into another new tab. Delete all columns except **keyword**, **position**, **previous position**, **search volume,** and **date last checked** and name the tab POST ALGO. Because we have the current position, which was checked after the algorithm update, and the previous position as well, we can set a cell formula in a blank cell to =(previous position)-(position) and hit enter; this will show the change in rank for each keyword after the algorithm update\*. I like to use conditional formatting to highlight queries where I moved up or down. By doing this, I can instantly see which keywords improved after the update. There are two things I look for - moving up on high search volume queries and moving from page 2 onto page 1. If you are trying to identify big drops, just reverse your logic and highlight the negative numbers.

![excel workbook SEO](https://static.semrush.com/blog/uploads/media/dc/5e/dc5e1a53487ea595da2abb2ce049eb68/workbook8.png)

*This data shows that we moved up from position 4 to position 1 for a high volume keyword after the update, explaining some of the boost.*

*Because Semrush does not timestamp the previous position, we do not know for sure that we are comparing a rank change from before the algorithm and after the algorithm for this dataset; this is why it is best to run this analysis quickly after you notice an impact to your traffic - I recommend doing it within a week.*

Okay, this is cool, we now have some of the keywords that increased or decreased for this page. But we are still missing some data.

**We need the other piece of the puzzle.**

Open the PRE ALGO tab and upload those keywords to a keyword tracking tool. Any which one is fine, but I use Semrush for this because it is fast. You can find the position tracking tool under projects when you set up your domain in there.

![SEMRush position tracking](https://static.semrush.com/blog/uploads/media/f5/ff/f5ff4820f18bed052d424a927f8b654e/semrush.png)

Once you have your keyword data, export it into a spreadsheet again, then copy it into a new tab on the sheet you have been working in and name it NEW RANKS. Open your PRE ALGO tab and change the name of the "position" column to "previous position." Insert a column next to it and name it "position." Bring your new ranking data over from the NEW RANKS tab using the Vlookup function. Now you have all the keywords for that page from Semrush's dataset, and you can see where you moved up and where you moved down.

### BONUS:

People who know me know that I am not a huge fan of Search Console for keyword data, but there are times when it can still provide value.

**Follow these steps:**

1. Login to your GSC account.
 2. Go to the performance report.
 3. Set your filter for the date range you want.
 4. Set a page filter for the URL you're investigating.

In my case, I am looking into an increase, so I set my date range to begin the day the algorithm impacted my site. If I were investigating a drop, then my end date would be the day before the algo affected my site. It should look something like this:

![Google Search Console page level data](https://static.semrush.com/blog/uploads/media/3a/25/3a2586efd17ac268b46037b91ad4c128/performance.png)

Scroll down to see all the queries that drove impressions and clicks to your site. We want this data in a spreadsheet. Change the rows to their maximum limit (500) and export to CSV.

**Note:** You may notice as we compare the two that Google Search Console is telling me that page received 876 clicks from search while Google Analytics is telling me it received 1,071 organic entrances in the same time frame. This is why I do not believe this data is complete, but I do believe it is accurate, so we will use it where we can.

Add a new tab titled GSC in your spreadsheet and copy the Search Console data into there. Use your VLOOKUP function to marry your click data to your keywords from Semrush. It is easiest to view this next to the rank change column we created, so insert a column and use [VLOOKUP](https://www.excel-easy.com/examples/vlookup.html) to bring over the click data. Now you can see which keywords Google is telling you has been driving clicks to your site, along with data from Semrush that shows what moved up and what moved down.

You may be wondering why we are going through this with Search Console. It appears that the bigger the search volume, the more clicks you get, and it is all as expected. Except no keyword index is complete and one of the first things I noticed is that the keyword that Google Search Console says is driving the most amount of traffic (126 clicks in 5 days) is not tracked in Semrush's index. Since that is my largest traffic driver, it is definitely a keyword that I want to keep an eye on and would be adding to my rank tracking tool.

The important thing to remember is that we are not going to get flawless and complete data from any source, but using this process, we can find many keywords that are driving traffic or stopped driving traffic after the update.

## Upgrade Your Tracking

Take this as an opportunity to promote why you need a bigger budget to track more keywords. It is much easier to look at daily historical data and just *know* where the increase or decrease occurred while looking at both your pages and your keywords. Map out the keywords that impacted traffic to different pages and use the insight to estimate how much of an increase you will need. When you know how Google altered rankings for your website, it is very easy to examine the SERPs, compare your page, and put a counter plan in place to climb back up the ladder.
