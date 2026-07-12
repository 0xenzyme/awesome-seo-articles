---
title: "Introducing Rich Snippets"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2009-05-introducing-rich-snippets"
url: "https://developers.google.com/search/blog/2009/05/introducing-rich-snippets"
canonical: "https://developers.google.com/search/blog/2009/05/introducing-rich-snippets"
author: "Written by Kavi Goel, Ramanathan V. Guha, and Othar Hansson"
published: "2009-05-12T00:00:00+00:00"
updated: "2009-05-12T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:58:12+00:00"
status_code: 200
html_hash: "47a47facec8c9cd0d1cc0da31c363ede80be743803ffc0be3837574e2ee8ab05"
clean_word_count: 1086
clean_char_count: 6739
---
# Introducing Rich Snippets

As a site owner, you have a unique understanding of your web pages and the content they represent.
Google helps users find your page by showing them a small sample of that content—the
"snippet." We use a variety of techniques to create these snippets and give users relevant
information about what they'll find when they click through to visit your site. Today, we're
announcing Rich Snippets, a new presentation of snippets that applies Google's algorithms to
highlight structured data embedded in web pages.

![a rich snippet line showing review stars](/static/search/blog/images/import/5c81c4599964edd430531e2319ea2016.png)

Rich Snippets give users convenient summary information about their search results at a glance.
We are currently supporting data about reviews and people. When searching for a product or
service, users can easily see reviews and ratings, and when searching for a person, they'll get
help distinguishing between people with the same name. It's a simple change to the display of
search results, yet our experiments have shown that users find the new data valuable—if they
see useful and relevant information from the page, they are more likely to click through. Now
we're beginning the process of opening up this successful experiment so that more websites can
participate. As a site owner, you can help by annotating your pages with structured data in a
standard format.

To display Rich Snippets, Google looks for markup formats (microformats and RDFa) that you can
easily add to your own web pages. In most cases, it's as quick as wrapping the existing data on
your web pages with some additional tags. For example, here are a few relevant lines of the HTML
from Yelp's review page for "Drooling Dog BarBQ" before adding markup data:

![html snippet without any extra structured markup](/static/search/blog/images/import/e48804fabaea78f6b14abfa97d37d118.png)

and now with microformats markup:

![html snippet with microformats annotations](/static/search/blog/images/import/4a3a969324f35c7a0b69b54714b1b7b8.png)

or alternatively, use RDFa markup. Either format works:

![html snippet with RDFa annotations](/static/search/blog/images/import/d05663f32e15e14e47055f9daee4fbc6.png)

By incorporating standard annotations in your pages, you not only make your structured data
available for Google's search results, but also for any service or tool that supports the same
standard. As structured data becomes more widespread on the web, we expect to find many new
applications for it, and we're excited about the possibilities.

To ensure that this additional data is as helpful as possible to users, we'll be rolling this
feature out gradually, expanding coverage to more sites as we do more experiments and process
feedback from site owners. We will make our best efforts to monitor and analyze whether
individual websites are abusing this system: if we see abuse, we will respond accordingly.

To prepare your site for Rich Snippets and other benefits of structured data on the web, please
see our [documentation](/search/docs/appearance/structured-data/intro-structured-data)
on structured data annotations.

## Q&A

Now, time for some Q&A with the team:

### If I mark up my pages, does that guarantee I'll get Rich Snippets?

No. We will be rolling this out gradually, and as always we will use our own algorithms and
policies to determine relevant snippets for users' queries. We will use structured data when we
are able to determine that it helps users find answers sooner. And because you're providing the
data on your pages, you should anticipate that other websites and other tools (browsers, phones)
might use this data as well. You can let us know that you're interested in participating by
filling out this
[form](https://www.google.com/support/webmasters/bin/request.py?contact_type=rich_snippets_feedback).

### What about other existing microformats? Will you support other types of information besides reviews and people?

Not every microformat corresponds to data that's useful to show in a search result, but we do
plan to support more of the existing microformats and define RDFa equivalents.

### What's next?

We'll be continuing experiments with new types (beyond reviews and people) and hope to announce
support for more types in the future.

### I have too much data on my page to mark it all up.

That wasn't a question, but we'll answer anyway. For the purpose of getting data into snippets,
we don't need every bit of data: it simply wouldn't fit. For example, a page that says it has
"497 reviews" of a product probably has data for 10 and links to the others. Even if you could
mark up all 497 blocks of data, there is no way we could fit it into a single snippet. To make
your part of this grand experiment easier, we have defined aggregate types where necessary: a
review-aggregate can be used to summarize all the review information (review count,
average/min/max rating, etc.).

### Why do you support multiple encodings?

A lot of previous work on structured data has focused on debates around encoding. Even within
Google, we have advocates for microformat encoding, advocates for various RDF encodings, and
advocates for our own encodings. But after working on this Rich Snippets project for a while, we
realized that structured data on the web can and should accommodate multiple encodings: we hope
to emphasize this by accepting both microformat encoding and RDFa encoding. Each encoding has
its pluses and minuses, and the debate is a fine intellectual exercise, but it detracts from the
real issues.

We do believe that it is important to have a common vocabulary: the language of object types,
object properties, and property types that enable structured data to be understood by different
applications. We debated how to address this vocabulary problem, and concluded that we needed to
make an investment. Google will, working together with others, host a vocabulary that various
Google services and other websites can use. We are starting with a small list, which we hope to
extend over time.

Wherever possible, we'll simply reuse vocabulary that is in wide use: we support the pre-existing
vCard and hReview types, and there are a variety of other types defined by various communities.
Sites that use Google Custom Search will be able to define their own types, which we will index
and present to users in
[rich Custom Search results pages](https://googlecustomsearch.blogspot.com/2009/05/enabling-rich-snippets-in-custom-search.html).
Finally, we encourage and expect this space to evolve based on new ideas from the structured data
community. We'll notice and reach out when our crawlers pick up new types that are getting broad
use.
