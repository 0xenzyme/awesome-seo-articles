---
title: "Nofollow vs. Follow Links: Everything You Need to Know"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "nofollow-links"
url: "https://ahrefs.com/blog/nofollow-links/"
canonical: "https://ahrefs.com/blog/nofollow-links/"
author: "Joshua Hardwick"
published: "2019-03-27T00:17:13+00:00"
updated: "2023-10-04T14:13:28+00:00"
categories:
  - "General SEO"
  - "Link Building"
  - "Technical SEO"
freshness_reasons:
  - "date_2023_aging"
fetched_at: "2026-06-12T11:53:56+00:00"
status_code: 200
html_hash: "3bbd2a52ac684e1351f7287cb6e3223947695b11835ec5f3d71f78bb2c425f34"
clean_word_count: 3999
clean_char_count: 24094
---
# Nofollow vs. Follow Links: Everything You Need to Know

The rel=”nofollow” tag is one of the simplest HTML tags around, and one that’s crucial to understand if you’re doing SEO. Learn everything you need to know about nofollowed links in this guide.

Nofollow links are nothing new. They’ve been around for 14 years.

If you care about your website’s performance in search engines, then knowing when and when not to use nofollowed links isn’t just important—it’s *crucial*.

In this guide, I’ll explain how nofollowed links came to be, how they help with SEO, and how using them correctly can protect your site from a dreaded Google penalty.

First, though, let’s cover the basics.

New to link building? Check out our

[Beginner’s guide to link building](https://ahrefs.com/blog/link-building/)

## What are nofollow links?

Nofollowed links are hyperlinks with a rel=“nofollow” tag.

These links do not influence the search engine rankings of the destination URL because [Google does not transfer PageRank or anchor text](https://support.google.com/webmasters/answer/96569?hl=en) across them. In fact, Google doesn’t even crawl nofollowed links.

**Recommended reading:** *[Google PageRank is NOT Dead: Why It Still Matters](https://ahrefs.com/blog/google-pagerank/)*

### Nofollow vs. follow links

Followed and nofollowed links look identical to the average web user.

The [blue text](https://ahrefs.com) in this sentence is a **followed** link. The [blue text](https://ahrefs.com) in this sentence is a **nofollowed** link. The difference between the two is apparent only when you dig into the HTML code.

**Followed:**

```
<a href="https://ahrefs.com">blue text</a>
```

**Nofollowed:**

```
<a href="https://ahrefs.com" rel="nofollow">blue text</a>
```

The HTML is identical except for the addition of the rel=”nofollow” tag.

It’s possible to nofollow **all** links on a webpage by placing a robots meta tag with the value “nofollow” in the header. However, the nofollow tag is more commonly used as it allows one to nofollow some links on the page while leaving others followed.

Not sure why you’d want to do that? It’s time for a quick history lesson.

## The history of *rel=”nofollow”*

Google originally [introduced](https://googleblog.blogspot.com/2005/01/preventing-comment-spam.html) the nofollow tag in 2005 to combat comment spam.

> If you’re a blogger (or a blog reader), you’re painfully familiar with people who try to raise their own websites’ search engine rankings by submitting linked blog comments like “Visit my discount pharmaceuticals site.” This is called comment spam, we don’t like it either, and we’ve been testing a new tag that blocks it. From now on, when Google sees the attribute (rel=“nofollow”) on hyperlinks, **those links won’t get any credit when we rank websites in our search results**. This isn’t a negative vote for the site where the comment was posted; it’s just a way to make sure that spammers get no benefit from abusing public areas like blog comments, trackbacks, and referrer lists.

Shortly after, [Yahoo](https://web.archive.org/web/20050203015651/http://www.ysearchblog.com/archives/000069.html), [Bing](https://web.archive.org/web/20150603030936/http://blogs.bing.com/webmaster/2008/06/03/robots-exclusion-protocol-joining-together-to-provide-better-documentation) and a few other search engines also announced their commitment to the nofollow tag.

IMPORTANT NOTE

The interpretation of nofollow varies somewhat between search engines. [Here’s a table](https://en.wikipedia.org/wiki/Nofollow#Interpretation_by_the_individual_search_engines) showing the differences.

Nowadays, WordPress adds the nofollow tag to comment links by default, as do many other CMS’. So even if you’ve never heard of a nofollow link before now, rest assured that any spammy commenters on your blog likely aren’t receiving any SEO benefits from their efforts.

However, if you’re concerned that your comments may not be nofollowed, here’s how to double-check:

1. Find a comment
2. Right-click the link
3. Hit “Inspect”
4. Look at the highlighted HTML code.

If you see the rel=nofollow tag, it’s nofollowed. Otherwise, it’s followed.

Not comfortable digging into HTML code? Install the [nofollow Chrome extension](https://chrome.google.com/webstore/detail/nofollow/dfogidghaigoomjdeacndafapdijmiid?hl=en) which visibly highlights all nofollowed links as you’re browsing the web.

Got it? Good. Back to our history lesson.

### 2009: Google combats PageRank sculpting

PageRank flows around a website via [internal links](https://ahrefs.com/blog/internal-links-for-seo/) (links from one page on the site to another).

For example, some of this article’s PageRank flows to the other pages on our site via hyperlinks like [this one](https://ahrefs.com/). In general, higher PageRank equates to higher rankings. Gary Illyses confirmed this last year.

> DYK that after 18 years we’re still using PageRank (and 100s of other signals) in ranking?
>
> Wanna know how it works?<https://t.co/CfOlxGauGF> [pic.twitter.com/3YJeNbXLml](https://t.co/3YJeNbXLml)
>
> — Gary “鯨理” Illyes (@methode) [9 February 2017](https://twitter.com/methode/status/829755916895535104?ref_src=twsrc%5Etfw)

However, PageRank only gets transferred via followed links, not nofollowed links.

That’s always been the case, but the way PageRank gets shared between the followed links on a page has changed over the years.

Before 2009, it worked like this:

If you had **three** links on a page and **one** of them was nofollowed, then the total PageRank was split between the **two** followed links.

Unfortunately, some people started taking advantage of this technicality to manipulate rankings by sculpting the flow of PageRank around their sites.

In other words, they’d nofollow links to their unimportant pages to allow for the maximum transference of PageRank to their “money” pages.

Google [announced changes](https://www.mattcutts.com/blog/pagerank-sculpting/) to nip this practice in the bud in 2009:

> So what happens when you have a page with “ten PageRank points” and ten outgoing links, and five of those links are nofollowed? […] Originally, the five links without nofollow would have flowed two points of PageRank each […] More than a year ago, **Google changed how the PageRank flows so that the five links without nofollow would flow one point of PageRank each.**

Here’s an illustration of the before and after:

IMPORTANT NOTE

PageRank is a complex beast. It’s been ten years since Google made this change. While they haven’t publicly announced any further changes to how PageRank works in recent years, it’s likely that at least some changes have taken place behind the scenes.

While PageRank sculpting is no longer a *thing*, “nofollowing” some internal links can help with crawl prioritization because **Google doesn’t crawl nofollow links.**

> Search engine robots can’t sign in or register as a member on your forum, so there’s no reason to invite [Googlebot](https://ahrefs.com/blog/googlebot/) to follow “register here” or “sign in” links. Using nofollow on these links enables Googlebot to crawl other pages you’d prefer to see in Google’s index.

However, this is a somewhat advanced topic, so I won’t go any deeper into that here.

**Recommended reading:** *[What Is Crawl Budget and Should SEOs Worry about It?](https://ahrefs.com/blog/crawl-budget/)*

### 2013 onwards: Google combats paid links

Google classes the buying or selling links that pass PageRank as [a violation of their Webmaster Guidelines](https://support.google.com/webmasters/answer/66356?hl=en).

As such, **all paid links should be nofollowed.**

That’s been the case for many years, even long before 2013.

However, from what I can see, Google became increasingly concerned about the effect of undisclosed paid links on their algorithm around this time… and has been ever since.

Matt Cutts delves deeper into their reasoning for the disclosure of paid links in this 2013 video:

But to summarize: Google wants to reward **earned** links, not **paid** links.

> People treat links as editorial votes. They link to something because it inspires passion in them. It’s something that’s interesting. They want to share it with friends. There’s some reason why they want to highlight that particular link.

The problem is that some paid links look no different from earned links. Think about the difference between a link in a paid review vs. a link in an unpaid review.

On the face of it, both links will look identical. That’s why there needs to be a way to disclose the paid one to Google.

Think of it like this: There are two ways to get an Oscar:

**Option #1:** Live to act, continuously hone your craft, and work hard for years.
 **Option #2:** [Buy 6 of them for $8.97 on Amazon](https://www.amazon.com/Gold-Award-Trophies-Trophy-Statues/dp/B06XFZ61BV)…

The nofollow tag (on paid links) is to Google what the $8.97 sticker on the bottom of your fake Oscar is to your friends: a tell-tale sign that you didn’t earn this legitimately and thus, don’t deserve credit for your tomfoolery manipulative efforts.

## Do nofollow links help with SEO?

Let’s briefly recap what Google says about the way they handle nofollowed links:

> Google does not transfer PageRank or anchor text across these links.

That all seems clear enough until you read the sentence that precedes it:

> **In general, we don’t follow them.** This means that Google does not transfer PageRank or anchor text across these links.

*In general*, I think this statement is vaguer than it needs to be and implies that they follow nofollowed links in some instances.

What those cases may be, nobody knows.

Some believe that all nofollowed links still transfer some PageRank. Some think that Google transfers PageRank to some, but not all nofollowed links. Others believe that people are reading too much into [wording that hasn’t changed for the best part of seven years](https://web.archive.org/web/20130714093949/https://support.google.com/webmasters/answer/96569?hl=en#).

Earlier this year, we [studied 44,589 SERPs](https://ahrefs.com/blog/links-with-traffic-study/) to see if there was any correlation between Google rankings and various backlink attributes—one of which was the number of followed backlinks.

Here’s what we found:

The correlation for the number of “dofollow” backlinks is a little bit weaker than that of the total number of backlinks.

Here’s what [Tim](https://ahrefs.com/tim) said about this:

> This **could** be an indication that Google values some nofollowed links from strong pages more than followed links from weak pages. **#whoknows**
>
>
>
> Tim Soulo, CMO [Ahrefs](https://ahrefs.com)

Take this finding with a large pinch of salt. The primary aim of this study was not to analyze the impact of nofollowed vs. followed links and as such, we didn’t make any effort to isolate this factor.

But even if we assume that nofollowed links have no **direct** impact on SEO, they can still have an **indirect** impact because:

### 1. They help diversify your link profile

Natural backlink profiles are diverse.

Some links are followed, and others are nofollowed. That fact is unavoidable because some people will inevitably link to you via nofollowed links… no matter how much you might wish this wasn’t the case.

Furthermore, most of the backlinks you get from following places are nofollowed:

- Social networks (Facebook, Twitter, YouTube, etc.)
- Forums (Reddit, Quora, etc.)
- Press releases
- Guestbooks (hello, 1998!)
- Wikipedia (hint: *anyone* can edit a Wikipedia page)
- Pingbacks
- Directories

Long story short, if a website only has followed backlinks or a conspicuously high percentage of followed backlinks, then that’s a tell-tale sign something fishy is going on.

To check the proportion of followed vs. nofollowed links for any website or webpage, use the **Overview** report in [Ahrefs Site Explorer](https://ahrefs.com/site-explorer).

*Site Explorer > enter any domain, URL, or subfolder > Overview*

It looks like 85% of the referring domains (linking websites) to the Ahrefs blog are followed.

Is this good or bad? Honestly, as long as there’s some diversity here, that’s a good sign.

What you don’t want to see is 100% “dofollow” or anything close because that’s a definite sign of manipulation. From experience, I’d say anywhere from 60-90% is normal—but that range isn’t definitive. If you suspect foul play, delve deeper.

### 2. They drive traffic, and traffic drives followed links

Links aren’t only useful for SEO purposes. They drive referral traffic too.

That’s why we’re so active on [Quora](https://www.quora.com/).

If you haven’t heard of Quora before, it’s a Q&A website where anyone can answer the questions people post. Within those answers, Quora allows links to relevant resources.

Here’s a recent answer posted by our Marketing Manager, [Rebekah Bek](https://twitter.com/itsrbek?lang=en), where she links to the Ahrefs blog:

Unfortunately, as all outbound links on Quora are nofollowed, that link has no direct SEO effect.

But here’s the interesting part:

If we check the **Backlinks** report in [Ahrefs Site Explorer](https://ahrefs.com/site-explorer) for *ahrefs.com* and filter for only “dofollow” links, here’s one of the many backlinks we see:

Now let’s take a closer look at the referring page (the page the followed link comes from):

The only reason we got this **followed** link is because the author of this article stumbled upon Rebekah’s Quora answer. In other words, the nofollowed link indirectly led to a followed link.

So remember this: for someone to link to you, three things have to happen in this order:

1. They **see** your content
2. They **enjoy** your content
3. They **recommend** it to others (via links on their site)

Because nofollow links can help with that first step, they’re often a catalyst for followed links.

### 3. They can protect against Google penalties

Sometimes there are legitimate reasons to pay for links.

If a website gets tons of traffic, buying a sponsored post on that site may make total sense. And if you’re paying good money for a feature, then you’ll probably want to include a backlink so that the readers can easily find your website.

The problem? Google states that followed paid links are against their Webmaster Guidelines.

That said, the SEO community is generally divided into two camps:

1. Those who believe Google **can** accurately identify paid links algorithmically.
2. Those who believe Google **can’t** accurately identify paid links algorithmically.

Which camp is correct is a debate for another day.

For now, let’s assume that camp #2 is correct and that Google struggles to identify any and all paid links. That means you’re safe to buy and sell links to your heart’s content, right? Not so fast.

Google has [a tool](https://www.google.com/webmasters/tools/paidlinks) which allows anyone to report a website for buying or selling links.

Google’s tool for reporting paid links.

Translation: it may not be Google that you should fear—but rather your competitors.

Think about it: If a competitor sees you ranking well for their target keyword, and they use a tool like [Ahrefs’ Site Explorer](https://ahrefs.com/site-explorer) to delve into your backlinks, only to discover followed links like this:

Then why wouldn’t they report you?

If doing so results in Google’s webspam team taking a look at your website, discovering the paid links, and issuing a manual penalty, then that’s one less competitor for them to compete with in the SERPs.

Which brings us neatly to:

## How to audit your website for issues related to nofollow links

Having followed backlinks that violate Google’s Webmaster Guidelines is risky.

The same is true for outbound links on your website that should be nofollowed.

But this isn’t only about the wrath of Google (i.e., [penalties](https://ahrefs.com/blog/google-penalties/)). It may also be the case that certain internal nofollowed links are hindering your SEO performance.

What follows is a quick audit to help identify and eliminate any such issues.

### 1. Look for followed backlinks with keyword-rich anchors

For the most part, people won’t use exact-match anchors when linking to your site. That’s why followed links with exact-match anchors *can* be a sign of backlink manipulation.

To find them, use the Anchors report in [Ahrefs Site Explorer](https://ahrefs.com/site-explorer).

*Site Explorer > enter your domain > Anchors > dofollow filter*

Here, we see that most of this website’s anchors are branded or generic (blurred for privacy purposes), but there are nineteen websites (referring domains) that link using the phrase “payday loans” as the anchor.

If we hit the caret, then Referring domains, we can see what these websites are.

Then, if we hit the caret again, we can see the context of all the links from each domain.

Here are some rough guidelines for dealing with different [types of links](https://ahrefs.com/blog/types-of-backlinks/) you find here:

- **Bought links on low-quality sites.** Ask for the link to be removed (preferably) or nofollowed. Disavow at the page or domain-level if they fail to do so.
- **Guest posts bio links.** Have you previously used keyword-rich anchors in your guest post author bios? Ask the person in charge of that site to swap out the keyword-rich link for a branded one. Or, if you prefer to keep the anchored link, ask for it to be nofollowed.
- **Widget links.** Change the HTML of your widget so that the link is nofollowed. Ask those who’ve already embedded your widget to nofollow the link.
- **Sitewide links.** Ask for the link to be nofollowed or changed to a branded anchor.

Note that exact-match followed links aren’t always indicative of low-quality or paid links. Such links can occur naturally and under legit circumstances.

That’s why you should always make sure to investigate links in-depth before disavowing them or asking for them to be nofollowed.

Fail to do that, and you could end up doing more harm than good.

PRO TIP

For large websites, there can be hundreds or thousands of different anchors in the **Anchors** report. Sifting through all of them can be time-consuming.

So here’s a quick trick you can use:

First, export the full list of followed anchors.

*Site Explorer > enter your domain > Anchors > add “dofollow” filter > Export > CSV*

Then copy and paste them into [Ahrefs Keywords Explorer](https://ahrefs.com/keywords-explorer) in batches of up to 10,000 at a time.

Hit search to generate a report, then sort by the CPC column from high to low.

Because high CPC anchors are often more likely to be the spammy ones, this should result in spammy anchors rising to the top of the list.

Finally, search for any spammy-looking anchors in the **Anchors** report in Site Explorer and investigate further.

### 2. Look for followed sponsored backlinks

Backlinks from sponsored posts should always be nofollowed.

That’s because you’re effectively paying for the link, so it shouldn’t pass PageRank.

To find such links, search for the word “sponsored” in the **Backlinks** report for your website in [Ahrefs Site Explorer](https://ahrefs.com/site-explorer).

*Site Explorer > Backlinks > search for “sponsored” > filter for “dofollow”*

Reach out and ask for any such links to be nofollowed.

### 3. Look for keyword-rich followed outgoing links on your website

Did you know that Forbes nofollowed all of their outbound links in 2017?

This move came after they noticed that some of their contributors were selling followed links from their articles. Because they have so many contributors, they decided it was impossible to vet all links on the site, and so took the lazy option to nofollow everything.

Why is this relevant?

Because if you’ve ever accepted guest posts on your site, or have any user-generated content, you could have the same issue.

To find out if that’s the case, take a look at your outgoing anchors in [Ahrefs Site Explorer](https://ahrefs.com/site-explorer).

*Site Explorer > enter your domain > Outgoing links > Anchors > add “dofollow” filter*

Look for suspicious words and phrases that you wouldn’t expect to see on your site, and remove or nofollow any that appear manipulative (e.g., keyword-rich anchors in guest post bios, etc.).

As for why this is important, Google [explains](https://support.google.com/webmasters/answer/96569?hl=en) this best:

> If you can’t or don’t want to vouch for the content of pages you link to from your site — for example, untrusted user comments or guestbook entries — you should nofollow those links. **This can discourage spammers from targeting your site, and will help keep your site from inadvertently passing PageRank to bad neighborhoods on the web.**

Do you see lots of anchors?

Use the pro tip from step #1.

### 4. Look for followed sponsored links on your site

Have you ever accepted a sponsored post on your website? Did you make sure to nofollow the link?

If you’re unsure, it might be worth checking.

To do that, search in Google for `site:yourwebsite.com "sponsored post"`

Open up any results one by one and locate the sponsored link.

If you installed the [nofollow Chrome extension](https://chrome.google.com/webstore/detail/nofollow/dfogidghaigoomjdeacndafapdijmiid?hl=en), all nofollow links on the page will be highlighted—so the sponsored link should definitely be highlighted. If it isn’t, it’s a followed link.

Confirm this is the case by digging into the HTML.

Right-click on the link, hit “Inspect,” and look for the rel=”nofollow” tag.

If it’s absent, then it’s a followed link and you should add a nofollow tag.

### 5. Look for nofollowed internal links

No internal links should be nofollowed unless they point to unimportant pages or pages that you want to exclude from search engines’ indexes.

To find nofollowed internal links, use the **Best by Links** report in [Ahrefs Site Explorer](https://ahrefs.com/site-explorer).

*Site Explorer > enter your domain > Best by Links > switch to Internal > sort by the “nofollow” column*

If you see any pages with nofollowed internal links, hit the number to see where those links come from and investigate further. It may be the case that these make total sense (e.g., nofollowed internal links to a login page).

However, if there’s no obvious reason for the links to be nofollowed, remove the nofollow tag.

That’s the case here. For some reason, we have a nofollowed link from one blog post to another.

PRO TIP

For a more granular breakdown of internal nofollowed link issues on your website, run a fresh crawl in [Ahrefs Site Audit](https://ahrefs.com/site-audit).

Not only does this give you 100% fresh data, but it also alerts you to a bunch of specific issues relating to internal and external nofollow links.

Example of issues related to nofollow internal links in [Ahrefs Site Audit](https://ahrefs.com/site-audit)

Learn how to set up your first crawl in Site Audit in [this video](https://www.youtube.com/watch?v=LjinWqfGyVE):

## Final thoughts

Nofollow links play a vital role when it comes to SEO.

Hopefully, this guide successfully armed you with the knowledge you need to make nofollow links work *for* you… not *against* you.

Before I wrap this up, I have one final—probably quite obvious—point: If you’re actively building links to your website, then it makes sense to prioritize the building of followed links. These are the ones that pass PageRank and have a direct impact on SEO.

In [Site Explorer](https://ahrefs.com/site-explorer), all our backlink-related reports have “dofollow” and “nofollow” filters.

That makes it easy to prioritize when you’re [analyzing competitors’ backlink profiles for replicable links](https://ahrefs.com/blog/find-competitors-backlinks/), or building a list of “[skyscraper](https://ahrefs.com/blog/skyscraper-technique/)” prospects, or whatever the case may be.

Do you still have questions? Hit me up in the comments below or [via Twitter](https://twitter.com/joshuachardwick?lang=en).
