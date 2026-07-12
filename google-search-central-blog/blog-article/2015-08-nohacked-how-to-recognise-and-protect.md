---
title: "#NoHacked: How to recognise and protect yourself against social engineering"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2015-08-nohacked-how-to-recognise-and-protect"
url: "https://developers.google.com/search/blog/2015/08/nohacked-how-to-recognise-and-protect"
canonical: "https://developers.google.com/search/blog/2015/08/nohacked-how-to-recognise-and-protect"
author: "Eric Kuan, Webmaster Relations Specialist and Yuan Niu, Webspam Analyst"
published: "2015-08-03T00:00:00+00:00"
updated: "2015-08-03T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2015_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:27:16+00:00"
status_code: 200
html_hash: "6b95a2e8ad78558c388169a519f00ed28036099febbd31dc12a6b35687e1675a"
clean_word_count: 707
clean_char_count: 4701
---
# #NoHacked: How to recognise and protect yourself against social engineering

Today in our #NoHacked campaign, we'll be talking about social engineering. Follow along with
discussions on [Twitter](https://twitter.com/googlesearchc) and
[Google+](https://google.com/+googlewebmasters)
using the #nohacked hashtag.
([Part 1](/search/blog/2015/07/nohacked-how-to-avoid-being-target-of))

![](/static/search/blog/images/import/0167b53951b3037de787974fd1e91f69.png)

If you've spent some time on the web, you have more than likely encountered some form of
[social engineering](https://en.wikipedia.org/wiki/Social_engineering_(security)).
Social engineering attempts to extract confidential information from you by manipulating or
tricking you in some way.

## Phishing

You might be familiar with phishing, one of the most common forms of social engineering. Phishing
sites and emails mimic legitimate sites and trick you into entering confidential information like
your username and password into these sites. A
[recent study from Google](https://research.google.com/pubs/pub43469.html)
found that some phishing sites can trick victims 45% of the time! Once a phishing site has your
information, the information will either be sold or be used to manipulate your accounts.

## Other Forms of Social Engineering

As a site owner, phishing isn't the only form of social engineering that you need to watch out
for. One other form of social engineering comes from the software and tools used on your site. If
you download or use any
[Content Management System](https://en.wikipedia.org/wiki/Content_management_system)
(CMS), plug-ins, or add-ons, make sure that they come from reputable sources like directly from
the developer's site. Software from non-reputable sites can contain malicious exploits that allow
hackers to gain access to your site.

For example, Webmaster Wanda was recently hired by Brandon's Pet Palace to help create a site.
After sketching some designs, Wanda starts compiling the software she needs to build the site.
However, she finds out that Photo Frame Beautifier, one of her favorite plug-ins, has been taken
off the official CMS plug-in site and that the developer has decided to stop supporting the
plug-in. She does a quick search and finds a site that offers an archive of old plug-ins. She
downloads the plug-in and uses it to finish the site. Two months later, a notification in Search
Console notifies Wanda that her client's site has been hacked. She quickly scrambles to fix the
hacked content and finds the source of the compromise. It turns out the Photo Frame Beautifier
plug-in was modified by a third party to allow malicious parties to access the site. She removed
the plug-in, fixed the hacked content, secured her site from future attacks, and filed a
reconsideration request in Search Console. As you can see, an inadvertent oversight by Wanda led
to her client's site being compromised.

## Protecting Yourself from Social Engineering Attacks

Social engineering is effective because it's not obvious that there's something wrong with what
you're doing. However, there are a few basic things you can do protect yourself from social
engineering.

- **Stay vigilant:** Whenever you enter confidential information online or install website
  software, have a healthy dose of skepticism. Check URLs to make sure you're not typing
  confidential information into malicious sites. When installing website software make sure the
  software is coming from known, reputable sources like the developer's site.
- **Use two-factor authentication:** Two-factor authentication like Google's
  [2-Step Verification](https://www.google.com/landing/2step/) adds
  another layer of security that helps protect your account even if your password has been stolen.
  You should use two-factor authentication on all accounts where possible. We'll be talking more
  in-depth next week about the benefits of two-factor authentication.

Additional resources about social engineering:

- Learn more about
  [how to protect yourself from phishing attacks](https://support.google.com/accounts/answer/75061)
- [Report a Phishing Page](https://www.google.com/safebrowsing/report_phish/)
- [Avoid and report Google scams](https://support.google.com/faqs/answer/2952493)
- [Identify "phishing" and "spoofing" emails](https://support.google.com/wallet/answer/105822)

If you have any additional questions, you can post in the
[Webmaster Help Forums](https://support.google.com/webmasters/go/community)
where a community of webmasters can help answer your questions. You can also join our
[Hangout on Air about Security](https://plus.google.com/events/csqjnqe8vl28qbn526makjecobc)
on August 26.
