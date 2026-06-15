---
title: "3 tips to find hacking on your site, and ways to prevent and fix it"
source: google-search-central-blog
content_type: "event"
freshness_risk: "historical"
slug: "2014-02-3tipstofindhacking"
url: "https://developers.google.com/search/blog/2014/02/3tipstofindhacking"
canonical: "https://developers.google.com/search/blog/2014/02/3tipstofindhacking"
author: "Megumi Hitomi"
published: "2014-02-28T00:00:00+00:00"
updated: "2014-02-28T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2014_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:23:40+00:00"
status_code: 200
html_hash: "f15a81544f55fef459aedd8d12c487223f4691e2b9efd87cd711657b236fde92"
clean_word_count: 678
clean_char_count: 4292
---
# 3 tips to find hacking on your site, and ways to prevent and fix it

![](/static/search/blog/images/import/ec8ab5b70a5774741c0cdc5619f54dd3.png)

Google shows this message in search results for
[sites that we believe may have been compromised](https://support.google.com/websearch/answer/190597).
You might not think your site is a target for hackers, but it's surprisingly common. Hackers
target large numbers of sites all over the web in order to exploit the sites' users or reputation.

One common way hackers take advantage of vulnerable sites is by adding spammy pages. These spammy
pages are then used for various purposes, such as redirecting users to undesired or harmful
destinations. For example, we've recently seen an increase in hacked sites redirecting users to
fake online shopping sites.

Once you recognize that your website may have been hacked, it's important to diagnose and fix the
problem as soon as possible. We want webmasters to keep their sites secure in order to protect
users from spammy or harmful content.

## 3 tips to help you find hacked content on your site

1. **Check your site for suspicious URLs or directories**:
   Keep an eye out for any suspicious activity on your site by performing a
   [`site:` search](/search/docs/monitor-debug/search-operators/all-search-site)
   of your site in Google, such as `site:example.com`. Are there any suspicious URLs
   or directories that you do not recognize?

   You can also set up a
   [Google Alert](https://www.google.com/alerts)
   for your site. For example, if you set a Google Alert for
   `site:example.com (viagra|cialis|casino|payday loans)`, you'll receive an email
   when these keywords are detected on your site.
2. **Look for unnatural queries on the Search Queries page in Webmaster Tools**:
   The
   [Search Queries](https://support.google.com/webmasters/answer/35252)
   page shows Google Web Search queries that have returned URLs from your site. Look for
   unexpected queries as it can be an indication of hacked content on your site.

   Don't be quick to dismiss queries in different languages. This may be the result of spammy
   pages in other languages placed on your website.

   ![Example of an English site hacked with Japanese content.](/static/search/blog/images/import/f2db9e903acb7b6c7e0503db894e1f49.png)
3. **Enable email forwarding in Webmaster Tools**
   Google will send you a message if we detect that your site may be compromised. Messages appear
   in Webmaster Tools' Message Center but it's a best practice to also
   [forward these messages to your email](https://support.google.com/webmasters/answer/140528).
   Keep in mind that Google won't be able to detect all kinds of hacked content, but we hope our
   notifications will help you catch things you may have missed.

## Tips to fix and prevent hacking

- **Stay informed**:
  The [Security Issues](/search/blog/2013/10/easier-recovery-for-hacked-sites) section
  in Webmaster Tools will show you hacked pages that we detected on your site. We also provide
  [detailed information to help you fix your hacked site](/web/fundamentals/security/hacked).
  Make sure to read through this documentation so you can quickly and effectively fix your site.
- **Protect your site from potential attacks**:
  It's better to prevent sites from being hacked than to clean up hacked content. Hackers will
  often take advantage of security vulnerabilities on commonly used website management software.
  Here are some tips to keep your site safe from hackers:

  - Always keep the software that runs your website up-to-date.
  - If your website management software tools offer security announcements, sign up to get the
    latest updates.
  - If the software for your website is managed by your hosting provider, try to choose a
    provider that you can trust to maintain the security of your site.

We hope this post makes it easier for you to identify, fix, and prevent hacked spam on your site.
If you have any questions, drop by the
[Google Webmaster Help Forum](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:security_malware_hacked)).

If you find suspicious sites in Google search results, please report them using
[the Spam Report tool](/search/docs/advanced/guidelines/report-spam).
