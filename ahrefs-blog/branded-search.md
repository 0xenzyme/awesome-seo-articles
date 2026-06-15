---
title: "Branded Search vs. Non-Branded Search: What's the Difference?"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "branded-search"
url: "https://ahrefs.com/blog/branded-search/"
canonical: "https://ahrefs.com/blog/branded-search/"
author: "Mateusz Makosiewicz"
published: "2022-05-20T07:18:34+00:00"
updated: "2022-08-24T13:54:58+00:00"
categories:
  - "Keyword Research"
freshness_reasons:
  - "date_2022_old"
fetched_at: "2026-06-12T11:20:15+00:00"
status_code: 200
html_hash: "2dd9927c96ddcded8f129d90a2d500dea50e05a09847c530e73037a3f8232c7b"
clean_word_count: 2056
clean_char_count: 12353
---
# Branded Search vs. Non-Branded Search: What’s the Difference?

Most SEO advice talks about optimizing for keywords that don’t mention your brand because that is how you can attract complete strangers to your business. But what about search queries that do mention your brand?

In other words, what about attracting people who are exactly searching for your business? Naturally, you can optimize your website for these kinds of queries too. In this guide, I’ll explain how to do that. We’ll cover the following:

- [Difference between branded and non-branded search](#1-difference-between-branded-and-nonbranded-search)
- [Why optimize for non-branded search](#2-optimize-for-nonbranded-search)
- [Why optimize for branded search](#3-optimize-for-branded-search)
- [How to optimize for branded search](#4-how-optimize-for-branded-search)

## Difference between branded search and non-branded search

The difference between branded and non-branded search is that a branded search contains your company, service, or product name, whereas a non-branded search doesn’t. This applies to both organic results and search ads.

## Why optimize for non-branded search

Ranking for non-branded keywords allows you to attract people who are searching for products or services related to your business **but may not necessarily know your brand**. Hence, this is a great way to attract new customers.

Our blog article about our [SEO checklist](https://ahrefs.com/blog/seo-checklist/) attracts searchers who don’t necessarily know our product. Data via Ahrefs’ [Site Explorer](https://ahrefs.com/site-explorer).

We have an [entire SEO course](https://ahrefs.com/seo) that focuses on optimizing for non-branded keywords. So in this article, we’re going to focus on SEO for branded search.

## Why optimize for branded search

Ranking for branded keywords allows you to attract people who are **specifically searching for information about your company**.

They already know your brand but want to learn more about what you do. For example, they may be looking for reviews, comparisons with other brands, or specific information like technical data or media assets.

So with branded search, depending on the query’s intent, you’re targeting people who are:

- **Close to buying** **from you** – People may be looking up your brand specifically or searching for comparisons between you and your competition. You can address any objections, answer questions, or reassure them you are the right choice.
- **Your current customers** – Keeping your current customers informed is a straight path to keeping them happy.
- **The press** – The aim here is to be the #1 source of information.
- **Brand fans and other people simply interested in what you do**

Our [landing page](https://ahrefs.com/vs) comparing our product to the competition attracts searchers who Google queries containing our brand name and “vs.” Data via Ahrefs’ [Site Explorer](https://ahrefs.com/site-explorer).

## How to optimize for branded search

There are basically four steps in this process. For the purpose of this guide, I’m going to use fintech company Revolut as an example (but this can be any company).

### 1. Find keywords related to your brand, company, or product

You need to create two lists of keywords to have a complete overview of your branded search landscape:

1. **Find keywords you rank for**
2. **Find keywords you** ***don’t*****rank for**

One thing to keep in mind here is that everything we’re going to do in this guide is country-specific. You will need to repeat the process for every country whose keywords you want to rank for.

#### Find keywords you rank for

When you have an SEO tool like [Ahrefs](https://ahrefs.com/), finding keywords you rank for is a piece of cake. All you need to do is plug in your domain, go to the **Organic keywords** report, and type in words/phrases denoting your brand or products in the filters.

Tip: Don’t bother about misspellings of keywords. Google’s algorithms will likely take care of that with the correct spellings once you create content that ranks for those keywords.

Export that list of keywords and import it into a spreadsheet editor. I’ll be using Google Sheets.

And this concludes our first list. Now on to the next one.

#### Find keywords you don’t rank for

To create a list of keywords you don’t rank for, you need to combine and compare two lists: the list of branded keywords that you rank for (it’s what we just created) and a list of all branded keywords for your company. This is what we’ll do.

In your keyword tool—I’ll use Ahrefs’ [Keywords Explorer](https://ahrefs.com/keywords-explorer)—plug in the same branded keywords you used for the first list, choose the same country as before, and hit “Enter.”

Then go to the **Matching terms** report. You will get a list of *all* branded keywords.

Now we need to compare keywords *you rank for* with *all* keywords in order to get branded keywords you don’t rank for. So do the following:

1. Export the list
2. Import the list to a new sheet in the same spreadsheet as the first list
3. Create an additional column in that newly imported list and name the column “Do we rank?”
4. Insert this array formula into the first cell of that column: `=ArrayFormula(COUNTIF(Ranking!A2:A, B2:B)=1)`

Where “Ranking” is the name of the sheet with keywords you rank for and the cell ranges are the column with your keywords.

This formula will automatically populate the entire column with “true” if you already rank for a given keyword and “false” if you don’t. Chances are you won’t get too many “falses” here, but the thing is you never know until you check.

This way, we’ve created the two keyword lists we need for this process. Now let’s see how we can use them.

### 2. Pick keywords worth targeting

Here’s how we’re going to categorize branded keywords worth targeting:

1. **Underperforming keywords** – Because if you improve their rankings, you can get more traffic from the SERPs (search engine results pages)
2. **Pages with mismatched intent** – Because mismatched search intent doesn’t give people what they came for
3. **Valuable new keywords** – Because you can get more traffic by targeting new keywords

#### Underperforming keywords

Underperforming branded keywords are basically keywords that don’t rank #1. How far from #1? It depends on the search query and the competition.

If you think there’s a reasonable chance of a keyword ranking higher than the current position, you should try it. Generally speaking, for some queries, ranking in the top three is a success. But for those with really fierce competition (like search queries used for comparisons), ranking in the top 10 is a success.

And so open the first list, click on the “Current position” column, and sort from Z to A. Anything here that doesn’t rank #1 is your opportunity. Look at each keyword. If it’s something you can potentially create better content about, mark it.

A cool trick to use for marking your keywords is to create an [in-cell dropdown list](https://support.google.com/docs/answer/186103?hl=en&co=GENIE.Platform%3DDesktop).

Additionally, look at the “Volume” column to determine if that keyword gets any search demand in the country you’ve chosen.

#### Pages with mismatched intent

Now let’s choose keywords for the second category: mismatched intent. Since you’ve already gone through keywords that don’t rank #1, it’s time to take a closer look at those ranking #1. If you want to play on the safer side, you can extend your search to the top three or even the top 10.

Here’s an example of a page with mismatched search intent. People looking for Revolut’s logo probably want an official, high-quality image that’s downloadable. But Revolut doesn’t offer that on the pages that rank #1 for this query in the U.S.

So this keyword can be highlighted as “mismatched intent.”

Let’s move on to the last category: valuable new keywords.

#### New keywords

For this, we’re going to open the second sheet with all branded keywords. To show only those you don’t rank for in the chosen country, filter the “Do we rank?” column to only show “false” results:

Before we start to look at particular keywords, I suggest sorting them by search volume to get the most potentially valuable keywords first.

Now we can see if any of these keywords catch our eye. Here’s one: a comparison between Revolut and another fintech company:

### 3. Optimize existing content or create something new

Now we need to give search engines something they can rank. That means either optimizing content on existing pages or creating new content.

The list of keywords created in the previous step will tell us whether we need to do the first or the second. So:

- **Keywords marked as “underperforming” or “mismatched intent”** will need optimized content. For this, we’ve got you covered. Here’s a detailed guide on how to [optimize your content for search engines](https://ahrefs.com/blog/content-optimization/).
- **New keywords** that you do not yet rank for will most likely need new content. I’m saying “likely” because you may need to reconsider that, sometimes, it’s better to include some topics on existing pages than have them be on separate pages. And here’s a complete guide on [creating content designed to rank](https://ahrefs.com/seo/seo-content) in search engines.

### 4. Add internal links

The last step in our process of optimizing for branded search is adding internal links.

Apart from helping users to navigate your website, internal links play an important role in SEO. First of all, search engines use them for [discovering, (re)crawling, and indexing pages](https://ahrefs.com/blog/googlebot/). Moreover, they help Google understand what your page is about. And last but not least, they pass link equity.

As this is quite a straightforward tip, I’ll keep it short. There are essentially three places on your website where you may want to add internal links to content targeting branded keywords:

1. **Site navigation** – That means the top navigation and/or footer.
2. **Important pages** – If you want your content to be discovered easily and quickly, add links to it on pages that get the most traffic (like the homepage) or on the most relevant pages (like features).
3. **Pages where you mention the keywords** – For example, if Revolut mentions “buying stocks with Revolut” somewhere on its website, it can link to a blog post or a landing page dedicated to that topic.

Regarding the last point, you can streamline that process using Ahrefs (you can also do this for free using [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools)).

Go to Ahrefs’ [Site Audit](https://ahrefs.com/site-audit) and open the **Link opportunities** report. In the advanced filter section, set a new filter with conditions: keyword context contains [your keyword or phrase]. This way, you can find relevant link opportunities for pages that haven’t even been published yet.

**Recommended reading:** *[Here’s Why You Should Prioritize Internal Linking in 2022](https://ahrefs.com/blog/prioritize-internal-linking/)*

## Final thoughts

The more a company grows, the more roads will lead to the company through branded search ([19% of searches for SMBs vs. 42% for global brands](https://www.statista.com/statistics/1143368/distribution-branded-search-volume-global-brands-smbs/#:~:text=For%20global%20brands%2C%2058%20percent,fifths%20of%20search%20was%20unbranded.)).

But no matter the company size, SERPs seem to play the role of a company’s business card—people ask search engines all sorts of questions, and what they find becomes what they know. Thus, it’s good to own your branded queries.

Finally, if you decide to optimize your website for branded search, it’s important to know that the changes you make probably won’t take effect overnight. Remember, SEO takes time.

And if your SEO software comes with a [rank tracker](https://ahrefs.com/blog/best-rank-tracker/), use it to save yourself some time and effort—instead of *manually* checking your ranking progress, which can’t be done accurately anyway.

Next step: You can take optimizing for branded search even further by taking advantage of [Google’s Knowledge Graph](https://ahrefs.com/blog/google-knowledge-graph/).

Got questions? Ping me [on Twitter](https://twitter.com/m_makosiewicz).
