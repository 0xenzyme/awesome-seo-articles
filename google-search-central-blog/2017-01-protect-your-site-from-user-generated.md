---
title: "Protect your site from user generated spam"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2017-01-protect-your-site-from-user-generated"
url: "https://developers.google.com/search/blog/2017/01/protect-your-site-from-user-generated"
canonical: "https://developers.google.com/search/blog/2017/01/protect-your-site-from-user-generated"
author: "Anouar Bendahou, Search Quality Strategist, Google Ireland"
published: "2017-01-27T00:00:00+00:00"
updated: "2017-01-27T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2017_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:30:01+00:00"
status_code: 200
html_hash: "1781561609f714f0b3d76c690e54eed7ab19e62aa7b67bffe096ea37dfe99f46"
clean_word_count: 745
clean_char_count: 4805
---
# Protect your site from user generated spam

As a website owner, you might have come across some auto-generated content in comments sections or
forum threads. When such content is created on your pages, not only does it disrupt those visiting
your site, but it also shows some content that you may not want to be associated with your site to
Google and other search engines.

In this blog post, we will give you tips to help you deal with this type of spam in your site and
forum.

Some spammers abuse sites owned by others by posting deceiving content and links, in an attempt to
get more traffic to their sites. Here are a few examples:

![](/static/search/blog/images/import/d8a7bcb8579cef084b5d6aa778736424.png)
![](/static/search/blog/images/import/8fb3f594c27c868a2be087f6cf6420ff.png)

Comments and forum threads can be a really good source of information and an efficient way of
engaging a site's users in discussions. This valuable content should not be buried by
auto-generated keywords and links placed there by spammers.

There are many ways of securing your site's forums and comment threads and making them
unattractive to spammers:

- **Keep your forum software updated and patched**:
  Take the time to keep your software up-to-date and pay special attention to important security
  updates. Spammers take advantage of security issues in older versions of blogs, bulletin
  boards, and other content management systems.

- **Add a CAPTCHA**:
  [CAPTCHAs](https://en.wikipedia.org/wiki/CAPTCHA)
  require users to confirm that they are not robots in order to prove they're a human being and
  not an automated script. One way to do this is to use a service like
  [reCAPTCHA](https://www.google.com/recaptcha/intro/index),
  [Securimage](https://www.phpcaptcha.org/)
  and [Jcaptcha](https://jcaptcha.sourceforge.net/).
- **Block suspicious behavior**:
  Many forums allow you to set time limits between posts, and you can often find plugins to look
  for excessive traffic from individual IP addresses or proxies and other activity more common
  to bots than human beings. For example,
  [phpBB](https://www.phpbb.com/customise/db/mod/limit_post_as_count_per_forum/),
  [Simple Machines](https://custom.simplemachines.org/mods/index.php?mod=1327),
  [myBB](https://mods.mybb.com/view/limit-number-of-posts), and many other forum
  platforms enable such configurations.
- **Check your forum's top posters on a daily basis**: If a user joined recently and has an
  excessive amount of posts, then you probably should review their profile and make sure that
  their posts and threads are not spammy.
- **Consider disabling some types of comments**:
  For example, it's a good practice to close some very old forum threads that are unlikely to
  get legitimate replies.

  If you plan on not monitoring your forum going forward and users are no longer interacting with
  it, turning off posting completely may prevent spammers from abusing it.
- **Make good use of moderation capabilities**:
  Consider enabling features in moderation that require users to have a certain reputation
  before links can be posted or where comments with links require moderation.

  If possible, change your settings so that you disallow anonymous posting and make posts from
  new users require approval before they're publicly visible.

  Moderators, together with your friends/colleagues and some other trusted users can help you
  review and approve posts while spreading the workload. Keep an eye on your forum's new users
  by looking on their posts and activities on your forum.
- **Consider blocklisting obviously spammy terms**:
  Block obviously inappropriate comments with a blocklist of spammy terms (for example, Illegal streaming
  or pharma related terms). Add inappropriate and off-topic terms that are only used by
  spammers, learn from the spam posts that you often see on your forum or other forums. Built-in
  features or plugins can delete or mark comments as spam for you.
- **Use the `nofollow` attribute for links in the comment field**: This will deter
  spammers from targeting your site. By default, many blogging sites (such as Blogger)
  automatically add this attribute to any posted comments.
- **Use automated systems to defend your site**: Comprehensive systems like
  [Akismet, which has plugins for many blogs and forum systems](https://akismet.com/development/)
  are easy to install and do most of the work for you.

For detailed information about these topics, check out our Help Center document on
[User Generated Spam](/search/docs/advanced/guidelines/user-gen-spam)
and
[comment spam](/search/docs/advanced/guidelines/prevent-comment-spam).
You can also visit our
[Webmaster Central Help Forum](https://support.google.com/webmasters/go/community)
if you need any help.
