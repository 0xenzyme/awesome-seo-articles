---
title: "13 Technical Marketing Skills You Can Learn (Even If You’re Not Technical)"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "technical-marketing-skills"
url: "https://ahrefs.com/blog/technical-marketing-skills/"
canonical: "https://ahrefs.com/blog/technical-marketing-skills/"
author: "Ryan Law"
published: "2025-03-21T16:23:25+00:00"
updated: "2025-04-04T14:29:51+00:00"
categories:
  - "General Marketing"
freshness_reasons: []
fetched_at: "2026-06-12T12:11:40+00:00"
status_code: 200
html_hash: "f02ff04f4879980fcea3107d3eb75abb6d8dcb1331996106b7304b1cc6bc487b"
clean_word_count: 3130
clean_char_count: 20003
---
# 13 Technical Marketing Skills You Can Learn (Even If You’re Not Technical)

Many marketers hit limits not because they lack ideas, but because they can’t execute or scale them.

Not everyone has the luxury of developers, designers, or analysts who can help turn big ideas into reality. Even if you do, you still need to compete for time and help with the rest of your organisation.

But times have changed. AI tools like ChatGPT make technical learning radically more accessible. It’s now possible to become “technical” even if you’re a humble writer, social media marketer, or brand strategist—because we all have access to a patient, capable technical tutor in the form of a large language model.

I’m a lifelong marketer and non-technical person. I always wanted to learn how to code, but never knew where to start. I bounced off half a dozen coding courses, until I realised that ChatGPT is the perfect teacher and troubleshooter. Now I can call APIs, write simple scripts, and automate parts of my workflow:

If I can do it, you can too.

## 1. Call an API to collect tons of marketing data

Ever wished you could pull live data from tools like Ahrefs, social platforms, or internal product analytics—without waiting on engineers?

The answer: APIs (Application Programming Interfaces) are tools that let different software talk to each other. They unlock access to data that can speed up competitive research, automation, and even building custom dashboards.

I used ChatGPT to learn how to use the Ahrefs API to fetch my top-performing content, track SERP volatility, and monitor backlinks automatically. We break down how it works in our [Ahrefs API guide](https://ahrefs.com/api/guide).

![](https://ahrefs.com/blog/wp-content/uploads/2025/03/word-image-186537-1.jpg)

Use the API button in Ahrefs to get a sense for how API requests are structured. If you have access to the Ahrefs API, you can [read our documentation](https://docs.ahrefs.com/docs/api/reference/introduction) and even make [free practice requests](https://docs.ahrefs.com/docs/api/reference/free-test-queries).

### How to get started:

- Learn the basics of HTTP requests, authentication (like API keys), and response parsing (usually JSON). [Try Mozilla’s API guide](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction), [Postman Learning Center](https://learning.postman.com/), or [RapidAPI’s beginner tutorials](https://rapidapi.com/blog/api-glossary/what-is-an-api/).
- Try your first live request using [Postman](https://www.postman.com/) to hit a simple endpoint, like fetching weather or headlines. For extra practice, try calling a public endpoint like the [News API](https://newsapi.org) to fetch the latest articles on any keyword—useful for content ideation or monitoring industry trends.
- Use ChatGPT to write a Python script using requests, explain each line, and handle API authentication. Paste in API docs—it can help translate them into working code.

## 2. Write SQL queries to analyze blog post performance data from GSC or GA4

What if you didn’t have to wait for an analyst to pull your numbers? That’s the power of SQL—a universal language for asking questions about data.

I use ChatGPT to help write SQL queries that pulled blog post impressions, clicks, and average position from Google Search Console—broken down by URL and date. Then I used those insights to prioritize which articles to update and re-promote.

(This works great alongside a full [content audit process](https://ahrefs.com/blog/content-audit/).)

One of many SQL queries I use as part of my blog reporting process. This example selects URLs from our international blogs (/es/ is Spain, and so on).

### How to get started:

- Focus on learning SELECT, WHERE, GROUP BY, JOIN, and CASE statements. For an excellent beginner-friendly walkthrough, try [Mode’s SQL tutorials](https://mode.com/sql-tutorial/) or [LearnSQL.com’s SQL Basics Track](https://learnsql.com/course/sql-basics/).
- Use free tools like [Mode](https://mode.com/sql), [DB Fiddle](https://www.db-fiddle.com/), or [BigQuery sandbox](https://cloud.google.com/bigquery/docs/sandbox) to write and test your queries.
- Paste your table schema (column names and types from your spreadsheet) into ChatGPT and describe what you want to measure—it will write and explain the full query.

## 3. Automate workflows with Zapier or Make

Sick of repetitive tasks clogging up your day? Learn how to automate your most mundane, repetitive tasks, and you can free up your time for more exciting things.

Automation platforms like [Zapier](https://zapier.com/app/home) and [Make](https://www.make.com/en) let you build “if-this-then-that” logic across all your marketing tools—without touching code. It’s technically “no-code,” but don’t be fooled—it still teaches you how to think like a programmer: setting conditions, chaining steps, handling exceptions, and reasoning through logic flows.

Here’s a super simple Zap that syncs changes in our master content spreadsheet with spreadsheets for each of our international blogs—in this case, notifying the Japanese marketing team that new articles are ready for localization:

I’ve used Zapier for a hundred different things: managing contact form submissions, triaging leads, triggering editorial workflows for content, syncing data between different spreadsheets, creating notifications in Slack, you name it.

### How to get started:

- Start with [Zapier’s template library](https://zapier.com/apps) or [Make’s visual scenario builder](https://www.make.com/en/features/scenarios).
- Build a simple multi-step automation that uses filters, conditions, and formatting. Zapier’s [getting started guide](https://help.zapier.com/hc/en-us/articles/8496244429453) is helpful if you’re new.
- Ask ChatGPT to map out logic flows or generate JSON webhook payloads for more advanced steps. You can also paste in existing Zap or Make configuration details and ask it to optimize or troubleshoot them.

## 4. Write Google Apps Scripts to automate Sheets

Apps Script (a form of JavaScript) lets you create automations and integrations inside Google Sheets.

You can use Apps Script to send automated email summaries, archive form responses, merge data from multiple Sheets, or trigger Slack alerts when new data appears. I use a script that automatically fetches author data from newly published blog posts in our CMS and logs it to a shared Google Sheet—so I could track who was publishing what, without chasing down teammates or manually copying data.

Apps Scripts also work in Google Docs. Here’s a simple script that I run to automatically add WordPress shortcodes into my finished drafts. ChatGPT wrote the script in about ten seconds flat, and this saves me about ten minutes per article draft:

### How to get started:

- Learn key methods like SpreadsheetApp, getRange(), and triggers like onEdit(). You can explore these in the [Apps Script documentation](https://developers.google.com/apps-script/guides/sheets) or look through examples on [GitHub](https://github.com/topics/google-apps-script) to see how real projects are built.
- Build a script that sends email alerts or fetches data from another Sheet. If you’re new to JavaScript, try starting with [JavaScript.info](https://javascript.info/), [MDN’s JS tutorial](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide), or [W3Schools JavaScript basics](https://www.w3schools.com/js/). These will help you understand the core programming concepts that Apps Script relies on.
- Use ChatGPT to write, explain, and debug your Apps Script line-by-line.

## 5. Clean messy CSVs with Python and Pandas

If you’ve ever imported email lists or GA4 exports, you know: raw marketing data is chaos.

Python’s Pandas library is built to clean and transform that chaos into clean, structured insights. It’s a Python library that makes it easy to filter, clean, and reshape spreadsheet-style data.

I’ve barely scraped the surface of the Pandas library, but I already use it deduplicate rows, normalize UTM parameters, and automatically reformat raw exports into the right format for my monthly reporting.

Pandas’ data frames are crucial for my blog reporting automations.

### How to get started:

- Install [Jupyter Notebook](https://jupyter.org/install) and [Pandas](https://pandas.pydata.org/docs/getting_started/index.html). Jupyter is an interactive coding environment where you can write and test Python code in your browser.
- Practice loading CSVs, renaming columns, filtering rows, and filling missing values.
- For hands-on learning, check out the [Pandas Getting Started tutorials](https://pandas.pydata.org/docs/getting_started/index.html), [Kaggle’s Python micro-course](https://www.kaggle.com/learn/pandas), or [Dataquest’s beginner Pandas course](https://www.dataquest.io/course/pandas-fundamentals/).
- Paste a sample dataset into ChatGPT and ask it to write and explain a data cleaning pipeline.

## 6. Visualize trends with Looker Studio

Being able to build dashboards or charts helps you get buy-in faster and uncover patterns that raw spreadsheets miss.

Looker Studio is one of the easiest ways to build custom dashboards from your marketing data—without needing to code or use BI tools.

Ahrefs now offers a direct integration with Looker Studio, so you can pull in SEO metrics like traffic, backlinks, keyword rankings, and site audit data to build real-time dashboards without exporting CSVs. That means less manual reporting and more time spent analyzing trends across content, campaigns, or competitor domains.

You can learn how to set it up [in this guide](https://help.ahrefs.com/en/articles/9229306-how-can-i-use-ahrefs-with-looker-studio).

### How to get started:

- Connect Google Sheets, GA4, or Ahrefs directly to Looker Studio. [Follow this guide to get started](https://support.google.com/looker-studio/answer/9053467?hl=en).
- Create visualizations like bar charts, pie charts, and time series with calculated fields.
- Use ChatGPT to help write Looker formulas, blend data sources, or troubleshoot broken charts.

## 7. Scrape public data with BeautifulSoup or Scrapy

Need structured data from websites that don’t offer APIs? Scraping public pages is one option—whether you’re gathering event listings, job boards, or blog metadata at scale.

(Just keep in mind: not every website wants to be scraped. Always check their robots.txt file and terms of service before you start.)

If you want a safe start project, try using BeautifulSoup and ChatGPT to scrape publicly available product data from the [Books to Scrape](https://books.toscrape.com/) demo site, which is designed specifically for practicing web scraping. Try to extract titles, prices, and star ratings, then organize the data into a spreadsheet for analysis. Because the site is built for learning, it’s a safe and responsible place to sharpen your scraping skills.

[Books to Scrape](https://books.toscrape.com/) is a site that actively encourages scraping.

### How to get started:

- Learn Python basics and install libraries like [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [Requests](https://requests.readthedocs.io/en/latest/).
- Practice scraping your own site to avoid breaking anything. You can also test your skills on sites that explicitly allow scraping—like [Books to Scrape](https://books.toscrape.com/), a demo e-commerce site built for this purpose.
- Ask ChatGPT to generate scraper scripts, explain the logic, and handle pagination or user-agent headers.

## 8. Learn Python for automating routine marketing tasks

You’ve probably noticed that I like Python. Python is the backbone of tons of cool workflows—it’s how you go from spreadsheets and manual processes to real automation.

Learning any coding language is obviously a big ongoing commitment, but even a small amount of fluency can let you build very cool things.

With help from ChatGPT, I’ve automated tasks like exporting blog performance data from Google Search Console and visualizing it for my monthly content report, downloading favicons for my “[top companies](https://ahrefs.com/blog/fastest-growing-ai-companies/)” lists, and extracting possible keywords from podcast transcripts.

A handful of my amateur Python projects.

### How to get started:

- Learn basic syntax (variables, functions, loops). One great place to start is Replit’s free [100 Days of Python](https://replit.com/learn/100-days-of-python), which combines bite-sized lessons with hands-on coding exercises right in your browser—no setup required.
- Use [os](https://docs.python.org/3/library/os.html), [csv](https://docs.python.org/3/library/csv.html), and [re](https://docs.python.org/3/library/re.html) libraries to automate tasks like renaming, cleaning, and categorizing.
- Ask ChatGPT for Python scripts tailored to your workflow and have it explain the code.

## 9. Build dashboards with Notion, Airtable, or Retool

While Airtable and Notion are no-code tools (hence “non-technical”), they help explain how relational databases work: how different tables connect, how data types influence behavior, and how to structure your information for easy querying and automation.

These are foundational concepts that not only make you better at using Airtable, but also dramatically improve your spreadsheet game and prep you for more advanced tools down the line.

I’ve used Airtable in particular to build lightweight CRMs, [programmatic SEO strategies](https://ahrefs.com/blog/programmatic-seo/), and entire content management systems, capable of tracking briefs, drafts, publish status, and performance.

Here’s an example content management system we built for our marketing agency, way back in 2017.

### How to get started:

- Create a base in [Airtable](https://airtable.com/) or table in [Notion](https://www.notion.so/) with fields like status, owner, due date.
- Build views to filter by content type, author, or due date.
- Use ChatGPT to draft formulas, suggest schema improvements, or automate with buttons.

## 10. Learn how to use Pivot tables in Google Sheets

Pivot tables are one of the most powerful ways to analyze large sets of spreadsheet data—without writing a single formula.

I used to use them a ton in my blog reporting: to summarize content performance by author, spot trends across different content types, and even explore correlations between publish cadence and traffic.

Here’s a real pivot table from our recent AI in content marketing survey. The pivot table turns tons of unwieldy data into specific, useful analyses.

### How to get started:

- For a step-by-step guide, try [Google’s pivot table tutorial](https://support.google.com/docs/answer/1272900?hl=en) or this excellent [pivot table walkthrough from Ben Collins](https://www.benlcollins.com/spreadsheets/pivot-tables-google-sheets/).
- Ask ChatGPT to help explain how to group data, calculate percentages, or create calculated fields inside your pivot.

## 11. Use Regex to extract and clean marketing data

Regex (short for Regular Expressions) is a compact language for finding patterns in text. While it looks intimidating at first, it’s one of the most useful technical skills you can pick up—and it’s perfect for marketers drowning in messy data.

I’ve used regex to clean UTM parameters, extract domain names from referral URLs, filter URL lists to find just international subfolders, validate email formats, and even pull keywords from content briefs. It’s especially useful for filtering in Ahrefs: [Site Explorer and Site Audit both accept regex queries](https://help.ahrefs.com/en/articles/9919240-where-can-you-use-regex-regular-expressions-in-ahrefs):

### How to get started:

- Try free RegEx testing tools like [Regex101](https://regex101.com/) or [RegExr](https://regexr.com/), which highlight matches and explain the logic.
- Start small: match email addresses, isolate URL slugs, or clean campaign tags.
- Use ChatGPT to write expressions for you—just describe the pattern you want, and it can generate and explain it line-by-line.
- Learn where [Ahrefs accepts regex](https://help.ahrefs.com/en/articles/9919240-where-can-you-use-regex-regular-expressions-in-ahrefs).
- For hands-on guides, check out [Regular Expressions for Beginners](https://www.freecodecamp.org/news/regular-expressions-for-beginners/) and JC Chouinard’s [Regex for SEO](https://www.jcchouinard.com/regex-for-seo/).

## 12. Master advanced formulas in Google Sheets

Spreadsheets aren’t just for simple sums—they’re one of the most powerful (and underutilized) platforms for logic-driven marketing automation.

When you combine formulas like ARRAYFORMULA, QUERY, REGEXMATCH, and IMPORTRANGE, you’re basically writing lightweight code. It’s structured thinking, modular logic, and data manipulation—all without touching a programming language.

I’ve used advanced formulas to automate monthly reporting dashboards, analyze [search visibility trends](https://ahrefs.com/websites), and even build [keyword clustering workflows](https://ahrefs.com/blog/keyword-clustering/) directly in Google Sheets. This weird nested formula is a crucial part of my blog team reporting dashboard:

This kind of fluency opens up huge leverage, especially when paired with data from tools like Ahrefs. In fact, we wrote a whole post about it: [29 Google Sheets formulas every SEO should know](https://ahrefs.com/blog/google-sheets-formulas-seo/).

### How to get started:

- Learn how ARRAYFORMULA, QUERY, and FILTER can replace manual copy-pasting with dynamic updates.
- Use IMPORTRANGE to combine data from different Sheets.
- Try REGEXMATCH or REGEXREPLACE to clean up messy UTM parameters or flag branded keywords.
- Ask ChatGPT to help explain formulas, debug errors, or optimize slow Sheets.

## 13. Learn to prompt LLMs like a pro

Let’s wrap-up with a meta skill: prompting.

There’s a lot of pseudoscience around prompting large language models (LLMs)—people talk about it like magic spells. But the truth is, there is a science to good prompting. It’s a technical skill that amplifies all the others on this list.

Whether you’re asking ChatGPT to write Python scripts, explain SQL joins, or debug a formula, how you ask determines the quality of the response. Below is a list of prompting methodologies gleaned from my experience and the academic literature:

### How to get started:

- **Provide grounding context.** If you’re using ChatGPT or Claude, consider uploading documents (via Projects) so the model has access to relevant examples, data, or style guides. This is essentially a lightweight version of RAG (retrieval augmented generation).
- **Use structured prompts.** Frame your request with sections like: overview, examples, what to avoid, and desired output format. This helps the model reason more clearly and deliver consistent results.
- **Use delimiters to separate content.** Enclose code, sample data, or reference text in triple backticks (“ ‘) to avoid confusion and improve output formatting.
- **Lean into emotional tone when appropriate.** Language like “you’re a world-class Python tutor” or “I’m really stuck—please walk me through this like I’m new” can affect how the model prioritizes clarity and tone.
- **Learn from best practices.** [OpenAI’s guide](https://platform.openai.com/docs/guides/gpt-best-practices) and [Simon Willison’s article on prompting](https://simonwillison.net/2023/Feb/21/in-defense-of-prompt-engineering/) offer great frameworks for improving reliability and output quality.

## Final thoughts

The best marketers aren’t just creative thinkers—they’re technical enough to actually execute, too. And now, with LLMs like ChatGPT, there’s no excuse. You have a 24/7 tutor, debugger, and strategist in your pocket.

Don’t just ask AI to do things *for* you. Ask it to teach you. That’s how you build real, durable skills. So pick one of these technical skills, give yourself a weekend project, and use AI to level up.
