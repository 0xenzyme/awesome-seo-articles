---
title: "37 Proven Ways to Use AI in Marketing"
source: "ahrefs-blog"
content_type: "blog_article"
freshness_risk: "low"
slug: "how-to-use-ai-in-marketing"
url: "https://ahrefs.com/blog/how-to-use-ai-in-marketing/"
canonical: "https://ahrefs.com/blog/how-to-use-ai-in-marketing/"
author: "Ryan Law"
published: "2026-08-13T08:32:36+00:00"
updated: "2026-08-13T08:32:36+00:00"
categories:
  - "General Marketing"
freshness_reasons: []
fetched_at: "2026-09-08T09:16:27.326020+00:00"
status_code: 200
html_hash: "94aeced7300e8c0817bc52282d058033bbc666d2af0a03bd92cb0a9ae196668d"
clean_word_count: 8042
clean_char_count: 45085
---
# 37 Proven Ways to Use AI in Marketing

Generative AI tools like ChatGPT, Claude, and Letaido have improved enormously over the past year. Parts of marketing that never seemed automatable now are, and you don't have to be a software engineer or rocket scientist.

This is a collection of 37 straightforward, useful ways to use AI in your marketing, organized by discipline, from SEO through to international marketing. Every one of them comes from a marketer who has actually done it and shown their working, so that you can follow along and achieve the same yourself.

All of these workflows can be built with [Letaido](https://letaido.com), the AI marketing agent from Ahrefs. If you're an Ahrefs customer, you can try it free for a month.

Here's how to use AI in marketing, according to real marketers:

## SEO

A lot of SEO is tedious and fiddly at the same time: crawl exports, Search Console downloads, spreadsheets held together with `VLOOKUP`, complicated data analysis. That combination of repetitive and complicated is exactly where AI can help.

Worth saying plainly, though: anyone promising that AI can automate your SEO for $9 a month is selling you snake oil. No AI tool is a substitute for knowing what you're doing. Each one still depends on the judgment of the person using it.

### 1. Grade your page the way a Google quality rater would

Dan Hinckley of Go Fish Digital has [built an AI agent](https://www.linkedin.com/feed/update/urn:li:activity:7413967787699884032) that reviews a page the way one of Google's own quality raters would, and marks it against Google's published guidelines for them.

You give it a keyword and a page on your site. It reads Google's 168-page rater handbook first and turns it into a checklist, then opens a real Chrome window, searches for the keyword, looks at the results to work out what the searcher wants, and clicks through to your page. It scrolls the page, checks your About page and your footer, and writes up a report on where you meet the guidelines and where you fall short. It even records a video of everything it did.

The handbook is the closest thing we have to Google telling us what a good page looks like, but reading 168 pages of it and then judging your own work against it is not something most of us are ever going to do. This gets you that verdict in a few minutes, and you can run it on the page ranking above you too, so you find out whose page is genuinely better and in what way, rather than guessing.

### 2. Do an afternoon of keyword research in twenty minutes

Sam, our VP Marketing, had Letaido [build a keyword research tool](https://ahrefs.com/blog/agent-a-for-seo/) because he was done sorting keywords by hand. You give it a niche, like "coffee", and it comes back with a plan.

It expands the niche into seed keywords, pulls real volume from Keywords Explorer, then reads the SERP for every surviving candidate to judge intent, difficulty and who already ranks. For each keyword it counts the page types in the top 10, so you can see when a SERP is video-heavy or full of Reddit threads before you commission an article for it.

Everything comes back graded Go, Maybe or Skip, clustered into topics, with a competitor gap list and a hub-and-spoke map. On one run it graded 8,437 keywords into 17 clusters and marked 1,809 as Go.

### 3. Turn every site audit into a pull request a developer will actually action

It's prett easy to analyze the technical health of a website (especially if you use a tool like [Site Audit](https://ahrefs.com/site-audit)), but it is usually much harder to actually fix the problems you uncover, especially on big websites. To solve this, the Ahrefs team used generative AI to [connect our regular site audit straight to GitHub](https://ahrefs.com/blog/agent-a-for-seo/), on a job that runs every Sunday.

It pulls the most recent Site Audit, ranks the issues by severity, and opens a pull request scoped to the high-severity ones: indexability problems, broken pages, broken internal links. The PR lands with a checklist and the audit data attached, and it skips anything already sitting in an open PR.

It means that the developer who picks the audit up on Monday doesn't have to work out what's wrong or which URLs are affected: they can just review the changes and push to production if they make sense. Easy peasy.

### 4. Add AI-generated FAQs to old posts for a 32% traffic lift

Steven Macdonald [ran a controlled experiment](https://www.linkedin.com/feed/update/urn:li:activity:7167805610892247040) that you can replicate: he took 21 existing posts across 3 sites and used ChatGPT to identify questions a reader would still have after finishing each article, then wrote answers and appended them as an FAQ section.

Traffic across the updated posts rose 32% on average, about 16,000 extra visits and 3,500 additional keyword rankings. The best gained 180%. Every updated post gained something, while his control group declined 4% over the same window. No schema markup changes.

The control group is what makes this credible. Plenty of people report gains after an update without checking what would have happened anyway.

### 5. Build an internal linking engine in a week, knowing nothing about embeddings

This one is mine. I [built a tool](https://www.linkedin.com/feed/update/urn:li:activity:7312410595377446913) that suggests internal links for any article on this blog, and I started by asking ChatGPT's Deep Research to teach me the maths behind it, because I had never worked with any of it before.

It reads every article on the blog and turns each one into a long string of numbers that stands for what the article is about (known as vector embeddings). Give it a URL and it compares that page against all the others, then hands back the 20 closest matches. It looks for pages about the same subject rather than pages that happen to share a keyword, and those are usually different lists.

[Internal links matter for SEO](https://ahrefs.com/blog/internal-links-for-seo/) for three reasons. They help Google find your pages, since a page nothing links to is a page Google may never discover. They pass authority around your site, so linking to a page from several strong ones is how you decide which of your pages deserves to rank. And the words you link with tell Google what the target page is about. As John Mueller put it, internal linking is "one of the biggest things you can do on a website to guide Google and visitors to the pages that you think are important."

None of that is difficult. It is just that doing it properly means holding several hundred articles in your head at once, so it never happens on the day you publish. That is the part this hands off.

Automatically get internal link recommendations for any blog post

---

You don't have to write a script to do this. [Ahrefs' Site Audit](https://ahrefs.com/site-audit) has an **Internal link opportunities** report that crawls your site and tells you which pages should link to each other, based on the keywords each page already ranks for.

The useful part is that it doesn't stop at naming a target. It shows you the specific passage of text where the link belongs, so each suggestion is an edit rather than a research task. The same crawl also flags the internal-linking problems you can't see by eye: orphan pages nothing links to, internal links pointing at dead pages, and pages whose internal links are set to nofollow.

### 6. Let a script write the internal link into the page for you

John Iwuozor [wrote a Python script](https://www.linkedin.com/feed/update/urn:li:activity:7318544284943589376) that finds a good internal link and then writes it into the page for you.

Point it at an article and it reads your other pages to work out which one covers the closest subject. Then it goes through the article paragraph by paragraph looking for a phrase that would make sensible anchor text, picks the best one, and drops the link into the HTML itself.

Finding the right page to link to is only half of the job. The other half is opening the article, reading it back, choosing a sentence that can carry the link without sounding forced, and editing the page. That second half is why internal linking backlogs never shrink, and it is the half this takes off you.

### 7. Turn a Search Console export into a prioritized plan

Rudiger Dalchow [built a tool](https://www.linkedin.com/feed/update/urn:li:activity:7417887880481509376) that reads your Search Console exports and gives you back a plan of what to write next.

You hand it the two exports Search Console already gives you, one of queries and one of pages. It groups your pages into topics, works out what people want from each one, points out the pages competing with each other for the same search, and writes briefs you can pass straight to a writer.

Most reporting tells you what happened and leaves the thinking to you. This tells you what to do, and the problems it finds are the structural ones you cannot see in a list sorted by traffic: two of your own pages splitting one search between them, or a topic where you have published plenty of articles and nothing in the middle tying them together.

Get a prioritized list of SEO opportunities

---

If you'd rather not build this, [Site Explorer's Opportunities report](https://help.ahrefs.com/en/articles/9127446-where-can-i-quickly-find-opportunities-to-improve-my-website-s-seo) does a version of it for any site: keywords you rank 4-15 for and could push higher, featured snippets you're close to taking, pages that may be cannibalizing each other, plus link and technical fixes. Each one opens as a filtered report you can work through.

## AI search optimization

You want your business to come up when somebody asks ChatGPT about the thing you sell. Working out how to make that happen is harder than it ought to be. There is a great deal of complexity and a great deal of snake oil, and the advice you find ranges from jargon like fan-out queries and retrieval-augmented generation through to schema markup and llms.txt files, with very little agreement about which of it works.

Plenty of what does work, though, is straightforward, and most of it is rooted in SEO you already understand. These five are all concrete: they look at what the models actually do with a page and edit against that rather than against a theory. And since the work involved is mostly reading and comparing at a volume no person would sit through, AI is a useful thing to have in the toolkit for speeding it up.

### 8. See your page the way an LLM sees it

Aimee Jurenka [built a tool](https://www.linkedin.com/feed/update/urn:li:activity:7328912573616082944) that takes a URL, captures both the raw HTML and a rendered screenshot, then asks GPT how the page reads to a language model.

It returns a score plus specific feedback on three things: whether the content is clear enough to extract, whether it's worth citing, and whether anything important is trapped behind JavaScript. That last one catches something people miss, because a page that looks fine in a browser can be close to empty to a crawler that doesn't execute your scripts.

### 9. Map fan-out queries against the pages you already have

Chris Long [wrote a script](https://www.linkedin.com/feed/update/urn:li:activity:7424086346970959872) that checks whether your site answers the questions an AI assistant is really asking.

Ask an assistant something and it rarely searches for the thing you typed. It breaks your question into several narrower ones and goes looking for those instead. The script pulls out those narrower questions, scores each one against the pages you already have, and writes the results to a spreadsheet.

What you end up with is a list of the questions your site cannot answer. That is a more useful thing to hold than a keyword list, because an assistant assembles its answer from whoever covers the parts of a subject, and a page that covers four of the six questions behind a topic simply gets used less often than one that covers all six.

### 10. Rewrite pages against the queries that actually surfaced them

Bing reports the searches behind each citation, so he collects the questions that led an assistant to a given page. Then he reads the page against that list and rewrites wherever the page does not really answer what was asked.

Everywhere else in AI search you are guessing at what people typed. Here you have the actual questions that pulled your page into an answer, which turns a rewrite from a hunch into a comparison anybody can do. He publishes no numbers on what it did for him, so take the method rather than a result.

### 11. Build your page templates from what the models actually quote

She tracks 460 prompts across ChatGPT, Perplexity, Gemini and Google AI Mode, then connects that data to Claude and works through it. Which of her pages get quoted, on which platform, for which prompt. How each assistant actually structures a comparison when it answers one. Which parts of a page turn up in the answers and which get ignored. Then she builds the template around that, section by section, so every part of the page exists because the data says an assistant pulls from it.

Everybody is guessing at how to write for AI answers, and most of the advice is somebody's theory about structure. This replaces the theory with a record of what got quoted. Her own conclusion is worth keeping in mind though: different prompts favored different page types, so what comes out is a template for your market rather than one that works everywhere. And the pages that win are the ones with real verdicts in them, where you say which tool is better at what and admit where a competitor beats you, because a page that only flatters itself loses to G2.

### 12. Decide what to write next from what AI already cites

They start with the prompts that actually lead to a sale, the "what's the best X" questions covering everything they sell, and put those into a tracker. Then they look at which pages get cited most often across the answers. That list, ranked by how often each page comes up, is the scorecard. What they're hunting for in it is companies like theirs, because a competitor being cited is proof the spot is winnable rather than reserved for Wikipedia.

The last step is the one that makes it a priority list rather than a wish list. They check those same topics against ordinary Google demand, and anything cited heavily by AI and searched heavily on Google goes to the top. You end up writing for the questions that pay, in the order that they pay, which is a firmer footing than guessing at what a model might like.

## Content marketing

Ask AI to write you a blog post and you get slop. No personality, no original thought, no research, and usually missing the basics too, like internal links and images.

Treat content marketing as a multi-step process, though, which is how a skilled writer and a good editorial team already work, and it turns out AI is remarkably useful at a lot of those individual steps. Research, briefing, outlining, structural editing, fact-checking, internal linking, formatting. We have written a great deal about this on the Ahrefs blog, and the article you are reading now was itself vibe-written in Letaido.

### 13. Get a publishable draft down to about two hours

This one is mine. I [wrote up the whole process](https://ahrefs.com/blog/my-complete-ai-content-process-for-ahrefs/), and it gets an article to publication standard for this blog in about two hours, down from several days.

It works because I broke our editorial process into steps small enough to write down, then wrote them down: topic selection, briefing, outlining, structural editing, drafting, working in our products, line editing, internal links, metadata, and the WordPress formatting at the end. Those documents live in a ChatGPT project along with writing samples and excerpts from my writing courses, so every conversation starts with the standard already loaded. I fill in a short brief, and then I sit in the editor's chair, reading each stage and pushing back before it moves to the next one.

The number of steps is the whole trick. One prompt asking for a finished article gets you slop, because you have handed over ten decisions at once. Ten narrow prompts, each doing one job with somebody checking the output, gets you something publishable. It does need a competent marketer driving it, and I only use it on topics I know well enough to tell when it's wrong.

### 14. Learn to build web pages yourself in a few weeks

Kelsey Libert, who co-founded the agency Fractl, [spent a month learning Cursor](https://www.linkedin.com/feed/update/urn:li:activity:7326307796608557056) and then wrote and built 30 landing pages with it, one for each of her company's agent products.

Cursor is a code editor with AI built into it, so you describe what you want in plain language and it writes the code. She worked in one window alongside several models, using her own marketing judgment to decide what each page had to explain: what the product does, why it matters, how it works, and how different kinds of buyer would use it. She had no development background going in and learned it through evening sessions with her co-founder.

Landing pages are the classic marketing bottleneck. You know exactly what the page should say, and then you wait weeks for somebody else to build it, and the version that comes back is not quite what you described. Being able to write and ship the page yourself removes a handoff that costs most teams more time than the writing does. Her verdict after a month was that what she produced was already better than what she would have expected from a competent marketing team.

### 15. Run a real data study without hiring an engineer

Mateusz from our content team wanted to know whether a company's organic traffic tracks its share price, which meant getting three years of monthly traffic and monthly closing prices for every ticker on the Nasdaq. He had AI [write the code](https://ahrefs.com/blog/ai-content-marketing/) that pulled both, from the Ahrefs and Polygon APIs, stitched the datasets together, ran the correlations and drew the charts. He describes it in plain terms: pretty much all of the number crunching in that article was AI.

He is also straight about where it stopped being enough. The study got materially better when an actual data scientist, our colleague Xibeijia Guan, took over the analysis and decided how the numbers should be weighted. So the honest version of this is that AI got him from no data to a working dataset and a first pass at the maths, which is the part that usually kills a research project before it starts. Original research is about the best link-earning asset a content team has, and "nobody here can pull the data" is normally why it never happens.

### 16. Stop ChatGPT writing like ChatGPT

Myriam Jessier [shared the system prompt](https://www.linkedin.com/feed/update/urn:li:activity:7368900812057587712) she has used for months to strip the padding out of ChatGPT's replies, which she calls Absolute Mode.

It is one block of text you paste into your custom instructions. It tells the model to drop emoji, filler, hype and the little conversational warm-ups, to stop asking follow-up questions and offering to help further, to stop mirroring your tone back at you, and to end the reply the moment it has answered rather than tacking on a summary and a suggestion.

Most of the work in editing AI copy is deleting things: the throat-clearing at the top, the "great question," the recap you did not ask for, the eager offer at the end. Fixing that at the instruction level rather than sentence by sentence in every draft is the best ten seconds you can spend if you write with these tools. It also makes the output easier to judge, because once the padding is gone you can see whether there was an idea underneath it.

### 17. Talk through an idea and get a deck back

Wil Reynolds [records himself explaining a concept](https://www.linkedin.com/feed/update/urn:li:activity:7401663718683537409), transcribes it, then feeds the transcript to an LLM to draw out a story arc. NotebookLM and Gamma turn that structure into several deck variations.

What comes back isn't a finished deck, and he doesn't use it as one. It's a rough shape he then edits. But talking is a much faster way to get an idea out of your head than writing it, and the parts of slide-making that eat an afternoon, working out what order things go in and making them look presentable, are already done by the time he opens it.

### 18. Make a 1,000-article refresh backlog manageable

There are around a thousand articles on this blog, and keeping old ones current is some of the highest-return work we do. A post published three years ago can still be the best thing on the internet about its subject and still be quietly losing traffic, because a statistic in it is out of date or a competitor covered two things we missed. Updating it is cheaper than writing something new and usually works faster.

It matters for AI search too. We [looked at 17 million citations](https://ahrefs.com/blog/do-ai-assistants-prefer-to-cite-fresh-content/) across seven platforms and found that AI assistants cite noticeably fresher pages than Google's organic results do, with ChatGPT the keenest on recent content of the lot. So an article nobody has touched in three years is working against itself in two places at once.

The catch is that a thousand articles is more than anyone can hold in their head, and checking one properly takes an hour. Our [Update Pipeline](https://ahrefs.com/blog/agent-a-for-content-marketing/) does that checking. Give it a published URL and it looks for statistics that have gone stale and finds newer sources for them, notes where we describe our own product as it used to work, and compares the article against what currently ranks to see what it is missing.

Then it shows you the old version and the new one side by side, and you accept or reject each change one at a time. Nothing goes live unread. Our monthly "refresh 20 old posts" sprint went from something we talked about to something we do.

### 19. Dig out statistics your competitors haven't found

Give it a topic and it goes hunting through PDFs, Word documents and PowerPoint decks rather than ordinary web pages. About ten minutes later it comes back with roughly 30 statistics, each one with the year it was published, a link, and the file it came out of.

The statistics everybody quotes are the ones sitting on web pages, easy to find and already in your competitors' articles. The ones nobody quotes are sitting in the appendix of a PDF that nobody has opened. Going after the file formats instead of the pages is what puts a number in your article that the other five results on that search do not have, and an original number is one of the few things left that still earns a link.

### 20. Query a pile of expert quotes instead of sorting them

Putting a callout out for expert quotes is one of the better ways to make an article worth reading, and anyone who has done it knows the catch. You post the request, and a few days later there are dozens of replies sitting in your inbox, most of them unusable, and no way to see across them without opening every one.

Mateusz Makosiewicz, who writes our data studies, [handles that pile with NotebookLM](https://ahrefs.com/blog/ai-content-marketing/). He saves the email notifications as PDFs, uploads the lot, and waits a minute while it reads them. From there he can ask questions of the whole set at once, in plain language, like showing him the most unconventional tips from business owners and naming which file each one came from. Once he has the quotes he wants he moves to a different tool to write with, because NotebookLM is good at finding things in your documents and less good at prose.

Two things make this work better than pasting everything into ChatGPT. It can hold far more text at once than most chat tools will accept, which matters when you have a hundred replies. And it answers only from the documents you gave it, with a reference back to the source, so a quote you get out of it is one somebody actually said.

### 21. Turn every webinar into three pieces of content

The first takes a webinar recording and produces three blog outlines, a guide to the best clips and briefs for social, filed in Notion. Approve an outline and the second grows it into a draft of about 1,200 words with sources and quotes. The third listens to sales calls and files every pain point and objection into a tagged database. The fourth does the same with longer customer calls, pulling out quotes and tagging them by the kind of buyer who said them.

Every company records these calls and almost nobody ever listens to them again, so the most honest account of what customers want sits in a folder nobody opens. The database of complaints is what makes this more than a time-saver. Most content teams keep no record of what customers actually grumble about, so every quarter somebody rebuilds that list from memory and calls it a content plan.

## Marketing analytics

Reporting is the most automatable job in marketing. It is also nobody's favorite part of the month, which is a decent sign that a machine should be doing it.

AI can do most of it for you: pull the exports, join them up, build the tables. And when I am the one doing that by hand, small mistakes creep in, a column mismatched or last month's number copied into this month's row, so having it done the same way every time is worth something beyond the hours it saves. What the tool still cannot do is tell you what any of it means. That part stays with you.

### 22. Turn a full day of monthly reporting into a scheduled job

Letaido [builds our monthly blog performance report](https://ahrefs.com/blog/agent-a-for-content-marketing/) on the 2nd of each month, pulling from Google Search Console and Ahrefs Web Analytics. KPI tiles, a 12-month trend chart, subfolder splits, winners-and-losers tables, daily anomaly callouts, paginated post lists.

It also drafts 6-10 candidate analysis bullets for whoever writes the commentary, so they're editing rather than starting from a blank page.

It used to take most of a day. It now runs automatically!

### 23. Check whether your content is actually on-topic

We [ran a semantic audit](https://ahrefs.com/blog/agent-a-for-content-marketing/) of this blog to find out how many of our articles cover our core topics—SEO, link building, content marketing—and how many cover topics Ahrefs isn't an authority on.

It starts the same way as the internal linking tool: turn every article into a long string of numbers called vector embeddings. Average all of those together and you get one string of numbers for the blog as a whole, which is as close as you can get to a mathematical answer to "what is this site about?" Then measure how far each article sits from that center. Close in, and it's squarely on topic. A long way out, and it's an article about something else that happens to live on your blog. We sorted every page into four groups on that basis, from core to far, and attached each one's traffic, links and rankings so we could see how the groups compare.

The pattern was clear enough to change what we commission. Core pages get about twice the organic traffic of the far ones. Every blog accumulates articles that seemed like a good idea at the time and sit slightly outside what the site is known for, and this puts a number on what that drift costs you.

### 24. Pipe crawl, analytics and Search Console data into one audit

Screaming Frog, Google Analytics and Search Console all feed into Claude through Zapier. Claude reads the three together and looks for pages losing traffic, pages answering a different question from the one people are asking, and pages that no longer fit the rest of the site. The work is in writing the instructions for it and rewriting them until the output is worth reading.

Many content problems are invisible in any single one of those reports. A page can look healthy in analytics while quietly losing impressions, or rank perfectly well for a search whose meaning has drifted away from what the page says. You only catch that when the three datasets sit side by side, and this combination of data sources is something AI is excellent at.

You can build this in [Letaido](https://letaido.com) without the plumbing. It has Google Analytics and Search Console connectors built in, so there's no Zapier step between the data and the analysis, and it can crawl your site itself, which means you don't need Screaming Frog either. Or you can point it at [Site Audit](https://ahrefs.com/site-audit) and use a crawl you already have.

## Social media and community

Social media is hard for two reasons: people mention your brand in more places than you can keep up with, and there is always more you could be posting than you have time to write.

AI is good at both of those jobs, as long as you use it to sort and to draft rather than to publish. Getting a reply wrong on social is more expensive than getting a report wrong. A bad report wastes your morning, and an ill-considered comment dropped into a subreddit by a robot gets you banned, screenshotted, and shamed. So let it find the mentions worth answering and give you a first draft to work from, then have somebody who knows the room decide what actually goes out.

### 25. Find the Reddit conversations worth joining

The team at lemlist [spent three months trying to work out](https://www.linkedin.com/feed/update/urn:li:activity:7373324721553154048) whether Reddit was worth their time, and they kept a record of exactly what they did. Over that period they started 12 threads of their own across 6 subreddits, joined 28 discussions that were already running, and replied to 13 places where somebody had brought up their brand unprompted. Traffic from Reddit went up 22%, and the people arriving from it signed up at a rate 20% higher than their average visitor. The threads themselves also started ranking in Google and turning up as sources in ChatGPT and Perplexity answers.

The part AI handled was the looking. Reddit is enormous, and the conversations where you would have something genuinely useful to add are scattered across it, buried under a much larger pile where you would be an intrusion. They used AI to read through that pile and surface the handful of threads that were actually relevant, then to give them a starting point for a reply.

Everything after that was a person. Somebody from the team read the thread, worked out whether they had anything worth saying, wrote it in their own words and posted it under their own account. That's not a compromise for the sake of Reddit's rules, though those rules are clear enough that you should read them. It's that the whole value of being in a subreddit is that people can tell you are a person who knows something. An automated reply fails at the only thing it was there to do.

### 26. Learn how your customers actually describe their problem

The version she recommends building yourself uses a platform's own free API to collect the discussions that mention your brand or your subject, then has a model read through them and pull out what's actually being said: the recurring complaints, the questions that come up again and again, the comparisons people make between you and a competitor, and the exact words they use for all of it. She runs a free workshop taking people through the build step by step.

What comes back is worth more than a sentiment score. It's the language your customers use when they don't know you're listening, which is usually nothing like the language on your website. That's the raw material for a landing page that sounds like it was written by somebody who has met them, and for knowing which objection to answer first.

### 27. Get five social drafts in your own voice for every article you publish

I had [Letaido](https://letaido.com) build me a social post generator, because writing the LinkedIn post is the bit of publishing an article I put off longest. It checks the blog's sitemap for anything new under my byline, reads the article, and writes five drafts of a post about it.

The five are deliberately different from each other: one leads with the most surprising thing in the article, one opens with a story, one asks the question the article answers, one lists the takeaways, and one argues against something most people believe. That's there because I don't know which angle I want until I see a few, and picking between options is much easier than starting from nothing.

The part that made it usable rather than a novelty is that it writes in my voice, not LinkedIn's. I marked up my own best-performing posts inside the app, and those get handed to the model as the style to copy, weighted above everything else. Once I've picked a draft and edited it, the app pushes it to my scheduling queue via [Ahrefs' Social Media Manager.](https://app.ahrefs.com/social-media) So the job goes from writing a post from scratch to choosing between five and fixing the one I like.

## PR and outreach

Outreach lives or dies on timing and relevance. Being the third person to pitch a journalist a story is worth nothing, so the job involves watching thousands of stories a day across feeds nobody has time to read, then writing to each contact as though you'd read their work. Both of those are jobs a machine can take on.

What it can't take on is the judgment about whether your pitch is welcome in the first place. AI-generated outreach at scale is already why a lot of journalists have stopped reading their inboxes, and personalizing faster only helps if the thing you send is worth receiving. So the four below all stop at the same place: they do the watching and the first draft, and leave you to decide what actually gets sent.

### 28. Monitor thousands of news stories a day for PR opportunities

Mark Williams-Cook [wrote a Python script](https://www.linkedin.com/feed/update/urn:li:activity:7486351996749488130) that runs a local LLM (Ollama with Gemma) across thousands of daily news stories pulled from RSS feeds, matching each headline and description against client interest profiles. Qualified leads go to Slack for the digital PR team.

Running the model locally is what makes the volume viable, because there's no per-call API bill to worry about when you're screening thousands of stories a day.

### 29. Write follow-up emails from call transcripts in five minutes

Andy Chadwick [feeds sales call transcripts](https://www.linkedin.com/feed/update/urn:li:activity:7341386148142809089) into a ChatGPT workflow trained on his own tone, his product details and the objections he hears most often. It drafts a follow-up reflecting that specific prospect's stated problems, he edits, he sends.

Composition went from 45 minutes to 5. He reports a 90% close rate on the high-ticket follow-ups he uses it for, on £5,000 to £10,000 services.

### 30. Run a cold outreach campaign that sounds like you wrote it

Ahrefs' own Sam Oh paid an agency to do outreach for him. They sent 100 emails and got three replies, two of which asked to be taken off the list. So he [built his own outreach campaign](https://www.youtube.com/watch?v=rGdR1KC6O2s) instead, and filmed it.

It runs as a team of agents with a manager. The manager starts by interviewing him about what he's after: what a good prospect looks like, what rules one out, how the emails should read. Then one agent goes looking for prospects and pulls the Ahrefs data on each one, a second checks whether their traffic growth is real rather than a blip, and a third writes the emails and leaves them in his Gmail drafts for him to approve. He runs all of it from Slack.

He set it going as he left for the airport, and by the time he reached his gate there were 74 drafts waiting. Of the 54 he sent, 11 came back and seven turned into booked meetings, against a goal of five. Cold outreach is mostly a research job rather than a writing one, since the reason most of it gets ignored is that nobody did the homework on who they were writing to. That's the part this does for you, and it's the reason the emails read like somebody had.

Sam built this over several days with a stack of agent instruction files, and says so in the video: [Letaido](https://letaido.com) does the same job natively, since it already has the Ahrefs data, the traffic checks and the connection to an outreach tool.

### 31. Turn a data study into a press release automatically

We [built a Press Release Generator](https://ahrefs.com/blog/agent-a-hackathon/) that takes a blog post URL or a note about a product feature and returns a formatted press release. The plan is to point it at our data studies, so that every new study comes with a release already drafted rather than waiting for somebody to find an afternoon.

Original research is how we get picked up by the press. Our studies have been cited by outlets including The Atlantic, CNN and the BBC, and that only happens if somebody actually pitches them, promptly, while the finding is still news. The writing was never the hard part of that, but it was the step where the whole thing stalled, so having a first draft waiting is what makes the promotion happen consistently rather than when there's time. The output still needs a person to read it before it goes anywhere.

## Product marketing

Launching one product means writing a landing page, an email, a video script, a sales deck and a one-pager, and they all have to say the same thing. They usually don't. Different people write them in different weeks, so the landing page promises something nobody agreed to and the email is aimed at a different customer than the deck. Reading all five side by side to catch that is a job everybody means to do and nobody does the week of a launch.

Writing the first versions is the easy part, and the part to check hardest. These three come from our product marketing team, and the best thing in them is the step that reads everything at the end and tells you where two documents disagree.

### 32. Generate an entire launch package from one product brief

Andrei, who leads product marketing at Ahrefs, [built a GTM Generator](https://ahrefs.com/blog/agent-a-for-product-marketing/) that turns one rough product brief into six things: a tidied-up brief, a landing page, a 90-second video script, a promotional email, a flyer that's nearly ready to print, and a final check.

That last one is the reason the whole thing holds together. It reads the five documents side by side and writes you a list of everywhere they disagree with each other, down to a landing page promising something is "10x faster" when nobody claimed that in the brief.

Once Andrei has edited the documents, he can put his edited versions back in and have the tool compare them against what it originally wrote.

### 33. Reverse-engineer a competitor's paid campaigns into your own ad copy

It pulls the keywords that competitor pays for and the pages they send that traffic to, then reads those pages so it can see the actual promises in their ad copy. It groups the keywords into themes, points out the ones you are not bidding on yourself, and writes Google Search ads against those gaps, three headlines and two descriptions per version, inside the character limits.

Paid search is the one place a competitor cannot hide what they believe is worth money. Every keyword on that list is one somebody chose to pay for, tested, and kept paying for, which makes it a shortlist that has already been validated with a budget that was not yours. Getting handed it, along with the ads to point at the gaps, is a fair afternoon's work for one domain name.

### 34. Set up an entire webinar from a title and a date

Constance runs Ahrefs' webinars, so she had Letaido [build a webinar automation app](https://ahrefs.com/blog/agent-a-for-product-marketing/). She types in a title, a date and who's speaking, and it sets the whole thing up for her.

It works backwards from the date of the webinar to decide when each job needs doing, then creates the tasks in Linear: setting up the Zoom event and the landing pages, writing the promotional copy, booking the paid promotion, building the slides and the script, and reporting on how it went afterwards. That's twenty jobs in total, written from templates she can change for any given webinar.

It also hands them over in stages rather than all at once, so she only ever sees the jobs she can actually do something about today. Running a webinar isn't difficult, it's just twenty small things that have to happen in the right order, and forgetting one of them is what costs you the audience.

## International marketing

International marketing multiplies. Every article you publish becomes seven articles, each with its own keyword research, its own internal links to remap, its own charts to redraw, its own hreflang tags to keep straight. Most of that added work is mechanical rather than skilled, which is why it's a good fit for automation and why it usually just doesn't get done.

The part worth being careful about is that translation and localization aren't the same thing. A model will happily give you fluent Spanish that reads as though it were written for the wrong country, and you won't notice if you don't speak it.

### 35. Translate a blog post without breaking the links inside it

Erik and Taka from Ahrefs' international marketing team built a [translation pipeline](https://ahrefs.com/blog/agent-a-for-international-marketing/) that handles seven languages, each with its own tone guide, glossary and translation rules: French, Spanish, Japanese, German, Italian, Korean and Traditional Chinese.

It also fixes the links, which is the bit that usually gets forgotten. Translate an article and the links inside it still point at the English versions of your other articles, so a reader in Japan follows one and lands back in English. This checks each link, and if there's a Japanese version of that article it swaps it in. If there isn't one, it tells you which links it left alone and why.

And before any of that it does keyword research in the country you're translating for, so the article goes after words people there actually search for rather than a word-for-word rendering of the English one.

### 36. Localize the charts and diagrams inside your posts

A translated article with English screenshots is only half translated, and an Ahrefs post can carry a dozen charts and flow diagrams. So the international team [built a translator just for visuals](https://ahrefs.com/blog/agent-a-for-international-marketing/): upload a PNG, JPG or PDF, pick a language and region, get the localized image back.

Two things happen. First one model looks at the image and writes down what needs changing, in plain language. Then a second one redraws the image with those changes made. You pick a region as well as a language, so Spanish for Mexico comes back different from Spanish for Spain, and the prices, example web addresses and names change to suit.

If it gets a word wrong you can tell it, and it redraws that image with your wording instead. In the screenshot below somebody is correcting one Japanese term to the phrase the team actually uses.

### 37. Run live subtitles at a conference for the price of a laptop

Professional simultaneous interpreters cost upwards of $2,000 a day and don't know your product. Taka runs a [Live Interpreter](https://ahrefs.com/blog/agent-a-for-international-marketing/) on a laptop next to the stage instead, generating English and Japanese subtitles from the microphone feed as somebody speaks.

Live speech arrives in half-finished chunks, so it waits and only ever puts a complete sentence on screen. It also reads from a glossary of our product names first, which means "AI Overviews" always comes out as the Japanese term we've agreed on rather than something close to it. The team uses Gemini 3 Flash, which is fast enough to keep up with somebody talking.

## Final thoughts

Plenty of people will tell you they have fired their marketing team and handed the whole thing to AI. In reality, AI is a tool, and it is only as good as the person holding it.

Every process on this list was designed by somebody who knows marketing inside out. They know the workflows and desired outcomes. They have taste and judgment. They could get a good result *without* generative AI, and that is precisely why they get a better one with it. The tool multiplies what you already bring; if you bring nothing, it multiplies nothing.

So stay skeptical. AI is not a magic box that solves your problems while you watch. But in hands like yours, it will make a lot of your work faster, quite a bit of it better, and some of it genuinely more fun than it used to be.

Got a workflow of your own that belongs here? Message me on [LinkedIn](https://www.linkedin.com/in/thinking_slow/) and I'll take a look.
