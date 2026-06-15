---
title: "Simplified Chinese blog: Tips for reducing comment spam"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2007-11-tips-for-reducing-comment-spam"
url: "https://developers.google.com/search/blog/2007/11/tips-for-reducing-comment-spam"
canonical: "https://developers.google.com/search/blog/2007/11/tips-for-reducing-comment-spam"
author: "Chao Ma and Marina Ma"
published: "2007-11-01"
updated: "2007-11-01"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2007_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:50:52+00:00"
status_code: 200
html_hash: "57d0f77362f80ed56998c6663a913faaa8eda6901f841cc1053716a6e82c5865"
clean_word_count: 687
clean_char_count: 4332
---
# Simplified Chinese blog: Tips for reducing comment spam

2007-11-01

Comments are a great way for webmasters to build visitor communities. Unfortunately, as most
people already know, comments are also commonly abused by spammers posting overwhelming numbers
of links to their own websites. Some use scripts or other software to generate and post gibberish
comments. At Google, we've been working hard to counter the negative effects of this spam on our
search results. Here are some tips for preventing comment spam on your blog or website:

## Use comments only when they're necessary

Think twice before deciding to enable a guestbook or comments. If this feature is not really
necessary or you will not be able to monitor the guestbook and comments regularly, consider
disabling it. If you already have a guestbook, check to see if it's useful to visitors, and if
they've been visiting it. If not, consider ways to improve the comments/guestbook feature, or
remove it. A lot of spam comments don't create a good impression. Most blogging software will
let you turn comments off for individual posts.

## Use anti-comment spam tool

Most website development tools, especially blog tools, have functionality that requires users to
pass a check to make sure they're a real live human, not a nasty spamming engine. You'll have seen
these: generally the user is presented with a distorted image or captcha and asked to type the
letters or numbers she sees in the image. This is a pretty effective way of preventing comment
spam. The process may reduce the number of casual readers who leave comments on your pages, but
it will definitely improve the quality of the comments. WordPress has a good introduction to
[plugins and anti-spam tools](https://codex.wordpress.org/Plugins/Spam_Tools).

## Turn on comment moderation

Comment moderation means that no comments will appear on your site until you manually review and
approve them. This means you'll spend more time monitoring your comments, but it can really help
to improve the user experience for your visitors. It's particularly worthwhile if you regularly
post about controversial subjects, where emotions can become heated. It's generally available as
a setting in your blogging software, under **Comments**.

## Use `nofollow` Tags

Together with Yahoo! and MSN, Google introduced the `nofollow` attribute a few years
ago, and the attribute has been widely accepted. Any link with the `nofollow` attribute
will not be used to calculate PageRank. For example, if a spammer includes a link in your comments
like this: `<a href="https://www.example.com/">`, it will get converted to
`<a href="https://www.example.com/" rel="nofollow">` and would not be taken into
account when calculating PageRank.

By default, many blogging sites (such as Blogger) automatically add this attribute to any posted
comments.

For more information about `nofollow` tags, check out
[How to Stop Spam Comments](https://googleblog.blogspot.com/2005/01/preventing-comment-spam.html).

## Block comment pages using robots.txt or `meta` tags

You can use your robots.txt file to block Google's access to certain pages. This won't stop
spammers from leaving comments, but it will mean that links in these comments won't negatively
impact your site. For example, if comments are stored in the subdirectory **guestbook**, you
could add the following to your robots.txt:

```
Disallow:/guestbook
```

This will block Google from indexing the contents of guestbook and any subdirectories.

You can also use `meta` tag to block access to a single selected page, for example
https://www.example.com/article/comments. Like this:

```
<html>
  <head>
    <meta name="googlebot" content="noindex">
  ...
```

For more information about robots.txt, check out our
[Help Center](/search/docs/crawling-indexing/robots/intro).

## Disallow hyperlinks in comment

If you have access to the server, you may want to change its configuration to remove HTML tags
inside your guestbook. Spammers will still be able to leave comments, but they won't be able to
publish active hyperlinks.

If comment spam is driving you crazy, try one or two of these methods and see how it works out.
Got comments or suggestions? Leave them in our
[Google Webmaster Help discussion group](https://support.google.com/webmasters/community).
