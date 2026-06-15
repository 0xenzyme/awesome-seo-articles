---
title: "Switching to the new website verification API"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2013-12-switching-to-new-website-verification"
url: "https://developers.google.com/search/blog/2013/12/switching-to-new-website-verification"
canonical: "https://developers.google.com/search/blog/2013/12/switching-to-new-website-verification"
author: "John Mueller"
published: "2013-12-23T00:00:00+00:00"
updated: "2013-12-23T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2013_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:23:22+00:00"
status_code: 200
html_hash: "f6507f5caf7d6470aa533c320cdf4aaf5fb699dea6b4f20d12cefc030c509574"
clean_word_count: 351
clean_char_count: 2451
---
# Switching to the new website verification API

Just over a year ago we introduced a new
[API for website verification](/site-verification)
for Google services. In the spirit of keeping things simple and focusing our efforts, we've
decided to deprecate the
[old verification API method](/webmaster-tools/docs/2.0/developers_guide_protocol#AD_Verifying)
on March 31st, 2014. The rest of the API will remain unchanged, this only affects the verification
method. For more information about verification in general, please see our
[site verification Help Center article](https://support.google.com/webmasters/answer/35179).

One advantage of upgrading to the new API for verification is that it uses the same client
libraries as most other Google APIs, which simplifies integration with other apps and tools.
Getting started is easy, especially if you're used to other Google APIs:

1. Download the
   [Google API client library](/site-verification/libraries)
   for your favorite programming language.
2. Learn about the
   [Site Verification API](/site-verification)
   and its methods.
3. Allow your users to authenticate with
   [OAuth](/identity/protocols/oauth2).
4. Start verifying!

If you can't wait to try it out and are a fan of command lines, here's a shortcut:

1. Download and install
   [oacurl](https://code.google.com/p/oacurl/).
2. Authenticate with a Google Account:

   ```
    $ java -cp oacurl-1.2.0.jar com.google.oacurl.Login \
   --scope https://www.googleapis.com/auth/siteverification
   ```
3. Request the verification information:

   ```
    $ echo '{ "verificationMethod": "FILE", "site": {
   "identifier": "https://www.example.com",
   "type": "SITE" } }' | \
   java -cp oacurl-1.2.0.jar com.google.oacurl.Fetch \
   'https://www.googleapis.com/siteVerification/v1/token' \
   --content-type JSON -X=POST
   ```
4. Create and add the file to your website, then verify:

   ```
    $ echo '{ "site": { "identifier": "https://www.example.com", "type": "SITE" } }' | \
   java -cp oacurl-1.2.0.jar com.google.oacurl.Fetch \
   'https://www.googleapis.com/siteVerification/v1/webResource?verificationMethod=FILE' \
   --content-type JSON -X=POST
   ```
5. Done!

We hope this API will make it easier to implement Google site verification in your projects.
Should you have any questions, you can post in our
[Webmaster Help Forum](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:search_console)).
