---
title: "Using OAI-PMH with Google Sitemaps"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2005-09-using-oai-pmh-with-google-sitemaps"
url: "https://developers.google.com/search/blog/2005/09/using-oai-pmh-with-google-sitemaps"
canonical: "https://developers.google.com/search/blog/2005/09/using-oai-pmh-with-google-sitemaps"
author: "Vanessa Fox"
published: "2005-09-20T00:00:00+00:00"
updated: "2005-09-20T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2005_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:43:49+00:00"
status_code: 200
html_hash: "e1a80ad10654177c78ad35077e29047b1a89bf84c5045218283edc89975d353b"
clean_word_count: 346
clean_char_count: 2183
---
# Using OAI-PMH with Google Sitemaps

If your site uses the
[Open Archives Initiative Protocol for Metadata Harvesting](https://www.openarchives.org/OAI/openarchivesprotocol.html)
(OAI-PMH) 2.0 protocol, an application-independent interoperability framework based on metadata
harvesting, you can use your OAI repository
[as your Sitemap](/search/docs/crawling-indexing/sitemaps/overview).

Simply submit the baseURL of your OAI repository (for instance,
https://www.example.com/oaiserver). When we query the baseURL, we automatically add query
parameters (such as `?verb=Identify` or `?verb=ListRecords`), so you can
simply submit the `baseURL` itself. When we extract the URLs for your site, we expect
the records in the repository to be formatted using Dublin Core, with the URLs embedded in
`<dc:identifier>` tags. Below is a sample record that includes the
`<dc:identifier>` tag in bold. The URL listed in that tag is what we extract.

```
<oai_dc:dc
  xmlns:oai_dc="https://www.openarchives.org/OAI/2.0/oai_dc/"
  xmlns:dc="https://purl.org/dc/elements/1.1/"
  xmlns:xsi="https://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="https://www.openarchives.org/OAI/2.0/oai_dc/
  https://www.openarchives.org/OAI/2.0/oai_dc.xsd">
<dc:title xml:lang="en">A title of extraordinary things</dc:title>
<dc:creator>McCormack, Michael</dc:creator>
<dc:subject>LCSH:Ausdehnungslehre; LCCN QA205.H99; Greatness:Amanda</dc:subject>
<dc:publisher>J. Wiley &mp; Sons</dc:publisher>
<dc:date>Created: 1906; Available: 1991</dc:date>
<dc:type>text</dc:type>
<dc:identifier>https://example.com/physics/1796949</dc:identifier>
<dc:language>english</dc:language>
<dc:rights xml:lang="en">Public Domain</dc:rights>
</oai_dc:dc>
```

As with other Sitemaps, the URLs must be within the same site and at the same directory location
or lower than the baseURL. For instance, if you submit
`https://www.example.com/oaiserver` as the `baseURL`, the following URLs
would be valid:

```
https://www.example.com/
https://www.example.com/samples.html
https://www.example.com/images/
```

However, if you submit `https://www.example.com/dataprovider/oaiserver`, then none of
those URLs would be valid.
