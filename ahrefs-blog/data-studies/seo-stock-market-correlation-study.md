---
title: "Are Stock Prices and Organic Traffic Correlated? I Analyzed 2,000 Public Companies to Find Out"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "seo-stock-market-correlation-study"
url: "https://ahrefs.com/blog/seo-stock-market-correlation-study/"
canonical: "https://ahrefs.com/blog/seo-stock-market-correlation-study/"
author: "Mateusz Makosiewicz"
published: "2025-02-19T16:02:46+00:00"
updated: "2025-03-17T11:08:27+00:00"
categories:
  - "Data & Studies"
freshness_reasons:
  - "news_or_research"
fetched_at: "2026-06-12T12:08:28+00:00"
status_code: 200
html_hash: "30f21d7cfe32af9237b609def742757b4b2884a55ceab8e2231a2ef34ac2393c"
clean_word_count: 3239
clean_char_count: 20345
---
# Are Stock Prices and Organic Traffic Correlated? I Analyzed 2,000 Public Companies to Find Out

SEO and the stock market — two completely different worlds. Yet when you run a correlation analysis between organic traffic and stock price on, say, Nasdaq, you suddenly get a strong positive correlation.

Here’s why that happens and what it means.

## Key takeaways

1. The combined stock prices typically rose along with the total organic traffic they received. Our research showed a strong positive relationship between the market cap weighted standardized price and the total traffic of all Nasdaq stocks used in the study.
2. 32% of Nasdaq companies with at least 100k annual traffic have a moderate or strong positive correlation between organic traffic and stock price.
3. SEO may directly increase the stock value of companies that invest in it. Positive effects may be more likely in industries that already show a stronger SEO-stock link such as consumer products, healthcare, finance, and real estate.
4. SEO is a great way to take advantage of the “entity” edge and any public relations efforts.
5. Publicly traded companies don’t necessarily need specialized strategies to attract organic traffic. After analyzing about 200 of the highest-traffic sites, most were simply applying typical SEO best practices.
6. Researchers say that investors can profit from the organic traffic and stock market correlation. They can also avoid losses this way.

Please note: correlation does not imply causation and past performance is not indicative of future results. This article is for informational purposes only and does not constitute investment advice.

## Methodology

I used [Ahrefs](https://docs.ahrefs.com/docs/api/reference/introduction) API and [Polygon’s](https://polygon.io/docs/stocks/getting-started) APIs to get the stock monthly closing price, monthly market cap, and monthly traffic for each month from 2021-11-01 to 2024-10-01.

Based on monthly close price and organic traffic I calculated the Spearman correlation for each ticker listed on Nasdaq.

To calculate the percentage of positively correlated tickers and market cap weighted data, we used one ticker per company and only the tickers with 36 rows of data (full 3 years). Hence, the difference between the number of tickers on Nasdaq and the number of tickers used for research. Big thanks to our data scientist [Xibeijia Guan](https://www.linkedin.com/in/xibeijia-guan/) for the idea and running the analysis!

To find out how positively correlated companies get traffic and links, I selected about 200 sites that have at least one million estimated visits per year.

## Positive stock market correlations and their causes

The analysis revealed a strong correlation between the total traffic and the value of the Nasdaq. This was supported by both the Spearman correlation of 0.680 and the Pearson correlation of 0.727, which are both typically considered strong correlations. The correlation was also visually apparent as you can see below.

![Nasdaq's organic traffic and price correlation. Weighted standarized price and sum traffic over time. ](https://ahrefs.com/blog/wp-content/uploads/2025/01/organic-traffic-nasdaq-prices-correlation.png)

To clarify the chart, here’s a breakdown of the methodology. Weighted standardized price is calculated in three steps:

1. **Standardization**: each ticker’s stock price is standardized on a scale of 0 to 1 to remove price scale variations between tickers, ensuring a fair comparison regardless of their original price levels.
2. **Weighting**: the standardized prices are then weighted by their respective monthly market cap.
3. **Summation**: the weighted standardized prices are summed to produce the final value.

However, this doesn’t imply that *all* Nasdaq listed companies have a positive correlation. The overall positive correlation of the stock market is influenced by the impact of websites with higher traffic. When examined more closely, the ratio of negative to positive correlations is almost equal — see the chart below.

Because publicly listed companies have access to many channels besides organic traffic, I expected to see many negative correlations. So, to me, the most interesting finding was that 32% of companies showed a moderate to strong correlation, which is a substantial correlation easily seen in examples like Makemytrip.

It’s not solely their SEO strategies at work here. Many companies benefit from existing demand that originates elsewhere: PR, offline advertising or word, mouth, etc.

To illustrate, here’s how interest in Soundhound’s stock (likely caused by Nvidia’s investment and partnership) impacted search volumes and organic traffic to their site simultaneously — there is likely no SEO magic there.

However, for high-traffic sites that consistently invest in SEO (e.g. Makemytrip, Airbnb, Wix) the connection between organic traffic and stock value becomes stronger. Companies like that typically have a higher non-branded-to-branded traffic ratio, just like the one below.

In these cases, SEO can have both a direct and indirect impact on stock value. The direct impact comes from attracting customers and increasing revenue, while the indirect impact is from increased brand awareness. Over time, this heightened brand awareness results in more branded search queries and improved search result rankings.

## Tech, health care, finance and consumer companies may have a stronger SEO-stock link

Market sectors from positively correlated companies may show a greater propensity to boost market valuation through SEO. Here are the sectors of the companies with the highest traffic with their percentage distribution in the dataset.

If you’ve been around the SEO block a few times, this list probably doesn’t shock you.

Many of these sectors share a common thread: customers frequently begin their purchase or research journey through Google. Whether it’s finding a mortgage lender, shopping for consumer products, or searching for medical information, high-intent searches can directly impact revenue.

That said, not all industries will see a significant SEO-stock price connection.

For businesses in deeply B2B niches or highly regulated sectors — where contracts are negotiated offline or through long lead cycles — organic traffic may be less predictive of market movements. The same goes for companies where everyone already knows their brand or they’ve got strong offline connections (like those making super specialized stuff).

## Entity SEO gives public brands a rankings edge

Many public companies seem to enjoy what I call the entity SEO edge. My theory is that publicly traded companies often have a natural head start in Google’s search results, thanks to the extensive online footprint that accompanies their “entity” status — mentions in financial news, investor portals, press releases, and other authoritative sources.

This visibility amplifies their overall domain authority, causing Google to more easily associate them with certain topics or services. That’s what gives them an *edge* over less-established brands when it comes to SEO.

For instance, Kelly ranks for “temp services near me” without ever using that exact phrase, and Robinhood ranks for “buy stocks” even though that phrase isn’t anywhere on the homepage.

Flexshopper has the same advantage. They rank for “rent to own,” even though those exact words don’t appear on their landing pages.

Nvidia ranks immediately and has no problems staying in the top 10 with a glossary page on generative AI.

It appears that Google’s understanding of entities goes beyond keyword matching; it may look at site context, user behavior, and external references. For instance, Google may get some of its authority signals from anchor texts in the links.

Further reading

- [SEO Benefits of Going Public (A Unique Study)](https://ahrefs.com/blog/seo-benefits-of-going-public/)

This brings us to the next point.

## PR without SEO is a missed opportunity

Not using link equity generated by PR is a missed opportunity to generate more online visibility through SEO and possibly increase brand value.

It’s like being a celebrity and not endorsing any brands. Or starting your own brand.

Media coverage, press releases, awards, and relationships with journalists often lead to [backlinks](https://ahrefs.com/blog/what-are-backlinks/) from trusted websites. Just look at Soundhound’s newsroom referring domain growth. “Regular people” usually don’t wander there but journalists do.

Backlinks from “regular” PR can help improve search rankings and bring more visitors to the company’s site because, as we know, search engines see them as a sign of credibility.

For instance, quite a few Nasdaq companies are on the Forbes 500 list, each with a link back to the homepage.

The fact alone that you’ve been included in the ranking is an opportunity to grab some more links.

Offering quotes for journalists is a known link building tactic and it’s even more effective when you represent a well-known brand. Your established reputation increases the likelihood that journalists will choose your information over the countless other sources they consider.

In other words, SEO is a way to make online visibility work even harder.

## Public traded companies don’t need unique SEO tactics

I checked out more than 200 Nasdaq sites with at least around 1M yearly organic visits, and it turns out publicly traded companies don’t need a totally different SEO playbook.

Lots of the same tactics that smaller businesses use to drive major traffic still get the job done. Let me show you some examples.

### Blogs still drive serious traffic

For example, Monday.com.com’s blog brings over a quarter of the entire traffic.

And here’s Cyberark with 24k monthly visits from a single blog post.

In general, Nasdaq companies stick to topics directly related to their core offerings, using their domain authority to outrank smaller competitors easily.

And so, Freshpet blogs about how the best spots to pet a dog or cat; 2.3K estimated monthly visits.

Nvidia blogs about new tech, recently mostly AI. Here’s a nice example of a high-traffic, high-backlink blog post.

Blogging also proves to be a great way to earn authoritative [backlinks](https://ahrefs.com/blog/what-are-backlinks/). For example, Carecloud’s blog is reputable enough that Healthline cites it as a source.

### Landing pages capture big (and small) demand

From deep product pages to sophisticated [topic clusters](https://ahrefs.com/blog/topic-clusters/), public companies craft landing pages for every type of search.

One of the best examples I’ve seen comes from Electronic Arts: they share real NFL player stats to help promote Madden NFL 25. It’s a clever twist on content marketing, blending authentic sports data with game promotion.

But examples like EA’s are few and far between. Most of the time, companies stick to tried-and-true strategies and simply execute them really well.

For instance, I came across quite a few topic clusters in my research. One stood out in particular: a single product-focused cluster that was pulling in nearly 37% of the site’s overall traffic.

Another thing I saw quite often was optimized clusters showing the site’s inventory. For example, when people look for “flights to Chicago”, they’ll likely find United’s landing page displaying their flight options — 29.3k estimated visits each month.

Makemytrip put together a collection of search-optimized landing pages, each offering different travel ideas based on how people search for their trips.

This helps them cover a wide range of queries resulting in an estimated 2.5M visits each month.

Airbnb uses a similar approach. Their topic clusters cater to searchers looking for specific types of accommodations, such as cabins, treehouses, glamping, and more.

Product landing pages with an informational twist are a common tactic among Nasdaq companies. They seamlessly blend product marketing with content marketing by introducing their offerings within educational content. The structure of this page says it all:

This tactic helped Micron rank twice for the same, high-volume keyword (“ddr5”).

Lastly, Matterport uses its own technology to create engaging [SEO content](https://ahrefs.com/seo/seo-content). They maintain a gallery of famous places captured with their cameras, which are typically used to produce 3D real estate tours. That is quite brilliant.

Matterport’s gallery also welcomes user-generated content, which helps them cover even more keywords. This approach brings in over 45,000 visits each month. Here are some of the search queries they rank for to showcase their product:

### Dictionaries, FAQs, and basic definitions = surprising traffic

I was genuinely surprised by this. Many public companies are leveraging good ‘ol dictionaries, and FAQs to effectively capture informational [search intent](https://ahrefs.com/blog/search-intent/) and boost their organic traffic.

Some of the examples I found and their results put together in Ahrefs’ Batch Analysis.

And it’s often quite a significant portion of these sites’ traffic. For instance, Crowdstrike generates 33% traffic through a cluster about cybersecurity basics.

Qualcomm added over 18% traffic worth 68k with one landing page.

Why this “boring” type of content? It’s how Google understands the search intent behind these keywords. It means that at least for now, tackling a keyword like “enterprise cloud” with a purely product-oriented has a lower chance of ranking.

### Free tools and resources pull in links and leads

Offering a useful resource — even if it’s just a re-packaged version of existing data — earns brands credibility, backlinks, and engaged visitors.

For example, Better makes it easy for people searching for a loan to find them by offering tools to help calculate and understand their options.

SoFi gets thousands of links and visits each month regularly publishing average US salaries.

And it’s not even original data.

Baker Hughes has published a weekly census of the number of drilling rigs actively exploring for or developing oil and natural gas in the United States and Canada… since the 1970s.

Adobe has more free tools than any company I’ve ever seen. They carve out high-demand features of premium products and publish them on optimized landing pages as free tools (with limited usage).

For instance, the background remover generates an estimated 2.9M visits each month promoting their Express tool suite.

Converting PDF to Word and vice verse could easily be one tool. But not if you’re creating landing pages for two separate keywords — you need two separate tools.

Here’s another awesome example: Newegg created a PC builder tool that attracts people searching for custom computers and recommends products from its own inventory. They even use AI for it.

Instacart follows this strategy, too. Their ideas directory attracts an estimated 448k visits each month and contributes 11.2% of the overall traffic. It offers things like metric converters, calculators, and even a list of different types of milk.

### Indexing dynamic search results for the most popular keywords

Indexing dynamic search results in SEO refers to getting search engines to crawl and index pages on your website that are generated in response to user queries. These pages are created “on the fly” based on the specific keywords or filters users enter into your site’s search function.

A great example of this in action is Adobe. They effectively rank for time-sensitive terms like “happy new year 2024.” As the season approaches, Adobe can capitalize on the surge in searches, tapping into 206,000 searches in the US and 2.2 million globally.

The secret is to have the pages listed on your site map.

Etsy employs a similar strategy. By leveraging user-generated content, they’re able to target and rank for millions of non-branded keywords, consistently securing top 10 positions in search results.

### Low-volume keywords can be hidden gems

Even in a bigger company, targeting niche, low-volume keywords can attract highly qualified leads and contribute to business growth, proving their value despite their lower search volume.

For example, the keyword “mass payouts” only gets around 100 visits each month in the US, but those searches are likely from businesses that are seriously interested. I found two Nasdaq companies competing for that low-volume keyword.

Another example: Beacon optimizes for the long tail to catch demand for high ticket sales.

### Local SEO on a national scale

Several companies with a national reach are tapping into local SEO tactics — Texas Roadhouse and Potbelly are great examples. But the standout here is DoorDash and its clever “near me” strategy.

We’ve detailed how this page works in the teardown video below. At that time, the “restaurants near me” page alone received an estimated 9.1 million visits per month and a staggering traffic value of $41.6 million.

https://youtu.be/Ag\_-pPtJpuI?si=vQxQHxGHN5MVcY9F&t=1

## Investors can profit (or avoid losses) on the market using SEO data

And this is not only my opinion. Third-party studies have shown that you can use branded search volume and the sentiment behind it to invest in the stock market. On SciSpace alone I found 10 papers on the topic.

I also found two papers where the authors actually outperformed the market using search data.

This is from [A Study on the Relationship between Internet Search Trends and Company’s Stock Price and Trading Volume](https://www.researchgate.net/publication/281706386_A_Study_on_the_Relationship_between_Internet_Search_Trends_and_Company%27s_Stock_Price_and_Trading_Volume):

> (…)we propose several generalized linear models for forecasting the probability of positive or negative directional movements, and propose a trade strategy from the generated forecasts, resulting in a 40% outperformance of a traditional buy-and-hold strategy in our testing period.

The other is from [Forecasting stock market movements using Google Trend searches](https://link.springer.com/article/10.1007/s00181-019-01725-1):

> Our search trend investment strategy has outperformed average stock market returns in both KOSPI and KOSDAQ markets during the seven-year study period (2007~2013).

I haven’t tried that strategy, but I wouldn’t be too surprised if it worked just as it says on tin. I’ve personally used organic traffic data to get nearly 21% ROI in a month on NRDS stock. I bought a tiny bit of stock just for kicks, to test out a hypothesis that their value will bounce back as soon as their traffic starts to bounce back. Well, I wish I had bought more.

In some cases, changes in organic traffic, especially non-branded, might precede changes in stock value, suggesting that SEO data could potentially serve as a leading indicator for investors.

Example: NerdWallet. First, its traffic fell, then the stock. Hypothetically, you could open Ahrefs before the company’s Q2 earnings call, see that traffic has been declining for months, and avoid being dragged through a sell-off.

## Final thoughts

There was a time were SEO was the underdog’s game. Small businesses with tiny budgets could snag tons of free traffic, and the playing field was level because the big guys weren’t paying attention to what seemed like “nerdy” tricks. That’s how SEO got famous.

Then, some bigger brands caught on, hopped on the bandwagon, and realized they had a built-in advantage on Google.

That is, until Google shook things up with its recent crackdown on site reputation abuse and its “helpful content” update. In theory, Google aims to promote a sense of parity for independent creators (relatively small sites), making both Google and SEO appealing again for smaller players, while serving as a warning and creating a sour note for larger brands.

But I think SEO is still a goldmine for publicly traded companies — and the bigger, the better. These big companies don’t need to reinvent the wheel. They can use the same SEO strategies as smaller companies and still have a massive head start. It’s kind of ironic.

Got questions or comments? Drop me a line on [LinkedIn](https://www.linkedin.com/posts/mateusz-makosiewicz_does-anyone-here-do-seo-for-real-estate-activity-7247168218237157376-jLA1).
