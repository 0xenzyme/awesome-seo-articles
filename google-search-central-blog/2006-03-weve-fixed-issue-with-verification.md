---
title: "We've fixed an issue with verification files that included leading zeros"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2006-03-weve-fixed-issue-with-verification"
url: "https://developers.google.com/search/blog/2006/03/weve-fixed-issue-with-verification"
canonical: "https://developers.google.com/search/blog/2006/03/weve-fixed-issue-with-verification"
author: "Vanessa Fox"
published: "2006-03-03T00:00:00+00:00"
updated: "2006-03-03T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:45:04+00:00"
status_code: 200
html_hash: "0530c668294f6f64cfde93bba8a30e5b5d9fc6948d3981082450cbf804dbd27e"
clean_word_count: 88
clean_char_count: 593
---
# We've fixed an issue with verification files that included leading zeros

Thank you to our
[Google Group](https://support.google.com/webmasters/community)
members for finding a bug in the
[verification](https://support.google.com/webmasters/answer/9008080)
file logic, which stripped out leading zeros when we accessed the verification file. We've fixed
this. This should have only affected site owners with verification files that had the pattern
`google0<unique_string>.html`. If your verification file has this pattern and you've
had trouble verifying, please request verification again.
