---
title: "How We Use AI for Every Article Without Making AI Slop"
source: "ahrefs-blog"
content_type: "blog_article"
freshness_risk: "low"
slug: "how-we-use-ai-without-making-ai-slop"
url: "https://ahrefs.com/blog/how-we-use-ai-without-making-ai-slop/"
canonical: "https://ahrefs.com/blog/how-we-use-ai-without-making-ai-slop/"
author: "Si Quan Ong"
published: "2026-08-28T13:05:40+00:00"
updated: "2026-08-28T13:05:40+00:00"
categories:
  - "Content Marketing"
freshness_reasons: []
fetched_at: "2026-09-08T09:16:11.916645+00:00"
status_code: 200
html_hash: "fe7b70cb375a5eeb1d81df26f1e09f662d9371689578a4e0b725f1251e4c8dc6"
clean_word_count: 1806
clean_char_count: 10362
---
# How We Use AI for Every Article Without Making AI Slop

Every article we publish at Ahrefs uses AI in some way.

(It could... but that's not how we use it, and I'll explain why.)

Crucially, I don’t think the amount of AI involved is what makes something slop. Nor is it the usual stylistic tells: too many em dashes, words like “delve”, or those “it’s not X, it’s Y” constructions.

Remove every em dash and banned phrase and congratulations: you may now have slop with cleaner punctuation.

Here’s my attempt at defining what AI slop is:

AI slop is content published without enough human understanding, judgement, evidence, or original contribution to justify the reader’s attention.

In short, **slop transfers effort from the creator to the reader**.

The publisher skips the difficult parts: investigating the topic, verifying claims, developing an opinion, and deciding what matters. The reader then has to work out what is trustworthy, relevant, or written by someone who understands the subject.

The creator saves time. Everyone else pays for it.

At Ahrefs, using AI-first does not mean abandoning the practices that made content worth reading before AI. It means finding ways to preserve them even when AI takes on more of the work.

## 

## 1. Do the human work before you draft

For most writers, writing used to be the doing. It was where the hours went. AI has made that part incredibly cheap, so more of our effort has to move upstream: deciding what deserves to be written, how to structure the post, and what we can contribute.

Before I ask AI to write prose, I want a rough premise that answers:

- **Reader**: Who is this for, and what are they trying to accomplish?
- **Promise**: What should they understand or be able to do after reading?
- **Point of view**: What am I actually trying to say, and where might someone disagree?
- **Evidence**: Which claims need sources, data, demonstrations, or expert input?
- [**Information gain**](https://ahrefs.com/blog/information-gain/): What can we add that isn’t already sitting in the search results?

You can see these are not new. They exist before AI and *should* exist even with AI.

AI can help to answer those questions. I can ask it to map the SERPs, challenge my angle, find counterarguments, or point out missing evidence. But it shouldn't make those decisions for me.

Planning is only half of it. The model also needs something interesting to work with.

Give it the same internet everyone else has, and it will give you a version of the same article everyone else has. A detailed style prompt won't fix that. You need raw material it could not have produced by itself: interviews, internal knowledge, proprietary data, real demonstrations, failed experiments, and specific examples from your work.

This is where you need things like a Source of Truth for your work. For example, my colleague [Mateusz built a Source of Truth app in Letaido](https://ahrefs.com/blog/agentic-marketing/): a searchable library for the information that his agent and he rely on when making content.

His tool stores four types of content: facts and stats, explanations, product details, and how-to guides.

Personally, the biggest practical change I’ve made is to talk instead of type.

When I type, I edit as I go. I turn the mess in my head into a tidy summary before AI sees it. Unfortunately, the mess often contains the useful part: uncertainty, caveats, opinions, and half-formed connections.

So I dictate using [Wispr Flow](https://wisprflow.ai/). I walk around my room or sit at my desk and talk. I rant, trying to offload as many things as possible from my head so I can give AI more raw material to work with.

Yes, I basically run a podcast episode with myself. Unedited.

Or I ask AI to interview me, find the gaps, and pull out possible claims before proposing an outline. It is no longer being asked to invent the substance. It is organising and interrogating substance I've supplied.

## 

## 2. Create places to stop and pass judgment

AI is very good at hiding decisions inside polished prose.

A one-shot prompt chooses the research, angle, structure, claims, examples, and tone all at once. By the time you see those choices, they have been packaged as an article. They feel more settled than they are.

That is why [Ryan's pipeline](https://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/) mirrors a human editorial workflow instead of producing one mysterious final file. The research, content gaps, outline, and draft are saved separately. He can inspect any stage, fix the output or instruction that caused the problem, and restart from the last acceptable point.

You do not need a 23-skill Claude Code pipeline to copy the principle. Break the work into stages and put a decision between them:

- **Idea gate**: Do we have something useful to add, or would this article simply repeat what’s already ranking?
- **Outline gate**: Does every section help the reader and support the article's promise?
- **Evidence gate**: Can we support the important claims? What still needs testing or verification?
- **Draft gate**: Has AI smuggled in certainty, filler, or examples we didn't earn?

At every gate, the writer has to pass judgement. That might mean asking for more research, deleting a section, changing the angle, or abandoning the article altogether.

This matters because cheap output creates a strange kind of sunk cost. The moment AI gives you 2,000 polished words, you want to improve them rather than question why they exist.

Sunk-cost fallacy, if you will. Except AI can create the sunk cost every six minutes.

Or if you’re not making a pipeline and are using AI for a single article, break the work into stages. Start by brainstorming first. No drafting. Then, once you’re happy with the angle after the back-and-forth, move to the next stage. Ask it for an outline. Keep working and reworking it with AI until you’re happy, then move to the next stage. You could even ask it to steelman your arguments along the way.

The point is to make better decisions, not to watch the word count go up.

Otherwise, AI turns you into an editor before you've finished being a thinker.

## 

## 3. Spend the time AI saves on making better content

I think this is where Ahrefs differs from many companies using AI for content.

The obvious cost-saving play is to produce roughly the same article for less, then spend the savings on volume. More articles. More keywords. More pages for Google to crawl.

To be clear, we use AI to automate tedious work so we can save time too. It would be silly to pretend otherwise.

For example, the [Data Refresh Hub I built](https://ahrefs.com/blog/taught-agent-to-refresh-data-content/) saves at least a day of manual work each month by fetching, cleaning, and preparing updates for 12 datasets. Work that used to happen quarterly, irregularly, or not at all can now happen every month.

So yes, AI does help us publish and update more.

But volume is not the only possible return on efficiency.

Drafting and publishing were never the only constraints on our content. Often, the bigger constraint was everything we wanted to add around an article but couldn't justify or invest in.

For example, if we wanted to do simple data analysis (not a large scale data study), we might need the help of a data scientist. If we wanted to make a free tool, we needed a developer. A more interactive article needed design and engineering help. A large research project might simply be too manual for one content marketer.

AI lowers those barriers. A writer can now analyse a dataset, prototype a tool, build an interactive element, improve a post's UI, or automate part of a research project. Not perfectly, and not without specialists when the stakes demand them. But the threshold for trying is much lower.

Or how a content marketer can make a quiz, free tool, or data visualisation without waiting for a rare pocket of developer time. Like our [free LLMs.txt generator](https://ahrefs.com/free-llms-txt-generator/):

This is the distinction we care about. You can use AI to remove the work behind each article, or you can use it to attempt work you previously could not afford to do.

Don't just ask how many more articles AI lets you publish. Ask what you can now put inside an article that used to be impossible.

The capability to scale still needs restraint. We are not trying to turn every writer into a content factory. The goal is to expand what each writer can make without lowering the standard for what deserves to go live.

## 

## 4. Give every article an owner and a second human

AI may execute much of the process, but a specific person still has to own the result.

The person running the workflow should understand the topic well enough to validate its claims, correct misinformation, explain where the evidence came from, and decide whether they are happy attaching their name to it.

This is why Ryan doesn’t publish hundreds of articles overnight, even with his pipeline.

As the Director of Content Marketing, he’s also the editor of all our content. In short, he reads every word of every article that reaches the Ahrefs blog.

And as a thought leader in the industry, Ryan also has the ability to read a piece and be able to challenge the premise, question the evidence, identify generic sections, and ask whether the article actually fulfils its promise to the reader.

A human in the loop means very little if the human only rubber-stamps the output. They need the knowledge, authority, and willingness to say no.

And yes, even if a piece is AI generated or AI assisted, we still put enough man hours (the writer and the editor) to make sure it’s worthy of being published.

## Final thoughts

But as AI use increased, search performance tended to decline. The likely reason isn’t that Google punishes AI content. It’s that companies often use AI to skip the difficult work and publish more average content.

That brings us back to the heart of this article: AI is not the problem. Abdicating responsibility is.

AI makes execution cheap. That should give us more time for the judgement, evidence, experiences, and ideas that make an article worth reading.

So the important question is not how many or what kind of words AI wrote. It is whether a human understood, judged, verified, and stood behind what went live.

If nobody truly owns the result, it's slop.
