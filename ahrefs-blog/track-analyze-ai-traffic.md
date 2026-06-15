---
title: "How to Track and Analyze Your AI Traffic"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "track-analyze-ai-traffic"
url: "https://ahrefs.com/blog/track-analyze-ai-traffic/"
canonical: "https://ahrefs.com/blog/track-analyze-ai-traffic/"
author: "Louise Linehan"
published: "2025-04-04T13:28:46+00:00"
updated: "2026-05-31T06:44:20+00:00"
categories:
  - "AI Search"
  - "General Marketing"
  - "General SEO"
freshness_reasons: []
fetched_at: "2026-06-12T12:13:32+00:00"
status_code: 200
html_hash: "ab1e22c58454f49abf93d5061e41d56d16830c62ca78020eedf13f0668d4dbdd"
clean_word_count: 2434
clean_char_count: 15044
---
# How to Track and Analyze Your AI Traffic

AI is already a pretty formidable new growth channel, driving brand interest through mentions and even direct product/service recommendations.

But its value goes beyond just awareness—AI citations can also drive engaged traffic to your site.

Like any new referral channel, AI traffic is still finding its footing. Our research shows [LLMs account for about 0.1% of traffic](https://ahrefs.com/blog/ai-traffic-research/), though this figure is likely vastly underestimated due to AI platforms [withholding referral source data](https://ahrefs.com/blog/ai-traffic-study/).

As the technology evolves and user behavior adapts, AI traffic patterns will inevitably shift even further.

Monitoring will help you stay on top of changes and make the most of any growth.

Here’s how to track your AI traffic in GA4 and [Ahrefs Web Analytics](https://ahrefs.com/web-analytics).

## Configure an AI traffic report in GA4

You can track your AI traffic in Google Analytics 4 by setting up a new **channel** and **source**.

### Track AI as a traffic channel

Good AI traffic reports should be easy to dip in and out of, and understand at a peek.

To make that happen, start by setting up a channel group.

#### 1. Find channel groups in admin

Head to Admin​ in GA4. Then, under “Data Display” ¹, select “Channel Groups” ².

Find the default channel group, then click on the three-dot menu next to it³ and choose “copy to create new”:

![Analytics interface showing how to create or manage Channel Groups in Google Analytics. A menu on the left highlights "Data display" and "Channel groups" under Property settings. A blue button allows creation of a new channel group. ](https://ahrefs.com/blog/wp-content/uploads/2025/04/word-image-186838-1.jpg)

#### 2. Create a new AI channel group and AI channel

Next, you need to:

- Name your new group “Channel group with AI”
- Click “add new channel” and call it “AI traffic”
- Set the condition “source” then select “matches regex”
- Paste this regular expression to track common AI platforms: `.*chatgpt\.com.*|.*perplexity.*|.*gemini\.google\.com.*|.*copilot\.microsoft\.com.*|.*openai\.com.*|.*claude\.ai.*|.*writesonic\.com.*|.*copy\.ai.*|.*deepseek\.com.*|.*huggingface\.co.*|.*bard\.google\.com*`

This regex will pull in traffic from ChatGPT, Perplexity AI, Google’s Gemini, and Microsoft’s Copilot, and more.

Then all that’s left to do is view your AI report.

#### 3. View your AI traffic

Head to Reports > Acquisition > Traffic Acquisition, and make sure you select “Channel group with AI” at the top of the table.

This will show you your top-level AI traffic vs. other channels.

### Track different AI traffic sources

Once you can see your top-level AI traffic, you’ll inevitably want to go deeper, to find out which AI platforms are sending it.

Here’s how to do that.

#### 1. Create a custom “AI traffic sources” segment that you can revisit

Head to the “Explore” tab, then:

- Start a new exploration
- Click the “+” icon next to “Segments”
- Click “create a new segment”
- Click on “Session segment”
- Define your segment. It should look like this:
  - Include sessions when:
  - “Traffic source”
  - “Matches regex”
- Paste the same regex you added to create your channel report:
   `.*chatgpt\.com.*|.*perplexity.*|.*gemini\.google\.com.*|.*copilot\.microsoft\.com.*|.*openai\.com.*|.*claude\.ai.*|.*writesonic\.com.*|.*copy\.ai.*|.*deepseek\.com.*|.*huggingface\.co.*|.*bard\.google\.com*`

- Name this segment “AI traffic source”
- Click “Apply”
- Your new custom segment should now be visible under “Segments” on the far left (above “Dimensions”)

Once your revisitable “AI traffic sources” are set up, it’s time to start reporting.

#### 2. View your “AI traffic sources” trended over time

To configure your report:

1. **Set dimension:** Choose “Traffic source”
2. **Set metrics:** Choose “Sessions”
3. **Set visualization:** Choose the line chart icon
4. **Set breakdown:** Choose “Session source/Medium” as the breakdown dimension
5. **Set values:** Choose “Sessions”
6. **Adjust the date range:** Choose your preferred date range
7. **Set the granularity:** Choose daily, weekly, or monthly

Or, instead of all that jiggery-pokery and manual configuration, you can just view a pre-built report in [Ahrefs Web Analytics](https://ahrefs.com/web-analytics)…

## Track your own AI traffic with Ahrefs Web Analytics

[Ahrefs Web Analytics](https://ahrefs.com/web-analytics) is a privacy-friendly Google Analytics alternative.

Here are three ways it compares with GA4:

- **Easier:** In seconds, Web Analytics gives you access to fully configured reports (e.g. top channels, sources, pages, regions, devices) that would take much longer to build in GA4.
- **Faster:** Google Analytics delays visitor data by 24-48 hours. [Ahrefs Web Analytics](https://ahrefs.com/web-analytics) shows events within 1 minute, giving you real-time visitor insights.
- **Lighter:** Google Tag Manager weighs ≈98kb and can grow with updates. Our script stays under 2kb, ensuring your site remains fast and efficient.

Once you’ve added a snippet of code to your site, viewing your AI traffic in [Ahrefs Web Analytics](https://ahrefs.com/web-analytics) is as easy as clicking a button.

Here’s a quick video of how you can set that up.

Now let’s get into some deep-dive AI traffic analysis.

For the rest of this article, we’ll be focusing on different [Ahrefs Web Analytics](https://ahrefs.com/web-analytics) reports and use cases.

## Benchmark your AI traffic against other channels

In AI platforms, the exact same question can be met with hundreds of different responses. Your brand could be cited in one of those answers, and then never again.

With that kind of volatility, tracking a small number of visits from AI can sometimes send you on a wild goose chase. It’s often better to look out for top-level patterns and trends in your AI traffic data, so you know when your brand is being consistently referenced.

To see a bird’s-eye view of your AI traffic, head to the “Overview” report in Ahrefs Web Analytics, make sure you’ve selected the “channels” tab under “traffic sources”¹. Then, select “view more” to bring up a full channel report².

This report will let you compare channel trends, and work out what percentage of your total traffic comes from AI.

In this case, our Ahrefs-owned Wordcount site receives <0.1% of its total traffic from AI, which, as we already mentioned, sits in line with the industry average.

In this same report, you can study behavior metrics (e.g. bounce rate or visit duration) to see whether your AI traffic is outperforming other channels.

From there, apply an LLM channel filter to your “Overview” report to isolate your AI traffic.

This will help you monitor growth more closely, and discover the sources/pages behind traffic spikes.

### Work out how much of your strategy to dedicate to AI

Benchmarking your AI traffic alongside other acquisition channels can give you a better idea of its strategic value.

For example, if AI accounts for just 0.1% of your total sessions, but shows consistent month-over-month growth, it might be worthy of some low-lift investment—like optimizing popular pages for AI visibility.

Similarly, if your AI traffic is already rivaling your social or referral traffic, you can justify tracking, testing, and allocating budget in the same way you would do for those channels.

Ultimately, evaluating AI traffic trends against other channels can help you make a judgment call on how much time and money to invest in AI.

### Assess the top-level impact of AI brand awareness campaigns

Track AI traffic data to measure whether your brand visibility campaigns—like media coverage or influencer partnerships—are successfully driving visitors to your site.

Just note down traffic numbers before, during, and after your campaign to gauge success.

For example, let’s say you actively tried to boost visibility of your product’s “SEO features” in AI, with a PR campaign in the month of September.

Now imagine AI referral traffic to your “SEO feature” page played out like this:

- **August:** 500 visitors
- **September:** 2,300 visitors
- **October:** 1,800 visitors

This demonstrates a 360% traffic spike during your campaign month, and 260% sustained growth thereafter.

Based on this data, you can reasonably assume your campaign increased AI visibility and drove more traffic to your site.

While it isn’t an exact science, a sharp uptick in AI traffic surrounding a brand push can give you directional insight into your campaign reach and impact.

Use it alongside other data points, like AI mentions in [Ahrefs Brand Radar](https://ahrefs.com/brand-radar) (below), to build a fuller picture of your AI awareness during your AI campaign window.

## Find your top AI traffic sources

Now you know a bit more about your top-level AI traffic, find out which specific AI platform sends you the most traffic.

Just set an “LLM”¹ channel filter (this should already be on if you followed the previous step), click the “sources” tab under the “traffic sources” component², then hit the “view more” button to draw up a full report³.

In this report, you’ll be able to see which AI platforms send you the most visits and engagement, and track how that traffic trends and changes over time.

Looking at the example above, you can see that our Wordcount site originally received the majority of its AI traffic from Gemini.

Now, it earns more visits from ChatGPT.

That flip is even more apparent when you switch to a “relative” view of traffic contribution.

### Unpick differences in AI referral traffic by source

Different AI systems interact with content in different ways.

By checking your traffic analytics, you might be able to spot patterns and subtle differences in how certain platforms refer traffic to your site.

For instance, some platforms may cite detailed technical content, while others might prefer clear, structured data or short explanations. These aren’t hard rules—just clues you can use to experiment.

Try small tests based on what you see. If a certain type of content attracts more AI-driven traffic, think about creating more of it, or updating other pages to better match what seems to work.

Treat this as an ongoing learning process. AI behavior changes over time, so staying flexible and curious will serve you better than sticking to a fixed strategy.

## Find your top AI traffic content

Find out which specific pieces of content are gaining popularity on AI platforms in the “Pages” report.

From your “overview” dashboard:

1. Set an “LLM” channel filter
2. Select “top pages” underneath the Pages component
3. Click “view more” to draw up the full Pages report

The “Pages” report not only shows you your most visited pages from AI—it also helps you understand how engagement and user behavior differs for each piece of content, with metrics like views, bounce rate, and time on page.

For example, we can see that the Argentinian version of our paraphrasing tool is a favorite of AI visitors.

But our Indonesian homepage achieves the lowest bounce rate, and the longest visit duration.

In this report, you can also find out more about typical AI customer journeys, with data on the top pages, entry pages, and exit pages.

### Expand popular content formats and reverse engineer positive user behavior

Look for patterns in the content that AI platforms are surfacing: do AI visitors prefer products, definitions, how-to guides, or localized landing pages?

Double down on the content that’s already getting traction. For example, if certain reviews are doing well, scale that format by reviewing similarly aligned products and services.

Matching popular formats might just give you a better chance of being cited in LLMs.

At this point, it’s also worth paying attention to user behavior.

If you notice that a page gets modest traffic from AI, but users are particularly engaged once they’re there, think about the micro improvements you can make to that page to drive up visibility—like [optimizing for speed](https://searchengineland.com/ai-optimization-how-to-optimize-your-content-for-ai-search-and-agents-451287#:~:text=crawling%20your%20site-,Optimize%20for%20speed,-Return%20content%20as).

Once you’ve experimented, feed all of your findings into internal brand and content guidelines, to standardize what “AI-friendly” content looks like, and give your team a repeatable playbook for LLM visibility.

### Test how quickly your content gets picked up by AI, with hourly tracking

AI platforms can surface and cite new content surprisingly quickly. If you need to boost your brand visibility fast, then AI can make for a good channel.

Using Ahrefs Web Analytics’ real-time reporting, you can monitor AI traffic changes hour-by-hour after publishing.

For instance, in January this year, I posted an article on the [fastest growing companies](https://ahrefs.com/blog/fastest-growing-companies-and-startups/) to the blog at 8.52am.

Going by Web Analytics data, the first AI visit we received came in at 2pm later that day.

This kind of analysis can help you test out which content types and tactics drive quick-turnaround AI visibility—especially useful for reactive campaigns, building brand visibility alongside developing news, or just refreshing to check your blog post stats after it goes live (guilty!).

## Learn more about your AI audience

AI traffic data can tell you a lot about your audience. Use Ahrefs Web Analytics to find out where they are and how they’re reaching your site.

### Location and usage insights

From your dashboard, make sure you’ve got your “LLM” channel filter on, then scroll down to the bottom of your report to the “geography” component.

This data will show you which continent, country, or city your AI audience is visiting from, and what language they speak.

Next to that report, you’ll see the “browser & systems” component. This shows you which browsers, operating systems, and devices your AI audience are using.

To get really granular, you can also add additional “source” or “page” filters, to see how audience locations, browsers, and systems change based on AI platform or content.

## Wrapping up

AI is changing how people discover and interact with online content. The question isn’t whether AI traffic matters—it’s how you can make it work for you.

By tracking it properly, you can figure out which AI platforms are sending visitors to your site, zero-in on how those visitors behave, then optimize your content in response.

Whether you’re using GA4 or Ahrefs Web Analytics, you need to make sure you track your AI traffic consistently. Start reporting now to see which pieces of content earn you the most engagement, then use those insights to develop your marketing strategy.

Don’t wait for AI traffic to pick up before you start tracking it—get ahead of the market and your competition. There’s probably already some great opportunities hiding in your analytics data.
