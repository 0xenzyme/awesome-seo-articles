---
title: "Message Center warnings for hackable sites"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2008-10-message-center-warnings-for-hackable"
url: "https://developers.google.com/search/blog/2008/10/message-center-warnings-for-hackable"
canonical: "https://developers.google.com/search/blog/2008/10/message-center-warnings-for-hackable"
author: "Matt Cutts"
published: "2008-10-16T00:00:00+00:00"
updated: "2008-10-16T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T12:55:09+00:00"
status_code: 200
html_hash: "b0888cc20a832dc2200d497579ac8b41a3bd324fb63103d16701f25cc06cfc53"
clean_word_count: 327
clean_char_count: 1939
---
# Message Center warnings for hackable sites

Recently we've seen more websites get hacked because of various security holes. In order to help
webmasters with this issue, we plan to run a test that will alert some webmasters if their content
management system (CMS) or publishing platform looks like it might have a security hole or be
hackable. This is a test, so we're starting out by alerting five to six thousand webmasters. We
will be leaving messages for owners of potentially vulnerable sites in the Google
[Message Center](/search/blog/2007/07/message-center-let-us-communicate-with)
that we provide as a service as part of
[Webmaster Tools](https://search.google.com/search-console).
If you manage a website but haven't signed up for Webmaster Tools, don't worry. The messages will
be saved and if you sign up later on, you'll still be able to
[access any messages that Google has left for your site](/search/blog/2008/03/webmaster-tools-keeps-your-messages).

One of the most popular pieces of software on the web is
[WordPress](https://www.wordpress.org/),
so we're starting our test with a specific version (2.1.1) that is known to be vulnerable to
exploits. If the test goes well, we may expand these messages to include other types of software
on the web. The message that a webmaster will see in their Message Center if they run
WordPress 2.1.1 will look like this:

![webmaster tools message center](/static/search/blog/images/import/0332fa783af67dda017d12ab8179b93a.png)

Quick note from Matt: In general, it's a good idea to make sure that your webserver's software is
up-to-date. For example, the current version of WordPress is 2.6.2; not only is that version more
secure than previous versions, but it will also alert you when a new version of WordPress is
available for downloading. If you run an older version of WordPress, I highly encourage you to
[upgrade to the latest version](https://wordpress.org/download/).
