---
title: "Keeping your hosting service valuable for searchers"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2012-03-keeping-your-free-hosting-service"
url: "https://developers.google.com/search/blog/2012/03/keeping-your-free-hosting-service"
canonical: "https://developers.google.com/search/blog/2012/03/keeping-your-free-hosting-service"
author: "Fili Wiese, Kaspar Szymanski"
published: "2012-03-06T00:00:00+00:00"
updated: "2012-03-06T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:18:18+00:00"
status_code: 200
html_hash: "bd61cc73d379448324ca6f1d5fff10956c646f61ddda2811083d17303cd436d0"
clean_word_count: 733
clean_char_count: 4632
---
# Keeping your hosting service valuable for searchers

[Web hosting services that are available without payment](https://en.wikipedia.org/wiki/Free_web_hosting_service)
can be great! Many of these services have helped to lower costs and technical barriers for
webmasters and they continue to enable beginner webmasters to start their adventure on the web.
Unfortunately, sometimes these lower barriers (meant to encourage less techy audiences) can
attract some dodgy characters like spammers who look for cheap and easy ways to set up
[dozens or hundreds of sites that add little or no value](/search/docs/essentials/spam-policies)
to the web. When it comes to automatically generated sites, our stance remains the same: if the
sites do not add sufficient value, we generally consider them as spam and take appropriate steps
to protect our users from exposure to such sites in our natural search results.

![Example of spammy content](/static/search/blog/images/import/7c94f78de82763d449d5bdc733bfbfcb.png)

We consider automatically generated sites like this one to be spammy.

If a hosting service that's available without payment begins to show patterns of spam, we make a
strong effort to be granular and tackle only spammy pages or sites. However, in some cases, when
the spammers have pretty much taken over the web hosting service or a large fraction of the
service, we may be forced to take more decisive steps to protect our users and remove the entire
web hosting service from our search results. To prevent this from happening, we would like to help
owners of web hosting services by sharing what we think may help you save valuable resources like
bandwidth and processing power, and also protect your hosting service from these spammers:

- Publish a clear abuse policy and communicate it to your users, for example during the sign-up
  process. This step will contribute to transparency on what you consider to be spammy activity.
- In your sign-up form, consider using
  [CAPTCHAs](https://www.google.com/recaptcha/about/) or
  [similar verification tools](https://www.evengrounds.com/developers/alternatives-to-captcha)
  to only allow human submissions and prevent automated scripts from generating a bunch of sites
  on your hosting service. While these methods may not be 100% foolproof, they can help to keep a
  lot of the bad actors out.
- Try to monitor your hosting service for other spam signals like redirections, large numbers of
  ad blocks, certain spammy keywords, large sections of escaped JavaScript code, etc. Using the
  [`site:` operator](/search/docs/monitor-debug/search-operators/all-search-site)
  query or
  [Google Alerts](https://www.google.com/alerts) may come in
  handy if you're looking for a simple, cost efficient solution.
- Keep a record of signups and try to identify typical spam patterns like form completion time,
  number of requests sent from the same IP address range, user-agents used during signup, user
  names or other form-submitted values chosen during signup, etc. Again, these may not always be
  conclusive.
- Keep an eye on your webserver log files for sudden traffic spikes, especially when a
  newly-created site is receiving this traffic, and try to identify why you are spending more
  bandwidth and processing power.
- Try to monitor your web hosting service for phishing and malware-infected pages. For example,
  you can use the [Google Safe Browsing API](/safe-browsing) to
  regularly test URLs from your service, or
  [sign up to receive alerts for your AS (Autonomous System number)](https://googleonlinesecurity.blogspot.com/2010/09/safe-browsing-alerts-for-network.html).
- Come up with a few confidence checks. For example, if you're running a local Polish web hosting
  service, what are the odds of thousands of new and legitimate sites in Japanese being created
  overnight on your service? There's a number of tools you may find useful for language detection
  of newly created sites, for example
  [language detection libraries](https://www.google.com/search?q=language+detection+library)
  or the
  [Google Translate API v2](https://cloud.google.com/translate).

Last but not least, if you run a web hosting service be sure to monitor your services for sudden
activity spikes that may indicate a spam attack in progress.

For more tips on running a quality hosting service, have a look at
[our previous post](/search/blog/2011/12/tips-for-hosting-providers-and). Lastly, be
sure to sign up and verify your site in
[Google Webmaster Tools](https://search.google.com/search-console)
so we may be able to notify you when needed or if we see issues.
