---
title: "Google Documents Leaked & SEOs Are Making Some Wild Assumptions"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "google-documents-leaked-seos-are-making-some-wild-assumptions"
url: "https://ahrefs.com/blog/google-documents-leaked-seos-are-making-some-wild-assumptions/"
canonical: "https://ahrefs.com/blog/google-documents-leaked-seos-are-making-some-wild-assumptions/"
author: "Patrick Stox"
published: "2024-05-30T05:20:56+00:00"
updated: "2024-07-05T13:12:32+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "date_2024_watch"
fetched_at: "2026-06-12T11:33:40+00:00"
status_code: 200
html_hash: "a107767b842aa89c380c2558f336cafb6046f86b29d24e68795b2785850c05a4"
clean_word_count: 1589
clean_char_count: 9048
---
# Google Documents Leaked & SEOs Are Making Some Wild Assumptions

You’ve probably heard about the recent Google documents leak. It’s on every major site and all over social media.

## Where did the docs come from?

My understanding is that a bot called yoshi-code-bot leaked docs related to the Content API Warehouse on Github on March 13th, 2024. It may have appeared earlier in some other repos, but this is the one that was first discovered.

They were discovered by [Erfan Azimi](https://www.youtube.com/watch?v=AEb8_rbfFVw) who shared it with [Rand Fishkin](https://sparktoro.com/blog/an-anonymous-source-shared-thousands-of-leaked-google-search-api-documents-with-me-everyone-in-seo-should-see-them/) who shared it with [Mike King](https://ipullrank.com/google-algo-leak). The docs were removed on May 7th.

I appreciate all involved for sharing their findings with the community.

## Google’s response

There was some debate if the documents were real or not, but they mention a lot of internal systems and link to internal documentation and it definitely appears to be real.

A Google spokesperson released the following statement to [Search Engine Land](https://searchengineland.com/google-responds-to-leak-documentation-lacks-context-442705):

> We would caution against making inaccurate assumptions about Search based on out-of-context, outdated, or incomplete information. We’ve shared extensive information about how Search works and the types of factors that our systems weigh, while also working to protect the integrity of our results from manipulation.

## SEOs interpret things based on their own experiences and bias

Many SEOs are saying that the ranking factors leaked. I haven’t seen any code or weights, just what appear to be descriptions and storage info. Unless one of the descriptions says the item is used for ranking, I think it’s dangerous for SEOs to assume that all of these are used in ranking.

Having some features or information stored does not mean they’re used in ranking. For our search engine, [Yep.com](https://yep.com/), we have all kinds of things stored that might be used for crawling, indexing, ranking, personalization, testing, or feedback. We store lots of things that we haven’t used yet, but likely will in the future.

What is more likely is that SEOs are making assumptions that favor their own opinions and biases.

It’s the same for me. I may not have full context or knowledge and may have inherent biases that influence my interpretation, but I try to be as fair as I can be. If I’m wrong, it means that I will learn something new and that’s a good thing! SEOs can, and do, interpret things differently.

[Gael Breton](https://twitter.com/GaelBreton) said it well:

https://twitter.com/GaelBreton/status/1795508097026269589

I’ve been around long enough to see many SEO myths created over the years and I can point you to who started many of them and what they misunderstood. We’ll likely see a lot of new myths from this leak that we’ll be dealing with for the next decade or longer.

Let’s look at a few things that in my opinion are being misinterpreted or where conclusions are being drawn where they shouldn’t be.

### SiteAuthority

As much as I want to be able to say Google has a Site Authority score that they use for ranking that’s like DR, that part specifically is about compressed quality metrics and talks about quality.

I believe DR is more an effect that happens as you have a lot of pages with strong [PageRank](https://ahrefs.com/blog/google-pagerank/), not that it’s necessarily something Google uses. Lots of pages with higher PageRank that internally link to each other means you’re more likely to create stronger pages.

- Do I believe that PageRank could be part of what Google calls quality? Yes.
- Do I think that’s all of it? No.
- Could Site Authority be something similar to DR? Maybe. It fits in the bigger picture.
- Can I prove that or even that it’s used in rankings? No, not from this.

From some of the Google testimony to the US Department of Justice, we found out that quality is often measured with an Information Satisfaction (IS) score from the raters. This isn’t directly used in rankings, but is used for feedback, testing, and fine-tuning models.

We know the quality raters have the concept of [E-E-A-T](https://ahrefs.com/blog/eeat-seo/), but again that’s not exactly what Google uses. They use signals that align to E-E-A-T.

Some of the E-E-A-T signals that Google has mentioned are:

- PageRank
- Mentions on authoritative sites
- Site queries. This could be “site:http://ahrefs.com E-E-A-T” or searches like “ahrefs E-E-A-T”

So could some kind of PageRank scores extrapolated to the domain level and called Site Authority be used by Google and be part of what makes up the quality signals? I’d say it’s plausible, but this leak doesn’t prove it.

I can recall 3 patents from Google I’ve seen about quality scores. One of them aligns with the signals above for site queries.

I should point out that just because something is patented, doesn’t mean it is used. [The patent](https://patentimages.storage.googleapis.com/07/09/65/91ec9e0455ddcf/US9760641.pdf) around site queries was written in part by Navneet Panda. Want to guess who the Panda algorithm that related to quality was named after? I’d say there’s a good chance this is being used.

The others were around n-gram usage and seemed to be to calculate a quality score for a new website and another mentioned time on site.

### Sandbox

I think this has been misinterpreted as well. The document has a field called hostAge and refers to a sandbox, but it specifically says it’s used “to sandbox fresh spam in serving time.”

To me, that doesn’t confirm the existence of a sandbox in the way that SEOs see it where new sites can’t rank. To me, it reads like a spam protection measure.

### Clicks

Are clicks used in rankings? Well, yes, and no.

We know Google uses clicks for things like personalization, timely events, testing, feedback, etc. We know they have models upon models trained on the click data including navBoost. But is that directly accessing the click data and being used in rankings? Nothing I saw confirms that.

The problem is SEOs are interpreting this as CTR is a ranking factor. Navboost is made to predict which pages and features will be clicked. It’s also used to cut down on the number of returned results which we learned from the DOJ trial.

As far as I know, there is nothing to confirm that it takes into account the click data of individual pages to re-order the results or that if you get more people to click on your individual results, that your rankings would go up.

That should be easy enough to prove if it was the case. It’s been tried many times. I tried it years ago using the Tor network. My friend [Russ Jones](https://twitter.com/rjonesx) (may he rest in peace) tried using residential proxies.

I’ve never seen a successful version of this and people have been buying and trading clicks on various sites for years. I’m not trying to discourage you or anything. Test it yourself, and if it works, publish the study.

Rand Fishkin’s tests for searching and clicking a result at conferences years ago showed that Google used click data for trending events, and they would boost whatever result was being clicked. After the experiments, the results went right back to normal. It’s not the same as using them for the normal rankings.

### Authors

We know Google matches authors with entities in the knowledge graph and that they use them in Google news.

There seems to be a decent amount of author info in these documents, but nothing about them confirms that they’re used in rankings as some SEOs are speculating.

## Was Google lying to us?

What I do disagree with whole-heartedly is SEOs being angry with the Google Search Advocates and calling them liars. They’re nice people who are just doing their job.

If they told us something wrong, it’s likely because they don’t know, they were misinformed, or they’ve been instructed to obfuscate something to prevent abuse. They don’t deserve the hate that the SEO community is giving them right now. We’re lucky that they share information with us at all.

If you think something they said is wrong, go and run a test to prove it. Or if there’s a test you want me to run, let me know. Just being mentioned in the docs is not proof that a thing is used in rankings.

## Final Thoughts

While I may agree or I may disagree with the interpretations of other SEOs, I respect all who are willing to share their analysis. It’s not easy to put yourself or your thoughts out there for public scrutiny.

I also want to reiterate that unless these fields specifically say they are used in rankings, that the information could just as easily be used for something else. We definitely don’t need any posts about Google’s 14,000 ranking factors.

If you want my thoughts on a particular thing, message me on [X](https://twitter.com/patrickstox) or [LinkedIn](https://www.linkedin.com/in/patrickstox/).
