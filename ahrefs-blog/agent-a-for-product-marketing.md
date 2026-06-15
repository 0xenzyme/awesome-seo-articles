---
title: "8 Ways to Automate Product Marketing with Agent A"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "agent-a-for-product-marketing"
url: "https://ahrefs.com/blog/agent-a-for-product-marketing/"
canonical: "https://ahrefs.com/blog/agent-a-for-product-marketing/"
author: "Ryan Law"
published: "2026-05-22T11:17:23+00:00"
updated: "2026-05-28T12:27:58+00:00"
categories:
  - "General Marketing"
freshness_reasons: []
fetched_at: "2026-06-12T11:10:45+00:00"
status_code: 200
html_hash: "4202c220567ccc0c8f421dc10983df262a38c346070b7a07b85718952102a507"
clean_word_count: 2415
clean_char_count: 15454
---
# 8 Ways to Automate Product Marketing with Agent A

Here’s how the small-but-mighty Ahrefs product marketing team uses AI to automate their work.

[Andrei](https://www.linkedin.com/in/andrei-tit/) leads product marketing at Ahrefs, with a small team covering copy, webinars, partnerships, and paid promotion for all of Ahrefs (including the dozens of updates we ship each month).

[Constance](https://www.linkedin.com/in/huai-en-constance-tan/) works on the product team, running all of our webinars, writing our help center documentation, and much more besides (check out Constance’s webinars on [YouTube](https://www.youtube.com/@AhrefsTutorials)).

Andrei and Constance built a product marketing workspace in [Agent A](https://ahrefs.com/agent-a) that automates their workflows and builds custom applications. Here are the eight tools they lean on the hardest as PMMs.

What is Agent A?

[Agent A](https://ahrefs.com/agent-a) is a marketing agent from Ahrefs—an AI assistant with direct access to the full Ahrefs dataset that can carry out marketing tasks autonomously, rather than just answer questions.

![](https://ahrefs.com/blog/wp-content/uploads/2026/05/word-image-197275-1.jpg)

Agent A includes:

- **Unrestricted access to Ahrefs endpoints.** Every endpoint we use to build Ahrefs is available, including many you cannot reach via API or MCP.
- **Serious tech stack underneath.** Postgres for state, Flask for UIs, an OpenRouter proxy with 300+ models, web fetch with full-page parsing, PDFs, OCR, scheduled jobs.
- **Native connectors to marketing tools.** Slack, HubSpot, GitHub, Notion, Linear, Mailchimp, Resend, SendGrid, Stripe, Gong, WordPress, Airtable, Apify, and even Semrush.
- **Expert skill library.** The Ahrefs team has contributed pre-built marketing skills and applications that encode how we actually work.

## 1. Create a full GTM package from one brief

Andrei’s main workflow lives in the **GTM Generator**, a tool that takes one product brief and produces an entire launch package in one sequence.

For every new product and feature launch, Andrei can automatically generate a standalone landing page draft, a 90-second video script, a promotional email, and an almost print-ready flyer.

There’s then a cross-asset consistency stage that reviews all of the outputs and flags any areas where the message drifts or the details become a little inconsistent. In practice, that means:

- The video script generator stays capped at 1:30.
- The email targets precisely the right ICP.
- The landing page covers all the key details (without hallucinating anything).

Consistency really matters in PM, so the final review stage also reads all five outputs side-by-side and writes a summary.md file listing every claim, headline phrase, and ICP framing that disagrees across assets (like a landing page claiming that a new update was “10x faster”…despite that claim being nowhere in the original brief).

Once Andrei has edited the assets, he can even upload the edited file back into the GTM Generator for it run a diff check between its output and the edited version, allowing it to learn from the changes he made.

Starter prompt

*Build me a GTM package orchestrator. Input is one freeform product brief. Cascade through six stages: (1) Brief: convert raw text into a structured contract brief.md with ICP tiers, positioning, proof points, KPIs; (2) Landing page: generate a standalone product landing page HTML, hard-rule that bans naming sibling products of the same company anywhere in body copy; (3) Video script: 90-second segment-structured script with VOICEOVER, SCREEN, ON-SCREEN-TEXT per beat, hard cap 1:50; (4) Email: single launch email plus 2 subject lines plus 2 preview texts, 120-180 words; (5) Flyer: 2-page A4 landscape HTML plus PDF; (6) Consistency check: LLM reads all five assets and writes summary.md listing every cross-asset contradiction. Each step writes to a runs table, per-step rerun supported, the brief is the upstream source of truth.*

## 2. Generate a standalone product landing page

The **Landing Page Generator** is part of the GTM workflow above, but Andrei runs it standalone all the time when he want to rewrite a product page or create a new use-case page.

After you paste a brief in to the tool, it pulls relevant keyword data using the **Keywords Explorer** endpoint, chooses a relevant template, drafts an outline Andrei can edit, before generating the page, ready for hand-off to the web team to build.

Andrei creates lots of landing pages catered to different persona types (agencies, marketers, ecommerce, SaaS, entrepreneurs, freelancers, enterprises). The landing page generator has pre-made “seed” templates for each persona, making it easy to generate multiple landing variations for each new feature or release.

Starter prompt

*Build me a product landing page generator. Hybrid brief input: freeform textarea plus editable structured form (product name, archetype, ICP tiers, proof points). Pipeline: (1) competitor scan, read canonical competitor list from a skill file; (2) Keywords Explorer matching\_terms, archetype seeds, top 50 by volume; (3) outline stage with editable section list; (4) page generation with a hard STANDALONE\_RULE prompt clause listing every sibling product of mine, plus a post-generation regex scan that flags any sibling-product name in body copy; (5) SEO metadata (slug, meta title, meta description). Output: standalone HTML plus spec markdown plus inline preview.*

## 3. Generate a paid ads campaign off a competitor’s spend

The **Paid Ads Campaign Builder** is what Andrei runs when he want to see how a competitor is messaging in their paid campaigns. The tool uses the **Site Explorer** `paid_keywords` and `paid_pages` endpoints to find any domain’s paid campaigns:

It then fetches every paid landing page to find and analyze the ad copy, clusters paid keywords into ad-group themes, and provides a strategic overview of the company’s paid strategy:

Then the generator outputs Google Search creatives for Andrei to review, with three headlines and two descriptions per variant, and three variants per ad group—complete with headline, CTA, and full copy:

Starter prompt

*Build me a paid ads campaign builder off a competitor’s spend. Input: competitor domain. Pipeline: (1) Ahrefs paid\_keywords plus paid\_pages on their domain; (2) web-fetch top paid landing pages so the LLM reads their ad copy; (3) cluster keywords into ad groups, flag non-branded, score gap vs my domain (where I do not currently bid); (4) generate Google Search creatives, 3 headlines plus 2 descriptions per variant, 3 variants per ad group, hard char caps (headline 30, description 90); (5) generate 1080x1080 social PNGs in 4 background styles via Pillow with my brand font, orange accent word. Describe reference ad visuals verbally in the system prompt instead of passing binaries. Persist runs in Postgres, ZIP download of all PNGs.*

## 4. Build a sales battlecard off a competitor URL

The **Battlecard Generator** takes a competitor URL and produces a 6-box sales battlecard (with sections for *Overview, Product, Pricing, Strengths, Weaknesses, How to position Ahrefs,* and *Where we might lose*).

The tool generates both an HTML preview and a real .pptx export that mirrors Andrei’s existing template:

Sidenote.

This is just an illustrative example, and not something we actually use.

The battlecard is generated based on tons of research:

- **Analysis of core website pages:** homepage, pricing pages, features and solutions pages, plus to 15 nav links discovered on the homepage.
- **Publicly available review sites:** like G2, TrustRadius, and Capterra.
- **Ahrefs data:** like DR, organic traffic, ref-domains DR distribution, top paid keywords, branded traffic split.
- **LLM analysis:** data synthesis to answer two crucial questions: “How to position Ahrefs”, and “Where we might lose”.

Starter prompt

*Build me a sales battlecard generator. Input: competitor URL. Output: a 6-box battlecard (Overview, Product, Pricing, Strengths, Weaknesses, How-to-position-us, Where-we-might-lose) as HTML plus a real .pptx that mirrors my team’s existing battlecard template. Pipeline: (1) deep scrape competitor (homepage plus /pricing, /features, /solutions plus up to 15 internal nav links, cap 18 URLs); (2) review fetch directly from G2 detractor URL (filters[nps\_score][]=1), TrustRadius, Capterra by slug, in parallel; (3) SEO signals on their domain (DR, organic traffic, ref-domains DR distribution, paid keywords, branded traffic split); (4) LLM synthesises Strengths, Weaknesses, How-to-position-us, Where-we-might-lose using my strategy skill as ground truth for our advantages and ICP framing; (5) HTML render to my team’s color palette plus a python-pptx export that mirrors the existing battlecard layout.*

## 5. Polish a LinkedIn draft into two voiced versions

The **LinkedIn Post Generator** is the smallest tool on this list but it’s one Andrei and Constance use most days. Paste a rough LinkedIn post idea, and the application returns two polished versions back with two different angles to choose from:

The generator uses a set of predefined “angles” to generate posts: narrative, hook-led, teardown, project reveal. The PM team picks two, or the app picks for them.

The tool refers to Andrei’s and Constance’s personal `linkedin-post-bank` (a curated selection of their best-performing posts), and uses a brand-voice skill to keep every product mention accurate.

Sidenote.

Contrary to the screenshot, I am not Ahrefs’ Product Marketing lead… but I will take a second paycheck if one is going.

Starter prompt

*Build me a LinkedIn post generator. Input: a rough draft and two angle picks from {narrative, hook-led, teardown, project reveal}. Read a personal “post bank” skill file as voice ground truth on every generation (it carries 15-30 reference posts in my voice). Detect the pattern of the draft, then rewrite into two versions, both fold-safe under 1300 chars. Add an “Add to bank” button that appends approved outputs back to the skill file. Persist runs in Postgres for history. Reuse the same bank skill file from any other agent session that drafts LinkedIn content, the file is the corpus.*

## 6. Plan a webinar in 5 phases, end-to-end in Linear

Constance runs a lot of webinars for Ahrefs, so she asked Agent A to build the **Webinar Automation** app: she enters a webinar title, date, and roster once, and it creates a full Linear project from scratch:

The tool runs through five distinct phases:

- **Phase 1 (Concept)** spins up the Linear project in the Product Marketing team with milestones back-calculated from the webinar date—Promo Start, Live, Recording Ready, Report.
- **Phase 2 (Landing)** creates a Zoom event, Admin landing page, updates the /webinars/ page, and creates a ticket for the design team.
- **Phase 3 (Promotions)** generates promotional copy, an Intercom workflow, and creates a ticket for our paid manager to start promotion.
- **Phase 4 (Content)** generates drafts of Agent A demos, webinar slides, and a script.
- **Phase 5 (Reporting)** creates a performance report to share with the team.

Starter prompt

*Build me a webinar automation Console app backed by Linear. Atomic input: a webinar title, date, and roster of teammates with their Linear user IDs. UI walks 5 sequential phases — Concept, Landing pages, Promotions, Content, Reporting — each with its own settings panel and a Launch button; phase N+1 is locked until phase N is launched. Phase 1 creates a Linear project in my Product Marketing team with 4 milestones back-calculated from the webinar date. Phases 2-5 create 14 issues + 6 sub-issues from Jinja-templated descriptions with {webinar.title} interpolation; I can override any title or assignee per-webinar before launch. Templates live in code so they version with the app. Use the linear connector for projects/issues and direct GraphQL for milestones.*

## 7. Turn sales calls into positioning shifts

The **Calls to Positioning** tool is for research, not deliverable generation, but it’s incredibly useful. It takes sales call snippets, analyses their content, and creates suggestions for how the PM team can update our product positioning to win more deals—all grounded in real customer quotes.

Sidenote.

This is a fabricated screenshot similar to Andrei’s tool, so there’s no PII here 😉

The analysis is broken into four categories:

- **Why we win:** winning patterns and selling points worth incorporating into website copy.
- **Why we lose or stall**: a list of objections, blockers, churn signals.
- **Verbatim language:** phrases customers actually use, ordered by recurrence.
- **Proposed positioning shifts**: before/after examples with the supporting quotes attached.

Starter prompt

*Build me a sales-calls-to-positioning tool. Input: paste call snippets one per blank-line block, optional speaker labels. Optionally ship a built-in 15-20 snippet sample corpus that covers wins, losses, churn, and competitor mentions, so the tool is usable on first run. Strip any source metadata (speaker, stage, deal outcome) from the prompt: clustering must come from the language itself, not the tag groups. Output four buckets: (1) Why we win, winning patterns with verbatim phrases worth lifting into copy; (2) Why we lose or stall, objections, blockers, churn signals; (3) Verbatim language, phrases customers actually use, ordered by recurrence count; (4) Proposed positioning shifts, before/after with the supporting verbatim quotes attached. Persist runs in Postgres for history.*

## 8. Turn a messy markdown brief into a branded PowerPoint

For Constance, slide decks are the worst part of every product launch. She used Agent A to build a **Text to PowerPoint** so she never needs to start from a blank slide again.

Constance writes her notes and ideas in Markdown and pastes into the tool. The tool splits the content into sections and slides, while a regex rule catches image-cue patterns (“show screenshot”, “insert diagram”, “[image]”, <screenshot>, “add a chart”…) and reserves a labeled dashed-orange placeholder box on the right of the slide.

The PowerPoint builder has the Ahrefs palette, and Constance can preview slide-by-slide in the browser, edit any slide inline, and export when she’s finished.

Starter prompt

*Build me a markdown-to-pptx generator. Input: pasted markdown or .md upload. Parser splits on #/##/### into title/section/content slides. Regex catches 8 image-cue patterns (“show screenshot”, “insert diagram”, “[image]”, <screenshot>, “add a chart”…) and reserves a labeled dashed-border placeholder box on the right of each affected slide. Claude Sonnet 4.6 rewrites each chunk into 3-5 concise bullets; original prose is preserved verbatim in the speaker notes (not the slide body). Use python-pptx with my brand palette baked in: navy header bar, orange accent stripe, 16:9, 26pt headings, 20pt bullets. Title and section slides are full-navy with a centered orange accent line. UI shows a slide-by-slide preview with inline edit + delete per slide. Export as .pptx.*

## **Final thoughts**

If you’re an Ahrefs customer, you can try [Agent A](https://ahrefs.com/agent-a) for free for one month. Copy any of these prompts into a fresh workspace and your own Agent A will start building the tool—or check out the application library to add some of these tools directly to your own workspace.
