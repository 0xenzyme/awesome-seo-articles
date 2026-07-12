---
title: "DNS Verification FTW"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2010-03-dns-verification-ftw"
url: "https://developers.google.com/search/blog/2010/03/dns-verification-ftw"
canonical: "https://developers.google.com/search/blog/2010/03/dns-verification-ftw"
author: "Sean Harding, Software Engineer"
published: "2010-03-31T00:00:00+00:00"
updated: "2010-03-31T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:05:08+00:00"
status_code: 200
html_hash: "8b35e090b48334a8d2b50610f6af2a2c111f6c269e1c72edf1fb02f47aacf5b7"
clean_word_count: 489
clean_char_count: 3080
---
# DNS Verification FTW

A few weeks ago, we
[introduced a new way of verifying site ownership](/search/blog/2010/03/sharing-verification-love),
making it easy to share verified ownership of a site with another person. This week, we bring you
another new way to verify. Verification by DNS record allows you to become a verified owner of an
entire domain (and all of the sites within that domain) at once. It also provides an alternative
way to verify for folks who struggle with the existing HTML file or `meta` tag methods.

I like to explain things by walking through an example, so let's try using the new verification
method right now. For the sake of this example, we'll say I own the domain
example.com. I have several websites under example.com, including https://www.example.com/,
https://blog.example.com/ and https://beta.example.com/. I could individually verify ownership of
each of those sites using the `meta` tag or HTML file method. But that means I'd need to go through
the verification process three times, and if I wanted to add https://customers.example.com/, I'd
need to do it a fourth time. DNS record verification gives me a better way!

First I'll add example.com to my account, either in
[Webmaster Tools](https://search.google.com/search-console)
or directly on the
[Verification Home page](https://www.google.com/webmasters/verification/).

![Webmaster Tools verification feature](/static/search/blog/images/import/91a18c1dd15d700a1600d9fac1af6b59.png)

On the verification page, I select the "Add a DNS record" verification method, and follow the
instructions to add the specified TXT record to my domain's DNS configuration.

![](/static/search/blog/images/import/09a25242f9125951236c66b3e9c7fd8d.png)
![](/static/search/blog/images/import/be31f779e8ce43ee63413da8fa341330.png)

When I click "Verify," Google will check for the `TXT` record, and if it's present,
I'll be a verified owner of example.com and any associated websites and subdomains. Now I can use
any of those sites in Webmaster Tools and other verification-enabled Google products without
having to verify ownership of them individually.

If you try DNS record verification and it doesn't work right away, don't despair!

![An error message warning about a failed DNS verification](/static/search/blog/images/import/2d3ec8743710795beb9f9ee03b01b7a9.png)

Sometimes DNS records take a while to make their way across the Internet, so Google may not see
them immediately. Make sure you've added the record exactly as it's shown on the verification
page. We'll periodically check, and when we find the record we'll make you a verified owner
without any further action from you.

DNS record verification isn't for everyone—if you don't understand DNS configuration, we recommend
you continue to use the HTML file and `meta` tag methods. But for advanced users, this is a
powerful new option for verifying ownership of your sites.

As always, please visit the
[Webmaster Help Forum](https://support.google.com/webmasters/community/label?lid=1a96dcd3ad5ea81e&hl=en)
if you have any questions.
