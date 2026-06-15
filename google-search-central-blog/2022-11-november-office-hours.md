---
title: "November Google SEO Office Hours"
source: google-search-central-blog
content_type: "event"
freshness_risk: "historical"
slug: "2022-11-november-office-hours"
url: "https://developers.google.com/search/blog/2022/11/november-office-hours"
canonical: "https://developers.google.com/search/blog/2022/11/november-office-hours"
author: "John Mueller"
published: "2022-11-29T00:00:00+00:00"
updated: "2022-11-29T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2022_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:41:07+00:00"
status_code: 200
html_hash: "744edb960eddedd645f853594f64a22029e021fd776a59b119a0f6aecdf7acc8"
clean_word_count: 5624
clean_char_count: 32790
---
# November Google SEO Office Hours

Thanks to everyone who submitted questions for the November edition of the Google SEO office hours!
In this episode, you'll hear answers from folks on the Google Search team: Gary Illyes,
Lizzi Sassman, John Mueller, Alan Kent, and Duy Nguyen. You can check out the
[full recording on our YouTube channel](https://www.youtube.com/watch?v=TepFVYrBVg0),
and we're also publishing the transcript of the questions for easier reference in this blog post.

We've been experimenting with how we do [office hours](https://www.youtube.com/playlist?list=PLKoqnv2vTMUMqH8IyzOMBc_Z8i-S6-tVJ)
over the past few months, so you may see us trying variations over time. The goal is to make it
easier to publish these and for other people on the Google Search team to contribute answers, so
the overhead for publishing these is kept at a minimum. We're currently aiming to publish this
audio-only format on a monthly cadence.

Want to submit your question for the December edition of Google SEO office hours? The form is open
and you can [submit a question](/search/help/office-hours)
for next month's edition. We recommend focusing on general questions
related to Google Search and SEO; if you have a specific question about your website, the
[Google Search Central Forum](https://support.google.com/webmasters/community)
is the best place to go for site-specific help.

How did you like the new setup? Drop us a note with the **Send Feedback** button
on this blog post or on the [YouTube video](https://www.youtube.com/watch?v=TepFVYrBVg0)
with your comments!

---

## Can we use multiple values in one schema markup field using comma separation?

**Lizzi**: Abhishek is asking, "Can we use multiple values in one schema markup field using
comma separation? For example, GTIN equals value one, value two".

Well, as always, you should check the documentation for the particular feature because some
of the guidance might differ from feature to feature. But in general, it's a good markup practice
to specify one value per field. In the case of GTIN, there should only really be one value, since
this is a unique product identifier. If you're specifying a GTIN and ISBN, then use the GTIN, and
then the ISBN property, so that we know which value applies to which property.

## What are the options to use the disavow feature in Search Console for domain properties?

**John**: Pierre asks: "The disavow feature in Search Console is currently unavailable for
domain properties. What are the options then?"

Well, if you have domain level verification in place, you can verify the prefix level without
needing any additional tokens. Verify that host and do what you need to do. Also, keep in mind
that disavowing random links that look weird or that some tool has flagged, is not a good use
of your time. It changes nothing. Use the disavow tool for situations where you actually paid for
links and can't get them removed afterwards.

## How bad is the helpful content update for sites accepting guest posts for money?

**Duy**: Hello, this is Duy recording for SEO Office Hours. Latha asked, "How bad is the helpful
content update for sites accepting guest posts for money?"

Our systems can identify sites with low value, low quality content, or content created just for
search engines. Sites accepting guest posts for money without carefully vetting content and links
risk ranking lowering service results, not just because of the helpful content update, but also
because of the other systems that we already put in place.

## What to do when Google does not detect the canonical tag correctly?

**John**: "What to do when Google does not detect the canonical tag correctly?"

So taking a step back, canonicalization is based on more than only the `link` `rel="canonical"` element.
When Google discovers URLs that are significantly alike, our systems try to pick one URL that best
represents the content. For that we take into account not only the `link` `rel="canonical"`, but also
redirects, sitemaps, internal links, external links, and more. If you have strong feelings about
which URL should be used, then make sure that all of your signals align. Keep in mind that canonicalization
is mostly about which URL is shown. It's not something that affects the ranking of the content.

## Is Google more likely to crawl and index the pages if the content is short?

**Gary**: "If a site has a directory covering on each topic, which isn't searched for very often,
is Google more likely to crawl and index the pages if the content is short, and so it's cheaper
to store it in the index."

This is an interesting question. The length of the content doesn't influence how often we crawl
and whether we index it. It also doesn't contribute to the crawl rate of a URL pattern. Niche
content can also be indexed. It's not in any way penalized, but generally content, that's popular
on the internet, for example, many people linked to it, gets crawled and indexed easier.

## Could dynamic sorting of listings be a reason for not indexing product images?

**Alan**: Paul asked, "Could dynamic sorting of listings be the reason for not indexing product images?"

It is unlikely that dynamic sorting of listings would be the reason for product images not being
indexed. Your product images should be referenced from your product description pages, so we know
the product the image is for. If needed, you can create a sitemap file or provide a Google
Merchant Center feed so Google can find all your product pages without depending upon your listings page.

## Is there a timeframe for the site migration?

**Lizzi**: Sergey is asking, "Is there a timeframe for the site migration? We're migrating a
large site to a new domain at the moment. After four months, there is still no signs of the new
domain getting SERP positions of the old one. So what should we do?"

With a big change like this, it's totally normal to see ranking fluctuations, especially while
you're still in the middle of the migration. There's no set timeframe for when things will settle
down, and also keep in mind that only moving one section of your site is not necessarily
indicative of a whole site move when it comes to Search. If you're still moving things around,
you're going to continue to see fluctuations. It's hard to say what you should do next without
seeing the site itself. And for site specific help, we definitely recommend posting in the forums
so people can see your specific situation and give more specific advice.

## Could the use of HTTP/3 improve SEO because it improves performance?

**John**: Flavio asks, "Could the use of HTTP/3, even indirectly, improve SEO, perhaps because
it improves performance?"

Google doesn't use HTTP/3 as a factor in ranking at the moment. As far as I know, we don't use
it in crawling either. In terms of performance, I suspect the gains users see from using HTTP/3
would not be enough to significantly affect the core web vitals, which are the metrics that we
use in the page experience ranking factor. While making a faster server is always a good idea,
I doubt you'd see a direct connection with SEO only from using HTTP/3. Similar to how you'd be
hard pressed to finding a direct connection to using a faster kind of RAM in your servers.

## Why does Google keep using backlinks as a ranking factor?

**Duy**: Andrea asked, "Why does Google keep using backlinks as a ranking factor if link
building campaigns are not allowed? Why can't Google find other ranking factors that can't be easily manipulated like backlinks?

There are several things to unpack here. First, backlinks as a signal has a lot less significant
impact compared to when Google Search first started out many years ago. We have robust ranking
signals, hundreds of them, to make sure that we are able to rank the most relevant and useful
results for all queries. Second, full link building campaigns, which are essentially link spam
according to our spam policy. We have many algorithms capable of detecting unnatural links at
scale and nullify them. This means that spammers or SEOs spending money on links truly have no
way of knowing if the money they spent on link building is actually worth it or not, since it's
really likely that they're just wasting money building all these spammy links and they were
already nullified by our systems as soon as we see them.

## Does it matter if the vast majority of anchors for internal content links are the same?

**John**: Sam asks, "does it matter if the vast majority of anchors for internal content links
are the same?"

Well, This is fine. It's normal even. When it comes to menus, they're usually everywhere, and
even products when they're linked within an e-commerce site, they're usually linked with the same
link all the time. That's perfectly fine. There's nothing that you really need to do there in terms of SEO.

## If you add the website schema, do you add software application schema too?

**Lizzi**: Anonymous is asking, "If you add the latest website schema to your home page, do
you still add software application or organization schema too? Google updated its schema markup
of documentation by adding website schema for brand, but it does not mention what happens with
organization or software application schema.

Well, it really depends. Sorry to give that answer. These are different features. If your site
is about a software application, then sure, you can also add software application structured data.
Just make sure that you nest everything so that there's one website node on the home page and not
multiple website nodes. That's really the key with this thing.

## Is an excessive number of `noindex` pages an issue for disovery or indexing?

**Gary**: Chris is asking, "How much of an issue for Google is excessive number of `noindex` pages,
and whether it will affect discovery and indexing of content if the volume is too high?"

Good question. `noindex` is a very powerful tool search engines support to help you,
the site owner keep content out of their indexes. For this reason, it doesn't carry any unintended
effects when it comes to crawling and indexing. For example, having many pages with `noindex`
will not influence how Google crawls and indexes your site.

## Is it a problem if the URL and the page don't use the same language?

**Alan**: Yasser asked if the URL doesn't contain characters of the same language used in the
pages, would that affect a site ranking?

From an SEO point of view, there's no negative effect, if the URL is in a different language
than the page content. Users on the other hand, may care, especially if they share the URL with other people.

## How should creators respond to sites that scrape and spam?

**Duy**: Kristen asked, "How should content creators respond to sites that use AI to plagiarize
the content, modify it, and then outrank them in search results?

Scraping content, even with some modification, is against our spam policy. We have many algorithms
to go after such behaviors and demote site scraping content from other sites. If you come across
sites that repeatedly scrape content, that perform well on Search, please feel free to report them
to us, with our spam report form so that we can further improve our systems, both in detecting
the spam and also ranking overall.

## Is it true that Google rotates indexed pages?

**Lizzi**: Ridwan is asking, "Is it true that Google rotates indexed pages? Because the site
I'm working on is rotating on indexed pages. Like for example, page A is indexed on Monday through
Thursday, but not indexed Friday through Sunday."

Okay. So the answer is real quick. No, this is not true. We are not rotating the index based off of days of the week.

## Should we keep an eye on the ratio between indexed and non-indexed pages?

**John**: Anton asks, "Should we keep an eye on the ratio between indexed and non-indexed
pages in Search Console in order to better recognize possibly wasted crawl budget on non-indexed pages?"

No, there is no magic ratio to watch out for. Also, for a site that's not gigantic, with less
than a million pages, perhaps, you really don't need to worry about the crawl budget of your
website. It's fine to remove unnecessary internal links , but for small to medium sized sites,
that's more of a site hygiene topic than an SEO one.

## How do we enable the Discover feature?

**Alan**: Joydev asked, "How do we enable the Discover feature?"

You do not need to take any action to make your content enabled for Discover. We do that
automatically. Google, however uses different criteria to decide whether to show your content
in Discover versus search results. So getting traffic from search is not a guarantee that you'll
get traffic from Discover.

## Does having many `noindex` pages linked from spammy sites affect crawl budget?

**Gary**: Sam is asking another `noindex` related question: "A lot of SEOs are
complaining about having millions of URLs flagged as excluded by noindex in Google Search Console.
All to nonsense internal search pages linked from spammy sites. Is this a problem for crawl budget?"

`noindex` is there to help you keep things out of the index, and it doesn't come
with unintended negative effects as we said previously. If you want to ensure that those pages or
their URLs more specifically don't end up in Google's index, continue using `noindex`
and don't worry about crawl budget.

## Is it thin content if I break down a long article into pieces?

**Lizzi**: Lalindra is asking: "Would it be considered thin content if an article covering a
lengthy topic was broken down into smaller articles and interlinked?"

Well, it's hard to know without looking at that content. But word count alone is not indicative
of thin content. These are two perfectly legitimate approaches: it can be good to have a thorough
article that deeply explores a topic, and it can be equally just as good to break it up into easier
to understand topics. It really depends on the topic and the content on that page, and you
know your audience best. So I would focus on what's most helpful to your users and that you're
providing sufficient value on each page for whatever the topic might be.

## Is it true that having lots of `404` pages can stop crawling and processing?

**Gary**: Michelle is asking: "HTTPS reports help center documentation says lots of `404` pages
can prompt Google to stop crawling and processing URLs. How much is a lot of 404s? And can having
lots of linked 404s in a website affect this?"

Well, this is awkward. Thank you for this question. We fixed a typo in our documentation that
initially suggested that `404` HTTP status codes cause crawling to stop on site level. It should
have been HTTPS certificate errors instead of `404` errors. Feel free to have as many `404` errors as
you need on your site. They don't affect crawling of your website overall. `404` pages are a very
healthy part of the internet.

## What is the current state of Key Moments video markup?

**Alan**: Iman asked, "What is the current state of Key Moments video markup? It seems like
this snippet is only available for YouTube videos. Is that the case?"

Key Moments video mark up is live and used by a range of video providers. It is not specific to
YouTube. If our online documentation is not sufficient, try reaching out into public forums.

## My new website is confused with a similar, older one - what can I do?

**John**: A user called "Weird All website" asks, my
new website, "Weird All", is not showing up in searches
when I type in the full name of the website. It confuses the term with the name of the singer
"Weird Al".

As someone who has grown up listening to lots of Weird Al music, I
totally sympathize with Google and with other search engines. For the most part, if people are
going to type in "weird all" with two L's, probably they
meant to reach Weird Al instead. Essentially, when it comes to SEO
for these kind of things, it's important that you pick a site name that is not just a typo of
something that's really well known, because you're going to have a really hard time differentiating
yourself from there. If something looks like a typo to our systems, we will try to treat it as a
typo and we will try to guide people to what they're probably looking for. And this is something
that our systems can work out over time as we see that well actually people really want to go to
"weird all" and not hear from "Weird Al"
but this takes a lot of time and especially when you're talking about someone as established as
Weird Al, you're going to really have a hard time differentiating
yourself in that regard.

## Is it possible to get FAQ featured snippets with just pure HTML?

**Lizzi**: Anonymous is asking, "Is it possible to get FAQ featured snippets with just pure
HTML? As simple HTML as possible, not referring to schema markup."

Okay. So if you're talking about the FAQ rich result, right now, you need FAQ schema markup to
be eligible for that enhancement in search results. Some features may be able to automatically
pick up what you're putting out on your webpage, but really you should check the specific
documentation to be sure if that's even a possibility. But for FAQ rich result, you definitely
need the markup.

## Do self-referring canonicals help for deduplication?

**John**: Esben asks, "Regarding self-referring canonicals: my idea is that they provide a
uniqueness signal for deduplication, but I see conflicting views. What do you think John?"

Well, from my point of view, they do nothing. But sometimes pages get seen under other URLs, and
then suddenly the canonical is no longer self-referential and actually useful. For example, if a
page is sometimes referred to with UTM tracking parameters.

## Should there be some percentage of randomness in the Search results?

**Alan**: A question received was, "It seems to me that the search engines promote strong
sites more and more and lowers weak resources more and more. Don't you think there should be some percentage of randomness?"

Our primary purpose is to provide the most useful results to people performing searches.

## Why is Google not taking action on spun web stories?

**Duy**: Kunal asked why Google is not taking action on copy or spun web stories? Can you check
on Discover?

Thank you for the report. We are aware of these attempts and we are looking into them. In general,
sites with spammy scraped content violate our spam policy, and our algorithms do a pretty good job
of demoting them in search results.

## Do comment pages linked with `link` `rel="ugc"` get deindexed?

**John**: Tom asks, "Do moderated blog comment pages internally linked as `link` `rel="ugc"` get deindexed?

No they don't. Pages can get indexed for a variety of reasons. While a link with a `rel="ugc"`
is treated differently, as is, for example, a link with the `rel` `nofollow`,
this doesn't negatively affect the destination page. If you want to prevent a page from being
indexed, then make sure to use the `noindex` robots `meta` tag instead.

## Are product reviews update for non-physical products without affiliate links ok?

**Alan**: Abdul Rahim asked, how does Google evaluate product reviews update for non-physical
products that don't have affiliate links?

Our focus is on physical products that can be purchased, but our system also at times evaluates
content involved for digital products. If you are reviewing a product, it is not required you
provide an affiliate link. It's a best practice to include useful links to other resources that
may also be helpful to the reader.

## I have 10,000 pages on my site: are there shortcuts for writing descriptions?

**Lizzi**: Siddiq is asking, "I have 10,000 plus pages on my site. Writing `meta` tags will take
a long time for all of them. Any shortcuts?

Well, our docs on meta descriptions have guidance on this. It can be a good idea for some sites
to programmatically generate the meta description, particularly larger database driven sites
like product aggregators. However, make sure that whatever you're generating is still good quality.
The descriptions should still be unique, specific, and relevant to each page. Don't use the same
meta descriptions over and over again.

## How can I best delete 10,000 pages of thin blog content?

**John**: "I'm looking at purging perhaps 10,000 pages of thin blog content. Is there a best practice for that?"

Well, delete the pages. There's nothing special that you need to do. Deleting thin pages also
doesn't automatically make your site more valuable, though. You really have to make sure that the
value exists independent of the thin or the remove pages.

## Are backlinks powerful or should I focus on maximizing the quality of my site?

**Duy**: "I'm new to SEO and I see many websites or videos suggest that I should buy backlinks.
Are backlinks as powerful or should I focus on maximizing quality of my site?"

There are always people seeking shortcuts or tricks to manipulate, search, ranking, or spend
money to make their sites appear more authoritative to search engines. Link spam is an example
of these tricks. We no longer use links predominantly compared to 20 years ago, for example. And
also launched many algorithms to nullify links spam, and you probably should not waste your money
in spamming links. That money is much needed in creating a great website with great user experience
and helpful content.

## Must a page have a cached copy to appear in the search results?

**John**: "Must a page have a cached copy to appear in the search results?"

No. It doesn't need to have a cached page. The caching system is a bit independent of search's
indexing and ranking. It's not a signal or a hint of quality if a page does not have a cached page.

## Why does Search Console report an unknown referring URL for `4xx` errors?

**Alan**: Esben Rasmussen asked, "How can Google Search Console report an unknown internal
URL as the referring URL for `400` series error URLs?

The URL may be unknown because Google does not index every page. The crawler may have come
across a page, but if it was not indexed, we'd report it as unknown.

## Should we mark automatically created pages as `nofollow`?

**Gary**: Yusuf is asking, "In a WordPress website or blog, should we mark as `nofollow`
automatically created pages such `abc.com/page/one`, and `page/two`, and so on.

If you want to restrict crawling or indexing of certain types of pages on your site, it's probably
a better idea to use robots.txt disallow rules than no-following URLs pointing to those pages.
If nothing else, it's much less work. Presumably, but it's also less brittle. You can't control
how people link to your pages after all, so some links might end up being air-quotes follow.

## How can I best understand the Performance report in Search Console?

**John**: Bobby asks, is anything being done to improve the metric shown in Search Console?
In particular, the Performance report sometimes looks confusing.

This is actually normal. We recently published a blog post on this topic on the Search Central
blog approximately called [a deep dive into the performance data](/search/blog/2022/10/performance-data-deep-dive).
There's a difference when you
look by query and by page, and there's some amount of privacy filtering that happens in the per
query data. Often the details are less critical since trends tend to be the same, but we have a
lot of documentation on that if you want to go down the rabbit hole.

## How do I prevent paywalled content from appearing in search results?

**Lizzi**: Michal is asking: "How do I prevent pay-walled content from appearing in search
results and Discover for non-paying users? I have implemented the paywalled content markup
properly, and I'm worried about unsatisfied users.

Well, that is what we recommend. Tell us what content is behind the paywall with paywall
structure data. So you're on the right track there. If you really want to prevent the paywall
content from appearing in Search entirely, then you can choose to `noindex` those pages.
But that's really up to you.

## Does the spam score affect my site's ranking?

**John**: Usama asks, "Does the spam score affect my site's ranking? Is there a way to improve
the spam score for any website, perhaps outside of disavowing links?"

So, top secret, or maybe not so top secret, but Google does not use third party SEO tools to
determine scores for individual pages. So if you have a tool that flags a spam score for your
website, keep in mind that Google doesn't use it. That doesn't mean that this tool is not useful.
It just means Google doesn't use that score. So my recommendation would be to try to understand
what this tool is trying to tell you, and if there's something actionable behind that, then go and do that.

## What should we do for out-of-stock product pages?

**Alan**: Vara Praad asked, "Once a product is sold out and it will never be return in stock,
what should we do for that product page? Should we delete the product page or redirect to a specific page?"

From a Search perspective, it is fine to delete the page. From a site usability perspective, you
might like to keep the page up for a while or do a redirect in case the old page was referenced
from a third party blog or bookmarked by a customer.

## If hreflang is missing return tags, will it still be considered?

**John**: Tomas asks, if hreflang is used, but they're missing return tags, will hreflang
still be considered for those tags, or will those errors have an effect across the website?

When we look at hreflang, we take into account any valid hreflang annotations. And when it comes
to broken ones, for example, ones that don't have a link back to those individual pages, then we
will drop just that connection. So if you have one page that has three working hreflang
annotations and one broken one. We will just ignore that one broken one because we can't
figure out how it works, but we will continue to use the others that you have specified on that
page. And since hreflang is a per page annotation, if you're doing this across your website and
you have some that work and some that don't work, we will take into account the ones that work
and we will just ignore the ones that don't work. There's no negative effect from the ones that
don't work other than that, they don't do hreflang. That said, if you're testing your site and
you find these kinds of broken annotations, my recommendation is still to fix them, just so that
you take that one worry out. And whenever you notice issues like this, often there are simple
things that you can do to just fix that. I would try to fix that, but it's not going to have a
negative effect on the other annotations that you have across your site.

## How can we implement hreflang without control of web pages in many countries?

**Gary**: Damian is asking, "How do you suggest a website can implement hreflang when
there is no control over brand sites in many countries?"

Fantastic question, and hreflang is an important and complicated topic. Implementing
hreflang among many variations of a site can be quite challenging indeed. However, there's an easy
way to control all the hreflang from a single location: sitemaps. Search for "sitemap cross submits"
on sitemaps.org to learn how to set it up, and then add the hreflang to your sitemaps instead of
your HTML pages. This can simplify the process quite a bit.

## Can hreflang sitemaps be placed in any folder location?

**John**: Andrew asks, "Can hreflang sitemaps be placed in any folder location?"

Yes. There's nothing special about hreflang sitemaps. These are traditional sitemap files with
additional hreflang annotations included in them. You can position them on your site like any other
sitemap file. You can use the robots.txt file to submit them and they can be located anywhere. If
you use Search Console to submit them, you can locate them anywhere within your verified sites.
The same idea applies to sitemaps with image or video annotations.

## What is happening to a website that is not being indexed?

**Alan**: Eze Kennedy asked: "What is happening to website that is not indexed again?"

I would first check Google Search Console to see if there are any errors blocking us from crawling
your site. But Google doesn't index everything on the web, so you really need to make sure your
content stands out in terms of quality.

## How can I handle `x-default` hreflang for new language updates?

**John**: Amy asks, "I have a site in 13 languages. As authors leave, the articles are dropped
with new language updates. The client gives us two options: either drop the `x-default`
or use the last translated language as the `x-default`. Which is better?"

This is totally up to you. You can specify languages on a per page- set basis. It doesn't have
to be the same across the whole website. It's fine to have English be the default language once
and maybe Japanese to be the default another time, if you think that's what users find valuable.
Keep in mind that `x-default` means that users who are not searching in one of these
specified languages would see that page. So I would focus this more on what would be useful
for users and less on your internal processes.

## Why do the product review updates impact non-review content?

**Alan**: Lucy asked, "Why do the product review updates impact non-review content?"

If you're seeing broad impact across your site, it's probably not due to your product reviews.
It may be some other update that have occurred.

## What's the best way to remove old content?

**Gary**: Anonymous is asking, "What's the best way to remove old content and stop it from
being indexed? Redirect? If so, what's the best page to redirect to?"

Interesting question. You can either delete altogether a page and serve a `404` or
`410` status code for its location when you want to retire the page. Or redirect it
to another page that will still help the user in some way accomplish their goal. It's really up
to you how and what you do. Ultimately, it has to make sense for you, not search engines.

## Does text in images influence ranking in image search?

**Lizzi**: Sean B is asking, "Does text in images influence ranking in Image Search, for
example, Image Search for T-shirt printing? I'm not concerned with the text on the t-shirt within
the image, rather the text around the image that might include features such as the price, the
product name, the brand URL, that kind of thing."

Well, Sean, the text around the image is certainly helpful when it comes to understanding the
image. Google can extract info around the image, like from the captions and image titles, so
definitely make sure the image is near relevant text and that that text is descriptive.

## Is it beneficial for the local businesses to use many local listing websites?

**Alan**: Akshay Kumar Sharma asked, is it beneficial for the local businesses to list their
local business details in many free or paid local listing websites? Does Google consider them for
their local query results?

Don't look at adding your site to reputable local listing sites as a way to improve your SEO.
Use them as a possible way to get more traffic, unrelated to Search. Local Search is different.

## Is a query parameter added to URLs bad for SEO?

**John**: Alfonso asks, "Is a query parameter added to a site URL, like for example, "add to cart". Is that bad for SEO?"

No, it's not necessarily bad for SEO on its own. However, for very large websites, it can play
a role in terms of crawl budget if you're unnecessarily adding query parameters to your URLs.
And this is something where you have to take a judgment call for your website and think about,
"is this actually a really large website?". And with these extra parameters that you're adding within
your website's internal linking, are you causing the number of URLs that could be found to explode
exponentially? And if that's the case, then I would work to try to reduce the number of
parameters that you're adding to URLs. But if you're talking about a smaller to medium sized
website, then probably those parameters are something that you can look at later on when you become
a gigantic website.

**Gary:** And with that, this was the November edition of the Google Search SEO Office Hours.
If you have thoughts about this episode, you can [leave as a comment on the YouTube video](https://www.youtube.com/watch?v=TepFVYrBVg0) or
on [Twitter at @GoogleSearchC](https://twitter.com/googlesearchc).

**John:** We also have linked the form for next month's episode if you want to
[ask your questions in the description below](/search/help/office-hours).
So check that out and until next time, bye everyone.
