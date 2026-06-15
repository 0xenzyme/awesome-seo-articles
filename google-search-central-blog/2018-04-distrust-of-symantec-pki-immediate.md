---
title: "Distrust of the Symantec PKI: Immediate action needed by site operators"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2018-04-distrust-of-symantec-pki-immediate"
url: "https://developers.google.com/search/blog/2018/04/distrust-of-symantec-pki-immediate"
canonical: "https://developers.google.com/search/blog/2018/04/distrust-of-symantec-pki-immediate"
author: "Devon O'Brien, Ryan Sleevi, Emily Stark, Chrome security team"
published: "2018-04-04T00:00:00+00:00"
updated: "2018-04-04T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2018_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:32:07+00:00"
status_code: 200
html_hash: "46c5eab9f04327cdd747021a3fd400305b7842b58780f1564c340b62b9e247dd"
clean_word_count: 809
clean_char_count: 5228
---
# Distrust of the Symantec PKI: Immediate action needed by site operators

Cross-posted from the
[Google Security Blog](https://security.googleblog.com/2018/03/distrust-of-symantec-pki-immediate.html).

We
[previously announced](https://security.googleblog.com/2017/09/chromes-plan-to-distrust-symantec.html)
plans to deprecate Chrome's trust in the Symantec certificate authority (including Symantec-owned
brands like Thawte, VeriSign, Equifax, GeoTrust, and RapidSSL). This post outlines how site
operators can determine if they're affected by this deprecation, and if so, what needs to be done
and by when. Failure to replace these certificates will result in site breakage in upcoming
versions of major browsers, including Chrome.

## Chrome 66

If your site is using a SSL/TLS certificate from Symantec that was issued before June 1, 2016, it
will stop functioning in Chrome 66, which could already be impacting your users.

If you are uncertain about whether your site is using such a certificate, you can preview these
changes in
[Chrome Canary](https://www.google.com/chrome/browser/canary) to see
if your site is affected. If connecting to your site displays a certificate error or a warning in
DevTools as shown below, you'll need to replace your certificate. You can get a new certificate
from any
[trusted CA](https://www.chromium.org/Home/chromium-security/root-ca-policy),
including Digicert, which recently acquired Symantec's CA business.

![An example of a certificate error that Chrome 66 users might see](/static/search/blog/images/import/b4f33c9f9034d08015cf3ada5b69360a.png)

An example of a certificate error that Chrome 66 users might see if you are using a Legacy
Symantec SSL/TLS certificate that was issued before June 1, 2016.

![The DevTools message explaining you need to replace your certificate before Chrome 66.](/static/search/blog/images/import/5eb18af52e0bbb406682afefe0f23455.png)

The DevTools message you will see if you need to replace your certificate before Chrome 66.

Chrome 66 has already been released to the Canary and Dev channels, meaning affected sites are
already impacting users of these Chrome channels. If affected sites do not replace their
certificates by **March 15, 2018**, Chrome Beta users will begin experiencing the failures as
well. You are strongly encouraged to replace your certificate as soon as possible if your site is
currently showing an error in Chrome Canary.

## Chrome 70

Starting in Chrome 70, all remaining Symantec SSL/TLS certificates will stop working, resulting in
a certificate error like the one shown above. To check if your certificate will be affected, visit
your site in Chrome today and open up DevTools. You'll see a message in the console telling you if
you need to replace your certificate.

![The DevTools message explaining you need to replace your certificate before Chrome 70.](/static/search/blog/images/import/69610b63f65ba1fd0764640f1cbfb722.png)

The DevTools message explaining you need to replace your certificate before Chrome 70.

If you see this message in DevTools, you'll want to replace your certificate as soon as possible.
If the certificates are not replaced, users will begin seeing certificate errors on your site as
early as **July 20, 2018**. The first Chrome 70 Beta release will be around September 13, 2018.

## Expected Chrome Release Timeline

The table below shows the First Canary, First Beta and Stable Release for Chrome 66 and 70. The
first impact from a given release will coincide with the First Canary, reaching a steadily
widening audience as the release hits Beta and then ultimately Stable. Site operators are strongly
encouraged to make the necessary changes to their sites before the First Canary release for Chrome
66 and 70, and no later than the corresponding Beta release dates.

|  |  |  |  |
| --- | --- | --- | --- |
| Release | First Canary | First Beta | Stable Release |
| Chrome 66 | January 20, 2018 | ~ March 15, 2018 | ~ April 17, 2018 |
| Chrome 70 | ~ July 20, 2018 | ~ September 13, 2018 | ~ October 16, 2018 |

For information about the release timeline for a particular version of Chrome, you can also refer
to the
[Chromium Development Calendar](https://www.chromium.org/developers/calendar)
which will be updated should release schedules change.

In order to address the needs of certain enterprise users, Chrome will also implement an
Enterprise Policy that allows disabling the Legacy Symantec PKI distrust starting with Chrome 66.
As of January 1, 2019, this policy will no longer be available and the Legacy Symantec PKI will be
distrusted for all users.

## Special Mention: Chrome 65

As noted in the
[previous announcement](https://security.googleblog.com/2017/09/chromes-plan-to-distrust-symantec.html),
SSL/TLS certificates from the Legacy Symantec PKI issued after December 1, 2017 are no longer
trusted. This should not affect most site operators, as it requires entering in to special
agreement with DigiCert to obtain such certificates. Accessing a site serving such a certificate
will fail and the request will be blocked as of Chrome 65. To avoid such errors, ensure that such
certificates are only served to legacy devices and not to browsers such as Chrome.
