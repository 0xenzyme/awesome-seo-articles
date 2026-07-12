---
title: "Musings on Down Under"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2007-05-musings-on-down-under"
url: "https://developers.google.com/search/blog/2007/05/musings-on-down-under"
canonical: "https://developers.google.com/search/blog/2007/05/musings-on-down-under"
author: "Aaron D'Souza, Software Engineer, Search Quality"
published: "2007-05-11T00:00:00+00:00"
updated: "2007-05-11T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2007_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:48:56+00:00"
status_code: 200
html_hash: "e060f4af4071b5be9ae2a2f27f468141efc35b382b3f04fe5f37ebda5f200ea5"
clean_word_count: 574
clean_char_count: 3449
---
# Musings on Down Under

Earlier this year, a bunch of Googlers (Maile, Peeyush, Dan, Adam and I) bunged ourselves across
the equator and headed to Sydney, so we could show our users and webmasters that just because
you're "down under" doesn't mean you're under our radar. We had a great time getting to know
folks at our Sydney office, and an even greater time meeting and chatting with all the people
attending [Search Summit](https://www.searchsummit.com.au/) and
[Search Engine Room](https://www.searchengineroom.com.au/).
What makes those 12-hour flights worthwhile is getting the chance to inform and be informed
about the issues important to the webmaster community.

One of the questions we heard quite frequently: Should we as webmasters/SEOs/SEMs/users be worried
about personalized search?

Our answer: a resounding NO! Personalized search takes each user's search behavior, and subtly
tunes the search results to better match their interests over time. For a user, this means that
even if you're a lone entomologist in a sea of sports fans, you'll always get the results most
relevant to you for the query "cricket". For the webmaster, it allows niche markets that collide
on the same search terms to disambiguate themselves based on individual user preferences, and
this really presents a tremendous opportunity for visibility. Also, to put things in perspective,
search engines have been moving towards some degree of personalization for years; for example,
providing country/language specific results is already a form of personalization, just at a
coarser granularity. Making it more fine-grained is the logical next step, and helps level the
playing field for smaller niche websites which now have a chance to rank well for users that want
their content the most.

Another question that popped up a lot: I'm moving my site from domain X to Y. How do I make sure
all my hard-earned reputation carries over?

Here are the important bits to think about:

- For each page on domain X, have it 301-redirect to the corresponding page on Y. (How? Typically
  through `.htaccess`, but check with your hosting provider).
- You might want to stagger the move, and redirect sub-sections of your site over time. This gives
  you the chance to keep an eye on the effects, and also gives search engines' crawl/indexing
  pipelines time to cover the space of redirected URLs.
- [https://www.google.com/webmasters](/search) is your friend. Keep an eye on it
  during the transition to make sure that the redirects are having the effect you want.
- Give it time. How quickly the transition is reflected in the results depends on how quickly we
  recrawl your site and see those redirects, which depends on a lot of factors including the
  current reputation of your site's pages.
- Don't forget to update your Sitemap. (You are using
  [Sitemaps](https://www.sitemaps.org/), aren't you?)
- If possible, don't substantially change the content of your pages at the same time you make the
  move. Otherwise, it will be difficult to tell if ranking changes are due to the change of
  content or incorrectly implemented redirects.

Before we sign off, we wanted to shout-out to a couple of the folks at the Sydney office: Lars
(one of the original Google Maps guys) gets accolades from all of us jetlagged migrants for
donating his awesome Italian espresso machine to the office. And Deepak, thanks for all your tips
on what to see and do around Sydney.
