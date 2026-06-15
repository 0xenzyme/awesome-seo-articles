---
title: "My site's been hacked - now what?"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-04-my-sites-been-hacked-now-what"
url: "https://developers.google.com/search/blog/2008/04/my-sites-been-hacked-now-what"
canonical: "https://developers.google.com/search/blog/2008/04/my-sites-been-hacked-now-what"
author: "Written by Nathan Johns, Search Quality Team"
published: "2008-04-07T00:00:00+00:00"
updated: "2008-04-07T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:52:12+00:00"
status_code: 200
html_hash: "1701aa8b6c966f9e25a59e755ef1a32070aab97ca71504d3325d289c5cf83353"
clean_word_count: 1033
clean_char_count: 6533
---
# My site's been hacked - now what?

All right, you got hacked. It happens to many webmasters, even despite the hard work you devote
to prevent this type of thing from happening. Prevention tips include keeping your site updated
with the latest software and patches, creating an account with
[Google Webmaster Tools](https://search.google.com/search-console)
to see what's being indexed, keeping tabs on your log files to make sure nothing fishy's going
on, etc. (There's more information in the
[Quick Security Checklist](/search/blog/2007/09/quick-security-checklist-for-webmasters)
we posted last year.)

Remember that you're not alone—hacked sites are becoming increasingly common. Getting hacked
can result in your site being infected with badware (more specifically malware, one type of
badware). Take a look at
[StopBadware's](https://www.stopbadware.org/) recently released report on
[Trends in Badware 2007](https://www.stopbadware.org/pdfs/trends_in_badware_2007.pdf)
for a comprehensive analysis of threats and trends over the previous year. Check out
[this light technical report](https://googleonlinesecurity.blogspot.com/2008/02/all-your-iframe-are-point-to-us.html)
on the
[Google Online Security Blog](https://googleonlinesecurity.blogspot.com/)
which highlights the increasing number of search results containing a URL labeled as harmful. For
even more in-depth technical reports on the analysis of web-based malware, see
[The Ghost in the Browser](https://www.usenix.org/events/hotbots07/tech/full_papers/provos/provos.pdf)
(pdf) and this
[technical report](https://research.google.com/archive/provos-2008a.pdf)
(pdf) on drive-by downloads. Read these, and you'll have a much better understanding of the scope
of the problem. They also include some real examples for different types of malware.

The first step in any case should be to contact your hosting provider, if you have one. Often
times they can handle most of the technical heavy lifting for you. Lots of webmasters use shared
hosting, which can make it difficult to do some of the things listed below. Certain tips labeled
with an asterisk (\*) are cases in which webmasters using shared hosting will most likely require
assistance from their hosting provider. In the case that you do have full control over your
server, we recommend covering these four bases:

## Getting your site off-line

- Take your site off-line temporarily, at least until you know you've fixed things.
- If you can't take it off-line, return a
  [`503` status code](/search/docs/crawling-indexing/http-network-errors)
  to prevent it from being crawled.
- In the Webmaster Tools, use the
  [URL removal tool](https://www.google.com/support/webmasters/bin/answer.py?answer=61062&topic=8459)
  to remove any hacked pages or URLs from search results that may have been added. This will
  prevent the hacked pages from being served to users.

## Damage Assessment

- It's a good idea to figure out exactly what the hacker was after.
  - Were they looking for sensitive information?
  - Did they want to gain control of your site for other purposes?
- Look for any modified or uploaded files on your web server.
- Check your server logs for any suspicious activity, such as failed login attempts, command
  history (especially as root), unknown user accounts, etc.
- Determine the scope of the problem—do you have other sites that may be affected?

## Recovery

- The absolute best thing to do here is a complete reinstall of the OS from a trusted source. It's
  the only way to be completely sure you've removed everything the hacker may have done.\*
- After a fresh re-installation, use the latest backup you have to restore your site. Don't forget
  to make sure the backup is clean and doesn't have any hacked content.\*
- Patch any software packages to the latest version. This includes things such as weblog
  platforms, content management systems, or any other type of third-party software installed.
- Change your passwords—
  [see our help center for tips about creating a strong password](https://www.google.com/accounts/PasswordHelp)

## Restoring your online presence

- Get your system back online.
- If you're a Webmaster Tools user, sign in to your account
  - If your site was flagged as having malware, request a review to determine whether your site
    is clean
  - If you used the URL removal tool on URLs which you do want in the index, request that
    Webmaster Tools re-include your content by revoking the removal.
- Keep an eye on things, as the hacker may try to return.

Answers to other questions you may be asking:

**Is it better to take my site off-line or use robots.txt to prevent it from being crawled?**
Taking it off-line is a better way to go; this prevents any malware or badware from being served
to users, and prevents hackers from further abusing the system.

**Once I've fixed my site, what's the fastest way to get re-crawled?** The best way, regardless
of whether or not your site got hacked, is to follow the
[Webmaster Help Center guidelines](/search/docs/fundamentals/get-on-google).

**I've cleaned it up, but will Google penalize me if the hacker linked to any bad
neighborhoods?** We'll try not to. We're pretty good at making sure good sites don't get
penalized by actions of hackers and spammers. To be safe, completely remove any links the hackers
may have added.

**What if this happened on my home machine?** All of the above still applies. You'll want to
take extra care to clean it up; if you don't, it's likely the same thing will happen again. A
complete re-install of the OS is ideal.

Additional resources you may find helpful:

- If your site's been flagged by Google as serving malware, we'll
  [alert you](/search/blog/2006/11/badware-alerts-for-your-sites)
  when you visit
  [Webmaster Tools](https://search.google.com/search-console).
- Don't forget about the
  [Google Webmaster Help Group](https://support.google.com/webmasters/community);
  it's full of extremely knowledgeable users, and Googlers as well. For a nice, on-topic
  example, check out
  [this thread](https://groups.google.com/group/Google_Webmaster_Help-Indexing/browse_thread/thread/98cd67810dc69942/72809bf28e8e039a).
  There's also a
  [Stop Badware group](https://groups.google.com/group/stopbadware).
- Matt Cutts recently posted
  [Three tips to protect your WordPress installation](https://www.mattcutts.com/blog/three-tips-to-protect-your-wordpress-installation/)
  on his blog, and there are lots of great comments below the post as well.
