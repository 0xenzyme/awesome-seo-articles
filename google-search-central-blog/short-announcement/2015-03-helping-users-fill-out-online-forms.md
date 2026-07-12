---
title: "Helping users fill out online forms"
source: google-search-central-blog
content_type: "short_announcement"
freshness_risk: "historical"
slug: "2015-03-helping-users-fill-out-online-forms"
url: "https://developers.google.com/search/blog/2015/03/helping-users-fill-out-online-forms"
canonical: "https://developers.google.com/search/blog/2015/03/helping-users-fill-out-online-forms"
author: "Zineb Ait Bahajji"
published: "2015-03-17T00:00:00+00:00"
updated: "2015-03-17T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2015_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:26:19+00:00"
status_code: 200
html_hash: "92fa5deb205a8a7e3b2dfcae4dedae237bb2f23bba9219f98b1d5f77242d2fe7"
clean_word_count: 329
clean_char_count: 2160
---
# Helping users fill out online forms

A lot of websites rely on forms for important goals completion, such as completing a transaction
on a shopping site or registering on a news site. For many users, online forms mean repeatedly
typing common information like their names, emails, phone numbers or addresses, on different sites
across the web. In addition to being tedious, this task is also error-prone, which can lead many
users to abandon the flow entirely. In a world where users browse the internet using their mobile
devices more than their laptops or desktops, having forms that are easy and quick to fill out is
crucial! Three years ago, we announced the support for a new "autocomplete" attribute in Chrome,
to
[make form-filling faster, easier and smarter](/search/blog/2012/01/making-form-filling-faster-easier-and).
Now, Chrome fully supports the `autocomplete` attribute for form fields according to
the current
[WHATWG HTML Standard](https://html.spec.whatwg.org/multipage/forms.html#autofill).
This allows webmasters and web developers to label input element fields with common data types,
such as `name` or `street-address`, without changing the user interface or
the backend. Numerous webmasters have increased the rate of form completions on their sites by
marking up their forms for auto-completion.

For example, marking up an email address field on a form to allow auto-completion would look like
this (with a
[full sample form](https://googlesamples.github.io/web-fundamentals/samples/input/form/order)
available): `<input type="email" name="customerEmail" autocomplete="email" />`

![](/static/search/blog/images/import/d479f37905b32e807aab0aa806700022.png)

Making websites friendly and easy to browse for users on mobile devices is very important. We hope
to see many forms marked up with the `autocomplete` attribute in the future. For more
information, you can check out our specifications about
[Label and name inputs](/web/fundamentals/input/form/label-and-name-inputs)
in Web Fundamentals. And as usual, if you have any questions, please post in our
[Webmasters Help Forums](https://support.google.com/webmasters/go/community).
