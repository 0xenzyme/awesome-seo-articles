---
title: "Detect and get rid of unwanted sneaky mobile redirects"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2015-10-detect-and-get-rid-of-unwanted-sneaky"
url: "https://developers.google.com/search/blog/2015/10/detect-and-get-rid-of-unwanted-sneaky"
canonical: "https://developers.google.com/search/blog/2015/10/detect-and-get-rid-of-unwanted-sneaky"
author: "Written by Vincent Courson and Badr Salmi El Idrissi, Search Quality team"
published: "2015-10-29T00:00:00+00:00"
updated: "2015-10-29T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2015_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:27:40+00:00"
status_code: 200
html_hash: "b522c4413f52e979d6a0690969b69c72f3c04b63abf1b1ba1cfb2cad297de909"
clean_word_count: 1052
clean_char_count: 6826
---
# Detect and get rid of unwanted sneaky mobile redirects

In many cases, it is OK to show slightly different content on different devices. For example,
optimizing the smaller space of a smartphone screen can mean that some content, like images, will
have to be modified. Or you might want to
[store your website's menu in a navigation drawer](/web/fundamentals/layouts/navigation-patterns/navigationdrawer)
to make mobile browsing easier and more effective. When implemented properly, these user-centric
modifications can be understood very well by Google.

The situation is similar when it comes to mobile-only redirect. Redirecting mobile users to
improve their mobile experience (like redirecting mobile users from `example.com/url1`
to `m.example.com/url1`) is often beneficial to them. But redirecting mobile users
sneakily to a different content is bad for user experience and is against
[Google's webmaster guidelines](/search/docs/essentials).

![](/static/search/blog/images/import/2057121a350eba872eb7fd7fa3ad477e.png)

## Who implements these mobile-only sneaky redirects?

There are cases where webmasters knowingly decide to put into place redirection rules for their
mobile users. This is typically a webmaster guidelines violation, and we do take manual action
against it when it harms Google users' experience (see last section of this article).

But we've also observed situations where mobile-only sneaky redirects happen without site owners
being aware of it:

- **Advertising schemes that redirect mobile users specifically**
  A script/element installed to display ads and monetize content might be redirecting mobile
  users to a completely different site without the webmaster being aware of it.
- **Mobile redirect as a result of the site being a target of hacking**
  In other cases, if your website has been hacked, a potential result can be redirects to spammy
  domains for mobile users only.

## How do I detect if my site is doing sneaky mobile redirects?

1. **Check if you are redirected when you navigate to your site on your smartphone**
   We recommend you to check the mobile user experience of your site by visiting your pages from
   Google search results with a smartphone. When debugging, mobile emulation in desktop browsers is
   handy, mostly because you can test for many different devices. You can, for example, do it
   straight from your browser in
   [Chrome](https://developer.chrome.com/devtools/docs/device-mode),
   [Firefox](https://addons.mozilla.org/En-us/firefox/addon/user-agent-overrider/)
   or
   [Safari](https://developer.apple.com/library/mac/documentation/AppleApplications/Conceptual/Safari_Developer_Guide/TheDevelopMenu/TheDevelopMenu.html#//apple_ref/doc/uid/TP40007874-CH7-SW5)
   (for the latter, make sure you have enabled the "Show Develop menu in menu bar" feature).
2. **Listen to your users**
   Your users could see your site in a different way than you do. It's always important to pay
   attention to user complaints, so you can hear of any issue related to mobile UX.
3. **Monitor your users in your site's analytics data**
   Unusual mobile user activity could be detected by looking at some of the data held in your
   website's analytics data. For example, looking at the average time spent on your site by your
   mobile users could be a good signal to watch: if all of a sudden, your mobile users (and only
   them) start spending much less time on your site than they used to, there might be an issue
   related to mobile redirections.

   To be aware of wide changes in mobile user activity as soon as they happen, you can for
   example
   [set up Google Analytics alerts](https://support.google.com/analytics/answer/1033021h2&vid=1-635769760082728193-812820847#create).
   For example, you can set an alert to be warned in case of a sharp drop in average time spent
   on your site by mobile users, or a drop in mobile users (always take into account that big
   changes in those metrics are not a clear, direct signal that your site is doing mobile sneaky
   redirects).

   ![](/static/search/blog/images/import/a4bbbd96200cd27085b26433cd458366.png)

## I've detected sneaky redirects for my mobile users, and I did not set it up: what do I do?

1. **Make sure that your site is not hacked.**
   Check the
   [Security Issues tool](https://search.google.com/search-console/security-issues)
   in the Search Console, if we have noticed any hack, you should get some information there.

   Review our additional resources on
   [typical symptoms of hacked sites](/search/blog/2015/08/nohacked-identifying-and-diagnosing#Monitoring),
   and our
   [case studies on hacked sites](/search/blog/2015/02/case-studies-fixing-hacked-sites).
2. **Audit third-party scripts/elements on your site**
   If your site is not hacked, then we recommend you take the time to investigate if third-party
   scripts/elements are causing the redirects. You can follow these steps:

   1. Remove one by one the third-party scripts/elements you do not control from the redirecting
      page(s).
   2. Check your site on a mobile device or through emulation between each script/element removal,
      and see when the redirect stops.
   3. If you think a particular script/element is responsible for the sneaky redirect, consider
      removing it from your site, and debugging the issue with the script/element provider.

## Last Thoughts on Sneaky Mobile Redirects

It's a violation of the Google Webmaster Guidelines to redirect a user to a page with the intent
of displaying content other than what was made available to the search engine crawler (more
information on
[sneaky redirects](/search/docs/essentials/spam-policies#sneaky-redirects)). To ensure
quality search results for our users, the Google Search Quality team can take action on such
sites, including removal of URLs from our index. When we take manual action, we send a message to
the site owner via Search Console. Therefore, make sure you've
[set up a Search Console account](https://support.google.com/webmasters/answer/6001104).

Be sure to choose advertisers who are transparent on how they handle user traffic, to avoid
unknowingly redirecting your own users. If you are interested in trust-building in the online
advertising space, you may check out industry-wide best practices when participating in ad
networks. For example, the Trustworthy Accountability Group's (Interactive Advertising Bureau)
[Inventory Quality Guidelines](https://www.tagtoday.net/iqg/) are a
good place to start. There are many ways to monetize your content with mobile solutions that
provide a high quality user experience, be sure to use them.

If you have questions or comments about mobile-only redirects, join us in our
[Google Webmaster Support forum](https://support.google.com/webmasters/community/).
