---
title: "Instant Previews"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2010-11-instant-previews"
url: "https://developers.google.com/search/blog/2010/11/instant-previews"
canonical: "https://developers.google.com/search/blog/2010/11/instant-previews"
author: "Jeremy Silber, Software Engineer"
published: "2010-11-09T00:00:00+00:00"
updated: "2010-11-09T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:09:50+00:00"
status_code: 200
html_hash: "509f2a646dc0c61c1e2cf54adcf955c5a809b0808820b3c8be165d08acb2cad5"
clean_word_count: 659
clean_char_count: 4019
---
# Instant Previews

Today Google introduced
[Instant Previews](https://googleblog.blogspot.com/2010/11/beyond-instant-results-instant-previews),
a new search feature that helps people find information faster by showing a visual preview of
each result. Traditionally, elements of the search results like the title, URL, and snippet—the
text description in each result—help people determine which results are best for them. Instant
Previews achieves the same goal with a *visual* representation of each page and where the
relevant content is, instead of a text description. For our webmaster community, this presents an
opportunity to reveal the design of your site and why your page is relevant for a particular
query. We'd like to offer some thoughts on how to take advantage of the feature.

First of all, it's important to understand what the new feature does. When someone clicks on the
magnifying glass on any result, a zoomed-out snapshot of the underlying page appears to the right
of the results. Orange highlights indicate where highly relevant content on the page is, and text
call outs show search terms in context.

![Instant Preview for the Google Webmaster Forum.](/static/search/blog/images/archived_1_Instant-Preview.png)

These elements let people know what to expect if they click on that result, and why it's relevant
for their query. Our testing shows that the feature really does help with picking the right
result—using Instant Previews makes searchers 5% more likely to be satisfied with the results
they click.

Many of you have put a lot of thought and effort into the structure of your sites, the layout of
your pages, and the information you provide to visitors. Instant Previews gives people a glimpse
into that design and indicates why your pages are relevant to their query. Here are some details
about how to make good use of the feature.

- Keep your pages clearly laid out and structured, with a minimum of distractions or extraneous
  content. This is always good advice, since it improves the experience for visitors, and the
  simplicity and clarity of your site will be apparent via Instant Previews.
- Try to avoid interstitial pages, ad pop-ups, or other elements that interfere with your content.
  In some cases, these distracting elements may be picked up in the preview of your page, making
  the screenshots less attractive.
- Many pages have their previews generated as part of our regular crawl process. Occasionally, we
  will generate screenshots on the fly when a user needs it, and in these situations we will
  retrieve information from web pages using a new "Google Web Preview" user-agent.
- Instant Previews does not change our search algorithm or ranking in any way. It's the same
  results, in the same order. There is also no change to how clicks are tracked. If a user clicks
  on the title of a result and visits your site, it will count as a normal click, regardless of
  whether the result was previewed. Previewing a result, however, doesn't count as a click by
  itself.
- Currently, adding the
  [`nosnippet` `meta` tag](/search/docs/crawling-indexing/robots-meta-tag#nosnippet)
  to your pages will cause them to not show a text snippet in our results. Since Instant Previews
  serves a similar purpose to snippets, pages with the nosnippet tag will also not show previews.
  However, we encourage you to think carefully about opting out of Instant Previews. Just like
  regular snippets, previews tend to be helpful to users—in our studies, results which were
  previewed were more than four times as likely to be clicked on. URLs that have been disallowed
  in the robots.txt file will also not show Instant Previews.
- Currently, some videos or Flash content in previews appear as a "puzzle piece" icon or a
  black square. We're working on rendering these rich content types accurately.

We hope you're as excited about this next step in the search results as we are. We're looking
forward to many more improvements to Instant Previews in the future.
