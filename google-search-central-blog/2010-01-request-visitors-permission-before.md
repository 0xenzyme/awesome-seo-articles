---
title: "Request visitors' permission before installing software"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2010-01-request-visitors-permission-before"
url: "https://developers.google.com/search/blog/2010/01/request-visitors-permission-before"
canonical: "https://developers.google.com/search/blog/2010/01/request-visitors-permission-before"
author: "Jonathan Simon"
published: "2010-01-29T00:00:00+00:00"
updated: "2010-01-29T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:04:22+00:00"
status_code: 200
html_hash: "bf4a549d8ab592e21b6f6cf0ae391eb2e85d73274a86bf7db1297a630678ed4b"
clean_word_count: 392
clean_char_count: 2579
---
# Request visitors' permission before installing software

*Cross-posted on the
[Google Korea Blog](https://googlekoreablog.blogspot.com/2010/01/blog-post_15)*

Legitimate websites may require that their visitors install software. These sites often do so to
provide their users with additional functionality beyond what's available in standard web
browsers, like viewing a special type of document. Please note, however, that if your site
requires specific software for your visitors, the implementation of this software installation
process is very important. Incorrect implementation can appear as though you're installing
[malware](/search/docs/monitor-debug/security/malware), triggering our malware detection
filters, and resulting in your site being labeled with a 'This site may harm your computer'
[malware warning](/search/blog/2008/10/malware-we-dont-need-no-stinking)
in our search results.

If using your site requires a special software install, you need to first inform visitors why
they need to install additional software. Here are two bad examples and one good example of how
to handle the situation of a new visitor to such a site:

**Bad**: Install the required software without giving the visitor a chance to choose whether or
not they want to install the software.

**Bad**: Pop up a confirmation dialog box that prompts the visitor to agree to install the
software, without providing enough detail for the visitor to make an informed choice. (This
includes the standard ActiveX control installation dialog box, since it doesn't contain enough
meaningful information for a visitor to make an informed decision about that particular piece of
software.)

**Good**: Redirect the new visitor to an information page which provides thorough details on
why a special software installation is required to use the site. From this page the visitor can
initiate the installation of the required software if they decide to proceed with installation.

Has your site been labeled with a malware warning in our search results due to a poorly
implemented software installation requirement? Updating the installation process to ensure that
visitors are fully informed on why the installation is necessary, and giving them a chance to opt
out, should resolve this issue. Once you've got this in place, you can go to
[Webmaster Tools](https://search.google.com/search-console)
and request a
[malware review](/search/blog/2007/08/malware-reviews-via-webmaster-tools)
to expedite the process of removing any malware warnings associated with your site in Google's
search results.
