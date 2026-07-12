---
title: "How to move from m-dot URLs to responsive site"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2017-09-how-to-move-from-m-dot-urls-to"
url: "https://developers.google.com/search/blog/2017/09/how-to-move-from-m-dot-urls-to"
canonical: "https://developers.google.com/search/blog/2017/09/how-to-move-from-m-dot-urls-to"
author: "Cherry Prommawin"
published: "2017-09-14T00:00:00+00:00"
updated: "2017-09-14T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2017_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:30:50+00:00"
status_code: 200
html_hash: "0f683d869d7595b9110ab38faf9824910ca6dbaa419de53e76f3af2c82d81871"
clean_word_count: 352
clean_char_count: 2341
---
# How to move from m-dot URLs to responsive site

With more sites moving towards responsive web design, many webmasters have questions about
migrating from
[separate mobile URLs](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing),
also frequently known as "m-dot URLs", to using
[responsive web design](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing).
Here are some recommendations on how to move from separate urls to one responsive URL in a way
that gives your sites the best chance of performing well on Google's search results.

## Moving to responsive sites in a Googlebot-friendly way

Once you have your responsive site ready, moving is something you can definitely do with just a
bit of forethought. Considering your URLs stay the same for desktop version, all you have to do is
to configure `301` redirects from the mobile URLs to the responsive web URLs.

Here are the detailed steps:

1. Get your responsive site ready
   ![](/static/search/blog/images/import/d07b9be179a990fda9ebbfa461e186b7.png)
2. Configure `301` redirects on the old mobile URLs to point to the responsive versions (the new
   pages). These redirects need to be done on a per-URL basis, individually from each mobile URLs
   to the responsive URLs.
   ![](/static/search/blog/images/import/0226356ed2be735b73bc126efe3d1dc8.png)
3. Remove any mobile-URL specific configuration your site might have, such as conditional redirects
   or a vary HTTP header.
4. As a good practice,
   [setup `rel=canonical`](/search/docs/crawling-indexing/consolidate-duplicate-urls)
   on the responsive URLs pointing to themselves (self-referential canonicals).

If you're currently using dynamic serving and want to move to responsive design, you don't need to
add or change any redirects.

## Some benefits for moving to responsive web design

Moving to a responsive site should make maintenance and reporting much easier for you down the
road. Aside from no longer needing to manage separate URLs for all pages, it will also make it
much easier to adopt practices and technologies such as hreflang for internationalization, AMP for
speed, structured data for advanced search features and more.

As always, if you need more help you can ask a question in our
[webmaster forum](https://support.google.com/webmasters/community).
