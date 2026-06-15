---
title: "To slash or not to slash"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2010-04-to-slash-or-not-to-slash"
url: "https://developers.google.com/search/blog/2010/04/to-slash-or-not-to-slash"
canonical: "https://developers.google.com/search/blog/2010/04/to-slash-or-not-to-slash"
author: "Maile Ohye"
published: "2010-04-21T00:00:00+00:00"
updated: "2010-04-21T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:06:00+00:00"
status_code: 200
html_hash: "195e3e1a61575f224dda6cd010eedef1c4b21cbdb6d790d93648ab89232a00e4"
clean_word_count: 706
clean_char_count: 4687
---
# To slash or not to slash

That is the question we hear often. Onward to the answers! Historically, it's common for URLs with
a trailing slash to indicate a directory, and those without a trailing slash to denote a file:

```
https://example.com/foo/ (with trailing slash, conventionally a directory)
https://example.com/foo (without trailing slash, conventionally a file)
```

But they certainly don't have to. Google treats each URL above separately (and equally) regardless
of whether it's a file or a directory, or it contains a trailing slash or it doesn't contain a
trailing slash.

## Different content on slash and non-slash URLs is okay for Google, but often is less ideal for users

From a technical, search engine standpoint, it's certainly permissible for these two URL versions
to contain different content. Your users, however, may find this configuration horribly
confusing—just imagine if `www.google.com/webmasters` and
`www.google.com/webmasters/` produced two separate experiences.

For this reason, trailing slash and non-trailing slash URLs often serve the same content. The most
common case is when a site is configured with a directory structure:

```
https://example.com/parent-directory/child-directory/
```

## Your site's configuration and your options

You can do a quick check on your site to see if either of the URLs matching this pattern
[redirects](/search/docs/crawling-indexing/301-redirects) to the other:

1. `https://example.com/foo/`

   (with trailing slash)
2. `https://example.com/foo`

   (no trailing slash)

- If only one version can be returned (that is, the other redirects to it), that's great! This
  behavior is beneficial because it reduces
  [duplicate content](/search/docs/advanced/guidelines/duplicate-content). In the
  particular case of redirects to trailing slash URLs, our search results will likely show the
  version of the URL with the
  [`200` response code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
  (most often the trailing slash URL)—regardless of whether the redirect was a
  `301` or `302`.
- If both slash and non-trailing-slash versions contain the same content and each returns
  `200`, you can:
  - Consider changing this behavior (more info below) to reduce duplicate content and improve
    [crawl efficiency](/search/blog/2009/08/optimize-your-crawling-indexing).
  - Leave it as-is. Many sites have duplicate content. Our indexing process often handles this
    case for webmasters and users. While it's not totally optimal behavior, it's perfectly
    legitimate and a-okay. :)
  - Rest assured that for your root URL specifically, `https://example.com` is
    equivalent to `https://example.com/` and can't be redirected even if you're Chuck
    Norris.

## Steps for serving only one URL version

What if your site serves duplicate content on these two URLs:

```
https://example.com/foo/
https://example.com/foo
```

Meaning that both URLs return `200` (neither has a redirect or contains
[`rel="canonical"` link tag](/search/docs/crawling-indexing/consolidate-duplicate-urls)
), and you want to change the situation?

1. Choose one URL as the preferred version. If your site has a directory structure, it's more
   conventional to use a trailing slash with your directory URLs (for example,
   `example.com/directory/` rather than `example.com/directory`), but you can
   choose whichever you like.
2. Be consistent with the preferred version. Use it in your internal links. If you have a
   [sitemap](/search/docs/crawling-indexing/sitemaps/overview), include the preferred version
   (and don't include the duplicate URL).
3. Use a `301` redirect from the duplicate to the preferred version. If that's not
   possible, the `rel="canonical"` link tag is a strong option.
   `rel="canonical"` works similarly to a `301` for Google's indexing
   purposes, and other major search engines as well.
4. Test your `301` configuration through
   [Fetch as Googlebot](https://support.google.com/webmasters/answer/9128668)
   in [Webmaster Tools](https://search.google.com/search-console).
   Make sure your URLs, `https://example.com/foo/` and
   `https://example.com/foo`, are behaving as expected. The preferred version should
   return a `200` status code. The duplicate URL should `301` redirect to the
   preferred URL.
5. Check for
   [Crawl errors](https://support.google.com/webmasters/answer/9679690)
   in Webmaster Tools, and, if possible, your webserver logs as a quick check that the
   `301` redirects are implemented.
6. Profit! (just kidding) But you can bask in the sunshine of your efficient server configuration,
   warmed by the knowledge that your site is better optimized.
