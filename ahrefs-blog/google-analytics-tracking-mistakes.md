---
title: "13 Google Analytics Tracking Mistakes (and How to Fix Them)"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "google-analytics-tracking-mistakes"
url: "https://ahrefs.com/blog/google-analytics-tracking-mistakes/"
canonical: "https://ahrefs.com/blog/google-analytics-tracking-mistakes/"
author: "Michal Pecánek"
published: "2020-03-04T00:02:22+00:00"
updated: "2025-07-21T15:15:56+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "time_sensitive_title"
fetched_at: "2026-06-12T11:33:29+00:00"
status_code: 200
html_hash: "ac44fead6c179777ad81867527b01b60c9b93b4e871e2633a64e33e44602e9a2"
clean_word_count: 2384
clean_char_count: 14875
---
# 13 Google Analytics Tracking Mistakes (and How to Fix Them)

If you saw this traffic drop in your Google Analytics account…

…then you’d probably want to prioritize [improving SEO](https://ahrefs.com/blog/how-to-improve-seo/) for that page.

But what if this data is flawed?

There’s a high risk of making bad decisions if you’re blindly relying on the data that you see in Google Analytics. You know the saying: garbage in, garbage out.

This guide will help you minimize data skewing factors by fixing these mistakes:

1. [Missing or duplicate Google Analytics code](#missing-duplicate-ga-codes)
2. [Incorrectly set up interaction events](#incorrect-interaction-event-setup)
3. [Tracking hits from other domains](#tracking-hits-from-other-domains)
4. [Tracking your own sessions](#tracking-your-own-sessions)
5. [Not using bot filtering](#not-filtering-bots)
6. [Tracking spam referrals](#tracking-spam-referrals)
7. [Sloppy use of UTM parameters](#sloppy-utm-parameters)
8. [Not excluding query parameters](#not-excluding-url-parameters)
9. [Not merging the same sources and mediums](#not-merging-sources-and-mediums)
10. [Not using a referral exclusion list](#not-using-a-referral-exclusion-list)
11. [Tracking Personally Identifiable Information (PII)](#tracking-pii)
12. [Not firing page views for Single Page Applications (SPAs)](#not-firing-pageviews-for-spa)
13. [Not having backup and testing views](#not-having-backup-views)

Out now: Ahrefs Web Analytics

Ahrefs [Web Analytics](https://ahrefs.com/web-analytics) is a simple Google Analytics alternative. Fast, privacy-friendly, and free for up to 1 million events per month per site.

[Learn more](https://ahrefs.com/web-analytics)

## 1. Missing or duplicate Google Analytics code

This sounds trivial, but it’s a common problem—especially on sites that use more than one CMS.

The good news is that Google Analytics has missing code [notifications built-in](https://support.google.com/analytics/answer/7030884?hl=en). The bad news is that it’s slow, and may take weeks to alert you about pages with missing code. It also doesn’t tell you about duplicate codes, which is another common problem.

For that reason, it’s best not to rely on Google’s notifications and instead crawl your site for errors with a tool that allows custom extraction.

Here’s how to set up a crawl with custom extraction in Screaming Frog to scrape both Google Tag Manager and Google Analytics codes:

It’s best to export the crawl to inspect the data. You can easily filter missing codes or see duplicates if there are more columns in the report, e.g., Find GTM code 1 and Find GTM code 2.

## 2. Incorrectly set up interaction events

Having things like purchases, form submissions, or video plays set up as interaction events makes sense. They’re important for your business, so the fact that they’re not counted as bounces—even when the visitor only views one page—is fine.

But if you’re using interaction events for tracking events that fire automatically on each page, like scroll depth tracking, that’ll result in close-to-zero bounce rates across your whole website—which isn’t good.

You can easily spot these issues by looking for unrealistically low [bounce rates in GA](https://ahrefs.com/blog/bounce-rate/).

If you suspect interaction events as the culprit, change the event’s “Non-interaction hit” setting from false to true in Google Tag Manager.

If you’re not using Google Tag Manager, just add [one more line of code](https://developers.google.com/analytics/devguides/collection/analyticsjs/events#non-interaction_events) to the GA event snippet.

## 3. Tracking hits from other domains

It’s surprisingly easy for someone to screw up your data if you don’t take preventive measures. Why? Because your GA/GTM tracking code is visible to anyone who opens your source code, so anyone can send hits to GA servers under your tracking code.

Luckily, it’s easy to prevent this from happening by setting up a view filter.

This will only include hits from your own (sub)domain:

Here’s the hostname regex filter pattern: `(^|\.)example\.com`

## 4. Tracking your own sessions

There are a lot of irregular actions we make on our websites, and we don’t want those reflected in our data.

So, while we’re setting up filters, let’s also make sure to exclude hits from internal IP addresses. It’s easy to do this for a single IP:

If you need to exclude more IPs, refer to [this guide from Google](https://support.google.com/analytics/answer/1034840?hl=en).

## 5. Not using bot filtering

Google can detect a fair portion of the spam/bot traffic coming to your website. All you need to do is to check a box.

You’ll find this in *Admin > View Settings*:

Note that it’s enough to check this only for your main analytics view. There’s no need to do this for the raw or testing views.

## 6. Tracking spam referrals

Popular websites attract spammy links. It’s just how things are.

Most of these are negligible and bring zero referral traffic, but some can send thousands of spammy referrals every day.

To check if that’s a problem for you, set the date range to three months minimum, then go to the Referrals report (*Acquisition > All Traffic > Referrals).*

Look for shady domains with a high number of referrals.

Don’t click suspicious domains as they might contain malware or spyware. Instead, create a list and exclude them with a filter (*Admin > Filter*). Set the Filter Field as “Campaign Source,” then list domains in the Filter Pattern field separated by a pipe (|) symbol.

**IMPORTANT**. Always remember to verify your filters to see how it influences your data. There’s a button below the filters for this.

## 7. Sloppy use of UTM parameters

UTM parameters are tags that are appended to URLs to label different traffic sources. They’re mostly used with paid ads and links that would otherwise get mixed with organic visits.

Let’s say that we’re running ads on Twitter. By default, the traffic would fall under “twitter.com / referral”, making any performance analysis impossible. So we append UTM parameters to URLs used for Twitter Ads:

These UTM parameters are then sent to GA servers and used in their respective dimensions.

are you part of a marketing team?

If there are multiple people handing the performance marketing side of things, you need to have guidelines for UTM parameters unification. Trust me, analyzing performance of marketing channels when the tagging is not unified is one of the things that you really don’t want to be doing in Google Analytics.

When doing this, keep in mind that the process of adding UTM parameters depends on the advertising platform. For example, Twitter Ads require URLs that already have the parameters in them, whereas Google Ads can (and should) be completely automatized.

## 8. Not excluding query parameters

Cluttering your (Landing) Page dimensions with [parameterized URLs](https://ahrefs.com/blog/url-parameters/) can be a nightmare for any further analyses. It breaks up the same URL into multiple rows, which leads to splintered metrics.

To solve this, use the report filter to show all parameterized URLs recorded in your GA view.

Then, to keep the page dimensions unified, exclude [parameters](https://ahrefs.com/blog/url-parameters/) that you don’t want to see in your reports.

You can do it in *View Settings*:

Just make sure not to exclude:

- Search query parameters (otherwise it’ll block your [internal site search data](https://ahrefs.com/blog/google-analytics-for-seo/#find-keyword-opportunities-from-site-search))
- UTM parameters (GA can already handle them properly)
- Parameters you want to track separately (e.g., those for different products on ecommerce sites)

If you’re dealing with a vast number of different parameters that you want to exclude, it’s better to use view filters instead. Their flexibility and the option to use regular expressions make them a better solution. Follow [this guide](https://www.bounteous.com/insights/2015/04/17/strip-query-parameters-google-analytics/) to set them up.

## 9. Not merging the same sources and mediums

You might have noticed that some of your traffic sources and mediums are a mess because they’re basically the same thing. The most common example is referral traffic from Facebook.

Those weird subdomains are called link shim referrals. Facebook uses them for security and privacy reasons, but they can make analyzing the performance of a particular source/medium difficult.

To fix them, use filters. Here’s one that merges referral traffic from Facebook:

Remember to verify the filter to check that it does what you think it does.

You should also create a note that you’ve merged the traffic so others won’t wonder what caused the change. Google Analytics doesn’t apply the filters retroactively, so you’ll still have to deal with the old data.

## 10. Not using a referral exclusion list

When you add a domain to a referral exclusion list, any traffic from it will no longer be labeled as referral traffic, and will not trigger a new session.

This is especially useful in three cases:

- **Payment gateways.** If you use any third-party payment processors, you’ll likely be redirecting your customers there and back after finishing the payment. That should be one session under one source of traffic.
- **Subdomain tracking.** Subdomains are separate hostnames, and traffic from them would naturally trigger a new referral session. Luckily, GA submits your own domain into the list when creating the property. Leave it there. And keep the default “Cookie Domain: Auto” as well if you ever encounter that in the tracking code or GTM.
- **[Cross-domain tracking](https://www.analyticsmania.com/post/google-analytics-cross-domain-tracking-with-google-tag-manager/).** You may have microsites and other separate domains for which you may want merged data if it’s the same business.

You’ll find this list in *Admin > Property column > Tracking Info > Referral Exclusion List.*

Enter the domains in the *example.com* format to cover all the subdomains.

## 11. Tracking Personally Identifiable Information (PII)

While this doesn’t harm your data clarity, it can cause some serious damage to your business.

You need to [make sure that you’re not tracking any PII](https://support.google.com/analytics/answer/6366371?hl=en) like emails, phone numbers, or names. Or even better—adhere to the data protection and privacy regulations that apply to your business.

Unfortunately, you may be tracking PII without knowing it by generating URL parameters with personal information in forms or elsewhere.

This probably won’t be the case if you’re using a popular CMS, but you should [definitely check this](https://www.getelevar.com/guides/google-analytics/how-to-find-and-fix-pii-in-google-analytics-data/) if you have a completely custom website.

Just to state the obvious, don’t try collecting PII through custom dimensions. And if you want to check what data websites are collecting, use a browser extension like [dataslayer](https://chrome.google.com/webstore/detail/dataslayer/ikbablmmjldhamhcldjjigniffkkjgpo) or [WASP](https://chrome.google.com/webstore/detail/waspinspector-analytics-s/niaoghengfohplclhbjnjheodgkejpih?hl=en).

## 12. Not firing pageviews for Single Page Applications (SPA)

Is your website a Single Page Application (SPA)? In other words, is it using JavaScript to generate page content dynamically?

If the answer is yes, then tracking just got a bit more tricky for you.

SPAs load everything needed with the first pageview and update the content and URLs dynamically. That means GA won’t track any subsequent pageviews because there are naturally no subsequent hits to their servers.

(I’m guilty of overlooking this when developers were gradually switching a project I was working on to the React framework.)

To fix this, you’ll need to use workarounds that will most likely require help from developers or GTM experts. If you want to learn more about this, check out Google’s [official documentation](https://developers.google.com/analytics/devguides/collection/analyticsjs/single-page-applications) and [this thorough guide](https://www.analyticsmania.com/post/single-page-web-app-with-google-tag-manager/).

## 13. Not having backup and testing views

This last one’s not so much a tracking mistake but rather a best practice for handling data in Google Analytics.

Even if you have just one account and property, always make sure to have at least three different [views](https://support.google.com/analytics/answer/2649553?hl=en):

1. **Master view**. You’ll use this one the most with all the desired settings and filters applied.
2. **Backup view**. A view left with all settings on default. If anything goes wrong with your master view, you’ll always have all the raw data here.
3. **Testing view.** You can play around with this one to test the waters first. It’s useful if you’re not sure about the implications of tweaking more complex view settings, such as various filters.

You can rename views in *Admin > View Settings > View Name.*

Just remember to make the view names as self-explanatory as possible so that others using the account understand them.

## Final thoughts

Test, verify, repeat.

Whenever you make changes to your GA settings, GTM, or tracking codes, you should take the role of a Quality Assurance engineer for a while.

That means you need to be comfortable working with the source code, cookies, and various debugging tools. I recommend using the following ones:

- [Google Tag Assistant](https://get.google.com/tagassistant/)
- [Google Analytics Debugger](https://chrome.google.com/webstore/detail/google-analytics-debugger/jnkmfdileelhofjcijamephohjechhna?hl=en)
- [dataslayer](https://chrome.google.com/webstore/detail/dataslayer/ikbablmmjldhamhcldjjigniffkkjgpo)
- [WASP](https://chrome.google.com/webstore/detail/waspinspector-analytics-s/niaoghengfohplclhbjnjheodgkejpih?hl=en)
- Real-time reports in GA to immediately see the effects of fired tags
- Debugging tools of any ad platforms that you use, e.g., [Facebook Pixel Helper](https://chrome.google.com/webstore/detail/facebook-pixel-helper/fdgfkebogiimcoedlicjlajpkdmockpc?hl=en)

Implementing, auditing, and debugging depends on the complexity of your tracking needs and code implementation. If you’re not using GTM yet, I’d strongly advise you to make the change unless your tracking needs are simple.

Yes, it will take quite a lot of time to [learn if you’re a beginner](https://analytics.google.com/analytics/academy/course/5). But the benefits are enormous. You won’t have to contact developers for tracking code changes, and it’s just awesome to have neatly organized containers, tags, triggers, and variables.

Did I mention to test and verify everything?

Ping me on [Twitter](https://twitter.com/michalpecanek) if you have any questions.
