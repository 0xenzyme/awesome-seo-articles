---
title: "New software version' notifications for your site"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2009-11-new-software-version-notifications-for"
url: "https://developers.google.com/search/blog/2009/11/new-software-version-notifications-for"
canonical: "https://developers.google.com/search/blog/2009/11/new-software-version-notifications-for"
author: "Patrick Chapman, Search Quality Team"
published: "2009-11-20T00:00:00+00:00"
updated: "2009-11-20T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:02:29+00:00"
status_code: 200
html_hash: "057ae28b1ce64b2211b39cc717fb6283e9ff733f461febb02fcb99438cdd7ee4"
clean_word_count: 522
clean_char_count: 3094
---
# New software version' notifications for your site

One of the great things about working at Google is that we get to take advantage of an enormous
amount of computing power to do some really cool things. One idea we tried out was to let
webmasters know about their
[potentially hackable websites](/search/blog/2008/10/message-center-warnings-for-hackable).
The initial effort was successful enough that we thought we would take it one step further by
expanding our efforts to cover other types of web applications—for example, more content
management systems (CMSs), forum/bulletin-board applications, stat-trackers, and so on.

This time, however, our goal is not just to isolate vulnerable or hackable software packages, but
to also notify webmasters about newer versions of the software packages or plugins they're running
on their website. For example, there might be a
[Drupal](https://drupal.org/)
[module](https://drupal.org/project/modules)
or
[Joomla](https://www.joomla.org/)
[extension](https://extensions.joomla.org/)
update available but some folks might not have upgraded. There are a few reasons a webmaster might
not upgrade to the newer version and one of the reasons could be that they just don't know a new
version exists. This is where we think we can help. We hope to let webmasters know about new
versions of their software by sending them a message via
[Webmaster Tools](https://search.google.com/search-console).
This way they can make an informed decision about whether or not they would like to upgrade.

One of the ways we identify sites to notify is by parsing source code of web pages that we crawl.
For example, WordPress and other CMS applications include a generator `meta` tag that specifies the
version number. This has proven to be tremendously helpful in our efforts to notify webmasters.
So if you're a software developer, and would like us to help you notify your users about newer
versions of your software, a great way to start would be to include a generator `meta` tag that
tells the version number of your software. If you're a plugin or a widget developer, including a
version number in the source you provide to your users is a great way to help too.

We've seen divided opinions over time about whether it's a good security practice to include a
version number in source code, because it lets hackers or worm writers know that the website
might be vulnerable to a particular type of exploit. But as
[Matt Mullenweg pointed out](https://wordpress.org/development/2009/09/keep-wordpress-secure/),
"Where [a worm writer's] 1.0 might have checked for version numbers, 2.0 just tests [a website's]
capabilities...". Meanwhile, the advantage of a version number is that it can help alert site
owners when they need to update their site. In the end, we tend to think that including a version
number can do more good than harm.

We plan to begin sending out the first of these messages soon and hope that webmasters find them
useful! If you have any questions or feedback, you can post in our
[forum](https://support.google.com/webmasters/go/community).
