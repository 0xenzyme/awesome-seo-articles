---
title: "Come see us at SES London and hear tips on successful site architecture"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2007-02-come-see-us-at-ses-london-and-hear"
url: "https://developers.google.com/search/blog/2007/02/come-see-us-at-ses-london-and-hear"
canonical: "https://developers.google.com/search/blog/2007/02/come-see-us-at-ses-london-and-hear"
author: null
published: "2007-02-13T00:00:00+00:00"
updated: "2007-02-13T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2007_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:47:26+00:00"
status_code: 200
html_hash: "cb901becba4b452cbe41763dafc420844eb5ebc184fadf8793509f679f3bffc4"
clean_word_count: 1059
clean_char_count: 6896
---
# Come see us at SES London and hear tips on successful site architecture

If you're planning to be at
[Search Engine Strategies London](https://www.searchenginestrategies.com/sew/london07/index)
February 13-15, stop by and say hi to one of the many Googlers who will be there. I'll be speaking
on Wednesday at the
[Successful Site Architecture](https://www.searchenginestrategies.com/sew/london07/agenda2.html#ssa)
panel and thought I'd offer up some tips for building crawlable sites for those who can't attend.

## Make sure visitors and search engines can access the content

- Check the
  [Crawl errors section](https://support.google.com/webmasters/answer/9679690)
  of Webmaster Tools for any pages Googlebot couldn't access due to server or other errors.
  If Googlebot can't access the pages, they won't be indexed and visitors likely can't access them
  either.
- Make sure your
  [robots.txt file](/search/docs/crawling-indexing/robots/create-robots-txt)
  doesn't accidentally block search engines from content you want indexed. You can see a list of
  the files Googlebot was
  [blocked from crawling](https://support.google.com/webmasters/answer/9679690)
  in Webmaster Tools. You can also use our
  [robots.txt analysis tool](https://support.google.com/webmasters/answer/6062598)
  to make sure you're blocking and allowing the files you intend.
- Check the
  [Googlebot activity reports](/search/blog/2006/10/googlebot-activity-reports)
  to see how long it takes to download a page of your site to make sure you don't have any network
  slowness issues.
- If pages of your site require a login and you want the content from those pages indexed, ensure
  you include a
  [substantial amount of indexable content](https://www.mattcutts.com/blog/guest-post-vanessa-fox-on-organic-site-review-session/)
  on pages that aren't behind the login. For instance, you can put several content-rich paragraphs
  of an article outside the login area, with a login link that leads to the rest of the article.
- How accessible is your site? How does it look in mobile browsers and screen readers? It's well
  worth testing your site under these conditions and ensuring that visitors can access the content
  of the site using any of these mechanisms.

## Make sure your content is viewable

- Check out your site in a text-only browser or view it in a browser with images and Javascript
  turned off. Can you still see all of the text and navigation?
- Ensure the important text and navigation in your site is in HTML, not
  [in images](/search/blog/2006/12/ses-chicago-using-images), and make sure all images
  have alt text that describe them.
- If you use Flash, use it only when needed. Particularly, don't put all of the text from your
  site in Flash. An ideal Flash-based site has pages with HTML text and Flash accents. If you use
  Flash for your home page, make sure that the navigation into the site is in HTML.

## Be descriptive

- Make sure each page has a unique
  [title tag](https://www.w3schools.com/tags/tag_title.asp) and
  [meta description tag](https://www.w3schools.com/tags/tag_meta.asp)
  that aptly describe the page.
- Make sure the important elements of your pages (for instance, your company name and the main
  topic of the page) are in HTML text.
- Make sure the words that searchers will use to look for you are on the page.

## Keep the site crawlable

- If possible,
  [avoid frames](https://www.google.com/support/webmasters/bin/answer.py?answer=34445).
  Frame-based sites don't allow for unique URLs for each page, which makes indexing each page
  separately problematic.
- Ensure the server returns a `404` status code for pages that aren't found.
  Some servers are
  [configured to return a `200` status code](/search/docs/crawling-indexing/troubleshoot-crawling-errors#soft-404-errors),
  particularly with custom error messages and this can result in search engines spending time
  crawling and indexing non-existent pages rather than the valid pages of the site.
- Avoid infinite crawls. For instance, if your site has an infinite calendar, add a
  [`nofollow` attribute](/search/docs/crawling-indexing/qualify-outbound-links)
  to links to dynamically-created future calendar pages. Each search engine may interpret the
  `nofollow` attribute differently, so check with the help documentation for each.
  Alternatively, you could use the
  [`nofollow` `meta` tag](/search/docs/crawling-indexing/robots-meta-tag#nofollow)
  to ensure that search engine spiders don't crawl any outgoing links on a page, or use
  robots.txt to prevent search engines from crawling URLs that can lead to infinite loops.
- If your site uses session IDs or cookies, ensure those are not required for crawling.
- If your site is dynamic, avoid using excessive parameters and use friendly URLs when you can.
  Some content management systems enable you to rewrite URLs to friendly versions.

See our
[tips for creating a Google-friendly site](/search/docs/fundamentals/seo-starter-guide)
and [webmaster guidelines](/search/docs/essentials) for more information on designing
your site for maximum crawlability and usability.

If you will be at SES London, I'd love for you to come by and hear more. And check out the other
Googlers' sessions too:

## Tuesday, February 13th

[Auditing Paid Listings and Clickfraud Issues](https://www.searchenginestrategies.com/sew/london07/agenda.html#aplppc);
10:45 - 12:00; Shuman Ghosemajumder, Business Product Manager for Trust and Safety

## Wednesday, February 14th

[A Keynote Conversation](https://www.searchenginestrategies.com/sew/london07/agenda2.html#keynote);
9:00 - 9:45; Matt Cutts, Software Engineer
[Successful Site Architecture](https://www.searchenginestrategies.com/sew/london07/agenda2.html#ssa);
10:30 - 11:45; Vanessa Fox, Product Manager, Webmaster Central
[Google University](https://services.google.com/events/ses_london07);
12:45 - 1:45
[Converting Visitors into Buyers](https://www.searchenginestrategies.com/sew/london07/agenda2.html#cvib);
2:45 - 4:00; Brian Clifton, Head of Web Analytics, Google Europe
[Search Advertising Forum](https://www.searchenginestrategies.com/sew/london07/agenda2.html#saf);
4:30 - 5:45; David Thacker, Senior Product Manager

## Thursday, February 15th

[Meet the Crawlers](https://www.searchenginestrategies.com/sew/london07/agenda3.html#mtc);
9:00 - 10:15; Dan Crow, Product Manager
[Web Analytics and Measuring Successful Overview](https://www.searchenginestrategies.com/sew/london07/agenda3.html#wamso);
1:15 - 2:30; Brian Clifton, Head of Web Analytics, Google Europe
[Search Advertising Clinic](https://www.searchenginestrategies.com/sew/london07/agenda3.html#sac);
1:15 - 2:30; Will Ashton, Retail Account Strategist
[Site Clinic](https://www.searchenginestrategies.com/sew/london07/agenda3.html#siteclinic_2);
3:00 - 4:15; Sandeepan Banerjee, Sr. Product Manager, Indexing
