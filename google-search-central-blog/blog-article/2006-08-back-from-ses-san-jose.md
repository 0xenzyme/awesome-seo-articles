---
title: "Back from SES San Jose"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2006-08-back-from-ses-san-jose"
url: "https://developers.google.com/search/blog/2006/08/back-from-ses-san-jose"
canonical: "https://developers.google.com/search/blog/2006/08/back-from-ses-san-jose"
author: null
published: "2006-08-16T00:00:00+00:00"
updated: "2006-08-16T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2006_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:46:02+00:00"
status_code: 200
html_hash: "de34c9a39577ba666f943d253110c47866a4a4c44f1720689087e76f771bca6f"
clean_word_count: 857
clean_char_count: 5119
---
# Back from SES San Jose

Thanks to everyone who stopped by to say hi at the
[Search Engine Strategies conference in San Jose](https://www.searchenginestrategies.com/sew/summer06/)
last week!

I had a great time meeting people and talking about our new Webmaster Tools. I got to hear a lot
of feedback about what webmasters liked, didn't like, and wanted to see in our
[Webmaster Central](/search) site. For those of you who couldn't make it or didn't
find me at the conference, you can post your comments and suggestions in our
[discussion group](https://support.google.com/webmasters/community).
I do want to hear about what you don't understand or what you want changed so I can make our
Webmaster Tools as useful as possible.

Some of the highlights from the week:

This year, Danny Sullivan invited some of us from the team to "chat and chew" during a lunch
hour panel discussion. Anyone interested in hearing about Google's Webmaster Tools was welcome
to come and many did—thanks for joining us! I loved showing off our product, answering
questions, and getting feedback about what to work on next. Many people had already tried
Sitemaps, but hadn't seen the new features like
[Preferred domain](https://www.google.com/support/webmasters/bin/answer.py?answer=44231&topic=9025)
and
[full crawling errors](/search/blog/2006/08/more-webmaster-tools).

One of the questions I heard more than once at the lunch was about how big a Sitemap can be,
and how to use Sitemaps with very large websites. Since Google can handle all of your URLs, the
goal of Sitemaps is to tell us about all of them. A Sitemap file can contain up to 50,000 URLs
and should be no larger than 10MB when uncompressed. But if you have more URLs than this, simply
break them up into several smaller Sitemaps and tell us about them all. You can create a
[Sitemap Index file](/search/docs/crawling-indexing/sitemaps/large-sitemaps), which is
just a list of all your Sitemaps, to make managing several Sitemaps a little easier.

While hanging out at the Google booth I got another interesting question: One site owner told
me that their site is listed in Google, but its description in the search results wasn't exactly
what they wanted. (We were using the description of their site listed in the
[Open Directory Project](https://www.dmoz.org/).)
They asked how to remove this description from Google's search results.
[Vanessa Fox knew the answer](/search/blog/2006/07/more-control-over-page-snippets)!
To specifically prevent Google from using the Open Directory for a page's title and description,
[use the following `meta` tag](/search/docs/crawling-indexing/special-tags):

```
<meta name="GOOGLEBOT" content="NOODP" />
```

My favorite panel of the week was definitely
[Pimp My Site](https://www.searchenginestrategies.com/sew/summer06/agenda3.html#445-5).
The whole group was dressed to match the theme as they gave some great advice to webmasters.
[Dax Herrera](https://www.webguerrilla.com/), the coolest "pimp" up
there (and a fantastic piano player), mentioned that a lot of sites don't explain their product
clearly on each page. For instance, when pimping
[Flutter Fetti](https://www.flutterfetti.com/), there were many
instances when all the site had to do was add the word "confetti" to the product description to
make it clear to search engines and to users reaching the page exactly what a Flutter Fetti
stick is.

Another site pimped was a
[Yahoo! Stores](https://smallbusiness.yahoo.com/merchant/) web
site. Someone from the audience asked if the webmaster could set up a Google Sitemap for their
store. As [Rob Snell](https://www.robsnell.com/) pointed out, it's
very simple: Yahoo! Stores will
[create a Google Sitemap](/search/blog/2006/06/yahoo-merchants-get-sitemaps)
for your website automatically, and even verify your ownership of the site in our Webmaster Tools.

Finally, if you didn't attend the Google dance, you missed out! There were Googlers dancing,
eating, and having a great time with all the conference attendees. Vanessa Fox represented my team
at the Meet the Google Engineers hour that we held during the dance, and I heard Matt Cutts even
starred in a music video! While demo-ing Webmaster Central over in the labs area, someone asked me
about the ability to share site information across multiple accounts. We associate your
[site verification](https://support.google.com/webmasters/answer/9008080)
with your Google Account, and allow multiple accounts to verify ownership of a site independently.
Each account has its own verification file or `meta` tag, and you can remove them at any time and
re-verify your site to revoke verification of a user. This means that your marketing person, your
techie, and your SEO consultant can each verify the same site with their own Google Account. And
if you start managing a site that someone else used to manage, all you have to do is add that site
to your account and verify site ownership. You don't need to transfer the account information from
the person who previously managed it.

Thanks to everyone who visited and gave us feedback. It was great to meet you!
