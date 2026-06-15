---
title: "Hey Google, I no longer have badware"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-08-hey-google-i-no-longer-have-badware"
url: "https://developers.google.com/search/blog/2008/08/hey-google-i-no-longer-have-badware"
canonical: "https://developers.google.com/search/blog/2008/08/hey-google-i-no-longer-have-badware"
author: "Written by Evan Tang, Search Quality Team"
published: "2008-08-22T00:00:00+00:00"
updated: "2008-08-22T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:53:43+00:00"
status_code: 200
html_hash: "ab9f664c2b4abd6ff4a2e310d11153d5f0ab0788bd4789cb6e0a97f3bb5711cb"
clean_word_count: 455
clean_char_count: 2999
---
# Hey Google, I no longer have badware

This post is for anyone who has been
[emailed or notified](/search/blog/2007/02/better-badware-notifications-for) by Google
about [badware](/search/blog/2006/11/badware-alerts-for-your-sites), received a
[badware warning](/search/blog/2007/01/about-badware-warnings) when browsing their own
site using Firefox, or has come across
[malware-labeled search results](https://support.google.com/websearch/answer/45449)
for their own site(s). As you know, these warnings are produced by our automated scanning systems,
which we've put in place to ensure the quality of our results by
[protecting our users](https://googleonlinesecurity.blogspot.com/2008/05/safe-browsing-diagnostic-to-rescue.html).
Whatever the case, if you are dealing with badware, here are a few recommendations that can help
you out.

![malware warning advisory interstitial page](/static/search/blog/images/archived_malware_warning_advisory.bmp)
![badware warning advisory interstitial page](/static/search/blog/images/archived_badware_warning.gif)

1. If you have badware, it usually means that your web server, your website, or a database used by
   your website has been compromised. We have a nifty post on
   [how to handle being hacked](/search/blog/2008/04/my-sites-been-hacked-now-what).
   Be very careful when inspecting for malware on your site so as to avoid exposing your computer
   to infection.
2. Once everything is clear and dandy, you can follow the steps in our post about
   [malware reviews via Webmaster Tools](/search/blog/2007/08/malware-reviews-via-webmaster-tools).
   Please note the screen shot on the previous post is outdated, and the new malware review form
   is on the Overview page and looks like this:

   ![malware review form in webmaster tools](/static/search/blog/images/archived_malware-clean2.png)

   Other programs, such as Firefox, also use our badware data and may not recognize the change
   immediately due to their caching of the data. So even if the badware label in search is
   removed, it may take some time for that to be visible in such programs.
3. Lastly, if you believe that your rankings were somehow affected by the malware, such as
   compromised content that violated our Webmaster Guidelines (that is, hacked pages with hidden
   pharmacy text links), you should fill out a
   [reconsideration request](/search/blog/2008/07/requesting-reconsideration-using-google).
   To clarify, reconsideration requests are usually used for when you notice issues stemming from
   violations of our Webmaster Guidelines and are separate from malware requests.

If you have additional questions, please review our
[documentation](/search/docs/monitor-debug/security/malware) or post to the
[discussion group](https://groups.google.com/group/stopbadware)
with the URL of your site. We hope you find this updated feature in
[Webmaster Tools](https://search.google.com/search-console)
useful in discovering and fixing any malware-related problems.
