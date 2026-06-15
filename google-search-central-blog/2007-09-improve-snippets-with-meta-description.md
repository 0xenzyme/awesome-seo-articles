---
title: "Improve snippets with a meta description makeover"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2007-09-improve-snippets-with-meta-description"
url: "https://developers.google.com/search/blog/2007/09/improve-snippets-with-meta-description"
canonical: "https://developers.google.com/search/blog/2007/09/improve-snippets-with-meta-description"
author: "Written by Raj Krishnan, Snippets Team"
published: "2007-09-28T00:00:00+00:00"
updated: "2007-09-28T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2007_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:50:14+00:00"
status_code: 200
html_hash: "3641d547d12c6f4d00488e4bf1476673b8dfff165ad410e7521978bc7caf710b"
clean_word_count: 882
clean_char_count: 5866
---
# Improve snippets with a meta description makeover

The quality of your snippet—the short text preview we display for each web result—can have a
direct impact on the chances of your site being clicked (that is, the amount of traffic Google sends
your way). We use a number of strategies for
[selecting snippets](/search/docs/appearance/snippet#how-snippet-created),
and you can control one of them by
[writing an informative meta description](/search/docs/appearance/snippet#meta-descriptions)
for each URL.

```
  <meta content="informative description here" name="Description"/>
```

## Why does Google care about meta descriptions?

We want snippets to accurately represent the
web result. We frequently prefer to display meta descriptions of pages (when available) because it
gives users a clear idea of the URL's content. This directs them to good results faster and
reduces the click-and-backtrack behavior that frustrates visitors and inflates web traffic
metrics. Keep in mind that meta descriptions comprised of long strings of keywords don't achieve
this goal and are less likely to be displayed in place of a regular, non-meta description,
snippet. And it's worth noting that while accurate meta descriptions can improve clickthrough,
they won't affect your ranking within search results.

![Snippet showing quality meta description](/static/search/blog/images/import/38a0bf995d0e21ba2ccf8090a63f63e8.png)

**Snippet showing quality meta description**

![Snippet showing lower-quality meta description](/static/search/blog/images/import/b96e23478c45eadd74df2037720c89b8.png)

**Snippet showing lower-quality meta description**

## What are some good meta description strategies?

### Differentiate the descriptions for different pages

Using identical or similar descriptions on every page of a site isn't very helpful when individual
pages appear in the web results. In these cases we're less likely to display the boilerplate text.
Create descriptions that accurately describe each specific page. Use site-level descriptions on
the main home page or other aggregation pages, and consider using page-level descriptions
everywhere else. You should obviously prioritize parts of your site if you don't have time to
create a description for every single page; at the very least, create a description for the
critical URLs like your home page and popular pages.

### Include clearly tagged facts in the description

The meta description doesn't just have to be in sentence format; it's also a great place to
include structured data about the page. For example, news or blog postings can list the author,
date of publication, or byline information. This can give potential visitors very relevant
information that might not be displayed in the snippet otherwise. Similarly, product pages might
have the key bits of information—price, age, manufacturer—scattered throughout a page,
making it unlikely that a snippet will capture all of this information. Meta descriptions can
bring all this data together. For example, consider the following meta description for the 7th
Harry Potter Book, taken from a major product aggregator.

Not as desirable:

```
  <meta name="Description" content="Example site: Harry Potter and the Deathly Hallows (Book 7): Books: J. K. Rowling,Mary GrandPré by J. K. Rowling,Mary GrandPré" />
  <!-- more HTML -->
  <p>
    Harry Potter and the Deathly Hallows (Book 7): Books: J. K. Rowling,Mary GrandPré by J. K. Rowling,Mary GrandPré
  </p>
```

There are a number of reasons this meta description wouldn't work well as a snippet on our search
results page:

- The title of the book is complete duplication of information already in the page title.
- Information within the description itself is duplicated (J. K. Rowling, Mary GrandPré are each
  listed twice).
- None of the information in the description is clearly identified; who is Mary GrandPré?
- The missing spacing and overuse of colons makes the description hard to read.

All of this means that the average person viewing a Google results page—who might spend
under a second scanning any given snippet—is likely to skip this result. As an
alternative, consider the meta description below.

Much nicer:

```
   <meta name="Description" content="Author: J. K. Rowling, Illustrator: Mary GrandPré, Category: Books, Price: $17.99, Length: 784 pages" />
```

What's changed? No duplication, more information, and everything is *clearly tagged and
separated*. No real additional work is required to generate something of this quality: the
price and length are the only new data, and they are already displayed on the site.

### Programmatically generate descriptions

For some sites, like news media sources, generating an accurate and unique description for each
page is easy: since each article is hand-written, it takes minimal effort to also add a
one-sentence description. For larger database-driven sites, like product aggregators,
hand-written descriptions are more difficult. In the latter case, though, programmatic generation
of the descriptions can be appropriate and is encouraged—just make sure that your
descriptions are not "spammy." Good descriptions are human-readable and diverse, as we talked
about in the first point above. The page-specific data we mentioned in the second point is a good
candidate for programmatic generation.

### Use quality descriptions

Finally, make sure your descriptions are... descriptive. It's easy to become lax on the quality of
the meta descriptions, since they're not directly visible in the UI for your site's visitors. But
meta descriptions might be displayed in Google search results—if the description is high
enough quality. A little extra work on your meta descriptions can go a long way towards showing a
relevant snippet in search results. That's likely to improve the quality *and* quantity of
your user traffic.
