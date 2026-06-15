---
title: "Keeping comment spam off your site and away from users"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-09-keeping-comment-spam-off-your-site-and"
url: "https://developers.google.com/search/blog/2008/09/keeping-comment-spam-off-your-site-and"
canonical: "https://developers.google.com/search/blog/2008/09/keeping-comment-spam-off-your-site-and"
author: "Jason Morrison, Search Quality Team"
published: "2008-09-26T00:00:00+00:00"
updated: "2008-09-26T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:54:17+00:00"
status_code: 200
html_hash: "5d8a3fe8ee972452ff02fa2a831405344a0dc5a3f0ff0d340389404e535c614b"
clean_word_count: 1043
clean_char_count: 6316
---
# Keeping comment spam off your site and away from users

So, you've set up a forum on your site for the first time, or enabled comments on your blog. You
carefully craft a post or two, click the submit button, and wait with bated breath for comments
to come in.

And they do come in. Perhaps you get a friendly note from a fellow blogger, a pressing update from
an MMORPG guild member, or a reminder from your Aunt Millie about dinner on Thursday. But then you
get something else. Something... disturbing. Offers for deals that are too good to be true,
bizarre logorrhean gibberish, and explicit images you certainly don't want Aunt Millie to see.
You are now buried in a deluge of dreaded
[comment spam](/search/docs/advanced/guidelines/prevent-comment-spam).

Comment spam is bad stuff all around. It's bad for you, because it adds to your workload. It's bad
for your users, who want to find information on your site and certainly aren't interested in dodgy
links and unrelated content. It's bad for the web as a whole, since it discourages people from
opening up their sites for user-contributed content and joining conversations on existing forums.

So what can you, as a webmaster, do about it?

A quick disclaimer: the list below is a good start, but not exhaustive. There are so many
different blog, forum, and bulletin board systems out there that we can't possibly provide
detailed instructions for each, so the points below are general enough to make sense on most
systems.

## Make sure your commenters are real people

- Add a CAPTCHA. CAPTCHAs require users to read a bit of obfuscated text and type it back in to
  prove they're a human being and not an automated script. If your blog or forum system doesn't
  have CAPTCHAs built in you may be able to find a plugin like
  [Recaptcha](https://recaptcha.net/), a project which also helps
  digitize old books. CAPTCHAs are not foolproof but they make life a little more difficult for
  spammers.
  [You can read more about the many different types of CAPTCHAS](https://www.codinghorror.com/blog/archives/000712),
  but keep in mind that just adding a simple one can be fairly effective.
- Block suspicious behavior. Many forums allow you to set time limits between posts, and you can
  often find plugins to look for excessive traffic from individual IP addresses or proxies and
  other activity more common to bots than human beings.

## Use automatic filtering systems

- Block obviously inappropriate comments by adding words to a blocklist. Spammers obfuscate words
  in their comments so this isn't a very scalable solution, but it can keep blatant spam at bay.
- Use built-in features or plugins that delete or mark comments as spam for you. Spammers use
  automated methods to besmirch your site, so why not use an automated system to defend yourself?
  Comprehensive systems like
  [Akismet, which has plugins for many blogs and forum systems](https://akismet.com/development/)
  and [TypePad AntiSpam](https://antispam.typepad.com/), which is
  open-source and compatible with Akismet, are easy to install and do most of the work for you.
- Try using Bayesian filtering options, if available. Training the system to recognize spam may
  require some effort on your part, but this technique
  [has been used successfully to fight email spam](https://www.paulgraham.com/spam).

## Make your settings a bit stricter

- [`nofollow`](/search/docs/advanced/guidelines/qualify-outbound-links)
  untrusted links. Many systems have a setting to add a `nofollow` attribute to the
  links in comments, or do so by default. This may discourage some types of spam, but it's
  definitely not the only measure you should take.
- Consider requiring users to create accounts before they can post a comment. This adds steps to
  the user experience and may discourage some casual visitors from posting comments, but may keep
  the signal-to-noise ratio higher as well.
- Change your settings so that comments need to be approved before they show up on your site. This
  is a great tactic if you want to hold comments to a high standard, don't expect a lot of
  comments, or have a small, personal site. You may be able to allow employees or trusted users
  to approve posts themselves, spreading the workload.
- Think about disabling some types of comments. For example, you may want to disable comments on
  very old posts that are unlikely to get legitimate comments. On blogs you can often disable
  trackbacks and pingbacks, which are very cool features but can be major avenues for automated
  spam.

## Keep your site up-to-date

Take the time to keep your software up-to-date and pay special attention to important security
updates. Some spammers take advantage of security holes in older versions of blogs, bulletin
boards, and other content management systems. Check the
[Quick Security Checklist](/search/blog/2007/09/quick-security-checklist-for-webmasters)
for additional measures.

You may need to strike a balance on which tactics you choose to implement depending on your blog
or bulletin board software, your user base, and your level of experience. Opening up a site for
comments without any protection is a big risk, whether you have a small personal blog or a huge
site with thousands of users. Also, if your forum has been completely filled with thousands of
spam posts and doesn't even show up in Google searches, you may want to
 [submit a reconsideration request](/search/blog/2008/07/requesting-reconsideration-using-google)
after you clear out the bad content and take measures to prevent further spam.

As a [long-time blogger and web developer](https://www.jasonmorrison.net/content/)
myself, I can tell you that a little time spent setting up measures like these up front can save
you a ton of time and effort later. I'm new to the Webmaster Central team, originally from
Cleveland. I'm very excited to help fellow webmasters, and have a passion for usability and
search quality (I've even done
[a bit of academic research](https://dx.doi.org/10.1016/j.ipm.2007.12.010)
on the topic). Please share your tips on preventing comment and forum spam in our
[forum](https://support.google.com/webmasters/community), and as
always you're welcome to ask questions in our
[discussion group](https://support.google.com/webmasters/community).
