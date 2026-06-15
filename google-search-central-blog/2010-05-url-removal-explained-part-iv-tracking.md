---
title: "URL removal explained, Part IV: Tracking your requests and what not to remove"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2010-05-url-removal-explained-part-iv-tracking"
url: "https://developers.google.com/search/blog/2010/05/url-removal-explained-part-iv-tracking"
canonical: "https://developers.google.com/search/blog/2010/05/url-removal-explained-part-iv-tracking"
author: "Susan Moskwa, Webmaster Trends Analyst"
published: "2010-05-03T00:00:00+00:00"
updated: "2010-05-03T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:06:37+00:00"
status_code: 200
html_hash: "bd0529874b4e1d76b003ac8407b9770b5e9cb8618d0a24f5ce155769abfa28e9"
clean_word_count: 1207
clean_char_count: 7417
---
# URL removal explained, Part IV: Tracking your requests and what not to remove

In this final installation in our URL removal series, let's talk about following up on your
removal requests, as well as when *not* to use Google's URL removal tool. If you haven't
already, I recommend reading the previous posts in this series:

- [Part I: Removing URLs and directories](/search/blog/2010/03/url-removal-explained-part-i-urls)
- [Part II: Removing and updating cached content](/search/blog/2010/04/url-removals-explained-part-ii-removing)
- [Part III: Removing content you don't own](/search/blog/2010/04/url-removal-explained-part-iii-removing)
- [Part IV: Tracking requests, what not to remove](/search/blog/2010/05/url-removal-explained-part-iv-tracking)

You might be also interested to read about
[managing what information is available about you online](/search/blog/2009/10/managing-your-reputation-through-search).

## Understanding the status of your requests

Once you've submitted a removal request, it will appear in your list of requests. You can check
the status of your requests at any time to see whether the content has been removed, or whether
the request is still or pending or was denied.

![removal requests and their status](/static/search/blog/images/archived_1_File.png)

If a request was denied, you should see a "Learn more" link next to it explaining why that
particular request was denied. Since different types of removals have different requirements, the
reason why a particular request was denied can vary. The "Learn more" link should help you figure
out what you need to change in order to make your request successful. For example, you may need to
change the URL in question so that it meets the requirements for the type of removal you
requested; or, if you can't do that, you may need to request a different type of removal (one
whose requirements your URL currently meets).

If a request has been marked "Removed" but you still see that content in search results, check
the following:

- **Is the URL that's appearing in search results the exact same URL** that you submitted for
  removal? It's fairly common for the same, or similar, content to appear on multiple URLs on a
  site. You may have successfully removed one URL, but still see others containing that same
  content.

  **Solution:** Request removal of the other URL(s) in question. See our help center article
  about
  [which URL should you use for removal/block requests](https://www.google.com/support/webmasters/bin/answer.py?answer=63758)
  for help.
- Keep in mind that **URLs are case sensitive**, so requesting removal of
  `https://www.example.com/embarrassingstuff.html` is not the same as requesting
  removal of `https://www.example.com/EmbarrassingStuff.html`

  **Solution:** Request removal of the other URL(s) in question. See our help center article
  about
  [which URL should you use for removal/block requests](https://www.google.com/support/webmasters/bin/answer.py?answer=63758)
  for help.
- When a request is marked "Removed," that can
  **mean different things depending on what type of request** you submitted. If you requested
  removal of an entire URL, then "Removed" should mean that that entire URL no longer appears in
  our search results. If you requested removal of the cached copy of a URL, "Removed" means that
  the cached copy has been removed and will no longer appear in search results; but the URL
  itself may still appear.

  **Solution:** Double-check what type of removal you requested by looking at the "Removal
  Type" column. If you requested a cache removal but you want the entire URL gone, make sure
  the URL meets the
  [requirements for complete removal](/search/blog/2010/03/url-removal-explained-part-i-urls)
  and then file a new request for complete removal of the URL.

## When not to use the URL removal tool

- **To clean up cruft**, like old pages that `404`. The tool is intended for URLs
  that urgently need to be removed, such as confidential data that was accidentally exposed. If
  you recently made changes to your site and just have some outdated URLs in the index, Google's
  crawlers will see this as we recrawl your URLs, and those pages will naturally drop out of our
  search results over time. There's no need to request an urgent removal through this tool.
- **To remove
  [crawl errors](https://support.google.com/webmasters/answer/9679690)**
  from your Webmaster Tools account. The removal tool removes URLs from Google's search results,
  not from your Webmaster Tools account. There's currently no way for you to manually remove URLs
  from this report; they will drop out naturally over time as we stop crawling URLs that
  repeatedly `404`.
- **To "start from scratch"** with your site. If you're worried that your site may have a
  penalty, or you want to "start from scratch" after purchasing a domain from someone else, we
  don't recommend trying to use the URL removal tool to remove your entire site and then "start
  over." Search engines gather a lot of information from other sites (such as who links to you, or
  what words they use to describe your site) and use this to help understand your site. Even if we
  could remove everything we currently know about your site, a lot of it would come back exactly
  the same once we'd recrawled all the other sites that help us understand your site and put it in
  context. If you're worried that your domain has some bad history, we recommend filing a
  [reconsideration request](https://www.google.com/support/webmasters/bin/answer.py?answer=35843)
  letting us know what you're worried about and what has changed (such as that you've acquired the
  domain from someone else, or that you've changed certain aspects of your site).
- **To take your site "offline" after hacking.** If your site was hacked and you want to get
  rid of bad URLs that got indexed, you can use the URL removal tool to remove any new URLs that
  the hacker created, for example,
  `https://www.example.com/buy-cheap-cialis-skq3w598.html`.
  But we don't recommend removing your entire site, or removing URLs that you'll eventually want
  indexed; instead, simply clean up the hacking and let us recrawl your site so that we can
  reindex the new, cleaned-up content as soon as possible.
  [This article](/search/blog/2008/04/my-sites-been-hacked-now-what) contains more
  details on how to deal with hacking.
- **To get the right "version" of your site indexed.** When a request to remove
  `https://www.example.com/tattoo.html` is accepted,
  `http://www.example.com/tattoo.html` is also removed. The same is true of the
  **www** and **non-www** versions of your URL or site. This is because the same content is
  often available at each of these URLs and we realize that most webmasters and searchers don't
  want these duplicates appearing in search results. In short, the URL removal tool should not be
  used as a
  [canonicalization](/search/docs/crawling-indexing/consolidate-duplicate-urls) tool.
  It won't keep your favorite version, it'll remove all versions (http/https and www/non-www) of
  a URL.

We hope this series has answered your questions about removing content from Google's search
results, and helped you troubleshoot any issues that may arise. Join us in our
[Help Forum](https://support.google.com/webmasters/community/label?lid=5489e59697a233d7)
if you still have questions.
