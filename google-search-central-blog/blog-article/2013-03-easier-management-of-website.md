---
title: "Easier management of website verifications"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2013-03-easier-management-of-website"
url: "https://developers.google.com/search/blog/2013/03/easier-management-of-website"
canonical: "https://developers.google.com/search/blog/2013/03/easier-management-of-website"
author: "Pierre Far"
published: "2013-03-21T00:00:00+00:00"
updated: "2013-03-21T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2013_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:21:16+00:00"
status_code: 200
html_hash: "57c4c782abae8521348b75894d82d3c2fb297d8e8d28955250437ff16bbb055c"
clean_word_count: 369
clean_char_count: 2412
---
# Easier management of website verifications

To help webmasters manage the
[verified](https://support.google.com/webmasters/answer/9008080)
owners for their websites in
[Webmaster Tools](https://search.google.com/search-console),
we've recently introduced three new features:

- **Verification details view**: You can now see the methods used to verify an
  owner for your site. In the Manage owners page for your site, you can now find the new
  Verification details link. This screenshot shows the verification details of a user who is
  verified using both an HTML file uploaded to the site and a `meta` tag:

  ![Verification details view in Webmaster Tools](/static/search/blog/images/archived_1_verification-details-dialog.png)

  Where appropriate, the Verification details will have links to the correct URL on your site
  where the verification can be found to help you find it faster.
- **Requiring the verification method be removed from the site before unverifying an
  owner**: You now need to remove the verification method from your site before
  [unverifying an owner](https://support.google.com/webmasters/answer/7687615)
  from Webmaster Tools. Webmaster Tools now checks the method that the owner used to verify
  ownership of the site, and will show an error message if the verification is still found. For
  example, this is the error message shown when an unverification was attempted while the DNS
  `CNAME` verification method was still found on the DNS records of the domain:

  ![An error showing that unverification was unsuccessful](/static/search/blog/images/archived_1_Unverify_blocked_-_CNAME.png)
- **Shorter `CNAME` verification string**: We've slightly modified the
  `CNAME` verification string to make it shorter to support a larger number of DNS
  providers. Some systems limit the number of characters that can be used in DNS records, which
  meant that some users were not able to use the
  [`CNAME` verification method](https://support.google.com/webmasters/answer/9008080).
  We've now made the `CNAME` verification method have a fewer number of characters.
  Existing `CNAME` verifications will continue to be valid.

We hope this changes make it easier for you to use Webmaster Tools. As always, please post in our
[Verification forum](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:search_console))
if you have any questions or feedback.
