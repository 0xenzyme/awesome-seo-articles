---
title: "Where's my data?"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-10-wheres-my-data"
url: "https://developers.google.com/search/blog/2008/10/wheres-my-data"
canonical: "https://developers.google.com/search/blog/2008/10/wheres-my-data"
author: "Susan Moskwa, Webmaster Trends Analyst"
published: "2008-10-20T00:00:00+00:00"
updated: "2008-10-20T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:55:24+00:00"
status_code: 200
html_hash: "f684dda8618f5cc2cc3fc4fd24842de06b02c54d21bb83f277d20bf6b59c78e8"
clean_word_count: 811
clean_char_count: 4770
---
# Where's my data?

Today we're going back to basics. We'll be answering the question: What is a website? ...Okay,
not exactly. But we will be looking into what a "website" means in the context of Webmaster Tools,
what kind of sites you can add to your Webmaster Tools account, and what data you can get from
different types of sites.

Why should you care? Well, the following are all questions that we've gotten from webmasters
recently:

- "I know my site has lots of incoming links; why don't I see any in my Webmaster Tools account?"
- "I see sitelinks for my site in Google's search results, but when I look in Webmaster Tools it
  says 'No sitelinks have been generated for your site.'"
- "Why does my Top search queries report still say 'Data is not available at this time'? My site
  has been verified for months."

In each of these cases, the answer was the same: the data was there, but the webmaster was
looking at the wrong "version" of their domain in Webmaster Tools.

The majority of tools and settings in Webmaster Tools operate on a per-site basis. This means
that when you're looking at, say, the
[Top search queries report](https://www.google.com/support/webmasters/bin/answer.py?answer=35252),
you're only seeing the top search queries for a particular site. Looking at the top queries for
`www.example.com` will show you different data than looking at the top queries for
`www.example.org`. Makes sense, right?

Not all websites have URLs in the form `www.example.com`, though. Your root URL may not
include the`www`subdomain (`example.com`); it may include a custom subdomain
(`rollergirl.example.com`); or your site may live in a subfolder, for example if it's
hosted on a hosting site that's available without payment
(`www.example.com/rollergirl/`). Since we want webmasters to be able to access our
tools regardless of how their site is hosted, you can add any combination of domain, subdomain(s),
and/or subfolder(s) as a "site" on your Webmaster Tools dashboard. Once you've
[verified your ownership](https://www.google.com/support/webmasters/bin/answer.py?answer=35179)
of that site, we'll show you the information we have for that particular piece of the web, however
big or small it may be. If you've verified your domain at the root level, we'll show you data for
that whole domain; if you've only verified a particular subfolder or subdomain, we'll only show
you data for that subfolder or subdomain. Take
[Blogger](https://www.blogger.com/)
as an example—someone who blogs with Blogger should only be able to have access to the data
for their own subdomain (`googlewebmastercentral.blogspot.com`), not the entire
`blogspot.com` domain.

What some people overlook is the fact that `www` is actually a subdomain. It's a very,
very common subdomain, and many sites serve the same content whether you access them with or
without the `www`; but the fact remains that `example.com` and
`www.example.com` are two different URLs and have the potential to serve different
content. For this reason, they're considered different sites in Webmaster Tools. Since they're
different sites—just like `www.example.com` and `www.example.org`—
*they can have different data*. When you're looking at the data for
`www.example.com` (with the`www`subdomain) you're not seeing the data for
`example.com` (without the subdomain), and vice versa.

## What can I do to make sure I'm seeing all my data?

- If you feel like you're missing some data, add both the`www`and the non-www version of your
  domain to your Webmaster Tools account. Take a look at the data for both sites.
- Do a `site:` search for your domain without the `www` (for example,
  `site:example.com`). This should return pages from your domain and any of your
  indexed subdomains (`www.example.com`, `rollergirl.example.com`, etc.).
  You should be able to tell from the results whether your site is mainly indexed with or without
  the `www` subdomain. The version that's indexed is likely to be the version that
  shows the most data in your Webmaster Tools account.
- Tell us whether you prefer for your site to be indexed with or without the `www` by
  [setting your preferred domain](https://www.google.com/support/webmasters/bin/answer.py?answer=44231).
- Let everyone else know which version you prefer by doing a
  [site-wide `301` redirect](/search/docs/crawling-indexing/301-redirects).

Even though `example.com` and `www.example.com` may *look* like
identical twins, any twins will be quick to tell you that they're not actually the same person.
:-) Now that you know, we urge you to give both your
`www` and non-www sites some love in Webmaster Tools, and—as usual—to post any
follow-up questions in our
[Webmaster Help Group](https://support.google.com/webmasters/community).
