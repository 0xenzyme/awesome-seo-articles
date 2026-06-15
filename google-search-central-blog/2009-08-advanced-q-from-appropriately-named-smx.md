---
title: "Advanced Q&A; from (the appropriately-named) SMX Advanced"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2009-08-advanced-q-from-appropriately-named-smx"
url: "https://developers.google.com/search/blog/2009/08/advanced-q-from-appropriately-named-smx"
canonical: "https://developers.google.com/search/blog/2009/08/advanced-q-from-appropriately-named-smx"
author: "Susan Moskwa"
published: "2009-08-06T00:00:00+00:00"
updated: "2009-08-06T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:59:36+00:00"
status_code: 200
html_hash: "dd46b1f08dfcc3d38b8151d41961fc3c1874c4b804aa8095e2079560c921d464"
clean_word_count: 891
clean_char_count: 5411
---
# Advanced Q&A; from (the appropriately-named) SMX Advanced

Earlier this summer
[SMX Advanced](https://searchmarketingexpo.com/advanced)
landed once again in our fair city—Seattle—and it was indeed advanced. I got a number of questions
at some Q&A panels that I had to go back and do a little research on. Here, as promised, are
answers:

**We hear that Google's now doing a
[better job](/search/blog/2009/06/flash-indexing-with-external-resource)
of
[indexing Flash content](/search/blog/2008/06/improved-flash-indexing). If I have a
Flash file that pulls in content from an external file and the external file is blocked by
[robots.txt](/search/docs/crawling-indexing/robots/intro), will that content be indexed in the
Flash (which is *not* blocked by robots.txt)? Or will Google not be able to index that
content?**
We won't be able to access that content if it's in a file that's disallowed by robots.txt; so even
though that content would be visible to humans (via the Flash), search engine crawlers wouldn't
be able to access it. For more details, see our blog post on
[indexing Flash that loads external resources](/search/blog/2009/06/flash-indexing-with-external-resource).

**Sites that customize content based on user behavior or clickstream are becoming more common.
If a user clicks through to my site from a search results page, can I customize the content of
that page or redirect the user based on the terms in their search query? Or is that considered
[cloaking](/search/docs/essentials/spam-policies#cloaking)? For example, if someone
searches for "vintage cameo pendants" but clicks on my site's general vintage jewelry page, can
I redirect that user to my vintage cameo-specific page since I know that's what they were
searching for?**
If you're redirecting or returning different content to the user than what Googlebot would see on
that URL (for example, based on the google.com referrer or query string), we consider that
cloaking. If the searcher decided to click on the 'vintage jewelry' result, you should show
them the page they clicked on even if you think a different page might be better. You can always
link between related pages on your website (that is, link to your 'vintage jewelry' page from
your 'vintage cameos' page and vice versa, so that anyone landing on those pages from any source
can cross-navigate); but we don't believe you should make that decision for the searcher.

Even though it involves showing different content to different visitors, Google considers
ethical website testing (such as A/B or multivariate testing) a legitimate practice that does
not violate Google's
[guidelines](/search/docs/essentials). One reason for
this is because, while search engines may only see the original content of the page and not the
variations, there's also a percentage of human users who see that same content; so the technique
doesn't specifically target search engines.

However, some testing services recommend running 100% of a site's traffic through the winning
combination for awhile after an experiment has completed, to verify that conversion rates stay
high. How does this fit in with Google's view of cloaking?

Running 100% of traffic through one combination for a brief period of time in order to verify
your experiment's results is fine. However, as our
[article on this subject](https://www.google.com/support/websiteoptimizer/bin/answer.py?answer=72507)
states, "if we find a site running a single non-original combination at 100% for a number of
months... we may remove that site from our index." If you want to confirm the results of your
experiment but are worried about "how long is too long," consider running a follow-up experiment
in which you send most of your traffic through your winning combination while still sending a
small percentage to the original page as a control.
[This is what Google recommends](https://www.google.com/support/websiteoptimizer/bin/answer.py?answer=61401)
with its own testing tool, Website Optimizer.

**If the character encoding specified in a page's HTTP header is different from that specified
in the `<meta equiv="Content-Type">` tag, which one will Google pay attention
to?**
We take a look at both of these, and also do a bit of processing/guessing on our own based on the
content of the page. Most major browsers prioritize the encoding specified in the HTTP header over
that specified in the HTML, if both are valid but different. However, if you're aware that they're
different, the best answer is to fix one of them!

**How does Google handle triple-byte UTF-8-encoded international characters in a URL (such as
Chinese or Japanese characters)? These types of URLs break in some applications; is Google able
to process them correctly? Does Google understand keywords that are encoded this way—that is,
can you understand that `www.example.com/%E9%9D%B4` is just as relevant to shoes as
`www.example.com/shoes`is?**
We can correctly handle percent-escaped UTF-8 characters in the URL path and in query parameters,
and we understand keywords that are encoded in this way. For international characters in a domain
name, we recommend using
[punycode](https://www.google.com/search?q=punycode)
rather than percent-encoding, because some older browsers (such as IE6) don't support non-ASCII
domain names.

Have a question of your own? Join our
[discussion forum](https://support.google.com/webmasters/community).
