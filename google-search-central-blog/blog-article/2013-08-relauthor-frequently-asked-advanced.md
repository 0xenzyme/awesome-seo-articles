---
title: "rel=\"author\" frequently asked (advanced) questions"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2013-08-relauthor-frequently-asked-advanced"
url: "https://developers.google.com/search/blog/2013/08/relauthor-frequently-asked-advanced"
canonical: "https://developers.google.com/search/blog/2013/08/relauthor-frequently-asked-advanced"
author: "Maile Ohye"
published: "2013-08-21T00:00:00+00:00"
updated: "2013-08-21T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2013_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:22:38+00:00"
status_code: 200
html_hash: "c52a9fe74e2a3024dccb2406998ca060b33b5d4b67b084ddcdc61b8c60c3482b"
clean_word_count: 740
clean_char_count: 4763
---
# rel="author" frequently asked (advanced) questions

Using [authorship](https://plus.google.com/authorship) helps searchers
discover great information by highlighting content from authors who they might find interesting.
If you're an author, signing up for authorship will help users recognize content that you've
written. Additionally, searchers can click the byline to see more articles you've authored or to
follow you on Google+. It's that simple! Well, except for several advanced questions that we'd
like to help answer...

![Authorship featured in search results from one of my favorite authors, John Mueller](/static/search/blog/images/import/4ef5355d78e0709604dae923baf44f56.png)
![Clicking the author's byline in search results can reveal more articles and a Google+ profile](/static/search/blog/images/import/e49589b6b202fb30aa1db7c9de491045.png)

## Recent authorship questions

**What kind of pages can be used with authorship?**
Good question! You can increase the likelihood that we show authorship for your site by only using
authorship markup on pages that meet these criteria:

- The URL/page contains a single article (or subsequent versions of the article) or single piece
  of content, by the same author. This means that the page isn't a list of articles or an updating
  feed. If the author frequently switches on the page, then the annotation is no longer helpful to
  searchers and is less likely to be featured.
- The URL/page consists primarily of content written by the author.
- Showing a clear byline on the page, stating the author wrote the article and using the same
  name as used on their Google+ profile.

**Can I use a company mascot as an author and have authorship annotation in search results?
For my pest control business, I'd like to write as the "Pied Piper."**
You can write articles in the manner you prefer—your users may really like the Pied Piper
idea. However, for authorship annotation in search results, Google prefers to feature a human who
wrote the content. By doing so, authorship annotation better indicates that a search result is the
perspective of a person, and this helps add credibility for searchers.
Again, because currently we want to feature people, link authorship markup to an individual's
profile rather than linking to a company's Google+ Page.

**If I use authorship on articles available in different languages, such as
`example.com/en/article1.html` for English and
`example.com/fr/article1.html` for the French translation, should I link to
two separate author/Google+ profiles written in each language?**
In your scenario, both articles: `example.com/en/article1.html` and
`example.com/fr/article1.html` should link to the same Google+ profile in the author's
language of choice.

**Is it possible to add two authors for one article?**
In the current search user interface, we only support one author per article, blog post, and so
on. We're still experimenting to find the optimal outcome for searchers when more than one author
is specified.

**How can I prevent Google from showing authorship?**
The fastest way to prevent authorship annotation is to make the author's Google+ profile
[not discoverable in search results](https://support.google.com/plus/answer/1151728).
Otherwise, if you still want to keep your profile in search results, then you can remove any
profile or contributor links to the website, or remove the markup so that it no longer connects
with your profile.

**What's the difference between
[`rel=author`](/search/docs/appearance/structured-data/article) and
[`rel=publisher`](https://support.google.com/webmasters/answer/1708844)?**
`rel=publisher` helps a business create a shared identity by linking the business'
website (often from the home page) to the business' Google+ Page. `rel=author` helps
individuals (authors!) associate their individual articles from a URL or website to their Google+
profile. While `rel=author` and `rel=publisher` are both link relationships,
they're actually completely independent of one another.

**Can I use authorship on my site's property listings or product pages since one of my
employees has customized the description?**
Authorship annotation is useful to searchers because it signals that a page conveys a real
person's perspective or analysis on a topic. Since property listings and product pages are less
perspective/analysis oriented, we discourage using authorship in these cases. However, an article
about products that provides helpful commentary, such as, "Camera X vs. Camera Y: Faceoff in the
Arizona Desert" could have authorship.

If you have additional questions, don't forget to check out the
[Webmaster Forum](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:structured_data)).
