---
title: "GET, POST, and safely surfacing more of the web"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-11-get-post-and-safely-surfacing-more-of"
url: "https://developers.google.com/search/blog/2011/11/get-post-and-safely-surfacing-more-of"
canonical: "https://developers.google.com/search/blog/2011/11/get-post-and-safely-surfacing-more-of"
author: "Pawel Aleksander Fedorynski, Maile Ohye"
published: "2011-11-01T00:00:00+00:00"
updated: "2011-11-01T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:16:17+00:00"
status_code: 200
html_hash: "8e270d014bf30f22930b289887654f4cefc4d1633f442d5d4d2f14126bfef93e"
clean_word_count: 1212
clean_char_count: 8212
---
# GET, POST, and safely surfacing more of the web

As the web evolves, Google's crawling and indexing capabilities also need to progress. We
[improved our indexing of Flash](/search/blog/2008/06/improved-flash-indexing), built
a more robust
[infrastructure called Caffeine](/search/blog/2010/06/our-new-search-index-caffeine),
and we even started
[crawling forms](/search/blog/2008/04/crawling-through-html-forms) where it makes
sense. Now, especially with the growing popularity of JavaScript and, with it, AJAX, we're
finding more web pages requiring `POST` requests—either for the entire content of
the page or because the pages are missing information and/or look completely broken without the
resources returned from `POST`. For Google Search this is less than ideal, because when
we're not properly discovering and indexing content, searchers may not have access to the most
comprehensive and relevant results.

We generally advise to use
[`GET`](https://www.google.com/search?q=GET+POST+HTTP)
for fetching resources a page needs, and this is by far our preferred method of crawling. We've
started experiments to rewrite `POST` requests to `GET`, and while this
remains a valid strategy in some cases, often the contents returned by a web server for
`GET` vs. `POST` are completely different. Additionally, there are
legitimate reasons to use `POST` (for example, you can attach more
data to a `POST` request than a `GET`). So, while `GET` requests
remain far more common, to surface more content on the web, Googlebot may now perform
`POST` requests when we believe it's safe and appropriate.

We take precautions to avoid performing any task on a site that could result in executing an
unintended user action. Our `POST` requests are primarily for crawling resources that
a page requests automatically, mimicking what a typical user would see when they open the URL in
their browser. This will evolve over time as we find better heuristics, but that's our current
approach.

Let's run through a few `POST` request scenarios that demonstrate how we're improving
our crawling and indexing to evolve with the web.

## Examples of Googlebot's `POST` requests

- *Crawling a page via a POST redirect*

  ```
      <html>
        <body onload="document.foo.submit();">
          <form name="foo" action="request.php" method="post"
            <input type="hidden" name="bar" value="234"/>
          </form>
        </body>
      </html>
  ```
- *Crawling a resource via a `POST` `XMLHttpRequest`*: In this
  step-by-step example, we improve both the indexing of a page and its Instant Preview by
  following the automatic `XMLHttpRequest` generated as the page renders.

1. Google crawls the URL, yummy-sundae.html.
2. Google begins indexing yummy-sundae.html and, as a part of this process, decides to attempt
   to render the page to better understand its content and/or generate the Instant Preview.
3. During the render, yummy-sundae.html automatically sends an XMLHttpRequest for a resource,
   hot-fudge-info.html, using the `POST` method.

   ```
         <html>
           <head>
             <title>Yummy Sundae</title>
             <script src="jquery.js"></script>
           </head>
           <body>
             This page is about a yummy sundae.
             <div id="content"></div>
             <script>
               $(document).ready(function() {
               $.post('hot-fudge-info.html', function(data)
               {$('#content').html(data);});
               });
             </script>
           </body>
         </html>
   ```
4. The URL requested through `POST`, hot-fudge-info.html, along with its data payload,
   is added to Googlebot's crawl queue.
5. Googlebot performs a `POST` request to crawl hot-fudge-info.html.
6. Google now has an accurate representation of yummy-sundae.html for Instant Previews. In
   certain cases, we may also incorporate the contents of hot-fudge-info.html into
   yummy-sundae.html.
7. Google completes the indexing of yummy-sundae.html.
8. User searches for "hot fudge sundae".
9. Google's algorithms can now better determine how yummy-sundae.html is relevant for this query,
   and we can properly display a snapshot of the page for Instant Previews.

## Improving your site's crawlability and indexability

General advice for creating crawlable sites is found in our
[Help Center](https://www.google.com/support/webmasters/bin/answer.py?answer=40349).
For webmasters who want to help Google crawl and index their content and/or generate the Instant
Preview, here are a few simple reminders:

- Prefer `GET` for fetching resources, unless there's a specific reason to use
  `POST`.
- Verify that we're allowed to crawl the resources needed to render your page. In the example
  above, if hot-fudge-info.html is disallowed by
  [robots.txt](/search/docs/crawling-indexing/robots/intro),
  Googlebot won't fetch it. More subtly, if the JavaScript code that issues the
  `XMLHttpRequest` is located in an external `.js` file disallowed by
  robots.txt, we won't see the connection between yummy-sundae.html and hot-fudge-info.html, so
  even if the latter is not disallowed itself, that may not help us much. We've seen even more
  complicated chains of dependencies in the wild. To help Google better understand your site it's
  almost always better to allow Googlebot to crawl all resources.
  You can test whether resources are blocked through
  [Webmaster Tools](https://search.google.com/search-console)
  *Labs* >
  [*Instant Previews*](/search/blog/2011/05/troubleshooting-instant-previews-in).
- Make sure to return the same content to Googlebot as is returned to users' web browsers.
  [Cloaking](/search/docs/essentials/spam-policies#cloaking)
  (sending different content to Googlebot than to users) is a violation of our
  [Webmaster Guidelines](/search/docs/essentials)
  because, among other things, it may cause us to provide a searcher with an irrelevant result
  —the content the user views in their browser may be a complete mismatch from what we
  crawled and indexed. We've seen numerous `POST` request examples where a webmaster
  non-maliciously cloaked (which is still a violation), and their cloaking—on even the
  smallest of changes—then caused JavaScript errors that prevented accurate indexing and
  completely defeated their reason for cloaking in the first place. Summarizing, if you want your
  site to be search-friendly, cloaking is an all-around sticky situation that's best to avoid.

  To verify that you're not accidentally cloaking, you can use
  [Instant Previews](/search/blog/2011/05/troubleshooting-instant-previews-in)
  within Webmaster Tools, or try setting the User-Agent string in your browser to something like:

  ```
  Mozilla/5.0 (compatible; Googlebot/2.1; +https://www.google.com/bot.html)
  ```

  Your site shouldn't look any different after such a change. If you see a blank page, a
  JavaScript error, or if parts of the page are missing or different, that means that something's
  wrong.
- Remember to include important content (that is, the content you'd like indexed) as text, visible
  directly on the page and without requiring user-action to display. Most search engines are
  text-based and generally work best with text-based content. We're always improving our ability
  to crawl and index content published in a variety of ways, but it remains a good practice to
  use text for important information.

## Controlling your content

If you'd like to prevent content from being crawled or indexed for Google Web Search, traditional
[robots.txt rules](/search/docs/crawling-indexing/robots/robots_txt#syntax)
remain the best method. To prevent the Instant Preview for your page(s), please see our
[Instant Previews FAQ](https://sites.google.com/site/webmasterhelpforum/en/faq-instant-previews)
which describes the `Google Web Preview` User-Agent and the `nosnippet` `meta` tag.

## Moving forward

We'll continue striving to increase the comprehensiveness of our index so searchers can find more
relevant information. And we expect our crawling and indexing capability to improve and evolve
over time, just like the web itself. Please let us know if you have questions or concerns.
