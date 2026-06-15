---
title: "Making the most of improvements to the +1 button"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-08-making-most-of-improvements-to-1-button"
url: "https://developers.google.com/search/blog/2011/08/making-most-of-improvements-to-1-button"
canonical: "https://developers.google.com/search/blog/2011/08/making-most-of-improvements-to-1-button"
author: "Daniel Dulitz"
published: "2011-08-24T00:00:00+00:00"
updated: "2011-08-24T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:14:35+00:00"
status_code: 200
html_hash: "da3c194e916d77fda667bbb70f19d866e33036554e30bdd12b247f1c21b3bab0"
clean_word_count: 462
clean_char_count: 2954
---
# Making the most of improvements to the +1 button

For the past few months,
[you might have used +1 buttons](https://googleblog.blogspot.com/2011/06/1-button-for-websites-recommend-content)
to help visitors recommend your content on Google Search and on their Google Profiles. We've
just announced
[a few changes](https://googleblog.blogspot.com/2011/08/doing-more-with-1-button-more-than-4)
that make +1 even more useful.

First, the +1 button now lets visitors share links to your pages on Google+. If someone wants to
start a conversation about your content, it's easy for them to do so. Second, you can use
+Snippets to customize the name, image and description that appear when your content is shared.
Finally, new inline annotations help increase engagement after users see a friend's
recommendation right on your page.

Here are a couple of tips to help you take full advantage of these improvements:

## +Snippets

The +1 button opens up your site to a valuable new source of traffic with sharing on Google+.
+Snippets let you put your best face forward by customizing exactly what appears when your
content is shared.

For example, if you're running a movie review site, you might want visitors to share posts
containing the title, movie poster, and a brief synopsis:

![The new sharing view of the Google+ sharing feature](/static/search/blog/images/import/35cbd2d299daffbf47f41cecc7a00a45.png)

You
[may already be using](https://googleblog.blogspot.com/2011/06/introducing-schemaorg-search-engines)
this markup to build rich annotations for your pages on Google Search. If not, marking up your
pages is simple. Just add the correct
[schema.org](https://schema.org/) attributes to the data already
present on your pages. You'll set a name, image, and description in your code:

```
<body itemscope itemtype="https://schema.org/Article">
<h1 itemprop="name">This is the article name</h1>
<img itemprop="image" src="thumbnail.jpg" />
<p itemprop="description">This is the description of the article.</p>
</body>
```

For more details on alternate markup types, please see our
[technical documentation](https://code.google.com/apis/+1button/#plus-snippet).

## Inline annotations

Now, when a person visits a page that someone they know has +1'd, they can see a name and face
reminding them to pay special attention to your content. Here's how it looks:

![Inline annotations let people see which of their friends +1'd your content](/static/search/blog/images/import/e773131464f1af040f5245e25862ade9.png)

To add inline annotations, you need to update your +1 button code. Visit the
[configuration tool](https://www.google.com/webmasters/+1/button/),
select 'inline' from the 'Annotation' menu, and grab a new snippet of code.

Both sharing from +1 and inline annotations are rolling out fully over the next few days. To test
these improvements right now, join our
[Platform Preview group](https://www.google.com/+/learnmore/platform-preview/).
