---
title: "How to Do Prompt Research for AI SEO"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "prompt-research-for-ai-seo"
url: "https://www.semrush.com/blog/prompt-research-for-ai-seo/"
canonical: "https://www.semrush.com/blog/prompt-research-for-ai-seo/"
author: "Sergei Rogulin, Cecilia Meis"
published: "2026-02-03T13:17:00+00:00"
updated: "2026-02-03T13:17:00+00:00"
categories:
  - "AI"
freshness_reasons:
  - "time_sensitive_title"
schema_genre: "AI"
fetched_at: "2026-06-12T18:43:28+00:00"
status_code: 200
html_hash: "6aceb98bc10dfcb6d895abd45d2f65f3f0f664ce5582da387fe18bbecce95077"
clean_word_count: 2692
clean_char_count: 18454
---
# How to Do Prompt Research for AI SEO

Prompt research is the process of identifying and tracking the questions that cause AI systems to compare options and recommend specific brands.

The prompt research process serves the same foundational role for AI visibility that keyword research serves for SEO and PPC but the unit of measurement is different. Instead of pages and queries, prompt research focuses on how AI systems form and present recommendations.

In AI SEO, visibility only matters when AI is evaluating choices. That’s when it weighs alternatives, applies constraints, and points someone toward a solution. If your brand isn’t present in those moments, it won’t factor into the decision.

Most prompts never reach that stage. They generate explanations, summaries, or general guidance. Prompt research filters those out and focuses on middle- and [bottom of the funnel (BOFU)](https://www.semrush.com/blog/lower-funnel-marketing/) prompts: comparisons, evaluations, and "best" queries where AI weighs alternatives and recommends solutions.

To show how prompt research works in practice, I’ll walk through the exact process I use to track Semrush’s own [LLM visibility growth](https://www.semrush.com/blog/how-we-are-using-semrush-to-drive-llm-visibility/).

My prompt research process follows four steps:

- Identify target audiences and buyer personas
- Describe solutions and how they help those audiences
- Use keyword research as supportive language input
- Use an LLM to generate BOFU prompts for tracking

By the end of this guide, you'll have a repeatable way to build a prompt set that shows where your brand competes and where it doesn't. But first, let's clarify how prompt research differs from the keyword research you already know.

## How Prompt Research Differs from Keyword Research

For search marketers, prompt research introduces a familiar concept with new challenges. Unlike traditional search, we don't have years of historical search volume, CPC, or trend data for AI prompts.

Because of that, prompt tracking doesn’t behave like keyword tracking.

SEO rankings tend to be relatively predictable. AI-generated answers are volatile and personalized. Prompt research focuses on direction and pattern recognition, not fixed positions or precise counts.

The contrast becomes clearer when you look at how the two approaches differ in practice.

![prompt research vs keyword research](https://static.semrush.com/blog/uploads/media/7e/60/7e6089b91348ff10c8b789c392ea3358/4bd9c26999fb6a28665c220c9e83af4f/EN-Prompt-Research-1.png)

Even with these differences, the objective hasn’t changed. You’re still defining a set of target questions, improving your visibility around them, and measuring performance over time.

What *has* changed is how visibility is discovered and evaluated.

Semrush has built a [prompt database informed by real clickstream data](https://www.semrush.com/kb/1607-semrush-ai-visibility-data#prompt-database-vis) from ChatGPT and other AI platforms, allowing you to estimate topic volume as it happens on LLMs.

### Is Keyword Research Still Relevant?

Yes.

Keyword research still plays an important supporting role because it reveals how people describe problems and what intent sits behind their searches.

Those signals help you decide which prompts are worth targeting. The difference is that keywords are no longer the endpoint; they’re a language input that gets rewritten into natural, conversational prompts.

The larger shift is what you optimize for.

Instead of tracking “wins” the way you would in SEO, prompt research looks at which topics, constraints, and personas consistently recommend your brand, and where it fails to appear. That’s why prompt research prioritizes the [ideal customer profile](https://www.semrush.com/blog/customer-profile-template/) (ICP), or type of customer a product is built for, over cost-per-click.

The guiding question changes from which terms are cheapest or highest volume to whether your brand appears for the types of intent that reflect real buying situations.

[Tracking AI responses](https://www.semrush.com/kb/1503-ai-search-tracking) over time makes that visibility observable. Daily snapshots of AI answers create a running record of how your brand is framed, compared, or omitted across decision-oriented prompts.

With that foundation in place, the next step is building a prompt set that reflects how your buyers actually make decisions.

## 1. Identify Your Target Audience

[Personas](https://www.semrush.com/blog/buyer-persona/#how-do-you-do-buyer-persona-researc) define what questions get asked. That’s true for keyword research and prompt research alike. But for prompt research, personas also determine whether AI recommends anything at all.

That’s because constraints are what push AI systems out of explanation mode and into recommendation mode. A generic question like “what’s good dog food?” produces education. A constrained question like “best limited-ingredient dog food for a dog with stomach issues under $60/month” forces a comparison.

Before generating prompts for LLM tracking, focus on the persona traits that change how AI evaluates options:

- **Context & experience level**: who’s asking and in what situation
- **Primary risk or pressure**: what they’re trying to avoid or resolve
- **Language & expertise**: casual vs. technical phrasing
- **Budget expectations**: affordable, mid-range, or premium

For example, a dog parent managing food sensitivities might input, "best limited-ingredient dog food for stomach issues." A different owner feeding healthy large dogs may search for "affordable dog food for large breeds," while a premium shopper focused on nutrition looks for "human-grade, single-protein fresh dog food."

The category stays the same, but the constraints and the recommendations AI returns change with the persona.

### Where to Tap into Persona Characteristics

Buyers reveal how they think, speak, and make decisions in open, unfiltered spaces like message boards, reviews, and support discussions where they talk about products in their own words.

![persona data to inform prompt generation](https://static.semrush.com/blog/uploads/media/1d/87/1d875b44560651a320332321874ca7b3/818fda2c9cbcf6f1558b687700594567/EN-Prompt-Research-2.png)

Personas that consistently uncover risk management, trade-offs, and uncertainty reduction create the strongest foundation for prompt research. Their constraints naturally force AI systems to compare options and make recommendations.

## 2. Connect Your Product’s Solutions to Your Persona’s Problems

When people ask AI to help them choose between options, they’re rarely comparing feature lists. They’re trying to decide whether a product fits their situation, reduces risk, and feels like a safe choice.

AI recommendations tend to reflect that behavior. Brands are suggested more often when their products clearly resolve the specific hesitation a buyer feels at the moment of decision.

Your product needs to be described across the sources AI systems rely on in terms that help a buyer decide, not just understand.

 These details include:

- **Features:** What the product delivers in concrete terms.
   These are factual attributes AI can reference directly (e.g., “single-protein formulas,” “SOC 2 compliant,” “native Shopify integration”).
- **Benefits:** Why those features matter to the persona.
   Benefits translate features into outcomes that reduce concern (e.g., “easier digestion,” “faster onboarding,” “lower implementation risk”).
- **Use cases:** Situations where the product fits cleanly.
   These help AI match solutions to scenarios (e.g., “for sensitive stomachs,” “for small teams,” “for regulated industries”).
- **Problems resolved:** The specific risk, friction, or uncertainty the product removes.
   This is often the strongest recommendation trigger (e.g., avoiding allergic reactions, preventing costly mistakes, reducing vendor lock-in).
- **Fit factors:** Indications that make the option feel safer or smarter than alternatives, such as clarity, simplicity, consistency, or alignment with buyer expectations.

Together, these elements describe much of the logic that AI systems use when comparing brands.

### Validating Which Attributes Matter in AI Comparisons

If you need help determining which attributes are driving persona preferences, leverage [Brand Performance](https://www.semrush.com/ai-seo/brand-performance/) in the Semrush AI Toolkit. This tool shows which features AI already emphasizes when comparing brands in your category.

For example, for the business Dover Saddlery, AI consistently explains its recommendations using operational fit indications, like “one-stop assortment depth” when buyers need multiple items at once and “fast, reliable fulfillment.”

![AI narrative drivers comparison from semrush](https://static.semrush.com/blog/uploads/media/2d/11/2d11e43fed2bb40ec86603b75075a279/1a45a5c139fc2bef45af02b514275591/image.png)

These are the reasons AI gives when justifying why Dover is a viable choice in a specific decision context. Collectively, they position the brand as a dependable, low-risk outfitter which is the signal AI needs to recommend a retailer when the buyer’s priority is reliability over exploration.

![Semrush AI brand performance key business drivers](https://static.semrush.com/blog/uploads/media/e9/fb/e9fb8465c0a5c616016333a6c52b6213/06a41632c45b07c135dc512c7b6ed69a/image.png)

These attributes become the building blocks for prompt generation. When you feed persona constraints and product fit factors into an LLM, you give it the context it needs to generate decision-stage prompts, not generic questions.

## 3. Use Keyword Research to Support Prompt Discovery

Keyword research validates language for prompt research by confirming how your audience naturally frames problems rather than estimating demand.

Tools like our [keyword research tool](https://www.semrush.com/analytics/keywordmagic/) reveal patterns in language, including:

- Which constraints appear repeatedly
- Which modifiers feel natural versus technical
- Which brand-plus-ingredient combinations show up consistently

Start with a topic tied to a constraint. In this case, “dog food ingredients” reflects how ingredient-sensitive buyers might frame the problem.

![keyword magic tool ideas related to dog food](https://static.semrush.com/blog/uploads/media/72/cd/72cdb057bbed0abe59458dabc35bdf41/04658940399bc8d0bd8375517539f74c/image.png)

Phrases like “limited ingredient dog food,” “best limited ingredient dog food,” and “limited ingredient dog food for allergies” recur across commercial and mixed-intent searches.

This consistency indicates how buyers in this niche phrase their options and modifiers. Keyword research helps validate language, but it doesn’t show how AI systems respond to that language in practice.

### Use Prompt Research to See How AI Responds

Once you’ve identified persona language, enter that wording into the [Prompt Research](https://www.semrush.com/ai-seo/prompt-research/) tool to explore how AI systems are responding to the topic.

For example, we entered “limited ingredient dog food” in the Prompt Research tool.

![prompt research topics related to dog food](https://static.semrush.com/blog/uploads/media/65/29/65299cb3cb7abb5aec297a3e37613723/f3863fae90c720c0ed03c5cc89d67161/image.png)

In the “**Topics”** view, AI clusters the category around formulations and brands, including hypoallergenic diets, limited ingredient products, and brand-specific variants. That structure indicates the “limited ingredient” topic already aids decisions, making it a strong candidate for a BOFU prompt.

## 4. Generate a List of BOFU Prompts for LLM Tracking

The [Prompt Research](https://www.semrush.com/ai-seo/prompt-research/) tool can uncover early prompt candidates for a quick start to query selection. Many of these, however, reflect exploratory questions that don’t make for reliable tracking. Prompts such as “What should I feed my dog?” rarely represent a real decision moment.

Instead, prioritize prompts that introduce constraints and force a choice for a specific persona, like “What’s a good dog food for a dog with digestive issues that isn’t expensive?” These are the prompts where brand mentions appear, and preferences start to form.

Once you can recognize what a trackable prompt looks like, you can use an LLM to efficiently generate and expand a focused prompt set at scale.

### How to Generate Decision-Stage Prompts with an LLM

Effective BOFU prompts require context. The LLM needs clarity on:

- Who is asking
- What outcome they’re trying to avoid
- What constraints shape the decision
- How the buyer naturally describes the problem
- That the question must result in a recommendation or comparison

With that context in place, the output shifts away from education and toward evaluation.

A best practice is to use a consistent pre-prompt to keep outputs focused on BOFU intent.

For example:

*Act as a buyer research assistant. Generate decision-stage questions that would cause an AI system to compare and recommend specific brands.*

*Buyer context:*
– Persona: [describe the buyer and situation]
– Primary risk or concern: [what they want to avoid]
– Constraints: [budget, requirements, exclusions]
– Language cues: [phrases the buyer uses]

*Instructions:*
– Do not include brand names in the questions
– Each question must require a recommendation or comparison
– Avoid educational or definitional phrasing
– Write prompts exactly as a real buyer would ask them

This template keeps every generation run aligned with decision-stage output.

If the output still feels educational (and not recommending any brand), tighten the constraints and try again until the model makes a recommendation.

When brand mentions appear consistently, and the questions reflect a real choice being made, you’ve reached a prompt worth tracking.

### Account for Query Fan-Out in Your Prompt Set

Query fan-out is the process of how AI systems break a prompt into several smaller queries, find answers to each, and combine them into one complete response.

![depiction of query fan out](https://static.semrush.com/blog/uploads/media/42/fc/42fceb342432f1c3dac1faf47b9152c6/60617035ac1771f8403d1f9ff6c67a14/image.png)

When someone asks "best limited-ingredient dog food for allergies," AI systems like ChatGPT and Google AI Mode break that question into multiple sub-queries, which could be:

- Hypoallergenic dog food recommendations
- Single-protein dog food brands
- Grain-free dog food for sensitive stomachs
- Dog foods without common allergens

The AI then retrieves information for each sub-query and merges it into a single response. This process allows AI to provide richer, more specific answers, even when no single source directly addresses the original query.

Track these variations to see how well you appear for all queries related to intents. If your brand appears across variations, you'll have a better chance of being recommended.

This approach mirrors how AI systems actually process queries, helping you build a prompt set that captures the full range of sub-queries AI might generate when evaluating your category.

## 5. Track Your Prompts and Measure Visibility Over Time

Once you've built your prompt set, the final step is to [set up your LLM prompt tracking](https://www.semrush.com/blog/llm-prompt-tracking/) to see how AI responds over time.

Semrush offers [Prompt Tracking](https://www.semrush.com/kb/1503-ai-search-tracking) via the Position Tracking tool.

Start a new campaign by entering your target AI platform prompt list to track.

![img-semblog](https://static.semrush.com/blog/uploads/media/90/83/90835eb1aae9aa116042747a2ff52d23/b94e8f7609246b885377c3998d659556/image.png)

Once your campaign is running, Semrush checks these prompts daily and records whether your brand appears in the AI-generated response. You’ll see AI Visibility, Mentions, and Average Position from the Landscape tab.

![img-semblog](https://static.semrush.com/blog/uploads/media/c9/a0/c9a0c7c3ffb8a08d7e738fdc82d0fedd/513439b721fd3f981aff061e87250fdc/image.png)

This helps you measure where you’re present, where competitors are winning, and where you’re missing visibility.

To report on progress, it's also easy to generate a PDF from your tracking campaign.

### How Many Prompts Should You Track?

To understand your AI visibility, track as many distinct decision-stage prompts as your allowance supports, focusing on different decision contexts rather than minor wording variations.

Each [Semrush One](https://www.semrush.com/blog/ai-search-with-semrush-one/) plan includes a fixed allowance of tracked prompts. This allowance determines how many unique prompts you can monitor at the same time (for example, 50, 100, or 200).

With a smaller prompt allowance, focus on prompts that might recommend your products or services that drive revenue.

Track a tight set of decision-focused prompts for each product or service. Based on our internal testing, 10 well-chosen prompts per product are usually enough to see whether AI systems consistently recommend your brand or default to competitors.

With a larger allowance, add prompts only where evaluation criteria change, like persona, industry, or use case rather than using small wording variations that usually produce the same AI behavior and don’t create new signals.

You can also align some tracked prompts with keywords you already monitor in SEO to compare search visibility with [AI visibility](https://www.semrush.com/blog/how-we-are-using-semrush-to-drive-llm-visibility/).

## Turn the Growth of AI Into an Actionable Signal for Your Marketing

As AI platforms influence more buying decisions, many brands still don’t know whether they’re being recommended or overlooked. Prompt research addresses that uncertainty by focusing on the moments where AI evaluates options and recommends a solution.

With Semrush, those decision moments become measurable signals you can monitor, interpret, and act on over time.

Start by documenting one persona and generating 10 decision-stage prompts this week. Add them to Semrush's [Prompt Tracking](https://www.semrush.com/position-tracking/?filter=geo), then monitor where your brand appears, where it doesn't, and how AI frames your category.

From there, AI visibility becomes something you can work with, not guess at.
