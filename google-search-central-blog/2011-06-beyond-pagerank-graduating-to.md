---
title: "Beyond PageRank: Graduating to actionable metrics"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-06-beyond-pagerank-graduating-to"
url: "https://developers.google.com/search/blog/2011/06/beyond-pagerank-graduating-to"
canonical: "https://developers.google.com/search/blog/2011/06/beyond-pagerank-graduating-to"
author: "Susan Moskwa"
published: "2011-07-01T00:00:00+00:00"
updated: "2011-07-01T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:13:34+00:00"
status_code: 200
html_hash: "e25062b9a7a4e9b44c7ed34ba915a2300cd0349b6194b4f8e7c9a7124e311878"
clean_word_count: 1450
clean_char_count: 8632
---
# Beyond PageRank: Graduating to actionable metrics

Like any curious netizen, I have a
[Google Alert](https://www.google.com/alerts)
set up to email me whenever my name is mentioned online. Usually I get a slow trickle of
[my forum posts](https://www.google.com/support/forum/user?userid=08843502888744721567),
[blog posts](/s/results/search/blog?q=%22by+susan+moskwa%22), and
[tweets](https://twitter.com/SusanMoskwa). But by far the most
popular topic of these alerts over the past couple years has been my off-handed mention that
[we removed PageRank distribution data from Webmaster Tools](https://support.google.com/webmasters/community/thread?tid=6a1d6250e26e9e48&hl=en)
in one of our 2009 releases.

The fact that people are still writing about this almost two years later—usually in the context
of "Startling news from Susan Moskwa: ..."—really drives home how much PageRank has become a
go-to statistic for some webmasters. Even the most inexperienced site owners I talk with have
often heard about, and want to know more about, PageRank ("PR") and what it means for their site.
However, as I said in my fateful forum post, the Webmaster Central team has been telling
webmasters for years that they shouldn't focus so much on PageRank as a metric for representing
the success of one's website. Today I'd like to explain this position in more detail and give
you some relevant, actionable options to fill your time once you stop tracking your PR!

## Why PageRank?

In 2008 Udi Manber, VP of engineering at Google,
[wrote on the Official Google Blog](https://googleblog.blogspot.com/2008/05/introduction-to-google-search-quality):

> The most famous part of our ranking algorithm is PageRank, an algorithm developed by Larry Page
> and Sergey Brin, who founded Google. PageRank is still in use today, but it is now a part of a
> much larger system.

PageRank may have distinguished Google as a search engine when it was founded in 1998; but given
the rate of change Manber describes—launching "about 9 [improvements] per week on the
average"—we've had a lot of opportunity to augment and refine our ranking systems over the last
decade. PageRank is no longer—if it ever was—the be-all and end-all of ranking.

If you look at Google's
[Technology Overview](https://www.google.com/corporate/tech),
you'll notice that it calls out relevance as one of the top ingredients in our search results. So
why hasn't as much ink been spilled over relevance as has been over PageRank? I believe it's
because PageRank comes in a number, and relevance doesn't. Both relevance and PageRank include a
lot of complex factors—context, searcher intent, popularity, reliability—but it's easy to graph
your PageRank over time and present it to your CEO in five minutes; not so with relevance. I
believe the succinctness of PageRank is why it's become such a go-to metric for webmasters over
the years; but just because something is easy to track doesn't mean it accurately represents
what's going on on your website.

## What do we really want?

I posit that none of us *truly* care about PageRank as an end goal. PageRank is just a
stand-in for what we really want: for our websites to make more money, attract more readers,
generate more leads, more newsletter sign-ups, etc. The focus on PageRank as a success metric only
works if you assume that a higher PageRank results in better ranking, then assume that that will
drive more traffic to your site, then assume that that will lead to more people
doing-whatever-you-want-them-to-do on your site. On top of these assumptions, remember that we
only update the PageRank displayed on the Google Toolbar a few times a year, and we may
[lower the PageRank displayed for some sites](/search/blog/2007/12/information-about-buying-and-selling)
if we believe they're engaging in spammy practices. So the PR you see publicly is different from
the number our algorithm actually uses for ranking. Why bother with a number that's at *best*
three steps removed from your actual goal, when you could instead directly measure what you want
to achieve? Finding metrics that are directly related to your business goals allows you to spend
your time furthering those goals.

## If I don't track my PageRank, what should I be tracking?

Take a look at metrics that correspond directly to meaningful gains for your website or business,
rather than just focusing on ranking signals. Also consider metrics that are updated daily or
weekly, rather than numbers (like PageRank) that only change a few times a year; the latter is far
too slow for you to reliably understand which of your changes resulted in the number going up or
down (assuming you update your site more than a few times a year). Here are three suggestions to
get you started, all of which you can track using services like
[Google Analytics](https://www.google.com/analytics/) or
[Webmaster Tools](https://search.google.com/search-console):

1. Conversion rate
2. Bounce rate
3. Clickthrough rate (CTR)

### Conversion rate

A "conversion" is when a visitor does what you want them to do on your website. A conversion might
be completing a purchase, signing up for a mailing list, or downloading a white paper. Your
conversion rate is the percentage of visitors to your site who convert (perform a conversion).
This is a perfect example of a metric that, unlike PageRank, is directly tied to your business
goals. When users convert they're doing something that *directly benefits* your organization
in a measurable way! Whereas your PageRank is both difficult to measure accurately (see above),
and can go up or down without having any direct effect on your business.

### Bounce rate

A "bounce" is when someone comes to your website and then leaves without visiting any other pages
on your site. Your
[bounce rate](https://www.google.com/support/analytics/bin/answer.py?answer=81986)
is the percentage of visits to your site where the visitor bounces. A high bounce rate may
indicate that users don't find your site compelling, because they come, take a look, and leave
directly. Looking at the bounce rates of different pages across your site can help you identify
content that's underperforming and point you to areas of your site that may need work. After all,
it doesn't matter how well your site ranks if most searchers are bouncing off of it as soon as
they visit.

### Clickthrough rate (CTR)

In the context of organic search results, your clickthrough rate is how often people click on your
site out of all the times your site gets shown in search results. A low CTR means that, no matter
how well your site is ranking, users aren't clicking through to it. This may indicate that they
don't think your site will meet their needs, or that some other site looks better. One way to
improve your CTR is to look at your site's titles and snippets in our search results: are they
compelling? Do they accurately represent the content of each URL? Do they give searchers a reason
to click on them? Here's some
[advice for improving your snippets](/search/blog/2007/09/improve-snippets-with-meta-description);
the
[HTML suggestions](https://www.google.com/support/webmasters/bin/answer.py?answer=80407)
section of Webmaster Tools can also point you to pages that may need help. Again, remember that it
doesn't matter how well your site ranks if searchers don't want to click on it.

Entire blogs and books have been dedicated to explaining and exploring web metrics, so you'll
excuse me if my explanations just scrape the surface; analytics evangelist
[Avinash Kaushik's site](https://www.kaushik.net/avinash/) is a
great place to start if you want to dig deeper into these topics. But hopefully I've at least
convinced you that there are more direct, effective and controllable ways to measure your site's
success than PageRank.

One final note: Some site owners are interested in their site's PR because people won't buy links
from their site unless they have a high PageRank.
[Buying or selling links for the purpose of passing PageRank violates our Webmaster Guidelines](/search/blog/2007/12/information-about-buying-and-selling)
and is very likely to have negative consequences for your website, so a) I strongly recommend
against it, and b) don't be surprised if we aren't interested in helping you raise your PageRank
or improve your website when this is your stated goal.

We'd love to hear what metrics you've found useful and actionable for your website! You can share
your success stories with us in the comments here or in our
[Webmaster Help Forum](https://support.google.com/webmasters/community/thread?tid=21b908489e1bbf66&hl=en).
