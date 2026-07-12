---
title: "Your fast pass through security"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-04-your-fast-pass-through-security"
url: "https://developers.google.com/search/blog/2011/04/your-fast-pass-through-security"
canonical: "https://developers.google.com/search/blog/2011/04/your-fast-pass-through-security"
author: "Kevin Marshall, Konstantin Roslyakov, Ian Porteous"
published: "2011-04-19T00:00:00+00:00"
updated: "2011-04-19T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:12:46+00:00"
status_code: 200
html_hash: "bd1e664b2bb47b2bb7f0d53a9770e525caa4dc2eacc7ffb05c693b65be4e7e25"
clean_word_count: 417
clean_char_count: 2690
---
# Your fast pass through security

Security checks are nobody's cup of tea. We've never seen people go through airport baggage
checks for fun. But while security measures are often necessary, that doesn't mean they have to
be painful. In that spirit, we've implemented several major improvements to make the Google Site
Verification process faster, more straightforward, and perhaps even a pleasure to use—so you can
get on with the tasks that matter to you.

## New verification method recommendations

![The old site verification tool in Webmaster Tools](/static/search/blog/images/import/201112eac76d5a206b1079234a87e235.png)

You'll quickly notice the changes we've made to the verification page, namely the new tabbed
interface. These tabs allow us to give greater visibility to the verification method that we think
will be most useful to you, which is listed in the Recommended Method tab.

![The new site verification tool in Webmaster Tools with alternative verification methods](/static/search/blog/images/import/11f99aa6ce48520c76716087245ba773.png)

Our recommendation is just an educated guess, but sometimes guesses can be wrong. It's possible
that the method we recommend might not work for you. If this is the case, simply click the
"Alternate methods" tab to see the other verification methods that are available. Verifying with
an alternate method is just as powerful as verifying with a recommended method.

Our recommendations are computed from statistical data taken from users with a similar
configuration to yours. For example, we can guess which verification methods might be successful
by looking at the public hosting information for your website. In the future we plan to add more
signals so that we can provide additional customized instructions along with more relevant
recommendations.

## New Google Sites Are Automatically Verified

For some of you, we've made the process even more effortless—Google Sites administrators are now
automatically verified for all new sites that they create. When you create a new Google Site,
it'll appear verified in the details page. The same goes for adding or removing owners: when you
edit the owners list in your Google Site's settings, the changes will automatically appear in
Webmaster Tools.

One thing to note is that we're unable to automatically verify preexisting Google Sites at this
time. If you'd like to verify your older Google Sites, please continue to use the `meta` tag method
already available.

We hope these enhancements help get you through security even faster. Should you get pulled over
and have any questions, check out our
[Webmaster Help Forums](https://support.google.com/webmasters/community).
