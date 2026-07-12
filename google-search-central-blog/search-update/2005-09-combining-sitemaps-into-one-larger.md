---
title: "Combining Sitemaps into one larger Sitemap"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2005-09-combining-sitemaps-into-one-larger"
url: "https://developers.google.com/search/blog/2005/09/combining-sitemaps-into-one-larger"
canonical: "https://developers.google.com/search/blog/2005/09/combining-sitemaps-into-one-larger"
author: "Vanessa Fox"
published: "2005-09-16T00:00:00+00:00"
updated: "2005-09-16T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2005_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:43:44+00:00"
status_code: 200
html_hash: "e61e96f0a95795b285b6cd76a2185269827ce9cff509dcb0dfb58388fce7739b"
clean_word_count: 353
clean_char_count: 2204
---
# Combining Sitemaps into one larger Sitemap

Do you have several small Sitemaps that you would like to combine into one larger one? With
[version 1.3 of the Sitemap Generator](https://sourceforge.net/project/showfiles.php?group_id=137793&package_id=153422),
which we told you about
[yesterday](/search/blog/2005/09/announcing-sitemap-generator-version), you can do just
that.

This version includes a new input method: sitemap, which lets you point to existing Sitemaps that
you created with the
[Sitemap Generator](/search/docs/crawling-indexing/sitemaps/overview). The Sitemap
Generator will create a single Sitemap that includes the URLs contained in each Sitemap you list.

To use this input method, locate the sitemap section of the config file and modify it as needed.
You should include one <sitemap> entry for each Sitemap you want to include. Each entry must
contain the path parameter, whose value should be the path and filename of an existing Sitemap
file.

The `example_config.xml` file included with the Sitemap Generator download includes a
sample `<sitemap>` section:

```
<-- ** MODIFY or DELETE **

"sitemap" nodes tell the script to scan other Sitemap files. This can
be useful to aggregate the results of multiple runs of this script into
a single Sitemap.

Required attributes:  path - path to the file -->

<sitemap path="/var/www/docroot/subpath/sitemap.xml">
```

This section gives one example. You should replace this example and include an entry for each
Sitemap you want to include. Ensure that the path value is the complete path and filename on your
web server. You can list gzipped Sitemaps as well, as long as they have a `.gz`
extension. Rather than list each Sitemap, you can use wildcards. For instance, the following entry
would include any Sitemaps that begin with the word "sitemap" and have
an `.xml` file extension:

```
<sitemap path="/var/www/docroot/subpath/sitemap*.xml">
```

The Sitemap Generator extracts all URLs and the optional data listed for each URL for every
Sitemap you list and creates one Sitemap with this information. At this time, we can't guarantee
that this method will work for Sitemaps created with tools other than the Sitemap Generator.
