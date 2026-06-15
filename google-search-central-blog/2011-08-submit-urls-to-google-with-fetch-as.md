---
title: "Submit URLs to Google with Fetch as Googlebot"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-08-submit-urls-to-google-with-fetch-as"
url: "https://developers.google.com/search/blog/2011/08/submit-urls-to-google-with-fetch-as"
canonical: "https://developers.google.com/search/blog/2011/08/submit-urls-to-google-with-fetch-as"
author: "Jonathan Simon, Susan Moskwa"
published: "2011-08-03T00:00:00+00:00"
updated: "2011-08-03T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:14:48+00:00"
status_code: 200
html_hash: "fec27c0b2a8ecabd2480325f7cd786a9cd39803742b223ddc6ac0ead635daabf"
clean_word_count: 601
clean_char_count: 3551
---
# Submit URLs to Google with Fetch as Googlebot

The Fetch as Googlebot feature in Webmaster Tools now provides a way to submit new and updated
URLs to Google for indexing. After you fetch a URL as Googlebot, if the fetch is successful,
you'll now see the option to submit that URL to our index. When you submit a URL in this way
Googlebot will crawl the URL, usually within a day. We'll then consider it for inclusion in our
index. Note that we don't guarantee that every URL submitted in this way will be indexed; we'll
still use our regular processes—the same ones we use on URLs discovered in any other way—to
evaluate whether a URL belongs in our index.

This new functionality may help you in several situations: if you've just launched a new site, or
added some key new pages, you can ask Googlebot to find and crawl them immediately rather than
waiting for us to discover them naturally. You can also submit URLs that are already indexed in
order to refresh them, say if you've updated some key content for the event you're hosting this
weekend and want to make sure we see it in time. It could also help if you've accidentally
published information that you didn't mean to, and want to update our cached version after you've
removed the information from your site.

## How to submit a URL

First, use Diagnostics > Fetch As Googlebot to fetch the URL
you want to submit to Google. If the URL is successfully fetched you'll see a new "Submit to
index" link appear next to the fetched URL.

![View of the fetch as googlebot feature in webmaster tools](/static/search/blog/images/import/39f225ab2c6eb18bd1476afbc962e042.png)

Once you click "Submit to index" you'll see a dialog box that allows you to choose whether you
want to submit only the one URL, or that URL and all its linked pages.

![The submit to url feature in Webmaster Tools](/static/search/blog/images/import/2d2bc67deaf7ba06c913ca669c7698f0.png)

When submitting individual URLs, we have a maximum limit of 50 submissions per week; when
submitting URLs with all linked pages, the limit is 10 submissions per month. You can see how many
submissions you have left on the Fetch as Googlebot page. Any URL submitted should point to
content that would be suitable for Google Web Search, so if you're trying to submit images or
videos you should use [Sitemaps](/search/docs/crawling-indexing/sitemaps/overview) instead.

## Submit URLs to Google without verifying

In conjunction with this update to Fetch as Googlebot, we've also updated the public "Add your
URL to Google" form. It's now the
[Crawl URL form](https://www.google.com/webmasters/tools/submit-url).
It has the same quota limits for submitting pages to the index as the Fetch as Googlebot feature
but doesn't require verifying ownership of the site in question, so you can submit any URLs that
you want crawled and indexed.

![The public crawl URL form](/static/search/blog/images/import/579c37901f151d5a3c41c1e3a4b00236.png)

Note that Googlebot is already pretty good about finding and crawling new content in a timely
fashion, so don't feel obligated to use this tool for every change or update on your site. But
if you've got a URL whose crawling or indexing you want to speed up, consider submitting it
using the
[Crawl URL form](https://www.google.com/webmasters/tools/submit-url)
or the updated Fetch as Googlebot feature in
[Webmaster Tools](https://search.google.com/search-console). You can visit our
[Webmaster Help Forum](https://support.google.com/webmasters/community)
if you have more detailed questions.
