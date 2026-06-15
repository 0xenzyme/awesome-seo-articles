---
title: "Feeling lucky at PubCon"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-01-feeling-lucky-at-pubcon"
url: "https://developers.google.com/search/blog/2008/01/feeling-lucky-at-pubcon"
canonical: "https://developers.google.com/search/blog/2008/01/feeling-lucky-at-pubcon"
author: "Michael Wyszomierski"
published: "2008-01-22T00:00:00+00:00"
updated: "2008-01-22T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:51:18+00:00"
status_code: 200
html_hash: "fb31ffc2d9cd8357e6a5e690426705ce6afdf62e7182aaefdd96d29a4dd563e9"
clean_word_count: 1196
clean_char_count: 7282
---
# Feeling lucky at PubCon

Last month, several of us with Webmaster Central
[raked in the "good times" jackpot](https://www.google.com/calendar/event?eid=NHFnOW85aG1tZ2NhaWFtbDZjNHNkZWNudXMgZ3dlYm1hc3RlcmNlbnRyYWxAbQ)
at PubCon Vegas 2007. We realize not all of you could join us, so instead of returning home with
fuzzy dice for everyone, we've got souvenir
[conference notes](/search/blog/2007/11/bringing-conference-to-you).

Listening to the Q&A, I was pleased to hear the major search engines agreeing on best
practices for many webmaster issues. In fact, the presentations in the duplicate content session
were mostly, well, duplicate. When I wasn't sitting in on one of the many valuable sessions, I was
chatting with webmasters either at the Google booth, or at Google's "Meet the Engineers" event. It
was exciting to hear from so many different webmasters, and to help them with Google-related
issues. Here are a few things that were on the minds of webmasters, along with our responses:

## Site Verification Files and Meta Tags

Several webmasters asked, "Is it necessary to keep the verification `meta` tag or HTML file in place
to remain a verified owner in Webmaster Tools?" The answer is yes, you should keep your
verification file or `meta` tag live to maintain your status as a verified owner. These
verification codes are used to control who has access to the owner-specific tools for your site
in Webmaster Tools. To ensure that only current owners of a site are verified, we periodically
re-check to see if the verification code is in place, and if it is not, you will get unverified
for that site. While we're on the topic:

### Site Verification Best Practices

- If you have multiple people working on your site with Webmaster Tools, it's a good idea to
  have each person verify the site with their own account, rather than using a shared login.
  That way, as people come and go, you can control the access appropriately by adding or
  removing verification files or `meta` tags for each account.
- You may want to keep a list of these verification codes and which owner they are connected to,
  so you can easily control access later. If you lose track, you can always use the "Manage
  site verification" option in Webmaster Tools, which allows you to force all site owners to
  reverify their accounts.

### Subdomains vs. Subdirectories

What's the difference between using subdomains and subdirectories? When it comes to Google, there
aren't major differences between the two, so when you're making that decision, do what works for
you and your visitors. Following PubCon, our very own Matt Cutts
[outlined many of the key issues](https://www.mattcutts.com/blog/subdomains-and-subdirectories/)
in a post on his personal blog. In addition to those considerations, if you use Webmaster Tools
(which we hope you do!), keep in mind that you'll automatically be verified for deeper
subdirectories of any sites you've verified, but subdomains need to be verified separately.

### Underscores vs. Dashes

Webmasters asked about the difference between how Google interprets underscores and dashes in
URLs. In general, we break words on punctuation, so if you use punctuation as separators, you're
providing Google a useful signal for parsing your URLs. Currently, dashes in URLs are
consistently treated as separators while underscores are not. Keep in mind our technology is
constantly improving, so this distinction between underscores and dashes may decrease over time.
Even without punctuation, there's a good chance we'll be able to figure out that
`bigleopard.html` is about a "big leopard" and not a
"bigle opard". While using separators is a good practice, it's
likely unnecessary to place a high priority on changing your existing URLs just to convert
underscores to dashes.

### Keywords in URLs

We were also asked if it is useful to have relevant keywords in URLs. It's always a good idea to
be descriptive across your site, with titles,
[ALT attributes](/search/blog/2007/12/using-alt-attributes-smartly), and yes, even
URLs, as they can be useful signals for users and search engines. This can be especially true
with image files, which otherwise may not have any text for a search engine to consider. Imagine
you've taken a picture of your cat asleep on the sofa. Your digital camera will likely name it
something like `IMG_2937.jpg`. Not exactly the most descriptive name. So unless your
cat really looks like an `IMG_2937`, consider changing the filename to something more
relevant, like adorable-kitten.jpg. And, if you have a post about your favorite cat names, it's
much easier to guess that a URL ending in my-favorite-cat-names would be the relevant page,
rather than a URL ending in `postid=8652`. For more information regarding issues with
how Google understands your content, check out our new
[content analysis](/search/blog/2007/12/new-content-analysis-and-sitemap)
feature in Webmaster Tools, as well as
[our post on the URL suggestions feature](/search/blog/2007/12/fyi-on-google-toolbars-latest-features)
of the new Google Toolbar.

### Moving to a new IP address

We got a question about changing a site's IP address, and provided a few steps you can take as a
webmaster to make sure things go smoothly. Here's what you can do:

1. Change the TTL (Time To Live) value of your DNS configuration to something short, like five
   minutes (300 seconds). This will tell web browsers to re-check the IP address for your site
   every five minutes.
2. Copy your content to the new hosting environment, and make sure it is live on the new IP
   address.
3. Change your DNS settings so your hostname points to the new IP address.
4. Check your logs to see when Googlebot starts crawling your site on the new IP address. To make
   sure it's really Googlebot who's visiting, you can verify Googlebot by following
   [these instructions](/search/blog/2006/09/how-to-verify-googlebot). You can then log
   into Webmaster Tools and monitor any crawl errors. Once Googlebot is happily crawling on the
   new IP address, you should be all set as far as Google is concerned.
5. To make sure everyone got the message of your move, you may want to keep an eye out for visits
   to your old IP address before shutting it down.

### Proxies

A few webmasters were concerned that proxy services are being indexed with copies of their
content. While it's often possible to find duplicate copies of your content in our results if you
look hard enough, the original source is most likely going to be ranked higher than a proxy copy.
However, if you find this not to be the case, please drop us some URLs in the Webmaster Help
Group. There are many Googlers including myself who monitor this group and escalate issues
appropriately.

It was great talking with webmasters at the conference—we hope those of you unable to join
us found this post useful. If you want to continue to talk shop with me, other Googlers, and your
fellow webmasters, join the follow-up conversation in the
[Webmaster Help Group](https://support.google.com/webmasters/community).

**Update**:
[Additional PubCon notes](https://groups.google.com/group/Google_Webmaster_Help-Indexing/browse_thread/thread/8d427cdd556f644e)
from Jonathan Simon are available in our discussion group.
