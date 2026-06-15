---
title: "More control over titles too"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2006-07-more-control-over-titles-too"
url: "https://developers.google.com/search/blog/2006/07/more-control-over-titles-too"
canonical: "https://developers.google.com/search/blog/2006/07/more-control-over-titles-too"
author: "Vanessa Fox"
published: "2006-07-14T00:00:00+00:00"
updated: "2006-07-14T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:45:52+00:00"
status_code: 200
html_hash: "3b97beab9ec54db35b2c3349a145e343cba016bed413c4b9347ffea30f39d43d"
clean_word_count: 117
clean_char_count: 694
---
# More control over titles too

Yesterday we told you that you can
[use a `meta` tag to ask us not to use descriptions](/search/blog/2006/07/more-control-over-page-snippets)
of your site from the
[Open Directory Project](https://www.dmoz.org/)
(ODP) when we generate snippets. Some of you have asked if this `meta` tag prevents us from using
the title from the ODP as well. Yes, this `meta` tag does apply to both the title and description
from the ODP.

Also, as noted in our
[webmaster help center](/search/docs/appearance/title-link), you can combine parameters
in the `meta` tag. So, for instance, you could use the following `meta` tag:

```
<meta="robots" content="noodp, noarchive">
```
