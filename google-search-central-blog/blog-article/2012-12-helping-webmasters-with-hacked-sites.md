---
title: "Helping Webmasters with Hacked Sites"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2012-12-helping-webmasters-with-hacked-sites"
url: "https://developers.google.com/search/blog/2012/12/helping-webmasters-with-hacked-sites"
canonical: "https://developers.google.com/search/blog/2012/12/helping-webmasters-with-hacked-sites"
author: "Oliver Barrett"
published: "2012-12-12T00:00:00+00:00"
updated: "2012-12-12T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:20:44+00:00"
status_code: 200
html_hash: "a904cedf962787865645435696d6398c82c8aa2a31a8c2d473376b5111924f69"
clean_word_count: 801
clean_char_count: 5060
---
# Helping Webmasters with Hacked Sites

Having your website hacked can be a frustrating experience and we want to do everything we can to
help webmasters get their sites cleaned up and prevent compromises from happening again. With this
post we wanted to outline two common types of attacks as well as provide clean-up steps and
additional resources that webmasters may find helpful.

To best serve our users it's important that the pages that we link to in our search results are
safe to visit. Unfortunately, malicious third-parties may take advantage of legitimate webmasters
by hacking their sites to manipulate search engine results or distribute malicious content and
spam. We will alert users and webmasters alike by labeling sites we've detected as hacked by
displaying a "This site may be compromised" warning in our search results:

![Example search result with the 'This site may be compromised' label](/static/search/blog/images/import/b7eaa8108afb7d2caa9017c95a950d24.png)

We want to give webmasters the necessary information to help them clean up their sites as quickly
as possible. If you've verified your site in Webmaster Tools we'll also send you a message when
we've identified your site has been hacked, and when possible give you example URLs.

Occasionally, your site may become compromised to facilitate the distribution of malware. When we
recognize that, we'll identify the site in our search results with a label of
"This site may harm your computer" and browsers such as Chrome may display a warning when users
attempt to visit. In some cases, we may share more specific information in the Malware section of
Webmaster Tools. We also have
[specific tips for preventing and removing malware from your site](https://support.google.com/webmasters/bin/answer.py&answer=163633)
in our Help Center.

Two common ways malicious third-parties may compromise your site are the following:

## Injected Content

Hackers may attempt to influence search engines by injecting links leading to sites they own.
These links are often hidden to make it difficult for a webmaster to detect this has occurred.
The site may also be compromised in such a way that the content is only displayed when the site is
visited by search engine crawlers.

![Example of injected pharmaceutical content](/static/search/blog/images/import/2f238bededba57648db97502d1360d79.png)

If we're able to detect this, we'll send a message to your Webmaster Tools account with useful
details. If you suspect your site has been compromised in this way, you can check the content
your site returns to Google by using the
[Fetch as Google](https://support.google.com/webmasters/bin/answer.py&answer=158587)
tool. A few good places to look for the source of such behavior of such a compromise are
`.php` files, template files and CMS plugins.

## Redirecting Users

Hackers might also try to redirect users to spammy or malicious sites. They may do it to all users
or target specific users, such as those coming from search engines or those on mobile devices. If
you're able to access your site when visiting it directly but you experience unexpected redirects
when coming from a search engine, it's very likely your site has been compromised in this manner.

One of the ways hackers accomplish this is by modifying server configuration files (such as
Apache's `.htaccess`) to serve different content to different users, so it's a good
idea to check your server configuration files for any such modifications.

![An .htaccess rule snippet that checks for the referrer and redirects the user based on their origin](/static/search/blog/images/import/ff28a8f3c2e6baa0805516bbeb46748d.png)

This malicious behavior can also be accomplished by injecting JavaScript into the source code of
your site. The JavaScript may be designed to hide its purpose so it may help to look for terms
like `eval`, `decode`, and `escape`.

![Example of malicious JavaScript code](/static/search/blog/images/import/4f1d3098560ebe3c4b385985eb882983.png)

## Cleanup and Prevention

If your site has been compromised, it's important to not only clean up the changes made to your
site but to also address the vulnerability that allowed the compromise to occur. We have
instructions for
[cleaning your site](https://support.google.com/webmasters/bin/answer.py&answer=163634)
and
[preventing compromises](https://support.google.com/webmasters/bin/answer.py&answer=163635)
while your hosting provider and our
[Malware and Hacked sites](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:security_malware_hacked))
forum are great resources if you need more specific advice.

Once you've cleaned up your site you should submit a
[reconsideration request](https://www.google.com/webmasters/tools/reconsideration?pli=1)
that if successful will remove the warning label in our search results.

As always, if you have any questions or feedback, please tell us in the
[Webmaster Help Forum](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:security_malware_hacked)).
