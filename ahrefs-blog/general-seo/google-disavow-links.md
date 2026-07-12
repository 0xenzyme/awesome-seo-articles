---
title: "Google's \"Disavow Links Tool\": The Complete Guide"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "google-disavow-links"
url: "https://ahrefs.com/blog/google-disavow-links/"
canonical: "https://ahrefs.com/blog/google-disavow-links/"
author: "Derek Gleason"
published: "2018-04-26T10:01:32+00:00"
updated: "2024-03-18T12:36:27+00:00"
categories:
  - "General SEO"
  - "Link Building"
freshness_reasons:
  - "date_2024_watch"
  - "time_sensitive_title"
fetched_at: "2026-06-12T11:33:31+00:00"
status_code: 200
html_hash: "2d920eac494ba42c35daccba3310775387f17e73d266998c6dd965d5e8d6679b"
clean_word_count: 3977
clean_char_count: 24659
---
# Google’s “Disavow Links Tool”: The Complete Guide

Good backlinks help a site rank higher. Bad backlinks can cause problems. You have only limited control over which links point to your site.

If you’ve spent any time in SEO, these are things you already know.

You also know that [Google’s “Disavow Links Tool”](https://www.google.com/webmasters/tools/disavow-links-main) can help protect your site from link-related penalties.

Even with that knowledge, most SEOs—even leading experts—answer the question, “Should I disavow?” with an emphatic, “It depends.”

And SEO “best practices” (e.g., “Disavow only bad links that are harming your site”) assume that it’s easy to separate links that boost rankings from those that threaten them.

In this article, I’ll explain when you should (and shouldn’t) disavow links, and how to identify “bad” links.

But first, you should understand why Google created the disavow tool and how its use has changed over the years.

## What is Google’s “Disavow Links Tool” and why did they create it?

Google’s Disavow Links Tool lets you tell Google to ignore specific backlinks for ranking purposes.

Like a [rel=”canonical” tag](https://support.google.com/webmasters/answer/139066?hl=en), a disavow file is a “[strong suggestion rather than a directive](https://webmasters.googleblog.com/2012/10/a-new-tool-to-disavow-links.html).”

The technical process is simple: You submit a text file containing the linking pages or domains that you want to disavow via Google Search Console (GSC).

![](https://ahrefs.com/blog/wp-content/uploads/2018/04/disavow-links-search-console.jpg)

*(More on this later.)*

The decision-making process—determining which domains should be in the disavow file or whether you should disavow at all—is more complicated.

To make that determination, you need to understand:

1. Why Google created the Disavow Links Tool;
2. How its importance has changed with algorithm updates.

### Why did Google create the Disavow Links Tool?

Google has fought spammy link-building for more than a decade.

Its first attempt to reduce link spam was the introduction of [the “nofollow” attribute](http://microformats.org/wiki/rel-nofollow) in January 2005, which sought to combat comment spam like this:

While Google continued to adjust its algorithm in subsequent years, the next significant change targeting link schemes didn’t occur until April 2012, when Google rolled out the [first Penguin algorithm](https://search.googleblog.com/2012/04/another-step-to-reward-high-quality.html).

Penguin was an “external filter” through which search results passed. That technical detail meant that an algorithmic penalty could persist for months after a thorough site clean-up.

Google supplemented algorithmic penalties with [Manual Actions](https://support.google.com/webmasters/answer/2604824?hl=en&visit_id=1-636566154205904353-4034071654&rd=1#unnatural-links-to-your-site), which it sent to webmasters if it “detected a pattern of unnatural artificial, deceptive, or manipulative outbound links.”

An entire site could be demoted even when a link scheme targeted a subsection or single page of a website.

The Disavow Links Tool, then, gave webmasters more control over the links that Google used to rank—or potentially penalize—their site.

Even [at its rollout](https://webmasters.googleblog.com/2012/10/a-new-tool-to-disavow-links.html) in October 2012, Google believed the disavow tool applied to a limited number of webmasters:

> If you’ve been notified of a manual spam action based on ‘unnatural links’ pointing to your site, this tool can help you address the issue. If you haven’t gotten this notification, this tool generally isn’t something you need to worry about.
>
>
>
> Jonathan Simon, Webmaster Trends Analyst, [Google](https://webmasters.googleblog.com/2012/10/a-new-tool-to-disavow-links.html)

The tool wasn’t intended then (or now) as a first line of defense against link-based penalties.

[As Matt Cutts explained in a 2012 interview](https://searchengineland.com/matt-cutts-qa-how-to-use-google-link-disavow-tool-137664), it could expedite site recovery *after* manual methods were exhausted:

> Right now it can be a difficult task to clean up a site’s backlinks, and from listening to the SEO community we wanted to provide a tool that could help **after site owners had already taken substantial steps to try to clean up their site’s backlinks**.
>
>
>
> Matt Cutts, former Head of Web Spam, [Google](https://searchengineland.com/matt-cutts-qa-how-to-use-google-link-disavow-tool-137664)

Through the first three iterations of Penguin, most SEOs believed that disavowing links was essential to protect sites from lengthy demotions in search results.

Consensus changed with [the introduction of Penguin 4.0](https://webmasters.googleblog.com/2016/09/penguin-is-now-part-of-our-core.html), which Google released in September 2016.

Penguin 4.0 marked Google’s update to a “real-time” Penguin algorithm, which also allowed Google to target link spam at a page-specific level.

Most importantly, it marked [a fundamental shift from “demoting” to “devaluing”](https://www.facebook.com/barryschwartz/posts/10154317937755783?pnref=story)—from algorithmic wrath to algorithmic apathy:

And so began the great debate: Is disavowing still necessary? And if so, when?

## When should (or shouldn’t) you disavow?

What constitutes a “low-quality” link? What is a “bad” directory? What is a “good” [guest post](https://ahrefs.com/blog/guest-blogging/)?

[According to Google](https://support.google.com/webmasters/answer/66356?hl=en), a low-quality link is one that is:

> *[…] intended to manipulate PageRank or a site’s ranking in Google [or] may be considered part of a link scheme and a violation of Google’s Webmaster Guidelines. This includes any behavior that manipulates links to your site or outgoing links from your site.*

[Gabriella Sannino](https://twitter.com/seocopy?lang=en), the founder of Level343, simplifies that definition for her link audits:

> A good rule of thumb is, if the link isn’t relevant to your site or your users, it probably shouldn’t be in your profile.
>
>
>
> Gabriella Sannino, Founder, [Level343](https://level343.com/)

[Marie Haynes](https://twitter.com/Marie_Haynes) applies a similar logic:

> Does the link serve any purpose outside of SEO? Does this link have legitimate potential to bring business to my site?
>
>
>
> Marie Haynes, Owner, [Marie Haynes Consulting](https://www.mariehaynes.com/)

In contrast, Google notes that high-quality links [are often “editorially earned”](https://support.google.com/webmasters/answer/66356?hl=en):

> *Links are usually editorial votes given by choice, and the more useful content you have, the greater the chances someone else will find that content valuable to their readers and link to it.*

There’s plenty of space for subjective interpretation between these definitions:

Still, there are some [unambiguously “bad” links](https://ahrefs.com/blog/bad-links/), and taking the time to investigate their origin and timing can help identify if a client is unknowingly paying another agency to build them.

(This can help you stop the leak instead of just bailing water.)

Here are six clear-cut sources of bad links:

### 1. Paid links

Google targets a subset of [paid links](https://ahrefs.com/blog/buy-backlinks/): non-editorial, dofollow links that are clearly designed to pass [PageRank](https://ahrefs.com/blog/google-pagerank/).

While some paid links may be difficult to detect, there are a few red flags:

- Dofollow site-wide links with exact-match anchor text;
- Dofollow links from unrelated sites/content;
- Dofollow links from pages with obvious footprints such as “Sponsored Post.”

### 2. Private Blogging Networks (PBNs)

Google began [actively de-indexing PBNs in 2014](https://searchengineland.com/google-targets-sites-using-private-blog-networks-manual-action-ranking-penalties-204000). They still exist, but links from PBNs are not part of any [white-hat link-building](https://ahrefs.com/blog/white-hat-link-building-techniques/) strategy.

PBNs are a focus of link audits by [Ryan Stewart](https://twitter.com/ryanwashere) and his team at WEBRIS, who

> […] generally focus on links that were built by humans. The internet is full of garbage and sites tend to pick up random links that look spammy but are really just ignored by the algorithm. The only links we disavow are ones from PBNs and low-quality domains with exact-match anchors.
>
>
>
> Ryan Stewart, Founder, [WEBRIS](https://webris.org/)

### 3. Low-quality directories

To identify a low-quality directory, ask yourself: Do you expect to get referral traffic from the listing? If the answer is “No,” it’s probably low quality.

While low-quality directory submissions haven’t worked for years (and many now use nofollow links that eliminate the need to disavow), some unethical SEOs claim the contrary when pitching their “services” to unsuspecting website owners.

A handful of high-quality or niche-specific directories might be worth the fee, but this tactic is not an effective way to grow [site authority](https://ahrefs.com/website-authority-checker).

### 4. Comment and forum spam

Commenting on relevant, authoritative sites and forums and linking back to related content on your site is [not only allowed but encouraged by Google](https://searchenginewatch.com/sew/news/2307497/matt-cutts-on-blog-comments-links-spam-use-your-name-not-keywords).

The problem is the scaling or automation of that process. Many comment systems now make all links nofollow by default, so there’s likely little risk or reward here.

### 5. Hacked sites

There’s no gray area when it comes to hacked websites.

Links from hacked sites will all but guarantee a penalty from Google, and participating in the hacking can also get you in real trouble. (It’s, you know, illegal.)

### 6. Negative SEO

The most common type of [negative SEO](https://ahrefs.com/blog/negative-seo/) is backlink spamming—intentionally linking back to a competitor from hundreds or thousands of low-quality websites.

If you’ve ever logged into [Site Explorer](https://ahrefs.com/site-explorer) and seen a massive, unwarranted jump in referring domains, it could indicate that your site has been attacked:

Receiving thousands of spammy links in a short period will arouse Google’s suspicion, potentially resulting in a penalty.

### What are the risks of disavowing?

Even with a firm grasp of which links are “bad” and which are “good,” disavowing remains risky. A link that looks “bad” may still help your site.

Google has [continued to caution users](https://support.google.com/webmasters/answer/2648487) about the use of the disavow tool:

Despite this warning, the fear of a penalty has led many SEOs to prune links aggressively.

Years ago, this overzealous approach was aided by a misinterpretation of [advice from Cutts](https://www.mattcutts.com/blog/what-to-expect-in-seo-in-the-coming-months/#comment-4405076) about the use of the disavow tool:

While the takeaway should have been an endorsement of domain-level rather than URL-level disavowal (read past the highlighted portion above), the enduring sound bite for many was to “disavow with a machete, not a scalpel.”

[Cutts is also on record](https://youtu.be/393nmCYFRtA?t=6m20s) noting that an effort to “reavow” links takes more time and may weaken the signals sent by those links:

> [If you want to ‘reavow’ a link, then that will] take a lot longer, and we might not even give it the same weight, if we start to allow it to be reavowed.
>
>
>
> Matt Cutts, former Head of Web Spam, Google

With so much at stake, only a handful of situations weight the risk-reward calculation heavily toward reward.

### So when should you disavow?

A Manual Action is the one absolute “yes” when it comes to the use of the disavow tool:

Beyond that, there are two instances when disavowing links is probably (but not definitely) the right choice:

1. **A dramatic jump in low-quality links that correlates with a sharp drop in rankings.** Correlation is not causation; however, a stable site that disappears from search results after an influx of bad links is a prime candidate for link disavowal. (Even without a sharp drop, a proactive disavow can protect a site.)
2. **If you can connect a suspicious backlink profile to a client’s admission that they paid for links in the past** (or still are today), a disavow of those links makes sense.

Nonetheless, experts remain divided in these and other situations that can fall into a “gray area.”

A sample of post–Penguin 4.0 tweets reveals a range of perspectives:

> Dwindling need for the disavow tool. Still there if you need it, but Google is handling spammy links now. <https://t.co/mFDY7EbWjd>
>
> — Glenn Gabe (@glenngabe) [March 15, 2018](https://twitter.com/glenngabe/status/974417837782532097?ref_src=twsrc%5Etfw)

> My Experience:
>  1) Google’s Disavow Tool works
>  2) It can also do damage
>  3) Poll says 62% of SEOs use it, 38% don’t <https://t.co/hryP62JzvA> [pic.twitter.com/mpJ6BY353e](https://t.co/mpJ6BY353e)
>
> — Cyrus (@CyrusShepard) [September 12, 2017](https://twitter.com/CyrusShepard/status/907686866715119618?ref_src=twsrc%5Etfw)

> Do We Still Need Disavow after Penguin 4.0? <https://t.co/hhGAQYHLSh> Penguin isn’t GONE, people. It’s part of the core algo now. Use Disavow
>
> — Ian Lurie (@portentint) [April 6, 2017](https://twitter.com/portentint/status/850056022655979520?ref_src=twsrc%5Etfw)

> And the disavow IS NOT dead <https://t.co/ovJ7tOxokE>
>
> — Rand Fishkin (@randfish) [March 16, 2017](https://twitter.com/randfish/status/842266347199434752?ref_src=twsrc%5Etfw)

> Removing Disavow File… 5 Months On = 37.31% Increase in Organic Traffic <https://t.co/RmEpoFC04D> by [@kevgibbo](https://twitter.com/kevgibbo?ref_src=twsrc%5Etfw)
>
> — Paul Shapiro (@fighto) [March 9, 2017](https://twitter.com/fighto/status/839857328065241089?ref_src=twsrc%5Etfw)

> Google Penguin doesn’t penalize for bad links – or does it? - You technically no longer need to use the disavow… <https://t.co/YhCcAs7ZNa>
>
> — duane forrester (@DuaneForrester) [September 28, 2016](https://twitter.com/DuaneForrester/status/781181042052911104?ref_src=twsrc%5Etfw)

When we asked a few other well-known SEOs about if they still disavow, the answer was often “Yes, but…”:

[Ryan Bartlett](https://twitter.com/seo_direct), founder of SEO Direct:

> Yes, we still use it if their link profile appears to be very spammy. Although, it doesn’t seem to have as much of an impact as it used to
>
>
>
> Ryan Bartlett, Founder, [SEO Direct](https://www.seodirect.org/)

Marie Haynes, founder of Marie Haynes Consulting:

> I do use the disavow tool today, but not nearly as much as I did prior to Penguin 4.0. In the past I would have entire days dedicated to link auditing, but that rarely happens now.
>
>
>
> Marie Haynes, Owner, [Marie Haynes Consulting](https://www.mariehaynes.com/)

Google is divided, too. Shortly after Penguin 4.0’s release, John Mueller confirmed that the update had no effect on disavow recommendations:

He also noted that [it remains valuable](https://www.seroundtable.com/google-clarifies-disavow-usage-24772.html) if you’re seeking peace of mind:

> *The disavow file is a great way to just like preemptively say well I know about these issues, I don’t want to lose any sleep over them, I’m just going to disavow them and get them taken out of the equation.*

However, while not contradicting Mueller’s advice, [Gary Illyes was more dismissive](https://www.seroundtable.com/google-disavow-manual-action-24751.html) of the need to disavow:

> “If you do not have a manual action then you do not need to submit a disavow!” [@methode](https://twitter.com/methode?ref_src=twsrc%5Etfw) [#Pubcon](https://twitter.com/hashtag/Pubcon?src=hash&ref_src=twsrc%5Etfw) Great questions by [@jimboykin](https://twitter.com/jimboykin?ref_src=twsrc%5Etfw)
>
> — Brian McDowell (@brian\_mcdowell) [November 8, 2017](https://twitter.com/brian_mcdowell/status/928314820289368065?ref_src=twsrc%5Etfw)

Illyes also confessed that [he’s never submitted a disavow file](https://www.ithinkmedia.co.uk/blog/seo/gary-illyes-interview-brighton-seo-2017/) for his site—or even evaluated his backlink profile:

> *I run my own site, which gets about, perhaps 100,000 visits per week. It’s been up for four years maybe and I don’t have a disavow file, I don’t even know who links to me.*

So how do you make the right choice with so much “gray area”? It requires a holistic evaluation of the client, the site, and your job.

Because disavowing bad links will have no impact on many sites, you must first **make a persuasive case to a client about why it’s valuable.**

You must also **position****your disavow effort within a hierarchy of SEO opportunities.**

Disavowing links is usually a secondary priority that protects gains made through other, more valuable SEO tasks.

That said: What would the consequences be if the site were penalized?

**Know that a penalty is a uniquely unforgivable sin for an SEO.** It’s one of the few specific events for which an agency may lose their client or an analyst their job.

(This is what keeps me up at night—not an irrational belief in the likelihood of a penalty but the very rational fear of its consequences.)

Ultimately, performing a link audit is the only way to know whether or not there is any real need to disavow.

Here’s how to do it.

## How to identify and disavow bad links

> ***IMPORTANT!** Remember, Google’s first recommendation is to remove low-quality links from the web. While this rarely works, you may still need to try if you’re filing a reconsideration request.*

If you know what a bad link looks like, the rest of the process is merely applying that knowledge across a site’s entire backlink profile.

### Step 1. Perform a high-level link audit

Regular, high-level link monitoring can help determine whether a deep dive is necessary.

Three reports in [Site Explorer](https://ahrefs.com/site-explorer) make that process pretty efficient: the “Referring domains” graph, the “Anchors cloud,” and the “CTLDs distribution” map.

The best part of these reports is that they provide a *relative* rather than *absolute* assessment—monitoring takes the same amount of time regardless of the size of the backlink profile.

**Referring domains graph:** The referring domains graph can identify a spike in links, which is often caused by link spam (self-directed or part of a negative SEO attack).

For the optimists out there, it may also reveal when a piece of [linkbait](https://ahrefs.com/blog/link-bait/) went “viral.”

In any case, high “link velocity” is cause for further investigation.

**Anchors cloud:** The anchors cloud can help identify whether links seem suspiciously “over-optimized.”

In this example from Blanchard’s Coffee Roasting Co., every anchor in the cloud is a brand term:

Brand-heavy anchor text is a safe bet that the link profile is natural and won’t raise any red flags.

Compare that to the anchor cloud of a hacked site for a family-run lamp shop in Sweden:

If only a single term or two raises suspicion, you can choose the “Anchors” report and “Details” to see the referring domains and backlinks with the concerning anchor text:

**CTLDs distribution map:** The country code top-level domain (CTLD) map is also a quick way to evaluate a backlink profile.

This example is troubling. The website is for a SaaS provider with an exclusively U.S. client base, yet its most common CTLDs are from Colombia, Libya, and Russia:

If everything looks good across these three reports, you can probably move on to something else.

However, if you’re growing increasingly suspicious, it’s time for a full link audit.

### Step 2: Perform a full link audit (if necessary)

The quality of a link audit depends heavily on the comprehensiveness of the source materials.

For the fullest possible picture, consider pulling [Google Search Console](https://www.google.com/webmasters/tools/home) data into your backlink analysis. In most cases, however, the link profile in Ahrefs can serve as a stand-alone source.

Go to **Site Explorer** -> **Enter your domain** -> **Backlink Profile** -> **Referring Domains** -> **Filter for dofollow links** -> **Sort by DR (low to high)**

Quick tip

Do you prefer working in a spreadsheet?

Hit “Export” to download the data in Excel format. 🙂

Two markers are good places to start link evaluation:

- Low DR;
- Unusual TLDs.

Neither is a guarantee that a link is bad, but together the metrics offer a useful way to sort links.

You should already have sorted by DR (low to high), but you can also use the built-in filters to filter for specific TLDs.

E.g., .ru, .cn, etc.

This example from a fitness blog has it all: low DR, a spammy domain name and page title, and spammy anchor text.

Disavow such spammy links at the root-domain level. If an offending link comes from a trusted domain, disavow it at the URL level.

[As Illyes has emphatically noted](https://www.ithinkmedia.co.uk/blog/seo/gary-illyes-interview-brighton-seo-2017/), do not disavow major domains because of a single strange link:

> *I was looking at people who disavowed links from CNN and from the telegraph and whatever because they just didn’t know why would, or why did they get that link. That was bat shit stupid.*

You can flag domains for disavow in your spreadsheet or directly in Ahrefs. Check the boxes and click “Disavow Domains” next to any domains you want to add to your list:

The next time you export your disavow file from Ahrefs, it will include these domains.

If you want to reavow the domains, the process is simple (if only it were this easy in Google):

If a domain falls into a gray area, flag it in a spreadsheet as “questionable.” After plowing through a full backlink profile, it’s easier to spot patterns among “questionable” links to help decide whether to disavow them.

Once you’ve identified all the domains you want to disavow, just format your list for the disavow file and upload it in GSC.

### Step 3. Format and upload your list to Google’s Disavow Links Tool

Google details the [step-by-step process](https://support.google.com/webmasters/answer/2648487?hl=en) for disavowing links in GSC, including how to format the text file.

Before you create a new disavow file, [download the most recent one](https://www.google.com/webmasters/tools/disavow-links-main) from GSC. A disavow list is cumulative, and a previous webmaster or agency may have already submitted a disavow file.

(If you didn’t create the existing disavow file, review it before adding to it. A prior effort may have disavowed valuable links.)

Formatting a new disavow file is straightforward, and GSC will alert you of any errors upon submission. Most errors result from a failure to strip the protocol or subdomain prefix from the root domain.

If you’ve disavowed links within Ahrefs, you can use Ahrefs to format your disavow file for you.

On the main Dashboard screen, click “Disavow links” in the row with the desired website, then choose “Export.” Check the “Save as TXT for upload to Google Disavow Tool” box and click “Ok”:

You can add comments to annotate each update of your disavow file:

Just don’t waste your time with any explanations or pleading to the non-sentient machine that will process it. These comments are for you—not Google.

Also, don’t worry that submitting a disavow file will make Google more likely to investigate your site’s links. [(It won’t.)](https://twitter.com/methode/status/892682930815979520)

### Step 4. Log your changes and monitor progress

It may take weeks for the effects of a disavow effort to become visible. Google needs to recrawl the disavowed links to adjust its evaluation of your site’s backlink profile.

Annotate the disavow file upload in Google Analytics (or another analytics platform) and monitor the site carefully.

You can also upload the submitted disavow file back to Ahrefs:

This will give you cleaner link data in Ahrefs and expedite the disavowal process in the future.

## Final thoughts

The Disavow Links Tool has given webmasters more control over how Google evaluates the links pointing to their site. That control was vital in the pre-Penguin 4.0 era.

Penguin 4.0 has changed some analyst perspectives, but monitoring and assessing a backlink profile remains a core part of SEO—regardless of whether you disavow.

Now it’s your turn: How are you reshaping your approach to link monitoring and disavowal in 2018?

Share your expertise by joining the conversation below.
