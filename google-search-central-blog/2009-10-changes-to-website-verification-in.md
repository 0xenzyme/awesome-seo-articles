---
title: "Changes to website verification in Webmaster Tools"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2009-10-changes-to-website-verification-in"
url: "https://developers.google.com/search/blog/2009/10/changes-to-website-verification-in"
canonical: "https://developers.google.com/search/blog/2009/10/changes-to-website-verification-in"
author: "Sean Harding, Software Engineer"
published: "2009-10-01T00:00:00+00:00"
updated: "2009-10-01T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:01:09+00:00"
status_code: 200
html_hash: "aa96f135db28fbd9a02a3f3d8ad74cf9707d33fb1aa80f118d259f39e7507190"
clean_word_count: 495
clean_char_count: 2981
---
# Changes to website verification in Webmaster Tools

If you use
[Webmaster Tools](https://search.google.com/search-console),
you're probably familiar with verifying ownership of your sites. Simply add a specific `meta` tag
or file to your site, click a button, and you're a verified owner. We've recently made a few small
improvements to the process that we think will make it easier and more reliable for you.

The first change is an improvement to the `meta` tag verification method. In the past, your
verification `meta` tag was partially based on the email address of your Google Account. That meant
that if you changed the email address in your account settings, your `meta` tags would also change
(and you'd become unverified for any sites you had used the old tag on). We've created a new
version of the verification `meta` tag which is unrelated to your email address. Once you verify
with a new `meta` tag, you'll never become unverified by changing your email address.

We've also revamped the way we do verification by HTML file. Previously, if your website returned
an HTTP status code other than `404` for non-existent URLs, you would be unable to use
the file verification method. A properly configured web server will return `404` for
non-existent URLs, but it turns out that a lot of sites have problems with this requirement. We've
simplified the file verification process to eliminate the checks for non-existent URLs. Now, you
just download the HTML file we provide and upload it to your site without modification. We'll
check the contents of the file, and if they're correct, you're done.

![the verification function in webmaster tools](/static/search/blog/images/import/e1e9e480381f673cd553eb2086e79103.png)

We hope these changes will make verification a little bit more pleasant. If you've already
verified using the old methods, don't worry! Your existing verifications will continue to work.
These changes only affect new verifications.

Some websites and software have features that help you verify ownership by adding the `meta` tag or
file for you. They may need to be updated to work with the new methods. For example,
[Google Sites](https://sites.google.com/)
doesn't currently handle the new `meta` tag verification method correctly. We're aware of that
problem and are working to fix it as soon as we can. If you discover other services that have
similar problems, please work with their maintainer to resolve the issue. We're sorry if this
causes any inconvenience.

This is just the first of several improvements we're working on for website verification. To give
you a heads up, in a future update, we'll begin showing the email addresses of all verified owners
of a given site to the other verified owners of that site. We think this will make it much easier
to manage sites with multiple verified owners. However, if you're using an email address you
wouldn't want the other owners of your site to see, now might be a good time to change it!
