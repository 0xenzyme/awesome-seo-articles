---
title: "More on 404"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-08-now-that-weve-bid-farewell-to-soft-404s"
url: "https://developers.google.com/search/blog/2008/08/now-that-weve-bid-farewell-to-soft-404s"
canonical: "https://developers.google.com/search/blog/2008/08/now-that-weve-bid-farewell-to-soft-404s"
author: "Maile Ohye"
published: "2008-08-15T00:00:00+00:00"
updated: "2008-08-15T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:53:52+00:00"
status_code: 200
html_hash: "013eb85f4b1194954f72255b270e643d2ce5fc90e5adc11ac128ea7aff08bbdd"
clean_word_count: 673
clean_char_count: 4781
---
# More on 404

Now that we've
[bid farewell to `soft 404` errors](/search/blog/2008/08/farewell-to-soft-404s),
in this post for [`404` week](/search/blog/2008/08/its-404-week-at-webmaster-central)
we'll answer your burning `404` questions.

**How do you treat the response code `410 "Gone"`?**
Just like a `404`.

**Do you index content or follow links from a page with a `404` response code?**

We aim to understand as much as possible about your site and its content. So while we wouldn't
want to show a hard `404` to users in search results, we may utilize a `404`
error page's content or links if it's detected as a signal to help us better understand your site.

Keep in mind that if you want links crawled or content indexed, it's far more beneficial to
include them in a page that's not `404`.

**What about `404` errors with a 10-second `meta refresh`?**

Yahoo! currently utilizes this method on their `404` errors. They
[respond with a `404`](https://www.yahoo.com/this-is-a-404),
but the `404` content also shows:
`<meta http-equiv="refresh" content="10;url=https://www.yahoo.com/?xxx" />`. We feel
this technique is fine because it reduces confusion by giving users 10 seconds to make a new
selection, only offering the home page after 10 seconds without the user's input.

**Should I `301` redirect misspelled `404` errors to the correct URL?**

Redirecting with `301` status `404` errors is a good idea when it's helpful
to users (that is, not confusing like `soft 404` errors). For instance, if you notice
that the
[Crawl Errors](https://support.google.com/webmasters/answer/9679690)
of Webmaster Tools shows a `404` for a misspelled version of your URL, you can
`301` the misspelled version of the URL to the correct version.

For example, if we saw this `404` in Crawl Errors:

```
https://www.google.com/webmsters <-- typo for "webmasters"
```

we may first correct the typo if it exists on our own site, then `301` the URL to the
correct version (as the broken link may occur elsewhere on the web):

```
https://www.google.com/webmasters
```

**Have you seen any good `404` errors?**

Yes, we have! (Confession: no one asked us this question, but few things are as fun to discuss as
response codes. :) We've put together a list of some of our favorite
`404` pages. If you have more `404` related questions, let us know, and
thanks for joining us for `404`
week!

> <https://www.metrokitchen.com/nice-404-page>:
> "If you're looking for an item that's no longer stocked (as I was), this makes it really easy
> to find an alternative."
> -
> [Riona](https://groups.google.com/groups/profile?enc_user=79Xl0DkAAAC0ZCEBAysSlShC_gPAdXUZZqg6TSmQIkXp0m5Qj12ma11TBTVYeFVkXW5wWwZyLtfjxVrrD5b9FzF5fEAvsymn),
> domestigeek
>
> <https://www.comedycentral.com/another-404>:
> "Blame the robot monkeys"
> -
> [Reid](https://groups.google.com/groups/profile?enc_user=InJR3DEAAAC0ZCEBAysSlShC_gPAdXUZxKBCyK9bzhy2GlsLkl4w2GXYtvvNIRI-oLWowSE9_jA77j2jf7J8ZFK392Ir2mQh),
> tells really bad jokes
>
> <https://www.splicemusic.com/and-another>:
> "Boost your 'Time on site' metrics with a `404` page like this."
> -
> [Susan](https://groups.google.com/groups/profile?enc_user=bfiHVTYAAAC0ZCEBAysSlShC_gPAdXUZVBJwbVrQrjnMBIELTfghYz0h8XMSxFluWFJdWS1BQ425JCaQw8q0rq28lNpPHZyv),
> dabbler in music and Analytics
>
> <https://www.treachery.net/wow-more-404s>:
> "It's not reassuring, but it's definitive."
> -
> [Jonathan](https://groups.google.com/groups/profile?enc_user=7R709zkAAAC0ZCEBAysSlShC_gPAdXUZ6pC83CPQcZTBRk4tCi5-z22zvE-Pg6zMb-JWoHM21aHjxVrrD5b9FzF5fEAvsymn),
> has trained actual spiders to build websites, ants handle the `404` errors
>
> <https://www.apple.com/iPhone4g>:
> "Good with respect to usability."
> <https://thcnet.net/lost-in-a-forest>:
> "At least there's a mailbox."
> -
> [JohnMu](https://groups.google.com/groups/profile?enc_user=lM-UKDAAAAC0ZCEBAysSlShC_gPAdXUZmjqRmRterNa8Oz21qsjVgj_wknTYgk2leeKLmFFGg7s),
> adventurous
>
> <https://lookitsme.co.uk/404>:
> "It's pretty cute. :)"
> -
> [Jessica](https://groups.google.com/groups/profile?enc_user=s6jB9DQAAAC0ZCEBAysSlShC_gPAdXUZ0gHXGLPrDpaxMgsW8m29Qsepl5x9hu-gpjd2BaCfTLFTofQ0MIAkuDMa7lXaxMYO),
> likes cute things
>
> [https://www.orangecoat.com/a-404-page.html](https://www.orangecoat.com/a-404-page):
> "Flow charts rule."
> -
> [Sahala](https://www.blogger.com/profile/75825),
> internet traveller
>
> <https://icanhascheezburger.com/iz-404-page>:
> "I can has useful links and even e-mail address for questions! But they could have added 'OH
> NOES! IZ MISSING PAGE! MAYBE TIPO OR BROKN LINKZ?' so folks'd know what's up."
> -
> [Adam](https://groups.google.com/groups/profile?enc_user=Cc3iUTUAAAC0ZCEBAysSlShC_gPAdXUZ6uYgiBXIh5DaeqWCtoTJbOW2QCIjchDn6OYwMZe7JK3IgJw9QHTrXt9e__Js8L8H),
> lindy hop geek
