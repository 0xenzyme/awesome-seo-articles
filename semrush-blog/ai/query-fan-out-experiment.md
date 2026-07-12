---
title: "We Tested Query Fan-Out Optimization (Here's What We Learned)"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "query-fan-out-experiment"
url: "https://www.semrush.com/blog/query-fan-out-experiment/"
canonical: "https://www.semrush.com/blog/query-fan-out-experiment/"
author: "Zach Paruch, Tushar Pol, Christine Skopec"
published: "2025-09-26T10:45:00+00:00"
updated: "2025-09-26T10:45:00+00:00"
categories:
  - "AI"
freshness_reasons: []
schema_genre: "AI"
fetched_at: "2026-06-12T18:46:51+00:00"
status_code: 200
html_hash: "1a21d8298a568f870574260eefe3e8feb968e03f09fc35886407f772d4d02e67"
clean_word_count: 2359
clean_char_count: 15115
---
# We Tested Query Fan-Out Optimization (Here's What We Learned)

Ever since Google launched AI Mode, I’ve had two questions on my mind:

- How do we ensure our content gets shown in AI results?
- How do we figure out what works when AI search is still largely a mystery?

While there’s a lot of advice online, much of it is speculative at best. Everyone has hypotheses about AI optimization, but few are running actual experiments to see what works.

One idea is optimizing for [query fan-out](https://www.semrush.com/blog/query-fan-out/). Query fan-out is a process where AI systems (particularly Google AI Mode and ChatGPT search) take your original search query and break it down into multiple sub-queries, then gather information from various sources to build a comprehensive response.

This illustration perfectly depicts the query fan-out process.

![query fan-out process illustration](https://static.semrush.com/blog/uploads/media/27/58/2758a9c35c1141a428543423448661fa/f5090501d28bda7a2f8a5c0a372e386b/image.png)

The optimization strategy is simple: Identify the sub-queries around a particular topic and then make sure your page includes content targeting those queries. If you do that, you have better odds of being selected in AI answers (at least in theory).

So, I decided to run a small test to see if this actually works. I selected four articles from our blog, had them updated by a team member to address relevant fan-out queries, and tracked our AI visibility for one month.

The results? Well, they reveal some interesting insights about AI optimization.

Here are the key takeaways from our experiment:

## Key Takeaways

- **Optimizing for fan-out queries significantly increases AI citations**: In our small sample of four articles, we more than doubled citations in tracked prompts from two to five. While the absolute numbers are small given the sample size, citations were the main metric we aimed to influence, and the increase is directionally indicative of success.
- **AI citations can be unpredictable**: I checked in periodically during the month, and at one point, our citations went as high as nine before dropping back down to five. There have been [reports](https://www.linkedin.com/posts/niklas-buschner_chatgpt-dropped-90-of-citations-overnight-activity-7375561708133728256-fZ4a?) of ChatGPT drastically reducing citations for brands and publishers across the board. It just shows how quickly things can change when you're relying on AI platforms for visibility.
- **Our brand mentions dropped for tracked queries, and so did everyone else's:** Overall**,** we noticed fewer brand references appearing in AI responses to the queries we were monitoring. This affected our share of voice, brand visibility, and total mention metrics. Other brands also experienced similar drops. This appears to be a distinct issue from citation changes—more about how AI platforms handled brand mentions during our experiment period.

We’ll discuss the results of this experiment in detail later in the article. First, let me walk you through exactly how we conducted this experiment, so you can understand our methodology and potentially replicate or improve upon our approach.

## How We Ran the Query Fan-Out Experiment

Here’s how we set up and ran our experiment:

- I selected four articles from our blog
- For each selected article, I researched 10 to 20 fan-out queries
- I partnered with [Tushar Pol](https://www.semrush.com/blog/user/203456689/), a Senior Content Writer on our team, to help me execute the content changes for this experiment. He edited the content in our articles to address as many fan-out queries as possible.
- I set up tracking for the fan-out queries so we could measure before and after AI visibility. I used the Semrush [Enterprise AIO](https://www.semrush.com/lp/enterprise-aio/en/) platform for this. We were mainly interested in seeing how our content changes impacted visibility in Google's AI Mode, but our optimizations could also boost visibility on other platforms like ChatGPT Search as a side effect, so I tracked performance there as well.

Let’s take a closer look at each of these steps.

### 1. Selecting Articles

I had specific criteria in mind when selecting the articles for this experiment.

First, I wanted articles that had stable performance over the last couple of months. Traffic has been volatile lately, and testing on unstable pages would make it impossible to tell whether any changes in performance were due to our modifications or just normal fluctuations.

Second, I avoided articles that were core to our business. This was an experiment, after all. If something went wrong, I didn't want to negatively affect our visibility for critical topics.

After reviewing our content library, I found four perfect candidates:

1. [A guide on how to create a marketing calendar](https://www.semrush.com/blog/marketing-calendar/)
2. [An explainer on what subdomains are and how they work](https://www.semrush.com/blog/what-is-a-subdomain/)
3. [A comprehensive guide on Google keyword rankings](https://www.semrush.com/blog/google-keyword-ranking/)
4. [A detailed walkthrough on how to conduct technical SEO audits](https://www.semrush.com/blog/technical-seo-audit/)

### 2. Researching Fan-Out Queries

Next, I moved on to researching fan-out queries for each article.

There's currently no way to know which fan-out queries (related questions and follow-ups) Google will use when someone interacts with AI Mode, since these are generated dynamically and can vary with each search.

So, I had to rely on synthetic queries. These are AI-generated queries that approximate what Google might generate when people search in AI Mode.

I decided to use two tools to generate these queries.

First, I used [Screaming Frog](https://www.screamingfrog.co.uk/). This tool let me run a [custom script](https://github.com/metehan777/screaming-frog-query-fan-out/blob/main/screaming-frog-query-fan-out.js) against each article. The script analyzes the page content, identifies the main keyword it targets, and then performs its own version of query fan-out to suggest related queries.

![Screaming Frog dashboard with the "Query Fan-Out" column highlighted.](https://static.semrush.com/blog/uploads/media/6f/54/6f54a4f5b8708f5839241b0d876f4ad3/32d6a6d119433918859d7eee0ed43b95/image.png)

Unfortunately, the data isn’t properly visible inside Screaming Frog—everything got crammed into a single cell. So, I had to copy and paste the entire cell contents into a separate Google Sheet.

![Query fan-out data generated on Screaming Frog pasted into a Google Sheet.](https://static.semrush.com/blog/uploads/media/f9/8c/f98ca16a2d516b01eba8d7309dfdcbfe/359704abdcb9ddea556d2215e1a54426/image.png)

Now I could actually see the data.

The good thing is that the script also checks whether our content already addresses these queries. If some queries were already addressed, we could skip them. But if there were new queries, we needed to add new content for them.

Next, I used [Qforia](https://qforia.streamlit.app/), a free tool created by [Mike King](https://www.linkedin.com/in/michaelkingphilly) and his team at iPullRank.

The reason I used another tool is simple: Different tools often surface different queries. By casting a wider net, I'd have a more comprehensive list of potential fan-out queries.

Plus, if certain queries are common across both tools, that's a signal that addressing them may be important.

The way Qforia works is straightforward: Enter the article's main keyword in the given field, add a Gemini API key, select the search mode (either Google AI Mode or AI Overview), and run the analysis. The tool will generate related queries for you.

![Qforia dashboard with a query entered, search mode selected, and "Run Fan-Out" clicked which generates a list of related queries.](https://static.semrush.com/blog/uploads/media/40/66/4066ca50ad0c70e9f8e7bd98aa9ea281/e2f33cf340ec464219c47981435e9653/image.png)

After running the analysis for each article, I saved the results in the same Google Sheet.

### 3. Updating the Articles

With a spreadsheet full of fan-out queries, it was time to actually update our articles. This is where Tushar stepped in.

My instructions were simple:

Check the fan-out queries for each article and address those that weren’t already covered **and** were feasible to add. If some queries felt like they were beyond the article's scope, it was OK to skip them and move on.

I also told Tushar that including the queries verbatim wasn't always necessary. As long as we were answering the question posed by the query, the exact wording didn't matter as much. The goal was making sure our content included what readers were actually looking for.

Sometimes, addressing a query meant making small tweaks—just adding a sentence or two to existing content. Other times, it required creating entirely new sections.

For example, one of the fan-out queries for our article about doing a technical SEO audit was: "difference between technical SEO audit and on-page SEO audit."

We could’ve addressed this query in many ways, but one smart option was to make a comparison right after we define what a technical SEO audit is.

![A blog post on Semrush with a paragraph, where a fan-out query could be addressed, highlighted.](https://static.semrush.com/blog/uploads/media/35/82/358250e87a66b26491f6d4c695f4b0b2/f063d35e364c7610c662652f4c8b4938/image.png)

Sometimes, it wasn't easy (or even possible) to integrate queries naturally into the existing content. In those cases, we addressed them by creating a new FAQ section and covering multiple fan-out queries in that section.

Here’s an example:

![FAQ section on a blog post addressing multiple fan-out queries.](https://static.semrush.com/blog/uploads/media/9d/77/9d77927f72a6979a5d02d555f6946ec0/e84fe646081d170107f4bd10225f97d1/image.png)

Over the course of one week, we updated all four articles from our list. These articles didn't go through our standard editorial review process. We moved fast. But that was intentional, given this was an experiment and not a regular content update.

### 4. Setting Up Tracking

Before we pushed the updates live, I recorded each article’s current performance to establish a baseline for comparison. This way, we would be able to tell if the query fan-out optimization actually improved our AI visibility.

I used our [Enterprise AIO](https://www.semrush.com/lp/enterprise-aio/en/) platform to track the results. I created a new project in the tool and plugged in all the queries we were targeting. The tool then began measuring our current visibility in Google AI Mode and ChatGPT.

![Enterprise AIO dashboard showing a list of prompts along with "Publish Project" clicked.](https://static.semrush.com/blog/uploads/media/86/c7/86c7e53ba594cda29ad24ea98e1a90a5/c00ce805ea0850d7d956c74f753994d6/image.png)

Here’s what performance looked like at the start of this experiment:

- **Citations**: This measures how many times our pages were cited in AI responses. Initially, only two out of our four articles were getting cited at least once.
- **Total mentions**: This metric shows the ratio of queries for which our brand was directly mentioned in the AI response. That ratio was 18/33—meaning out of 33 tracked queries, we were being mentioned for 18 queries.
- **Share of voice**: This is a weighted metric that considers both brand position and mention frequency across tracked AI queries. Our score was 23.4%, which indicated we were present in some responses but not all or in the lead positions.
- **Brand visibility**: This told us what percentage of prompt responses mentioned our brand at least once, regardless of the position.

![Baseline performance metrics for a query fan-out experiment: citations, total mentions, share of voice, brand visibility.](https://static.semrush.com/blog/uploads/media/76/db/76dba9e82199e98764e1d32ce68881be/b3f5fa5d506afb99e28fb37041abb576/image.png)

I decided to wait one month before logging metrics again. Then, it was time to conclude our experiment.

## The Results: What We Learned About Query Fan-Out Optimization

The results were honestly a mixed bag.

First off, some good news: our total citations increased.

Our four articles went from being cited two times to five times—a 150% increase. For example, one of the edits we made to the technical SEO article (which we showed earlier) got used as a source in the AI response.

![The Enterprise AIO tool dashboard showing AI positions and Prompt & Response details.](https://static.semrush.com/blog/uploads/media/23/68/2368c83197e4e30423065b5e22d2b66e/3036ce10cbc47b2a31f9f2d677c68c76/image.png)

Seeing our content cited is exactly what we hoped for, so this is a win. (Despite the small sample size.)

Interestingly, our final results could’ve been more impressive if we ended our experiment earlier. At one point, we got to nine citations, but then they decreased when ChatGPT [significantly reduced citations](https://www.linkedin.com/posts/niklas-buschner_chatgpt-dropped-90-of-citations-overnight-activity-7375561708133728256-fZ4a?) for all brands.

This just shows how unpredictable AI platforms can be, and that factors completely outside your control could impact your visibility.

But what about the other metrics we tracked?

Our share of voice went down from 23.4% to 20.0%, brand visibility fell from 13.6% to 10.6%, and our brand mentions dropped from 18 to 10.

According to our data, we're not the only ones who saw declines in brand metrics. Here's a chart showing how many brands’ share of voice went down at the same time.

![Declining share of voice on AI platforms for multiple brands like Ahrefs, Semrush, HubSpot, etc.](https://static.semrush.com/blog/uploads/media/63/65/6365d88c37235c6508bbe3b7a4ba3500/927d02a1b2cc1aca35176727e1abe989/image.png)

This happened because AI platforms mentioned fewer brand names overall when generating responses to our tracked queries. This was a completely different issue from the citation fluctuations I mentioned earlier.

Considering the external factors, I believe our optimization efforts performed better than the data shows. We managed to increase our citations despite the things working against us.

So, now the question is:

## Does Query Fan-Out Optimization Work?

Based on what we learned in our experiment, I'd say yes—but with a huge asterisk.

Query fan-out optimization can help you get more citations, which is valuable. But it’s hard to drive predictable growth when things are this volatile. Keep this in mind when you’re optimizing for AI.

If you’re interested in learning more about AI SEO, keep an eye out for the new content we regularly publish on our blog. Here are some articles you should check out next:

- [How AI Search Really Works: Findings from Our AI Visibility Study](https://www.semrush.com/blog/ai-search-visibility-study-findings/)
- [What Is LLMs.txt & Should You Use It?](https://www.semrush.com/blog/llms-txt/)
- [Why Your Brand Is Your Most Important SEO Asset in 2026](https://www.semrush.com/blog/seo-branding/)
