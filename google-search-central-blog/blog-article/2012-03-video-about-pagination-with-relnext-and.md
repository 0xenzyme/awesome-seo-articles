---
title: "Video about pagination with rel=\"next\" and rel=\"prev\""
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2012-03-video-about-pagination-with-relnext-and"
url: "https://developers.google.com/search/blog/2012/03/video-about-pagination-with-relnext-and"
canonical: "https://developers.google.com/search/blog/2012/03/video-about-pagination-with-relnext-and"
author: "Maile Ohye"
published: "2012-03-13T00:00:00+00:00"
updated: "2012-03-13T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:18:33+00:00"
status_code: 200
html_hash: "3e83c3ffed22bcffacc243d131d77071a7fe241cd5aa90d826b9565bbb97eca0"
clean_word_count: 692
clean_char_count: 4484
---
# Video about pagination with rel="next" and rel="prev"

If you're curious about the
[`rel="next"` and `rel=prev"` for paginated content announcement](/search/blog/2011/09/pagination-with-relnext-and-relprev)
we made several months ago, we filmed a
[video covering more of the basics of pagination](https://www.youtube.com/watch?v=njn8uXTWiGg)
to help answer your questions. Paginated content includes things like an article that spans
several URLs/pages, or an e-commerce product category that spans multiple pages. With
`rel="next"` and `rel="prev"` markup, you can provide a strong hint to
Google that you would like us to treat these pages as a logical sequence, thus consolidating their
linking properties and usually sending searchers to the first page. You can check out our
presentation for more information:

*This video on pagination covers the basics of `rel="next"` and
`rel="prev"` and how it could be useful for your site.*

*Slides from the pagination video*

Additional resources about pagination include:

- Webmaster Central Blog post announcing
  [support of `rel="next"` and `rel="prev"`](/search/blog/2011/09/pagination-with-relnext-and-relprev)
- Webmaster Help Center article with more
  [implementations of `rel="next"` and `rel="prev"`](https://support.google.com/webmasters/bin/answer.py?answer=1663744)
- [Webmaster Forum thread](https://support.google.com/webmasters/community/thread?tid=344378292ff91e8d&hl=en)
  with our answers to the community's in-depth questions, such as:
  - *Does `rel=next/prev` also work as a signal for only one page of the series
    (page 1 in most cases?) to be included in the search index? Or would
    `noindex` tags need to be present on page 2 and on?*

    > When you implement `rel="next"` and `rel="prev"` on component
    > pages of a series, we'll then consolidate the indexing properties from the component
    > pages and attempt to direct users to the most relevant page/URL. This is typically the
    > first page. There's no need to mark page 2 to n of the series with `noindex`
    > unless you're sure that you don't want those pages to appear in search results.
  - *Should I use the `rel next/prev` in the `<head>`
    section of a blog even if the two contents are not strictly correlated (but they are just
    time-sequential)?*

    > In regard to using `rel="next"` and `rel="prev"` for entries in
    > your blog that "are not strictly correlated (but they are just time-sequential),"
    > pagination markup likely isn't the best use of your time—time-sequential pages
    > aren't nearly as helpful to our indexing process as semantically related content, such as
    > pagination on component pages in an article or category. It's fine if you include the
    > markup on your time-sequential pages, but please note that it's not the most helpful use
    > case.
  - *We operate a real estate rental website. Our files display results based on numerous
    parameters that affect the order and the specific results that display. Examples of
    such parameters are "page number", "records per page", "sorting" and "area
    selection"...*

    > It sounds like your real estate rental site encounters many of the same issues that
    > e-commerce sites face... Here are some ideas on your situation:
    > 1. It's great that you are using the Webmaster Tools URL parameters feature to more
    >    efficiently crawl your site.
    > 2. It's possible that your site can form a `rel="next"` and
    >    `rel="prev"` sequence with no parameters (or with default parameter
    >    values). It's also possible to form parallel pagination sequences when users select
    >    certain parameters, such as a sequence of pages where there are 15 records and a
    >    separate sequence when a user selects 30 records. Paginating component pages, even
    >    with parameters, helps us more accurately index your content.
    > 3. While it's fine to set `rel="canonical"` from a component URL to a single
    >    view-all page, setting the canonical to the first page of a parameter-less sequence
    >    is considered improper usage. We make no promises to honor this implementation of
    >    `rel="canonical"` .

Remember that if you have paginated content, it's fine to leave it as-is and not add
`rel="next"` and `rel="prev"` markup at all. But if you're interested in
pagination markup as a strong hint for us to better understand your site, we hope these resources
help answer your questions!
