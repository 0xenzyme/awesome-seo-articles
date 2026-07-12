---
title: "I rebuilt our content update pipeline in Claude Code. Here's why."
source: "semrush-blog"
content_type: "blog_article"
freshness_risk: "low"
slug: "how-i-rebuilt-our-content-update-pipeline"
url: "https://www.semrush.com/blog/how-i-rebuilt-our-content-update-pipeline/"
canonical: "https://www.semrush.com/blog/how-i-rebuilt-our-content-update-pipeline/"
author: "Carlos Silva"
published: "2026-06-25T14:19:00+00:00"
updated: "2026-06-25T14:19:00+00:00"
categories:
  - "Content"
  - "Marketing"
freshness_reasons: []
fetched_at: "2026-07-12T19:58:21.522192+00:00"
status_code: 200
html_hash: "55b0be9719f410895016aa5652cae08c51de021f462ddc2f5746bdcd292f6a35"
clean_word_count: 1853
clean_char_count: 10905
---
# I rebuilt our content update pipeline in Claude Code. Here's why.

Semrush has thousands of blog posts, and a lot of them are informational pieces readers rely on to learn about topics related to SEO, AI visibility, and content. Keeping those articles current and at the quality bar Semrush is known for is a significant and ongoing job.

For a while, I tried to solve maintaining our informational content with an n8n workflow. It worked for research but broke at drafting.

So, I rebuilt the pipeline in Claude Code. This one handles both research and drafting.

Here's why I made the call to switch from n8n to Claud Code, how the new system works, and what changed for our team.

## What kept breaking with n8n

Updating an existing article is two jobs in one: an audit and a surgical rewrite.

You have to figure out what's stale, where competitors have moved, what the AI search landscape now expects, which new product capabilities to weave in, and how to update the piece without touching what's still working. Multiplying that by a backlog in the hundreds means the workflow has to be fast, accurate, and consistent.

My first attempt to streamline this work was an n8n workflow.

The research half worked. For each article, it pulled together:

- Comprehensive SERP data for the keyword
- The top-ranking competitor articles
- An embedded domain intelligence (EDI) scan comparing our article against those competitors
- Google's AI Overview for the query
- Related searches Google surfaces
- Internal linking opportunities across our own content

![A flowchart showing an SEO content research and analysis pipeline from inputs to draft output.](https://static.semrush.com/blog/uploads/media/ab/79/ab796d5a1470c67467bd0958da1bf0f7/711dc9887a1a0658f0dd4bf28f237d06/image.jpeg)

But the drafting never worked.

The drafts came back somewhat close to what I was looking for, but never close enough to publish.

The voice was off. The structure ignored the style guide. The language was fluffy and verbose. And worst of all, there were hallucinations — the AI sometimes described Semrush features that don't exist, and in convincing detail.

I tried everything I could think of to improve the output. Using different AI models. Tightening the prompts. Splitting drafting into smaller steps. Giving it the style guide. Giving it more past drafts as examples.

None of it produced consistent, high-quality outputs. I'd get an acceptable draft once, then the next run would be wrong in a new way.

Eventually I stopped trying to fix the content I was getting from n8n. The research half still gave us information for briefs the team could write from, so we kept that running and set the drafting aside.

But I couldn’t stop thinking about why the drafting kept failing.

It turns out the failure was structural all along. n8n is great at chaining API calls — fetch this, transform that, and send it onward.

Drafting an article, however, requires editorial reasoning — judgment calls about voice, structure, and what to change. That kind of reasoning needs to consider the whole article at once, plus reference material like the style guide and past examples available as decisions get made.

Workflow tools simply aren't built for that.

## Why I switched to Claude Code

I needed something that could do real editorial work, like read the original article, understand the intent behind the query, and make calls about what to change and what to leave alone.

I looked at a few options and kept coming back to Claude Code.

Here's what made it fit:

Claude Code is an agent that runs inside a folder on your computer. The pipeline is that folder. The style guide, past drafts, the research output, and the article being updated are all files inside it.

Claude Code reads what it needs when it needs it, and the work it does becomes another file the next step can use.

The structural difference from n8n is in how the AI fits into the workflow. In n8n, you build the workflow in advance, and the AI does one specific step, like writing a section or summarizing data.

In Claude Code, the AI runs the workflow itself, reading the files, deciding what to do, and writing the outputs. Combined with skill instructions that tell it what to do at each step, Claude Code has both the context drafting needs and the constraints that keep it from going off the rails.

That's what made the difference.

The AI had access to what it needed when it needed it, and a defined job at each step. The work it produced was a file the next skill could pick up and a writer could open later to check.

I rebuilt the whole pipeline in Claude Code, including the API calls that had been working fine in n8n. With everything in one folder, the drafting step could read the research output, the original article, past drafts, and the style guide whenever it needed them.

And it worked.

The pipeline produces drafts our writers can edit and publish, and a trail of files they can check when something looks off.

## Nine skills, end to end

The pipeline I built in Claude Code is nine skills, chained together by a master script that runs them in order.

I give it the URL of the article I want to update and a target keyword, and I get back a draft. The draft goes through our normal editorial workflow the same as any other article: review, revisions, editing, and images. Our team makes every editorial call.

Here are the nine skills:

1. Fetch the live article
2. Research the SERP and competitors
3. Run an EDI semantic similarity check against our existing piece
4. Synthesize an update plan
5. Identify outdated content
6. Audit product mentions
7. Draft the updates
8. Generate a side-by-side comparison of the original and the new draft, with changes highlighted
9. Format the result for publishing

![A workflow showing Claude Code automating nine SEO content update steps from URL and keyword to a writer-ready draft.](https://static.semrush.com/blog/uploads/media/3c/38/3c38390f5be60fe6117611e4dfe4e4d5/81a49ea2e298543f4003940cf6a94ab9/image.jpeg)

I kept it at nine skills on purpose. It was the smallest number that gave me a distinct skill for every decision the pipeline needed to make.

And one design choice turned out to be really important. Every skill saves its work to a file before the next one runs.

Those files are what I call the pipeline's artifacts. They include the research, the plan, the draft, and the side-by-side comparison. Saving each step as a file means any single skill can be re-run without starting over, and anyone can open the files to check when a draft looks off.

## What changed when the Claude Code pipeline ran

Two things changed when the Claude Code pipeline started working:

1. The hallucinations the AI still occasionally produced became easy to catch
2. The drafts started reading like we wrote them

Any AI generation step can hallucinate sometimes. The pipeline is built to catch them fast.

Dana — one of our contributors — was reviewing a draft and ran into plausible-looking instructions for a feature that doesn't exist. The kind of error that, in the old n8n version, would have either slipped through or cost twenty minutes of cross-checking.

She opened the side-by-side diff, looked at the same section in the original article, saw the original didn't mention the workflow, and replaced the fabrication. The whole thing took about a minute.

Here’s what the diff artifact looks like:

![A side-by-side comparison of original versus draft with new URL parameter guidance added to an existing content section.](https://static.semrush.com/blog/uploads/media/e6/2e/e62eae470a34e83f8f09989be54c10aa/97f47611a12d0a443136e1747a3450f0/image.jpeg)

That's what the artifacts are for. The AI is still going to make mistakes. The pipeline is built so a reviewer can catch them and check in one minute instead of 20 minutes.

The bigger story is what happened across runs.

For months, I'd been trying to get the drafting step to produce something that read like Semrush. Meaning the right approach to voice, tone, structure, and how we describe our own products. In n8n, I'd get a draft that maybe nailed one of those things and missed three others. And the next run, I’d get a different combination.

But in Claude Code, three runs with small adjustments between them got me there. By the third, the drafts were consistently strong.

The voice matched the existing article. The structure followed our style guide. The tone was Semrush. The brand positioning was right. The AI got the product descriptions correct. The same kind of errors didn't keep showing up in different places.

This was the part I hadn't expected. Months of adjustments in n8n hadn't gotten me here. Three runs in Claude Code did.

Dana still caught things, but they were the smaller editorial fixes any draft needs, like sharpening an opening, reframing a section, or smoothing a clunky transition. The drafts no longer arrived with the bigger problems n8n had given us, like the wrong voice, ignoring the style guide, or fabricated Semrush features.

Dana's feedback after several runs was that the writing was much better than what we'd produced before. And the side-by-side view was actually useful.

![Feedback on Claude Code content from a writer talking about how the piece was easy to work with and how the writing feels better.](https://static.semrush.com/blog/uploads/media/f7/cf/f7cfa6a2ad1d9e8145648b1e5615ca13/8ed73d615741f7547d57551f9ab9484f/image.jpeg)

## What ended up mattering

Three things held up across every run.

1. **Drafting needs full context**. Treating the LLM as one step in a workflow gives you inconsistent writing. The drafting work has to see the article, the style guide, and the research at the same time.
2. **The trail of files is the system**. Every skill saves its work before the next one runs. That trail is how our team catches problems, and how I can re-run any single step without starting over.
3. **Fewer skills, more refinement**. Nine covered the work. Every time I've been tempted to add a tenth skill, the right move has been to sharpen one of the existing nine.

![File explorer showing a numbered sequence of markdown and JSON files for an AI content pipeline.](https://static.semrush.com/blog/uploads/media/c6/52/c652f998c16b513c74006ace41734d5e/7aeddcd08a7c767e33fd5994991cc661/image.jpeg)

The pipeline is running, the team is using it, contributors are saving substantial time, and the feedback has been more positive than anything we've had with AI-generated content.

If you're hitting a quality ceiling with AI content, start by asking where your AI is making its writing decisions. If they happen inside a workflow step, that's where the ceiling is coming from.

Move the drafting work somewhere the AI can read your files directly. That might be an agent like Claude Code or any tool that gives the AI persistent access to reference material. That's the move that broke through the ceiling for us.
