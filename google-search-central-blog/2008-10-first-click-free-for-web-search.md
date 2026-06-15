---
title: "First Click Free for Web Search"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-10-first-click-free-for-web-search"
url: "https://developers.google.com/search/blog/2008/10/first-click-free-for-web-search"
canonical: "https://developers.google.com/search/blog/2008/10/first-click-free-for-web-search"
author: "John Mueller"
published: "2008-10-17T00:00:00+00:00"
updated: "2008-10-17T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:54:36+00:00"
status_code: 200
html_hash: "86f379bfd43bdd94c9fe833875660ed0d60f3dc2b695eb2db064d98f3119c27d"
clean_word_count: 692
clean_char_count: 4218
---
# First Click Free for Web Search

While working on
[our mission](https://www.google.com/corporate/)
to organize the world's information and make it universally accessible and useful, we sometimes
run into situations where important content is not publicly available. In order to help users find
and access content that may require registration or a subscription, Google offers an option to
web and news publishers called "First Click Free." First Click Free has two main goals:

1. To include highly relevant content in Google's search index. This provides a better experience
   for Google users who may not have known that content existed.
2. To provide a promotion and discovery opportunity for publishers with restricted content.

First Click Free is designed to protect your content while allowing you to include it Google's
search index. To implement First Click Free, you must allow all users who find your page through
Google search to see the full text of the document that the user found in Google's search results
and that Google's crawler found on the web without requiring them to register or subscribe to see
that content. The user's first click to your content is available without payment and does not
require logging in. You may, however, block the user with a login or payment or registration
request when they try to click away from that page to another section of your content site.

## Guidelines

Webmasters wishing to implement First Click Free should follow these guidelines:

- All users who click a Google search result to arrive at your site should be allowed to see the
  full text of the content they're trying to access.
- The page displayed to all users who visit from Google must be identical to the content that is
  shown to Googlebot.
- If a user clicks to a multi-page article, the user must be able to view the entire article. To
  allow this, you could display all of the content on a single page—you would need to do this for
  both Googlebot and for users. Alternately, you could use cookies to make sure that a user can
  visit each page of a multi-page article before being asked for registration or payment.

## Implementation Suggestions

To include your restricted content in Google's search index, our crawler needs to be able to
access that content on your site. Keep in mind that Googlebot cannot access pages behind
registration or login forms. You need to configure your website to serve the full text of each
document when the request is
[identified as coming from Googlebot](/search/docs/crawling-indexing/verifying-googlebot)
via the user agent and IP-address. It's equally important that your
[robots.txt file](/search/docs/crawling-indexing/robots/create-robots-txt)
allows access of these URLs by Googlebot.

When users click a Google search result to access your content, your web server will need to check
the "[`Referer`](https://tools.ietf.org/html/rfc2616#section-14.36)"
HTTP request header field. When the referring URL is on a Google domain, like
`www.google.com` or `www.google.de`, your site will need to display the full
text version of the page instead of the protected version of the page that is otherwise shown.
Most web servers have instructions for implementing this type of behavior.

## Frequently Asked Questions

Q: Can I allow Googlebot to access some restricted content pages but not others?
A: Yes.

Q: Can I limit the number of restricted content pages that an individual user can access on my
site via First Click Free?
A: No. Any user arriving at your site from a Google search results page should be shown the full
text of the requested page.

Q: Can First Click Free URLs be submitted using
[Sitemap files](/search/docs/crawling-indexing/sitemaps/overview)?
A: Yes. Simply [create](/search/docs/crawling-indexing/sitemaps/build-sitemap) and
[submit](/search/docs/crawling-indexing/sitemaps/overview) your Sitemap file as usual.

Q: Is First Click Free content guaranteed inclusion in the Google Index?
A: No. Google does not guarantee inclusion in the web index.

Do you have any more questions or comments? Come on over to the
[Google Webmaster Help forum](https://support.google.com/webmasters/community)
and join the discussion!
