---
title: "FAQs about the April 21st mobile-friendly update"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2015-04-faqs-april-21st-mobile-friendly"
url: "https://developers.google.com/search/blog/2015/04/faqs-april-21st-mobile-friendly"
canonical: "https://developers.google.com/search/blog/2015/04/faqs-april-21st-mobile-friendly"
author: "Maile Ohye"
published: "2015-04-21T00:00:00+00:00"
updated: "2015-04-21T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2015_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:26:35+00:00"
status_code: 200
html_hash: "c9bad85e22a5b76aab11e91be0028896b0803868f6608cef71431d91f258ddac"
clean_word_count: 1592
clean_char_count: 10731
---
# FAQs about the April 21st mobile-friendly update

We'd like to share answers to your frequently asked questions. For background, in February,
[we announced that the mobile-friendly update](/search/blog/2015/02/finding-more-mobile-friendly-search)
will boost the rankings of mobile-friendly pages—pages that are legible and usable on mobile
devices—in mobile search results worldwide. (Conversely, pages designed for only large
screens may see a significant decrease in rankings in mobile search results.) To get us all on the
same page, here are the most frequently asked questions:

## General FAQs

**1. Will desktop and/or tablet ranking also be affected by this change?**
No, this update has no effect on searches from tablets or desktops. It affects searches from
mobile devices across all languages and locations.

**2. Is it a page-level or site-level mobile ranking boost?**
It's a page-level change. For instance, if ten of your site's pages are mobile-friendly, but the
rest of your pages aren't, only the ten mobile-friendly pages can be positively impacted.

**3. How do I know if Google thinks a page on my site is mobile-friendly?**
Individual pages can be tested for "mobile-friendliness" using the
[Mobile-Friendly Test](https://www.google.com/webmasters/tools/mobile-friendly).

![Test individual URLs in real-time with the Mobile-Friendly Test](/static/search/blog/images/archived_lgRhY4O6dT1kT69QvaiH3-TFB2u9eXdzYaM2pDfrwxHEkVDRr3.png)

To review site-level information on mobile-friendliness, check out the
[Mobile Usability report in Webmaster Tools](https://search.google.com/search-console/mobile-usability).
This feature's data is based on the last time we crawled and indexed your site's pages.

![Mobile Usability in Webmaster Tools provides a snapshot of your entire site's mobile-friendliness](/static/search/blog/images/archived_egGhk2N72zSgS5Ckl4MFocJoOCOvdBLK0rgfEmDN3L0IwIubce.png)

**4. Unfortunately, my mobile-friendly pages won't be ready until after April 21st. How long
before they can be considered mobile-friendly in ranking?**
We determine whether a page is mobile-friendly every time it's crawled and indexed—you don't
have to wait for another update. Once a page is mobile-friendly, you can wait for
[Googlebot for smartphones](/search/blog/2014/01/a-new-googlebot-user-agent-for-crawling)
to naturally (re-)crawl and index the page or you can expedite processing by using
[Fetch as Google with Submit to Index](/search/docs/crawling-indexing/ask-google-to-recrawl)
in
[Webmaster Tools](https://search.google.com/search-console). For a large volume of
URLs, consider submitting a
[sitemap](/search/docs/crawling-indexing/sitemaps/overview). In the sitemap, if your mobile
content uses pre-existing URLs (such as with
[Responsive Web Design](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing#responsive-design)
or
[dynamic serving](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing#dynamic-serving)),
also include the
[`lastmod` tag](https://www.sitemaps.org/protocol.html#lastmoddef).

**5. Since the mobile ranking change rolls out on April 21st, if I see no drop in traffic on
April 22nd, does that mean that my site's rankings aren't impacted?**
You won't be able to definitively determine whether your site's rankings are impacted by the
mobile-friendly update by April 22nd. While we begin rolling out the mobile-friendly update on
April 21st, it'll be a week or so before it makes its way to all pages in the index.

**6. I have a great mobile site, but the Mobile-Friendly Test tells me that my pages aren't
mobile-friendly. Why?**
If a page is designed to work well on mobile devices, but it's not passing the Mobile-Friendly
Test, the most common reason is that Googlebot for smartphones is blocked from crawling resources,
like CSS and JavaScript, that are critical for determining whether the page is legible and usable
on a mobile device (that is, whether it's mobile-friendly). To remedy:

1. Check if the
   [Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)
   shows blocked resources (often accompanied with a partially rendered image).
2. [Allow Googlebot](/search/docs/crawling-indexing/overview-google-crawlers) to crawl
   the necessary files.
3. Double-check that your page passes the Mobile-Friendly Test.
4. Use
   [Fetch as Google with Submit to Index](/search/docs/crawling-indexing/ask-google-to-recrawl)
   and
   [submit your updated robots.txt to Google](/search/docs/crawling-indexing/robots/submit-updated-robots-txt)
   to expedite the re-processing of the updated page (or just wait for Google to naturally re-crawl
   and index).

![](/static/search/blog/images/archived_wBSGXuIza8Gl2NrZgOkwXX7DVjAI0maA8dNqxNz8o6O08Xi-ZM.png)

The most common reason why a mobile page fails the Mobile-Friendly Test is that Googlebot for
smartphones is blocked from crawling resources, like CSS and JavaScript, that are crucial for
understanding the page's mobile-friendliness.

To reiterate, we recommend that site owners allow Googlebot to crawl all resources for a page
(including CSS, JavaScript, and images), so that we can properly render, index, and in this case,
assess whether the page is mobile-friendly.

**7. What if I link to a site that's not mobile-friendly?**
Your page can still be "mobile-friendly" even if it links to a page that's not mobile-friendly,
such as a page designed for larger screens, like desktops. It's not the best experience for mobile
visitors to go from a mobile-friendly page to a desktop-only page, but hopefully as more sites
become mobile-friendly, this will become less of a problem.

**8. Does Google give a stronger mobile-friendly ranking to pages using Responsive Web Design
(which uses the same URL and the same HTML for the desktop and mobile versions) vs. hosting a
separate mobile site (like www for desktop and m.example.com for mobile)?**
No, mobile-friendliness is assessed the same, whether you use
[responsive web design](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing#responsive-design)
(RWD),
[separate mobile URLs](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing#separate-urls),
or [dynamic serving](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)
for your
[configuration](/search/mobile-sites/mobile-seo). If your site
uses separate mobile URLs or dynamic serving, we recommend reviewing the Mobile SEO guide to make
sure Google is properly crawling and indexing your mobile pages.

**9. Will my site / page disappear on mobile search results if it's not mobile-friendly?**
While the mobile-friendly change is important, we still use a variety of signals to rank search
results. The intent of the search query is still a very strong signal—so even if a page with
high quality content is not mobile-friendly, it could still rank high if it has great content for
the query.

## Specialized FAQs

**10. What if my audience is desktop only? Then there's no reason to have a mobile site,
right?**
Not exactly. Statistics show that more people are going "mobile only"—either because they
never had a desktop or because they won't replace their existing desktop. Additionally, a
non-mobile-friendly site may not see many mobile visitors precisely for that reason.

The mobile-friendly update will apply to mobile searches conducted across all sites, regardless of
the site's target audiences' language, region, or proportion of mobile to desktop traffic.

**11. I have pages showing mobile usability errors because they embed a YouTube video. What can I
do?**
We suggest paying close attention to how the YouTube video is embedded. If you are using the
"old-style" `<object>` embeds in the mobile page, convert to
`<iframe>` embeds for broader compatibility. YouTube now uses the
[HTML5 player on the web by default](https://youtube-eng.blogspot.com/2015/01/youtube-now-defaults-to-html5_27),
so it's mobile-friendly to embed videos using the `<iframe>` tags from the
"share" feature on the watch page or from the
[YouTube iFrame API](/youtube/iframe_api_reference).
If you have a more complex integration, that should also be mobile-friendly, since it'll instruct
the device to use the device's native support.

For Flash content from sites other than YouTube, check if there is an equivalent HTML5 embed tag
or code snippet to avoid using proprietary plugins.

**12. Is there a clear standard for
[sizing tap targets](/speed/docs/insights/SizeTapTargetsAppropriately)?**
Yes, we suggest a minimum of 7mm width/height for primary tap targets and a minimum margin of 5mm
between secondary tap targets. The average width of an adult's finger pad is 10mm, and these
dimensions can provide a usable interface while making good use of screen real estate.

**13. To become mobile-friendly quickly, we're thinking of creating a very stripped down version
of our site (separate mobile pages) until our new responsive site is complete. Do you foresee
any problems with this?**
First, keep in mind that we support
[three mobile configurations](/search/mobile-sites/mobile-seo)
and that your website doesn't have to be responsive to be mobile-friendly. In response to your
question, please be cautious about creating a "stripped down" version of your site. While the page
may be formatted for mobile, if it doesn't allow your visitors to easily complete their common
tasks or have an overall smooth workflow, it may become frustrating to your visitors and perhaps
not worth the effort. Should a temporary mobile site be created, once the RWD is live, be sure to
[move the site properly](/search/docs/crawling-indexing/site-move-with-url-changes).
For example, update all links so they no longer reference the separate mobile URLs and
`301` redirect mobile URLs to their corresponding RWD version.

## Recommendations

If you're totally new to building a mobile-friendly site, it's not too late! Check out our
[Getting Started guide](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing) in the
[Mobile-Friendly Websites documentation](/search/mobile-sites).

![Screeshot of the Search Central documentation focusing on mobile sites](/static/search/blog/images/archived_aKKLszTF1d590fW0smgqSHzcoH_66S56xtasHTkoEesbBYLgf0.png)

If you already have a mobile site, investigate the
[Mobile Usability report in Webmaster Tools](https://search.google.com/search-console/mobile-usability)
to make sure that Google detects your site's pages as mobile-friendly.

Still more questions? Please ask below or check out the
[Mobile Websites section of the Webmaster Forum](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:crawling_indexing_ranking)).
