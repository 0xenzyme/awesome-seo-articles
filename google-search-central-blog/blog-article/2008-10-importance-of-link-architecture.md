---
title: "Importance of link architecture"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-10-importance-of-link-architecture"
url: "https://developers.google.com/search/blog/2008/10/importance-of-link-architecture"
canonical: "https://developers.google.com/search/blog/2008/10/importance-of-link-architecture"
author: "Maile Ohye"
published: "2008-10-07T00:00:00+00:00"
updated: "2008-10-07T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:54:55+00:00"
status_code: 200
html_hash: "e90af70da20820595928e189ca743ee7ec273635247b374dfdc304ef620f2719"
clean_word_count: 1011
clean_char_count: 6413
---
# Importance of link architecture

In Day 2 of
[links week](/search/blog/2008/10/links-information-straight-from-source), we'd like
to discuss the importance of link architecture and answer more advanced questions on the topic.
Link architecture—the method of internal linking on your site—is a crucial step in
site design if you want your site indexed by search engines. It plays a critical role in
Googlebot's ability to find your site's pages and ensures that your visitors can navigate and
enjoy your site.

## Keep important pages within several clicks from the home page

Although you may believe that users prefer a search box on your site rather than category
navigation, it's uncommon for search engine crawlers to type into search boxes or navigate via
pulldown menus. So make sure your important pages are clickable from the home page and easy
for Googlebot to find throughout your site. It's best to create a link architecture that's
intuitive for users and crawlable for search engines. Here are more ideas to get started:

### Intuitive navigation for users

Create common user scenarios, get "in character," then try working through your site. For example,
if your site is about basketball, imagine being a visitor (in this case a "baller"
:) trying to learn the best dribbling technique.

- Starting at the home page, if the user doesn't use the search box on your site or a pulldown
  menu, can they easily find the desired information (ball handling like a superstar) from the
  navigation links?
- Let's say a user found your site through an external link, but they didn't land on the home page.
  Starting from any (sub-/child) page on your site, make sure they can easily find their way to
  the home page and/or other relevant sections. In other words, make sure users aren't trapped or
  stuck. Was the "best dribbling technique" easy for your imaginary user to find? Often
  breadcrumbs such as "Home > Techniques
  > Dribbling" help users to understand where they are.

### Crawlable links for search engines

- Text links are easily discovered by search engines and are often the safest bet if your priority
  is having your content crawled. While you're welcome to try the latest technologies,
  keep-in-mind that when text-based links are available and easily navigable for users, chances
  are that search engines can crawl your site as well.

  ```
  This <a href="new-page">text link</a> is easy for search engines to find.
  ```
- [Sitemap](/search/docs/crawling-indexing/sitemaps/overview) submission is also helpful for
  [major search engines](https://www.sitemaps.org/),
  though it shouldn't be a substitute for crawlable link architecture. If your site utilizes
  newer techniques, such as AJAX, see "Verify that Googlebot finds your internal links" below.

## Use descriptive anchor text

Writing descriptive anchor text, the clickable words in a link, is a useful signal to help search
engines and users alike to better understand your content. The more Google knows about your
site—through your content, page titles, anchor text, etc.—the more relevant results we can return
for users (and your potential search visitors). For example, if you run a basketball site and you
have videos to accompany the textual content, a **not-very-optimal way** of linking would be:

```
To see all our basketball videos, <a href="videos">click here</a> for the entire listing.
```

However, instead of the generic "click here," you could rewrite the anchor text
**more descriptively** as:

```
You can browse all of our <a href="videos">basketball videos</a>.
```

## Verify that Googlebot finds your internal links

For verified site owners,
[Webmaster Tools](https://search.google.com/search-console)
has the feature "Links >
[Pages with internal links](https://www.google.com/support/webmasters/bin/answer.py?answer=55281)
that's great for verifying that Googlebot finds most of the links you'd expect. This is especially
useful if your site uses navigation involving JavaScript (which Googlebot doesn't always
execute)—you'll want to make sure that Googlebot is finding other internal links as
expected.

Here's an abridged snapshot of our internal links to the introductory post for "
[`404` week at Webmaster Central](/search/blog/2008/08/its-404-week-at-webmaster-central)".
Our internal links are discovered as we had hoped.

![webmaster tools internal links report](/static/search/blog/images/archived_webmaster-tools-internal-links.png)

## You can ask more internal linking questions

Here are some to get you started...

Q: What about using
[`rel="nofollow"`](/search/docs/advanced/guidelines/qualify-outbound-links)
for maximizing PageRank flow in my internal link architecture (such as
[PageRank sculpting](https://www.google.com/search?q=pagerank+sculpting), or
[PageRank siloing](https://www.google.com/search?q=pagerank+siloing))?
A: It's not something we, as webmasters who also work at Google, would really spend time or
energy on. In other words, if your site already has strong link architecture, it's far more
productive to work on keeping users happy with fresh and compelling content rather than to worry
about PageRank sculpting.

Matt Cutts answered more questions about "appropriate uses of `nofollow`" in our
[webmaster discussion group](https://groups.google.com/group/Google_Webmaster_Help-Indexing/browse_thread/thread/cf504ffd28b6bb68).

Q: Let's say my website is about my favorite hobbies: biking and camping. Should I keep my
internal linking architecture "themed" and not cross-link between the two?
A: We haven't found a case where a webmaster would benefit by intentionally "theming" their link
architecture for search engines. And, keep-in-mind, if a visitor to one part of your site can't
easily reach other parts of your site, that may be a problem for search engines as well.

Perhaps it's cliche, but at the end of the day, and at the end of this post,
:) it's best to create solid link architecture (making navigation
intuitive for users and crawlable for search engines)—implementing what makes sense for your
users and their experience on your site.

Thanks for your time today! Information about outbound links will soon be available in Day 3 of
[links week](/search/blog/2008/10/links-information-straight-from-source). And, if you
have helpful tips about internal links or questions for our team, please share them in the
comments below.
