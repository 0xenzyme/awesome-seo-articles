---
title: "What is agentic SEO? 8 workflows run on a live site"
source: "semrush-blog"
content_type: "blog_article"
freshness_risk: "low"
slug: "agentic-seo"
url: "https://www.semrush.com/blog/agentic-seo/"
canonical: "https://www.semrush.com/blog/agentic-seo/"
author: "Carlos Silva"
published: "2026-09-18T14:37:00+00:00"
updated: "2026-09-18T14:37:00+00:00"
categories:
  - "AI"
  - "Marketing"
freshness_reasons: []
fetched_at: "2026-10-12T10:03:54.963112+00:00"
status_code: 200
html_hash: "5b47b672ffe55f7143ffabd203858cb9519989474e0b11b5341f38e1649730e7"
clean_word_count: 5155
clean_char_count: 31965
---
# What is agentic SEO? 8 workflows run on a live site

Agentic SEO means handing a defined SEO workflow to an AI agent that executes it for you. Done well, it saves time and money.

The difference between the two is structure.

Rather than merely typing a prompt into an AI like “audit my site’s SEO and tell me what to do,” agentic SEO holds up when you split the work into four layers:

1. A project that carries your business context
2. Skills that carry the workflow for each step
3. Model Context Protocols (MCPs) that pull live data
4. A prompt that only carries the current task

I built all four and ran eight workflows against a live site. Below is a free agentic SEO setup along with the workflows and how to use them.

## What is agentic SEO?

Agentic SEO is the practice of handing a defined SEO workflow to an AI that pulls its own data, follows a documented method, and returns the same analysis every time it runs.

The keyword here is “same”. An AI SEO agent that produces a brilliant competitor analysis once and an unrecognizable one next month has not automated anything.

Two things separate agentic SEO from a well-written prompt:

1. The system retrieves its own data instead of waiting for you to paste an export, so it reads this week's numbers rather than the ones you happened to download
2. It follows a method that lives outside the conversation, so the checks that matter get applied whether or not you remembered to ask for them

### What makes an SEO workflow agentic?

An SEO workflow is agentic when four layers are used together: context, methodology, data, and prompting. Each layer has one job:

1. **Project**: A folder containing all of the context about your site, business, and constraints via documents such as your business plan, content guidelines, branding, and ideal client profile. Accessible across every run; it’s how the AI remembers who you are and your standards.
2. **Skills**: The method. Steps, checks, definitions, and the things that are never skipped. You write them once, and they get improved over time with use.
3. **Model Context Protocols (MCPs)**: Servers that pull live data from Semrush, Google Search Console, or Google Analytics instead of waiting on an export.
4. **Prompt**: This run's ask. It’s kept short, because the other three layers carry everything else.

[Faizan Ali](https://www.linkedin.com/in/faizanali1/), SEO & AI Search Strategist at Semrush, explains why it’s worth making your workflows agentic:

> *"With one long prompt I'd be re-explaining everything every time, and the longer it gets the more Claude drifts, loses context, and starts filling gaps with hallucinated stuff. Plus if something breaks, I know exactly which layer to fix instead of debugging a wall of text."*

### Agentic SEO vs. AI-assisted SEO vs. workflow automation

Agentic SEO differs from AI-assisted SEO and from workflow automation on one axis: who decides what happens next.

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Workflow automation** | **AI-assisted SEO** | **Agentic SEO** |
| **Who chooses the steps** | You, in advance | You, per conversation | You define the method once |
| **Where the data comes from** | Wired-in integrations | Whatever you paste in | The system retrieves it |
| **On an unexpected input** | Breaks, or produces nonsense | Depends on your phrasing | A documented rule, or it escalates |
| **Run-to-run consistency** | Perfect, and inflexible | Low | High, and adaptable |
| **Best for** | High-volume, unchanging tasks | Exploration and one-off questions | Recurring analysis that needs judgment |
| **Where it fails** | Anything the rules missed | Anything you need twice | Tasks with no repeatable method |

Each method has its place. If a task differs every time you do it, there is no method to write down, and an agentic workflow adds overhead with no benefit. To check 50,000 URLs for a status code, an automation script beats an agent.

But for recurring tasks that follow defined steps, agentic SEO can save you hours of manual work and even spot errors and patterns many human reviews would miss.

## What you need to run an agentic SEO workflow

To run an agentic SEO workflow you need four things:

1. An AI environment (we use Claude)
2. MCP connections to your data
3. A project carrying your business background, context, and instructions
4. A set of skills to execute the workflow

Any capable chatbot can do a version of this. We use Claude throughout because its projects and skills features map directly onto the four layers, and because the eight workflows below were built for it.

You’ll want to set up the following if you haven’t already:

Each of these is either free or has a free trial. SerpAPI gives you 250 credits per month for free and Firecrawl gives you 1,000. That’s totally fine for most smaller sites.

*As of September 2026, Claude's free plan is limited to one custom connector. You can connect Semrush for your one connection and run four of the eight workflows below: the technical triage, the competitor investigation, the search opportunity brief, and the AI citation mapping. The other workflows will require a paid Claude subscription.*

Let’s get into setting everything up.

### 1. A Claude environment

You have two options for your Claude environment: the [web app](https://claude.ai/) or the [desktop app](https://claude.com/download). We recommend the desktop app, as it gives you the most control over your agentic workflow, with more options for settings and scheduled runs. It also sits alongside Claude Code, the terminal version some of the workflows below run best in.

Either way, you get projects, which hold persistent context, and skills, which hold repeatable procedures. Both are available on every plan including the free one, though free accounts are capped at five projects and one custom connector.

*Claude Code is the terminal version. Use it when a workflow needs to read local crawl exports, run a bundled Python script, inspect a repository, or write a code specification. It’s only available on a paid Claude plan. Our guide to*[*using Claude Code for SEO*](https://www.semrush.com/blog/claude-code-seo/) *covers it in more depth.*

### 2. MCP connections to SEO data and tools

Model Context Protocol (MCP) is an open standard for connecting AI to external tools. MCP connections give workflow access to live data, which makes an output current and true rather than guessing. Our explainer on [what an MCP connector is](https://www.semrush.com/blog/what-is-mcp-connector/) covers the mechanics.

Connect the following MCPs:

- [Semrush MCP](https://www.semrush.com/kb/1618-mcp) for rankings, keywords, competitors, backlinks, and Site Audit
- [Google Search Console](https://github.com/saurabhsharma2u/search-console-mcp) (GSC) for clicks, impressions, and index status
- [Google Analytics](https://github.com/saurabhsharma2u/search-console-mcp) (through the same MCP server as GSC) for engagement and conversions
- [SerpAPI MCP](https://serpapi.com/integrations/mcp) for getting SERP AI overview data
- [Firecrawl MCP](https://www.firecrawl.dev/) for scraping web data
- Your content management system (CMS) such as WordPress
- GitHub, Slack, Google Drive, or a project management tool for delivery

Connect the Semrush MCP in Claude by navigating to Settings > “**Connectors.**” Search for “Semrush” and click “**Connect**,” then sign in to your account, approve the connection, and go back to Claude. Confirm the connection by asking if it’s connected.

The easiest way to connect the rest is to start a session in Claude, ask it to install the MCPs, and give it live links to MCP documentation for reference. It will tell you exactly what you need to do to install it.

Here’s a prompt you can use to have Claude assist you. Remember to replace the brackets with anything else you want to set up, such as Slack or WordPress:

*I want to connect MCP servers to Claude so I can run agentic SEO workflows. Walk me through it.*

*Before you start, confirm whether I am using Claude on web or desktop or in Claude Code, and what plan I am on. The free plan allows only one custom connector, so if I am on it, tell me before I begin.*

*Read these before giving me any instructions, and follow what they actually say rather than what you remember:*

*I also want to connect the following MCPs: [insert MCPs here, such as for WordPress, GitHub, Slack, etc.]*

*Then take me through one connector at a time. Give me the exact steps for my environment, wait for me to confirm, and do not move on until it works.*

*Verify each one before proceeding. Have me open a new chat and ask you to list your available tools, then confirm the expected tools appear by name. Do not tell me a connector is working because a settings screen says connected. Only your own tool list counts.*

*If a connector does not appear, work through this with me in order: is the config file valid JSON, did I fully quit and reopen the app rather than closing the window, does the command resolve on my PATH, and does the server run on its own from my terminal?*

*Finish with a summary: which connectors are live, what tools each exposes, and which of the eight workflows I can now run.*

Once you’ve set them all up, you can ask Claude to test the connections and verify that they are all working. It will tell you if anything isn’t working, and also instruct you on how to fix it.

### 3. A Claude project with persistent context

A [Claude project](https://support.claude.com/en/articles/9517075-what-are-projects) holds everything about your business that does not change between runs, so the AI remembers without you needing to add the info into each individual prompt.

In the Claude app, click “**Projects**” in the sidebar menu, then click the “**New project**” button.

![Claude project creation window with “SEO Agent” entered as the project name and the Create project button highlighted](https://static.semrush.com/blog/uploads/media/b1/f1/b1f11f1666cda35b046a810dbc1824cb/0ef539765b75c7929ef512703c7a302b/image.png)

Name your project something like “SEO Agent” and describe your project (this won’t affect how the AI works, it’s just for you and your team to understand what the project is for).

Create context documents to put inside the project folder that include:

- The website and primary market
- Target audience(s)
- Products and conversion goals
- Main competitors
- Priority topic areas
- Brand and editorial guidelines
- Definitions of high-, medium-, and low-priority issues
- Reporting requirements
- Actions that always require human approval

If you don’t yet have context documents, use the following prompt to get Claude to interview you and create the documents for you:

*I'm setting up a Claude Project to run agentic SEO workflows and I need the context files first. Help me build them.*

*Interview me before you write anything. Ask in batches of no more than five questions and wait for my answers before the next batch. If an answer is vague, ask a follow-up rather than filling the gap yourself.*

*Cover:*

- *The site, the primary market, and the languages it serves*
- *Who buys, in their words rather than marketing language, and what triggers the search*
- *Products or services, what counts as a conversion, and roughly what one is worth*
- *Who I think my competitors are, and who actually appears when my buyers search*
- *The topics I want to own, and the topics I have decided not to chase*
- *Brand and editorial rules: voice, banned words, claims that need legal review, sources I will not cite*
- *What makes an SEO issue high, medium, or low priority for this business specifically, not in general*
- *Who reads the output, in what format, and how often*
- *Actions that always need my approval before they happen*

*Push back on my competitor list. Ask how I know, and whether those companies actually appear when a buyer searches, or whether they are simply companies I think about.*

*Then produce these as separate files I can upload to the Project knowledge:*

1. *business-context.md — site, market, audiences, products, conversions*
2. *competitors.md — the set, with one line each on why they qualify and how confident I am*
3. *content-priorities.md — topics to own, topics to skip, and why*
4. *editorial-rules.md — voice, banned terms, claim rules, linking rules*
5. *priority-definitions.md — what high, medium and low mean here, with an example of each*
6. *reporting-and-approvals.md — who gets what, how often, and every action requiring approval*

*Rules for every file:*

- *Use only what I told you. Do not fill gaps with plausible detail.*
- *Mark anything I did not answer as TO CONFIRM: rather than guessing.*
- *Separate what I stated as fact from what you inferred, and label the inferences.*
- *Keep each file under a page. These load on every run.*

Once you get the documents back, review them and make any adjustments. When you’re happy with them, put them all in the project folder you linked the project to. Now, every time you run a chat window within that project, Claude will have all of this context for every run.

And lastly, set the project instructions by clicking the “**+**” button in the Instructions box. This is separate from the description you set when you made the project; Claude will use these instructions for all the chats within the project.

![Claude SEO Agent project with the Edit instructions button highlighted for adding custom project instructions](https://static.semrush.com/blog/uploads/media/52/6a/526a5e4c346d407aee030eebd3c9083c/cbb69e179363c37a934148634d419583/image.png)

#### Guardrails and approval rules

First, set these 10 guardrails and approval rules for your Claude project:

1. Keep production tools read-only unless I approve a write action.
2. Show me your plan before beginning a multi-step workflow.
3. Use connected tools to retrieve evidence instead of relying on assumptions.
4. Follow the relevant Claude skill when one is available.
5. If a tool call fails, retry once and then surface the error.
6. For each finding, explain the supporting evidence in one sentence.
7. Separate confirmed findings from hypotheses.
8. Flag missing data and low-confidence conclusions.
9. Stop when the workflow exceeds the agreed URL, result, or API-unit limit.
10. Ask for approval before publishing, redirecting, deleting, editing code, merging changes, or sending external messages.

#### Copy these project instructions

Our agentic SEO project instructions are below, ready to paste. Replace the bracketed parts with your own:

*I'm using this Claude project to run agentic SEO workflows.*

***Business context***

- *My site: [yoursite.com]*
- *My audience: [describe]*
- *My primary market: [country or region]*
- *Main competitors: [comp1.com, comp2.com]*
- *What I'm trying to grow: [qualified traffic, signups, revenue, brand searches, or AI visibility]*

***Available data and tools***

- *SEO data: [Semrush MCP]*
- *Search performance: [Google Search Console]*
- *Website analytics: [Google Analytics]*
- *Website content: [CMS, crawler, or Site Audit]*
- *Delivery tools: [Slack, Google Drive, Jira, GitHub, etc.]*

***Operating rules***

- *Keep production tools read-only unless I approve a write action.*
- *Show me your plan before beginning a multi-step workflow.*
- *Use connected tools to retrieve evidence instead of relying on assumptions.*
- *Follow the relevant Claude skill when one is available.*
- *If a tool call fails, retry once and then surface the error.*
- *For each finding, explain the supporting evidence in one sentence.*
- *Separate confirmed findings from hypotheses.*
- *Flag missing data and low-confidence conclusions.*
- *Stop when the workflow exceeds the agreed URL, result, or API-unit limit.*
- *Ask for approval before publishing, redirecting, deleting, editing code, merging changes, or sending external messages.*

***Before starting a workflow, confirm:***

1. *Which skill you will use*
2. *Which connected tools you need*
3. *What output you will produce*
4. *Which actions require human approval*

If you would rather have Claude tailor the rules to your business than start from the template above, use this prompt instead:

*Write the project instructions for a Claude Project that runs agentic SEO workflows. The output goes straight into the "Set project instructions" field, so give me one paste-ready block.*

*If I have already uploaded my context files, read them first and do not ask me anything they answer.*

*Then ask me only what is missing, in one batch:*

- *Which tools are connected right now, and which are read-only versus read-write*
- *What counts as high, medium and low priority for my business specifically*
- *Which actions must never happen without my explicit approval*
- *Who reads the output, in what format, and how often*
- *Any hard limit on URLs, rows, or API units per run*

*Then produce the block, structured as:*

1. *One line on what this project is for*
2. *The tools available, each labeled with what it is the source of truth for*
3. *Operating rules, written as imperatives*
4. *What to confirm before starting any workflow: which Skill, which tools, what output, what needs approval*
5. *What to do when data is missing or a tool call fails*

*Rules for the output:*

- *Keep it under 400 words. This loads into every conversation, so length costs me context.*
- *Every rule must be checkable. "Be accurate" is not a rule. "Report missing records rather than estimating them" is.*
- *Do not list a tool I have not told you is connected.*
- *Leave out my business context, audiences, competitors and topics. Those live in the knowledge files, not here.*
- *Mirror my phrasing where I gave you specifics. Do not smooth my priority definitions into generic ones.*

*Show me the block, then tell me in one line what you left out and why.*

Answer any questions Claude asks, tweak the output if necessary, and paste it into your instructions field.

### 4. Claude skills for repeatable SEO procedures

A Claude skill is a written procedure the model loads and follows, which is what turns a good prompt into a repeatable workflow.

A skill is a folder containing a “SKILL.md” file that describes when to use it, what data it needs, the ordered steps, the scoring rules, the output format, and the actions that require human approval. It can carry reference files and scripts. Claude loads it when the task matches its description, so you do not have to invoke it by name.

The project supplies business context. The skill supplies the method.

Without a skill, Claude may approach the same task differently each time. With one, the process is consistent, testable, and reusable, and an improvement made once applies to every run afterward.

The eight skills in this guide cover diagnosing content decline, prioritizing Site Audit issues, investigating competitor growth, building content briefs, finding internal linking opportunities, auditing a content portfolio, analyzing AI citation gaps, and checking a site after a migration.

Faizan has published all eight [on GitHub](https://github.com/crazylunatic007/agentic-seo-skills/tree/main/dist). To install them in Claude Code, copy the “skills/” folder into your “.claude/skills/” directory. To install them on the web or desktop, upload the pre-zipped skills from the “dist/” folder one at a time.

Then verify. Ask Claude to list its available skills; all eight should return. If one is missing, the frontmatter in that folder is the place to look.

## 8 agentic SEO workflows you can put into practice

Each workflow is one skill. Load the skills once, then invoke the one you need and answer its questions. The skill knows what data to pull, which checks to apply, and what to hand back, so it’s pretty plug-and-play. Invoke a skill with the slash command "/skill-name-here" or just ask: "Use the [skill name] to….”

All eight are [on GitHub](https://github.com/crazylunatic007/agentic-seo-skills).

### 1. Identify content decay

**Invoke:** /content-decline-diagnosis

This workflow helps you identify content with declining organic traffic, and potential reasons for the decline, plus a prioritized list based on your specific priorities. It asks for your domain or folder, your comparison windows, and a materiality floor (meaning the minimum drop worth investigating, by default a 30% decline and at least 100 clicks lost).

The skill works down a fixed order:

1. Pull period-over-period performance from Search Console
2. Drop everything under the floor
3. Check indexation before anything else
4. Look at rankings, demand, links and cannibalization

**Reading the output**: You get a ranked table of URLs with clicks lost, the likely cause, the evidence behind that call, and a primary and fallback action. A page that lost rankings needs a rewrite, a page that lost demand needs nothing, and a page that lost its canonical needs a five-minute fix.

![Content decline diagnosis ranking lost clicks and showing likely causes, supporting evidence, actions, and confidence](https://static.semrush.com/blog/uploads/media/fc/af/fcaf98bc2acfe4ab4b5fff9b4b83f254/fff2aff8c4e6c5f3b8bbded9ed4692e4/image.png)

**What happened when we ran it**: Three URLs dropped significantly across a 90-day year-over-year comparison. One page had a 230-click drop, but was a deliberate 301 from a planned consolidation, caught by the indexation check at step three. A second page turned out to be indexed but missing from the submitted sitemap, which is a five-minute fix.

### 2. Turn a Site Audit into a technical SEO sprint

**Invoke:** /technical-seo-sprint-triage

This workflow requires an existing [Site Audit](https://www.semrush.com/siteaudit/) project. The Semrush MCP cannot return full rendered page content, create a Site Audit project, trigger a crawl, or export the crawled URL set from a snapshot.

The skill will read the project and how much capacity you have. It then groups issues by root cause rather than by issue type, joins the affected URLs to traffic and rankings, scores impact against effort and confidence, and verifies its top items against live pages before producing a prioritized list of fixes.

**Reading the output**: You get a backlog of 10 to 15 items, each with a root cause, a fix type, and acceptance criteria written so a developer who is not an SEO can confirm the fix. Read the two lists underneath the table as well: what it excluded and why, and which fixes depend on other fixes shipping first.

![Technical SEO sprint triage prioritizing issues by impact and effort, with acceptance criteria for each fix](https://static.semrush.com/blog/uploads/media/03/e7/03e72e271fafccc99c1d76dcb3676443/265007462e1a8e05e602d61c6ef42a40/image.png)

**What happened when we ran it**: The workflow found 10 “temporary redirect” rows with a single root cause: internal CTA links without a trailing slash. And it found that two of the site’s five reported errors were the same javascript:void(0) link on a page with no traffic.

### 3. Investigate competitor traffic spikes

**Invoke:** /competitor-growth-investigation

This workflow pulls organic domain and URL reports, isolates the pages and keywords behind any movement, separates branded from non-branded, and tests each change against a driver: new content, improved rankings, seasonality, a migration, or a data artifact.

**Reading the output**: You get one row per competitor with the traffic change, the pages responsible, the likely driver, the relevance to you, and a confidence level. Treat the driver and confidence columns as the answer. A large number with a low confidence score is a prompt to investigate, not a reason to react.

![Competitor growth investigation comparing traffic changes, likely drivers, responses, relevance, and confidence](https://static.semrush.com/blog/uploads/media/16/f1/16f1703970b70c7e5f7e9c022e922d2f/daef1ae7d931fe3bdfe53f3e702f9952/image.png)

**What happened when we ran it**: It found a competitor getting most of their high-intent traffic from just two pages, even with a similar backlink profile. That told us where to build comparable pages on our client's site. This told me it would be smart to re-create similar pages on my client’s site.

### 4. Turn a search opportunity into a complete content brief

**Invoke:** /search-opportunity-to-brief

This workflow asks for a seed topic, your audience and your business objective. Before writing anything it checks your existing coverage and decides between create, update, consolidate, and no action. If a brief is warranted, it expands the keyword space, groups queries by audience problem rather than by string similarity, and reads what currently ranks.

**Reading the output**: You get a full brief with a working title, reader problem, intent, recommended headings, questions to answer, evidence required, internal links, cannibalization risks, and claims needing verification. It ends on a single decision with a confidence level, and that decision is the part to read first.

![Search opportunity analysis recommends creating a new page and lists findings missed by the human brief](https://static.semrush.com/blog/uploads/media/f2/d4/f2d4d0f669848a893666f47e5f177e4c/1a55d9b85fec5df71753a50573aaf3e8/image.png)

**What happened when we ran it**: We aimed it at the brief a human wrote for this article. It agreed the piece was worth writing, then found four things the brief had missed. One was a keyword we meant to target that brings up a completely different kind of search result, so it did not belong on this page. Another was three questions people have only recently started searching for. What it could not do was decide how to structure the article. A human still made that call.

### 5. Find internal linking opportunities and orphaned pages

**Invoke:** /internal-linking-rescue

This workflow builds a candidate pool from pages that already rank or earn links, reads them, finds passages directly related to each destination, and applies a reader-value test: would someone partway through this sentence actually want to go there next? Give it the priority pages you want strengthened.

**Reading the output**: You get two deliverables. First, [internal link](https://www.semrush.com/blog/internal-links/) recommendations with source, destination, anchor and the exact sentence to attach them to. Second, a structural report on [internal link mistakes](https://www.semrush.com/blog/internal-linking-mistakes/) like orphaned pages, broken internal links, and important pages linked only from low-value sections.

![Internal linking recommendations showing source and target URLs, anchor text, exact placement, and reader benefit](https://static.semrush.com/blog/uploads/media/25/e8/25e8a37733bd9a6bbd4c99031f3ea4ae/bf699461a6ef302dcb6f10f2b436dd03/image.png)

**What happened when we ran it**: It looked at the four pages bringing in 96% of the site's traffic and told us not just which pages to link from, but the exact sentence to put each link in. It also found that the site's second-biggest page, worth 27% of all traffic, had no internal links pointing to it at all. It sat in the sitemap and nowhere else.

### 6. Build a content portfolio decision engine

**Invoke:** /content-portfolio-decisions

**Runs best in:** Claude Code

This workflow helps you [audit your content](https://www.semrush.com/blog/content-audit/). It asks for your scope, your business rules, and how aggressive you want to be. It then builds one inventory keyed on URL from performance, ranking, link, freshness and conversion data, then applies ordered decision rules where the protective ones fire first. Above a few hundred URLs it runs a bundled script so the rules apply identically to every row.

**Reading the output**: You get every URL classified as keep, update, consolidate, redirect, remove, or investigate, with supporting and conflicting signals shown separately. Investigate is a real answer, not a failure. It means the evidence does not support a decision yet, and flags it for a manual review.

![Content portfolio decisions compare supporting and conflicting signals to determine which URLs need human review](https://static.semrush.com/blog/uploads/media/22/b5/22b59c408c02d488f81096d03f328f50/0f8985ec7772ec875833b277416a1a0d/image.png)

**What happened when we ran it**: This particular site did not have conversion data properly set up, so it came back with a lot of “0” conversion data. In order for this report to be useful, we would need to [set up conversion tracking in GA4](https://www.semrush.com/blog/ga4-conversions/) and re-run the report after a few weeks of data have come in.

### 7. Turn AI citation gaps into a digital PR queue

**Invoke:** /ai-citation-influence-mapping

This workflow groups prompts by topic and buying stage, finds the domains and pages cited most, separates source types to help you choose the angle, then reads the cited pages to work out what would earn you a mention.

**Reading the output**: You get a prioritized queue with the recommended asset and outreach angle per source, plus a separate list of sources where the right answer is no outreach at all (for example, forums and competitor-owned properties).

![AI citation analysis compares brand visibility across models and identifies sources where outreach is not appropriate](https://static.semrush.com/blog/uploads/media/8d/be/8dbeeceb62d6153923f09b01d978ac93/23302dddc399a5652542cd2b36ed8886/image.png)

**What happened when we ran it**: We asked four AI tools 32 questions and collected the 693 sources they cited. Unless the brand was named in the prompt, it did not show up in the answers. The tool surfaced places we could pitch to [get included in the listicles AI cited](https://www.semrush.com/blog/ai-seo-tips/) and, hopefully, get into the answer.

For ongoing tracking, the Semrush [AI Visibility Toolkit](https://www.semrush.com/blog/how-agencies-use-semrush-for-ai-visibility/) handles prompt monitoring, share of voice and citations. For the discipline behind this workflow, see our guide to [answer engine optimization](https://www.semrush.com/blog/answer-engine-optimization/).

### 8. Monitor SEO regressions after a release or migration

**Invoke:** /seo-release-regression-guard

**Runs best in:** Claude Code

This workflow needs a pre-release crawl, a post-release crawl with matching settings, and your approved-change list. It confirms the two crawls are comparable before diffing anything, runs the diff across status codes, redirects, canonicals, robots directives, sitemap membership, internal links and rendered content, then classifies each difference as expected, expected but implemented wrong, or unplanned.

**Reading the output**: You get a list of regressions ranked P0 (high severity) to P2 (low) with before-and-after evidence, an owner, acceptance criteria, and a verification step. Save the report. When fixes ship, the same skill loads it back and re-checks each item against its recorded criteria rather than accepting "fixed" as an input.

![SEO release regression analysis separates unexpected issues from approved changes using acceptance criteria](https://static.semrush.com/blog/uploads/media/94/1d/941df5a3cadc8bb60ffb58914f494c65/f8da7af29a596f70af3d8d5f61786de2/image.png)

**What happened when we ran it**: The comparison found two serious issues: cross-domain and trailing-slash redirects issued as temporary, and an approved page removal that never got executed in the migration.

## Start with one workflow, not an autonomous SEO department

You do not need eight skills, seven connections and a scheduler to get started with agentic SEO.

Instead, sign up for the [Semrush free trial](https://www.semrush.com/lp/product-free-trial/en/), connect the Semrush MCP as your single connection, install one skill, and run it. The technical sprint triage is the fastest one to prove out, because you can point it at a Site Audit you already have and judge the result in minutes.
