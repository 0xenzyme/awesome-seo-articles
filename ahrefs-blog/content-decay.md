---
title: "What Is Content Decay? (And How to Fix It Before It Tanks Your Traffic)"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "content-decay"
url: "https://ahrefs.com/blog/content-decay/"
canonical: "https://ahrefs.com/blog/content-decay/"
author: "Louise Linehan"
published: "2026-03-13T11:34:48+00:00"
updated: "2026-05-31T07:45:23+00:00"
categories:
  - "Content Marketing"
  - "General SEO"
freshness_reasons: []
fetched_at: "2026-06-12T11:23:10+00:00"
status_code: 200
html_hash: "64485e1fcaf485071472c170e542cd1bf7232211aeafb17471ba6a74c294684b"
clean_word_count: 3303
clean_char_count: 20788
---
# What Is Content Decay? (And How to Fix It Before It Tanks Your Traffic)

Every piece of content you’ve ever published is slowly dying.

That may sound defeatist, but unfortunately that’s just how the web works.

Rankings slip, competitors improve, search intent shifts, and what was your best-performing article two years ago might be leaking traffic right now without you even noticing.

![A graph shows three peaks of "traffic you hustle to get" that quickly decay to "no traffic."](https://ahrefs.com/blog/wp-content/uploads/2026/03/a-graph-shows-three-peaks-of-traffic-you-hustle-t.png)

This is content decay: the gradual, often invisible decline of a page’s organic traffic and rankings.

In this guide, I’ll show you how to find decaying content using Ahrefs, decide what to do about it, execute the fix, and set up a process so you catch it earlier next time.

## What is content decay?

Content decay is the gradual decline in a page’s organic traffic and rankings over time.

Unlike a sudden traffic drop caused by a Google penalty or a major algorithm update, decay is slow—it happens over months, sometimes years, and it’s easy to miss until significant ground has been lost.

Think of content as having a lifecycle.

Most articles follow the same rough arc:

- **Early traction:** The article gets indexed, starts showing up in search results, and picks up a few early links or shares. Traffic is low but moving in the right direction.
- **Growth**: Rankings climb, organic traffic builds, and the article starts pulling in a consistent stream of visitors.
- **Traffic peak**: The article reaches its highest point of visibility and clicks, typically when it’s ranking in top positions for its target keywords.
- **Slow plateau**: Traffic looks stable on the surface, but rankings are quietly slipping. The content is starting to age and competitors are catching up.
- **Decline**: Fresher, more authoritative content pushes the article down the SERPs, and traffic drops off.

Most content teams invest heavily in the first three phases and almost nothing in the last two.

The other thing worth noting: content decay now has two dimensions.

A page can lose ground in Google rankings *and* disappear from AI-generated answers independently.

It’s possible to still rank on page one but be consistently absent from ChatGPT recommendations or Google AI Overviews—and those are increasingly where decisions get made. I’ll cover both.

## What causes content decay?

There’s rarely one cause. Usually it’s a combination of the following.

### Age and freshness

Google favors recently updated content for many query types—particularly anything with an implicit freshness signal, like “best [X]” or “how to [Y]”.

This is Google’s “[query deserves freshness](https://ahrefs.com/seo/glossary/query-deserves-freshness-qdf)” system in action.

Content that hasn’t been touched in two years is at a structural disadvantage against well-maintained competitor content, even if that older article is objectively better and more comprehensive.

AI systems compound this. Our own research shows that URLs cited by AI assistants are [25.7% “fresher”](https://ahrefs.com/blog/do-ai-assistants-prefer-to-cite-fresh-content/) than organic SERP results on average.

And AI expert [Metehan Yeşilyurt](https://tr.linkedin.com/in/metehanyesilyurt) identified a `URL_freshness_score` within ChatGPT’s configuration files that suggests it favors newer content.

In [his research](https://metehan.ai/blog/i-found-it-in-the-code-science-proved-it-in-the-lab-the-recency-bias-thats-reshaping-ai-search/), he discovered studies showing that artificially refreshing publication dates can improve AI ranking positions by as much as **95 places**.

All of this is to say that AI is even more biased toward recency than traditional Google.

### Competitor improvement

Your content can decay if someone publishes a better article targeting the same keywords.

Maybe it earns more links, or matches intent more precisely, and over the course of the year it displaces yours.

This is the most common cause of content decay, and it’s the hardest to notice because the displacement happens so gradually.

### Search intent shift

[Search intent](https://ahrefs.com/blog/search-intent/) for a keyword can drift meaningfully over years, even if the keyword itself doesn’t change.

For instance, “LLM” used to mean “Master of Laws” but by 2024, “large language model” content dominated.

You can spot [search intent shifts](https://ahrefs.com/blog/search-intent-shift/) in Ahrefs’ SERP Overview tool—look for lots of “Lost” and “New” rankings, plus a low SERP similarity score.

Google’s SERP reflects the current dominant intents—if your article was written for an older version of the query, it loses relevance even without any change on your end.

### Internal keyword cannibalization

This one is underappreciated.

When you publish two or more articles targeting the same or similar keywords, they split authority instead of combining it.

All rank worse than a single authoritative piece would, and over time the newest article often quietly overtakes the older ones, which then decay without anyone realizing what happened.

## How to find decaying content with Ahrefs

The fastest way to find decaying content is to look at your site’s [Top Pages](https://ahrefs.com/academy/how-to-use-ahrefs/site-explorer/top-pages) filtered for traffic decline, then use [Content Changes](https://ahrefs.com/blog/content-changes/) to understand *why* each page is declining.

### Find your decaying content in Ahrefs Top Pages

Here are six quick steps to finding content decay in Ahrefs.

1. Go to [Ahrefs’ Site Explorer](https://ahrefs.com/site-explorer)
2. Enter your domain, and open the Top Pages report
3. Set the traffic filter to “Declining”
4. Select an “easy” Keyword Difficulty score
5. Set the date range to 12 months
6. Sort by negative traffic change.

The pages at the top of this list are your biggest traffic losers—your decay candidates.

I recommend setting a KD filter under 40.

This filters out pages where the real problem is a link authority gap rather than content quality.

Those need a different solution; content decay fixes only help where content is actually the issue.

### Use Content Changes to find the cause of decay

Once you’ve found a declining page, you need to understand *why* it’s declining before you decide what to do.

Open the page in [Site Explorer](https://ahrefs.com/site-explorer) and check the Content Changes timeline.

Look for green circle markers on the traffic graph—these show when changes to the page were made and how significant they were.

There are two patterns to watch for:

- **Traffic declined with no preceding changes:** This is classic decay. Your content stood still; the world moved on. The fix is a content refresh.
- **Traffic declined after a content change:** You may have accidentally degraded a page that was previously working. Compare the before/after content to see what was removed or altered.

This distinction matters a lot. Without it, you might refresh a page that actually needs its previous version restored.

### Check traffic and engagement in Google Search Console

In GSC, go to Performance → filter by page → compare date ranges (last 3 months vs. same period 1 year ago).

Look at impressions and CTR together:

- **Both declining:** This is a classic decay signal. You’re losing visibility and the clicks that come with it.
- **Impressions down, CTR up:** You’ve lost positions, but the users who still find you are engaged. Potentially recoverable.
- **Impressions flat, CTR down:** You’re still ranking, but something changed in the SERP around you — an AI Overview appeared, a featured snippet was added, or a competitor earned a rich result. This isn’t decay per se; it’s a SERP feature problem.

Beyond GSC’s click and impression data, analytics expert [Dana DiTomaso](https://www.linkedin.com/feed/update/urn:li:activity:7415006934896017408/) points to GA4’s engagement rate as another crucial early warning system for diagnosing traffic quality issues.

— [Dana DiTomaso on LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7415006934896017408)

### Prioritize your decay backlog

Now you have a list of decaying pages, but not all of them are worth fixing.

Prioritize by:

- **Business relevance:** Does the topic still matter to your audience and business?
- **Historical traffic peak:** How much did this page earn at its best?
- **Keyword Difficulty:** Is this a keyword you can still realistically win?

Pages that score high on all three should be fixed first—pages that score low on all three should be pruned.

## Update, consolidate, redirect, or prune? A decision framework

The right action depends on the page’s specific situation.

Applying the wrong fix—refreshing a page that should be consolidated, for example—wastes time and can make things worse.

| Situation | Action |
| --- | --- |
| Keyword still relevant; content is just outdated | Update/refresh |
| Two pages competing for the same keyword, one stronger | Consolidate weaker into stronger |
| Keyword no longer fits your strategy; page has backlinks | Redirect to a relevant page |
| Low-value keyword, minimal traffic, few backlinks | Prune (noindex or delete) |
| Page was poorly optimized from the start; topic still competitive | Rewrite from scratch |

### When to update

Update when the keyword still has search volume and business relevance, the page has a backlink profile worth preserving, and the structure is basically sound—you just need fresher data, updated examples, and coverage of new subtopics.

This is the most common scenario.

### When to consolidate

Consolidate when you have two or more articles competing for the same keyword.

Identify which one has better traffic, more links, and stronger authority—that’s the survivor.

Absorb the weaker article’s best content into it, then 301 redirect the weaker URL to the survivor.

Don’t skip the redirect: you want to consolidate the link equity, not just merge the content.

### When to redirect

If the keyword no longer fits your content strategy but the page has accumulated meaningful backlinks, redirecting preserves that link equity without the overhead of maintaining content you don’t care about.

Make sure the redirect destination is genuinely relevant—a redirect to your homepage doesn’t pass meaningful authority.

In this situation, it helps to think about the context of the links you’ve acquired.

What does the anchor text say? Are you gaining links for a specific statistic or quote?

If so, grab those “link magnets”, and add them to the piece of content you’re redirecting to.

### When to prune

[Content pruning](https://ahrefs.com/blog/content-pruning/) is the right call for pages that have minimal traffic, minimal backlinks, and low business value.

Left indexed, they dilute your topical authority, drag down the pages you actually care about, and create unnecessary maintenance work.

But pruning isn’t just about getting rid of the deadwood—when done right, it can lead to big gains.

SEO consultant [Jes Scholz](https://www.linkedin.com/feed/update/urn:li:activity:7417132754611638272) saw this firsthand with a client, where deleting over 60% of articles from their real estate website led to a significant increase in clicks.

But remember: Noindex is reversible if you change your mind; deletion is not.

## How to fix decaying content

Once you’ve decided a page is worth updating, here’s how to do it properly—not just cosmetically.

### 1. Start with a topical gap analysis

Before editing a word, run the decaying page through [Ahrefs’ AI Content Helper](https://ahrefs.com/ai-content-helper).

It grades your content against the top-ranking pages for your target keyword and highlights which topics they cover that you don’t.

These gaps are where you need to add or expand based on what’s actually satisfying the query right now.

Focus on gaps that reflect genuine searcher needs. Stuffing in keyword mentions for the sake of a better content score doesn’t work.

### 2. Update stale data and examples

Outdated statistics are one of the clearest signals to both readers and search engines that content hasn’t been maintained.

Replace every data point you can find a more recent source for.

You can try automating these updates. For example, [Buffer](https://www.linkedin.com/feed/update/urn:li:activity:7379507797840904192/) has developed a semi-automated process for content refreshes.

> “Buffer has 2,000+ articles on our blog. Refreshing content has always been a pain. We recently started experimenting with a semi-automated process for tackling this ongoing task through the use of some highly trained LLM agents, and the early results are impressive! We’ve already quadrupled our pace of refreshes, plus we’re getting 25% more articles done at a fraction of the previous cost. The best part? Search engines and LLMs are responding favourably to these refreshes. We’re seeing immediate, sustained upticks in traffic on most of our pieces.”
>
>
>
> Simon Heaton, Director of Growth Marketing, [Buffer](https://www.buffer.com)

We’ve even had a go at automating updates. Our Director of Content, [Ryan Law](https://uk.linkedin.com/in/thinkingslow), has used Claude Code to vibecode a blog post updating tool.

It makes instant recommendations for stat and resource updates…

This should help us stave off the symptoms of content decay for much longer.

Next on the agenda is vibecoding a tool to automatically update screenshots of features, and replace case studies with more recent examples.

### 3. Align with current search intent

Check the current SERP for your target keyword. What’s ranking now that wasn’t ranking when you wrote the article?

You can check this in the SERP Overview report in [Ahrefs Keywords Explorer](https://ahrefs.com/keywords-explorer).

For example, over the last year, SERPs for the term “How to start a blog” have seen 13 changes, with a SERP similarity of just 31/100.

From there, you can check whether the dominant format shifted—say, from a guide to a forum discussion, or from a listicle to a how-to.

Just check out the “Page type” column to figure this out…

Or hit “Identify intents” for a deeper breakdown of the overarching SERP intent.

For example, last year the SERPs for “How to start a blog” showed split intent: Reddit forum posts made up 34% of page one, and “How to” beginner guides accounted for 27%.

But by the following year, Reddit posts made up 60% of the SERPs, while “How to” beginner guides made up 22%.

If intent has shifted substantially, a targeted refresh won’t be enough—you may need a structural rewrite.

In this case, the SERP has shifted toward User Generated Content (UGC).

If you still wanted to show up for this topic, you would need to participate in relevant forum discussions, as well as refreshing your decaying content.

### 4. Strengthen on-page signals

Update your title tag and meta description. It’s true that [~80% of metadata gets rewritten by search engines](https://searchengineland.com/google-changed-76-of-title-tags-in-q1-2025-heres-what-that-means-454847) (e.g. sometimes your H1s and page anchor text gets repurposed [¹](https://www.linkedin.com/feed/update/urn:li:activity:7384212574797660160/)), but if the original version overperforms during testing, it will be used [²](https://www.linkedin.com/posts/markseo_seo-activity-7430284997485514752-4vRH?utm_source=share&utm_medium=member_desktop&rcm=ACoAABoEm7QBekJrKEnvC5H6nTAmYwOb4R1k5GE).

[Title tags](https://ahrefs.com/blog/title-tag-seo/) and meta descriptions are crucial for AI visibility too—many AI assistants use them to decide whether a page is worth reading further before citing it in a response.[¹](https://www.linkedin.com/feed/update/urn:li:activity:7339191681256177664/) [²](https://www.linkedin.com/feed/update/urn:li:activity:7399408916415094784/)

So, give your content the best possible chance; write a relevant title and description—but for the sake of efficiency, don’t agonize over it.

Links are also crucial. Add [internal links](https://ahrefs.com/blog/internal-links-for-seo/) from high-authority pages on your site to the refreshed article, and fix broken external links—these are a credibility signal and a minor technical issue.

For a really quick [SEO audit](https://ahrefs.com/blog/seo-audit/) of your content, bring up [Ahrefs Site Audit](https://ahrefs.com/site-audit), search your article URL, and hit the “Issues” tab.

### 5. Check AI visibility separately

After refreshing, use [Ahrefs Brand Radar](https://ahrefs.com/brand-radar) to check whether your updated content starts showing up in AI citations.

A page can recover in Google rankings and still be absent from ChatGPT responses and AI Overviews—these are separate visibility layers.

If you’re not [getting cited in AI answers](https://ahrefs.com/blog/answer-engine-optimization/) after a refresh, look at what competitor content *is* being cited.

That tells you which signals—structure, authority, external references—your content is still missing.

### 6. Re-promote after updating

Make your [content refresh](https://ahrefs.com/blog/republishing-content/) visible.

Send it to your email list, share it on social, and update the internal links pointing to it.

One great way to tackle updates is by involving contributors and subject matter experts from the outset.

You’re essentially engineering increased visibility, because you’re tapping into their network as well as your own.

Here’s an example from [Mateusz](https://pl.linkedin.com/in/mateusz-makosiewicz) in our blog team doing exactly that.

He updated a piece of content on [automotive SEO](https://ahrefs.com/blog/automotive-seo/), then reached out to industry experts and asked for their input and opinions.

This can be an especially effective strategy for social media distribution.

In short, redistribution signals activity and gets fresh eyes on the updated content.

If the changes are substantial enough, you can update the publish date—but only with genuine content improvements.

As SEO expert [Roxana Stingu](https://www.linkedin.com/feed/update/urn:li:activity:7384174543336022016/) points out

> “Google spent a lot of time refining how it handles [updates] and it can look back across multiple versions of a page and assess whether a change is meaningful enough outside of just getting a new timestamp.”
>
>
>
> Roxana Stingu, Head of Search & SEO, [Alamy](https://www.alamy.com)

In other words, changing the date without meaningfully changing the content can cause further decay.

## How to prevent content decay

The goal isn’t to eliminate decay—that’s impossible. The goal is to catch it early, before significant traffic is lost.

### Run a quarterly decay audit

Every quarter, go to Site Explorer → Top Pages → Declining filter (as I showed earlier) and flag any pages that have dropped more than 20% in traffic year-over-year.

Triage what you find: schedule high-priority pages for an immediate refresh sprint; add others to a backlog.

### Set up Ahrefs Alerts for your key keywords

[Ahrefs Alerts](https://ahrefs.com/alerts) can notify you when new content starts ranking for a keyword you’re targeting.

This is proactive competitor monitoring: you know a competitor is gaining ground before your rankings start sliding, giving you time to refresh before the damage compounds.

### Schedule annual updates for your most important content

For your highest-traffic, highest-business-value articles, put a calendar reminder to review them once a year—regardless of whether the metrics show a decline yet.

A modest update (a new statistic, a fresh screenshot, an expanded section) is much cheaper than a full rescue operation on a page that’s already lost 60% of its traffic.

### Build clusters, not silos

Interconnect related articles so authority distributes across your content rather than being split by competing pages.

When you publish something new, check whether it’s targeting a keyword already covered by an existing article—if so, either differentiate clearly or merge rather than fragmenting.

## Final thoughts

Content decay is going to happen to every article you’ve published—it’s just a matter of when. The question is whether you find out when you’re down 20% or when you’re down 80%.

Start auditing your content decay backlog this week in [Site Explorer](https://ahrefs.com/site-explorer).

Everything else—the decision framework, the refresh process, the prevention workflow—becomes much clearer once you know which specific pages you’re actually dealing with.

Got questions? Ping me [on LinkedIn](https://www.linkedin.com/in/louise-linehan/).
