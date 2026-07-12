---
title: "The SEO Process in a Nutshell (Updated for AI Search)"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "seo-process"
url: "https://ahrefs.com/blog/seo-process/"
canonical: "https://ahrefs.com/blog/seo-process/"
author: "Mateusz Makosiewicz"
published: "2022-06-28T06:59:10+00:00"
updated: "2026-04-30T19:40:04+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "ai_search_topic"
fetched_at: "2026-06-12T12:07:10+00:00"
status_code: 200
html_hash: "cc8a5a0cac8621dbeb4f7927016369f67cc07184a9af7f50299f5b70f676e57f"
clean_word_count: 3664
clean_char_count: 22846
---
# The SEO Process in a Nutshell (Updated for AI Search)

Search engine optimization (SEO) is the practice of growing a website’s traffic from organic search results. Here are the five general steps of the SEO process:

1. **Get your technicals right**. Make sure your website is crawlable and indexable.
2. **Find a keyword to target**. The topic of your page and the main source of organic traffic.
3. **Create an optimized page.** Both users and Google want useful and interesting content.
4. **Build links to the page**. Links are one of the most important ranking factors.
5. **Optimize for AI search visibility.** The same fundamentals plus a few moves that get you cited in ChatGPT, Perplexity, Gemini, and AI Overviews. When this guide first went live, AI search wasn’t a thing; that’s why I’m updating it.

In this article, I’ll explain and demonstrate how this process works using some of the SEO tactics Ahrefs used to grow into a 9-figure SaaS company.

## 1. Get your technicals right

Technical factors can impact your rankings or even prevent your site from appearing on Google’s search result pages.

To rank your content, Google needs to:

1. **Find and crawl your content**. You won’t rank if your content is inaccessible to Google (this may be because of a disallowed [Googlebot](https://ahrefs.com/blog/googlebot/)).
2. **Index your content**. We’re talking about the master list of all pages that Google keeps in order to display them for relevant search queries. Google may not want to show certain pages if it “thinks” those pages are not the main version of the content (see [canonicalization](https://ahrefs.com/blog/canonicalization/) for more info) or if the Googlebot is blocked.

![How Google builds its index](https://ahrefs.com/blog/wp-content/uploads/2022/09/how-google-builds-its-index.png)

In most cases, unless you’ve specifically instructed Googlebot not to crawl and/or index your site, your pages are ready to show up on the search engine results pages (SERPs). Keep in mind that it may take some time before Google indexes your content.

The easiest solution to technical SEO issues is to get SEO auditing tools and fix any problems they report back to you.

Two tools we recommend are [Google Search Console](https://ahrefs.com/blog/google-search-console/) and [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools) (they’re free). You can also set up [Bing Webmaster Tools](https://www.bing.com/webmasters/about) if you want to monitor your performance on Bing.

For example, to find sitemap issues in Ahrefs Webmaster Tools:

1. Open **Site Audit**
2. Go to the **All issues** report and scroll to the **Sitemap** category
3. Click on the found issues and see the affected pages. You can also see the recommended solution

While you’re at it, check your ‘robots.txt‘ for AI crawlers. GPTBot, PerplexityBot, ClaudeBot, and Google-Extended are the main ones. Block them only if you have a deliberate reason to. Most sites benefit from letting them in, since being part of an LLM’s training or retrieval set is how you show up in AI answers.

Start with ‘robots.txt‘. It lives at the root of your domain, so you can pull it up directly: ‘https://yourdomain.com/robots.txt‘. The file is plain text and groups rules by ‘User-agent‘. Look for any block that disallows the AI bots either explicitly or as part of a wildcard ‘User-agent: \*‘ rule. The bots worth checking by name are:

- **GPTBot**. OpenAI’s training crawler.
- **OAI-SearchBot**. powers ChatGPT search results.
- **ChatGPT-User**. Fires when a user clicks a link inside ChatGPT
- **PerplexityBot and Perplexity-User**. Training and on-demand retrieval
- **ClaudeBot**. Anthropic.
- **Google-Extended**. Controls whether Google can use your content for Gemini and AI Overviews. Note this is separate from Googlebot, so blocking it does not affect classic search rankings.
- **Bingbot** with the ‘nocache‘/‘noarchive‘ directives (relevant for Copilot).
- **Applebot-Extended.** Apple Intelligence.

A permissive setup for AI typically just lets these bots through with no explicit ‘Disallow‘ rules. If you want to restrict crawling on specific paths (admin sections, search result pages, faceted URLs), do it under each bot rather than a blanket disallow.

‘robots.txt‘ is the most common place this gets misconfigured, but it’s not the only one. A few other places blocks can hide:

- **Meta robots tags and ‘X-Robots-Tag‘ headers on individual pages or templates**. A stray ‘noindex‘ or ‘noai‘ directive in your CMS template, theme, or framework config can keep AI bots from using a page even when ‘robots.txt‘ looks fine.
- **CDN bot management rules**. Cloudflare, Fastly, AWS WAF, and similar services often have a one-click “Block AI Bots” toggle, plus rule sets that match known AI user agents and challenge or 403 them. Check your firewall rules and bot management dashboard.
- **Server-level rate limits and IP blocks**.  Aggressive throttling that returns 429 or 403 to the AI bots’ IP ranges effectively blocks them. Review your access logs filtered by the user agents above.
- **Cloudflare’s AI crawl controls**. If you’re on Cloudflare, the dashboard has a dedicated AI Crawlers section that overrides whatever your ‘robots.txt‘ says. Don’t trust the file alone.

Further reading

- [How Do Search Engines Work? Beginner’s Guide](https://ahrefs.com/seo/how-do-search-engines-work)
- [The Beginner’s Guide to Technical SEO](https://ahrefs.com/seo/technical-seo)
- [9 Common Technical SEO Issues That Actually Matter](https://ahrefs.com/blog/seo-issues/)

## 2. Find a keyword to target

To get traffic from search engines, you need to create content about something people search for.

To illustrate, the content on our blog alone brings us an estimated 256.9K organic visits every month. That’s because we create content designed to rank for keywords with search demand.

This is where keyword research tools, such as Ahrefs’ [Keywords Explorer](https://ahrefs.com/keywords-explorer), come in. With the help of such tools, you’ll easily find hundreds or even thousands of keyword ideas.

For example, entering the main focus of our blog, SEO, in [Keywords Explorer](https://ahrefs.com/keywords-explorer) reveals over 395K keyword ideas.

395K keywords are probably a bit too many to manage, and probably not all of them would be a good fit. So here’s what to consider when prioritizing keywords:

- **Search traffic potential**. Search traffic potential (not to be confused with search volume) tells you how much traffic you can potentially get from a keyword.
- **Business potential**. Topics with high business potential can convert a good portion of your visitors to customers. Topics with low business potential will make it tough for you to feature your product/service.
- **Ranking difficulty**. The more backlinks the top-ranking pages have and the more renowned the competing brands are, the harder it will be for you to rank.
- **Search intent**. The reason behind the search. Usually, it’s one of three things: finding a specific website, learning something, or buying something.

Here’s an example. One of the keyword research methods we use is to look for search demand for specific niches or industries in our area of business. For this, we filter for keywords that include the word “for.”

For instance, the ones highlighted display considerable Traffic Potential (TP), have no extreme ranking difficulty (KD), and have high business potential for us.

Keywords that tick all of the four things above are an ideal situation, but that doesn’t happen all of the time. Mostly, SEOs and content marketers need to go for compromises, e.g., targeting a keyword with high business potential but lower traffic potential.

Further reading

- [Keyword Research: The Beginner’s Guide by Ahrefs](https://ahrefs.com/seo/keyword-research)
- [How to Do Local Keyword Research](https://ahrefs.com/blog/local-keyword-research/)
- [Keyword Competitive Analysis: How to Find Your Competitors’ Keywords](https://ahrefs.com/blog/keyword-competitive-analysis/)

## 3. Create an optimized page

The content of a page is something that allows Google to “connect you” with the searchers.

The more interesting and useful your content is, the better. And that’s because quality content is something users expect and search engines need to provide. In fact,

[Google admits](https://developers.google.com/search/docs/beginner/seo-starter-guide#makesiteinteresting) that content is the most important ranking signal.

How Google exactly ranks content is kept a secret. But they actually [provide a hint](https://www.google.com/search/howsearchworks/how-search-works/ranking-results/#relevance) on the five things that determine which results will be shown for a given search query:

- **Meaning** – How well a page matches searchers’ expectations.
- **Relevance** – Does a page contain relevant information, e.g., words, phrases, and even pictures and videos relevant to what the searchers are looking for.
- **Quality** – Content also needs to be helpful. To determine content quality, Google will take into account both factors occurring [on the page](https://ahrefs.com/seo/on-page-seo) (e.g., [E-E-A-T,](https://ahrefs.com/blog/eeat-seo/) clear and organized form, freshness) and those occurring [outside the page](https://ahrefs.com/seo/glossary/off-page-seo) (backlinks, which we’ll talk more about later).
- **Usability** – If your pages and your competitors’ are equal in every other way, Google may allocate a higher ranking to pages that it finds more accessible (e.g., mobile-friendly, secured with an SSL, fast loading).
- **Context and settings** – Google may customize search results based on users’ search history and their current whereabouts.

Let’s take a look at an example of optimizing a page for search.

In the case illustrated below, the search intent seems to favor listicles for the keyword “free seo tools”. Because of that, we had little chance of ranking with a product landing page, even though we offer free SEO tools. So we decided to target the keyword with a content type more aligned with search intent. It now ranks #1 and brings about 1.3K organic visits each month.

There are many techniques SEOs and content marketers use to adhere to Google’s guidelines - too many to explain in this short article. If you want to take a moment to learn about them, see the video below. Otherwise, let’s move on to the next point: building links.

https://www.youtube.com/watch?v=ZWiNz-7gZ24

Further reading

- [What Is SEO](https://ahrefs.com/seo/seo-content) [Cont](https://ahrefs.com/seo/seo-content)[ent?](https://ahrefs.com/seo/seo-content) [How to Write Content That Ranks](https://ahrefs.com/seo/seo-content)

## 4. Build links to it

You’ll need two types of links: internal links and backlinks. Both are ranking signals, with backlinks being one of the major signals in SEO.

### Internal links

Internal links are links from other pages on the same website, e.g., a link from one article to another on our blog.

Their main roles in SEO are to help search bots crawl pages more efficiently and pass link equity from linking pages.

Because of the above reasons, you probably won’t find an article on our blog without at least one internal link pointing to another article or a product landing page.

By having internal links, we can create a situation where a page with a lot of backlinks can give a much-needed boost to newer pages (see the [middleman method](https://ahrefs.com/blog/orchard-seo-strategy/) for more details).

Here’s an example interlinking tactic. Including a link to our guide on SEO in the blog’s navigation automatically creates an internal link from every blog post to that guide, helping it to rank higher.

The Internal Backlinks report in Site Explorer shows different articles linking to the SEO guide, and some of them come from navigation of the site.

Further reading

- [Internal Links for SEO: An Actionable Guide](https://ahrefs.com/blog/internal-links-for-seo/)

### Backlinks

Backlinks are links from external websites. They act as votes. The more “votes” you get, the higher your chance of outranking the competition.

Backlinks impact rankings, and rankings impact traffic. So, generally speaking, the more backlinks you get, the more organic traffic you can generate.

The difficulty here is that you can’t fully control backlinks. You can either earn them organically (wait for people to discover you and link to you) or build them (ask people to link to you). Let’s look at that in more detail.

In the picture below, you can see examples of our case studies that continue to earn backlinks organically. Publishing original, unique data is one of the best ways to attract backlinks.

The Best by links growth report in Site Explorer allows you to see content that people like to link to and/or is a current target of a link building campaign (useful for competitive research).

And here’s an example of a content piece created specifically for an outreach campaign. Unlike the previous examples, it didn’t need any original studies: [63 SEO Statistics](https://ahrefs.com/blog/seo-statistics/). Our [process](https://www.youtube.com/watch?v=eTF6OBwidhc) was:

1. Researching most cited SEO statistics among the top-ranking articles.
2. Finding and including their more up-to-date versions in our article.
3. Asking people who linked to websites with outdated statistics to link to our article instead (that’s the outreach part).

This article got so many backlinks mainly due to an outreach campaign.

Regarding backlinks, it’s important to know that not all links will carry the same weight.

Generally speaking, the best links you can get are [“followed” links](https://ahrefs.com/blog/nofollow-links/) placed within the main content and those that come from relevant, authoritative websites.

Head on to the guides listed below if you want to learn more about backlinks and link building.

Further reading

- [Link Building for SEO: The Beginner’s Guide](https://ahrefs.com/seo/link-building)
- [How to Get Backlinks: 15 Proven Tactics](https://ahrefs.com/blog/how-to-get-backlinks/)

Recommendation

In the AI era, unlinked brand mentions matter too. After analyzing 75,000 brands, we found that branded [web mentions correlate strongly with how often ChatGPT brings your brand up](https://ahrefs.com/blog/ai-brand-visibility-correlations/). LLMs look for consensus. When many sources mention you in the right context, you start showing up in AI answers, with or without a backlink. So a podcast appearance, a Reddit thread, or a quote in a roundup post all count.

## Optimize for AI search visibility

The final step in modern SEO is making sure your brand shows up in AI assistants. A lot of the same signals still matter, but the way they’re used is different enough that it needs its own focus.

### 1. Build more online mentions of your brand

[Our correlation study of 75,000 brands](https://ahrefs.com/blog/ai-brand-visibility-correlations/) ranked search factors by how strongly each predicts AI visibility. The top of the list wasn’t backlinks or Domain Rating. It was YouTube mentions (~0.737), with general branded web mentions close behind (0.66–0.71). DR sat at 0.266. Backlink count was negligible.

AI assistants are scoring brand presence, the web’s consensus, not link authority. A brand discussed in many places (linked or not) is a brand the model trusts to recommend. YouTube carries extra weight because LLMs are partly trained on its transcripts, and in the case of Google’s AI Overviews, it seems to be a trusted layer of information, coming from their own product.

To turn this into action, do a quarterly \*mention gap analysis\*. Add your brand plus 3–5 competitors to [Ahrefs Brand Radar](https://ahrefs.com/brand-radar), then use the “Others only” filter on the AI charts to surface prompts where competitors get name-checked and you don’t.

The Cited Pages report shows the third-party URLs feeding those mentions, which doubles as your outreach pipeline.

### 2. Keep consistent brand information across sources

Because AI synthesizes responses from many sources at once, contradictions between those sources produce wrong or muddled output. The model may pick an arbitrary version, or stitch details from incompatible sources into a hybrid that doesn’t match reality.

Preventing this is mostly bookkeeping. Standardize one version of your brand name, tagline, founding year, headquarters, and one-line description, then push that version everywhere it appears: LinkedIn, Crunchbase, G2, Capterra, ProductHunt, AngelList, Wikipedia, industry directories.

Mark up your homepage with Organization [schema](https://ahrefs.com/blog/schema-markup/) and use the ‘sameAs‘ property to link your verified social profiles together. Don’t forget founder profiles, since prompts about company leadership pull from them disproportionately.

### 3. Fill information gaps

When there’s no authoritative information available, AI doesn’t typically say “I don’t know.” It grounds in whatever third-party content it can find, or it fabricates plausible-looking details. Both outcomes are bad for the brand at the center of the answer.

A [made-up brand experiment](https://ahrefs.com/blog/ai-vs-made-up-brand-experiment/) we ran shows the failure mode clearly. We built a fake company, seeded the web with three deliberately conflicting third-party sources, and posed 56 questions to 8 different models. Most models repeated the planted fictions as fact, even when the brand’s own FAQ contradicted them. When an AI must choose between an unspecific truth and a specific fabrication, the specific fabrication usually wins.

The practical implication is that being silent about yourself is a competitive risk. Publish an FAQ specific enough to leave nothing to interpretation, including direct denials of rumors that float around your category (“we have not been acquired,” “we don’t disclose unit counts”).

Keep pricing, plan limits, and policies in plain HTML rather than behind JavaScript widgets. Publish original numbers when you can. Maintain head-to-head comparison pages so the framing of “you vs competitor” comes from your side, not someone else’s.

### 4. Keep product documentation and help docs up to date

When people ask AI about your product specifically, the model can reach for  your documentation, help center articles, and changelog pages on your own domain. Those pages carry strong authority for branded queries because they’re explicitly about your brand and they’re well indexed.

That dependency is also a liability. Old docs hand AI an authoritative source for inaccurate answers: pricing tiers that no longer exist, features you’ve since removed, integrations that shipped without ever making it into the docs. Run a docs audit on a quarterly cadence. Publish changelogs and release notes openly so recency signals follow updates. Roughly once a month, run a short query set against ChatGPT, Perplexity, and Gemini, and verify what they say about your product.

When something is wrong, find the page feeding the error and update it. Brand Radar’s Cited Pages report shows you which of your own URLs AI is actually reading.

### 5. Write for AI humans, but help machines understand the content

If your content is easy to read, technically accessible, clear, and specific, it’s more likely to be picked up and used by AI systems.

#### Use clear formatting

AI tools prefer content that’s easy to scan and understand.

- Use **H1, H2, H3 headings** to show structure.
- Break information into **bullet points.**
- Keep sentences **short and direct.**
- Avoid long, dense paragraphs.

#### Add technical optimizations

Make your site easy for AI systems to access and interpret.

- Add **structured data (schema markup)**
  - Use FAQ schema for common questions.
  - Use product schema for product pages.
- Improve performance
  - Ensure **fast loading speeds.**
  - Optimize images and reduce unnecessary scripts.
- Design for all devices
  - Make your site **mobile-friendly.**
- Allow access to AI crawlers
  - Don’t block bots in `robots.txt`
- Limit heavy JavaScript
  - Many AI crawlers **don’t fully render JavaScript.**
  - Keep key content in **plain HTML.**

#### Write for clarity

Clear writing improves both human understanding and AI accuracy.

- Use **simple, direct language.**
- Break up long sections into smaller chunks.
- Include **specific facts, numbers, and details.**
- Answer **common questions clearly and directly.**

Further reading

- [How to Rank on ChatGPT: What Actually Works (Based on Data)](https://ahrefs.com/blog/how-to-rank-on-chatgpt/)
- [The Complete AI Visibility Guide for SEOs, Marketers, and Site Owners](https://ahrefs.com/blog/ai-visibility/)
- [How to Choose the Best Prompts to Monitor Your AI Search Visibility](https://ahrefs.com/blog/custom-prompt-tracking/)
- [AI Visibility Audit: How to Measure Your Brand’s Presence in AI Search](https://ahrefs.com/blog/ai-visibility-audit/)

## Good to know before you start

Before your jump into the process, it’s good to have realistic expectations in terms of the time and money needed to do SEO successfully.

When it comes to the results, SEO is usually a lengthy process. We [learned from over 4k respondents](https://ahrefs.com/blog/how-long-does-seo-take/) that it typically takes between 3 - 6 months.

Here are a couple of other things to know when it comes to the time involved in the process:

- Crawling a page can take Google anywhere from a few days to a few weeks ([source](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl)). So it seems that there’s a “natural delay” in SEO that comes from the technology itself.
- According to [our study](/blog/how-long-does-it-take-to-rank-in-google-and-how-old-are-top-ranking-pages/), only 5.7% of pages ranked in the top 10 (for at least one keyword) within no longer than one year.

As for the cost of SEO, the least costly option is doing SEO by yourself - all you need is time to learn and experiment and tools that fit your budget.

Alternatively, you can consider hiring an agency, a freelancer, or a consultant. Read our full [study on SEO pricing](https://ahrefs.com/blog/seo-pricing/) to know what costs to expect.

## Final thoughts

Monitor your results on a regular basis because search engine rankings tend to change. For this, it’s best to use a tool that tracks your ranking history and shows how you stack up against competitors—see our [Rank Tracker,](https://ahrefs.com/rank-tracker)) for example.

Track AI visibility on the same cadence using a tool like [Ahrefs Brand Radar](https://ahrefs.com/brand-radar)).

Thanks for reading! Feel free to reach out on [LinkedIn](https://www.linkedin.com/in/mateusz-makosiewicz/).
