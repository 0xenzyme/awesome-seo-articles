---
title: "We'd like your feedback on a potential new verification process"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2006-02-wed-like-your-feedback-on-potential_22"
url: "https://developers.google.com/search/blog/2006/02/wed-like-your-feedback-on-potential_22"
canonical: "https://developers.google.com/search/blog/2006/02/wed-like-your-feedback-on-potential_22"
author: "Vanessa Fox"
published: "2006-02-22T00:00:00+00:00"
updated: "2006-02-22T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:44:53+00:00"
status_code: 200
html_hash: "23c0e54ba00f74ac07f3ac5b8dbbf81b39248af9a519c7b19d3d23144b92c879"
clean_word_count: 308
clean_char_count: 1822
---
# We'd like your feedback on a potential new verification process

Before we show you
[site stats](https://search.google.com/search-console), we
[verify](https://support.google.com/webmasters/answer/9008080)
site ownership by asking you to upload a uniquely named file. Some webmasters can't do this (for
instance, they can't upload files or they can't choose filenames). We are considering adding an
alternate verification option and would like your feedback. This option would be an additional
choice. It would not replace the current verification process. If you have already verified your
site, you won't need to do anything new.

This alternate verification process would require that you place a `meta` tag in the
`<HEAD>` section of your home page. This META tag would contain a text string
unique to your Sitemaps account and site. We would provide you with this tag, which would look
something like this:

```
<meta name="owner-v1" contents="unique_string">
```

We would check for this `meta` tag in the first `<HEAD>` section of the page,
before the first `<BODY>` section. We would do this so that if your home page
is editable (for instance, is a wiki-type page or a blog with comments), someone could not add
this `meta` tag to the editable section of your page and claim ownership of your site.

The unique string would be a base-64 encoded SHA-256 hash of a string that is composed of the
email address of the owner of the site (for instance, `admin@google.com`) and the
domain name of the site (for instance, `google.com`).

We'd like your comments on this proposal. For those of you who can't verify now, would this be a
method you could use to verify? Do you see any potential problems with this method? Let us know
what you think in our
[Google Group](https://support.google.com/webmasters/community).
