---
title: "#NoHacked 3.0: How do I know if my site is hacked?"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2017-12-nohacked-30-how-do-i-know-if-my-site-is"
url: "https://developers.google.com/search/blog/2017/12/nohacked-30-how-do-i-know-if-my-site-is"
canonical: "https://developers.google.com/search/blog/2017/12/nohacked-30-how-do-i-know-if-my-site-is"
author: null
published: "2017-12-08T00:00:00+00:00"
updated: "2017-12-08T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2017_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:31:21+00:00"
status_code: 200
html_hash: "0919f01461bccf42e2c1353563b4482a0ed400ad7e894f050dc89fc416ec751c"
clean_word_count: 804
clean_char_count: 5264
---
# #NoHacked 3.0: How do I know if my site is hacked?

Last week #NoHacked is back on our
[G+](https://plus.google.com/+GoogleWebmasters) and
[Twitter](https://twitter.com/googlesearchc) channels! #NoHacked is
our social campaign which aims to bring awareness about hacking attacks and offer tips on how to
keep your sites safe from hackers. This time we would like to start sharing content from #NoHacked
campaign on this blog in your local language!

![](/static/search/blog/images/import/2b539f957e4c8ce78d5f8b6326be564e.png)

Why do sites get hacked? Hackers have
[different motives for compromising a website](/web/fundamentals/security/hacked/FAQs_for_hacked_sites),
and hack attacks can be very different, so they are not always easily detected. Here are some tips
which will help you in detecting hacked sites!

- **Getting started:**

  ![](/static/search/blog/images/import/a6183bc0ae2b36401e7af7f6fae0cecd.png)

  Start with our guide "How do I know if my site is hacked?" if you've received a security alert
  from Google or another party.
  [This guide](/web/fundamentals/security/hacked/how_do_I_know_if_site_hacked)
  will walk you through basic steps to check for any signs of
  compromises on your site.
- **Understand the alert on Google Search:**

  ![](/static/search/blog/images/import/e233d42366b847d7456838d98ca414b8.png)

  At Google, we have different processes to deal with hacking scenarios. Scanning tools will often
  detect malware, but they can miss some spamming hacks. A clean verdict from Safe Browsing does
  not mean that you haven't been hacked to distribute spam.

  - If you ever see
    ["This site may be hacked"](https://support.google.com/websearch/answer/190597),
    your site may have been hacked to display spam. Essentially, your site has been hijacked to
    serve some advertising.
  - If you see
    ["This site may harm your computer"](https://support.google.com/websearch/answer/45449)
    beneath the site URL then we think the site you're about to visit might allow programs to
    install malicious software on your computer.
  - If you see a big red screen before your site, that can mean a
    [variety of things](https://support.google.com/chrome/answer/99020):
    - If you see "The site ahead contains malware", Google has detected that your site
      distributes [malware](/search/docs/monitor-debug/security/malware).
    - If you see "The site ahead contains harmful programs", then the site has been flagged
      for distributing
      [unwanted software](https://www.google.com/about/unwanted-software-policy.html).
    - "Deceptive site ahead" warnings indicate that your site may be serving
      [phishing or social engineering](/search/docs/monitor-debug/security/social-engineering).
      Your site could have been hacked to do any of these things.
- **Malvertising vs Hack:**

  ![](/static/search/blog/images/import/b2b83e270d91b2936015db7f8100c149.png)

  Malvertising happens when your site loads a bad ad. It may make it seem as though your site
  has been hacked, perhaps by redirecting your visitors, but in fact is just an ad behaving
  badly.
- **Open redirects: check if your site is enabling open redirects**

  ![](/static/search/blog/images/import/93c9826c261abc9d172b954b351f0852.png)

  Hackers might want to take advantage of a good site to mask their URLs. One way they do this
  is by using open redirects, which allow them to use your site to redirect users to any URL of
  their choice. You can read more about
  [unvalidated redirects and forwards](https://www.owasp.org/index.php/Unvalidated_Redirects_and_Forwards_Cheat_Sheet).
- **Mobile check: make sure to view your site from a mobile browser in incognito mode.
  Check for bad mobile ad networks.**

  ![](/static/search/blog/images/import/f1496b565a8560c30bbdb3985cdd2f87.png)

  Sometimes bad content like ads or other third-party elements
  [unknowingly redirect mobile users](https://support.google.com/webmasters/answer/6388720).
  This behavior can easily escape detection because it's only visible from certain browsers. Be
  sure to check that the mobile and desktop versions of your site show the same content.
- **Use Search Console and get message:**

  ![](/static/search/blog/images/import/450dc041989cad1b2f041edd18f81ee8.png)

  Search Console is a tool that Google uses to communicate with you about your website. It also
  includes many other tools that can help you improve and manage your website. Make sure you have
  your site
  [verified in Search Console](https://support.google.com/webmasters/answer/35179)
  even if you aren't a primary developer on your site. The alerts and messages in Search Console
  will let you know if Google has detected any critical errors on your site.

If you're still unable to find any signs of a hack, ask a security expert or post on
[our Webmaster Help Forums](https://support.google.com/webmasters/community/)
for a second look.

The #NoHacked campaign will run for the next 3 weeks. Follow us on our
[G+](https://plus.google.com/+GoogleWebmasters) and
[Twitter](https://twitter.com/googlesearchc) channels or look out for
the content in this blog as we will be posting summary for each week right here at the beginning
of each week! Stay safe meanwhile!
