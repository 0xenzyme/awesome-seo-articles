---
title: "More stats and analysis of robots.txt files"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2006-02-more-stats-and-analysis-of-robotstxt"
url: "https://developers.google.com/search/blog/2006/02/more-stats-and-analysis-of-robotstxt"
canonical: "https://developers.google.com/search/blog/2006/02/more-stats-and-analysis-of-robotstxt"
author: "Vanessa Fox"
published: "2006-02-06T00:00:00+00:00"
updated: "2006-02-06T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
  - "time_sensitive_title"
fetched_at: "2026-06-14T12:44:47+00:00"
status_code: 200
html_hash: "f6b24ba47ddc9158155b9c29823bde0abc255222e8ca24295526a9ba89097d5d"
clean_word_count: 310
clean_char_count: 1849
---
# More stats and analysis of robots.txt files

Today, we released new features for Sitemaps.

## robots.txt analysis

If the site has a
[robots.txt file](https://www.robotstxt.org/wc/exclusion.html),
the new robots.txt tab
[provides Googlebot's view](https://support.google.com/webmasters/answer/6062598)
of that file, including when Googlebot last accessed it, the status it returns, and if it blocks
access to your home page. This tab also lists any syntax errors in the file.

![quick view of the analysed robots.txt file in webmaster tools](/static/search/blog/images/import/ab8f3c4d756bc049b12c980c669f4547.jpg)

You can enter a list of URLs to see if the robots.txt file allows or blocks them.

![analysis of multiple urls against the robots.txt file in webmaster tools](/static/search/blog/images/import/30a5d6d8e4266fcb6a59550596167097.jpg)

You can also test changes to your robots.txt file by entering them here and then testing them
against the Googlebot user-agent, other Google user agents, or the Robots Standard. This lets you
experiment with changes to see how they would impact the crawl of your site, as well as make sure
there are no errors in the file, before making changes to the file on your site.

If you don't have a robots.txt file, you can use this page to test a potential robots.txt file
before you add it to your site.

## More stats

Crawl stats now include the page on your site that had the highest PageRank, by month, for the
last three months.

![report of the blocked urls with the highest pagerank in webmaster tools](/static/search/blog/images/import/a3a862b4c6da5c05118ffea3ac99b6d1.gif)

Page analysis now includes a list of the most common words in your site's content and in external
links to your site. This gives you additional information about why your site might come up for
particular search queries.
