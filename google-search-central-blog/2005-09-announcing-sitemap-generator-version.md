---
title: "Announcing Sitemap Generator version 1.3: Improved encoding support"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2005-09-announcing-sitemap-generator-version"
url: "https://developers.google.com/search/blog/2005/09/announcing-sitemap-generator-version"
canonical: "https://developers.google.com/search/blog/2005/09/announcing-sitemap-generator-version"
author: "Vanessa Fox"
published: "2005-09-15T00:00:00+00:00"
updated: "2005-09-15T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2005_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:43:42+00:00"
status_code: 200
html_hash: "0838df7c68bd383c71e0a5ab274c98edaec83c4f466c9bbb9a2f561062efe52c"
clean_word_count: 339
clean_char_count: 2267
---
# Announcing Sitemap Generator version 1.3: Improved encoding support

The
[Sitemap Generator version 1.3](https://sourceforge.net/project/showfiles.php?group_id=137793&package_id=153422)
is now available and provides improved encoding support. If your webserver uses an encoding other
than UTF-8 or if your domain name or some the URLs in your site use non-ASCII characters, and you
plan to use the Sitemap Generator to create your Sitemap, you should download this latest version.

Generally, non-ASCII URLs should be
[encoded](/search/docs/crawling-indexing/sitemaps/build-sitemap#general-guidelines)
using UTF-8 before being percent-escaped. However, some webservers respond correctly only if URLs
are encoded specifically for the webserver's configuration. All URLs within your Sitemap, as well
as the URL of the Sitemap itself, must be encoded for readability by the web server on which they
are located.

If you are using the
[Sitemap Generator](/search/docs/crawling-indexing/sitemaps/overview),
you can specify the encoding of the URLs contained in the Sitemap from within the
`config.xml` file. Within the
[site definition section](/search/docs/crawling-indexing/sitemaps/overview#config_reference)
of that config file, use the optional default\_encoding attribute to specify the
[encoding](/search/docs/crawling-indexing/sitemaps/overview#encoding)
used by your webserver. If you don't use this attribute and your webserver uses an encoding other
than UTF-8, the Sitemap Generator can't know which encoding to use, although it does attempt to
determine the correct encoding. If the generated Sitemap doesn't list the URLs correctly, you
should explicitly indicate the encoding with the default\_encoding attribute and run the Sitemap
Generator again.

If your URLs contain non-ASCII characters, we recommend that you run the Sitemap Generator script
using Python 2.3 or higher. This version of Python has increased non-ASCII support. If your domain
name contains non-ASCII characters, you must use Python 2.3 or later, as
[Internationalizing Domain Names in Applications (IDNA)](https://www.rfc-editor.org/rfc/rfc3490.txt)
support wasn't added until this version. Without IDNA support, the Sitemap Generator can't
correctly encode a non-ASCII domain name.
