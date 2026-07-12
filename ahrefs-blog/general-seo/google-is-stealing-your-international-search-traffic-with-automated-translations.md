---
title: "Google Is Stealing Your International Search Traffic With Automated Translations"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "google-is-stealing-your-international-search-traffic-with-automated-translations"
url: "https://ahrefs.com/blog/google-is-stealing-your-international-search-traffic-with-automated-translations/"
canonical: "https://ahrefs.com/blog/google-is-stealing-your-international-search-traffic-with-automated-translations/"
author: "Erik Sarissky"
published: "2025-06-02T14:51:10+00:00"
updated: "2026-05-28T12:45:35+00:00"
categories:
  - "General SEO"
freshness_reasons: []
fetched_at: "2026-06-12T11:33:43+00:00"
status_code: 200
html_hash: "0b4778ef50264341f1c0431d57fb3bd3b041d425e28efa62c3abf582a92b74aa"
clean_word_count: 970
clean_char_count: 6354
---
# Google Is Stealing Your International Search Traffic With Automated Translations

Since the March Core update, there’s been a huge increase in Google’s efforts to automatically translate English-language webpages into other languages. The catch? These newly translated pages are hosted on a Google subdomain, so the original content creators don’t see any benefit from them.

![](https://ahrefs.com/blog/wp-content/uploads/2025/06/Screenshot-2025-06-02-at-14.39.53.png)

This coincides with the [massive rollout of AI Overviews we saw alongside the March update](https://ahrefs.com/blog/ai-overview-growth/). AI Overviews are now in 200 countries and 40 + languages. It seems that when AI Overviews lack sufficient native-language content, Google resorts to auto-translating English-language content.

These Google-hosted translations are prevalent in AI Overviews, but they also appear in Featured snippets, other SERP features, and the SERP’s normal 10 blue links. In other words: **if you haven’t localized your content, you now run the risk of Google capturing that local traffic for itself.**

As Patrick Stox points out, Google has talked about improving the [hreflang](https://ahrefs.com/blog/hreflang-tags/) system for years. Instead of continuing to help content creators translate and localize their content, it seems that Google has decided the best option is to claim the traffic as their own (something we’re seeing [more and more often](https://ahrefs.com/blog/google-looking-out-for-number-one/)). This seems hypocritical given their long-standing advice to avoid auto-translating your content.

Let’s take a closer look at what’s happening and also big thanks to Metehan Yesilyurt for being one of the [first people to highlight this](https://x.com/metehan777/status/1927353690471477348).

## What exactly is a Translate-Proxy page?

When Google can’t find a strong local-language source, it now grabs an authoritative English page, AI translates it on the fly, and serves the copy under a Google-owned subdomain that looks like this:

```
www-your-site-com.translate.goog/path?hl=es&sl=en
```

Because the HTML is proxied through Google, users never visit your domain. The page can then be cited throughout Google’s SERPs, including inside AI Overviews, which now appear in 200 countries and 40 + languages.

These pages look like this:

## Which countries are hardest hit?

If we use [Ahrefs Site Explorer](https://ahrefs.com/site-explorer) to analyze organic performance metrics for [translate.google.com/translate](https://translate.google.com/translate), we can estimate which countries are seeing the most of these auto-translated pages:

| Location | Estimated monthly organic traffic | AI Overview appearances | Crawled pages |
| --- | --- | --- | --- |
| All | 377M | 6.2M | 50.9M |
| India | 136M | 743k | 10.7M |
| Indonesia | 39M | 997k | 9.3M |
| Brazil | 36.9M | 1.2M | 6M |
| Turkey | 33.3M | 162k | 5.3M |
| Mexico | 28.3M | 1M | 7.1M |
| Thailand | 23.4M | 50.6k | 3.4M |
| Vietnam | 13.7M | 24k | 2.5M |
| Argentina | 9.4M | 398k | 3.8M |
| Colombia | 8.3M | 441k | 3.6M |
| Peru | 6M | 209k | 1.8M |

## How to find out if Google is stealing your international traffic

If you want to see if Google is auto-translating your website pages, you can use Search Console and Ahrefs to find out:

1. Search Console filter. Search Appearance *→* Translated Pages

2. [Ahrefs Site Explorer](https://ahrefs.com/site-explorer) *→* Open the top pages report for [translate.google.com](https://translate.google.com) and apply a “URL contains” filter, entering your domain name.

3. Country-by-country spot-checks. Incognito-search your brand/topic in target languages. Alternatively, simulate the search with the Ahrefs toolbar.
4. Log-file or GA4 referrer checks. Look for sessions where the referrer equals [translate.google.com](https://translate.google.com)

When Google shows its proxy-translated version in the SERP, the user lands on [translate.google.com](https://translate.google.com). A click to your site would be recorded as google / organic, but a click that leads to [translate.google.com](https://translate.google.com) showing your site is recorded as translate.google.com / referral instead. Your organic traffic (and any sales it drives) is under-reported.

Every internal link inside that proxy page also points to [translate.google.com](https://translate.google.com), so the mis-attribution continues as users click around.

## What can we do about it?

**Ship even a** [**300-word native-language version**](https://www.searchenginejournal.com/ideal-blog-post-length-for-seo/255633/)**,** even if it’s an MVP**.** Gives Google a local URL to cite, usually displacing the proxy.

Quick steps for simple solution (can vary by cases, of course)

**Scenario:**

Your article lives at */blog/how-to-pick-a-vpn*. Google is proxy-translating it and sending Spanish-speaking searchers to *translate.googleusercontent.com*. You want those visitors (and analytics credit) back.

Translate your page. If you are translating with AI, make sure you double-check brand terms, idioms, screenshots…etc

Make sure you use [hreflang](https://ahrefs.com/blog/hreflang-tags/) tags to connect the pages.

**What changes in search and analytics:**

Google now has a genuine Spanish URL to rank, so the proxy link disappears from Spanish SERPs within a day or two.

In **Search Console → Search appearance → Translated pages** you’ll see impressions for that page drop to zero.

GA4 stops logging translate.google.com / referral and assigns the clicks to **google / organic** restoring your search traffic stats.

If you don’t or can’t do that, you can **ask Google not to auto-translate important URLs** using the X-Robots-Tag.

Tip

Only block translation on pages where losing the canonical URL hurts (checkout flows, lead-gen). Leaving *notranslate* off blog content lets Google still translate when helpful.

<https://developers.google.com/search/docs/appearance/translated-results>

Bonus: Natzir came with his own script how to solve this. [Link to github](https://gist.github.com/natzir/f13e37febb8ba7e5f1e9caed620c26d4)

The proxy surge won’t kill SEO, but it rewrites the playbook in a multilingual, AI-first SERP, “be the best local answer *or* be proxied.” Make sure your brand lands on the right side of that equation.
