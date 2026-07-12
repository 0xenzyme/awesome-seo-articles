---
title: "Your Guide to Understanding Google's Sitelinks Search Box"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "your-guide-to-understanding-googles-sitelinks-search-box"
url: "https://www.semrush.com/blog/your-guide-to-understanding-googles-sitelinks-search-box/"
canonical: "https://www.semrush.com/blog/your-guide-to-understanding-googles-sitelinks-search-box/"
author: "Shane Jones"
published: "2015-05-28T18:00:09+00:00"
updated: "2015-05-28T18:00:09+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "date_2015_very_old"
schema_genre: "General SEO"
fetched_at: "2026-06-12T21:27:09+00:00"
status_code: 200
html_hash: "08acecd36ffc81fae7697be590f6376679115946e30f6399b957a26815223d33"
clean_word_count: 1319
clean_char_count: 7947
---
# Your Guide to Understanding Google's Sitelinks Search Box

Have you ever Googled a website only to find a second Google search box embedded underneath the first? That’s a recently updated Google feature, the Sitelinks search box. It has the capability to streamline your own website’s search function, but opinions are mixed regarding the benefit it provides.

Here’s the rundown on how Google’s Sitelinks search box works, both sides of the controversy about its usefulness, and how to maximize your own benefit.

## How it Works

Google’s Sitelinks search box highlights webpages’ internal search function. It’s triggered by a query that directly names a website. Here’s an example, taken from one of the most popular sites for internal searches, Youtube.

It’s important to note that the query must be specific. A search result for “New York Times” will feature the NYTimes.com Sitelinks search box, but a search for “New York paper” won’t, even though the results are very similar.

As you can see, the Sitelinks search box comes complete with its own autocomplete dropdown menu. It functions the same in mobile, too. The embedded search box removes an extra action standing between a user and a site’s content. Simply put, it’s an intuitive, useful tweak to the typical Google result that helps searchers find what they want faster.

Not all websites have the Sitelinks search box, however. Google only allows sites with enough authority to use it.

Even if your site qualifies, you still need to take another action in order to benefit: By using the right [schema](http://schema.org/), the preferred markup to streamline website and search engine integration, webmasters can ensure that their own search page shows up as the result a Sitelinks search box query, rather than another page of Google’s results.

Since [this version of the Sitelinks search box](http://blog.similarweb.com/revealing-the-popularity-of-each-schema-markup-type/)’s introduction in September 2014, the Search Action schema has risen in popularity among webmasters. According to [SimilarTech’s statistics](https://www.similartech.com/categories/schema), it’s the most used schema for the top ten thousand websites on the internet, used by 6.75 percent of the sites while the second most used schema clocks in at a mere 4.49 percent.

But has the benefit been proven to justify this popularity?

## Pros

The Sitelinks search box feature itself has a clear benefit to the user: streamlined searching. The benefit to the webmaster is less clear, but is still existent in theory: by directly receiving users at the page that they want, a website will encourage them to stick around longer and send them away happier with their experience. Just the existence of the Sitelink search box boosts user experience.

However, you can’t affect whether or not your site gets a search box. The true pros and cons to consider are about the search box are about the schema that can ensure a website’s Sitelink search box results are native to that website.

We already know that pages with any schema markups at all [rank four positions higher in search results](http://searchenginewatch.com/sew/study/2341710/pages-with-schema-markup-rank-4-positions-higher-in-search-results-study) than those that don’t. This could easily be a correlation rooted in a separate causation. Does the search action schema itself increase traffic?

The short answer is “yes, but not by much.” Webmasters have reported boosts in traffic after implementing the search action schema, but those boosts haven’t been significant, adding up to a rise in traffic of just fractions of a percent.

## Cons

With the benefits underwhelming but existent, you might need to consider the downsides. The first warning sign is the fact that Amazon has opted out, and doesn’t even allow a Sitelinks search box for their website. It’s unclear why, but there are several potential reasons.

![Google Search](https://static.semrush.com/blog/uploads/media/ce/50/ce5010a364733980e65c9edb0f0fbeaf/search2.jpg)

First, they might not want to allow Google to access their information. As a big player, Amazon keeps its cards close to its chest. Letting Google get even a peak at their secret sauce might hurt them more than improving the user experience a tad could justify.

Second, Amazon may not want to lose access to the data provided by the customers who arrive on its homepage. Letting them search directly from Google dilutes their knowledge of how their audience works. Given how [data-driven Amazon’s success is](http://www.fastcodesign.com/1669551/how-companies-like-amazon-use-big-data-to-make-you-love-them), this is probably their largest reason for rejecting the search box.

The right move for a website with Amazon’s size and dominance is often very different from the right move for a smaller site. The size of your data and how you acquire it may be a smaller factor in your decision to embrace or reject Google’s Sitelinks search box.

Some webmasters may be wary of giving more information to Google. If that’s you, than the meager benefits of adding the search action schema might not tempt you. But for the major players ranked by SimilarTech, that’s the first schema they reach for when working to improve their search results.

## How to Add the Schema

If you want to get the schema, there are several barriers. Navigate these steps to secure that additional user experience for your website’s search function.

### Are You Eligible?

Google isn’t very transparent about how sites become eligible, and if your site isn’t, than adding the schema code will be useless. To get a better idea of your site’s eligibility, consider these variables.

Is your site the first result for its brand name search? Does it already have its own search box on the results page for a branded search? Also, check Google Webmaster Tools for the most sanctioned verification method: an alert that you qualify.

### Install an Internal Search Engine

Your site might have a search function already, but if it doesn’t, you definitely need to get one. It’s what you’ll be hooking up to the Sitelinks search box in order to get the results to appear on your site.

The default Wordpress search engine works well, as do other common internal search functions. If you don’t have one of your own, it’s simple to add [Google’s custom search](https://developers.google.com/custom-search/). However, if you go with Google, you’ll either have to pay for an ad-free version or accept the free version that uses the same Adwords ads that you’re installing this schema to avoid.

### Add the Code

Open the source code of your website homepage. Then add this code, [available from Google](https://developers.google.com/structured-data/slsb-overview):

<script type="application/ld+json">

{

"@context": "http://schema.org",

"@type": "WebSite",

"url": "https://www.example-petstore.com/",

"potentialAction": {

"@type": "SearchAction",

"target": "https://query.example-petstore.com/search?q={search\_term\_string}",

"query-input": "required name=search\_term\_string"

}

}

</script>

After replacing the example links in the code with your website’s address and search page links, you’re done, and you just need to wait a matter of days or weeks for Google’s bots to recognize the change.

## Alternately: How to Opt Out

If, like Amazon, you don’t want the Sitelinks search box to appear for your site at all, Google has released a meta tag to make opting out easy:

<meta name="google" content="nositelinkssearchbox" />

Slap this tag on your site, and its Sitelinks search box will disappear from Google within a few days.

## Conclusion

Considering all benefits and disadvantages, I would recommend adding the search action schema if your site is popular enough to qualify for the Sitelinks search box. While it may not greatly impact traffic, it provides a better user experience, and that has never hurt a website yet.
