---
title: "Inside Googlebot: demystifying crawling, fetching, and the bytes we process"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "2026-03-crawler-blog-post"
url: "https://developers.google.com/search/blog/2026/03/crawler-blog-post"
canonical: "https://developers.google.com/search/blog/2026/03/crawler-blog-post"
author: "Gary"
published: "2026-03-31T00:00:00+00:00"
updated: "2026-03-31T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "news_or_research"
fetched_at: "2026-06-14T13:46:05+00:00"
status_code: 200
html_hash: "42e616e52ca591d22968c76688e1b52801a1caaed33a915af400425a09d3c293"
clean_word_count: 939
clean_char_count: 5941
---
# Inside Googlebot: demystifying crawling, fetching, and the bytes we process

If you tuned into
[episode 105 of the Search Off the Record podcast](https://www.youtube.com/watch?v=JpweMBnpS4Q),
you might have heard us diving deep into a topic that is close to our hearts
(and our servers): the inner workings of Googlebot.

For a long time, the name "Googlebot" has conjured up the image of a single,
tireless robot systematically reading the internet. But the reality is a bit
more complex — and a lot more interesting. Today, we want to pop the
hood on our crawling infrastructure, with a special focus on the very thing
that makes our own heads spin: bytesize limits.

## First, Googlebot isn't a single program

Let's clear up a historical misnomer first. Back in the early 2000s, Google
had one product, so we had one crawler. The name "Googlebot" stuck. But
today, Googlebot is just a user of something that resembles a centralized
crawling platform.

When you see Googlebot in your server logs, you are just looking at Google
Search. Dozens of other clients — Google Shopping, AdSense, and
more — all route their crawl requests through this same underlying
infrastructure under different crawler names, the larger ones documented
on the
[Google Crawler infrastructure site](/crawling/docs/crawlers-fetchers/overview-google-crawlers).

## The 2MB limit: what happens to your bytes?

This is where things get somewhat confusing. Every client of the crawler
infrastructure needs to set some settings for their fetches. These settings
include the user agent string, what user agent tokens will they look for in
robots.txt, and how many bytes they will fetch from a single URL.

Googlebot currently fetches up to 2MB for any individual URL (excluding
PDFs). This means it crawls only the first 2MB of a resource, including the
HTTP header. For PDF files, the limit is 64MB.

Image and video crawlers typically have a wide range of threshold values,
and it largely depends on the product that they're fetching for. For
example, fetching a favicon might have a very low limit, unlike Image Search.

For any other crawler that doesn't specify a limit, the default is 15MB
regardless of content type.

What does this mean for the bytes your server sends over the wire?

1. **Partial fetching:** If your HTML file is larger than 2MB,
   Googlebot doesn't reject the page. Instead, it stops the fetch exactly at
   the 2MB cutoff. Note that the limit includes HTTP request headers.
2. **Processing the cutoff:** That downloaded portion (the first
   2MB of bytes) is passed along to our indexing systems and the Web
   Rendering Service (WRS) as if it were the complete file.
3. **The unseen bytes:** Any bytes that exist *after* that
   2MB threshold are entirely ignored. They aren't fetched, they aren't
   rendered, and they aren't indexed.
4. **Bringing in resources:** Every referenced resource in the
   HTML (excluding media, fonts, and a few exotic files) will be fetched by
   WRS with Googlebot like the parent HTML. They have their own, separate,
   per-URL byte counter and don't count towards the size of the parent page.

For the vast majority of the web, a 2MB HTML payload is massive, and you
will never hit this limit. However, if your page includes bloated inline
base64 images, massive blocks of inline CSS/JavaScript, or starts with
megabytes of menus, you could accidentally push your actual textual content
or critical structured data past the 2MB mark. If those crucial bytes aren't
fetched, to Googlebot, they simply don't exist.

## Rendering the bytes

Once the crawler has successfully retrieved the bytes (up to the limit), it
passes the baton to the WRS. The WRS processes JavaScript and executes
client-side code similar to a modern browser to understand the final visual
and textual state of the page. Rendering pulls in and executes JavaScript and
CSS files, and processes XHR requests to better understand the page's textual
content and structure (it doesn't request images or videos). For each
requested resource, the 2MB limit also applies.

However, remember that the WRS can only execute the code that the crawler
actually retrieved. Furthermore, the
[WRS operates statelessly](/search/docs/crawling-indexing/javascript/fix-search-javascript)
— it clears local storage and session data between requests. This may
have particular implications for how dynamic, JavaScript-dependent elements
are interpreted by our systems.

## Best practices for your bytes

To ensure Googlebot can efficiently fetch and understand your content, keep
these byte-level best practices in mind:

- **Keep your HTML lean:** Move heavy CSS and JavaScript to
  external files. While the initial HTML document is capped at 2MB, external
  scripts, and stylesheets are fetched separately (subject to their own
  limits).
- **Order matters:** Place your most critical elements —
  like meta tags, `<title>` elements,
  `<link>` elements, canonicals, and essential structured
  data — higher up in the HTML document. This ensures they are unlikely
  to be found below the cutoff.
- **Monitor your server logs:** Keep an eye on your server
  response times. If your server is struggling to serve bytes, our crawlers
  will automatically back off to avoid overloading your infrastructure, which
  will drop your crawl frequency.

**Note that this limit is not set in stone** and may change
over time as the web evolves and HTML pages grow in size. (Or shrink.
Hopefully shrink.)

Crawling isn't magic; it's a highly orchestrated, scaled exchange of bytes.
By understanding how our central fetching infrastructure retrieves and
limits those bytes, you can ensure your site's most important content always
makes the cut.

Happy optimizing!

*Want to hear more behind-the-scenes details? Check out
[Episode 105 of the Search Off the Record podcast on YouTube](https://www.youtube.com/watch?v=JpweMBnpS4Q)
or wherever you get your podcasts!*
