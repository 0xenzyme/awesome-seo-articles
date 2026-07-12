---
title: "Do 404 errors hurt my site?"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-05-do-404s-hurt-my-site"
url: "https://developers.google.com/search/blog/2011/05/do-404s-hurt-my-site"
canonical: "https://developers.google.com/search/blog/2011/05/do-404s-hurt-my-site"
author: "Susan Moskwa"
published: "2011-05-02T00:00:00+00:00"
updated: "2011-05-02T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:12:50+00:00"
status_code: 200
html_hash: "9fc47e868f7ee3fab998c482a85900f794df6ab88d0c443180abee044c964892"
clean_word_count: 1480
clean_char_count: 8325
---
# Do 404 errors hurt my site?

So there you are, minding your own business, using Webmaster Tools to check out how awesome your
site is... but, wait! The
[Crawl errors](https://support.google.com/webmasters/answer/7440203)
page is full of
[`404 (Not found)` errors](/search/blog/2008/08/its-404-week-at-webmaster-central)!
*Is disaster imminent??*

![The Crawl Errors feature in Webmaster Tools](/static/search/blog/images/archived_1_Screen_shot_2011-04-13_at_3.59.27_PM.png)

Fear not, my young padawan. Let's take a look at `404` errors and how they do (or do
not) affect your site:

**Q: Do the `404` errors reported in Webmaster Tools affect my site's ranking?**
A: `404` errors are a perfectly normal part of the web; the Internet is always
changing, new content is born, old content dies, and when it dies it (ideally) returns a
`404` HTTP response code. Search engines are aware of this; we have `404`
errors on our own sites, as you can see above, and we find them all over the web. In fact, we
actually *prefer* that, when you get rid of a page on your site, you make sure that it
returns a proper `404` or `410` response code (rather than a `soft
404`). Keep in mind that in order for our crawler to see the HTTP response code of a
URL, it has to be able to crawl that URL—if the URL is blocked by your robots.txt file we won't be
able to crawl it and see its response code. The fact that some URLs on your site no longer exist or
return `404` errors does not affect how your site's other URLs (the ones that return
[`200 (Success)`
status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)) perform in our search results.

**Q: So `404` errors don't hurt my website at all?**
A: If some URLs on your site `404`, this fact alone does not hurt you or count against
you in Google's search results. However, there may be other reasons that you'd want to address
certain types of `404` errors. For example, if some of the pages that
`404` are pages you actually care about, you should look into why we're seeing
`404` errors when we crawl them! If you see a misspelling of a legitimate URL
(www.example.com/awsome instead of www.example.com/awesome), it's likely that someone intended to
link to you and simply made a typo. Instead of returning a `404`, you could
`301` redirect the misspelled URL to the correct URL and capture the intended traffic
from that link. You can also make sure that, when users do land on a `404` page on
your site, you
[help them find what they were looking for](/search/docs/crawling-indexing/http-network-errors#pagegone)
rather than just saying "`404` Not found."

**Q: Tell me more about "`soft 404` errors."**
A: A
[`soft 404`](/search/docs/crawling-indexing/troubleshoot-crawling-errors#soft-404-errors)
is when a web server returns a response code other than `404` (or `410`) for
a URL that doesn't exist. A common example is when a site owner wants to return
[a pretty `404` page with helpful information for their users](/search/blog/2008/08/make-your-404-pages-more-useful),
and thinks that in order to serve content to users, they have to return a `200`
response code. Not so! You can return a `404` response code *while* serving
whatever content you want. Another example is when a site redirects any unknown URLs to their
home page instead of returning `404` errors. Both of these cases can have negative
effects on our understanding and indexing of your site, so we recommend making sure your server
returns the proper response codes for nonexistent content. Keep in mind that *just because a
page **says** "`404` Not Found," doesn't mean it's actually returning a
`404` HTTP response code*—use the
[Fetch as Googlebot](https://www.google.com/support/webmasters/bin/answer.py?answer=158587)
feature in Webmaster Tools to double-check. If you don't know how to configure your server to
return the right response codes, check out your web host's help documentation.

**Q: How do I know whether a URL should `404`, or `301`, or
`410`?**
A: When you remove a page from your site, think about whether that content is moving somewhere
else, or whether you no longer plan to have that type of content on your site. If you're moving
that content to a new URL, you should `301` redirect the old URL to the new URL—that
way when users come to the old URL looking for that content, they'll be automatically redirected
to something relevant to what they were looking for. If you're getting rid of that content
entirely and don't have anything on your site that would fill the same user need, then the old URL
should return a `404` or `410`. Currently Google treats
`410 (Gone)` the same as `404 (Not found)`, so it's immaterial to us whether
you return one or the other.

**Q: Most of my `404` errors are for bizarro URLs that never existed on my site.
What's up with that? Where did they come from?**
A: If Google finds a link somewhere on the web that points to a URL on your domain, it may try to
crawl that link, whether any content actually exists there or not; and when it does, your server
*should* return a `404` if there's nothing there to find. These links could be
caused by someone making a typo when linking to you, some type of misconfiguration (if the links
are automatically generated, for example, by a CMS), or by Google's increased efforts to recognize
and crawl links embedded in JavaScript or other embedded content; or they may be part of a quick
check from our side to see how your server handles unknown URLs, to name just a few. If you see
`404` errors reported in Webmaster Tools for URLs that don't exist on your site, you
can safely ignore them. We don't know which URLs are important to you vs. which are supposed to
`404`, so we show you *all* the `404` errors we found on your site and
let you decide which, if any, require your attention.

**Q: Someone has scraped my site and caused a bunch of `404` errors in the
process. They're all "real" URLs with other code tacked on, like
`https://www.example.com/images/kittens.jpg" width="100" height="300" alt="kittens"/>`
Will this hurt my site?**
A: Generally you don't need to worry about "broken links" like this hurting your site. We
understand that site owners have little to no control over people who scrape their site, or who
link to them in strange ways. If you're a whiz with the
[regex](https://www.google.com/search?q=define:regex),
you could consider
[redirecting these URLs](/search/docs/crawling-indexing/301-redirects), but generally
it's not worth worrying about. Remember that you can also file a
[takedown request](https://www.google.com/dmca)
when you believe someone is stealing original content from your website.

**Q: Last week I fixed all the `404` errors that Webmaster Tools reported, but
they're still listed in my account. Does this mean I didn't fix them correctly? How long will it
take for them to disappear?**
A: Take a look at the 'Detected' column on the Crawl errors page—this is the most recent date on
which we detected each error. If the date(s) in that column are from before the time you fixed the
errors, that means we haven't encountered these errors since that date. If the dates are more
recent, it means we're continuing to see these `404` errors when we crawl.

After implementing a fix, you can check whether our crawler is seeing the new response code by
using
[Fetch as Googlebot](https://www.google.com/support/webmasters/bin/answer.py?answer=158587).
Test a few URLs and, if they look good, these errors should soon start to disappear from your
list of Crawl errors.

**Q: Can I use Google's URL removal tool to make `404` errors disappear from my
account faster?**

A: No; the URL removal tool removes URLs from Google's search results, not from your Webmaster
Tools account. It's designed for urgent removal requests only, and using it isn't necessary when a
URL already returns a `404`, as such a URL will drop out of our search results
naturally over time. See the bottom half of
[this blog post](/search/blog/2010/05/url-removal-explained-part-iv-tracking)
for more details on what the URL removal tool can and can't do for you.

Still want to know more about `404` errors? Check out
[`404` week](/s/results/search/blog?q=%22404+week%22) from our blog, or drop
by our
[Webmaster Help Forum](https://support.google.com/webmasters/community).
