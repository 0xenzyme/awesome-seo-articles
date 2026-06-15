---
title: "Case Studies: Fixing Hacked Sites"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2015-02-case-studies-fixing-hacked-sites"
url: "https://developers.google.com/search/blog/2015/02/case-studies-fixing-hacked-sites"
canonical: "https://developers.google.com/search/blog/2015/02/case-studies-fixing-hacked-sites"
author: "Julian Prentice and Yuan Niu, Search Quality Team"
published: "2015-02-18T00:00:00+00:00"
updated: "2015-02-18T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2015_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:26:03+00:00"
status_code: 200
html_hash: "bdde006fcb3dad5daeccb6c88994aeeb205e5473f4dd218ac32566f4ab1cb926"
clean_word_count: 1364
clean_char_count: 8457
---
# Case Studies: Fixing Hacked Sites

Every day, thousands of websites get hacked. Hacked sites can harm users by serving malicious
software, collecting personal information, or redirecting them to sites they didn't intend to
visit. Webmasters want to fix hacked sites quickly, but unfortunately recovering from a hack can
be a complicated process.

We're trying to make the process of recovering from a hack easier for webmasters with features like
[Security Issues](https://search.google.com/search-console/security-issues),
[Help for Hacked Sites](/web/fundamentals/security/hacked), and
[a section of our forum just for hacked sites](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:security_malware_hacked)).
Recently we talked to two webmasters with hacked sites to learn more about how they were able to
fix their sites. We're sharing their stories with the hope that they might provide ideas to other
webmasters who have been victims of hacking. We're also using these stories and other feedback for
improving our documentation for hacked sites to make the process easier for everyone going
forward.

## Case Study #1: Restaurant website with multiple hack-injected scripts

A restaurant website using WordPress received a message from Google in their Webmaster Tools
account, alerting them that their site had been altered by hackers. To protect Google users, the
website was labelled as hacked in Google's search results. The webmaster of the site, Sam, looked
at the source code and noticed many unfamiliar links on the site with pharmaceuticals terms such
as "viagra" and "cialis." She also noticed many pages where the meta description tags (in the
HTML) had added content such as "buy valtrex in florida." There were also hidden `div`
tags (also in the HTML) of many pages that linked to many sites. None of these links were added
by Sam.

Sam removed all of the hacked content she found and filed a reconsideration request. The request
was rejected but in the message she received from Google, she was advised to check for any
unfamiliar scripts in the any PHP files (or any other server files), as well as changes to the
[`.htaccess`](https://httpd.apache.org/docs/trunk/howto/htaccess)
file. These files are likely to have scripts added by the hackers that modify the site. These
scripts typically only show the hacked content to search engines, while hiding the content from a
normal user. Sam checked out all of the `.php` files and compared them to the clean
copies she had in her backup. She found new content added to her `footer.php`,
`index.php`, and `functions.php`. When she replaced those files with the
clean backups, she could no longer find any hacked content on her site. When she filed another
reconsideration request, she got a response from Google notifying her that her site no longer had
hacked content!

Even though Sam had cleaned up the hacked content on her site, she knew that she would need to
continue to
[secure her site](https://codex.wordpress.org/Hardening_WordPress)
against future attacks. She followed the steps below to keep her site safe in the future:

- Keep the CMS (content management system like WordPress, Joomla, Drupal, etc) up to date with the
  most current version. Make sure plugins are up to date as well.
- Make sure the account used to access the administrative features of the CMS uses a difficult and
  unique password.
- If the CMS supports it, enable
  [2-step verification](https://en.support.wordpress.com/security/two-step-authentication/)
  for login. (This might also be called two factor authentication or two step authentication.)
  This is recommended for the account being used for password recovery as well. Most email
  providers, like
  [Google](https://www.google.com/landing/2step/),
  [Microsoft](https://windows.microsoft.com/en-us/windows/two-step-verification-faq),
  [Yahoo!](https://help.yahoo.com/kb/activate-sign-in-verification-sln5013)
  all support this!
- Make sure the plugins and themes installed are from a reputable source—pirated plugins or
  themes can often contain code that makes it even easier for hackers to get in!

## Case Study #2: Professional website with lots of hard to find hacked pages

A small business owner named Maria who also manages her own website received a message in her
Webmaster Tools that her site was hacked. The message provided an example of a page added by
hackers: `https://example.com/where-to-buy-cialis-over-the-counter/`. She talked to her
hosting provider who looked at the source code on the home page but could not find any
pharmaceutical keywords. When the hosting provider visited
`https://example.com/where-to-buy-cialis-over-the-counter/`, it returned an error page.
Maria also bought a malware scanning service but the service was not able to find any malicious
content on her site.

Maria then went to Webmaster Tools and used the Fetch as Google tool on the example URL Google had
provided (`https://example.com/where-to-buy-cialis-over-the-counter/`) which returned
no content. Confused, she filed a reconsideration request and received a rejection message which
advised her to do two things:

1. Verify the non-www version of her site as hackers often try to hide content in folders that
   may be overlooked by the webmaster.

   While it may seem like `https://example.com` and `https://www.example.com`
   are the same site, Google actually treats these as different sites.
   `https://example.com` is referred to as the "root domain" while
   `https://www.example.com` is called the subdomain. Maria had
   `https://www.example.com` verified but not `https://example.com` verified
   which is important because the pages added by hackers were non-www pages like
   `https://example.com/where-to-buy-cialis-over-the-counter/`. Once she verified
   `https://example.com` she was able to successfully see the hacked content on the
   provided URL with the Fetch as Google tool in Webmaster Tools.
2. Check her `.htaccess` file for new rules.

   Maria talked to her hosting provider who showed her how to access her `.htaccess`
   file. She noticed right away that her `.htaccess` file had some strange content
   that she had not added:

   ```
   <ifmodule mod_rewrite.c="mod_rewrite.c">
   RewriteEngine On
   RewriteCond %{HTTP_USER_AGENT} (google|yahoo|msn|aol|bing) [OR]
   RewriteCond %{HTTP_REFERER} (google|yahoo|msn|aol|bing)
   RewriteRule ^([^/]*)/$ /main.php?p=$1 [L]
   </ifmodule>
   ```

   The
   [`mod_rewrite`](https://httpd.apache.org/docs/2.0/misc/rewriteguide)
   rule you see above was inserted by the hacker and redirects anyone coming from certain search
   engines, as well as search engine crawlers, to main.php, which generates all of the hacked
   content. It's also possible that these rules can redirect users accessing the site on a mobile
   device. On the same day, she also saw that a recent malware scan found suspicious content on
   the `main.php` file. One top of that, she also noticed an unknown user in the FTP
   users area of her website development software.

She removed the `main.php` file, the `.htaccess` file, and removed the
unknown user from her FTP users area and her site was no longer hacked!

## Steps to prevent getting hacked in the future

- Avoid using FTP when transferring files to your servers. FTP does not encrypt any traffic,
  including passwords. Instead, use SFTP, which will encrypt everything, including your password,
  as a protection against eavesdroppers examining network traffic.
- Check the permissions on sensitive files like `.htaccess`. Your hosting provider may
  be able to assist you if you need help. The `.htaccess` file can be used to improve
  and protect your site, but it can also be used for malicious hacks if they are able to gain
  access to it.
- Be vigilant and look for new and unfamiliar users in your administrative panel and any other
  place where there may be users that can modify your site.

We hope your site never gets hacked, but if it does, we have many resources for hacked webmasters
on our
[Help for Hacked Sites page](/web/fundamentals/security/hacked). If
you need more help or would like to share your own tips, you can post in our
[Webmaster Help Forum](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:security_malware_hacked)).
If you do post to the forum or submit a reconsideration request for your site, please include
`#NoHacked`.
