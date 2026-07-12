---
title: "Crawling December: HTTP caching"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "2024-12-crawling-december-caching"
url: "https://developers.google.com/search/blog/2024/12/crawling-december-caching"
canonical: "https://developers.google.com/search/blog/2024/12/crawling-december-caching"
author: "Gary Illyes"
published: "2024-12-09T00:00:00+00:00"
updated: "2024-12-09T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2024_watch"
  - "news_or_research"
fetched_at: "2026-06-14T13:44:25+00:00"
status_code: 200
html_hash: "5f2dc1ead95ee37242799d01a2b1d10c8a7a3af8845b67c14e56287f7d3687d7"
clean_word_count: 1155
clean_char_count: 7272
---
# Crawling December: HTTP caching

Allow us to cache, pretty please.

As the internet grew over the years, so did how much Google crawls. While Google's crawling
infrastructure supports heuristic caching mechanisms, in fact always had, the number of requests
that can be returned from local caches has decreased: 10 years ago about 0.026% of the total
fetches were cacheable, which is already not that impressive; today that number is 0.017%.

## Why is caching important?

Caching is a critical piece of the large puzzle that is the internet. Caching allows pages to load
lightning fast on revisits, it saves computing resources and thus also natural resources, and
saves a tremendous amount of expensive bandwidth for both the clients and servers.

Especially if you have a large site with rarely-changing content under individual URLs, allowing
caching locally may help your site be crawled more efficiently. Google's crawling infrastructure
supports heuristic HTTP caching as defined by the
[HTTP caching standard](https://www.rfc-editor.org/rfc/rfc9111.html),
specifically through the `ETag` response- and `If-None-Match` request
header, and the `Last-Modified` response- and `If-Modified-Since` request
header.

We strongly recommend using `ETag` because it's less prone to errors and mistakes (the
value is not structured unlike the `Last-Modified` value). And, if you have the option,
set them both: the internet will thank you. Maybe.

As for what you consider a change that requires clients to refresh their caches, that's up to you.
Our recommendation is that you require a cache refresh on significant changes to your content; if
you only updated the copyright date at the bottom of your page, that's probably not significant.

## `ETag` and `If-None-Match`

Google's crawlers support `ETag` based conditional requests exactly as defined in the
[HTTP caching standard](https://www.rfc-editor.org/rfc/rfc9111.html).
That is, to signal caching preference to Google's crawlers, set the `Etag` value to any
arbitrary ASCII string (usually a hash of the content or version number, but it could also be a
piece of the π, up to you) unique to the representation of the content hosted by the accessed URL.
For example, if you host different versions of the same content under the same URL (say, mobile
and desktop version), each version could have its own unique `ETag` value.

Google's crawlers that support caching will send the `ETag` value returned for a
previous crawl of that URL in the `If-None-Match header`. If the `ETag`
value sent by the crawler matches the current value the server generated, your server should
return an HTTP `304` (Not modified) status code with no HTTP body. This last bit, no
HTTP body, is the important part for a couple reasons:

- your server doesn't have to spend compute resources on actually generating content; that is, you
  save money
- your server doesn't have to transfer the HTTP body; that is, you save money

On the client side, like a user's browser or Googlebot, the content under that URL is retrieved
from the client's internal cache. Because there's no data transfer involved, this happens
lightning fast, making users happy and potentially saving some resources for them, too.

## `Last-Modified` and `If-Modified-Since`

Similarly to `ETag`, Google's crawlers support `Last-Modified based`
conditional requests, too, exactly as defined in the HTTP Caching standard. This works the same
way as `ETag` from a semantic perspective — an identifier is used to decide
whether the resource is cacheable —, and provides the same benefits as `ETag` on
the clients' side.

We have but a couple recommendations if you're using `Last-Modified` as a caching
directive:

1. The date in the `Last-Modified` header must be formatted according to the
   [HTTP standard](https://www.rfc-editor.org/rfc/rfc9110.html).
   To avoid parsing issues, we recommend using the following date format:
   "Weekday, DD Mon YYYY HH:MM:SS Timezone". For example,
   "Fri, 4 Sep 1998 19:15:56 GMT".
2. While not required, consider also setting the `max-age` field of the
   `Cache-Control` header to help crawlers determine when to recrawl the specific URL.
   Set the value of the `max-age` field to the expected number of seconds the content
   will be unchanged. For example, `Cache-Control: max-age=94043`.

## Examples

If you're like me, wrapping my head around how heuristic caching works is challenging, however
showing an example of the chain of requests and responses seems to help me. Here are two chains
— one for `ETag`/`If-None-Match` and one for
`Last-Modified`/`If-Modified-Since` — to visualize how it's supposed
to work:

|  | `ETag`/`If-None-Match` | `Last-Modified`/`If-Modified-Since` |
| --- | --- | --- |
| **A server's response to a crawl:** This is the response from which a crawler can save the precondition header fields `ETag` and `Last-Modified`. | ``` HTTP/1.1 200 OK Content-Type: text/plain Date: Fri, 4 Sep 1998 19:15:50 GMT ETag: "34aa387-d-1568eb00" ... ``` | ``` HTTP/1.1 200 OK Content-Type: text/plain Date: Fri, 4 Sep 1998 19:15:50 GMT Last-Modified: Fri, 4 Sep 1998 19:15:56 GMT Cache-Control: max-age=94043 ... ``` |
| **Subsequent crawler conditional request:** The conditional request is based on the precondition header values saved from a previous request. The values are sent back to the server for validation in the `If-None-Match` and `If-Modified-Since` request headers. | ``` GET /hello.world HTTP/1.1 Host: www.example.com Accept-Language: en, hu User-Agent: Googlebot/2.1 (+http://www.google.com/bot.html) If-None-Match: "34aa387-d-1568eb00" ... ``` | ``` GET /hello.world HTTP/1.1 Host: www.example.com Accept-Language: en, hu User-Agent: Googlebot/2.1 (+http://www.google.com/bot.html) If-Modified-Since: Fri, 4 Sep 1998 19:15:56 GMT ... ``` |
| **Server response to the conditional request:** Since precondition header values sent by the crawler are validated on the server's side, the server returns a `304` HTTP status code (without an HTTP body) to the crawler. This will happen to every subsequent request until the preconditions fail to validate (the `ETag` or the `Last-Modified` date changes on the server's side). | ``` HTTP/1.1 304 Not Modified Date: Fri, 4 Sep 1998 19:15:50 GMT Expires: Fri, 4 Sep 1998 19:15:52 GMT Vary: Accept-Encoding If-None-Match: "34aa387-d-1568eb00" ... ``` | ``` HTTP/1.1 304 Not Modified Date: Fri, 4 Sep 1998 19:15:50 GMT Expires: Fri, 4 Sep 1998 19:15:51 GMT Vary: Accept-Encoding If-Modified-Since: Fri, 4 Sep 1998 19:15:56 GMT ... ``` |

If you're in the business of making your users happy and perhaps also want to potentially save a
few bucks on your hosting bill, talk to your hosting or CMS provider, or your developers about how
to enable HTTP caching for your site. If nothing else, your users will like you a bit more.

If you wanna chat about caching, head to your nearest
[Search Central help community](https://goo.gle/sc-forum), and if
you have comments about how we're caching, leave feedback on
[the documentation about caching](/search/docs/crawling-indexing/overview-google-crawlers#http-caching)
that we published together with this blog post.

---

## Want to learn more about crawling? Check out the entire Crawling December series:
