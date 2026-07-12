---
title: "Website testing and Google search"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2012-08-website-testing-google-search"
url: "https://developers.google.com/search/blog/2012/08/website-testing-google-search"
canonical: "https://developers.google.com/search/blog/2012/08/website-testing-google-search"
author: "Susan Moskwa"
published: "2012-08-09T00:00:00+00:00"
updated: "2012-08-09T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:19:59+00:00"
status_code: 200
html_hash: "405575b108555258d0b61a4623ec871c3048bd466eff033153e3933a8e57b07d"
clean_word_count: 999
clean_char_count: 6110
---
# Website testing and Google search

We've gotten several questions recently about whether website testing—such as A/B or multivariate
testing—affects a site's performance in search results. We're glad you're asking, because we're
glad you're testing! A/B and multivariate testing are great ways of making sure that what you're
offering really appeals to your users.

Before we dig into the implications for search, a brief primer:

**Website testing** is when you try out different versions of your website (or a part of your
website), and collect data about how users react to each version. You use software to track which
version causes users to do-what-you-want-them-to-do most often: which one results in the most
purchases, or the most email signups, or whatever you're testing for. After the test is finished
you can update your website to use the "winner" of the test—the most effective content.

**A/B testing** is when you run a test by creating multiple versions of a page, each with its
own URL. When users try to access the original URL, you redirect some of them to each of the
variation URLs and then compare users' behaviour to see which page is most effective.

**Multivariate testing** is when you use software to change differents parts of your website
on the fly. You can test changes to multiple parts of a page—say, the heading, a photo, and the
'Add to Cart' button—and the software will show variations of each of these sections to users in
different combinations and then statistically analyze which variations are the most effective.
Only one URL is involved; the variations are inserted dynamically on the page.

So how does this affect what Googlebot sees on your site? Will serving different content variants
change how your site ranks? Below are some guidelines for running an effective test with minimal
impact on your site's search performance.

- **No cloaking.** [Cloaking](/search/docs/essentials/spam-policies#cloaking)—showing
  one set of content to humans, and a different set to Googlebot—is against our
  [Webmaster Guidelines](/search/docs/essentials/spam-policies),
  whether you're running a test or not. Make sure that you're not deciding whether to serve the
  test, or which content variant to serve, based on user-agent. An example of this would be always
  serving the original content when you see the user-agent "Googlebot." Remember that infringing
  our Guidelines can get your site demoted or removed from Google search results—probably not
  the desired outcome of your test.
- **Use `rel="canonical"`.** If you're running an A/B test with multiple URLs, you
  can use the
  [`rel="canonical"`](/search/docs/crawling-indexing/consolidate-duplicate-urls)
  link attribute on all of your alternate URLs to indicate that the original URL is the preferred
  version. We recommend using `rel="canonical"` rather than a `noindex`
  `meta` tag because it more closely matches your intent in this situation. Let's say you were
  testing variations of your home page; you don't want search engines to not index your home page,
  you just want them to understand that all the test URLs are close duplicates or variations on
  the original URL and should be grouped as such, with the original URL as the canonical. Using
  `noindex` rather than `rel="canonical"` in such a situation can sometimes
  have unexpected effects (for example, if for some reason we choose one of the variant URLs as
  the canonical, the "original" URL might also get dropped from the index since it would get
  treated as a duplicate).
- **Use `302` redirects, not `301`.** If you're running an A/B test that
  redirects users from the original URL to a variation URL, use a `302 (temporary)`
  redirect, not a `301 (permanent)` redirect. This tells search engines that this
  redirect is temporary—it will only be in place as long as you're running the experiment—and
  that they should keep the original URL in their index rather than replacing it with the target
  of the redirect (the test page). JavaScript-based redirects are also fine.
- **Only run the experiment as long as necessary.** The amount of time required for a reliable
  test will vary depending on factors like your conversion rates, and how much traffic your
  website gets; a good testing tool should tell you when you've gathered enough data to draw a
  reliable conclusion. Once you've concluded the test, you should update your site with the
  desired content variation(s) and remove all elements of the test as soon as possible, such as
  alternate URLs or testing scripts and markup. If we discover a site running an experiment for
  an unnecessarily long time, we may interpret this as an attempt to deceive search engines and
  take action accordingly. This is especially true if you're serving one content variant to a
  large percentage of your users.

The recommendations above should result in your tests having little or no impact on your site in
search results. However, depending on what types of content you're testing, it may not even matter
much if Googlebot crawls or indexes some of your content variations while you're testing. Small
changes, such as the size, color, or placement of a button or image, or the text of your
"call to action" ("Add to cart" vs. "Buy now!"), can have a surprising impact on users'
interactions with your webpage, but will often have little or no impact on that page's search
result snippet or ranking. In addition, if we crawl your site often enough to detect and index
your experiment, we'll probably index the eventual updates you make to your site fairly quickly
after you've concluded the experiment.

To learn more about website testing, check out
[these articles](https://support.google.com/analytics/bin/answer.py?answer=1745147)
on Content Experiments, our testing tool in
[Google Analytics](https://www.google.com/analytics/).
You can also ask questions about website testing in the
[Analytics Help Forum](https://support.google.com/analytics/community),
or about search impact in the
[Webmaster Help Forum](https://support.google.com/webmasters/community).
