---
title: "Will the Real <Your Site Here> Please Stand Up?"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2010-03-will-real-site-here-please-stand-up"
url: "https://developers.google.com/search/blog/2010/03/will-real-site-here-please-stand-up"
canonical: "https://developers.google.com/search/blog/2010/03/will-real-site-here-please-stand-up"
author: "Written by Colin Whittaker, Anti-Phishing Team"
published: "2010-03-30T00:00:00+00:00"
updated: "2010-03-30T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:05:31+00:00"
status_code: 200
html_hash: "940342843bd9525e078ef8bd1129b0a243c33be660c39cb23bc114b38b8a4ace"
clean_word_count: 713
clean_char_count: 4298
---
# Will the Real <Your Site Here> Please Stand Up?

![Warning sign for suspected phishing](/static/search/blog/images/import/2f81d800abc9c6db3127488eb81932b6.png)

In our recent post
[on the Google Online Security Blog](https://googleonlinesecurity.blogspot.com/2010/03/phishing-phree.html),
we described our system for identifying phishing pages. Of the millions of webpages that our
scanners analyze for phishing, we successfully identify 9 out of 10 phishing pages. Our
classification system only incorrectly flags a non-phishing site as a phishing site about 1 in
10,000 times, which is significantly better than similar systems. In our experience, these "false
positive" sites are usually built to distribute spam or may be involved with other suspicious
activity. If you find that your site has been added to our phishing page list ("Reported Web
Forgery!") by mistake, please
[report](https://www.google.com/safebrowsing/report_error/)
the error to us. On the other hand, if your site has been added to our malware list ("This site
may harm your computer"), you should follow the instructions on
[fixing issues with malware](/search/blog/2008/10/malware-we-dont-need-no-stinking).
Our team tries to address all complaints within one day, and we usually respond within a few
hours.

Unfortunately, sometimes when we try to follow up on your reports, we find that we are just as
confused as our automated system. If you run a website, here are some simple guidelines that will
allow us to quickly fix any mistakes and help keep your site off our phishing page list in the
first place.

## Don't ask for usernames and passwords that do not belong to your site.

We consider this behavior phishing by definition, so don't do it! If you want to provide an add-on
service to another site, consider using a public API or
[OAuth](https://en.wikipedia.org/wiki/Oauth) instead.

## Avoid displaying logos that are not yours near login fields.

Someone surfing the web might mistakenly believe that the logo represents your website, and they
might be misled into entering personal information into your site that they intended for the other
site. Furthermore, we can't always be sure that you aren't doing this intentionally, so we might
block your site just to be safe. To prevent misunderstandings, we recommend exercising caution
when displaying these logos.

## Minimize the number of domains used by your site, especially for logins.

Asking for a username and password for Site X looks very suspicious on Site Y. Besides making it
harder for us to evaluate your website, you may be inadvertently teaching your visitors to ignore
suspicious URLs, making them more vulnerable to actual phishing attempts. If you must have your
login page on a different domain from your main site, consider using a
[transparent proxy](https://en.wikipedia.org/wiki/Proxy_server#Transparent_and_non-transparent_proxy_server)
to enable users to access this page from your primary domain. If all else fails...

## Make it easy to find links to your pages

It is difficult for us (and for your users) to determine who controls an off-domain page in your
site if the links to that page from your main site are hard to find. All it takes to clear this
problem up is to have each off-domain page link back to an on-domain page which links to it. If
you have not done this, and one of your pages ends up on our list by mistake, please mention in
your error report how we can find the link from your main site to the wrongly blocked page.
However, if you do nothing else...

## Don't send strange links via email or IM

It's all but impossible for us to verify unusual links that only appeared in your emails or
instant messages. Worse, using these kinds of links conditions your users/customers/friends to
click on strange links they receive through email or IM, which can put them at risk for other
[Internet crimes](https://www.viruslist.com/en/virusesdescribed?chapter=153312410)
besides phishing.

While we hope you consider these recommendations to be common sense, we've seen major e-commerce
and financial companies break these guidelines from time to time. Following them will not only
improve your experience with our anti-phishing systems, but will also help provide your visitors
with a better online experience.
