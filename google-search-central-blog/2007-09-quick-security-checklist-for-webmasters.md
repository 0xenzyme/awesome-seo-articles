---
title: "Quick security checklist for webmasters"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2007-09-quick-security-checklist-for-webmasters"
url: "https://developers.google.com/search/blog/2007/09/quick-security-checklist-for-webmasters"
canonical: "https://developers.google.com/search/blog/2007/09/quick-security-checklist-for-webmasters"
author: "Written by Nathan Johns, Search Quality Team"
published: "2007-09-18T00:00:00+00:00"
updated: "2007-09-18T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2007_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:50:16+00:00"
status_code: 200
html_hash: "f055a31fe188119a466fe25f2dd050b5d4d9d1c3a7dab5655bb7bdd1ed4fb6dc"
clean_word_count: 795
clean_char_count: 4942
---
# Quick security checklist for webmasters

In recent months, there's been a noticeable increase in the number of compromised websites around
the web. One explanation is that people are resorting to hacking sites in order to distribute
malware or attempt to spam search results. Regardless of the reason, it's a great time for all
of us to review helpful webmaster security tips.

## Check your server configuration.

Apache has some
[security configuration tips](https://httpd.apache.org/docs/1.3/misc/security_tips)
on their site and Microsoft has some
[tech center resources for IIS](https://technet2.microsoft.com/windowsserver/en/library/354f4539-982a-418c-bfe7-4d5155b83f4a1033.mspx?mfr=true)
on theirs. Some of these tips include information on directory permissions, server side includes,
authentication and encryption.

## Stay up-to-date with the latest software updates and patches.

A common pitfall for many webmasters is to install a forum or blog on their website and then
forget about it. Much like taking your car in for a tune-up, it's important to make sure you have
all the latest updates for any software program you have installed. Need some tips? Blogger Mark
Blair has a few
[good ones](https://www.mblair.net/no-sweat-website-security/),
including making a list of all the software and plug-ins used for your website and keeping track
of the version numbers and updates. He also suggests taking advantage of any feeds their websites
may provide.

## Regularly keep an eye on your log files.

Making this a habit has many great benefits, one of which is added security. You might be
surprised with what you find.

## Check your site for common vulnerabilities.

Avoid having directories with open permissions. This is almost like leaving the front door to your
home wide open, with a door mat that reads "Come on in and help yourself!" Also check for any
[XSS](https://www.owasp.org/index.php/Cross_Site_Scripting)
(cross-site scripting) and
[SQL injection](https://www.owasp.org/index.php/SQL_injection)
vulnerabilities. Finally, choose good passwords. The Gmail support center has some good
[guidelines](https://mail.google.com/support/bin/answer.py?answer=29409&topic=8266)
to follow, which can be helpful for choosing passwords in general.

## Be wary of third-party content providers.

If you're considering installing an application provided by a third party, such as a widget,
counter, ad network, or webstat service, be sure to exercise due diligence. While there are lots
of great third-party content on the web, it's also possible for providers to use these
applications to push exploits, such as dangerous scripts, towards your visitors. Make sure the
application is created by a reputable source. Do they have a legitimate website with support and
contact information? Have other webmasters used the service?

## Try a Google `site:` search to see what's indexed.

This may seem a bit obvious, but it's commonly overlooked. It's always a good idea to do a quick
check and make sure things look normal. If you're not already familiar with the
`site:` search operator, it's a way for you to restrict your search to a specific site.
For example, the search
[site:googleblog.blogspot.com](https://www.google.com/search?q=site%3Agoogleblog.blogspot.com)
will only return results from the Official Google Blog.

## Use Google's [Webmaster Tools](https://search.google.com/search-console/about)

It includes all kinds of good stuff like a site status wizard and tools for managing how Googlebot
crawls your site. Another nice feature is that if Google believes your site has been hacked to
host malware, our
[webmaster console will show more detailed information](/search/blog/2007/08/malware-reviews-via-webmaster-tools),
such as a sample of harmful URLs. Once you think the malware is removed, you then can request a
reevaluation through Webmaster Tools.

## Use secure protocols.

SSH and SFTP should be used for data transfer, rather than plain text protocols such as telnet
or FTP. SSH and SFTP use encryption and are much safer. For this and many other useful tips,
check out StopBadware.org's
[Tips for Cleaning and Securing Your Website](https://www.stopbadware.org/home/security).

## Read the [Google Online Security Blog](https://googleonlinesecurity.blogspot.com/).

Here's some great content about online security and safety with pointers to lots of useful
resources. It's a good one to add to your Google Reader feeds. :)

## Contact your hosting company for support.

Most hosting companies have helpful and responsive support groups. If you think something may be
wrong, or you simply want to make sure you're in the know, visit their website or give 'em a call.

We hope you find these tips helpful. If you have some of your own tips you'd like to share, you
can start a discussion in the
[Google Webmaster Help](https://support.google.com/webmasters/community)
group. Practice safe webmastering!
