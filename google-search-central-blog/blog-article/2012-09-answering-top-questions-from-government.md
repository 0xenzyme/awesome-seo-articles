---
title: "Answering the top questions from government webmasters"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2012-09-answering-top-questions-from-government"
url: "https://developers.google.com/search/blog/2012/09/answering-top-questions-from-government"
canonical: "https://developers.google.com/search/blog/2012/09/answering-top-questions-from-government"
author: "Jason Morrison"
published: "2012-09-14T00:00:00+00:00"
updated: "2012-09-14T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:20:01+00:00"
status_code: 200
html_hash: "6752a6d9ad8334c353270ed8a1f3b15665eec5d9a5697641c3bff3ca50cc60c6"
clean_word_count: 1370
clean_char_count: 8436
---
# Answering the top questions from government webmasters

Government sites, from city to state to federal agencies, are extremely important to Google
Search. For one thing, governments have a lot of content—and government websites are often
the canonical source of information that's important to citizens. Around
[20 percent](https://sites.google.com/a/pressatgoogle.com/googleplaces/metrics)
of Google searches are for local information, and local governments are experts in their
communities.

That's why I've spoken at the
[National Association of Government Webmasters](https://nagw.org/)
(NAGW) national conference for the past few years. It's always interesting speaking to webmasters
about search, but the people running government websites have particular concerns and questions.
Since some questions come up frequently I thought I'd share this FAQ for government websites.

**Question 1: How do I fix an incorrect phone number or address in search results or Google Maps?**
Although managing their agency's site is plenty of work, government webmasters are often called
upon to fix problems found elsewhere on the web too. By far the most common question I've taken is
about fixing addresses and phone numbers in search results. In this case, government site owners
really can do it themselves, by
[claiming their Google+ Local listing](https://www.google.com/places/).
Incorrect or missing phone numbers, addresses, and other information can be fixed by claiming the
listing.

Most locations in Google Maps have a Google+ Local listing—businesses, offices, parks,
landmarks, etc. I like to use the
[San Francisco Main Library](https://plus.google.com/105369682299420794294/about)
as an example: it has contact info, detailed information like the hours they're open, user reviews
and fun extras like photos. When we think users are searching for libraries in San Francisco, we
may display a map and a listing so they can find the library as quickly as possible.

If you work for a government agency and want to claim a listing, we recommend using a shared
Google Account with an email address at your .gov domain if possible. Usually, ownership of the
page is confirmed via a phone call or post card.

**Question 2: I've claimed the listing for our office, but I have 43 different city parks to claim
in Google Maps, and none of them have phones or mailboxes. How do I claim them?**
Use the bulk uploader! If you have 10 or more listings / addresses to claim at the same time, you
can upload a
[specially-formatted spreadsheet](https://support.google.com/places/bin/answer.py?answer=178024).
Go to
[www.google.com/places/](https://www.google.com/places/),
click the "Get started now" button, and then look for the "bulk upload" link.

If you run into any issues, use the
[Verification Troubleshooter](https://support.google.com/places/bin/static.py?ts=1399021&page=ts.cs).

**Question 3: We're moving from a .gov domain to a new .com domain. How should we move the site?**
We have a
[Help Center article](/search/docs/crawling-indexing/site-move-with-url-changes)
with more details, but the basic process involves the following steps:

- Make sure you have both the old and new domain verified in the same Webmaster Tools account.
- Use a [`301` redirect](/search/docs/crawling-indexing/301-redirects) on
  all pages to tell search engines your site has moved permanently.

- Don't do a single redirect from all pages to your new home page—this gives a bad user
  experience.
- If there's no 1:1 match between pages on your old site and your new site (recommended), try to
  redirect to a new page with similar content.
- If you can't do redirects, consider
  [cross-domain canonical links](/search/docs/crawling-indexing/consolidate-duplicate-urls).

- Make sure to check if the new location is crawlable by Googlebot using the
  [Fetch as Google](https://support.google.com/webmasters/bin/answer.py?answer=158587)
  feature in Webmaster Tools.
- Use the
  [Change of Address](https://support.google.com/webmasters/bin/answer.py?answer=83106)
  tool in Webmaster Tools to notify Google of your site's move.
- Have a look at the
  [Links to Your Site](https://support.google.com/webmasters/bin/answer.py?answer=55281)
  in Webmaster Tools and inform the important sites that link to your content about your new location.
- We recommend not implementing other major changes at the same time, like large-scale content,
  URL structure, or navigational updates.
- To help Google pick up new URLs faster, use the Fetch as Google tool to ask Google to crawl your
  new site, and submit a Sitemap listing the URLs on your new site.
- To prevent confusion, it's best to retain control of your old site's domain and keep redirects
  in place for as long as possible—at least 180 days.

What if you're moving just part of the site? This question came up too—for example, a city
might move its "Tourism and Visitor Info" section to its own domain.

In that case, many of the same steps apply: verify both sites in Webmaster Tools, use
`301` redirects, clean up old links, etc. In this case you don't need to use the
Change of Address form in Webmaster Tools since only part of your site is moving. If for some
reason you'll have some of the same content on both sites, you may want to include a
[cross-domain canonical link](/search/docs/crawling-indexing/consolidate-duplicate-urls)
pointing to the preferred domain.

**Question 4: We've done a ton of work to create unique titles and descriptions for pages.
How do we get Google to pick them up?**
First off, that's great!
[Better titles and descriptions](/search/docs/appearance/title-link)
help users decide to click through to get the information they need on your page. The government
webmasters I've spoken with care a lot about the content and organization of their sites, and work
hard to provide informative text for users.

Google's generation of page titles and descriptions (or "snippets") is completely automated and
takes into account both the content of a page as well as references to it that appear on the web.
Changes are picked up as we recrawl your site. But you can do two things to let us know about
URLs that have changed:

- [Submit an updated XML Sitemap](/search/docs/crawling-indexing/sitemaps/overview)
  so we know about all of the pages on your site.
- In Webmaster Tools, use the Fetch as Google feature on a URL you've updated. Then you can
  choose to
  [submit it to the index](/search/blog/2011/08/submit-urls-to-google-with-fetch-as).

- You can choose to submit all of the linked pages as well—if you've updated an entire
  section of your site, you might want to submit the main page or an index page for that section
  to let us know about a broad collection of URLs.

**Question 5: How do I get into the YouTube government partner program?**
For this question, I have bad news, good news, and then even better news. On the one hand, the
government partner program has been discontinued. But don't worry, because most of the features
of the program are now available to your regular YouTube account. For example, you can now
[upload videos longer than 10 minutes](https://youtube-global.blogspot.com/2011/09/additional-creator-tools-from-youtube).

Did I say I had even better news? YouTube has added a lot of functionality useful for governments
in the past year:

- You can now
  [broadcast live streaming video](https://googleblog.blogspot.com/2012/05/google-hangouts-on-air-broadcast-your)
  to YouTube via Hangouts On Air (requires a Google+ account).
- You can
  [link your YouTube account with your Webmaster Tools account](/search/blog/2012/06/adding-associates-to-manage-your),
  making it the "official channel" for your site.
- Automatic captions continue to
  [get better and better](https://youtube-global.blogspot.com/2012/02/captions-for-all-more-options-for-your),
  supporting
  [more languages](https://youtube-global.blogspot.com/2012/06/youtube-automatic-captions-now).

I hope this FAQ has been helpful, but I'm sure I haven't covered everything government webmasters
want to know. I highly recommend our
[Webmaster Academy](/search/docs/fundamentals/seo-starter-guide),
where you can learn all about making your site search-engine friendly. If you have a specific
question, please you can add a question in the comments or visit our really helpful
[Webmaster Central Forum](https://support.google.com/webmasters/community).
