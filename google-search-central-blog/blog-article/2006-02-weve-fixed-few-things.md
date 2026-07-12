---
title: "We've fixed a few things"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2006-02-weve-fixed-few-things"
url: "https://developers.google.com/search/blog/2006/02/weve-fixed-few-things"
canonical: "https://developers.google.com/search/blog/2006/02/weve-fixed-few-things"
author: "Vanessa Fox"
published: "2006-02-13T00:00:00+00:00"
updated: "2006-02-13T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:44:55+00:00"
status_code: 200
html_hash: "c1f3ef0cb06a7d683aed7614d5ce5fc31d05826a7f780f31446047345472807c"
clean_word_count: 383
clean_char_count: 2447
---
# We've fixed a few things

We've just fixed a few issues that our
[Google Group](https://support.google.com/webmasters/community)
members brought to our attention.

## Capitalization in robots.txt lines

Our robots.txt analysis tool didn't correctly interpret lines that include capitalized letters.
This has been fixed. All results with URLs that include capital letters are being processed
correctly. Note that in a robots.txt file, the capitalization of the rules don't matter. For
instance, `Disallow:` and `disallow:` are interpreted in the same way.
However, capitalization of URLs *does* matter. So, for the following robots.txt file:

```
User-agent: *
Disallow: /Myfile.html
```

`https://www.example.com/Myfile.html` is blocked. But
`https://www.example.com/myfile.html` is not blocked.

## Google User-agents other than Googlebot

Our robots.txt analysis tool didn't correctly process robots.txt files for Google user-agents
other than Googlebot. This has been fixed. The Google user-agents we provide analysis for are:

- `Googlebot-Mobile:` crawls pages for our
  [mobile index](https://mobile.google.com/mobile_search.html)
- `Googlebot-Image:` crawls pages for our
  [image index](https://www.google.com/imghp?tab=wi&q=)
- `Googlebot-MediaPartners:` crawls pages to determine
  [AdSense content](https://www.google.com/adsense/) (used only
  if you show AdSense ads on your site)

## robots.txt files with extra initial characters

Some robots.txt files have extra characters before the start of the first rule. Some text editors
place these characters in the file, but you can't see them with the editor. When the tool
processed these characters, it reported a syntax error. The tool now mimics Googlebot's behavior
and ignores these extra characters.

## Capitalization in site URLs

When you add a site, we now convert all the letters in the domain portion of the URL to lowercase,
regardless of how you entered the letters. For instance, if you enter
`https://www.Example.com/`, we convert that to
`https://www.example.com/` in your account. This applies only to the domain, so for
instance, if you add `https://www.Example.com/MySite/`, we will convert it to
`https://www.example.com/MySite/`. If you added sites to your account using
capitalized letters, you'll notice the domain portions have been converted to lowercase. We
made this minor change as part of our efforts to ensure you see all available stats for your site.
