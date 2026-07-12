---
title: "Verifying your site: trouble with 404 pages"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2005-09-verifying-your-site-trouble-with-404"
url: "https://developers.google.com/search/blog/2005/09/verifying-your-site-trouble-with-404"
canonical: "https://developers.google.com/search/blog/2005/09/verifying-your-site-trouble-with-404"
author: "Vanessa Fox"
published: "2005-09-07T00:00:00+00:00"
updated: "2005-09-07T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2005_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:43:51+00:00"
status_code: 200
html_hash: "1a071d4726e2b4236534b92315e706c53792a1bc02bceb728c071020a7f22340"
clean_word_count: 353
clean_char_count: 2020
---
# Verifying your site: trouble with 404 pages

You want to
[verify your site](https://support.google.com/webmasters/answer/9008080)
so you can view additional statistics. You click the verify link beside the site on the My
Sitemaps page, create the file we ask for, upload it to your server, and click the Check Status
button. And then you see this error message:

**We've detected that your `404 (file not found)` error page returns a status of
`200 (OK)` in the header.**

What should you do?

[This error](https://support.google.com/webmasters/answer/9008080#verificationfileconfigerror)
means that we've detected that your server returns a status of OK when the requested file is not
found. This is the same status that the server returns when the file exists. When we look for
the verification file, we can't tell if your server is returning a status of OK because it finds
the file, or because it can't find the file. This means we are unable to verify your site.

Modify your web server configuration to return a status of `404 (file not found)` in
the header of `404` pages. If your site is hosted, ask your hosting company to do this.

Make sure that if your server returns a custom error page when a requested file is not found,
that page returns a `404` status in the header. And make sure that the server doesn't
redirect requests that return "file not found" to a valid page of your site, such as your home
page. This configuration returns a redirect status code (such as `301` or
`302`) rather than the correct `404` status code.

You can read more about
[HTTP status codes](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html).
If you don't have a mechanism for checking the headers that your server returns, you can do a
search for terms such as
[check server header tool](https://www.google.com/search?q=check%20server%20header%20tool)
to find online tools that will check this for you.

Once your web server is configured correctly, try to verify your site again and we'll check the
configuration.
