---
title: "URL removals explained, part II: Removing sensitive text from a page"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2010-04-url-removals-explained-part-ii-removing"
url: "https://developers.google.com/search/blog/2010/04/url-removals-explained-part-ii-removing"
canonical: "https://developers.google.com/search/blog/2010/04/url-removals-explained-part-ii-removing"
author: "John Mueller"
published: "2010-08-06T00:00:00+00:00"
updated: "2010-08-06T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:06:06+00:00"
status_code: 200
html_hash: "b020b74008e8b98039747ec6c5c105d4eceec3c045a5316f69596113754964c1"
clean_word_count: 1550
clean_char_count: 9428
---
# URL removals explained, part II: Removing sensitive text from a page

Change can happen—sometimes, as we saw in our
[previous post on URL removals](/search/blog/2010/03/url-removal-explained-part-i-urls),
you may completely block or remove a page from your site. Other times you might only change parts
of a page, or remove certain pieces of text. Depending on how frequently a page is being crawled,
it can take some time before these changes get reflected in our search results. In this blog post
we'll look at the steps you can take if we're still showing old, removed content in our search
results, either in the form of a "snippet" or on the cached page that's linked to from the search
result. Doing this makes sense when the old content contains sensitive information that needs to
be removed quickly—it's not necessary to do this when you just update a website normally.

As an example, let's look at the following fictitious search result:

|  |  |
| --- | --- |
| **Walter** E. **Coyote** | < Title |
| Chief Development Officer at Acme Corp 1948-2003: worked on the top  secret velocitus incalculii capturing device which has shown potential**...** | < Snippet |
| www.example.com/about/**waltercoyote** - Cached | < URL + link to cached page |

To change the content shown in the snippet (or on the linked cached page),
**you'll first need to change the content on the actual (live) page**. Unless a page's publicly
visible content is changed, Google's automatic processes will continue to show parts of the
original content in our search results.

Once the page's content has been changed, there are several options available to make those
changes visible in our search results:

1. **Wait for Googlebot to re-crawl and re-index the page**: This is the natural method for
   how most content is updated at Google. Sometimes it can take a fairly long time, depending on
   how frequently Googlebot currently crawls the page in question. Once we've re-crawled and
   re-indexed the page, the old content will usually not be visible as it'll be replaced by the
   current content. Provided Googlebot is not blocked from crawling the page in question (either
   by robots.txt or by not being able to access the server properly), you don't have to do
   anything special for this to take place. It's generally not possible to speed up crawling and
   indexing, as these processes are fully automated and depend on many external factors.
2. Use
   [Google's public URL removal tool](https://www.google.com/webmasters/tools/removals)
   to **request removal of content that has been removed from someone else's webpage**. Using
   this tool, it's necessary to enter the
   [exact URL of the page](https://www.google.com/support/webmasters/bin/answer.py?answer=63758)
   that has been modified, select the "Content has been removed from the page" option, and then
   specify one or more words that have been completely removed from that page.

   ![google cache removal tool](/static/search/blog/images/archived_1_removal-cache.png)

   Note that *none* of the words you enter can appear on the page; even if a word has been
   removed from one part of the page, your request will be denied if that word still appears on
   another part of the page. Be sure to choose a word (or words) that no longer appear
   *anywhere* on the page. If, in the above example, you removed
   "top secret velocitus incalculii capturing device", you should
   submit those words and not something like "my project." However, if the word
   "top" or "device" still exists
   anywhere on the page, the request would be denied. To maximize your chances of success, it's
   often easiest to just enter one word that you're sure no longer appears anywhere on the page.

   Once your request has been processed and it's found that the submitted word(s) no longer
   appear on the page, the search result will no longer show a snippet, nor will the cached page
   be available. The title and the URL of the page will still be visible, and the entry may still
   appear in search results for searches related to the content that has been removed (such as
   searches for
   [velocitus incalculii](https://www.google.com/search?q=velocitus+incalculii)),
   even if those words no longer appear in the snippet. However, once the page has been
   re-crawled and re-indexed, the new snippet and cached page can be visible in our search
   results.

   Keep in mind that we will need to verify removal of the word(s) by viewing the page. If the
   page no longer exists and the server is returning a proper
   [`404` or `410` HTTP result code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes),
   making us unable to view the page, you may be better off
   [requesting removal of the page](/search/blog/2010/03/url-removal-explained-part-i-urls)
   altogether.
3. Use Google Webmaster Tools URL removal tool to
   **request removal of information on a page from your website**. If you have access to the
   website in question and have verified ownership of it in
   [Google Webmaster Tools](https://search.google.com/search-console),
   you can use the URL removal tool there (under
   *Site Configuration > Crawler access*) to request
   that the snippet and the cached page be removed until the page has been re-crawled. To use this
   tool, you only need to submit the
   [exact URL of the page](https://www.google.com/support/webmasters/bin/answer.py?answer=63758)
   (you won't need to specify any removed words). Once your request has been processed, we'll
   remove the snippet and the cached page from search results. The title and the URL of the page
   will still be visible, and the page may also continue to rank in search results for queries
   related to content that has been removed. After the page has been re-crawled and re-indexed,
   the search result with an updated snippet and cached page (based on the new content) can be
   visible.

Google indexes and ranks items based not only on the content of a page, but also on other external
factors, such as the inbound links to the URL. Because of this, it's possible for a URL to
continue to appear in search results for content that no longer exists on the page, even after
the page has been re-crawled and re-indexed. While the URL removal tool can remove the snippet
and the cached page from a search result, it will not change or remove the title of the search
result, change the URL that is shown, or prevent the page from being shown for searches based on
any current or previous content. If this is important to you, you should make sure that the URL
fulfills the requirements for a
[complete removal from our search results](/search/blog/2010/03/url-removal-explained-part-i-urls).

## Removing non-HTML content

If the changed content is not in (X)HTML (for example if an image, a Flash file or a PDF file has
been changed), you won't be able to use the cache removal tool. So if it's important that the old
content no longer be visible in search results, the fastest solution would be to change the URL
of the file so that the old URL returns a `404` HTTP result code and use the URL
removal tool to remove the old URL. Otherwise, if you chose to allow Google to naturally refresh
your information, know that previews of non-HTML content (such as
[Quick View links for PDF files](https://googleblog.blogspot.com/2009/10/quickly-view-formatted-pdfs-in-your.html))
can take longer to update after recrawling than normal HTML pages would.

## Proactively preventing the appearance of snippets or cached versions

As a webmaster, you have the option to use robots
[`meta` tags](/search/docs/advanced/crawling/special-tags)
to proactively prevent the appearance of snippets or cached versions without using our removal
tools. While we don't recommend this as a default approach (the snippet can help users recognize a
relevant search result faster, and a cached page gives them the ability to view your content even
in the unexpected event of your server not being available), you can use the "nosnippet" robots
`meta` tag to
[prevent showing of a snippet](/search/docs/crawling-indexing/robots-meta-tag#nosnippet),
or the "noarchive" robots `meta` tag to disable caching of a page. Note that if this is changed on
existing and known pages, Googlebot will need to re-crawl and re-index those pages before this
change becomes visible in search results.

We hope this blog post helps to make some of the processes behind the URL removal tool for updated
pages a bit clearer. In our next blog post we'll look at ways to request removal of content that
you don't own; stay tuned!

As always, we welcome your feedback and questions in our
[Webmaster Help Forum](https://support.google.com/webmasters/community/label?lid=5489e59697a233d7).

## Other posts of this series

- [Part I: Removing URLs and directories](/search/blog/2010/03/url-removal-explained-part-i-urls)
- [Part II: Removing and updating cached content](/search/blog/2010/04/url-removals-explained-part-ii-removing)
- [Part III: Removing content you don't own](/search/blog/2010/04/url-removal-explained-part-iii-removing)
- [Part IV: Tracking requests, what not to remove](/search/blog/2010/05/url-removal-explained-part-iv-tracking)

Finally, you might be also interested to read about
[managing what information is available about you online](/search/blog/2009/10/managing-your-reputation-through-search).
