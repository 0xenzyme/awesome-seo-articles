---
title: "Using a robots.txt file"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2006-02-using-robotstxt-file"
url: "https://developers.google.com/search/blog/2006/02/using-robotstxt-file"
canonical: "https://developers.google.com/search/blog/2006/02/using-robotstxt-file"
author: "Vanessa Fox"
published: "2006-02-24T00:00:00+00:00"
updated: "2006-02-24T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:44:51+00:00"
status_code: 200
html_hash: "16f8f484448417fa963c2110248133ed6bb71ba41b0d312656a2f3ffbfbab5ff"
clean_word_count: 1023
clean_char_count: 6213
---
# Using a robots.txt file

A couple of weeks ago, we
[launched a robots.txt](/search/blog/2006/02/more-stats-and-analysis-of-robotstxt)
analysis tool. This tool gives you information about how
[Googlebot](/search/docs/crawling-indexing/googlebot)
interprets your robots.txt file. You can read more about the
[robots.txt Robots Exclusion Standard](https://www.rfc-editor.org/rfc/rfc9309.html),
but we thought we'd answer some common questions here.

## What is a robots.txt file?

A robots.txt file provides restrictions to search engine robots (known as "bots") that crawl the
web. These bots are automated, and before they access pages of a site, they check to see if a
robots.txt file exists that prevents them from accessing certain pages.

## Does my site need a robots.txt file?

Only if your site includes content that you don't want search engines to index. If you want
search engines to index everything in your site, you don't need a robots.txt file (not even an
empty one).

## Where should the robots.txt file be located?

The robots.txt file *must* reside in the root of the domain. A robots.txt file located in
a subdirectory isn't valid, as bots only check for this file in the root of the domain. For
instance, `https://www.example.com/robots.txt` is a valid location. But,
`https://www.example.com/mysite/robots.txt` is not. If you don't have access to the
root of a domain, you can restrict access using the
[Robots META tag.](/search/docs/crawling-indexing/robots-meta-tag)

## How do I create a robots.txt file?

You can create this file in any text editor. It should be an
[ASCII-encoded text file](https://www.google.com/search?q=ascii+text+file),
not an HTML file. The filename should be lowercase.

## What should the syntax of my robots.txt file be?

The simplest robots.txt file uses two rules:

- **`User-Agent:`** the robot the following rule applies to
- **`Disallow:`** the pages you want to block

These two lines are considered a single entry in the file. You can include as many entries as you
want. You can include multiple Disallow lines in one entry.

## `User-Agent`

A user-agent is a specific search engine robot. The
[Web Robots Database](https://www.robotstxt.org/wc/active.html)
lists many common bots. You can set an entry to apply to a specific bot (by listing the name) or
you can set it to apply to all bots (by listing an asterisk). An entry that applies to all bots
looks like this:

```
User-Agent: *
```

## `Disallow`

The `Disallow` line lists the pages you want to block. You can list a specific URL or
a pattern. The entry should begin with a forward slash (/).

- **To block the entire site**, use a forward slash: `Disallow: /`
- **To block a directory**, follow the directory name with a forward slash:
  `Disallow: /private_directory/`
- **To block a page**, list the page:
  `Disallow: /private_file.html`

URLs are case-sensitive. For instance, `Disallow: /private_file.html` would block
`https://www.example.com/private_file.html`, but would allow
`https://www.example.com/Private_File.html`.

## How do I block Googlebot?

Google uses several user-agents. You can block access to any of them by including the bot name on
the User-Agent line of an entry.

- **Googlebot:** crawl pages from our
  [web index](https://www.google.com/).
- **Googlebot-Mobile:** crawls pages for our
  [mobile index](https://mobile.google.com/mobile_search.html).
- **Googlebot-Image:** crawls pages for our
  [image index](https://www.google.com/imghp?tab=wi&q=).
- **Mediapartners-Google:** crawls pages to determine
  [AdSense content](https://www.google.com/adsense/)
  (used only if you show AdSense ads on your site).

## Can I allow pages?

Yes, Googlebot recognizes an extension to the robots.txt standard called `Allow`. This
extension may not be recognized by all other search engine bots, so check with other search
engines you're interested in to find out. The `Allow` line works exactly like the
`Disallow` line. Simply list a directory or page you want to allow.

You may want to use `Disallow` and `Allow` together. For instance, to block
access to all pages in a subdirectory except one, you could use the following entries:

```
User-Agent: Googlebot
Disallow: /folder1/

User-Agent: Googlebot
Allow: /folder1/myfile.html
```

Those entries would block all pages inside the folder1 directory except for
`myfile.html`.

## I don't want certain pages of my site to be indexed, but I want to show AdSense ads on those pages. Can I do that?

Yes, you can `Disallow` all bots other than `Mediapartners-Google` from
those pages. This keeps the pages from being indexed, but lets
`Googlebot-MediaPartners` bot analyze the pages to determine the ads to show.
`Googlebot-MediaPartners` bot doesn't share pages with the other Google user-agents.
For instance, you could use the following entries:

```
User-Agent: *
Disallow: /folder1/

User-Agent: MediaPartners-Google
Allow: /folder1/
```

## I don't want to list every file that I want to block. Can I use pattern matching?

Yes, Googlebot interprets some pattern matching. This is an extension of the standard, so not all
bots may follow it.

## Matching a sequence of characters

You can use an asterisk (`*`) to match a sequence of characters. For instance, to block
access to all subdirectories that begin with `private`, you could use the following
entry:

```
User-Agent: Googlebot
Disallow: /private*/
```

## How can I make sure that my file blocks and allows what I want it to?

You can use our
[robots.txt analysis tool](/search/blog/2006/02/analyzing-robotstxt-file) to:

- Check specific URLs to see if your robots.txt file allows or blocks them.
- See if Googlebot had trouble parsing any lines in your robots.txt file.
- Test changes to your robots.txt file.

Also, if you don't currently use a robots.txt file, you can create one and then test it with the
tool before you upload it to your site.

## If I change my robots.txt file or upload a new one, how soon will it take effect?

We generally download robots.txt files about once a day. You can see the last time we downloaded
your file by accessing the robots.txt tab in your Sitemaps account and checking the
**Last downloaded** date and time.
