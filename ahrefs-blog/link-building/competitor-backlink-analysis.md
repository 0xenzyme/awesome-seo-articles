---
title: "How to Perform a Competitor Link Analysis in 3 Steps"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "competitor-backlink-analysis"
url: "https://ahrefs.com/blog/competitor-backlink-analysis/"
canonical: "https://ahrefs.com/blog/competitor-backlink-analysis/"
author: "Patrick Stox"
published: "2022-12-15T17:00:00+00:00"
updated: "2023-04-18T20:32:20+00:00"
categories:
  - "Link Building"
freshness_reasons:
  - "date_2023_aging"
fetched_at: "2026-06-12T11:22:24+00:00"
status_code: 200
html_hash: "c8b7e1b011641a01895e570e972aaa01da606756e9689924b825f5d9d974b610"
clean_word_count: 2055
clean_char_count: 12051
---
# How to Perform a Competitor Link Analysis in 3 Steps

A competitor link analysis is an assessment of the link profiles of major competitors where you look at their link building strategies to gain insights. Implementing some of the same strategies in your own link building can lead to higher rankings in search engines and increased business outcomes.

Performing this kind of analysis allows you to find sites that commonly link to websites similar to yours. If you look at well-ranking competitors and they have a lot of the same links, those links may be the ones helping them to rank.

Let’s take a look at how to perform a basic audit. Later, I’ll show you how to scale this process to get even more insights using bigger data.

## How to perform a competitor link analysis in three steps

This simple process can uncover a lot of link opportunities by looking at the common links that your immediate competitors already have.

### 1. Identify competitors

You may already know who your competitors are and can use that list later in the process. If you need some help, check out the **Organic competitors** report in Ahrefs’ [Site Explorer](https://ahrefs.com/site-explorer) to find a list of sites ranking for the same things you are.

If you don’t have a website yet, then you can search for a few main terms and you may be able to tell who the competitors will be. Another way of doing this is to simply add a few terms to Ahrefs’ [Keywords Explorer](https://ahrefs.com/keywords-explorer) and go to the [**Traffic share by domains** report](https://ahrefs.com/academy/how-to-use-ahrefs/keywords-explorer/traffic-share-domains#:~:text=This%20report%20shows%20the%20domains,on%20up%20to%2010%2C000%20keywords.), which will show you which sites are getting the most traffic for those terms.

### 2. Find common links

Take your list of competitors and enter them in the [**Link Intersect** report](https://ahrefs.com/link-intersect) in [Site Explorer](https://ahrefs.com/site-explorer). This is going to give you a list of all the referring domains that your competitors have and show how many different competitors have links from those sites.

You can click the numbers under each domain to see the kind of links they have from each website.

### 3. Identifying competitor strategies

There are a couple of ways to use this data. You can look at the common links your competitors have that you’re missing and work your way through those, or you can look for patterns in the data to see the type of sites where competitors are getting links. You may see things like niche sites, local listings, or other local websites.

Congratulations, you’ve done a basic competitor link analysis!

If you have a little more time, you can scale the link intersect process to gather even more data and opportunities. Keep reading to find out how.

bonus tip: check your competitors’ most linked content

If you look at the [**Best by links** report](https://ahrefs.com/academy/how-to-use-ahrefs/site-explorer/best-by-links) for some of your competitors in [Site Explorer](https://ahrefs.com/site-explorer), you may see some interesting content driving links to competitors that you otherwise may not find.

I commonly see things like tools, studies, or even quotes that drive a lot of links to individual competitors.

A lot of these links may be unique to a particular competitor, and you may miss them when looking at the overlap of competitor links.

If you see a competitor successfully gaining links this way, you may be able to create similar tools and content to gain more links for your own site.

## Scaled link intersect process

With a scaled process, you’re working with more data that can lead to additional insights and opportunities. You’ll spend more time up front going through this process, but you may be able to reuse the opportunities you find for other clients. I would expect it to take two to four hours for most people to follow this process.

First, we’ll look at your competitors’ links to find your niche-specific links. And later, we’ll look at other sites in your city to find local link opportunities.

### Niche links

The easier process that we covered earlier just looks at direct competitors. If you have more than 10 direct competitors, you can still use a similar process to what I’m about to show to gain more insights.

Just skip the section below and go directly to where you’re exporting referring domains of competitors. You can use your own list or get a larger list from the **Competing Domains** report in [Site Explorer](https://ahrefs.com/site-explorer).

#### Local only

This process is a great fit for companies focused on [local SEO](https://ahrefs.com/seo/local-seo), but it requires a little more work.

By local SEO, I mean companies that mostly compete in one area like dentist offices, law firms, plumbing companies, etc. If you look at sites competing in other markets that may be stronger or more competitive than your own, you’ll find a lot of additional opportunities that no one in your market has taken advantage of.

First, create a copy of this [Google sheet with the top 50 U.S. cities](https://docs.google.com/spreadsheets/d/1_wSRfQyy2DTucqAfR075hs3U_ZB1bKV4VLbYhXqzYe0/copy). Replace “service” with the name of your niche and copy the value down to create your keyword list.

If you’re in a different country, you can create a similar sheet with popular cities in your country.

Copy the resulting list of terms from column C and paste them into [Keywords Explorer](https://ahrefs.com/keywords-explorer), then click the search button.

If you click the export option, you’ll see another menu with an option to include the [SERPs](https://ahrefs.com/blog/serps/) in the export. This will include the sites in the top 10.

With the list of sites, delete anything that doesn’t look like a niche site.

You can set your own filters to make this easier. But as a general way to clean the data, I’d recommend:

- Insert > Table
- Filter > DR less than 50. Most local sites won’t have a DR that high, whereas directories and aggregators like yellowpages.com will. This is trying to get rid of all the directory/roundup/best-of-type sites.
- Filter Type > Organic

Then manually delete anything that seems out of place. What you’ll be left with is the top sites in your niche from different cities.

#### All companies

The most time-consuming process is what’s next. For each site, you’ll need to export its referring domains using the [**Referring domains** report](https://ahrefs.com/academy/how-to-use-ahrefs/site-explorer/referring-domains) in [Site Explorer](https://ahrefs.com/site-explorer). I’d recommend saving them to a new folder to make the next step easier.

Or if you have an enterprise plan that has [API](https://docs.ahrefs.com/docs/api) access and you want to do this quickly, you can iterate through the websites. We provide the needed request if you click the “{ } API” button.

Now we need to combine all the files into one. I’ll show you how to do this in Windows and on MacOS. But if it’s easier for you, then you may want to try one of the online tool options that can combine CSV files.

I usually do this with Windows Command Prompt. Here’s the process:

1. Save the files to a new folder
2. Get the path either by using shift+right-click on the folder and “Copy as path,” or copy it from the address bar when viewing the contents of the folder
3. Open Command Prompt, which you can find by searching “cmd”
4. Type “cd,” press “Space,” right-click and paste, then press “Enter”
5. Type “copy \*.csv whatever-name.csv” and press “Enter”

For MacOS, you’ll use Terminal instead of Command Prompt, and the command to combine them is “cat \*.csv > whatever-name.csv” for step #5. But otherwise, the instructions should be the same.

Open the new combined file. We’ll need to get a count of how many times each of the referring domains appears in the file. Here’s how to do that:

- Insert > Table
- Insert Column next to Referring Domain column and name it Count
- In the Count Column, add the formula `=COUNTIF(B:B,[@[Referring Domain]])`

Copy the numbers in the Count column and paste in the same place as values. This makes it so the numbers aren’t lost when we remove duplicates. To remove duplicates:

- Data > Remove Duplicates based on the Referring Domain
- Data > Sort by Count > Largest to Smallest

This leaves you with the top referring sites in your niche. It should look something like this:

You’ll want to categorize them in ways that make sense to you. I’d highly recommend pulling out the niche-specific domains. Sometimes, you’ll see various organizations, trade shows, suppliers, vendors, niche-specific directories, etc.

Take that list and look at how they’re linking to these other sites. There are a number of ways to do this like checking the [**Linked Domains** report](https://ahrefs.com/academy/how-to-use-ahrefs/site-explorer/linked-domains) for these sites to see how they link out to other sites.

You can even repeat this process with other similar niches where you may find additional opportunities that no one in your niche has taken advantage of.

Next, let’s look at how you can use a similar process to find local link opportunities.

### Local links

If we look outside our niche to other sites in the same city, the overlap of their links can provide a lot of opportunities for [local link building](https://ahrefs.com/blog/local-link-building/). Local websites tend to talk about and link to other local websites. If you’re an agency that has a lot of local SEO clients in the same area, you’ll definitely want to go through this process.

Make a copy of this [Google sheet with some of the most popular niches for local businesses](https://docs.google.com/spreadsheets/d/1YtCs0d-B65UZq4pXa41crFMYThAJgT2_A5RbyEhzw7I/copy). Simply add the name of your city and copy the value down to create your keyword list.

The rest of the steps are the same as the niche example above where you copy the terms into [Keywords Explorer](https://ahrefs.com/keywords-explorer), export the results with the SERPs, and then pull the referring domains for all of the sites.

When you get to the categorization part, look for any interesting patterns. Here are a few I found for my hometown of Raleigh:

1. **Colleges/universities** – These include jobs, scholarships, club sponsorships, discounts, and alumni links.
2. **City-specific sites and directories**
3. **Local news and magazines**
4. **Sites about the state and surrounding areas**
5. **Suppliers/affiliations/partners** – Some of these were testimonials and case studies.
6. **Churches** – They seem to link to a lot of local organizations and businesses of their members.
7. **Business groups** – They link to those who are part of the group.
8. **Events** – I saw a lot of links from meetup.com—most of which were from hosting or sponsoring.
9. **Sponsorships and charities** – This is also great for supporting the local community.
10. **Podcasts**
11. **Awards** – Especially local favorites.
12. **Coupons**
13. **Directories**
14. **Job postings**

You may find some other interesting patterns. For example, I saw that pretty much anyone involved in weddings like DJs, photographers, event planners, and caterers all seem to link to each other. I found another pattern where realtors, apartments, and HOA sites tend to link to things to do and places to eat.

I also saw some well-done ego bait expert roundups. Many of these people have their own personal sites and blogs that link to this type of content.

There were also a lot of links from the local Reddit community, Facebook groups, and Nextdoor. These types of sites can also be valuable sources for referrals.

## Final thoughts

Analyzing your competitors’ links is a great way to reverse engineer their strategies and find the links that may be helping your competitors the most. Scaling that process can lead to a lot of unique insights.

Message me [on Twitter](https://twitter.com/patrickstox) if you have any questions.
