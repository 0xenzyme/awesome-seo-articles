---
title: "Mo' better to also detect \"mobile\" user-agent"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2011-03-mo-better-to-also-detect-mobile-user"
url: "https://developers.google.com/search/blog/2011/03/mo-better-to-also-detect-mobile-user"
canonical: "https://developers.google.com/search/blog/2011/03/mo-better-to-also-detect-mobile-user"
author: "Maile Ohye"
published: "2011-03-30T00:00:00+00:00"
updated: "2011-03-30T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:11:55+00:00"
status_code: 200
html_hash: "8dc1d3ef21afb57c14af9513a4949b9e1c315816b4ca70287995caf79400b7b3"
clean_word_count: 338
clean_char_count: 2249
---
# Mo' better to also detect "mobile" user-agent

Here's a trending User-Agent detection misstep we hope to help you prevent: While it seems
completely reasonable to key off the string "android" in the User-Agent and then redirect users
to your mobile version, there's a small catch... Android tablets were just released! Similar to
mobile, the User-Agent on Android tablets also contains "android," yet tablet users usually prefer
the full desktop version over the mobile equivalent. If your site matches "android" and then
automatically redirects users, you may be forcing Android tablet users into a sub-optimal
experience.

As a solution for mobile sites, our Android engineers recommend to specifically
[detect "mobile" in the User-Agent string](https://android-developers.blogspot.com/2010/12/android-browser-user-agent-issues.html)
as well as "android." Let's run through a few examples.

With a User-Agent like this:

```
Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13
```

Since there is no "mobile" string, serve this user the desktop version (or a version customized
for Android large-screen touch devices). The User-Agent tells us they're coming from a
large-screen device, the XOOM tablet.

On the other hand, this User-Agent:

```
Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; Nexus One Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
```

Contains "mobile" and "android," so serve the web surfer on this Nexus One the mobile experience!

You'll notice that Android User-Agents have commonalities:

![Disambiguation of a typical Android user-agent string](/static/search/blog/images/import/08c3bf107d43373569a81acfdaf7c615.jpg)

While you may still want to detect "android" in the User-Agent to implement Android-specific
features, such as touch-screen optimizations, our main message is: Should your mobile site depends
on UA sniffing, please detect the strings "mobile" and "android," rather than just "android," in
the User-Agent. This helps properly serve both your mobile and tablet visitors.

For questions, please join our Android community in their
[developer forum](https://developer.android.com/community/index).
