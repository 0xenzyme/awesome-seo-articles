---
title: "Good maintenance"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-03-good-housekeeping"
url: "https://developers.google.com/search/blog/2008/03/good-housekeeping"
canonical: "https://developers.google.com/search/blog/2008/03/good-housekeeping"
author: "Michael Wyszomierski"
published: "2008-03-20T00:00:00+00:00"
updated: "2008-03-20T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:51:42+00:00"
status_code: 200
html_hash: "715dc8803c6fb1dbcf7f977936ed03be8720de916844b31541b9a772018a5448"
clean_word_count: 1000
clean_char_count: 6112
---
# Good maintenance

Today's the first day of spring in the Northern Hemisphere, so now is a perfect time to start your
spring cleaning. But as a webmaster, your chores don't end after you've cleaned the
garage—you'll probably also want to do some cleaning on your server as well.

## Exterior

Before we get to the interior, step outside, and see how your site looks from the street—or
in Google search results. Just head on over to your nearest Google search box, and do a site
search on your site using the query format site:example.com. Just like
you keep your street number visible on your house, and maybe even your name on the mailbox, check
to see that your visitors can easily identify your site and its contents from the title and
snippet listed in Google. If you'd like to improve your current appearance, try out the
[content analysis](/search/blog/2007/12/new-content-analysis-and-sitemap)
feature in
[Webmaster Tools](https://search.google.com/search-console),
and read up on how to influence your
[snippets](/search/blog/2007/09/improve-snippets-with-meta-description).

![google site search operator](/static/search/blog/images/import/94659ee72572d4aa5064fcc81883c90b.png)

Speaking of making your address visible, how are you listed? My name is Michael, but I'll also
answer to Mike or even Wysz. However, I only expect to be listed once in the phone book.
Similarly, your site may have pages that can be accessed from multiple URLs: for instance,
`www.example.com` and `example.com`. To consolidate your site's listings in
Google, use [`301` redirects](/search/docs/crawling-indexing/301-redirects)
to tell Google (and other search engines) how you'd prefer your pages to be listed. You can also
easily
[let Google know about your preferred domain](/search/blog/2006/09/setting-preferred-domain)
via Webmaster Tools. And just like I'd want my bank to understand that deposits to Mike and
Michael should route to the same account, those redirects can help Google appropriately
consolidate link properties (like PageRank) to the destination page.

## Interior

No matter how clean your home is, all that work may go unnoticed if your visitors can't get in the
door or find their way around. Review your site's appearance and functionality on multiple
browsers to make sure that all of your visitors get the experience you've worked so hard to
design. Not everyone uses Internet Explorer, so it's a good idea to test using browsers
representing different layout engines. Firefox, Safari, and Opera all see things differently, and
these three browsers likely control how at least 20% of your users are experiencing the web. For
some sites it can be dramatically higher—The New York Times
[recently reported](https://bits.blogs.nytimes.com/2008/02/22/the-browser-choices-we-make/)
that around 38% of their online readers used either Firefox or Safari.

If your site requires the use of plug-ins, check to see how this additional content behaves across
different operating systems. Keep in mind that many people only update their operating system with
the purchase of a new computer, so go back a version or two and see how your site works on
yesterday's OS. And to make sure you're not completely shutting out visitors with
[limited capabilities](/search/blog/2008/03/tips-for-making-information-universally),
try to navigate your site without using images,
[Flash](/search/blog/2007/07/best-uses-of-flash) or
[JavaScript](/search/blog/2007/11/spiders-view-of-web-20). If you want to see where
Google may be having trouble getting in, check Webmaster Tools to see if there have been any
[crawl errors](https://support.google.com/webmasters/answer/9679690)
reported for your site.

## Taking out the trash

Unfortunately, many of us have hosted unwelcome guests. If they left a mess behind, do your future
visitors a favor and get rid of the garbage. Tear out spammed guestbook pages. Pull out those
weeds in your forum that were planted by an off-topic advertiser. And while you're throwing stuff
away, look out for any blank or abandoned pages. We've all had projects in the basement that never
got finished. If your site still shows URLs with one of those circa-1997 "under construction"
graphics or templates showing "Products > Shirts > Graphic T's: There are no graphic t's at
this time" and they're just gathering dust, it's probably safe to say you'll never get around to
finishing it. After you've collected the junk and corrected any broken links on your site, make
sure you let everyone know it's really gone by using the `404` HTTP status code. You
can check to see which code your server is returning by using the
[Live HTTP Headers](https://livehttpheaders.mozdev.org/)
extension for Firefox.

## Security and preventive maintenance

To prevent problems with future visitors, especially those who may try to come in your back door
at night, go through our
[checklist](/search/blog/2007/09/quick-security-checklist-for-webmasters)
to verify you've covered security basics.

If your site's maintenance tasks, such as upgrading software packages, make your content
temporarily unavailable, let your visitors know to "pardon the dust" by using the `503`
HTTP status code. This will let Google know to check back later, and not index your error page
as part of your site's content. If you're using WordPress, you can easily set up your message
along with the status code using the
[Maintenance Mode](https://sw-guide.de/wordpress/plugins/maintenance-mode/)
plug-in.

And speaking of intruders and software updates, you just never know when something will go wrong.
Before something does happen, now is a great time to evaluate your backup strategy. Like insurance
for your home, the effort and expense put into it is well worth the peace of mind alone, not to
mention if you ever actually need it. A good backup system archives your backups in a different
location than the working site, and happens automatically to avoid the problems of forgetfulness.
It's a great idea to make a backup of your site (including databases) right before running any
software updates or making a major change.
