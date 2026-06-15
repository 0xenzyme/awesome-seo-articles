---
title: "Easier domain verification"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2012-06-easier-domain-verification"
url: "https://developers.google.com/search/blog/2012/06/easier-domain-verification"
canonical: "https://developers.google.com/search/blog/2012/06/easier-domain-verification"
author: "Anthony Chavez, Product Manager"
published: "2012-06-04T00:00:00+00:00"
updated: "2012-06-04T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:19:22+00:00"
status_code: 200
html_hash: "8d2caccf6ba26c1eb6a2075d208b7b9a5b34780b841345d673d34b86ee7e31ad"
clean_word_count: 520
clean_char_count: 3596
---
# Easier domain verification

Today we're announcing a new initiative that makes it easier for users to verify domains for
Google services like
[Webmaster Tools](https://google.com/webmasters/tools) and
[Google Apps](https://google.com/a).

First, some background on this initiative. To use certain Google services with your website or
domain, you currently have to
[verify](https://support.google.com/webmasters/bin/answer.py?answer=35179)
that you
[own](https://support.google.com/a/bin/answer.py?answer=60216&topic=2413164&ctx=topic)
the site or domain, since these services can share sensitive data (like
[search queries](https://support.google.com/webmasters/answer/7576553))
or operate Internet-facing services (like
[hosted email](https://www.google.com/enterprise/apps/business/products.html#gmail))
on your behalf.

One of our supported verification methods is domain verification. Currently this method requires
a user to manually create a
[DNS `TXT` record](https://support.google.com/a/bin/answer.py?answer=183895)
to prove their ownership. For many users, this can be challenging and difficult to do.

So now, in collaboration with [Go Daddy](https://www.godaddy.com/)
and [eNom](https://www.enomcentral.com/), we're introducing a simple, automated solution
for domain verification that guides you through the process in a few easy steps.

If your domain name records are managed by eNom or Go Daddy, in the Google site verification
interface you will see a new, easier verification method as shown in these screenshots:

![Domain verification in Webmaster Tools with eNom as a domain provider](/static/search/blog/images/import/24736d3f6c94e432d0801cfd030f6f96.png)
![Domain verification in Webmaster Tools with GoDaddy as a domain provider](/static/search/blog/images/import/1532d51160d43be5473da5f4c06c518b.png)

Selecting this method launches a pop-up window that asks you to log in to the provider using your
existing account with them.

![](/static/search/blog/images/import/bd5e6f46abcb8513b087c514769c52c4.png)
![](/static/search/blog/images/import/ee66eff4e3ac739286369442356abc19.png)

The first time you log in, you'll be asked to authorize the provider to access the Google site
verification service on your behalf.

![](/static/search/blog/images/import/8c47e9668eb2ee242dfb023d95a76f51.png)
![](/static/search/blog/images/import/de78069f667c99c04219786c93506b41.png)

Next you'll be asked to confirm that you wish to verify the domain.

![](/static/search/blog/images/import/922e29c42150fda3f3b21eaf7f0c3c15.png)
![](/static/search/blog/images/import/73e3660a93ab0eea034d3cccb97efbd2.png)

And that's it! After a few seconds, your domain should be automatically verified and a
confirmation message displayed.

![](/static/search/blog/images/import/3772a05b0de2d741b4765d1d6dd89242.png)
![](/static/search/blog/images/import/d791cf8474a38faa66d6947c543d690c.png)

Now eNom and Go Daddy customers can more quickly and easily verify their domains to use with
Google services like Webmaster Tools and Google Apps.

We're also happy to share that [Bluehost](https://www.bluehost.com/)
customers will be able to enjoy the same capability in the near future. And we look forward to
working with more partners to bring easier domain verification to even more users. (Interested
parties can
[contact us via this form](https://docs.google.com/a/google.com/spreadsheet/viewform?formkey=dEd3UTRKeEUxc1Jpb2x3aXdjWnFHclE6MQ#gid=0).)

If you have any questions or feedback, as always please let us know via our
[webmaster help forum](https://support.google.com/webmasters/community).
