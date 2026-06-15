---
title: "Working with multi-regional websites"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2010-03-working-with-multi-regional-websites"
url: "https://developers.google.com/search/blog/2010/03/working-with-multi-regional-websites"
canonical: "https://developers.google.com/search/blog/2010/03/working-with-multi-regional-websites"
author: "John Mueller"
published: "2010-03-12T00:00:00+00:00"
updated: "2010-03-12T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:05:33+00:00"
status_code: 200
html_hash: "8a05e8dcda1e89cb6a6ca4eee787db253b545f692ae6e9430aa6c7528cce00c5"
clean_word_count: 1355
clean_char_count: 8736
---
# Working with multi-regional websites

Did you know that a majority of users surveyed feel that having information in their own language
was more important than a low price? Living in a non-English-speaking country, I've seen friends
and family members explicitly look for and use local and localized websites—properly localized
sites definitely have an advantage with users. Google works hard to show users the best possible
search results. Many times those are going to be pages that are localized, for the user's location
and/or in the user's language.

If you're planning to take the time to create and maintain a localized version of your website,
making it easy to recognize and find is a logical part of that process. In this blog post series,
we'll take a look at what is involved with multi-regional and multi-lingual websites from a search
engine point of view. A multi-regional website is one that explicitly targets users in various
regions (generally different countries); we call it
[multilingual](/search/blog/2008/08/how-to-start-multilingual-site) when it is
available in multiple languages, and sometimes, the website targets both multiple regions and is
in multiple languages. Let's start with some general preparations and then look at websites that
target multiple regions.

## Preparing for global websites

Expanding a website to cover multiple regions and/or languages can be challenging. By creating
multiple versions of your website, any issues with the base version will be multiplied; make sure
that you have everything working properly before you start. Given that this generally means you'll
suddenly be working with a multiplied number of URLs, don't forget that you'll need appropriate
infrastructure to support the website.

## Planning multi-regional websites

When planning sites for multiple regions (usually countries), don't forget to research legal or
administrative requirements that might come into play first. These requirements may determine how
you proceed, for instance whether or not you would be eligible to use a country-specific domain
name.

All websites start with domain names; when it comes to domain names, Google differentiates between
two types of domain names:

- **ccTLDs** (country-code top level domain names): These are tied to a specific country (for
  example .de for Germany, .cn for China). Users and search engines use this as a strong sign that
  your website is explicitly for a certain country.
- **gTLDs** (generic top level domain names): These are not tied to a specific country.
  Examples of gTLds are .com, .net, .org, .museum. Google sees regional top level domain names
  such as .eu and .asia as gTLDs, since they cannot be tied to a specific country. We also treat
  some vanity ccTLDs (such as .tv, .me, etc.) as gTLDs as we've found that users and webmasters
  frequently see these as being more generic than country-targeted (we don't have a complete list
  of such vanity ccTLDs that we treat as gTLDs as it may change over time). You can set
  geotargeting for websites with gTLDs using the
  [Webmaster Tools Geographic Target setting](https://www.google.com/support/webmasters/bin/answer.py?answer=62399).

## Geotargeting factors

Google generally uses the following elements to determine the geotargeting of a website (or a
part of a website):

1. **Use of a ccTLD** is generally a strong signal for users since it explicitly specifies a
   single country in an unmistakable way.

   or

   **Webmaster Tools' manual geotargeting for gTLDs** (this can be on a domain, subdomain or
   subdirectory level); more information on this can be found in our
   [blog post](/search/blog/2008/04/where-in-world-is-your-site) and in the
   [Help Center](https://www.google.com/support/webmasters/bin/answer.py?answer=62399).
   With
   [region tags from geotargeting being shown in search results](/search/blog/2009/12/region-tags-in-google-search-results),
   this method is also very clear to users. Please keep in mind that it generally does not make
   sense to set a geographic target if the same pages on your site target more than a single
   country (say, all German-speaking countries)—just write in that language and do not use
   the geotargeting setting (more on writing in other languages will follow soon!).
2. **Server location** (through the IP address of the server) is frequently near your users.
   However, some websites use distributed content delivery networks (CDNs) or are hosted in a
   country with better webserver infrastructure, so we try not to rely on the server location
   alone.
3. **Other signals** can give us hints. This could be from local addresses and phone numbers on
   the pages, use of local language and currency, links from other local sites, and/or the use of
   Google's Local Business Center (where available).

Note that we do not use locational `meta` tags (like `geo.position` or
`distribution`) or HTML attributes for geotargeting. While these may be useful in other
regards, we've found that they are generally not reliable enough to use for geotargeting.

## URL structures

The first three elements used for geotargeting are strongly tied to the server and to the URLs
used. It's difficult to determine geotargeting on a page by page basis, so it makes sense to
consider using a URL structure that makes it easy to segment parts of the website for
geotargeting. Here are some of the possible URL structures with pros and cons with regards to
geotargeting:

|  |  |  |  |
| --- | --- | --- | --- |
| **ccTLDs** for example: example.de, example.fr | **Subdomains with gTLDs** for example: de.site.com, fr.site.com, etc. | **Subdirectories with gTLDs** for example: site.com/de/, site.com/fr/, etc. | **URL parameters** for example: site.com?loc=de, ?country=france, etc. |
| pros (+)   - clear geotargeting - server location is irrelevant - easy separation of sites - legal requirements (sometimes) | pros (+)   - easy to set up - can use Webmaster Tools geotargeting - allows different server locations - easy separation of sites | pros (+)   - easy to set up - can use Webmaster Tools geotargeting - low maintenance (same host) | pros (+)  (not recommended) |
| cons (-)   - expensive (+ availability) - more infrastructure - ccTLD requirements (sometimes) | cons (-)   - users might not recognize geotargeting from the URL alone (is "de" the language or   country?) | cons (-)   - users might not recognize geotargeting from the URL alone - single server location - separation of sites harder | cons (-)   - segmentation based on the URL is difficult - users might not recognize geotargeting from the URL alone - geotargeting in Webmaster Tools is not possible |

As you can see, geotargeting is not an exact science (even sites using country-code top level
domain names can be global in nature), so it's important that you plan for the users from the
"wrong" location. One way to do this could be to show links on all pages for users to select their
region and language of choice. We'll look at some other possible solutions further on in this
blog post series.

## Dealing with duplicate content on global websites

Websites that provide content for different regions and in different languages sometimes create
content that is the same or similar but available on different URLs. This is generally not a
problem as long as the content is for different users in different countries. While we strongly
recommend that you provide unique content for each different group of users, we understand that
this may not always be possible for all pages and variations from the start. There is generally
no need to "hide" the duplicates by disallowing crawling in a
[robots.txt file](/search/docs/crawling-indexing/robots/intro)
or by using a
[`noindex` robots `meta` tag](/search/docs/advanced/crawling/special-tags).
However, if you're providing the same content to the same users on different URLs (for instance,
if both "example.de/" and "example.com/de/" show German language content for users in Germany),
it would make sense to choose a preferred version and to
[redirect](/search/docs/crawling-indexing/301-redirects)
(or use the
[`"rel=canonical"` `link` element](/search/docs/crawling-indexing/consolidate-duplicate-urls))
appropriately.

Do you already have a website that targets multiple regions or do you have questions about the
process of planning one? Come to the Help Forum and
[join the discussion](https://support.google.com/webmasters/community/thread?tid=12a5507889c20461&hl=en).
In following posts, we'll take a look at multi-lingual websites and then look at some special
situations that can arise with global websites.
[Bis bald](https://translate.google.com/#auto%7Cen%7CBis%20bald)!
