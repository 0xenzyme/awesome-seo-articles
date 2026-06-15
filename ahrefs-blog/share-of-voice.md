---
title: "What Is Share of Voice? How to Measure It Across Channels"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "share-of-voice"
url: "https://ahrefs.com/blog/share-of-voice/"
canonical: "https://ahrefs.com/blog/share-of-voice/"
author: "Michal Pecánek"
published: "2020-08-13T16:00:11+00:00"
updated: "2023-10-04T11:28:30+00:00"
categories:
  - "General Marketing"
  - "General SEO"
freshness_reasons:
  - "date_2023_aging"
fetched_at: "2026-06-12T12:09:40+00:00"
status_code: 200
html_hash: "14f04f158f27ad16c8d2decf0a056ad8ba07adb8d823acc6b21e9d676855f4ac"
clean_word_count: 2042
clean_char_count: 12198
---
# What Is Share of Voice? How to Measure It Across Channels

Share of voice (SOV) is traditionally a measure of your advertising share compared to competitors. However, with most brands now fighting for visibility on organic channels like social and search, we can broaden that definition to how visible your brand is in the market.

The formula to calculate share of voice is:

> SOV = Brand visibility value / Total market visibility value

… where the ‘visibility value’ depends on the most suitable metric for the channel you’re measuring.

In this guide, you’ll learn why SOV is one of the most essential marketing KPIs and how to measure it in today’s complex omnichannel marketing world.

- [Why is SOV important?](#why-sov-is-important)
- [How to measure SOV in organic search](#measuring-sov-organic-search)
- [How to measure SOV for Google Ads](#measuring-sov-google-ads)
- [How to measure SOV for social](#measuring-sov-social-media)
- [How to measure SOV for mass media channels](#measuring-sov-mass-media)

## Why is SOV important?

There is [a strong relationship](https://hbr.org/1990/01/ad-spending-maintaining-market-share) between SOV and market share. If you have 17% SOV, you can also expect your market share to head towards 17%.

That said, you should strive for a higher SOV than market share. This is known as excess share of voice (eSOV), and it’s a key long-term driver responsible for increasing your market share.

Let me highlight the word “long-term” because reaching the equilibrium doesn’t happen overnight. It’s realistic to [expect a 0.7% annual growth](https://business.linkedin.com/content/dam/me/business/en-us/amp/marketing-solutions/images/lms-b2b-institute/pdf/LIN_B2B-Marketing-Report-Digital.pdf) rate in market share for every ten eSOV percentage points. It may not seem much, but those decimal points may be worth millions in your industry.

However, keep in mind that spending more on communications doesn’t necessarily mean creating eSOV. It’s about increasing your SOV relative to competitors.

Lidl in the UK is a stellar example of SOV theory becoming a reality. Back in 2013, they had approximately 3% market share and SOV. From 2014, they began increasing their media coverage and [doubled their market share](https://www.theguardian.com/business/2019/aug/20/lidl-attains-biggest-uk-market-share) in just five years.

Watch this video for more details:

But there’s more you need to know…

Researchers have discovered that small brands have to overspend to maintain their market share, whereas bigger brands can get away with an SOV lower than their market share and still stand their ground. That’s why the curve on the graph isn’t linear.

Why does this happen? It boils down to the [fact](http://data2decisions.com/wp-content/uploads/2016/05/Top-10-Drivers-of-Advertising-Profitability.pdf) that the bigger your brand is, the more efficiently your marketing dollars are spent.

That said, your business likely isn’t competing with the big brands through primetime TV ads yet. And unlike the big brands, you probably don’t have a team of analysts and researchers on your payroll to keep you updated about your overall SOV.

Luckily, you can still measure SOV for smaller pieces of the cake and use that as a KPI. We’re going to focus on doing precisely that across various marketing channels below.

## How to measure SOV in organic search

Organic search is the biggest traffic source for a lot of businesses, including us:

While the number above might be impressive, it tells us nothing about SOV. To calculate that, use one of these two methods:

### 1. Overall organic traffic compared to competitors

First, make a list of your competitors’ domains. We’ll be using only direct business competitors because there’s always going to be blogs and other websites popping up in the top results. These may get significant traffic in your industry, but they don’t own any market share.

Next, paste you and your competitors’ domains into [Ahrefs’ Batch Analysis](https://ahrefs.com/batch-analysis) to see each site’s estimated organic traffic and the number of keywords they rank for.

Export the data and get rid of anything other than the Target, Keywords, and Traffic columns.

Then, create two new columns for keyword and traffic shares.

Enter this formula in row one of the first new column: `=iferror(arrayformula(if(row(B$1:B)=1,"Keyword share",if(B1:B="","",B1:B/sum($B$2:B)))))`

And this formula in the first row of the second new column: `=iferror(arrayformula(if(row(C$1:C)=1,"Traffic share",if(C1:C="","",C1:C/sum($C$2:C)))))`

Sidenote.

Here’s [an example sheet](https://docs.google.com/spreadsheets/d/1XlF2HYqRf2Kbfsp4CvANSqdVEzs2im6nGeHq8SlL9D8/copy) with cells with formulas highlighted green.

Now comes the drawback of this quick method. The broader the target audience of a given website, the more keywords and traffic opportunities there is.

That means websites with abnormally high keyword shares probably target a wider audience. On top of that, some sites rank for high-volume keywords with virtually no value for their business. Those can skew the data quite a bit.

For example, one ‘competitor’ of ours gets a lot of organic traffic to a Spanish blog post explaining what a CEO is.

Although that pumps up their SOV when using this method, the blog post has pretty much zero ‘business value’ and is unlikely to attract any customers.

In conclusion, take these numbers with a grain of salt.

We’ll move onto a method that eliminates these drawbacks and inaccuracies to a certain degree.

### 2. Tracking a representative sample of your industry keywords

The only way to avoid the differences between websites’ target audiences is to choose the keywords you want to consider traffic from.

The best approach here is to take your [keyword research](https://ahrefs.com/seo/keyword-research) master sheet, paste all main keywords into [Rank Tracker](https://ahrefs.com/rank-tracker/), add your competitors’ domains, and check the visibility in the **Competitors overview** tab:

The visibility metric shows the percentage of all clicks from your tracked keywords that land on the respective website.

Just a couple of quick notes when doing this:

First, you only want to track the main keywords. That’s the “fat head” keyword that gets the most clicks for a topic. Keyword research master sheets often contain tens of thousands of keywords, and you only want to work with the most representative sample here. This sample will include keywords that you’re already targeting with content and those you’re yet to target.

Second, always exclude yours and your competitors’ branded keywords.

Once you’ve done that, just copy and paste the keywords into [Rank Tracker](https://ahrefs.com/rank-tracker/). If you have a location-specific business, make sure to track the right locations in this step. I’m only going after our biggest market here: the United States.

You should also tag the keyword list so you can filter the SOV keywords later on:

Hit “Add keywords,” and you should see the **Overview** report. If you’re already tracking other keywords, you’ll need to filter the “SOV keywords” using the tag:

The **Overview** report is useful for tracking your progress, but you’ll need to switch to the **Competitors overview** tab to see how you stack up against your competitors.

You can see our visibility comparison here:

For a percentage representation, head to the **Traffic share** report to see how the pie is split between you and the tracked competitors:

Just keep in mind that this is only one channel, and the proportions above don’t correspond to overall SOV or market shares. The relationship between SOV, market share, and advertising effectiveness only works when looking at SOV across all channels.

## How to measure SOV for Google Ads

We’re going to take a different route here and go after impression share instead. That’s because it’s the only metric suitable for SOV tracking offered by Google Ads, which will always be more accurate than metrics from third-party tools.

Impression share (IS) represents the percentage of times your ads were shown out of the total impressions it could have received based on your targeting.

Search Keywords report from Google Ads. You’ll find the Search impression share metric under ‘Competitive metrics’ when you modify the columns of the default report.

Regardless of how valuable this metric is for PPC specialists, there’s still one drawback we need to keep in mind for SOV tracking. It’s the “based on your ads targeting” part. To give an extreme example, let’s say you’re targeting just one exact-match keyword in a small geographical area. Doing that makes it easy to achieve 100% IS with an optimized bid, ad, and landing page.

That said, such a PPC objective could be something like “increase IS from 54% to 70% in the UK among potential keyword research tool buyers by the end of the year.”

## How to measure SOV for social media

First of all, we’re focusing on organic channels only. With paid social ads, you can see metrics such as ad frequency, reach, impressions, and estimated audience size, but there’s no way to compare them to the competition. That makes it impossible to create any viable paid social SOV tracking.

Luckily, organic social SOV measurements are quite straightforward. It’s all about keeping track of all your and your competitors’ brand mentions.

While there are plenty of [social media monitoring tools for this](https://www.g2.com/categories/social-media-monitoring), I only have experience with Brand24. However, the concept should work across the board. You monitor keywords (brand names) across selected social media channels, and the tool shows you the number of mentions over a specific period. If it doesn’t show SOV, just compare your brand mentions to the overall market mentions.

The following screenshot shows how that might look. In this case, we’re filtering for mentions of Ahrefs on Twitter. To get SOV, you’d just divide our brand mentions by the overall number of brand mentions in the category. So, if you see overall 500 mentions of three brands that you’re tracking, and 133 of those mentions belong to your brand, your SOV is 26.6%:

I’m not leaving this without a “but,” though.

As you know, social media is rife with bots, so keep in mind that quite a lot of brand mentions won’t be coming from a real person. To correct for that, you’ll have to adjust the monitoring by applying some filters based on what your social monitoring platform offers.

## How to measure SOV for mass media channels

I’m sure you get the gist now. We can go on and on in terms of marketing channels, so I’ll just end this with mass marketing channels that gave birth to SOV.

The essential mass media metric for channels like TV or radio is Gross Rating Points (GRP). Not only is it suitable for measuring SOV, it’s also often used as a pricing unit to quote campaign costs.

GRP is calculated by multiplying audience reach by exposure frequency during a specific period. If your ad airs five times with 12% reach and three times with 15% reach, your GRP is 60 + 45 = 105.

All serious media houses have and will share the metrics that you need. I wish I could add some personal experience here, but I’ve only run print ads. All I can say is that we predominantly “digital” marketers can learn a lot from looking at the bigger picture.

## Final thoughts

SOV tracking allows you to set marketing goals for eSOV, which is crucial for increasing market share. Just keep in mind that measurement is one thing, and taking action is another.

Achieving eSOV is a whole different topic. You need to focus on eSOV for short-term sales activation and long-term brand building channels. The mix of channels you use to achieve that should be derived from your marketing strategy. Watch these [two](https://www.youtube.com/watch?v=2LkK-UdbMuM) [videos](https://vimeo.com/373969781) to learn more about [marketing strategies](https://ahrefs.com/blog/small-business-marketing-strategies/) and advertising effectiveness from the best.

Got any questions or comments? Ping me on [Twitter](https://twitter.com/michalpecanek).
