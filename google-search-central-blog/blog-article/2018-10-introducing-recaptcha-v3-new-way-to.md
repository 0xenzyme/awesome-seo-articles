---
title: "Introducing reCAPTCHA v3: the new way to stop bots"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2018-10-introducing-recaptcha-v3-new-way-to"
url: "https://developers.google.com/search/blog/2018/10/introducing-recaptcha-v3-new-way-to"
canonical: "https://developers.google.com/search/blog/2018/10/introducing-recaptcha-v3-new-way-to"
author: "Wei Liu, Google Product Manager"
published: "2018-10-29T00:00:00+00:00"
updated: "2018-10-29T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2018_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:33:05+00:00"
status_code: 200
html_hash: "7e641fd89024eeb124c63c222f6fcadea8150451576da6b9dddab0b9f5f8e930"
clean_word_count: 640
clean_char_count: 3910
---
# Introducing reCAPTCHA v3: the new way to stop bots

Today, we're excited to introduce reCAPTCHA v3, our newest API that helps you detect abusive
traffic on your website without user interaction. Instead of showing a CAPTCHA challenge,
[reCAPTCHA v3](/recaptcha/docs/v3)
returns a score so you can choose the most appropriate action for your website.

## A Frictionless User Experience

Over the last decade, reCAPTCHA has continuously evolved its technology. In reCAPTCHA v1, every
user was asked to pass a challenge by reading distorted text and typing into a box. To improve
both user experience and security, we introduced reCAPTCHA v2 and began to use many other signals
to determine whether a request came from a human or bot. This enabled reCAPTCHA challenges to move
from a dominant to a secondary role in detecting abuse, letting about half of users pass with a
single click. Now with reCAPTCHA v3, we are fundamentally changing how sites can test for human
vs. bot activities by returning a score to tell you how suspicious an interaction is and
eliminating the need to interrupt users with challenges at all. reCAPTCHA v3 runs adaptive risk
analysis in the background to alert you of suspicious traffic while letting your human users enjoy
a frictionless experience on your site.

## More Accurate Bot Detection with "Actions"

In reCAPTCHA v3, we are introducing a new concept called "Action"—a tag that you can use to define
the key steps of your user journey and enable reCAPTCHA to run its risk analysis in context. Since
reCAPTCHA v3 doesn't interrupt users, we recommend adding reCAPTCHA v3 to multiple pages. In this
way, the reCAPTCHA adaptive risk analysis engine can identify the pattern of attackers more
accurately by looking at the activities across different pages on your website. In the reCAPTCHA
admin console, you can get a full overview of reCAPTCHA score distribution and a breakdown for the
stats of the top 10 actions on your site, to help you identify which exact pages are being
targeted by bots and how suspicious the traffic was on those pages.

![a chart showing risk score distributions in the reCAPTCHA admin console](/static/search/blog/images/import/886a34c30f8f64bc1f493d3918c9df72.png)
![a chart showing per-page risk score distributions in the reCAPTCHA admin console](/static/search/blog/images/import/7dddb2c376278799cbe5c347654f26c3.png)

## Fighting Bots Your Way

Another big benefit that you'll get from reCAPTCHA v3 is the flexibility to prevent spam and
abuse in the way that best fits your website. Previously, the reCAPTCHA system mostly decided
when and what CAPTCHAs to serve to users, leaving you with limited influence over your website's
user experience. Now, reCAPTCHA v3 will provide you with a score that tells you how suspicious
an interaction is. There are three potential ways you can use the score. First, you can set a
threshold that determines when a user is let through or when further verification needs to be
done, for example, using two-factor authentication and phone verification. Second, you can
combine the score with your own signals that reCAPTCHA can't access—such as user profiles or
transaction histories. Third, you can use the reCAPTCHA score as one of the signals to train
your machine learning model to fight abuse. By providing you with these new ways to customize
the actions that occur for different types of traffic, this new version lets you protect your
site against bots and improve your user experience based on your website's specific needs.

In short, reCAPTCHA v3 helps to protect your sites without user friction and gives you more power
to decide what to do in risky situations. As always, we are working every day to stay ahead of
attackers and keep the Internet easy and safe to use (except for bots).

Ready to get started with reCAPTCHA v3? Visit our
[developer site](/recaptcha/docs/v3)
for more details.
