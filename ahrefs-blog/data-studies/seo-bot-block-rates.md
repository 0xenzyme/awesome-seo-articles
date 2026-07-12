---
title: "The SEO Bots That ~140 Million Websites Block the Most"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "seo-bot-block-rates"
url: "https://ahrefs.com/blog/seo-bot-block-rates/"
canonical: "https://ahrefs.com/blog/seo-bot-block-rates/"
author: "Patrick Stox"
published: "2025-05-22T09:30:00+00:00"
updated: "2025-05-25T17:33:19+00:00"
categories:
  - "Data & Studies"
freshness_reasons:
  - "news_or_research"
fetched_at: "2026-06-12T12:02:51+00:00"
status_code: 200
html_hash: "8dbcce33f76d55db18d410e33d74587733f0d61973815e62c60ec1e1064494d1"
clean_word_count: 1001
clean_char_count: 6452
---
# The SEO Bots That ~140 Million Websites Block the Most

Ever wonder which SEO bots are the most blocked? This can impact the quality of the data the tools provide.

Blocking these bots will mostly impact the link index of the tools. They won’t be able to crawl the pages, so they can’t check where those pages are linking. It doesn’t matter for traffic estimates, keyword rankings, top pages, etc. Those are built from different data sources.

For Ahrefs, it would also impact the internal links we show and the page history feature that shows changes to your pages over time, which you might need at some point. Ahrefsbot also powers the index for our search engine, [Yep.com](https://yep.com/), so blocking Ahrefsbot means you wouldn’t show in Yep’s search results.

We looked at ~140 million websites to see how often SEO bots were blocked. I want to give a huge thanks to our data scientist [Xibeijia Guan](https://sg.linkedin.com/in/xibeijia-guan) for pulling this data.

## Key takeaways

Here are the top 3 most blocked SEO bots:

1. **MJ12bot (Majestic)**. Blocked by 6.49% of all websites.
2. **SemrushBot**. Blocked by 6.34% of all websites.
3. **AhrefsBot**. Blocked by 6.31% of all websites.

## How often are SEO bots blocked?

We looked at the total number of websites blocking the bots. There are many ways to block bots with robots.txt, and this accounts for all of them including:

- **Explicit blocks**, where the bot is mentioned and disallowed
- **General blocks**, where all bots may be blocked
- Any instances where a directive **allowed the bot**, after blocking all bots

Caveats: this doesn’t include any other block types such as firewalls or IP blocks. It is also Ahrefs view of the web, which means if we’re blocked by one of these methods, we may not see the robots.txt files at all.

As I mentioned earlier, the most blocked bot is MJ12bot from Majestic. I suspect there are a few reasons for this.

1. They’re a distributed crawler, meaning you can’t look up or block them by IPs, which makes them less trusted and also more likely to be blocked by user agent.
2. They’ve been crawling the web for longer.
3. They have a smaller user base than more popular SEO tools and therefore less leverage to remove any blocks.

Here are the most blocked SEO bots:

![SEO bots block rate](https://ahrefs.com/blog/wp-content/uploads/2025/05/seo-bots-block-rate.jpg)

And the total websites blocking SEO bots:

Here’s the data:

| Bot Name | Count | Percentage % | Bot Operator |
| --- | --- | --- | --- |
| MJ12bot | 9081205 | 6.49 | Majestic |
| SemrushBot | 8868486 | 6.34 | Semrush |
| AhrefsBot | 8831316 | 6.31 | Ahrefs |
| dotbot | 8569766 | 6.13 | Moz |
| BLEXBot | 8374216 | 5.99 | SEO PowerSuite |
| serpstatbot | 7878935 | 5.63 | Serpstat |
| DataForSeoBot | 7872939 | 5.63 | DataForSEO |
| SemrushBot-CT | 7855400 | 5.62 | Semrush |
| Barkrowler | 7804425 | 5.58 | Babbar |
| SemrushBot-BA | 7796785 | 5.57 | Semrush |
| SemrushBot-SWA | 7789812 | 5.57 | Semrush |
| SemrushBot-SI | 7789062 | 5.57 | Semrush |
| SEOkicks | 7758904 | 5.55 | SEOkicks |
| Screaming Frog SEO Spider | 7711108 | 5.51 | Screaming Frog |
| linkdexbot | 7704425 | 5.51 | LinkDex |
| DomainStatsBot | 7696944 | 5.5 | Domainstats |
| ZoomBot | 7669495 | 5.48 | SEOZoom |
| SiteCheckerBotCrawler | 7666545 | 5.48 | Sitechecker |
| Cocolyzebot | 7666233 | 5.48 | Cocolyze |
| SeobilityBot | 7664228 | 5.48 | Seobility |
| SenutoBot | 7655145 | 5.47 | Senuto |
| hypestat | 7648671 | 5.47 | HypeStat |
| online-webceo-bot | 7648444 | 5.47 | WebCEO |
| BrightEdge Crawler | 7648139 | 5.47 | BrightEdge |
| SEOlizer | 7648112 | 5.47 | SEOLizer |

It gets a little more complicated to analyze. For the above, we looked at the main robots.txt file for a website, but every subdomain can have their own set of instructions. If we look at the ~461M robots.txt in total, then the most blocked SEO bot is SemrushBot at 5.76%. Here are the top 5:

1. **SemrushBot**: 5.76%
2. **Dotbot (Moz)**: 5.34%
3. **MJ12bot (Majestic)**: 4.96%
4. **BLEXBot**: 4.88%
5. **Ahrefsbot**: 4.67%

## How often are SEO bots specifically targeted

For this measure, we’re looking only at cases where a particular bot is disallowed. It does not include any overall disallow statements or cases where only certain bots may be allowed. In these cases, website owners went out of their way to specifically block certain bots.

Majestic’s bot is the most targeted, followed by Moz’s bot.

Here are the most blocked SEO bots by explicit mentions:

Here are the number of websites explicitly blocking SEO bots:

Here’s the data:

| Bot Name | Count | Percentage % | Bot Operator |
| --- | --- | --- | --- |
| MJ12bot | 2000372 | 1.43 | Majestic |
| dotbot | 1402305 | 1 | Moz |
| AhrefsBot | 1350771 | 0.97 | Ahrefs |
| SemrushBot | 1285857 | 0.92 | Semrush |
| BLEXBot | 861184 | 0.62 | SEO PowerSuite |
| serpstatbot | 354683 | 0.25 | Serpstat |
| DataForSeoBot | 284694 | 0.2 | DataForSEO |
| Barkrowler | 276332 | 0.2 | Babbar |
| SEOkicks | 219961 | 0.16 | SEOkicks |
| SemrushBot-CT | 211895 | 0.15 | Semrush |
| linkdexbot | 166405 | 0.12 | Linkdex |
| DomainStatsBot | 157053 | 0.11 | Domainstats |
| SemrushBot-BA | 154349 | 0.11 | Semrush |
| SemrushBot-SI | 147999 | 0.11 | Semrush |
| SemrushBot-SWA | 146261 | 0.1 | Semrush |
| ZoomBot | 125310 | 0.09 | SEOZoom |
| SiteCheckerBotCrawler | 122574 | 0.09 | Sitechecker |
| Cocolyzebot | 121737 | 0.09 | Cocolyze |
| SeobilityBot | 117558 | 0.08 | Seobility |
| Screaming Frog SEO Spider | 87673 | 0.06 | Screaming Frog |
| SenutoBot | 54978 | 0.04 | Senuto |
| hypestat | 861 | 0 | HypeStat |
| SenutoBot | 54978 | 0.04 | Senuto |
| hypestat | 861 | 0 | HypeStat |
| online-webceo-bot | 659 | 0 | WebCEO |
| BrightEdge Crawler | 289 | 0 | BrightEdge |
| SEOlizer | 253 | 0 | SEOLizer |

## SEO bot blocks over time by DR

We looked at the top 1M sites by DR, which aligns to sites with a DR >45. Semrush is the most blocked followed by Majestic and Moz.

## SEO bot blocks over time by domain category

Here’s how it breaks down for each individual bot in different categories of websites. The top 3 are:

1. **Autos\_and\_Vehicles:** 39%
2. **Books\_and\_Literature:** 27%
3. **Real\_Estate:** 17%

## Which bots crawl the fastest?

Going by the bot requests in [Cloudflare Radar](https://radar.cloudflare.com/), Ahrefs is by far the fastest crawler in the SEO space. ~4.6x faster than Moz and ~6.7x faster than Semrush.
