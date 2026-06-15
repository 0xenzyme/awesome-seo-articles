---
title: "New notifications about inbound links"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2012-07-new-notifications-about-inbound-links"
url: "https://developers.google.com/search/blog/2012/07/new-notifications-about-inbound-links"
canonical: "https://developers.google.com/search/blog/2012/07/new-notifications-about-inbound-links"
author: "Matt Cutts"
published: "2012-07-27T00:00:00+00:00"
updated: "2012-07-27T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:19:39+00:00"
status_code: 200
html_hash: "0f52539c3174db722af05471b0325ea019196795b125e0628b554f62686a9941"
clean_word_count: 1454
clean_char_count: 8458
---
# New notifications about inbound links

Lots of site owners use our
[webmaster console](https://search.google.com/search-console)
to see how their site is doing in Google. Last week we
[began sending new messages](https://plus.google.com/109412257237874861202/posts/gik49G9c5LU)
to sites with a pattern of unnatural links pointing to them, and I wanted to give more context
about these new messages.

## Original Link Messages

First, let's talk about the original link messages that we've been sending out for months. When we
see unnatural links pointing to a site, there are different ways we can respond. In many severe
cases, we reduce our trust in the entire site. For example, that can happen when we believe a site
has been engaging in a pretty widespread pattern of link spam over a long period of time. If your
site is notified for these unnatural links, we recommend removing as many of the spammy or
low-quality links as you possibly can and then submitting a
[reconsideration request](https://www.google.com/webmasters/tools/reconsideration)
for your site.

In a few situations, we have heard about directories or blog networks that won't take links down.
If a website tries to charge you to put links up and to take links down, you can let us know about
that, either in your reconsideration request or by mentioning it on our
[webmaster forum](https://support.google.com/webmasters/community)
or in a separate
[spam report](/search/docs/advanced/guidelines/report-spam). We have taken action on
several such sites, because they often turn out to be doing link spamming themselves.

## New Link Messages

In less severe cases, we sometimes target specific spammy or artificial links created as part of
a link scheme and distrust only those links, rather than taking action on a site's overall
ranking. The new messages make it clear that we are taking "targeted action on the unnatural links
instead of your site as a whole." The new messages also lack the yellow exclamation mark that
other messages have, which tries to convey that we're addressing a situation that is not as
severe as the previous "we are losing trust in your entire site" messages.

## How serious are these new link messages?

These new messages are worth your attention. Fundamentally, it means we're distrusting some links
to your site. We often take this action when we see a site that is mostly good but might have some
spammy or artificial links pointing to it (widgetbait, paid links, blog spam, guestbook spam,
excessive article directory submissions, excessive link exchanges, other types of linkspam, etc.).
So while the site's overall rankings might not drop directly, likewise the site might not be able
to rank for some phrases. I wouldn't classify these messages as purely advisory or something to
be ignored, or only for innocent sites.

On the other hand, I don't want site owners to panic. We do use this message some of the time for
innocent sites where people are pointing hacked anchor text to their site to try to make them rank
for queries like "buy viagra".

## Example scenario: widget links

A fair number of site owners emailed me after receiving one of the new messages, and I think it
might be helpful if I paraphrased some of their situations to give you an idea of what it might
mean if you get one of these messages.

The first example is widget links. An otherwise good site emailed me about the message. Here's
what I wrote back, with the identifying details removed:

*"Looking into the very specific action that we took, I think we did the right thing. Take URL1
and URL2 for example. These pages are using your EXAMPLE1 widgets, but the pages include
keyword-rich anchortext pointing to your site's url. One widget has the link ANCHORTEXT1 and
the other has ANCHORTEXT2.*
*If you do a search for "widgetbait matt cutts" you'll find tons of stories where I discourage
people from putting keyword-rich anchortext into their widgets; see
https://www.stonetemple.com/articles/interview-matt-cutts-061608.shtml for example. So this
message is a way to tell you that not only are those links in your widget not working, they're
probably keeping that page from ranking for the phrases that you're using."*

## Example scenario: paid links

The next example is paid links. I wrote this email to someone:

*"I wouldn't recommend that Company X ignore this message. For example, check out
SPAMMY\_BLOG\_POST\_URL. That's a link from a very spammy website, and it calls into question the
linkbuilding techniques that Company X has been using (we also saw a bunch of links due to
widgets). These sorts of links are not helping Company X, and it would be worth their time to
review how and why they started gathering links like this."*

I also wrote to another link building SEO who got this message pointing out that the SEO was
getting links from a directory that appeared to offer only paid links that pass PageRank, and so
we weren't trusting links like that.

Here's a final example of paid links. I emailed about one company's situation as follows:

*"Company Y is getting this message because we see a long record of buying paid links that pass
PageRank. In particular, we see a lot of low-quality 'sponsored posts' with keyword-rich
anchortext where the links pass PageRank. The net effect is that we distrust a lot of links
to this site. Here are a couple examples: URL1 and URL2. Bear in mind that we have more examples
of these paid posts, but these two examples give a flavor of the sort of thing that should
really be resolved. My recommendation would be to get these sort of paid posts taken down, and
then Company Y could submit a reconsideration request. Otherwise, we'll continue to distrust
quite a few links to the site."*

## Example scenario: reputation management

In some cases we're ignoring links to a site where the site itself didn't violate our guidelines.
A good example of that is reputation management. We had two groups write in; one was a large news
website, while the other was a not-for-profit publisher. Both had gotten the new link message. In
one case, it appeared that a "reputation management" firm was using spammy links to try to push up
positive articles on the news site, and we were ignoring those links to the news site. In the
other case, someone was trying to manipulate the search results for a person's name by buying
links on a well-known paid text link ad network. Likewise, we were just ignoring those specific
links, and the not-for-profit publisher didn't need to take any action.

## What should I do if I get the new link message?

We recently launched the ability to
[download backlinks to your site sorted by date](https://plus.google.com/113006028898915385825/posts/gEBvDvXmvux).
If you get this new link message, you may want to check your most recent links to spot anything
unusual going on. If you discover that someone in your company has been doing widgetbait, paid
links, or serious linkspam, it's worth cleaning that up and submitting a reconsideration request.
We're also looking at some ways to provide more concrete examples to make these messages more
actionable and to help narrow down where to look when you get one.

Just to give you some context, less than 20,000 domains received these new messages—that's less
than one-tenth the number of messages we send in a typical month—and that's only because we sent
out messages retroactively to any site where we had distrusted some of the sites' backlinks. Going
forward, based on our current level of action, on average only about 10 sites a day will receive
this message.

## Summing up

I hope this post and some of the examples above will help to convey the nuances of this new
message. If you get one of these new messages, it's not a cause for panic, but neither should you
completely ignore it. The message says that the current incident isn't affecting our opinion of
the entire website, but it is affecting our opinion of some links to the website, and the site
might not rank as well for some phrases as a result.

This message reflects an issue of moderate severity, and we're trying to find the right way to
alert people that their site may have a potential issue (and it's worth some investigation)
without overly stressing out site owners either. But we wanted to take this extra step toward more
transparency now so that we can let site owners know when they might want to take a closer look
at their current links.
