---
title: "Domain verification using CNAME records"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2012-08-domain-verification-using-cname-records"
url: "https://developers.google.com/search/blog/2012/08/domain-verification-using-cname-records"
canonical: "https://developers.google.com/search/blog/2012/08/domain-verification-using-cname-records"
author: "Pooja Wagh, Software Engineer"
published: "2012-08-02T00:00:00+00:00"
updated: "2012-08-02T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:19:50+00:00"
status_code: 200
html_hash: "1cbc746696c5c45629e02b4942659a65a0e53e4561004f8849e34487f5b05b36"
clean_word_count: 487
clean_char_count: 2967
---
# Domain verification using CNAME records

In order to use Google services like
[Webmaster Tools](https://search.google.com/search-console)
and [Google Apps](https://www.google.com/enterprise/apps/business/)
you must verify that you own the site or domain. One way you can do this is by creating a
[DNS `TXT` record](/search/blog/2010/03/dns-verification-ftw)
to prove your ownership of the domain. Now you can also use
**DNS [`CNAME`](https://en.wikipedia.org/wiki/CNAME_record)
records** to verify ownership of your domains. This is a new domain verification option for
users that are not able to create DNS `TXT` records for their domains.

For example, if you own the domain **example.com**, you can verify your ownership of the domain
by creating a DNS `CNAME` record as follows.

1. Add the domain example.com to your account either in
   [Webmaster Tools](https://search.google.com/search-console)
   or directly on the
   [Verification Home page](https://www.google.com/webmasters/verification/).
   ![](/static/search/blog/images/archived_1_AddASite.png)
2. Select the Domain Name Provider method of verification, then select your domain name provider that
   manages your DNS records or "Other" if your provider is not on this list.
   ![](/static/search/blog/images/archived_2_image01.png)
3. Based on your selection you may either see the instructions to set a `CNAME` record or
   see a link to the option **Add a `CNAME` record**. Follow the instructions to add
   the specified `CNAME` record to your domain's DNS configuration.
   ![](/static/search/blog/images/archived_2_image00.png)
4. Click the **Verify** button.

When you click **Verify**, Google will check for the `CNAME` record and if
everything works you will be added as a verified owner of the domain. Using this method
automatically verifies you as the owner of all websites on this domain. For example, when you
verify your ownership of example.com, you are automatically verified as an owner of
www.example.com as well as subdomains such as blog.example.com.

Sometimes DNS records take a while to make their way across the Internet. If we don't find the
record immediately, we'll check for it periodically and when we find the record we'll make you a
verified owner. To maintain your verification status don't remove the record, even after
verification succeeds.

If you don't have access to your DNS configuration at your domain name provider you can continue
to use any of the other verification methods, such as the
[HTML file](https://support.google.com/webmasters/bin/answer.py?answer=35658), the
[`meta` tag](https://support.google.com/webmasters/bin/answer.py?answer=35659) or
[Google Analytics tag](https://support.google.com/webmasters/bin/answer.py?answer=185871)
in order to verify that you own a site.

If you have any questions please let us know via our
[Webmaster Help forum](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:search_console)).
