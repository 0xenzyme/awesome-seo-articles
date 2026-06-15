---
title: "How to Track, Measure, and Boost AI Referral Traffic"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "ai-referral-traffic"
url: "https://www.semrush.com/blog/ai-referral-traffic/"
canonical: "https://www.semrush.com/blog/ai-referral-traffic/"
author: "Carlos Silva, Christine Skopec"
published: "2025-09-02T12:34:00+00:00"
updated: "2025-09-02T12:34:00+00:00"
categories:
  - "AI"
freshness_reasons: []
schema_genre: "AI"
fetched_at: "2026-06-12T13:34:45+00:00"
status_code: 200
html_hash: "80750252687085bc7bd402150762d3cfe5cd391548bfacde4a35e597ab23eda8"
clean_word_count: 2420
clean_char_count: 16617
---
# How to Track, Measure, and Boost AI Referral Traffic

## What Is AI Referral Traffic?

AI referral traffic refers to website visits that come from links cited in AI-generated responses from platforms like ChatGPT, Perplexity, Claude, and Google's AI Overviews.

If a user clicks a link in a large language model tool (LLM) like one of those shown below to visit your site, that's AI referral traffic.

![AI Mode on Google with the website links used in its response appearing on the right-hand side.](https://static.semrush.com/blog/uploads/media/10/4c/104c2998cb27160bb98632893fa178ff/e2f748b2bf044f12002f18cfdd8890e0/image.png)

## Why Does AI Referral Traffic Matter?

AI referral traffic matters because our research suggests that AI search visitors will [surpass traditional search visitors](https://www.semrush.com/blog/ai-search-seo-traffic-study/) by 2028. And tracking your AI referral traffic can help you uncover opportunities to stay ahead of competitors.

![Projected annual visitors by source from 2025 to 2029 for traditional organic search vs LLMs.](https://static.semrush.com/blog/uploads/media/14/ff/14ff98c501dd4f84da912565798a3fa1/c2b5e1aed214f7f7259a2f96eb692925/image.png)

The catch?

Many AI clicks show up as "direct" traffic in Google Analytics 4 (GA4) because AI platforms don't always pass referrer information. This means you're likely getting more AI traffic than your reports show.

![Sessions by session source report on GA4 with the "direct" traffic row highlighted.](https://static.semrush.com/blog/uploads/media/37/f9/37f937b7775ff384e0248eaefcff3c3b/e4e252f047e7dfd5ed8ec5c5d5cd2bce/image.png)

But there **is** a way to more accurately track AI referral traffic. A few ways, actually.

## Which AI Platforms Send the Most Traffic?

We analyzed the world’s five largest websites in July 2025 (youtube.com, wikipedia.org, reddit.com, instagram.com, and facebook.com) based on [Semrush data](https://www.semrush.com/trending-websites/global/all/) and found ChatGPT is the platform that sends the most traffic to those sites. Followed by Gemini, Perplexity, CoPilot, and Grok.

![AI platforms ranked by how much search traffic they send: ChatGPT, Gemini, Perplexity, CoPilot, and Grok.](https://static.semrush.com/blog/uploads/media/dc/ff/dcff0d7fabfe38967b6c9c050967e85e/966422a0d77876d7ca71c8a7f4e2f745/image.png)

We also used Semrush’s [Traffic Analytics](https://www.semrush.com/analytics/traffic/traffic-overview/) tool to find that ChatGPT has the largest traffic share out of 10 major AI platforms based on July 2025 traffic data.

|  |  |  |
| --- | --- | --- |
| **AT Platform** | **July 2025 Visits** | **Traffic Share %** |
| chatgpt.com | 5,244,855,278 | 85.79% |
| gemini.google.com | 287,535,861 | 4.70% |
| perplexity.ai | 173,581,751 | 2.84% |
| grok.com | 153,011,519 | 2.50% |
| claude.ai | 136,577,834 | 2.23% |
| copilot.microsoft.com | 97,802,733 | 1.60% |
| meta.ai | 16,599,298 | 0.27% |
| yiyan.baidu.com | 3,327,311 | 0.05% |
| deepseek.ai | 243,299 | 0.00% |
| brave.com/leo/ | 55,803 | 0.00% |

So, optimizing content for ChatGPT might be a good place to start.

However, we recommend checking your competition to see which platforms send them the most traffic. Then, optimize your content for those platforms. To try to win some of your competitors’ traffic.

## How to Track AI Referral Traffic

Setting up custom reports, setting up custom groups, and using a dedicated AI tracking tool helps you track AI traffic (like ChatGPT referrals), so you get accurate data to analyze.

[Celia Harding](https://www.linkedin.com/in/celiaharding/) is the founder of Leoprd, an agency that specializes in building recognition in LLMs. She says:

> *Use GA4 to see if you're getting any traffic from AI models or if you're being overlooked entirely. Then uncover your share of models versus your competitors.*

Here's how to do that:

### Set Up Regex Filters in GA4

Using regular expression or “regex” patterns (sequences of characters that define search patterns) to create a custom filter can help you accurately monitor AI referral traffic.

In Google Analytics 4 (GA4), go to “**Reports**” > “**Acquisition**” > “**Traffic acquisition**.”

Click “**Add filter +**” and fill out the filter like this:

- **Dimension**: Session source/medium
- **Match Type**: matches regex
- **Value**: .\*(chatgpt\.com|openai\.com|perplexity\.ai|claude\.ai|gemini\.google\.com|bard\.google\.com|you\.com|search\.brave\.com|copilot\.microsoft\.com).\*

![Adding a regex filter of GA4 by customizing the dimension, match type, and value.](https://static.semrush.com/blog/uploads/media/22/0c/220ca8e542529fddc08d2bd6a0bac380/12c23a165cf1319184f891ac29123d9e/image.png)

Click “**Apply**.”

This regex catches traffic from major AI platforms like ChatGPT, Perplexity, Claude, etc. (You can adjust the regex to display other LLMs if needed.)

And you can see which pages LLMs are sending traffic to by clicking “**+**” > “**Landing page + query string**.”

![GA4 report with the regex filter applied to show all major AI platforms like ChatGPT, Perplexity, etc.](https://static.semrush.com/blog/uploads/media/2f/da/2fda682e56da9e8cab39c8da31ac0c7b/a464fd0089f21a49de22899d6cb84e2b/image.png)

### Create Custom AI Traffic Channel Groups in GA4

Setting up a dedicated AI channel group lets you analyze AI performance alongside organic search, social media, and paid channels. And you can use it across reports.

In GA4, navigate to “**Admin,**”find the **“**Data display**”** section, select“**Channel groups**,” and either select your default channel group or your own custom group.

Name your group something like “Channel group with AI.” Then click “**Add new channel**.”

!["Create new channel group" window on GA4 with a group name entered and "Add new channel" clicked.](https://static.semrush.com/blog/uploads/media/c8/47/c847ac9ff16bf0c08dbbad7a43bf3412/d1ed2067637f385bdd9d82fb2a00a1f1/image.png)

Name the channel group "AI Referral Traffic" and click “**+ Add condition group**.”

Select “**Source**,” then “**matches regex**” and enter

**Source matches regex**: .\*(chatgpt\.com|openai\.com|perplexity\.ai|claude\.ai|gemini\.google\.com|bard\.google\.com|you\.com|search\.brave\.com|copilot\.microsoft\.com).\*

Click “**Save channel**” and then click “**Save group**.”

!["Create new channel" window on GA4 with a channel name & channel conditions entered and "Save channel" clicked.](https://static.semrush.com/blog/uploads/media/53/b0/53b0e10829920b39e16c53d2bcf2726c/ec0a586a9c38171d3c318674a28ea665/image.png)

To view this filter, head to “**Reports**” > “**Acquisition**” > “**Traffic acquisition**.” Select your channel with the drop-down.

![Navigating to the session channel group with AI on the Traffic acquisition report on GA4.](https://static.semrush.com/blog/uploads/media/8c/1f/8c1fc45772653f172635884eb42e773a/cdf511312877ff2bcc7980c9cf645186/image.png)

Now you can compare AI traffic against other traffic sources.

![The "AI Referral Traffic" highlighted to see how it compares against other traffic sources.](https://static.semrush.com/blog/uploads/media/93/2b/932bb7a32b21825456aba0c37f1c400c/df8f733cfcd929a247ca34ee85b54188/image.png)

### Use Semrush’s AI Traffic Dashboard

Semrush’s [AI Traffic](https://www.semrush.com/analytics/traffic/ai-traffic/) dashboard lets you analyze AI referral traffic to your domain and competing domains, so you can see how you compare to your rivals.

Start by entering your domain and up to four competitors. Click “**Analyze**.”

![AI Traffic tool start with two competing domains entered and "Analyze" clicked.](https://static.semrush.com/blog/uploads/media/52/c1/52c1696e7dd5d91d9f808495b1ce1fab/4c552387d08ebcc4bbd4bce5f9f6004e/image.png)

You’ll see data for all specified sites. Like how traffic flows from different LLMs to the selected domain.

![AI Traffic report on Semrush showing the percentage of traffic each inputted site gets from LLMs.](https://static.semrush.com/blog/uploads/media/2f/80/2f8099ff3f943d3b8718ffc214230ef0/2968209b677d986a03932e16874ddbc0/image.png)

And the “All Sources” section highlights how many visits each domain received from a specified LLM compared to the others. Simply hover over the traffic-split bar to see the breakdown.

!["All Sources" on the AI Traffic report showing how many visits each domain received from different LLMs.](https://static.semrush.com/blog/uploads/media/7a/81/7a81d131b9c02aae389b309e30ec712f/33d7d39bb572f1af07b79263e1d4b12c/image.png)

## How to Increase AI Referral Traffic to Your Website

Getting AI platforms to cite your content is called [generative engine optimization](https://www.semrush.com/blog/generative-engine-optimization/) (GEO), and it’s similar to traditional SEO but with added emphasis toward technical performance and answer-focused content formats.

Here’s what to focus on:

### Optimize Page Speed

Ensure your webpages load quickly, so AI bots can crawl (find and read) more of your pages and boost their chances of appearing in AI-generated responses.

Target these benchmarks for [Core Web Vital](https://www.semrush.com/blog/core-web-vitals/) (metrics that outline the usability of your site):

- **Largest Contentful Paint (LCP)**: The time it takes for the biggest element on the screen—like an image or video—to fully show up after someone first opens the page
- **Interaction to Next Paint (INP)**: The delay between when a user clicks, taps, or types and when the page visually responds
- **Cumulative Layout Shift (CLS)**: How much the content jumps around while the page loads—for example, when buttons or images suddenly shift position

Running your priority pages through Google’s [PageSpeed Insights](https://pagespeed.web.dev/) tool can give you an idea of their current performance.

![The Core Web Vitals Assessment report for a domain on Google’s PageSpeed Insights.](https://static.semrush.com/blog/uploads/media/aa/90/aa90ab468fb00883e200cefa4141129a/2ed64ff39fb626b2b6041a0db987e753/image.png)

Scroll down to the “Insights” and “Diagnostics” sections to see a list of elements you can fix to improve your [Core Web Vitals](https://www.semrush.com/blog/core-web-vitals/).

!["Insights" and "Diagnostics" showing a list of elements a site can fix to improve their core web vitals and site speed.](https://static.semrush.com/blog/uploads/media/13/96/13962b4b5d4f2b2220cfee61f613eaf3/9dd554690cc907b6fcacec4dc22a445b/image.png)

Some fixes are simple. For example, you can improve image delivery by reducing image file sizes.

A modification like minimizing JavaScript might require a developer’s help. But it’s worth doing, especially when you consider that JavaScript-heavy pages can be difficult for LLMs to render.

### Target Conversational Search Queries

Target questions people ask naturally (e.g., "how do I cook a brisket as fast as possible?") instead of keyword fragments (e.g., “cook brisket fast”).

AI systems often pull direct answers from content that clearly poses questions and provides immediate responses.

Format your content with:

- Questions as subheadings that mirror how people actually speak
- Natural language and varied terminology rather than keyword-stuffed phrases
- Direct answers immediately after each question and supporting details that expand on the core answer.

![A question as a subheading and a direct answer using natural language as the response to increase citation likelihood on LLMs.](https://static.semrush.com/blog/uploads/media/dc/53/dc530019a9a694554b6e7f7092f7ffa7/1b173d3ac5d75b73c373f56cafee5161/image.png)

This approach creates content chunks that AI platforms can easily extract and attribute to your site.

You can find question-based keywords by reviewing the People Also Ask boxes in Google search results.

![Google SERP with a search term entered and the "People also ask" section highlighted.](https://static.semrush.com/blog/uploads/media/f3/7b/f37b0ff0a7bf201f6118e983f47feae9/a689cc7afcffd55330bf7f5d60bbb6d8/image.png)

Semrush [Keyword Magic Tool](https://www.semrush.com/analytics/keywordmagic/) can also give you numerous question ideas based on a single term. Open the tool and enter a seed keyword (a broad term related to your niche) and click “**Questions**” for keyword ideas.

![Keyword Magic Tool report with the "Questions" filter applied showing question-based keyword ideas for AEO.](https://static.semrush.com/blog/uploads/media/6f/1b/6f1bf021be36651cd8fa270ad166e56e/8882ede282b79e4380f69c124a1bf645/image.png)

### Build Authority Signals

Brand mentions may not give you direct referral traffic, but they can broadly improve your visibility in LLMs to help you build brand awareness.

A study by [Leoprd](https://www.leoprd.io/post/leo-report-2025-reputation-to-revenue-building-trust-authority-and-visibility-in-and-ai-era) found 61.9% of citations that mention a brand come from editorial coverage, awards, and reviews—not from content the brand itself publishes.

And organic mentions on forums like Reddit might help your brand earn more mentions within LLMs.

You can strengthen your authority with:

- Original research or data studies that other sites reference
- Industry mentions in respected publications and expert roundups
- Consistent brand presence across platforms that links back to your main site
- [Building backlinks](https://www.semrush.com/blog/link-building/) and mentions from high-authority sites

The goal is establishing your content as a primary source that other experts reference and cite. Which signals to AI platforms that you're an authoritative voice in your field.

### Implement Schema Markup

[Schema markup](https://www.semrush.com/blog/schema-markup/) (code you add to your website to help crawlers understand its content) helps AI platforms better understand your content, which enables LLMs to cite your site when relevant.

For example, the below review has schema markup that displays information like a star rating, the reviewer's name, and a list of pros and cons.

![A SERP listing with schema markup that displays a star rating, the reviewer's name, and a list of pros and cons.](https://static.semrush.com/blog/uploads/media/56/e3/56e3b2ac6b1a846bf32df178035bbda6/b15e11686579d9fe5f7bd128dc0bc970/image.png)

Consider adding these schema types to your pages where relevant:

- Article schema for blog posts and guides
- FAQ schema for question-answer sections
- Organization schema for company information and credentials for pages like the “About Us” page
- Author schema for author information and expertise
- Product schema for reviews and recommendations

### Create Original and Useful Content

LLMs want to highlight content that highlights genuine expertise and creating original content might improve your chances of getting mentions in LLMs.

Build original content by:

- Including examples and practical applications
- Adding supporting data and research findings from research you conduct
- Including personal opinions from experts in your organization (like your CEO)
- Sharing real-world examples from customers of how people are using your product

### Regularly Refresh Your Content

AI platforms favor recent, up-to-date content, which means keeping your content fresh could boost your visibility in LLMs.

Keep content current by:

- Updating statistics and data points regularly
- Adding new examples and case studies
- Refreshing screenshots and interface references
- Including recent developments in your industry
- Adding publication dates and "last updated" timestamps

Set a schedule to review and refresh your most important content. How frequently you do this will depend on the type of content, your industry, and other factors.

## Start Capturing Your AI Referral Traffic Today

As more people turn to AI to answer their questions, you can stay ahead of your competitors by tracking your AI referral traffic and optimizing for different AI platforms.

Here's your action plan:

1. **Set up tracking first.** Create the GA4 regex filter and custom channel group we covered to start seeing your actual AI traffic volume. You can't optimize what you can't measure.
2. **See which AI platforms send your competitors the most traffic**. This gives you an idea of which platforms you might want to optimize for first.
3. **Audit your most important pages for the technical basics**—page speed under two seconds, clear question-answer formatting, and proper schema markup. Focus on your top five pages that already get traffic from AI platforms.

Want to see which AI platforms send your competitors the most traffic?

Try Semrush today.
