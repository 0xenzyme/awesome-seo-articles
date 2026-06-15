---
title: "Helping hacked sites with reconsideration requests"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2015-09-helping-hacked-sites-with"
url: "https://developers.google.com/search/blog/2015/09/helping-hacked-sites-with"
canonical: "https://developers.google.com/search/blog/2015/09/helping-hacked-sites-with"
author: "Josh Feira and Yuan Niu, Search Quality Team"
published: "2015-09-23T00:00:00+00:00"
updated: "2015-09-23T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2015_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:27:29+00:00"
status_code: 200
html_hash: "612bd3a4a26bbaab129edf816f5c95dccdfe52bfef87b9b555ea404e2acc4c77"
clean_word_count: 805
clean_char_count: 5257
---
# Helping hacked sites with reconsideration requests

Thus far in 2015 we have seen a 180% increase in the number of sites getting hacked and a 300%
increase in hacked site reconsideration requests. While we are working hard to help webmasters
prevent hacks in the first place through efforts such as
[blog posts](/search/blog/2014/02/3tipstofindhacking) and
[#NoHacked](/search/blog/2015/07/nohacked-how-to-avoid-being-target-of) campaigns, we
recognize that our reconsideration process is an important part of making recovering from a hack
faster and easier. Here's what we've been focusing on:

1. Improved communication
2. Better tools
3. Continuous feedback loop

## Improving communications with webmasters of hacked sites

Last year we launched the
"[Note from your reviewer](https://www.seroundtable.com/google-reconsideration-request-note-18708)"
feature in our reconsideration process. This feature enables us to give specific examples and
advice tailored to each case in response to a reconsideration request. Thus far in 2015 we have
sent a customized note to over 70% of webmasters whose hacked reconsideration request was
rejected, with specific guidance on where and how to find the remaining hacked content. The
results have been encouraging, as we've seen a 29% decrease in the average amount of time from
when a site receives a hacked manual action to the time when the webmaster cleans up and the
manual action is removed.

![Example 'note from your reviewer' with detailed guidance and a custom example of hacked text and a hacked page](/static/search/blog/images/import/4d33fe52b0bc333c0d2bcde954a41688.png)

We have also completed our second #NoHacked campaign, with more detailed help on preventing and
recovering from hacks. In the campaign, we focused on ways to improve the security on your site as
well as ways to fix your site if it was compromised. You can catch up by reading the
[first post](/search/blog/2015/07/nohacked-how-to-avoid-being-target-of).

## Better tools including auto-removal of some hacked manual actions

Last year we launched the "Fetch and Render" feature to the
[Fetch as Google](https://support.google.com/webmasters/answer/6066468)
tool, which allows you to see the website exactly as Googlebot sees it. This functionality is
useful in recovering from a hack, since many hackers inject
[cloaked content](/search/docs/essentials/spam-policies#cloaking)
that's not visible to the normal user but obvious to search engine crawlers like Googlebot.

This year we also launched the
[Hacked Sites Troubleshooter](https://support.google.com/webmasters/troubleshooter/6155978)
in 23 languages which guides webmasters through some basic steps to recover from a hack. Let us
know if you have found the troubleshooter useful as we're continuing to expand its features and
impact.

Finally, we're beta testing the automated removal of some hacked manual actions. In Search Console
if Google sees a
["Hacked site" manual action under "Partial matches"](https://support.google.com/webmasters/answer/2604824),
and our systems detect that the hacked content is no longer present, in some cases we will
automatically remove that manual action. We still recommend that you submit a reconsideration
request if you see any manual actions, but don't be surprised if a "Hacked site" manual action
disappears and saves you the trouble!

![Example of a Hacked site manual action on a Partial match: if our systems detect that the hacked content is no longer present, in some cases we will automatically remove the manual action](/static/search/blog/images/import/e6bfeb8701a405ea1f706e0d6e5e2a76.png)

## Soliciting your feedback and taking action

Our improved communication and tools have come directly from feedback we've collected from
webmasters of sites that have been hacked. For example, earlier this year we hosted webmasters who
have been through the hacked reconsideration process in both Mountain View, USA and Dublin,
Ireland for brainstorming sessions. We also randomly sampled webmasters that had been through a
hacked reconsideration. We found that while only 15% of webmasters were dissatisfied with the
process, the main challenges those webmasters faced were in clearer notification of their site
being hacked and clearer guidance on how to resolve the hack. This feedback contributed directly
our more detailed
[blog post](/search/blog/2015/02/case-studies-fixing-hacked-sites) on hacked recovery,
and to much of the content in our latest
[#NoHacked](/search/blog/2015/07/nohacked-how-to-avoid-being-target-of) campaign.

![Googlers in Dublin brainstorming ways to improve the hacked reconsideration process after meeting with local webmasters](/static/search/blog/images/import/9cff722920d8208a0edacfff5fc9bebc.png)

We will continue to support webmasters of hacked sites through the methods detailed above, in
addition to the
[Webmasters help for hacked sites](/web/fundamentals/security/hacked)
portal and the
[security, malware and hacked sites section of our forum](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:security_malware_hacked)).
And we'd love to hear your ideas in the comments below on how Google can better support webmasters
recovering from a hacked website!
