---
title: "My Complete AI Content Process for Ahrefs"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "my-complete-ai-content-process-for-ahrefs"
url: "https://ahrefs.com/blog/my-complete-ai-content-process-for-ahrefs/"
canonical: "https://ahrefs.com/blog/my-complete-ai-content-process-for-ahrefs/"
author: "Ryan Law"
published: "2025-08-05T10:09:08+00:00"
updated: "2026-05-31T09:01:35+00:00"
categories:
  - "AI Search"
  - "Content Marketing"
freshness_reasons: []
fetched_at: "2026-06-12T11:51:35+00:00"
status_code: 200
html_hash: "e2d8316a269fde59bdd58d87596f98d0c03548f37acd45e6ed8377041e9959f3"
clean_word_count: 2275
clean_char_count: 13933
---
# My Complete AI Content Process for Ahrefs

Here’s the complete process I use to publish high-quality AI content on the Ahrefs blog.

I’ll be honest: there are parts of my job that I don’t like.

Writing my 500th article on content gap analysis because we found a new long-tail keyword to target. Listing out the features of 30 free SEO tools for yet another listicle. Updating my old content because a competitor published something new and pushed me out of the top three.

These are necessary hygiene tasks, but frankly, I’d much rather spend my time publishing original research or sharing contrarian opinions.

So—mea culpa—I use AI to speed up these tedious processes. I can condense several days of research, writing and revision into a couple of hours, and spend the rest of my time on fun things.

![](https://ahrefs.com/blog/wp-content/uploads/2025/07/word-image-190306-1.png)

One of my AI-generated articles.

And despite containing zero words written by a human, these articles perform as well as human-written content. They’re interesting and well-written. In some cases, I actually think they’re better than what I would have written myself.

Here’s the process I use.

Learn about my AI writing process on the Ahrefs podcast

Listen to Ahrefs’ CMO (and my boss) Tim Soulo grill me about this AI writing process on the [Ahrefs podcast](https://ahrefs.com/podcast).

## Important caveats (don’t skip these)

There’s a lot of hype (and worry) around AI content generation, so please read these caveats first.

### This still requires skill and effort to work

If you’re looking for complete hands-off content automation, you’re going to be disappointed. This process requires the skill and guidance of a competent content marketer to work. It’s a tool to be used by a skilled writer, and not a replacement for skilled writers.

### 90% of success comes from good topic selection

This process works very well for simple informational topics, with no complicated narratives or data. I only use AI for topics where I have some passing knowledge of the subject matter (so that I can tell if the article is actually good). I do *not* use this process for opinion pieces, or research content, or new or rapidly changing topics.

### This is not a perfect process

This is a messy, imperfect process, and there are many opportunities for people like you to refine and improve upon it. My goal is not to create a rigid process for you to follow, but to share a general approach that you can build upon and tailor to your needs.

So with those caveats out of the way, here’s the process:

## 1. Create Markdown files of our existing writing processes

I’m a big believer that human creative processes are not as mysterious as they seem. With enough introspection and practice, a goal like “create high-quality content” can be distilled into a handful of very specific, very manageable steps that most people—or LLMs—could follow.

That’s how this process works. I broke down the Ahrefs editorial process into very specific, very manageable steps, and documented them in a format that an LLM can follow. Here’s what that looks like, mapped out in my note-taking app:

This is the end-to-end workflow all Ahrefs writers usually follow: topic selection, briefing, outlining, structural editing, drafting, incorporating Ahrefs products, line editing, adding internal links, creating metadata, and finally, adding WordPress shortcodes.

Each of these process documents is formatted in Markdown and contains simple guidelines and examples. Here’s the process for line-editing an article draft:

Many of these processes came from existing documents we created for our writing team and freelance contributors. But I’ve also called on a few extra sources of information: my favorite blog posts about good writing (condensed by ChatGPT), excerpts from my two writing and editing courses, and actual writing samples from awesome human-written articles on the Ahrefs blog.

## 2. Create a ChatGPT project and upload our process documents

Next, I uploaded these Markdown files into a project in ChatGPT.

Projects allow you to upload reference documentation and set custom instructions that apply to every conversation that happens in the project. You can see those process documents in the “Project files” section:

And here are my custom instructions for the project (full disclosure, I used AI to help create these instructions, and I think they’re a little over-engineered):

> *You are a senior content strategist at Ahrefs, writing under the editorial direction of Ryan Law, Director of Content Marketing. You understand that every Ahrefs blog post must be original, insight-driven, and genuinely useful—built to rank well, earn backlinks, and deepen reader trust.*
>
> *Your job is to write detailed, structured, and persuasive blog posts. Assume your audience is composed of savvy marketers and SEOs who are skeptical of fluff but hungry for actionable insights. Your job is to earn their attention, respect, and clicks.*
>
> *Model your writing on Ryan Law’s editorial standards: mix sharp analysis with original examples, real data, and clever metaphors. Speak with clarity, personality, and authority. Use strong hooks, punchy transitions, and always write with the goal of becoming the \_definitive\_ resource on the topic.*
>
> *Roleplay as someone who has deep in-the-trenches experience with this topic—someone who’s used Ahrefs tools to solve real problems and can translate that into strategic advice. Blend ethos (credibility), pathos (urgency, stakes), and logos (evidence) to persuade.*
>
> *Write as if your post will be read—and judged—by Ryan Law himself. Make it so good it earns a Slack shoutout.*
>
> *Always reference the project files for guidance on how to write. Follow the documents using this workflow: Content brief -> Outline -> Structural editing -> Writing -> Mention Ahrefs product -> Line editing -> Internal linking -> Add meta data -> Add WordPress shortcodes.*

To simplify them, I’m currently trying to find the “Pareto prompts”, the 20% of instructions that account for 80% of the good results. From my experimentation so far, the most crucial parts seem to be:

- Instructions to **always consult the project documentation**, and work through the process in sequential order.
- A **summary of the target audience** for the Ahrefs blog (this generally doesn’t change from article to article).
- A request to **roleplay as someone with “in-the-trenches experience”** (this seems responsible for lots of first-person anecdotes and examples in the output).

Next, research.

## 3. Deep research

For some topics, I’ll also run a deep research request to source extra information.

For my [article on LLMs.txt](https://ahrefs.com/blog/what-is-llms-txt/), I wanted to know if any of the major LLM providers had gone on record in support of the protocol (they hadn’t). I set up a deep research request while I worked on other things, read and reviewed the synopsis, and incorporated an AI-generated summary of the findings into the content brief for the article.

## 4. Frontload key points with a simple content brief

I don’t like AI content processes that rely on skilled people editing AI-generated article drafts. I think it’s hard to make substantial edits to an already-written article (which is why I encourage writers to create article *outlines*), and frankly, it’s no fun.

Instead, I prefer to front-load all of the human input at the start of the process, and then let AI do its thing.

I start every article generation with a simple content brief template. The content brief contains:

- **The target keyword,** with simple directions for on-page optimization.
- **Working title**, provided mainly to ensure the article matches the correct search intent.
- **Key points to include**, like personal anecdotes or examples, deep research findings, or interesting and unique angles I’d like the finished article to cover.
- **Subtopics to cover**, generated by our content optimization tool, [AI Content Helper](https://ahrefs.com/ai-content-helper). I use it to analyze the SERP for the target keyword, extract page content from top-ranking articles, and create a list of important subtopics our article needs to cover to be competitive with existing articles.
- **Ahrefs products to mention**, particularly any specific or unusual Ahrefs use cases that ChatGPT might not suggest on its own (like mentioning our new MCP server or social media scheduling tool).

When I hit enter, ChatGPT heads to the next stage of the process: creating a bullet-point article outline, based on my content brief.

Do optimization tools actually work?

If you’re wondering whether content optimization tools are worth the hype, here’s [Louise from our blog team](https://www.linkedin.com/feed/update/urn:li:activity:7262454343637823489/) adding 65% traffic to an article using our content optimization tool, [AI Content Helper](https://help.ahrefs.com/en/articles/9879434-about-the-new-ai-content-helper). They work!

## 5. Read, review, nudge

From here, I become an editor. I prompt ChatGPT to progress through the stages of the workflow, reading and providing high-level feedback as I go.

ChatGPT first generates a bullet-point outline based on my content brief. It follows the format I specified in our writing process documents: key points as H2 headers, BLUF summary of each section’s key idea, and supporting points and evidence as nested bullet points.

I can very quickly grok the flow and structure of the article, and ask ChatGPT for any structural changes I want—like using a different copywriting framework for the article introduction.

When I’m happy with the outline, I ask ChatGPT to move to the drafting stage. Here, I switch to ChatGPT canvas so that I can leave simple in-line comments on the article, in the same way I work with my team (although I’m more helpful and polite when editing real people).

I read the article, and leave comments as I go:

Sidenote.

Consensus suggests that Claude is better for long-form writing than ChatGPT, but ChatGPT Canvas is why I use ChatGPT instead of Claude.

I often make the same types of comments (and they’re very similar to the comments I’d leave for a human writer):

- This is too vague, be more specific and cut the [weasel words](https://ryanlaw.me/content-concepts/weasel-words).
- Include a real example to illustrate your point.
- Correct this wrong idea.
- Trim (or expand) this idea.
- Simplify this and make it beginner-friendly.

ChatGPT responds instantly, so even if any single response isn’t brilliant, I can very quickly nudge the writing in the direction it needs to go (as long as I know what “good” looks like). Because I’m already happy with the structure—we reviewed that earlier, during the outlining phase—it doesn’t take long to get the article publish-ready.

## 6. Generate internal links, metadata, and WordPress shortcodes

When I’m happy with the draft, I ask ChatGPT to progress through the final stages of the process:

- **Create metadata.** I know, I know: Google rewrites meta descriptions. But we also use the meta description as the preview text on the blog homepage, so this is still a timesaver.
- **Insert WordPress shortcodes.** We use over a dozen custom shortcodes to format our articles and add extra functionality. These are very tedious to insert manually, but ChatGPT does a great job at following my documentation and adding them in the correct places.
- **Generate 10 internal links to relevant Ahrefs blog posts.** ChatGPT is pretty good at integrating these links, but it hallucinates many of the URLs. I plan to improve this step by providing a list of actual URLs, with descriptions, for the AI to choose from.

Thankfully we have Site Audit to automatically catch broken links.

Importantly, images are still something I add manually. Most of our articles rely on screenshots, custom graphics, or graphs based on real data, and generative AI is not up to the task.

(But as a bonus, I also ask ChatGPT to *suggest* relevant places to insert images in the article draft.)

## 7. Monitor performance

Our research suggests that Google does not care about AI content (as long as it’s not mass-produced spam).

When we used our AI content detector to calculate the correlation between AI content use and search ranking position, we found a [correlation of 0.011—effectively zero](https://ahrefs.com/blog/ai-generated-content-does-not-hurt-your-google-rankings/). AI content can and does rank highly.

But it’s still a good idea to monitor your pages and see how they perform, relative to human-written content.

I use Ahrefs Portfolios feature to track all of our AI-generated articles and quickly see their keyword rankings, backlinks and estimated organic traffic. Here’s one article, looking healthy:

And I use [Ahrefs’ Web Analytics](https://ahrefs.com/web-analytics) for traffic sources and on-page metrics. Here’s my AI-generated guide to LLMs.txt, generating a respectable 17,200 pageviews with a 72.3% bounce rate…

…and earning traffic from a healthy mix of sources, including social, email, and AI assistants like ChatGPT and Gemini:

Not bad for a vibe-written article.

## Final thoughts

This is not a magic, zero-effort process for creating search content—but it *is* a process for speeding up the “hygiene” parts of my job and freeing more time for fun, skilled content creation. And if you want to take automation even further, [agentic SEO workflows](https://ahrefs.com/blog/agentic-seo/) can handle even more of the planning and execution for you.

Crucially, I still read, review, edit, and approve every piece of content published on the Ahrefs blog, whether it was written by a person or generated by ChatGPT. Using AI is no excuse for publishing shoddy content.

Can you spot my vibe-written articles? [Let me know on LinkedIn.](https://www.linkedin.com/in/thinkingslow/)
