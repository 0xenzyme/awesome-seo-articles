---
title: "#NoHacked: Identifying and Diagnosing Injected Gibberish URL Hacking"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2015-08-nohacked-identifying-and-diagnosing"
url: "https://developers.google.com/search/blog/2015/08/nohacked-identifying-and-diagnosing"
canonical: "https://developers.google.com/search/blog/2015/08/nohacked-identifying-and-diagnosing"
author: "Eric Kuan, Webmaster Relations Specialist and Yuan Niu, Webspam Analyst"
published: "2015-08-17T00:00:00+00:00"
updated: "2015-08-17T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2015_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:27:18+00:00"
status_code: 200
html_hash: "06c16eca049d74d405f8616712d42c243001b5bc2a2fafa7b76b9876bc651be0"
clean_word_count: 1176
clean_char_count: 7422
---
# #NoHacked: Identifying and Diagnosing Injected Gibberish URL Hacking

Today in our #NoHacked campaign, we'll be discussing how to identify and diagnose a trending hack.
Even if your site is not infected with this specific type of hack, many of these steps can be
helpful for other types of hacks. Next week, we'll be following up with a post about fixing this
hack. Follow along with discussions on
[Twitter](https://twitter.com/googlesearchc) and
[Google+](https://google.com/+googlewebmasters)
using the #NoHacked tag.
([Part 1](/search/blog/2015/07/nohacked-how-to-avoid-being-target-of),
[Part 2](/search/blog/2015/08/nohacked-how-to-recognise-and-protect),
[Part 3](/search/blog/2015/08/nohacked-using-two-factor))

- [Identifying Symptoms](#IDSymptoms)
  - [Gibberish pages](#Gibberish)
  - [Cloaking](#Cloaking)
- [Monitoring your Site](#Monitoring)
  - [Looking for a surge in website traffic](#Surge)
  - [Tracking your site appearance in search results](#Tracking)
  - [Signing up for alerts from Google](#Alerts)
- [Diagnosing your Site](#Diagnosing)
  - [Gathering tools that can help](#Tools)
  - [Checking for hacked pages](#HackedPages)
  - [Checking for cloaking on hacked pages](#CloakingonHackedPages)
- [Appendix](#Appendix)

![](/static/search/blog/images/import/904d2c4b356e585c785df41c1bc17a24.png)

## Identifying Symptoms

### Gibberish pages

The hallmark of this type of hacking is spammy pages that appear to be added to the site. These
pages contain keyword-rich gibberish text, links, and images in order to manipulate search
engines. For example, the hack creates pages like
[`www.example.com/pf/download-2012-free-full-crack.html`](https://www.example.com/pf/download-2012-free-full-crack)
which contain gibberish content like below:

![](/static/search/blog/images/import/19d3b6daca5d42ff557354a408580ffc.png)

### Cloaking

This hack often uses
[cloaking](/search/docs/essentials/spam-policies#cloaking)
to avoid webmasters from detecting it. Cloaking refers to the practice of presenting different
content or URLs to webmasters, visitors, and search engines. For example, the webmaster of the
site might be shown an empty or HTTP `404` page which would lead the webmaster to
believe the hack is no longer present. However, users who visit the page from search results will
still be redirected to spammy pages, and search engines that crawl the site will still be
presented with gibberish content.

## Monitoring your Site

Properly monitoring your site for hacking allows you to remedy the hack more quickly and minimize
damage the hack might cause. There are several ways you can monitor your site for this particular
hack.

### Looking for a surge in website traffic

Because this hack creates many keyword heavy URLs that are crawled by search engines, check to
see if there was any recent, unexpected surges in traffic. If you do see a surge, use the
[Search Analytics tool](https://search.google.com/search-console/performance/search-analytics)
in Search Console to investigate whether or not hacked pages are the source of the unusual website
traffic.

### Tracking your site appearance in search results

Periodically checking how your site appears in search results is good practice for all webmasters.
It also allows you to spot symptoms of hacking. You can check your site in Google by using the
[`site:` operator](https://support.google.com/websearch/answer/2466433)
on your site (that is, search for `site:example.com`). If you see any gibberish links
associated with your site or a label that says "This site may be hacked.", your site might have
been compromised.

### Signing up for alerts from Google

We recommend you sign up for
[Search Console](https://google.com/webmasters/tools/). In Search
Console, you can check if Google has detected any hacked pages on your site by looking in the
[Manual Actions Viewer](https://support.google.com/webmasters/answer/2604824)
or
[Security Issues](https://search.google.com/search-console/security-issues)
report. Search Console will also message you if Google has detected any hacked pages on your site.

Also, we recommend you set up
[Google Alerts](https://google.com/alerts) for your site. Google Alerts
will email you if Google finds new results for a search query. For example, you can set up a
Google Alert for your site in conjunction with
[common spammy terms](https://www.google.com/search?q=common+spam+terms)
like site:example.com cheap software. If you receive an email that
Google has returned a new query for that term, you should immediately check what pages on your
site are triggering that alert.

## Diagnosing your Site

### Gathering tools that can help

In Search Console, you have access to the
[Fetch as Google tool](https://support.google.com/webmasters/answer/6066468)
in Search Console. The Fetch as Google tool allows you to see a page as Google sees it. This will
help you to identify cloaked hacked pages. Additional tools from others are listed in the appendix
to this post.

### Checking for hacked pages

If you're not sure if there is hacked content on your site, the
[Google Hacked Troubleshooter](https://support.google.com/webmasters/troubleshooter/6155978)
can walk you through some basic checks. For this type of hack, you'll want to perform a
`site:` search on your site. Look for suspicious pages and URLs loaded with strange
keywords in the search results. If you have a large number of pages on your site, you might need
to try a more targeted query.
[Find common spam terms](https://www.google.com/search?q=common+spam+terms)
and append them to your `site:` search query like
`site:example.com cheap software`. Try this with several spammy terms to see if any
results show up.

### Checking for cloaking on hacked pages

Because this type of hacking employs cloaking to prevent accurate detection, it's very important
that you use the Fetch as Google tool in Search Console to check the spammy pages you found in the
previous step. Remember, cloaked pages can show you an HTTP `404` page that tricks you
into thinking the hack is fixed even if the page is still live. You should also use Fetch as
Google on your home page as well. This type of hack often adds text or links to the home page.

We hope this post has given you a better idea of how to identify and diagnose hacks that inject
gibberish URLs on your site. Tune in next week where we'll be explaining how to remove this hack
from your site. Be sure to follow our social campaigns and share any tips or tricks you might have
about staying safe on the web with the #NoHacked hashtag.

If you have any additional questions, you can post in the
[Webmaster Help Forums](https://support.google.com/webmasters/go/community)
where a community of webmasters can help answer your questions. You can also join our
[Hangout on Air about Security](https://plus.google.com/events/csqjnqe8vl28qbn526makjecobc)
on August 26.

## Appendix

These are tools that scan your site and may be able to find problematic content. Other than
VirusTotal, Google doesn't run or support them:
[Virus Total](https://www.virustotal.com/),
[Aw-snap.info](https://aw-snap.info/),
[Sucuri Site Check](https://sitecheck.sucuri.net/),
[Wepawet](https://wepawet.iseclab.org/). These are tools that may be
able to scan your site for problematic content. Keep in mind that these scanners can't guarantee
that they will identify every type of problematic content.
