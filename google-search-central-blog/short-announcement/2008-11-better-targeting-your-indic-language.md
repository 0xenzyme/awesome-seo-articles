---
title: "Better targeting your indic language site"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2008-11-better-targeting-your-indic-language"
url: "https://developers.google.com/search/blog/2008/11/better-targeting-your-indic-language"
canonical: "https://developers.google.com/search/blog/2008/11/better-targeting-your-indic-language"
author: "Jayashree and Zareen, Search Quality Team, Google India"
published: "2008-11-14T00:00:00+00:00"
updated: "2008-11-14T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:55:33+00:00"
status_code: 200
html_hash: "26f46697e9aa7fc94dfb29ec04a749d481845dbe9de6c3ebc7e9a21dd97d72d4"
clean_word_count: 348
clean_char_count: 2279
---
# Better targeting your indic language site

A lot has been said about
[how to start a multi-lingual site](/search/blog/2008/08/how-to-start-multilingual-site)
and how to better target content through
[`meta` tags](/search/docs/advanced/crawling/special-tags). Our users have raised a
number of interesting questions about creating websites in different languages, like the one
below.

From [ganex](https://www.blogger.com/profile/12462803572730503354):

> How does one do for INDIA.
>
> As there are many languages spoken here.
>
> My Site is primarily in English, but my site targets different cities in INDIA.
>
> For Hyderabad - I want in Urdu and Telugu and for Chennai I want in Tamil
>
> for Bengaluru I want in Kannada.
>
> For North I want in Hindi.

We'd like to introduce the
[transliteration API](https://googleajaxsearchapi.blogspot.com/2008/09/introducing-transliteration-api.html)
for Indic languages (languages spoken in India) in addition to our Ajax API for languages. With
this API at your disposal, content creation is simplified because it not only helps integrating
transliteration in your websites but also allows users visiting your site to type in Indic
languages.

To include the transliteration API, first you need the AJAX script.

```
<script src="https://www.google.com/jsapi"></script>
```

This script tag will load the `google.load` function, which lets you load the
individual Google APIs. For loading Google Transliteration API, call to `google.load`
looks like this:

```
<script>
  google.load("elements", "1", {
  packages: "transliteration"
});
</script>
```

When it comes to targeting, don't forget to add `meta` tags in your local language. And for your
questions, we have a new addition to our already existing communication channels like the
webmaster help groups and Webmaster Tools (available in
[26 languages](/search/blog/2008/05/webmaster-tools-now-in-26-languages)!). We also
have our own official
[Orkut webmaster community](https://www.orkut.co.in/Main#Community.aspx?cmm=65242009)!
Here users can share thoughts and discuss webmaster related issues.

[Sign up](https://www.orkut.co.in/Main#Community.aspx?cmm=65242009)
for our Orkut community now and if you have any additional thoughts we'd love to hear about them.

Cheers,
