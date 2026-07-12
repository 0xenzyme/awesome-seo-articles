---
title: "Directing smartphone users to the page they actually wanted"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2014-06-faulty-redirects"
url: "https://developers.google.com/search/blog/2014/06/faulty-redirects"
canonical: "https://developers.google.com/search/blog/2014/06/faulty-redirects"
author: "Mariya Moeva"
published: "2014-06-05T00:00:00+00:00"
updated: "2014-06-05T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2014_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:24:53+00:00"
status_code: 200
html_hash: "14668ed380739e6b33469ebd4476dfc97aed53e5dd743d227f4b6dbfb19b2b91"
clean_word_count: 449
clean_char_count: 2867
---
# Directing smartphone users to the page they actually wanted

Have you ever used Google Search on your smartphone and clicked on a promising-looking result,
only to end up on the mobile site's home page, with no idea why the page you were hoping to see
vanished? This is such a common annoyance that
[we've even seen comics about it](https://xkcd.com/869/). Usually this
happens because the website is
[not properly set up to handle requests from smartphones](https://support.google.com/webmasters/answer/4046647)
and sends you to its smartphone home page—we call this a "faulty redirect".

We'd like to spare users the frustration of landing on irrelevant pages and help webmasters fix
the faulty redirects. Starting today in our English search results in the US, whenever we detect
that smartphone users are redirected to a home page instead of the page they asked for, we may note
it below the result. If you still wish to proceed to the page, you can click "Try anyway":

![](/static/search/blog/images/import/b8262d748f25e7b9712565534d85ebfe.png)

And we're providing advice and resources to help you direct your audience to the pages they want.
Here's a quick rundown:

1. Do a few searches on your own phone (or with
   [a browser set up to act like a smartphone](https://developer.chrome.com/devtools/docs/mobile-emulation))
   and see how your site behaves. Simple but effective. :)
2. Check out
   [Webmaster Tools](https://search.google.com/search-console)
   —we'll send you a message if we detect that any of your site's pages are redirecting
   smartphone users to the home page. We'll also show you any faulty redirects we detect in the
   Smartphone Crawl Errors section of Webmaster Tools:

   ![](/static/search/blog/images/import/67a1f3960655d040bdd19e0a025dda4b.png)
3. Investigate any faulty redirects and fix them. Here's what you can do:

   - Use the example URLs we provide in Webmaster Tools as a starting point to debug exactly
     where the problem is with your server configuration.
   - Set up your server so that it redirects smartphone users to the equivalent URL on your
     smartphone site.
   - If a page on your site doesn't have a smartphone equivalent, keep users on the desktop page,
     rather than redirecting them to the smartphone site's home page. Doing nothing is better than
     doing something wrong in this case.
   - Try using
     [responsive web design](/web/fundamentals/documentation/multi-device-layouts/rwd-fundamentals),
     which serves the same content for desktop and smartphone users.

If you'd like to know more about building smartphone-friendly sites,
[read our full recommendations](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing). And, as always, if
you need more help you can ask a question in our
[webmaster forum](https://support.google.com/webmasters/go/community).
