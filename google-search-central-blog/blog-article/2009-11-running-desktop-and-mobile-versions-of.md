---
title: "Running desktop and mobile versions of your site"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2009-11-running-desktop-and-mobile-versions-of"
url: "https://developers.google.com/search/blog/2009/11/running-desktop-and-mobile-versions-of"
canonical: "https://developers.google.com/search/blog/2009/11/running-desktop-and-mobile-versions-of"
author: "Jun Mukai, Software Engineer, Mobile Search Team"
published: "2009-11-19T00:00:00+00:00"
updated: "2009-11-19T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:02:35+00:00"
status_code: 200
html_hash: "5a9fd085d40687af24ddc238f74092f99b77910e14a918a9716b5e648a97a43b"
clean_word_count: 837
clean_char_count: 5157
---
# Running desktop and mobile versions of your site

*This post was largely translated from our
[Japanese version of the Webmaster Central Blog](/search/blog/2009/11/running-desktop-and-mobile-versions-of?hl=ja)*

Recently I introduced several methods to
[ensure your mobile site is properly indexed by Google](/search/blog/2009/11/help-google-index-your-mobile-site).
Today I'd like to share information useful for webmasters who manage both desktop and mobile phone
versions of a site.

One of the most common problems for webmasters who run both mobile and desktop versions of a site
is that the mobile version of the site appears for users on a desktop computer, or that the
desktop version of the site appears when someone finds them from a mobile device. In dealing
with this scenario, here are two viable options:

## Redirect mobile users to the correct version

When a mobile user or crawler (like Googlebot-Mobile) accesses the desktop version of a URL, you
can redirect them to the corresponding mobile version of the same page. Google notices the
relationship between the two versions of the URL and displays the standard version for searches
from desktops and the mobile version for mobile searches.

If you redirect users, please make sure that the content on the corresponding mobile/desktop URL
matches as closely as possible. For example, if you run a shopping site and there's an access
from a mobile phone to a desktop-version URL, make sure that the user is redirected to the mobile
version of the page for the same product, and not to the home page of the mobile version of the
site. We occasionally find sites using this kind of redirect in an attempt to boost their search
rankings, but this practice only results in a negative user experience, and so should be avoided
at all costs.

On the other hand, when there's an access to a mobile-version URL from a desktop browser or by our
web crawler, Googlebot, it's not necessary to redirect them to the desktop-version. For instance,
[Google](https://www.google.com/m/)
doesn't automatically redirect desktop users from their mobile site to their desktop site,
instead they include a link on the mobile-version page to the desktop version. These links are
especially helpful when a mobile site doesn't provide the full functionality of the desktop
version—users can easily navigate to the desktop-version if they prefer.

## Switch content based on User-agent

Some sites have the same URL for both desktop and mobile content, but change their format
according to `User-agent`. In other words, both mobile users and desktop users access
the same URL (that is, no redirects), but the content/format changes slightly according to the
`User-agent`. In this case, the same URL will appear for both mobile search and desktop
search, and desktop users can see a desktop version of the content while mobile users can see a
mobile version of the content.

However, note that if you fail to configure your site correctly, your site could be considered to
be cloaking, which can lead to your site disappearing from our search results.
[Cloaking](/search/docs/essentials/spam-policies#cloaking)
refers to an attempt to boost search result rankings by serving different content to Googlebot
than to regular users. This causes problems such as less relevant results (pages appear in search
results even though their content is actually unrelated to what users see/want), so we take
cloaking very seriously.

So what does "the page that the user sees" mean if you provide both versions with a URL? As I
mentioned in the
[previous post](/search/blog/2009/11/help-google-index-your-mobile-site),
Google uses `Googlebot` for web search and `Googlebot-Mobile` for mobile
search. To remain within our guidelines, you should serve the same content to Googlebot as a
typical desktop user would see, and the same content to Googlebot-Mobile as you would to the
browser on a typical mobile device. It's fine if the contents for Googlebot are different from
the one for Googlebot-Mobile.

One example of how you could be unintentionally detected for cloaking is if your site returns a
message like "Please access from mobile phones" to desktop browsers, but then returns a full
mobile version to both crawlers (so Googlebot receives the mobile version). In this case, the
page which web search users see (for example, "Please access from mobile phones") is different
from the page which Googlebot crawls (for example, "Welcome to my site"). Again, we detect
cloaking because we want to serve users the same relevant content that Googlebot or
Googlebot-Mobile crawled.

![Diagram of serving content from your mobile-enabled site](/static/search/blog/images/import/94cfa65cebf29a526da616177dc63108.png)

We're working on a daily basis to improve search results and solve problems, but because the
relationship between PC and mobile versions of a web site can be nuanced, we appreciate the
cooperation of webmasters. Your help will result in more mobile content being indexed by Google,
improving the search results provided to users. Thank you for your cooperation in improving the
mobile search user experience.
