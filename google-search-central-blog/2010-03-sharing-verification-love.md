---
title: "Sharing the verification love"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2010-03-sharing-verification-love"
url: "https://developers.google.com/search/blog/2010/03/sharing-verification-love"
canonical: "https://developers.google.com/search/blog/2010/03/sharing-verification-love"
author: "Sean Harding, Software Engineer"
published: "2010-03-03T00:00:00+00:00"
updated: "2010-03-03T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:05:23+00:00"
status_code: 200
html_hash: "3933660e6d3ada6ea67e78d5017dc5fe737db790481f27409b3294553a9959d9"
clean_word_count: 399
clean_char_count: 2400
---
# Sharing the verification love

Everything is more fun with a friend! We've just added a feature to
[Webmaster Tools Site Verification](https://www.google.com/webmasters/verification/)
to make it easier to share verified ownership of your websites.

In the past, if more than one person needed to be a verified owner of a website, they each had to
go through the `meta` tag or HTML file verification process. That works fine for some situations,
but for others it can be challenging. For example, what if you have twenty people who need to be
verified owners of your site? Adding twenty `meta` tags or HTML files could be pretty time
consuming. Our new verification delegation feature makes adding new verified owners a snap.

![the user delegation feature for site verifications in webmaster tools](/static/search/blog/images/import/4dc489fb22ffa2edda2111c69cbb1d2c.png)

Once you're a verified owner of a website, you can view the Verification Details page (linked from
[Webmaster Tools](https://search.google.com/search-console)
or the
[Verification home page](https://www.google.com/webmasters/verification/)).
That page will show you information about the site as well as a list of any other verified owners.
At the bottom of the list of owners, you'll now see a button labeled "Add a user...". Click that,
enter the user's email address, and that person will instantly become a verified owner for the
site! You can remove that ownership at any time by clicking the "Unverify" link next to the
person's email address on the Details page.

There are a few important things to keep in mind as you use this feature. First, each site must
always have at least one owner who has verified directly (via `meta` tag or HTML file). If all of
the directly verified owners become unverified, the delegated owners may also become unverified.
Second, you can only delegate ownership to people with
[Google Accounts](https://www.google.com/accounts/). Finally,
remember that anyone you delegate ownership to will have exactly the same access you have. They
can delegate to more people, submit URL Removal requests and manage Sitelinks in Webmaster Tools,
etc. Only delegate ownership to people you trust!

We hope this makes things a little easier for those of you who need more than one person to be a
verified owner of your site. As always, please visit the Webmaster Help Forum if you have any
questions.
