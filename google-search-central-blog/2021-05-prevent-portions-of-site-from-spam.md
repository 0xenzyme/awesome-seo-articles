---
title: "Prevent portions of your site from being abused by spam"
source: google-search-central-blog
content_type: "event"
freshness_risk: "historical"
slug: "2021-05-prevent-portions-of-site-from-spam"
url: "https://developers.google.com/search/blog/2021/05/prevent-portions-of-site-from-spam"
canonical: "https://developers.google.com/search/blog/2021/05/prevent-portions-of-site-from-spam"
author: "the Search Quality Team"
published: "2021-05-26T00:00:00+00:00"
updated: "2021-05-26T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2021_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:39:00+00:00"
status_code: 200
html_hash: "a090d0164e7de386a3b4b1a0ebf9207fdd2417f27bcf68bfcc4759f56f82bd59"
clean_word_count: 1326
clean_char_count: 8930
---
# Prevent portions of your site from being abused by spam

As a website owner, you might provide a few channels where your users can interact, such as forums,
guestbooks, social media platforms, file uploaders, hosting services, or internal search
services. These services allow users to create an account to post content, upload a file, or search
on your site. Unfortunately, spammers often take advantage of these types of services to generate
hundreds of spam pages that add little or no value to the web. Under the principles set out in
[Google's Webmaster Guidelines](/search/docs/essentials),
this may result in Google taking manual actions against the affected pages. Here are some examples:

![Abused forum/guestbook](/static/search/blog/images/abused-forum.png "Abused forum/guestbook")
![Abused file uploader with spammy PDF file](/static/search/blog/images/abused-file-uploader.png "Abused file uploader with spammy PDF file")
![Abused hosting services](/static/search/blog/images/abused-free-hosting.png "Abused hosting services")
![Abused internal search results](/static/search/blog/images/abused-internal-search-results.png "Abused internal search results")

Spammy content like this can be harmful to your site and users in several ways:

- Low-quality content on some parts of a website can impact the whole site's ranking.
- Spammy content can potentially lead users to unwanted or even harmful content, such as sites
  with malware or phishing, which may lower the reputation of your site.
- Unintended traffic from unrelated content on your site can slow down your site and raise
  hosting costs.
- Google might remove or demote pages that are overrun with third-party generated spam to protect
  the quality of our search results.

In this blog post, we will provide some tips to prevent spammers from abusing your site.

## Block automated account creation

When users create an account on your site, consider using Google's
[CAPTCHAs](https://www.google.com/recaptcha/about/) service or similar
verification tools (for example: [Securimage](https://www.phpcaptcha.org/)
or [Jcaptcha](https://jcaptcha.sourceforge.net/)) to only allow human
submissions and prevent automated scripts from generating accounts and content on your site's
public platforms.

Requiring new users to validate a real email address when they sign up for a new account can also
prevent many spam bots from automatically creating accounts. Additionally, you can set up filters
to block email addresses that are suspicious or originating from email services that you don't
trust.

## Turn on moderation features

Consider enabling comment and profile creation moderation features that require users to have a
certain reputation before links can be posted. If possible, change your settings so that you don't
allow anonymous posting, and make posts from new users require approval before they are publicly
visible.

## Monitor your site for spammy content and clean up any issues

Register and verify your website ownership in [Search
Console](https://support.google.com/webmasters/answer/9128669). To see if there are any issues detected by Google, check the
[Security Issues
report](https://support.google.com/webmasters/answer/9044101) and [Manual
actions report](https://support.google.com/webmasters/answer/9044175). You can also check the Messages panel to learn more information.

![A message in Search Console about a site abused with third-party spam](/static/search/blog/images/third-party-spam.png)

In addition, it is good to occasionally check your site for unexpected or spammy content by using
the [`site:`
operator](https://support.google.com/websearch/answer/2466433) in Google Search, together with commercial or adult keywords that are unrelated to
your site's topic. For example, search for [`site:your-domain-name viagra`] or
[`site:your-domain-name watch online`] to detect the irrelevant content on your site,
especially for:

- Out-of-context text or off-topic links with the sole purpose of promoting a third-party
  website/services (for example, "free movie download/watch online")
- Gibberish or text that is automatically generated (not written by a real user)
- [Internal search results](/search/docs/fundamentals/seo-starter-guide#no-find) where
  the user query appears off-topic with the purpose of promoting a third-party website/services

Monitor your web server log files for sudden traffic spikes, especially for newly created pages.
For example, look for any URLs with keywords in URL patterns that are completely irrelevant to
your website. To identify potential high traffic problematic URLs, use the
[Pages
report](https://analytics.google.com/analytics/web/#/report/content-overview/) in Google Analytics.

Block obviously inappropriate content from being published to your platform with a list of spammy
terms (for example: streaming or download, adult, gambling, pharma related terms). Built-in
features or plugins can delete or mark these content as spam for you.

Another great tool for this is [Google
Alerts](https://www.google.com/alerts). Set up a [`site:your-domain-name spammy-keywords`] alert using commercial
or adult keywords that you wouldn't expect to see on your site. Google Alerts is also a great tool
for detecting hacked pages.

## Identify and terminate spam accounts

Monitor your web server log for user sign-ups and identify typical spam patterns, such as:

- Large number of sign-up form completions within a short time.
- Number of requests sent from the same IP address range.
- Unexpected user agents used during sign-up.
- Nonsense user names or other nonsense submitted values during sign-up. For example, commercial
  usernames (names like "Free movie download") that don't sound like real human names and link to
  unrelated sites.

## Prevent Google Search from showing or following untrusted content

If your site allows users to create pages like profile pages, forum threads, or websites, you can
deter spam abuse by preventing Google Search from showing or following new or untrusted content.

For example, you can use the [`noindex`
meta standard](/search/docs/crawling-indexing/block-indexing) to block access to untrusted pages. Like this:

```
<html>
  <head>
    <meta name="googlebot" content="noindex">
  </head>
</html>
```

Or you can use the [robots.txt standard](/search/docs/crawling-indexing/robots/intro) to
temporarily block the pages. For example:

```
Disallow: /guestbook/
```

You can also mark user-generated content (UGC) links, such as comments and forum posts, as UGC by
using `rel="ugc"`
or `rel="nofollow"`.
This helps you explain your relationship with the linked page to Google and request that Google not
follow that link.

## Consolidate your open platform content into a concentrated file path or directory

With automated scripts or software, spammers can generate a large number of spammy pages on your
site in a short time. Some of this content may be hosted in fragmented file paths or directories,
which prevent site owners from effectively detecting and cleaning up spam. Some examples are like:

```
example.com/best-online-pharma-buy-red-viagra-online
example.com/free-watch-online-2021-full-movie
```

It is also recommended to consolidate your user-generated content into a concentrated file path or
directory for easier maintenance and spam detection. For example, the following file path would be
recommended:

```
example.com/user-generated-content-dir-name/example01.html
example.com/user-generated-content-dir-name/example02.html
```

## Keep your website software updated and use automated systems to defend your site

Take the time to keep your software up-to-date and pay special attention to important security
updates. Spammers may take advantage of security issues in older versions of blogs, bulletin
boards, and other content management systems.

In addition, some comprehensive anti-spam systems like
[Akismet](https://akismet.com/) have plugins for many blogs
and forum systems that are easy to install and do most of the spam fighting work for you.
Additionally, there are trusted and well-known security plugins available for some platforms,
which help secure the website, and may be able to catch abuse early.

Depending on your site's situation, please check out our documentation for more detailed information:

- [Protect your site from
  user-generated spam](/search/blog/2017/01/protect-your-site-from-user-generated)
- [Ways to prevent comment
  spam](/search/docs/advanced/guidelines/prevent-comment-spam)
- [Preventing spam on host
  services](/search/docs/advanced/guidelines/free-web-hosters)
- [Applying best practices on internal
  search results](/search/docs/fundamentals/seo-starter-guide#no-find)
- [Fixing hacked pages](/web/fundamentals/security/hacked)

You can also visit our [Search
Central Help Community](https://support.google.com/webmasters/community/) if you need any help.
