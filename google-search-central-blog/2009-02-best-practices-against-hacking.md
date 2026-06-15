---
title: "Best practices against hacking"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2009-02-best-practices-against-hacking"
url: "https://developers.google.com/search/blog/2009/02/best-practices-against-hacking"
canonical: "https://developers.google.com/search/blog/2009/02/best-practices-against-hacking"
author: "Paolo Petrolini and Iris Mariano, Search Quality Team"
published: "2009-02-20T00:00:00+00:00"
updated: "2009-02-20T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2009_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T12:56:44+00:00"
status_code: 200
html_hash: "ca39fd440c2a1d0114d7f987502e3484771e4ad0fe41cb600d9e7237b4ba0831"
clean_word_count: 1573
clean_char_count: 9796
---
# Best practices against hacking

These days, the majority of websites are built around applications to provide good services to
their users. In particular, are widely used to create, edit and administrate content. Due to the
interactive nature of these systems, where the input of users is fundamental, it's important to
think about security in order to avoid exploits by malicious third parties and to ensure the best
user experience.

## Some types of hacking attempts and how to prevent them

There are many different types of attacks hackers can conduct in order to take partial or total
control of a website. In general, the most common and dangerous ones are SQL injection and
cross-site scripting (XSS).

SQL injection is a technique to inject a piece of malicious code in a web application, exploiting
a security vulnerability at the database level to change its behavior. It is a really powerful
technique, considering that it can manipulate URLs (query string) or any form (search, login,
email registration) to inject malicious code. You can find some examples of SQL injection at the
[Web Application Security Consortium](https://www.webappsec.org/projects/threat/classes/sql_injection.shtml).

There are definitely some precautions that can be taken to avoid this kind of attack. For example,
it's a good practice to add a layer between a form on the front end and the database in the back
end. In PHP, the
[PDO](https://www.php.net/pdo)
extension is often used to work with parameters (sometimes called placeholders or bind variables)
instead of embedding user input in the statement. Another really easy technique is character
escaping, where all the dangerous characters that can have a direct effect on the database
structure are escaped. For instance, every occurrence of a single quote (`'`) in a
parameter must be replaced by two single quotes (`''`) to form a valid SQL string
literal. These are only two of the most common actions you can take to improve the security of a
site and avoid SQL injections. Online you can find many other specific resources that can fit your
needs (programming languages, specific web applications ...).

The other technique that we're going to introduce here is cross-site scripting (XSS). XSS is a
technique used to inject malicious code in a webpage, exploiting security vulnerabilities of web
applications. This kind of attack is possible where the web application is processing data
obtained through user input and without any further check or validation before returning it to
the final user. You can find some examples of cross-site scripting at the
[Web Application Security Consortium](https://www.webappsec.org/projects/threat/classes/cross-site_scripting.shtml).

There are many ways of securing a web application against this technique. Some easy actions that
can be taken include:

- Stripping the input that can be inserted in a form (for example, see the
  [strip tags](https://php.net/strip-tags)
  function in PHP);
- Using data encoding to avoid direct injection of potentially malicious characters (for example,
  see the
  [htmlspecialchars](https://www.php.net/manual/en/function.htmlspecialchars.php)
  function in PHP);
- Creating a layer between data input and the back end to avoid direct injection of code in the
  application.

## Some resources about CMSs security

SQL injection and cross-site scripting are only two of the many techniques used by hackers to
attack and exploit innocent sites. As a general security guideline, it's important to always stay
updated on security issues and, in particular when using third party software, to make sure you've
installed the latest available version. Many web applications are built around big communities,
offering constant support and updates.

To give a few examples, four of the biggest communities of Open Source content management
systems—Joomla, WordPress, PHP-Nuke, and Drupal—offer useful guidelines on security on their
websites and host big community-driven forums where users can escalate issues and ask for support.
For instance, in the
[Hardening WordPress](https://codex.wordpress.org/Hardening_WordPress)
section of its website, WordPress offers comprehensive documentation on how to strengthen the
security of its CMS. Joomla offers many resources regarding security, in particular a
[Security Checklist](https://docs.joomla.org/Category:Security_Checklist)
with a comprehensive list of actions webmasters should take to improve the security of a website
based on Joomla. On Drupal's site, you can access information about security issues by going to
their
[Security section](https://drupal.org/security).
You can also subscribe to their security mailing list to be constantly updated on ongoing issues.
PHP-Nuke offers some documentation about
[Security](https://phpnuke.org/modules.php?name=PHP-Nuke_HOWTO&page=security)
in chapter 23 of their "How to" section, dedicated to the system management of this CMS platform.
They also have a section called
[Hacked - Now what?](https://phpnuke.org/modules.php?name=PHP-Nuke_HOWTO&page=hacked-now-what)
that offers guidelines to solve issues related to hacking.

## Some ways to identify the hacking of your site

As mentioned above, there are many different types of attacks hackers can perform on a site, and
there are different methods of exploiting an innocent site. When hackers are able to take complete
control of a site, they can deface it (changing the home page), erase all the content (dropping the
tables of your database), or insert malware or cookie stealers. They can also exploit a site for
spamming, such as by hiding links pointing to spammy resources or creating pages that redirect to
malware sites. When these changes in your application are evident (like defacing), you can easily
spot the hacking activity; but for other types of exploits, in particular those with spammy
intent, it won't be so obvious. Google, through some of its products, offers webmasters some ways
of spotting if a site has been hacked or modified by a third party without permission. For
example, by using Google Search you can spot typical keywords added by hackers to your website and
identify the pages that have been compromised. Just open
[google.com](https://www.google.com/) and run a `site:`
search query on your website, looking for commercial keywords that hackers commonly use for
spammy purposes (such as viagra, porn, mp3, gambling, etc.): `site:example.com viagra`.
If you're not already familiar with the `site:` search operator, it's a way to query
Google by restricting your search to a specific site. For example, the search
[site:googleblog.blogspot.com](https://www.google.com/search?q=site%3Agoogleblog.blogspot.com)
will only return results from the
[Official Google Blog](https://googleblog.blogspot.com/).
When adding spammy keywords to this type of query, Google will return all the indexed pages of
your website that contain those spammy keywords and that are, with high probability, hacked. To
check these suspicious pages, just open the cached version proposed by Google and you will be able
to spot the hacked behavior, if any. You could then clean up your compromised pages and also check
for any anomalies in the configuration files of your server (for example on Apache web servers:
`.htaccess` and `httpd.conf`).

If your site doesn't show up in Google's search results anymore, it could mean that Google has
already spotted bad practices on your site as a result of the hacking and may have temporarily
removed it from our index, due to infringement of our
[webmaster quality guidelines](/search/docs/essentials#quality).

In order to constantly keep an eye on the presence of suspicious keywords on your website, you
could also use
[Google Alerts](https://www.google.com/alerts)
to monitor queries like `site:example.com viagra OR casino OR porn OR ringtones`. You
will receive an email alert whenever these keywords are found in the content of your site.

You can also use Google's
[Webmaster Tools](https://search.google.com/search-console)
to spot any hacking activity on your site. Webmaster Tools provide statistics about top search
queries for your site. This data will help you to monitor if your site is ranking for suspicious
unrelated spammy keywords. The 'What Googlebot sees' data is also useful, since you'll see whether
Google is detecting any unusual keywords on your site, regardless of whether you're ranking for
them or not.

If you have a Webmaster Tools account and Google believes that your site has been hacked, often
you will be notified according to the type of exploit on your site:

- If a malicious third party is using your site for spammy behaviors (such as hiding links or
  creating spammy pages) and it has been detected by our crawler, often you will be notified in
  the Message Center with detailed information (a sample of hacked URLs or anchor text of the
  hidden links);
- If your site is exploited to place malicious software such as malware, you will see a malware
  warning on the 'Overview' page of your Webmaster Tools account.

## Hacked behavior removed, now what?

Your site has been hacked or is serving malware? First, clean up the malware mess and then do one
of the following:

- If your site was hacked for spammy purpose, please visit our
  [reconsideration request](https://www.google.com/webmasters/tools/reconsideration)
  page through Webmaster Tools to request reconsideration of your site;
- If your site was serving malware to users, please submit a malware review request on the
  'Overview' page of Webmaster Tools.

We hope that you'll find these tips helpful. If you'd like to share your own advice or experience,
we encourage you to
[post in our forum](https://support.google.com/webmasters/community).
Thanks!
