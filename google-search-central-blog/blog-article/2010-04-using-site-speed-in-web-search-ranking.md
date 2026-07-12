---
title: "Using site speed in web search ranking"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2010-04-using-site-speed-in-web-search-ranking"
url: "https://developers.google.com/search/blog/2010/04/using-site-speed-in-web-search-ranking"
canonical: "https://developers.google.com/search/blog/2010/04/using-site-speed-in-web-search-ranking"
author: "Amit Singhal, Google Fellow and Matt Cutts, Principal Engineer, Google Search Quality Team"
published: "2010-04-09T00:00:00+00:00"
updated: "2010-04-09T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:06:08+00:00"
status_code: 200
html_hash: "8c9dac57abb00464a181a91f7296bbec0909550a629a0149d6c5347dd3b1d64d"
clean_word_count: 472
clean_char_count: 2929
---
# Using site speed in web search ranking

You may have heard that here at Google we're obsessed with speed, in
[our products](https://www.google.com/chrome/intl/en/more/speed)
and
[on the web](https://googleblog.blogspot.com/search/label/faster%20web).
As part of that effort, today we're including a new signal in our search ranking algorithms: site
speed. Site speed reflects how quickly a website responds to web requests.

Speeding up websites is important—not just to site owners, but to all Internet users. Faster
sites create happy users and we've seen in our
[internal studies](https://googleresearch.blogspot.com/2009/06/speed-matters)
that when a site responds slowly, visitors spend less time there. But faster sites don't just
improve user experience; recent data shows that improving site speed also
[reduces operating costs](https://radar.oreilly.com/2009/07/velocity-making-your-site-fast).
Like us, our users place a lot of value in speed—that's why we've decided to take site speed
into account in our search rankings. We use a variety of sources to determine the speed of a site
relative to other sites.

If you are a site owner, webmaster or a web author, here are some tools that you can use to
evaluate the speed of your site:

- [Page Speed](https://code.google.com/speed/page-speed/), an open
  source Firefox/Firebug add-on that evaluates the performance of web pages and gives suggestions
  for improvement.
- [YSlow](https://developer.yahoo.com/yslow/), a tool from Yahoo!
  that suggests ways to improve website speed.
- [WebPagetest](https://www.webpagetest.org/)
  shows a waterfall view of your pages' load performance plus an optimization checklist.
- In
  [Webmaster Tools](https://search.google.com/search-console),
  Labs > Site Performance shows the speed of your website as experienced by users around the
  world as in the chart below. We've also blogged about
  [site performance](/search/blog/2009/12/your-sites-performance-in-webmaster).

  ![site performance graph in webmaster tools](/static/search/blog/images/import/3ebe0d36506812f8abef45b834f9b7aa.png)
- Many other tools on
  [code.google.com/speed](https://code.google.com/speed/).

While site speed is a new signal, it doesn't carry as much weight as the
[relevance of a page](https://www.youtube.com/watch?v=muSIzHurn4U).
Currently, fewer than 1% of search queries are affected by the site speed signal in our
implementation and the signal for site speed only applies for visitors searching in English on
Google.com at this point. We launched this change a few weeks back after rigorous testing. If you
haven't seen much change to your site rankings, then this site speed change possibly did not
impact your site.

We encourage you to start looking at your site's speed (the tools above provide a great starting
point)—not only to improve your ranking in search engines, but also to improve everyone's
experience on the Internet.
