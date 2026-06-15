---
title: "How we fought spam on Google Search in 2022"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2023-04-webspam-report-2022"
url: "https://developers.google.com/search/blog/2023/04/webspam-report-2022"
canonical: "https://developers.google.com/search/blog/2023/04/webspam-report-2022"
author: "Duy Nguyen"
published: "2023-04-11T00:00:00+00:00"
updated: "2023-04-11T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2023_aging"
  - "news_or_research"
  - "title_year_2022_before_2026"
fetched_at: "2026-06-14T13:41:59+00:00"
status_code: 200
html_hash: "d616a98c17961714132d39d6b6f08093cd27048f774e28f0cab1c8c219910224"
clean_word_count: 593
clean_char_count: 3831
---
# How we fought spam on Google Search in 2022

![googlebot and crawly explaining how we fought spam on Google Search in 2022](/static/search/blog/images/webspamreport2022/webspam-report-2022-blog.png)

Every day, we're discovering, indexing, and serving billions of web pages, and a significant portion of pages we discover are spam. In 2022 we launched multiple updates to our systems to thwart these attacks and ensure a spam-free experience for all Search users.

## Improvements to SpamBrain

[SpamBrain](/search/blog/2022/04/webspam-report-2021#spambrain:-our-most-effective-solution-against-spam) is central to our spam-fighting efforts and we made many improvements in 2022 to improve coverage. SpamBrain detected 5 times more spam sites compared to 2021 and 200 times compared to when it first launched. Thanks to SpamBrain, we were able to make sure that more than 99% of visits from Search are spam-free.

### Tackling abusive links and hacked spam

We also improved SpamBrain as a robust and versatile platform, launching multiple solutions to improve our coverage of different abuse types. One such example was link spam. As we [shared in December](/search/blog/2022/12/december-22-link-spam-update), we trained SpamBrain to detect sites building spammy links, as well as sites created to pass spammy links to other sites. Thanks to SpamBrain's learning capability, we detected 50 times more link spam sites compared to the [previous link spam update](/search/blog/2021/07/link-tagging-and-link-spam-update). Similarly, our efforts to teach SpamBrain more about hacked spam resulted in a 10 times improvement in hacked site detection.

### Faster spam handling

SpamBrain was also a big factor in better detecting spam at [crawling time](/search/docs/fundamentals/how-search-works#crawling). This means we can better identify spam when we first visit a page and not index it at all, allowing our resources to be better used to index helpful pages.

## Extending user safety

Beyond spam, we also rolled out new anti-scam solutions to improve user safety on Search. These new solutions improved coverage and extended our scam protections to all languages for the first time. Compared to 2021, we reduced clicks on scam sites by 50%.

### Refreshed guidelines for site owners

In addition to fighting spam, we updated our [spam policies](/search/docs/essentials/spam-policies) as part of our [Search Essentials](/search/blog/2022/10/search-essentials). These spam policies cover the most common types of spam and abusive behaviors, and could lead to a site ranking lower or not appearing at all in Search results. We updated our spam policies with more relevant and precise language, and included new examples that help site owners avoid creating harmful content.

We also recognized that there's a lot of interest in AI-generated and AI-assisted content, and published [guidance on AI-generated content](/search/blog/2023/02/google-search-and-ai-content). We hope this guidance is useful in explaining how AI and automation can be a useful tool to create helpful content, but if AI is used for the primary purpose of manipulating search rankings, that's a violation of our long-standing policy against [spammy automatically-generated content](/search/docs/essentials/spam-policies#scaled-content).

We're constantly working to detect and nullify spam so that users can find the most useful content through Search. We can't do this alone; thank you for creating helpful content and functional websites for users, as well as giving us feedback and insightful reports on spam and abuse. If you come across spammy content or manipulative behaviors, please [report them to us](https://support.google.com/websearch/answer/3338405) or visit the [Search Central help community](https://support.google.com/webmasters/community).
