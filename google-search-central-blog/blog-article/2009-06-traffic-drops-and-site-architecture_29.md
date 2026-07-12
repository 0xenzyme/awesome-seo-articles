---
title: "Traffic drops and site architecture issues"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2009-06-traffic-drops-and-site-architecture_29"
url: "https://developers.google.com/search/blog/2009/06/traffic-drops-and-site-architecture_29"
canonical: "https://developers.google.com/search/blog/2009/06/traffic-drops-and-site-architecture_29"
author: "Written by Luisella Mazza, Search Quality Senior Analyst"
published: "2009-06-28T00:00:00+00:00"
updated: "2009-06-28T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:58:58+00:00"
status_code: 200
html_hash: "ac48abeb00ccaaf7bd704efa79adddd846c1e79a7e7a4497ce93ff437e94f06d"
clean_word_count: 874
clean_char_count: 5642
---
# Traffic drops and site architecture issues

We hear lots of questions about site architecture issues and traffic drops, so it was a pleasure
to talk about it in greater detail at
[SMX London](https://searchmarketingexpo.com/london/2009/full_agenda2)
and I'd like to highlight some key concepts from my presentation here. First off, let's gain a
better understanding of drops in traffic, and then we'll take a look at site design and
architecture issues.

## Understanding drops in traffic

As you know, fluctuations in search results happen all the time;
[the web is constantly evolving and so is our index](/search/docs/fundamentals/how-search-works).
Improvements in our ability to understand our users' interests and queries also often lead to
differences in how our algorithms select and rank pages. We realize, however, that such changes
might be confusing and sometimes foster misconceptions, so we'd like to address a couple of these
myths head-on.

## Myth number 1: Duplicate content causes drops in traffic!

Webmasters often wonder if the duplicates on their site can have a negative effect on their site's
traffic. As
[mentioned in our guidelines](/search/docs/advanced/guidelines/duplicate-content),
unless this duplication is intended to manipulate Google and/or users, the duplication is not a
violation of our Webmaster Guidelines. The second part of my presentation illustrates in greater
detail how to deal with duplicate content
[using canonicalization](/search/docs/crawling-indexing/consolidate-duplicate-urls).

## Myth number 2: Affiliate programs cause drops in traffic!

Original and compelling content is crucial for a good user experience. If your website
participates in
[affiliate programs](/search/docs/essentials/spam-policies#thin-affiliate-pages),
it's essential to consider whether the same content is available in many other places on the web.
Affiliate sites with little or no original and compelling content are not likely to rank well in
Google search results, but including affiliate links within the context of original and compelling
content isn't in itself the sort of thing that leads to traffic drops.

Having reviewed a few of the most common concerns, I'd like to highlight two important sections
of the presentation. The first illustrates how malicious attacks—such as an injection of
[hidden text and links](/search/docs/advanced/guidelines/hidden-text-links)
—might cause your site to be removed from Google's search results. On a happier note, it
also covers how you can use the Google cache and Webmaster Tools to identify this issue. On a
related note, if we've found a violation of the Webmaster Guidelines such as the use of hidden
text or the presence of
[malware on your site](/search/blog/2008/10/message-center-warnings-for-hackable),
you will typically find a note regarding this in your Webmaster Tools Message center.

You may also find your site's traffic decreased if your users are being redirected to another
site...for example, due to a hacker-applied server- or page-level redirection triggered by
referrals from search engines. A similar scenario—but with different results—is the
case in which a hacker has instituted a redirection for crawlers only. While this will cause no
immediate drop in traffic since users and their visits are not affected, it might lead to a
decrease in pages indexed over time.

## Site design and architecture issues

Now that we've seen how malicious changes might affect your site and its traffic, let's examine
some design and architecture issues. Specifically, you want to ensure that your site is able to
be both effectively crawled and indexed, which is the prerequisite to being shown in our search
results. What should you consider?

- First off, check that your robots.txt file has the correct status code and is not
  [returning an error](https://www.google.com/support/webmasters/bin/answer.py?answer=35147).
- Keep in mind some best practices when
  [moving to a new site](/search/blog/2008/04/best-practices-when-moving-your-site)
  and the new
  "[Change of address](https://www.google.com/support/webmasters/bin/answer.py?answer=83106)"
  feature
  [recently added](/search/blog/2009/06/out-with-old-in-with-new)
  to Webmaster Tools.
- Review the settings of the robots.txt file to make sure no pages—particularly those
  rewritten and/or dynamic—are blocked inappropriately.
- Finally, make good use of
  [the `rel="canonical"` attribute](/search/docs/crawling-indexing/consolidate-duplicate-urls)
  to reduce the indexing of duplicate content on your domain. The example in the presentation
  shows how using this attribute helps Google understand that a duplicate can be clustered with
  the canonical and that the original, or canonical, page should be indexed.

In conclusion, remember that fluctuations in search results are normal but there are steps that
you can take to avoid malicious attacks or design and architecture issues that might cause your
site to disappear or fluctuate unpredictably in search results. Start by learning more about
[attacks by hackers and spammers](/search/blog/2009/01/preventing-virtual-blight-my),
make sure everything is running properly at crawling and indexing level by double-checking the
[HTML suggestions in Webmaster Tools](https://www.google.com/support/webmasters/bin/answer.py?answer=80407),
and finally,
[test your robots.txt](https://www.google.com/webmasters/tools/robots-testing-tool)
file in case you are accidentally blocking Googlebot. And don't forget about those
["robots.txt unreachable" errors](https://www.google.com/support/webmasters/bin/answer.py?answer=35147)!
