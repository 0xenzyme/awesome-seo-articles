---
title: "#NoHacked: Fixing the Injected Gibberish URL Hack"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2015-08-nohacked-fixing-injected-gibberish-url_24"
url: "https://developers.google.com/search/blog/2015/08/nohacked-fixing-injected-gibberish-url_24"
canonical: "https://developers.google.com/search/blog/2015/08/nohacked-fixing-injected-gibberish-url_24"
author: "Posted by: Eric Kuan, Webmaster Relations Specialist and Yuan Niu, Webspam Analyst"
published: "2015-08-24T00:00:00+00:00"
updated: "2015-08-24T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2015_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:27:14+00:00"
status_code: 200
html_hash: "9a9e4611cda5e23b5e0eb66dfb41bf8d95e6a4193615fb0a55cfaa979ff4e62e"
clean_word_count: 1336
clean_char_count: 8280
---
# #NoHacked: Fixing the Injected Gibberish URL Hack

Today in our #NoHacked campaign, we'll be discussing how to fix the injected gibberish URL hack we
wrote about last week. Even if your site is not infected with this specific type of hack, many of
these steps can be helpful for fixing other types of hacks. Follow along with discussions on
[Twitter](https://twitter.com/googlesearchc)
and [Google+](https://google.com/+googlewebmasters) using the
#NoHacked tag.
([Part 1](/search/blog/2015/07/nohacked-how-to-avoid-being-target-of),
[Part 2](/search/blog/2015/08/nohacked-how-to-recognise-and-protect),
[Part 3](/search/blog/2015/08/nohacked-using-two-factor),
[Part 4](/search/blog/2015/08/nohacked-identifying-and-diagnosing))

![](/static/search/blog/images/import/e1e83f15129a93fd8f4ea2a5c040e3bf.png)

- [Temporarily Take your Site Offline](#TempOffline)
- [Treating your Site](#TreatingSite)
  - [Checking your `.htaccess` file](#Checkhtaccess)
  - [Identifying other malicious files](#IDMalicious)
  - [Removing malicious content](#RemoveMalicious)
  - [Identifying and Fixing the Vulnerability](#IDVulnerability)
- [Next Steps](#NextSteps)
- [Appendix](#Appendix)

## Temporarily Take your Site Offline

Taking your site offline temporarily will prevent your site's visitors from going to hacked pages
and give you time to properly fix your site. If you keep your site online, you run the risk of
getting compromised again as you clean up your site.

## Treating your Site

The next few steps require you to be comfortable making technical changes to your site. If you
aren't familiar or comfortable enough with your site to make these changes, it might be best to
consult with or hire someone who is. However, reading through these steps will still be helpful.

Before you start fixing your site, we advise that you back up your site. (This backed up version
will still contain hacked content and should only be used if you accidentally remove a critical
file.) If you're unsure how to back up your site, ask your hosting provider for assistance or
consult your content management system (CMS) documentation. As you work through the steps, any
time you remove a file, make sure to keep a copy of the file as well.

### Checking your `.htaccess` file

In order to manipulate your site, this type of hack creates or alters the contents of your
[`.htaccess` file](https://en.wikipedia.org/wiki/.htaccess).
If you're not sure where to find your `.htaccess` file, consult your server or CMS
documentation.

Check the contents of your `.htaccess` file for any suspicious content. If you're not
sure how to interpret the contents of the `.htaccess` file, you can read about it on
the [Apache.org](https://httpd.apache.org/docs/2.0/misc/rewriteguide)
documentation, ask in a help forum, or you can consult an expert. Here is an example of a
`.htaccess` modified by this hack:

```
<IfModule mod_rewrite.c>
RewriteEngine On
#Visitors that visit your site from Google will be redirected
RewriteCond %{HTTP_REFERER} google\.com
#Visitors are redirected to a malicious PHP file called happypuppy.php
RewriteRule (.*pf.*) /happypuppy.php?q=$1 [L]
</IfModule>
```

### Identifying other malicious files

The most common types of files that are modified or injected by this hack are JavaScript and PHP
files. Hackers typically take two approaches: The first is to insert new PHP or JavaScript files
on your server. The inserted files can sometimes be named something very similar to a legitimate
file on your site like `wp-cache.php` versus the legitimate file
`wp_cache.php`. The second approach is to alter legitimate files on your server and
insert malicious content into these files. For example, if you have a template or plugin
JavaScript file on your site, hackers might add malicious JavaScript to the file.

For example, on [www.example.com](https://www.example.com/) a malicious
file named `happypuppy.php`, identified earlier in the `.htaccess` file, was
injected into a folder on the site. However, the hackers also corrupted a legitimate JavaScript
file called `json2.js` by adding malicious code to the file. Here is an example of a
corrupted `json2.js` file. The malicious code is highlighted in red and has been added
to the very bottom of the `json2.js` file:

![](/static/search/blog/images/import/aa515c435ab90ad996a5fe8697709a55.png)

To effectively track down malicious files, you'll need to understand the function of the
JavaScript and PHP files on your site. You might need to consult your CMS documentation to help
you. Once you know what the files do, you should have an easier time tracking down malicious files
that don't belong on your site.

Also, check your site for any recently modified files. Template files that have been modified
recently should be thoroughly investigated. Tools that can help you interpret obfuscated PHP files
can be found in the Appendix.

### Removing malicious content

As mentioned previously, back up the contents of your site appropriately before you remove or
alter any files. If you regularly make backups for your site, cleaning up your site might be as
easy as restoring a clean backed-up version.

However, if you do not regularly back up your site, you have a few alternatives. First, delete any
malicious files that have been inserted on your site. For example, on www.example.com, you would
delete the `happypuppy.php` file. For corrupted PHP or JavaScript files like
`json2.js`, you'll have to upload a clean version of those files to your site. If you
use a CMS, consider reloading a fresh copy of the core CMS and plugin files on your site.

## Identifying and Fixing the Vulnerability

Once you've removed the malicious file, you'll want to track down and fix the vulnerability that
allowed your site to be compromised, or you risk your site being hacked again. The vulnerability
could be anything from a stolen password to outdated web software. Consult
[Google Webmaster Hacked Help](/web/fundamentals/security/hacked/vulnerability)
for ways to identify and fix the vulnerability. If you're unable to figure out how your site was
compromised, you should change your passwords for all your login credentials,update all your web
software, and seriously consider getting more help to make sure everything is ok.

## Next Steps

Once you're done cleaning your site, use the Fetch as Google tool to check if the hacked pages
still appear to Google. You'll need to bring your site back online to test with Fetch as Google.
Don't forget to check your home page for hacked content as well. If the hacked content is gone,
then, congratulations, your site should be clean! If the Fetch as Google tool is still seeing
hacked content on those hacked pages, you still have work to do. Check again for any malicious PHP
or JavaScript files you might have missed.

Bring your site back online as soon as you're sure your site is clean and the vulnerability has
been fixed. If there was a
[manual action](https://support.google.com/webmasters/answer/2604824)
on your site, you'll want to file a
[reconsideration request](https://support.google.com/webmasters/answer/35843)
in Search Console. Also, think about ways to protect your site from future attacks. You can read
more about how to secure your site from future attacks in the
[Google Hacked Webmaster Help Center](/web/fundamentals/security/hacked).

We hope this post has helped you gain a better understanding of how to fix your site from the
injected gibberish URL hack. Be sure to follow our social campaigns and share any tips or tricks
you might have about staying safe on the web with the #nohacked hashtag.

If you have any additional questions, you can post in the
[Webmaster Help Forums](https://support.google.com/webmasters/community/)
where a community of webmasters can help answer your questions. You can also join our
[Hangout on Air about Security](https://plus.google.com/events/csqjnqe8vl28qbn526makjecobc)
on August 26.

## Appendix

These are tools that may be useful. Google doesn't run or support them.
[PHP Decoder](https://ddecode.com/phpdecoder/),
[UnPHP](https://www.unphp.net/): Hackers will often distort PHP files
to make them harder to read. Use these tools to clean up the PHP files so you understand better
what the PHP file is doing.
