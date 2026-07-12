---
title: "Webmaster Tools verification strategies"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2012-12-webmaster-tools-verification-strategies"
url: "https://developers.google.com/search/blog/2012/12/webmaster-tools-verification-strategies"
canonical: "https://developers.google.com/search/blog/2012/12/webmaster-tools-verification-strategies"
author: "John Mueller"
published: "2012-12-17T00:00:00+00:00"
updated: "2012-12-17T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:20:49+00:00"
status_code: 200
html_hash: "a37100536652d939c3ab519870b43baab0d8721819e9c57657a9d427aee8d3f7"
clean_word_count: 453
clean_char_count: 2838
---
# Webmaster Tools verification strategies

[Verifying ownership](https://support.google.com/webmasters/answer/9008080)
of your website is the first step towards using
[Google Webmaster Tools](https://search.google.com/search-console). To
help you keep verification simple and reduce its maintenance to a minimum, especially when you
have multiple people using Webmaster Tools, we've put together a small list of tips and tricks
that we'd like to share with you:

- The method that you choose for verification is up to you, and may depend on your CMS and hosting
  providers. If you want to be sure that changes on your side don't result in an accidental loss
  of the verification status, you may even want to consider using two methods in parallel.
- Back in 2009, we [updated the
  format of the verification `meta` tag and file](/search/blog/2009/10/changes-to-website-verification-in). If you're still using the old format, we
  recommend moving to the newer version. The newer
  [`meta` tag](/search/docs/advanced/crawling/special-tags)
  is called `google-site-verification`, and the newer file format
  contains just one line with the file name. While we're currently supporting ye olde format, using
  the newer one ensures that you're good to go in the future.
- When removing users' access in Webmaster Tools, remember to remove any active associated
  verification tokens (for example, a file or a `meta` tag). Leaving them on your server means that
  these users would be able to gain access again at any time. You can view the site owners list in
  Webmaster Tools under Configuration / Users.
- If multiple people need to access the site, we recommend using the
  [add users](https://support.google.com/webmasters/answer/7687615)
  functionality in Webmaster Tools. This makes it easier for you to maintain the access control
  list without having to modify files or settings on your servers.
- Also, if multiple people from your organization need to use Webmaster Tools, it can be a good
  policy to only allow users with email addresses from your domain. By doing that, you can verify
  at a glance that only users from your company have access. Additionally, when employees leave,
  access to Webmaster Tools is automatically taken care of when that account is disabled.
- Consider using
  [restricted](https://support.google.com/webmasters/answer/7687615)
  (read-only) access where possible. Settings generally don't need to be changed on a daily basis,
  and when they do need to be changed, it can be easier to document them if they have to go
  through a central account.

We hope these tips help you to simplify the situation around verification of your website in
Webmaster Tools. For more questions about verification, you can drop by our
[Webmaster Help Forums](https://support.google.com/webmasters/community).
