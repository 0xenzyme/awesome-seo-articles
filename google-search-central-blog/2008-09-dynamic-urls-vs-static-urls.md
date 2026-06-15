---
title: "Dynamic URLs vs. static URLs"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-09-dynamic-urls-vs-static-urls"
url: "https://developers.google.com/search/blog/2008/09/dynamic-urls-vs-static-urls"
canonical: "https://developers.google.com/search/blog/2008/09/dynamic-urls-vs-static-urls"
author: "Written by Juliane Stiller and Kaspar Szymanski, Search Quality Team"
published: "2008-09-22T00:00:00+00:00"
updated: "2008-09-22T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:54:06+00:00"
status_code: 200
html_hash: "4dade9183d6ab12720f5bad61c64be5eaa74a8a1cedfd7c832b7cba417d07c2e"
clean_word_count: 1483
clean_char_count: 8834
---
# Dynamic URLs vs. static URLs

Chatting with webmasters often reveals widespread beliefs that might have been accurate in the
past, but are not necessarily up-to-date any more. This was the case when we recently talked to a
couple of friends about the structure of a URL. One friend was concerned about using dynamic URLs,
since (as they told us) "search engines can't cope with these." Another friend thought that
dynamic URLs weren't a problem at all for search engines and that these issues were a thing of the
past. One even admitted that they never understood the fuss about dynamic URLs in comparison to
static URLs. For us, that was the moment we decided to read up on the topic of dynamic and static
URLs. First, let's clarify what we're talking about:

## What is a static URL?

A static URL is one that does not change, so it typically does not contain any URL parameters. It
can look like this: `https://www.example.com/archive/january.htm`. You can search for
static URLs on Google by typing
[filetype:htm](https://www.google.com/search?q=filetype%3Ahtm)
in the search field. Updating these kinds of pages can be time consuming, especially if the amount
of information grows quickly, since every single page has to be hard-coded. This is why webmasters
who deal with large, frequently updated sites like online shops, forum communities, blogs or
content management systems may use dynamic URLs.

## What is a dynamic URL?

If the content of a site is stored in a database and pulled for display on pages on demand,
dynamic URLs maybe used. In that case the site serves basically as a template for the content.
Usually, a dynamic URL would look something like this:
<https://code.google.com/p/google-checkout-php-sample-code/issues/detail?id=31>.
You can spot dynamic URLs by looking for characters like: `?`,`=`,
`&`. Dynamic URLs have the disadvantage that different URLs can have the same
content. So different users might link to URLs with different parameters which have the same
content. That's one reason why webmasters sometimes want to rewrite their URLs to static ones.

## Should I try to make my dynamic URLs look static?

Following are some key points you should keep in mind while dealing with dynamic URLs:

1. It's quite hard to correctly create and maintain rewrites that change dynamic URLs to
   static-looking URLs.
2. It's much safer to serve us the original dynamic URL and let us handle the problem of detecting
   and avoiding problematic parameters.
3. If you want to rewrite your URL, please remove unnecessary parameters while maintaining a
   dynamic-looking URL.
4. If you want to serve a static URL instead of a dynamic URL you should create a static equivalent
   of your content.

## Which can Googlebot read better, static or dynamic URLs?

We've come across many webmasters who, like our friend, believed that static or static-looking
URLs were an advantage for indexing and ranking their sites. This is based on the presumption that
search engines have issues with crawling and analyzing URLs that include session IDs or source
trackers. However, as a matter of fact, we at Google have made some progress in both areas. While
static URLs might have a slight advantage in terms of clickthrough rates because users can easily
read the urls, the decision to use database-driven websites does not imply a significant
disadvantage in terms of indexing and ranking. Providing search engines with dynamic URLs should
be favored over hiding parameters to make them look static.

Let's now look at some of the widespread beliefs concerning dynamic URLs and correct some of the
assumptions which spook webmasters. :)

## Myth: "Dynamic URLs cannot be crawled."

**Fact:** We can crawl dynamic URLs and interpret the different parameters. We might have
problems crawling and ranking your dynamic URLs if you try to make your urls look static and in
the process hide parameters which offer the Googlebot valuable information. One recommendation is
to *avoid reformatting a dynamic URL to make it look static*. It's always advisable to use
static content with static URLs as much as possible, but in cases where you decide to use dynamic
content, you should give us the possibility to analyze your URL structure and not remove
information by hiding parameters and making them look static.

## Myth: "Dynamic URLs are okay if you use fewer than three parameters."

**Fact:** There is no limit on the number of parameters, but a good rule of thumb would be to
*keep your URLs short* (this applies to all URLs, whether static or dynamic). You may be able
to remove some parameters which aren't essential for Googlebot and offer your users a nice looking
dynamic URL. If you are not able to figure out which parameters to remove, we'd advise you to
serve us all the parameters in your dynamic URL and our system will figure out which ones do not
matter. Hiding your parameters keeps us from analyzing your URLs properly and we won't be able to
recognize the parameters as such, which could cause a loss of valuable information.

Following are some questions we thought you might have at this point.

**Does that mean I should avoid rewriting dynamic URLs at all?** That's our recommendation,
unless your rewrites are limited to removing unnecessary parameters, or you are very diligent in
removing all parameters that could cause problems. If you transform your dynamic URL to make it
look static you should be aware that we might not be able to interpret the information correctly
in all cases. If you want to serve a static equivalent of your site, you might want to consider
transforming the underlying content by serving a replacement which is truly static. One example
would be to generate files for all the paths and make them accessible somewhere on your site.
However, if you're using URL rewriting (rather than making a copy of the content) to produce
static-looking URLs from a dynamic site, you could be doing harm rather than good. You can serve
us your standard dynamic URL and we will automatically find the parameters which are unnecessary.

**Can you give me an example?** If you have a dynamic URL which is in the standard format like
`foo?key1=value&key2=value2` we recommend that you leave the URL unchanged, and
Google will determine which parameters can be removed; or you could remove unnecessary parameters
for your users. Be careful that you only remove parameters which do not matter. Here's an example
of a URL with a couple of parameters:

```
www.example.com/article/bin/answer.foo?language=en&answer=3&sid=98971298178906&query=URL
```

- `language=en`: indicates the language of the article
- `answer=3`: the article has the number 3
- `sid=8971298178906`: the session ID number is 8971298178906
- `query=URL`: the query with which the article was found is "URL"

Not all of these parameters offer additional information. So rewriting the URL to
`www.example.com/article/bin/answer.foo?language=en&answer=3` probably would not
cause any problems as all irrelevant parameters are removed.

The following are some examples of static-looking URLs which may cause more crawling problems than
serving the dynamic URL without rewriting:

- `www.example.com/article/bin/answer.foo/en/3/98971298178906/URL`
- `www.example.com/article/bin/answer.foo/language=en/answer=3/sid=98971298178906/query=URL`
- `www.example.com/article/bin/answer.foo/language/en/answer/3/sid/98971298178906/query/URL`
- `www.example.com/article/bin/answer.foo/en,3,98971298178906,URL`

Rewriting your dynamic URL to one of these examples could cause us to crawl the same piece of
content needlessly via many different URLs with varying values for session IDs
(`sid`) and `query`. These forms make it difficult for us to understand that
`URL` and `98971298178906` have nothing to do with the actual content which
is returned via this URL. However, here's an example of a rewrite where all irrelevant parameters
have been removed:

```
www.example.com/article/bin/answer.foo/en/3
```

Although we are able to process this URL correctly, we would still discourage you from using this
rewrite as it is hard to maintain and needs to be updated as soon as a new parameter is added to
the original dynamic URL. Failure to do this would again result in a static looking URL which is
hiding parameters. So the best solution is often to keep your dynamic URLs as they are. Or, if you
remove irrelevant parameters, bear in mind to leave the URL dynamic as the above example of a
rewritten URL shows:

```
www.example.com/article/bin/answer.foo?language=en&answer=3
```

We hope this article is helpful to you and our friends to shed some light on the various
assumptions around dynamic URLs. Please you can join our
[discussion group](https://support.google.com/webmasters/community)
if you have any further questions.
