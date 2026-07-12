---
title: "Verifying a Blogger blog in Webmaster Tools"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2009-10-verifying-blogger-blog-in-webmaster"
url: "https://developers.google.com/search/blog/2009/10/verifying-blogger-blog-in-webmaster"
canonical: "https://developers.google.com/search/blog/2009/10/verifying-blogger-blog-in-webmaster"
author: "Jonathan Simon, Webmaster Trends Analyst"
published: "2009-10-22T00:00:00+00:00"
updated: "2009-10-22T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:01:55+00:00"
status_code: 200
html_hash: "5ec2dbaf207fbe97162390bcf5cf7e49b5bdaee00f8619a3774016104b8cef50"
clean_word_count: 282
clean_char_count: 1751
---
# Verifying a Blogger blog in Webmaster Tools

You may have seen our recent announcement of changes to the verification system in Webmaster
Tools. One side effect of this change is that blogs hosted on Blogger (that haven't yet been
verified) will have to use the `meta` tag verification method rather than the "one-click"
integration from the Blogger dashboard. The "Webmaster Tools" auto-verification link from the
Blogger dashboard is no longer working and will soon be removed. We're working to reinstate an
automated verification approach for Blogger hosted blogs in the future, but for the time being we
wanted you to be aware of the steps required to verify your Blogger blog in Webmaster Tools.

## Step-By-Step Instructions

In Webmaster Tools:

1. Click the "Add a site" button on the Webmaster Tools Home page
2. Enter your blog's URL (for example, googlewebmastercentral.blogspot.com) and click the
   "Continue" button to go to the Manage verification page
3. Select the "Meta tag" verification method and copy the `meta` tag provided

In Blogger

4. Go to your blog and sign in
5. From the Blogger dashboard click the "Layout" link for the blog you're verifying
6. Click the "Edit HTML" link under the "Layout" tab which will allow you to edit the HTML for
   your blog's template
7. Paste the `meta` tag (copied in step 3) immediately after the `<head>` element
   within the template HTML and click the "SAVE TEMPLATE" button
![](/static/search/blog/images/import/bece6ff93b3c709d6f7ffab2033f6b15.png)

In Webmaster Tools

8. On the Manage Verification page, confirm that "Meta tag" is selected as the verification
   method and click the "Verify" button

Your blog should now be verified. You're ready to start using Webmaster Tools!
