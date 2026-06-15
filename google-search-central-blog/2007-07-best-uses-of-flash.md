---
title: "Best uses of Flash"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2007-07-best-uses-of-flash"
url: "https://developers.google.com/search/blog/2007/07/best-uses-of-flash"
canonical: "https://developers.google.com/search/blog/2007/07/best-uses-of-flash"
author: "Written by Mark Berghausen, Search Quality Team"
published: "2007-07-05T00:00:00+00:00"
updated: "2007-07-05T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2007_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T12:49:20+00:00"
status_code: 200
html_hash: "3910c5e0249efd3c93ddf1446cf91c42f562182518eeff32548ce3e40f01787a"
clean_word_count: 546
clean_char_count: 3326
---
# Best uses of Flash

We occasionally get questions on the
[Webmaster Help Group](https://support.google.com/webmasters/community)
about how webmasters should work with
[Adobe Flash](https://www.adobe.com/products/flashplayer/). I thought it would be
worthwhile to write a few words about the search considerations designers should think about
when building a Flash-heavy site.

As many of you already know, Flash is inherently a visual medium, and Googlebot doesn't have
eyes. Googlebot can typically read Flash files and extract the text and links in them, but the
structure and context are missing. Moreover, textual contents are sometimes stored in Flash as
graphics, and since Googlebot doesn't currently have the algorithmic eyes needed to read these
graphics, these important keywords can be missed entirely. All of this means that even if your
Flash content is in our index, it might be missing some text, content, or links. Worse, while
Googlebot can understand some Flash files, not all Internet spiders can.

So what's an honest web designer to do? The only hard and fast rule is to show Googlebot the
exact same thing as your users. If you don't, your site risks appearing suspicious to our search
algorithms. This simple rule covers a lot of cases including
[cloaking, JavaScript redirects, hidden text, and doorway pages](/search/docs/essentials/spam-policies#cloaking).
And our engineers have gathered a few more practical suggestions:

1. Try to use Flash only where it is needed. Many rich media sites such as Google's
   [YouTube](https://www.youtube.com/)
   use Flash for rich media but rely on HTML for content and navigation. You can too, by limiting
   Flash to on-page accents and rich media, not content and navigation. In addition to making your
   site Googlebot-friendly, this makes you site accessible to a larger audience, including, for
   example, blind people using screen readers, users of old or non-standard browsers, and those on
   limited low-bandwidth connections such as on a cell phone or PDA. As a bonus, your visitors can
   use bookmarks effectively, and can email links to your pages to their friends.
2. [`sIFR`](https://en.wikipedia.org/wiki/Scalable_Inman_Flash_Replacement):
   Some websites use Flash to force the browser to display headers, pull quotes, or other textual
   elements in a font that the user may not have installed on their computer. A technique like
   `sIFR` still lets non-Flash readers read a page, since the content/navigation is
   actually in the HTML—it's just displayed by an embedded Flash object.
3. Non-Flash Versions: A common way that we see Flash used is as a front page "splash screen"
   where the root URL of a website has a Flash intro that links to HTML content deeper into the
   site. In this case, make sure there is a regular HTML link on that front page to a non-Flash
   page where a user can navigate throughout your site without the need for Flash.

If you have other ideas that don't violate these guidelines that you'd like to ask about, you
can ask them in the Webmaster Help Group under
[Crawling, Indexing, and Ranking](https://groups.google.com/group/Google_Webmaster_Help-Indexing/topics).
The many knowledgeable webmasters there, along with myself and a cadre of other Googlers, will do
our best to clear up any confusion.
