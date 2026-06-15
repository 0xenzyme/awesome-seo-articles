---
title: "Helping webmasters re-secure their sites"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2016-04-helping-webmasters-re-secure-their-sites"
url: "https://developers.google.com/search/blog/2016/04/helping-webmasters-re-secure-their-sites"
canonical: "https://developers.google.com/search/blog/2016/04/helping-webmasters-re-secure-their-sites"
author: "Kurt Thomas and Yuan Niu, Spam and Abuse Research"
published: "2016-04-19T00:00:00+00:00"
updated: "2016-04-19T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2016_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:28:34+00:00"
status_code: 200
html_hash: "9a8ce9221ee35a0d53920f218531d6cf159a54a435919423b86243f9eee42a87"
clean_word_count: 897
clean_char_count: 5971
---
# Helping webmasters re-secure their sites

*Cross-posted from the
[Google Security Blog](https://security.googleblog.com/2016/04/helping-webmasters-re-secure-their-sites.html).*

Every week,
[over 10 million users encounter harmful websites](https://www.google.com/transparencyreport/safebrowsing/)
that deliver malware and scams. Many of these sites are compromised personal blogs or small
business pages that have fallen victim due to a weak password or outdated software. Safe Browsing
and Google Search protect visitors from dangerous content by displaying browser warnings and
labeling search results with
['this site may harm your computer'](https://support.google.com/websearch/answer/45449).
While this helps keep users safe in the moment, the compromised site remains a problem that needs
to be fixed.

Unfortunately, many webmasters for compromised sites are unaware anything is amiss. Worse yet,
even when they learn of an incident, they may lack the security expertise to take action and
address the root cause of compromise. Quoting one webmaster from a survey we conducted, "our
daily and weekly backups were both infected" and even after seeking the help of a specialist,
after "lots of wasted hours/days" the webmaster abandoned all attempts to restore the site and
instead refocused his efforts on "rebuilding the site from scratch".

In order to find the best way to help webmasters clean-up from compromise, we recently teamed up
with the University of California, Berkeley to explore how to quickly contact webmasters and
expedite recovery while minimizing the distress involved. We've summarized our key lessons below.
The full study, which you can read
[full study on Remedying Web Hijacking](https://research.google.com/pubs/pub44924),
was recently presented at the
[International World Wide Web Conference](https://www2016.ca/).

When Google works directly with webmasters during critical moments like security breaches, we can
help 75% of webmasters re-secure their content. The whole process takes a median of 3 days. This
is a better experience for webmasters and their audience.

## How many sites get compromised?

![Number of freshly compromised sites Google detects every week.](/static/search/blog/images/import/f510f348dd26b07ba4d411b616e82356.jpg)

Number of freshly compromised sites Google detects every week.

Over the last year Google detected nearly 800,000 compromised websites—roughly 16,500 new sites
every week from around the globe. Visitors to these sites are exposed to low-quality scam content
and malware via
[drive-by downloads](https://security.googleblog.com/2008/02/all-your-iframe-are-point-to-us.html).
While browser and search warnings help protect visitors from harm, these warnings can at times
feel punitive to webmasters who learn only after-the-fact that their site was compromised. To
balance the safety of our users with the experience of webmasters, we set out to find the best
approach to help webmasters recover from security breaches and ultimately reconnect websites with
their audience.

## Finding the most effective ways to aid webmasters

1. **Getting in touch with webmasters:**
   One of the hardest steps on the road to recovery is first getting in contact with webmasters. We
   tried three notification channels: email, browser warnings, and search warnings. For webmasters
   who proactively registered their site with
   [Search Console](https://search.google.com/search-console), we found
   that email communication led to 75% of webmasters re-securing their pages. When we didn't know a
   webmaster's email address, browser warnings and search warnings helped 54% and 43% of sites
   clean up respectively.
2. **Providing tips on cleaning up harmful content:**
   Attackers rely on hidden files, easy-to-miss redirects, and remote inclusions to serve scams and
   malware. This makes clean-up increasingly tricky. When we emailed webmasters, we included tips
   and samples of exactly which pages contained harmful content. This, combined with expedited
   notification, helped webmasters clean up 62% faster compared to no tips—usually within 3 days.
3. **Making sure sites stay clean:**
   Once a site is no longer serving harmful content, it's important to make sure attackers don't
   reassert control. We monitored recently cleaned websites and found 12% were compromised again in
   30 days. This illustrates the challenge involved in identifying the root cause of a breach
   versus dealing with the side-effects.

## Making security issues less painful for webmasters—and everyone

We hope that webmasters never have to deal with a security incident. If you are a webmaster, there
are some quick steps you can take to reduce your risk. We've made it easier to
[receive security notifications through Google Analytics](https://security.googleblog.com/2015/02/safe-browsing-and-google-analytics.html)
as well as through
[Search Console](https://search.google.com/search-console). Make sure
to register for both services. Also, we have laid out helpful tips for
[updating your site's software](/search/blog/2015/07/nohacked-how-to-avoid-being-target-of)
and [adding additional authentication](/search/blog/2015/08/nohacked-using-two-factor)
that will make your site safer.

If you're a hosting provider or building a service that needs to notify victims of compromise,
understand that the entire process is distressing for users. Establish a reliable communication
channel before a security incident occurs, make sure to provide victims with clear recovery steps,
and promptly reply to inquiries so the process feels helpful, not punitive.

As we work to make the web a safer place, we think it's critical to empower webmasters and users
to make good security decisions. It's easy for the security community to be pessimistic about
incident response being 'too complex' for victims, but as our findings demonstrate, even just
starting a dialogue can significantly expedite recovery.
