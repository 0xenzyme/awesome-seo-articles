---
title: "Spam2.0: Fake user accounts and spam profiles"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2009-06-spam20-fake-user-accounts-and-spam"
url: "https://developers.google.com/search/blog/2009/06/spam20-fake-user-accounts-and-spam"
canonical: "https://developers.google.com/search/blog/2009/06/spam20-fake-user-accounts-and-spam"
author: "Written by Jason Morrison, Search Quality Team"
published: "2009-06-26T00:00:00+00:00"
updated: "2009-06-26T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:58:50+00:00"
status_code: 200
html_hash: "7fd6c0be3529579fe9d5727e75f255e3468373ef5853ce1b20c56b0f20aa6157"
clean_word_count: 1386
clean_char_count: 8484
---
# Spam2.0: Fake user accounts and spam profiles

You're a good webmaster or web developer, and you've done everything you can
[to keep your site from being hacked](/search/blog/2009/02/best-practices-against-hacking)
and
[keep spam out of your forums and comment sections](/search/blog/2008/09/keeping-comment-spam-off-your-site-and).
You're now the proud owner of a buzzing web2.0 social community, filling the web with
user-generated content, and probably getting lots of visitors from Google and other search
engines.

Many of your site's visitors will create user profiles, and some will spend hours posting in
forums, joining groups, and getting the sparkles exactly right on the rainbow-and-unicorn image
for their
[BFF](https://www.google.com/search?q=define:bff)'s
birthday. This is all great.

Others, however, will create accounts and fill their profiles with gibberish, blatherskite and
palaver. Even worse, they'll add a sneaky link, a bit of redirecting JavaScript code, or a big
fake embedded video that takes your users off to the seediest corners of the web.

Welcome to the world of spam profiles. The social web is growing incredibly quickly and spammers
look at every kind of user content on the web as an opportunity for traffic. I've spoken with a
number of experienced webmasters who were surprised to find out this was even a problem, so I
thought I would talk a little bit about spam profiles and what you might do to find and clean
them out of your site.

## Why is this important?

Imagine the following scenario:

> "Hello there, welcome to our new web2.0 social networking site. Boy, have I got a new friend for
> you. His name is Mr. BuyMaleEnhancementRingtonesNow, and he'd love
> for you to check out his profile. He's a NaN-year-old from
> Pharmadelphia, PA and you can check out his exciting home page at
> https://example.com/obviousflimflam.
>
> Not interested? Then let me introduce you to my dear friend
> PrettyGirlsWebCam1234, she says she's an old college friend of
> yours and has exciting photos and videos you might want to see."

You probably don't want your visitors' first impression of your site to include inappropriate
images or bogus business offers. You definitely don't want your users hounded by fake invites
to the point where they stop visiting altogether. If your site becomes filled with spammy
content and links to bad parts of the web, search engines may lose trust in your otherwise
fine site.

## Why would anyone create spam profiles?

Spammers create fake profiles for a number of nefarious purposes. Sometimes they're just a way
to reach users internally on a social networking site. This is somewhat similar to the way email
spam works - the point is to send your users messages or friend invites and trick them into
following a link, making a purchase, or downloading malware by sending a fake or low-quality
proposition.

Spammers are also using spam profiles as yet another avenue to generate webspam on otherwise
good domains. They scour the web for opportunities to get their links, redirects, and malware
to users. They use your site because it's no cost to them and they hope to piggyback off your
good reputation.

The latter case is becoming more and more common. Some fake profiles are obvious, using popular
pharmaceuticals as the profile name, for example; but we've noticed an increase in savvier
spammers that try to use real names and realistic data to sneak in their bad links. To make sure
their newly-minted gibberish profile shows up in searches they will also generate links on
hacked sites, comment spam, and yes, other spam profiles. This results in a lot of bad content
on your domain, unwanted incoming links from spam sites, and annoyed users.

## Which sites are being abused?

You may be thinking to yourself, "But my site isn't a huge social networking juggernaut; surely
I don't need to worry." Unfortunately, we see spam profiles on everything from the largest social
networking sites to the smallest forums and bulletin boards. Many popular bulletin boards and
content management systems (CMS) such as vBulletin, phpBB, Moodle, Joomla, etc. generate member
pages for every user that creates an account. In general CMSs are great because they make it easy
for you to deploy content and interactive features to your site, but auto-generated pages can be
abused if you're not aware.

For all of you out there who do work for huge social networking juggernauts, your site is a target
as well. Spammers want access to your large userbase, hoping that users on social sites will be
more trusting of incoming friend requests, leading to larger success rates.

## What can you do?

This isn't an easy problem to solve - the bad guys are attacking a wide range of sites and seem to
be able to adapt their scripts to get around countermeasures. Google is constantly under attack
by spammers trying to create fake accounts and generate spam profiles on our sites, and despite
all of our efforts some have managed to slip through. Here are some things you can do to make
their lives more difficult and keep your site clean and useful:

- **Make sure you have standard security features in place**, including
  [CAPTCHAs](https://en.wikipedia.org/wiki/Captcha),
  to make it harder for spammers to create accounts en masse. Watch out for unlikely behavior -
  thousands of new user accounts created from the same IP address, new users sending out
  thousands of friend requests, etc. There is no simple solution to this problem, but often
  some simple checks will catch most of the worst spam.
- **Use a blocklist to prevent repetitive spamming attempts**. We often see large numbers of
  fake profiles on one innocent site all linking to the same domain, so once you find one, you
  should make it simple to remove all of them.
- **Watch out for
  [cross-site scripting (XSS) vulnerabilities](/search/blog/2007/09/quick-security-checklist-for-webmasters)** and other security holes that allow spammers to inject questionable code onto their
  profile pages. We've seen techniques such as JavaScript used to redirect users to other sites,
  iframes that attempt to give users malware, and custom CSS code used to cover over your page
  with spammy content.
- **Consider
  [adding `rel="nofollow"` to the links](/search/docs/advanced/guidelines/qualify-outbound-links)
  on untrusted user profile pages.** This makes your site less attractive to anyone trying to
  pass PageRank from your site to their spammy site. Spammers seem to go after the low-hanging
  fruit, so even just nofollowing new profiles with few signals of trustworthiness will go a long
  way toward mitigating the problem. On the flip side, you could also consider manually or
  automatically lifting the nofollow attribute on links created by community members that are
  likely more trustworthy, such as those who have contributed substantive content over time.
- **Consider
  [a `noindex` robots `meta` tag to profile pages](/search/docs/crawling-indexing/control-what-you-share)** for new, not yet trustworthy users. You may even want to make initial profile pages
  completely private, especially if the bulk of the content on your site is in blogs, forums,
  or other types of pages.
- **Add a "report spam" feature to user profiles and friend invitations**. Let your users help
  you solve the problem - they care about your community and are annoyed by spam too.
- **Monitor your site for spammy pages**. One of the best tools for this is
  [Google Alerts](https://www.google.com/alerts) - set up a
  `site:` query along with commercial or adult keywords that you wouldn't expect to
  see on your site. This is also a great tool
  [to help detect hacked pages](/search/blog/2009/02/best-practices-against-hacking).
  You can also
  [check 'Keywords' data in Webmaster Tools](https://www.google.com/support/webmasters/bin/answer.py?answer=35255)
  for strange, volatile vocabulary.
- **Watch for spikes in traffic from suspicious queries**. It's always great to see the line
  on your pageviews chart head upward, but pay attention to commercial or adult queries that
  don't fit your site's content. In cases like this where a spammer has abused your site, that
  traffic will provide little if any benefit while introducing users to your site as "the place
  that redirected me to that virus."

If you have any questions, you can always ask in our
 [Webmaster Help Forum](https://support.google.com/webmasters/community).
