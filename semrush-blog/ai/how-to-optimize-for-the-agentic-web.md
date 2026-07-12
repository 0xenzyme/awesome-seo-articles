---
title: "How to optimize for the agentic web: a guide for marketers"
source: "semrush-blog"
content_type: "blog_article"
freshness_risk: "low"
slug: "how-to-optimize-for-the-agentic-web"
url: "https://www.semrush.com/blog/how-to-optimize-for-the-agentic-web/"
canonical: "https://www.semrush.com/blog/how-to-optimize-for-the-agentic-web/"
author: "Tushar Pol"
published: "2026-06-16T15:04:00+00:00"
updated: "2026-06-16T15:04:00+00:00"
categories:
  - "AI"
  - "Marketing"
freshness_reasons: []
fetched_at: "2026-07-12T19:58:27.074762+00:00"
status_code: 200
html_hash: "00a5d1a5cef9f9bc7be1b513f964ae0291b307329fe92f8ac5637d86569f3a60"
clean_word_count: 4442
clean_char_count: 28104
---
# How to optimize for the agentic web: a guide for marketers

For decades, websites had one audience: people. Now they have another.

AI agents inside tools like ChatGPT, Gemini, and Perplexity can browse the web, compare options, and complete tasks on a person's behalf, from looking up a fact to booking a trip or placing an order.

Since launch, these tools have gotten so much better. Now, they can even browse websites to perform tasks for you. For example, here’s ChatGPT making purchases on a user’s behalf:

![Using a ChatGPT prompt to make a purchase on Instacart.](https://static.semrush.com/blog/uploads/media/2c/87/2c873fc9ce405975813328705b9a72e4/0cc5f71634f52f6d48556d6711fafd20/image.jpeg)

That changes how customers find and choose brands. When someone asks an agent to "find the best project management software for my team," the agent visits sites, weighs the options, and may recommend or even buy one, often without the person opening a single website. Whether your brand makes that shortlist depends on how well your site communicates with machines, not just people.

This guide breaks agentic web optimization into a five-layer stack, walks through the steps at each layer, and shows how to measure whether the work is paying off.

## What is the agentic web?

The agentic web is internet infrastructure that enables AI agents to browse, evaluate, and act on websites for users, handling tasks from simple lookups to full purchases and bookings.

It differs from the web most of us grew up with. The traditional web is built for people who click, scroll, read, and decide for themselves.

Say you wanted project management software: You would open a few tabs, compare features and pricing, read reviews, and pick one. The agentic web assumes the visitor might be a machine doing that work for you. You describe what you need, and the agent handles the research and the steps that follow.

A prompt to an agent might read: "Find a project management tool for a 10-person team under $15 per user, with time tracking and a free trial. Compare the top three and start a trial on the best-reviewed one."

To answer it, the agent has to reach your site, understand what you offer, trust what it finds, and act on it. The rest of this guide is about making each of those possible.

## Why your business needs to be agent-ready now

Over the past year, the biggest AI and commerce companies shipped the standards that let agents act on websites:

- [**WebMCP**](https://www.semrush.com/blog/webmcp/), a browser standard that lets sites expose actions directly to agents, was published as a W3C draft in February 2026 and is available as an early preview in Chrome Canary.
- Google announced the [**Universal Commerce Protocol**](https://www.semrush.com/blog/universal-commerce-protocol/) **(UCP)** at NRF in January 2026 with Shopify, Walmart, Target, and more than 20 partners.
- OpenAI and Stripe's **Agentic Commerce Protocol (ACP)** has powered checkout inside ChatGPT since September 2025, and ChatGPT's in-chat purchasing opened to U.S. users in February 2026.
- **ChatGPT** and [**Google's AI Mode**](https://www.semrush.com/blog/google-ai-mode/) already surface agent-assisted shopping.

Agents will keep acting for your customers either way. The open question is whether your site lets them finish tasks. When an agent hits a dead end, the sale goes to a competitor whose site got out of the way. That risk runs highest in ecommerce, SaaS, travel, and services, where a visit really only counts if it ends in a transaction.

## The agentic web optimization stack

Agentic web optimization works as a five-layer stack, and each layer depends on the one beneath it. Build from the foundation up, because a site that is agent-ready but not crawlable still fails:

- **SEO foundations**: Make sure your site is crawlable and free of technical issues. If agents can’t access your content, nothing else in this stack matters.
- **Agent readiness**: Write your content clearly and structure it well. This helps AI agents easily parse your information to form an accurate understanding of your brand.
- **Off-site presence:** Strengthen your brand presence across the web. Clear positioning ([entity optimization](https://www.semrush.com/blog/entity-based-seo-strategy/)), consistent information, and mentions on trusted sites give agents the confidence to surface your brand in their answers.
- **Action layer**: Make your site usable for AI agents. They need to be able to navigate your site and complete tasks, such as filling out a form.
- **Protocol layer:** Implement standards like MCP, WebMCP, ACP, and UCP. These let agents interact with your site reliably and at scale.

![Agentic web optimization stack: SEO foundations, agent readiness, off-site presence, action layer, protocol layer.](https://static.semrush.com/blog/uploads/media/be/b2/beb26d89ad38df612f8c7f6a1e89800a/e99eef38411566aef2e51b57d798e83e/image.png)

## 5 steps to optimize for the agentic web

Work through the stack one layer at a time, starting with the foundation:

### 1. Start with technical SEO

Everything else depends on whether agents can reach your site, so technical SEO comes first.

When someone asks an agent to find a project management tool for a small business, the agent visits sites in that category, checks which tools fit, reads reviews, and builds a shortlist.

If technical problems block that visit, you never make the shortlist, no matter how good your product is.

Common technical issues to look for on your site:

- A misconfigured [robots.txt file](https://www.semrush.com/blog/beginners-guide-robots-txt/) that accidentally blocks agents from crawling your most important pages
- Slow [page load times](https://www.semrush.com/blog/page-speed/) that cause agents to move on before your content even loads
- Content that's locked inside JavaScript and never renders for some AI agents
- [Broken internal links](https://www.semrush.com/blog/broken-link/) that send agents to dead pages
- Redirect loops that send agents in circles so they never land on the right page
- 5xx server-side errors that make your pages unreachable for agents

To find out if these issues exist on your site, use the [Site Intelligence](https://www.semrush.com/enterprise/product/si/) tool inside Semrush’s Enterprise SEO.

Once in the tool, click “**Issues**” > “**Issue Overview**” and scroll to the “Issue Overview” report. Each issue is ranked with an impact score and a priority so you know which issues are worth fixing first.

![The Issue Overview report with the "Impact Score" and "Priority" columns highlighted.](https://static.semrush.com/blog/uploads/media/82/f0/82f01ad99340ff59eac59122f5b4a529/2a7656d1abcbf220d250283e6ddeaf51/image.jpeg)

Click any issue to see the affected pages and step-by-step fixes. Resolve what you can in-house. Route the rest to your development team.

![Images missing ALT Tags showing issue history, unresolved issues, total impact, and new vs. resolves issues.](https://static.semrush.com/blog/uploads/media/47/ea/47eaa6219fb9830559e243bd08b3f443/dedfe3e2e0957127827085d951571a78/image.jpeg)

### 2. Make your content easy for agents to parse

Once agents can reach your site, your content has to be easy for them to read and understand.

This is where many brands stumble: Pages load fine, but key information is buried, the language is vague, and there’s no clear structure.

A lot of this overlaps with good generative engine optimization (GEO). The agent-specific part is that agents don’t just extract an answer — they compare facts across sites to make a decision. So explicit, comparable details matter more here than anywhere else.

To make your content parseable:

- **Write clearly**: Use plain sentences that state what your product does, who it’s for, and what problem it solves
- **Structure for scanning**: Use headings, short paragraphs, and bullets so each block stands on its own as a unit an agent can use
- **Lead with the point**: Open each section with the takeaway; then add detail so agents capture the main idea even without reading every line
- **Answer real questions**: Add an FAQ section that addresses the questions buyers actually ask, because FAQs are a major source of agent answers in this category and close wording matches how people phrase their queries

Let's quickly go over an example to see what an agent-friendly page actually looks like.

This page about [sales automation](https://www.make.com/en/solutions/automate-sales) opens with a clear headline and follows immediately with an explanation of what the product does.

![The hero section of an agent-friendly page using a clear headline and description.](https://static.semrush.com/blog/uploads/media/e4/8b/e48b2bfb6d776bb1311f5d173a641278/ac50ff1a3f3ae983dd1c159f97a1a1a0/image.jpeg)

The page is also broken into distinct sections to create an easy-to-follow structure. Each section has its own heading and a short, self-contained description.

![The "Use cases" section of an agent-friendly page using a clear structure with each section containing a heading and description.](https://static.semrush.com/blog/uploads/media/48/ed/48ede706e986a8a545e9af192a58c7a2/2bb3976c86991cc76e7ca22cede38efd/image.jpeg)

It closes with an FAQ that answers common questions, which agents can lift directly when users ask about sales automation.

![The FAQ section of an agent-friendly page addressing common user queries about sales automation.](https://static.semrush.com/blog/uploads/media/9b/26/9b26b3ffde4509423aed2ed0ac1522e2/238588e4dfbbee387910f00e1758f6a4/image.jpeg)

Schema markup can improve the machine-readability of your content in some cases. It’s structured code that tells bots exactly what a page contains. Three types cover most needs:

- **Product schema:** Gives agents clear price, availability, ratings, and specifications for ecommerce pages
- **FAQ schema:** Marks up your questions and answers so agents can match them to user queries on any content site
- **Organization schema:** Spells out who you are, including name, logo, contacts, and social profiles, to reinforce entity clarity

You can find the full list of types and properties at [schema.org](http://schema.org).

### 3. Build your off-site presence

Your own pages are only part of what an agent weighs. Off-site signals, meaning what other sites say about you and whether they say it consistently, may decide whether an agent recognizes you as a credible option and surfaces you at all.

Start by benchmarking where you stand: Semrush's [Enterprise AIO](https://enterprise.semrush.com/solutions/ai-optimization/) and [AI Visibility Toolkit](https://www.semrush.com/ai-seo/overview/) can show how often agents mention your brand for category prompts and where competitors appear instead.

When someone asks an agent about project management tools, the agent may look past your homepage to reviews, comparison articles, forum threads, and "best of" roundups. A strong, consistent off-site presence gives it the confidence to recommend you.

Start with consistency. Your brand name, product description, and core value proposition should match everywhere they appear. If your site says you serve small businesses and your G2 profile says enterprise teams, an agent has no way to tell which is right. So it favors a competitor with cleaner positioning.

Use Semrush's [Brand Monitoring](https://www.semrush.com/apps/brand-monitoring/) tool to see exactly where your brand is mentioned, in what context, and whether the information is accurate.

![Brand Monitoring tool showing a list of brand mentions for "semrush.com" across platforms.](https://static.semrush.com/blog/uploads/media/43/d6/43d69731f71831bce5fefa02fc537b91/032580c1371abe5ddeb505f61f8483d5/image.jpeg)

Reviewing those mentions is a manual step. When you spot outdated or inconsistent information, contact the site owner and request a correction.

Next, earn high-quality mentions. The more often your brand appears in credible places, the more confident agents are recommending you.

A few ways to earn them include:

- [**Digital PR**](https://www.semrush.com/blog/digital-pr/): Pitch data-driven stories or offer expert commentary to journalists covering topics relevant to the industry. If they decide to feature your insights or include your data in an article, they’ll likely mention your brand name.
- [**Guest posting**](https://www.semrush.com/blog/guest-posts/): Write for respected blogs in your category. Most blogs have an author bio where your brand name can seamlessly fit in.
- **Inclusion in “Best of” lists**: Reach out to websites that have published roundup posts like "best project management tools for small businesses." Send them a brief pitch suggesting they include your product with a short pitch and ready-to-use copy and screenshots

Reviews matter, too. Agents may weigh them when deciding whether your product fits.  
  
If people describe your product as “great for small teams,” “easy to set up,” or “affordable,” an agent researching tools for a small business is more likely to recommend you when those descriptors matter to the user.

Actively encourage satisfied customers to leave reviews on platforms like G2, Capterra, and Trustpilot. You can send them a link to your profile where they can leave feedback.

### 4. Prepare your site for agent interactions

Most sites are designed for people, and the same choices that work for human visitors create dead ends for agents.

For example:

- **Vague buttons:** Labels like "Learn more" or "Get started" don't tell an agent what the action leads to, so it can’t act confidently. Use specific labels instead: "Book a demo," "Start free trial," "Get a quote."
- **Pop-ups and modals:** These components can block the page for agents. They can't dismiss them easily to jump to the next steps in the workflow. Avoid using these components, especially on conversion-focused pages.
- **Information locked in images:** Agents may be unable to read text that's part of an image. Keep important information like product pricing, specs, and availability as text on the page.

The best way to understand the impact of these issues is to trace what happens when an agent actually tries to complete a task.

To see why this matters, trace what happens when an agent tries to act. Say it has shortlisted a few project management tools, and the user asks it to start a free trial on one. For the agent to finish, a few things have to be true:

- Pricing and plan details should be accessible so the agent can confirm the plan with the user before proceeding
- The signup flow needs to be simple, with clearly labeled fields and buttons
- No overlays or pop-ups should interrupt the process midway

In other words, if the signup flow is clean and unambiguous, the agent can complete the task.

When the flow is clean and unambiguous, the agent completes the task. This is the best case, though. Agents are probabilistic, not deterministic, so they can still miss steps or fail a flow. Protocols give them a more reliable way to act, which is the next layer.

### 5. Prepare for agentic protocols

Protocols are emerging standards that give agents a structured, reliable way to interact with your site instead of working through the human interface. They differ in function and maturity, so it helps to know what each one does before deciding which to prioritize:

- **Model Context Protocol (MCP):** Released by Anthropic in November 2024, MCP lets agents connect to SaaS products and act on a user's behalf, such as pulling a report from a CRM or running a query in an analytics tool. It’s the most mature and widely adopted of the four.
- [**WebMCP**](https://www.semrush.com/blog/webmcp/)**:** Published by Google and Microsoft as a W3C draft in February 2026 and available in Chrome Canary, WebMCP extends MCP to the browser so agents can complete on-page tasks like signing up or submitting a form. It’s an early preview, but not production-ready as of this article’s writing.
- **Agentic Commerce Protocol (ACP):** Launched by OpenAI and Stripe in September 2025, ACP was the first major standard for agent-led commerce, giving agents a structured way to access product data and complete purchases inside ChatGPT.
- [**Universal Commerce Protocol (UCP)**](https://www.semrush.com/blog/universal-commerce-protocol/)**:** Announced by Google at NRF in January 2026 with Shopify, Walmart, Target, and more than 20 partners, UCP standardizes how agents access product data, pricing, and availability — and how they complete purchases for users.

Adoption is still early. ACP and UCP are limited to select U.S. merchants, and WebMCP is not yet production-ready.

Read the documentation for each; then align your product and engineering teams on which fit your business and scope an integration plan. If you run B2B SaaS, start with MCP. If you sell in ecommerce, prioritize ACP and UCP. For a closer look at the commerce protocols, see our guide to [agentic commerce optimization](https://www.semrush.com/blog/agentic-commerce-optimization/).

## How to measure agentic web optimization performance

Agentic web optimization needs new metrics, because traditional SEO measures like rankings, CTR, and bounce rate do not capture whether agents can find or use your site. Track two tiers: visibility metrics, which tell you whether agents are finding and recommending you, and action metrics, which tell you whether agents are completing tasks on your site.

### Visibility metrics

These metrics are purely about your brand’s presence in AI platforms.

#### AI visibility score

The AI visibility score tells you how prominently your brand appears in AI platforms compared to competitors. The score is on a scale from 0 to 100, where a higher score means a more dominant presence in AI tools.

Check your score using [Semrush AIO](https://www.semrush.com/enterprise/product/ai/)’s AI Visibility tool. Head to “**AI Visibility**” > “**Visibility Overview**.” Enter your domain and click “**Check AI Visibility**.”

![The Visibility Overview report with the input box to enter a domain and the "Check AI Visibility" button highlighted.](https://static.semrush.com/blog/uploads/media/9c/61/9c61cd235ff988c11e8d943d05d12b7b/afd161bcfb270774a83681ac3339efd4/image.jpeg)

At the top you’ll see an aggregate visibility score. Click the “Visibility” tab to see your site’s visibility trends over time.

![The Visibility Overview report with the "AI Visibility" score and the visibility trend chart highlighted.](https://static.semrush.com/blog/uploads/media/5e/cc/5eccd2d82390e0a5a9a4bb46a31244b9/a416a37c4eecc1fb600155c9c20a1bc4/image.jpeg)

And see your performance on a specific platform, such as ChatGPT, Gemini, or Google AI Mode by changing the model in the dropdown.

![The Visibility Overview report with the "All Models" dropdown opened showing different platforms to choose from.](https://static.semrush.com/blog/uploads/media/56/e8/56e88fdaa625afc5a55b81493ca88f27/c97854a06bf90b9f91a3662aac71b61f/image.jpeg)

#### Mentions

Mentions is the number of times AI tools name your brand in their answers. Every time someone asks ChatGPT or Gemini a question about your category and your brand shows up in the answer, that counts as one mention.

You'll find this data in the AI Visibility tool. The AI Visibility report shows total mentions, mentions by model, plus how your mentions are trending month over month. Use this to see whether your mentions are growing or declining.

![AI Visibility report](https://static.semrush.com/blog/uploads/media/70/dc/70dc319eae1a54dc41b69bebf5dfc4e3/4d1bece93f15bcaae4d7a8770af017f7/image.jpeg)

A growing mentions count means AI tools are trusting your brand more often when people ask category-relevant questions.

#### Citations

A citation is when an AI tool quotes your specific content as a source for its answer. Mentions and citations sound similar, but they're different things. A mention is when AI names your brand. A citation is when AI uses your content and adds a link back to your domain to credit you as a source.

You can see how many citations you’ve got by going to “**Sources**” > “**Citations**” in Prompt Tracking.

![Citations report with total citations highlighted.](https://static.semrush.com/blog/uploads/media/42/32/42324085f9c969dc717f0d3326490203/a33f56b2ccfc257bda726579b3195d23/image.jpeg)

Citations can drive AI-referred traffic because they include a link back to your site. Mentions build visibility but don’t always send a visit. Growing citations mean AI tools treat your content as authoritative enough to use as a source.

If you want to know where you aren’t being cited, scroll to the “**Citation Gap**” report.

![Citation Gap report showing a list of prompts with all the cited domains for each prompt.](https://static.semrush.com/blog/uploads/media/32/4e/324e905a5cebc317559d9766b6455da8/9a2907d2331c484e7961c5ea483938a2/image.jpeg)

Look for relevant prompts that don’t cite your brand. Click into each prompt for more details like which brands have the highest position within that prompt.

![Prompt Response Details showing a prompt, response, and a list of brands mentioned along with position changes.](https://static.semrush.com/blog/uploads/media/86/b3/86b3de857a387df7de2fa728e0e6b1fc/d002acef8f573842327bd2e97266f825/image.jpeg)

### Action metrics

These measure whether your visibility turns into activity on your site: AI traffic, AI-bot activity, and AI-assisted conversions.

#### AI-referred sessions

AI-referred sessions is the volume of sessions on your site that come from AI tools like ChatGPT, Gemini, and Perplexity.

They matter because that traffic converts well: Semrush research found the average AI search visitor is worth 4.4 times more than a traditional organic visitor in conversion value.

Track your AI traffic in [Google Analytics](https://developers.google.com/analytics) by setting up a custom segment that filters for referrals from chatgpt.com, gemini.google.com, perplexity.ai, and others.

![Creating an "AI Referral Traffic" channel on GA4 to show referrals from ChatGPT, Gemini, and Perplexity.](https://static.semrush.com/blog/uploads/media/7e/d8/7ed8dbcbab6118ea4f2ccd5dfcc2c171/3d1a9d7bd7da4f0cd128201be0948e43/image.jpeg)

Once the segment is built, apply it to your traffic reports to see AI-referred sessions broken out from the rest of your traffic.

![The "AI Referral Traffic" row highlighted on the Traffic Acquisition report of GA4.](https://static.semrush.com/blog/uploads/media/f0/46/f0460b331bcbd842222e5a129fa30b93/6bed29e18423cd74206c045fcc00436e/image.jpeg)

You want this trending up. As your mentions and citations grow, AI traffic usually follows.

#### AI bot traffic

AI bot traffic is the volume of requests to your site coming from AI crawlers. These are the bots that AI platforms send to read your content, build their training data, or fetch information for real-time responses.

Tracking this matters because it tells you whether AI tools visit your site and how often they do so.

You can track AI-bot activity on your site by analyzing your server logs. Semrush’s [Log File Analyzer](https://www.semrush.com/log-file-analyzer/) is built exactly for this. All you have to do is upload your server logs, and you’ll get a report that shows which bots are visiting your site and how often they’re making requests.

![Log File Analyzer showing a list of bots visiting a site and how often they're making requests.](https://static.semrush.com/blog/uploads/media/85/7e/857ebbd467fd89c610671dea023741eb/ea2107e4276fa5744e3f430b51ec7bf2/image.jpeg)

Rising AI-bot traffic is a positive signal, though it can mean training-data harvesting, real-time retrieval, or both, and not all of those show up in user-facing answers.

#### AI-assisted conversions

AI-assisted conversions are the signups, purchases, and demo requests that come from AI-referred sessions. They show what AI traffic contributes to your goals.

To track this, apply your existing GA4 conversion goals to your AI-traffic segment.

In [Google Analytics](https://developers.google.com/analytics), go to **Reports** > **Acquisition** > **Traffic acquisition**, select your AI traffic segment, and add your conversion event as a secondary dimension.

You'll see how many conversions are coming from AI traffic and understand its value.

!["Checkout" added as a conversion event on the right and the "AI Referral Traffic" row highlighted on the right of a GA4 report.](https://static.semrush.com/blog/uploads/media/90/06/900608946d72bf99f070a2d199aacb67/1755569ee898ab5573687f53a9438b9f/image.jpeg)

Check whether AI-assisted conversion rates are on par with or higher than your site's overall conversion rate. If AI traffic converts less effectively, treat it as a prompt to investigate rather than a single diagnosis. The cause could be a different intent profile, agents abandoning carts they didn’t fully commit to, checkout friction agents can’t navigate, or less favorable AI recommendations.

## FAQs

### Is there a way to track AI agents’ activities on my site?

Not directly yet. Analytics solutions that specifically track agent activities on your site, such as agents browsing your site, filling out forms, or making purchases, don't exist yet. Tooling hasn't caught up with how quickly the space is evolving.

For now, the closest you can get is by tracking AI-referred sessions in Google Analytics and analyzing your server logs for AI bots. These won't show you what agents are doing on your site, but they'll tell you about your AI traffic and which crawlers are accessing your content.

### Is SEO still relevant in the agentic web?

Yes. The fundamentals of good SEO (technical foundations, content quality, etc.) carry over directly to the agentic web. The mechanics are the same. AI agents crawl your site, read your content, and weigh trust signals like search engines do.

What changes is the goal: You're no longer just optimizing for clicks on a search results page. You're optimizing to be the source AI agent cites, the brand they recommend, and the option they choose to buy from.

### How do I see how my competitors are doing in the agentic web?

Use the [Competitor Research](https://www.semrush.com/ai-seo/competitor-research/) feature in our AI Visibility Toolkit. Just enter your domain and up to four competitors you want to analyze.

You'll see everyone’s AI visibility score and total mentions, along with how they’ve trended over time. Compare the performance to gauge how you’re doing against the competition.

![The Competitor Research report showing how a brand performs over time on visibility, audience & mentions compared to rivals.](https://static.semrush.com/blog/uploads/media/f1/c9/f1c9e7a9a4262883544814df2a863144/31d8b2f7b612b706e1ab89480f1588ae/image.jpeg)

Next, scroll down to explore the topics and prompts relevant to your category, and check whether everyone is showing up for them.

![Topics & Prompts showing brand performance for relevant topics in relation to selected competitors.](https://static.semrush.com/blog/uploads/media/4c/8e/4c8ec0a8d1abb8d8d05a19ad1c09f409/e2d74a729bcb42cae5a099b1f20caa14/image.jpeg)

You can focus on specific prompts where competitors show up but you don't. This surfaces the exact gaps in your AI visibility, so you know which topics to prioritize next.

!["Prompts" and "Missing" filters applied showing prompts where a brand's competitors show up but the brand doesn't.](https://static.semrush.com/blog/uploads/media/53/ef/53ef5e274e42893e8adbdd4f98e4edb3/cf74f88a58408ea98bd100646253b908/image.jpeg)

## Start optimizing for the agentic web

AI agents are already evaluating your brand, and the question is whether they recommend you or a competitor.

Working through the five layers in this guide, from technical foundations to protocols, sets your site up to be found, trusted, and chosen by agents.

Start by checking where you stand.

Semrush's [AI Visibility Toolkit](https://www.semrush.com/ai-seo/overview/) shows how your brand appears across AI platforms today, so you know which layer to work on first.
