---
title: "Making the Internet safer and faster: Introducing reCAPTCHA Android API"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2017-06-making-internet-safer-and-faster"
url: "https://developers.google.com/search/blog/2017/06/making-internet-safer-and-faster"
canonical: "https://developers.google.com/search/blog/2017/06/making-internet-safer-and-faster"
author: "Wei Liu, Product Manager, reCAPTCHA"
published: "2017-06-08T00:00:00+00:00"
updated: "2017-06-08T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2017_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:30:31+00:00"
status_code: 200
html_hash: "fa48a310d84cebf983b7296fdecded6112586e1ceb8f624dfed88fc8861f3220"
clean_word_count: 381
clean_char_count: 2550
---
# Making the Internet safer and faster: Introducing reCAPTCHA Android API

When we launched reCAPTCHA ten years ago, we had a simple goal: enable users to visit the sites
they love without worrying about spam and abuse. Over the years, reCAPTCHA has changed quite a
bit. It evolved from the distorted text to
[street numbers](https://security.googleblog.com/2014/04/street-view-and-recaptcha-technology.html)
and names, then
[No CAPTCHA reCAPTCHA](https://security.googleblog.com/2014/12/are-you-robot-introducing-no-captcha.html)
in 2014 and Invisible reCAPTCHA in March this year.

![](/static/search/blog/images/import/5a3637448a1163bae0417577e635048c.gif)

By now, more than a billion users have benefited from reCAPTCHA and we continue to work to refine
our protections.

reCAPTCHA protects users wherever they may be online. As the use of mobile devices has grown
rapidly, it's important to keep the mobile applications and data safe. Today, on reCAPTCHA's tenth
birthday, we're glad to announce the first reCAPTCHA
[Android API](https://developer.android.com/training/safetynet/recaptcha)
as part of Google Play Services.

With this API, reCAPTCHA can better tell human and bots apart to provide a streamlined user
experience on mobile. It will use our newest Invisible reCAPTCHA technology, which runs risk
analysis behind the scene and has enabled millions of human users to pass through with zero click
everyday. Now mobile users can enjoy their apps without being interrupted, while still staying
away from spam and abuse.

![](/static/search/blog/images/import/e38d8398057fd6aa474d392591e73c9a.gif)

reCAPTCHA Android API is included with Google
[SafetyNet](https://developer.android.com/training/safetynet/index),
which provides services like device attestation and safe browsing to protect mobile apps. Mobile
developers can do both the device and user attestations in the same API to mitigate security risks
of their apps more efficiently. This adds to the
[diversity of security protections](https://security.googleblog.com/2017/03/diverse-protections-for-diverse.html)
on Android:
[Google Play Protect](https://blog.google/products/android/google-play-protect/)
to monitor for potentially harmful applications, device encryption, and regular security updates.
Please
[visit our site](/recaptcha/docs/versions)
to learn more about how to integrate with the reCAPTCHA Android API, and keep an eye out for our
iOS library.

The journey of reCAPTCHA continues: we'll make the Internet safer and easier to use for everyone
(except bots).
