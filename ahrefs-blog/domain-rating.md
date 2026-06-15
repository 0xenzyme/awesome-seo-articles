---
title: "Domain Rating: What It Is & What It’s Good For"
source: ahrefs-blog
content_type: "product_blog"
freshness_risk: "low"
slug: "domain-rating"
url: "https://ahrefs.com/blog/domain-rating/"
canonical: "https://ahrefs.com/blog/domain-rating/"
author: "Tim Soulo"
published: "2022-05-04T10:47:41+00:00"
updated: "2024-10-04T15:13:50+00:00"
categories:
  - "Product Blog"
freshness_reasons:
  - "date_2024_watch"
  - "product_or_tool_content"
fetched_at: "2026-06-12T11:27:41+00:00"
status_code: 200
html_hash: "140b964e4c218f4b2900a6b6df075fd87ee3c5aa00ebbd645ecb6f728d585f1d"
clean_word_count: 1941
clean_char_count: 10910
---
# Domain Rating: What It Is & What It’s Good For

Domain Rating (or DR) is one of the most prominent metrics in Ahrefs. You can spot it in nearly every tool and report within our platform.

And while this metric can be incredibly useful for making informed SEO decisions, it can also lead you astray if you don’t understand it well enough.

So in this article, I’m going to lay out all the details of DR, break down its most common use cases, and provide answers to some frequently asked questions.

## What is Domain Rating?

Domain Rating (DR) is an Ahrefs metric that shows the relative strength of a website’s backlink profile.

DR is measured on a logarithmic scale from 0 to 100, with the latter being the strongest.

Sidenote.

The term “logarithmic scale” means that the gap between DR 70 and DR 71 is much bigger than the one between DR 20 and DR 21. In other words, the higher your DR gets, the more challenging it will be to grow it by another few points.

## How is Domain Rating calculated?

We calculate DR in a somewhat similar way to how [PageRank](https://ahrefs.com/blog/google-pagerank/) is calculated. The main difference is that PageRank is calculated between pages, while DR is calculated between websites.

Technically, it looks something like this:

1. We find all domains that have at least one followed link to the target domain.
2. We look up how many other domains each linking domain links to.
3. We then pass some amount of “DR juice” from each linking domain to the target domain. That amount is determined (roughly) by dividing the DR of the linking domain by the number of unique domains that it links to.

This is obviously a severely oversimplified explanation, but it does capture the essence of how we calculate the DR of a given website.

Let me also reframe this in a more practical way:

- If a website is only linking to you via nofollow links, it won’t increase your DR.
- Only the first link from a domain will increase your DR. All subsequent links don’t affect your DR any further.
- If a website (which has previously linked to you) keeps linking out to more and more new websites, the amount of “DR juice” that it is sending you will decrease over time. So your own DR may eventually decrease too.
- As the DR of a website that links to you increases, it will start sending more “DR juice” to your website. So your own DR may increase too.

Please note that Ahrefs’ DR metric is **purely link-based**. We don’t take into account things such as the search traffic of a given website, the age of its domain, or the popularity of a parent brand.

It is also important to note that DR doesn’t account for backlink SPAM. In fact, large amounts of [low-quality backlinks](https://ahrefs.com/blog/bad-links/) may actually increase your DR, not decrease it.

In the past few years, some black-hat SEOs found ways to inflate Ahrefs’ DR with link spam and exploited that loophole to make a profit. But we managed to identify many of those methods and make sure they can no longer be exploited today.

## Is Domain Rating important for growing your search traffic?

Although DR correlates strongly with a website’s search traffic, you should not focus your efforts on growing this metric specifically.

Google ranks pages, not websites. So your efforts should, therefore, be focused on producing high-quality content and acquiring [high-quality backlinks](https://ahrefs.com/blog/high-quality-backlinks/) directly to that content.

Both your DR and your search traffic will grow naturally as a byproduct of this.

## What are the main use cases of Domain Rating?

I like to think of DR as a measure of a website’s “link popularity” or how much the pages of a given website were referenced around the web. Measuring that “link popularity” has two straightforward use cases in SEO.

### 1. Gauging the “ranking potential”

If you have roughly the same DR as your competitor, you can plug their website into Ahrefs’ [Content Gap tool](https://ahrefs.com/content-gap) and look for keywords that bring them traffic and that you don’t currently rank for. There’s a good chance you’ll be able to rank for them too.

For example, basecamp.com has nearly the same DR as asana.com (88 and 89, respectively). So the folks at Basecamp can try going after the same keywords that Asana is ranking for, as there’s a good chance their site will rank for the keywords fairly easily.

But if your DR is just 20, going after the keywords that a DR 80 website is ranking for is rather unreasonable. You should instead look for lower-DR websites to get “rankable” content ideas from.

Obviously, it’s not guaranteed that you’ll rank for a given keyword just because a site with a similar DR is ranking for it. But sourcing your content ideas from websites with similar “link popularity” is a reasonable strategy.

### 2. Link prospecting

When you have a list of hundreds of relevant websites to potentially acquire a backlink from, the DR of these websites will help you to determine which of them is likely to cast the “stronger” link.

Don’t get me wrong, though. I’m not telling you to avoid low-DR websites and only focus on the bigger ones.

If relevant, even a low-DR link will help your page to rank better. But gauging the relative value of a link from a given website will help you to prioritize your efforts accordingly.

For example, let’s say your friend has a DR 25 blog, and they are keen on publishing your guest post. On the other hand, you have applied to write for a large DR 80 publication, and it is expecting a guest post from you too.

As a general rule, you should prioritize getting a link from a big publication. This is because the value of its link is likely to be much higher than that of your friend’s small blog (no offense to your friend, though).

[Link building is obviously much more nuanced than that](https://ahrefs.com/seo/link-building). There are many different factors that determine how much a given link helps your page to rank higher on Google. But as a general rule, links from high-DR websites tend to bring more value than links from low-DR websites.

## Do all subdomains have the same DR as their root domains?

No, there are some exceptions.

The DR scores of wordpress.org and its subdomain codex.wordpress.org both show DR 98.

But wordpress.com and discover.wordpress.com have DR 93 and DR 66, respectively.

What is the difference between the two cases?

Well, wordpress.com is what we call a “service root domain.” Anyone can launch a subdomain at wordpress.com and put some content there. And because the resulting “sub-sites” will belong to different people and have entirely different content and purposes, they should not inherit the high DR of their parent website.

WordPress.org, on the other hand, doesn’t allow random people to freely create subdomains. Only the owners of this website can do that, which is why the DR of the parent domain is being passed to its subdomains.

Here are a few more examples of domains that do not pass their DR to the subdomains:

- wordpress.com
- typepad.com
- squarespace.com
- blogspot.com
- tumblr.com
- webs.com
- hubpages.com
- wikispaces.com

## Are Domain Rating and Ahrefs Rank related?

Both of these metrics indicate how strong a given website’s backlink profile is, but each metric measures it differently.

DR assigns a value from 0 to 100 according to the size and quality of a website’s backlink profile. And Ahrefs Rank (AR) simply orders all websites by how strong their backlink profiles are.

Let me explain that with an example.

Huffingtonpost.com, techcrunch.com, and salesforce.com all have the same DR of 92. But their backlink profiles aren’t perfectly equal, right?

Here are these websites [ordered by AR](https://app.ahrefs.com/ahrefs-top):

- AR **316** – huffingtonpost.com
- AR **317** – techcrunch.com
- AR **346** – salesforce.com

These numbers tell us that huffingtonpost.com has just a slightly stronger backlink profile compared to techcrunch.com, with no other websites in between them. But there are 29 websites with a stronger backlink profile than salesforce.com (AR 346) but a weaker one than techcrunch.com (AR 317).

This kind of granularity helps you to compare websites with the same DR score and rank them by their link popularity.

## Frequently asked questions

The information I shared above should give you a pretty good idea of our DR metric and address many of the questions that you might have had before.

But just in case, here’s also a selection of some frequently asked questions that Ahrefs’ support team receives:

### I didn’t lose any backlinks. Why did my DR drop?

That could be due to many other sites in our database gaining a lot of backlinks. Think of it this way: When a DR 100 website gets more backlinks, we can’t make it DR 101. So instead, we push all the other websites down by 1. That’s a very raw explanation of why you may see a drop in your DR even though no backlinks are lost.

Another possible reason is sites that are linking to you have lost backlinks and their DR scores have decreased. Or perhaps they have started linking to more sites. In both cases, the amount of “DR juice” they’re passing to your website will decrease as well.

### My competitor doesn’t have any links from high-DR sites, but their DR is higher than mine. Why?

You don’t necessarily need links from high-DR websites to grow your DR. You can actually get a very high DR with links from low-DR websites only; you just need a whole lot of them.

### I got a link from techcrunch.com, which has a very high DR of 93. How come my own DR didn’t move a bit?

As explained above, the amount of “DR juice” that TechCrunch will pass to your website is divided by the number of all websites that techcrunch.com is linking out to (with followed links). And it’s linking out to nearly 100K+ other websites (according to Ahrefs). So the amount of “DR juice” it contributes to your website is relatively low.

### Do homepage links pass more DR than deep links?

This does not make any difference for DR. Both kinds of links will contribute to your DR in the same way.

### Does Ahrefs use Domain Rating to prioritize crawling the web?

Yes, DR is one of the factors that we feed to our own crawler. It helps us decide how many pages of a given website we want to crawl (and how deep we want to go).

The web is not a tidy, structured, or logical place. There are tons of ugly websites that generate millions of pages—some by mistake and others purposefully. And having this kind of heuristic in place allows us not to waste resources on crawling all that junk.

## Final thoughts

Even though I’m obviously a biased party, I’m hoping that I was able to give you a rather objective look at our DR metric and its practical applications.

If you still have any further questions or concerns, feel free to ping me [on Twitter](https://twitter.com/timsoulo).
