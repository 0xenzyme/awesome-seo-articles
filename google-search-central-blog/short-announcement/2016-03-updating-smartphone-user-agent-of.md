---
title: "Updating the smartphone user-agent of Googlebot"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2016-03-updating-smartphone-user-agent-of"
url: "https://developers.google.com/search/blog/2016/03/updating-smartphone-user-agent-of"
canonical: "https://developers.google.com/search/blog/2016/03/updating-smartphone-user-agent-of"
author: "Katsuaki Ikegami (池上 克明)"
published: "2016-03-15T00:00:00+00:00"
updated: "2016-03-15T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2016_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:28:32+00:00"
status_code: 200
html_hash: "9745e0d0945d279cae0b1f006587868bbd4ace6da44f1fea454cdd575bc287be"
clean_word_count: 347
clean_char_count: 2195
---
# Updating the smartphone user-agent of Googlebot

As technology on the web changes, we periodically update the user agents we use for Googlebot.
Next month, we will be updating the smartphone `user-agent` of Googlebot:

Googlebot smartphone `user-agent` starting from April 18, 2016:

```
Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P)
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36
(compatible; Googlebot/2.1; +https://www.google.com/bot.html)
```

Today, we use the following smartphone `user-agent` for Googlebot:

```
Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X)
AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4
(compatible; Googlebot/2.1; +https://www.google.com/bot.html)
```

We're updating the `user-agent` string so that our renderer can better understand pages
that use newer web technologies. Our renderer evolves over time and the `user-agent`
string indicates that it is becoming more similar to Chrome than Safari. To make sure your site
can be viewed properly by a wide range of users and browsers, we recommend using
[feature detection](https://www.html5rocks.com/en/tutorials/detection/)
and progressive enhancement.

Our evaluation suggests that this user-agent change should have no effect on 99% of sites. The
most common reason a site might be affected is if it specifically looks for a particular Googlebot
`user-agent` string. User agent sniffing for Googlebot is not recommended and is
considered to be a form of [cloaking](/search/docs/essentials/spam-policies#cloaking).
Googlebot should be treated like any other browser.

If you believe your site may be affected by this update, we recommend checking your site with the
[Fetch and Render Tool](https://www.google.com/webmasters/tools/googlebot-fetch)
in Search Console (which has been updated with the new `user-agent` string) or by
changing the `user-agent` string in Developer Tools in your browser (for example, via
[Chrome Device Mode](/web/tools/chrome-devtools/iterate/device-mode)).
If you have any questions, we're always happy to answer them in our
[Webmaster help forums](https://support.google.com/webmasters/community).
