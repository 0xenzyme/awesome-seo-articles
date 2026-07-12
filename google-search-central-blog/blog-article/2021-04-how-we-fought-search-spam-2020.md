---
title: "How we fought Search spam on Google in 2020"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2021-04-how-we-fought-search-spam-2020"
url: "https://developers.google.com/search/blog/2021/04/how-we-fought-search-spam-2020"
canonical: "https://developers.google.com/search/blog/2021/04/how-we-fought-search-spam-2020"
author: "Cody Kwok, Principal Engineer"
published: "2021-04-29T00:00:00+00:00"
updated: "2021-04-29T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2021_very_old"
  - "news_or_research"
  - "title_year_2020_before_2026"
fetched_at: "2026-06-14T13:38:45+00:00"
status_code: 200
html_hash: "cddc85b88e46f0e100e2e46e18ff4d86fae9785e9a99dcfecf107399dfe87700"
clean_word_count: 1357
clean_char_count: 8432
---
# How we fought Search spam on Google in 2020

![Googlebot and spider friend are reading the 2020 webspam report](/static/search/blog/images/webspamreport2020/WebspamReport2020_1.png)

Google Search is a powerful tool to help you find useful information on the open web. Unfortunately, not all web pages are created with good intent. Many of them are explicitly created to deceive people, and that is something we fight against every day. To ensure your safety and protect your search experience against disruptive content and malicious behaviors, Search has invested in many innovations in 2020.

## Fighting spam smarter

While we have been [fighting spam](https://www.youtube.com/watch?v=oJixNEmrwFU) since the early days of Search, recent advances in Artificial Intelligence (AI) offer unprecedented potential to revolutionize our approach.

By combining our deep knowledge of spam with AI, last year we were able to build our very own spam-fighting AI that is incredibly effective at catching both known and new spam trends. For example, we have reduced sites with auto-generated and scraped content by more than 80% compared to a couple of years ago.

Hacked spam was still rampant in 2020 as the number of vulnerable web sites remained quite large, although we have improved our detection capability by more than 50% and [removed most of the hacked spam from search results](https://www.youtube.com/watch?v=TnhKznlJfTM).

This is a problem that we cannot solve alone. Even if we could detect and protect against all spam, the hackers would not cease exploiting loopholes until they’re all closed. Website owners can protect their sites by practicing good security hygiene: it is easier to prevent a site from getting hacked than to recover from a hack. Google offers resources to help you understand [the most common ways websites get hacked](/web/fundamentals/security/hacked/top_ways_websites_get_hacked_by_spammers) and how to [use Search Console](/web/fundamentals/security/hacked/use_search_console) to check [whether your site got hacked](/web/fundamentals/security/hacked). Please do take a look and let's keep the web safer together!

With major events last year, including a global pandemic, we have devoted significant effort in extending protection to the billions of searches we received on such important topics. If you're looking for a COVID testing site near you, you shouldn't have to worry about landing on gibberish spam that may redirect you to phishing sites. Besides eliminating spam content, we worked with several other Search teams to make sure you receive the most up-to-date and highest quality information when and where it matters the most.

## Preventing spam from reaching you

Before we deliver a set of search results on Google, [there's a lot that happens behind the scenes](https://www.google.com/search/howsearchworks/). Every day, we're discovering, crawling, and indexing billions of web pages. Among those pages is a lot of spam—every day, we discover 40 billion spammy pages. Here’s how we work to keep that spam from getting in the way of your search for helpful, useful information.

![how we defend against spam at every step](/static/search/blog/images/webspamreport2020/WebspamReport2020_EverySteps.png)

This diagram conceptualizes how we defend against spam.

First, we have systems that can detect spam when we crawl pages or other content. Crawling is when our automatic systems visit content and consider it for inclusion in the index we use to provide search results. Some content detected as spam isn't added to the index.

These systems also work for content we discover through sitemaps and [Search Console](https://search.google.com/search-console/about). For example, Search Console has a [Request Indexing](/search/docs/crawling-indexing/ask-google-to-recrawl) feature so creators can let us know about new pages that should be added quickly. We observed spammers hacking into vulnerable sites, pretending to be the owners of these sites, verifying themselves in the Search Console and using the tool to ask Google to crawl and index the many spammy pages they created. Using AI, we were able to pinpoint suspicious verifications and prevented spam URLs from getting into our index this way.

Next, we have systems that analyze the content that is included in our index. When you issue a search, they work to double-check if the content that matches might be spam. If so, that content won’t appear in the top search results. We also use this information to better improve our systems to prevent such spam from being included in the index at all.

The result is that very little spam actually makes it into the top results anyone sees for a search, thanks to our automated systems that are aided by AI. We estimated that these automated systems help keep more than 99% of visits from Search completely without spam. As for the tiny percentage left, our teams take [manual action](https://support.google.com/webmasters/answer/9044175) and use the learnings from that to further improve our automated systems.

## Protecting you beyond spam

![Googlebot and friend protecting you beyond spam](/static/search/blog/images/webspamreport2020/WebspamReport2020_2.png)

Beyond spam, we expanded our effort in 2020 to protect you against other types of abuse. Many of these can cause significant financial and personal harm.

In 2020, we made significant progress in improving our coverage and protecting more users against online scams and fraud. Online scams have many shapes and they can negatively affect you in more ways than traditional webspam. For example, many scammers pretend to be offering customer support phone numbers to popular services and products, only to trick users who call in into paying them via bank transfers or gift cards. Commonly known as 'customer support scam' or 'tech support scam', this type of scam has been reported by [hundreds of thousands of users](https://www.ftc.gov/system/files/documents/reports/consumer-sentinel-network-data-book-2020/csn_annual_data_book_2020.pdf) where users may lose [hundreds of dollars](https://www.ftc.gov/news-events/blogs/data-spotlight/2019/03/older-adults-hardest-hit-tech-support-scams) to scammers in each case.

![example of customer support scam on search results](/static/search/blog/images/webspamreport2020/WebspamReport2020_ScamExample.png)

Since 2018, our systems have been able to protect hundreds of millions of searches a year by detecting potentially scammy sites. On the web, scammers attempted to create many low quality websites with keyword stuffing, logos of brands they're imitating, and a phone number they want you to call. Our algorithmic solutions made sure that scam and fraud are very unlikely to show up in your search results. This is but one of the several types of protections we have launched last year to ensure the quality of search results and your safety. Our mission is to get ahead of the challenges to provide you with the most trustworthy results. At the same time, you can also better protect yourself by staying informed and [learning about scams](https://blog.google/technology/safety-security/scam-spotter/).

Another dimension where advances in AI helped tremendously was in understanding content of sites. An example of this can be found in how we helped improve [the way we rank product review, informational, and shopping sites](/search/blog/2021/04/product-reviews-update). Google Search is a great way to research and find products before you make a purchase, and we wanted to make sure that you’re getting the most useful information for your next purchase by rewarding content that has more in-depth research and useful information.

In spite of the significant advancements we made in our spam-fighting efforts, spammers are highly motivated to develop new techniques that can evade our detection. We're always working to get better and protect people from new types of abuse, and external reports can help. Do you have any recent experiences with Search where you feel misled, scammed, or spammed, and you think we can do a better job with preventing those experiences? If so, please share feedback using the [spam report](/search/docs/advanced/guidelines/report-spam), along with the query and any other information that might be useful.

![Googlebot working with you to fight spam](/static/search/blog/images/webspamreport2020/WebspamReport2020_3.png)
