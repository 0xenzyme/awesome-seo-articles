---
title: "ChatGPT for SEO: 9 Best Use Cases (And 4 Suboptimal Ones)"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "chatgpt-for-seo"
url: "https://ahrefs.com/blog/chatgpt-for-seo/"
canonical: "https://ahrefs.com/blog/chatgpt-for-seo/"
author: "Si Quan Ong"
published: "2023-02-22T06:18:21+00:00"
updated: "2026-01-06T15:24:54+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "ai_search_topic"
  - "time_sensitive_title"
fetched_at: "2026-06-12T11:21:19+00:00"
status_code: 200
html_hash: "7d1b86c78445e7d2c2a65b6fa9c575e2f966c6bf33e22cfb4ec1690f249536dd"
clean_word_count: 3149
clean_char_count: 19210
---
# ChatGPT for SEO: 9 Best Use Cases (And 4 Suboptimal Ones)

I’ll have to admit: ChatGPT iscool. I don’t think we expected AI to come this far so soon.

But it doesn’t mean every free “ChatGPT prompt” ebook you see on Gumroad is the future. Many of the use cases are simply engagement bait.

So in this post, we’ll look at the actual best use cases of ChatGPT for SEO. I’ll also cover cases where you shouldn’t use ChatGPT.

Prefer video?

Here’s Sam Oh on the best and worst cases of ChatGPT for SEO:

Further reading

[10 ChatGPT SEO Tools That Help You Rank Higher](https://ahrefs.com/blog/chatgpt-seo-tools/)

## Best use cases

Here are some of our favorite ChatGPT use cases for SEO that we have found at Ahrefs.

### 1. Construct regex

A regular expression (regex) is a sequence of characters used to find patterns within text. For example, the pattern `/b[aeiou]t/` will find words like “bat, bet, bit, bot, but” on a page.

If we want to find keywords phrased as a question in [Google Search Console (GSC)](https://search.google.com/search-console/about), we can ask ChatGPT:

> What is the regular expression to show matches that contain any of the following words in it: how, what, who, when, where, why, do? These words should be the first word in the match.

And here’s ChatGPT’s answer:

![Prompt for ChatGPT to create a regular expression](https://ahrefs.com/blog/wp-content/uploads/2023/02/image1-12.png)

With this answer, we can go to GSC and paste the custom regex with the **Query** filter:

Then, we’ll set the **Positions** filter to >10 and sort the list in ascending order.

We now have a list of informational keywords we can work on to bring those pages from page two to page one of Google.

Sidenote.

[H/T to Lily Ray](https://twitter.com/lilyraynyc/status/1605238442337632257) for sharing this use case.

Further reading

- [How to Rank Higher on Google (10 Steps)](https://ahrefs.com/blog/how-to-rank-higher-on-google/)

### 2. Create automations

ChatGPT can write code too.

> ChatGPT can code an entire simple app for you.
>
> — Csaba Kissi (@csaba\_kissi) [February 5, 2023](https://twitter.com/csaba_kissi/status/1622238302442033153?ref_src=twsrc%5Etfw)

If you’re tech-savvy, you’ll already see plenty of ways to use this to improve your processes. Here’s a quick example.

Let’s say you’re working on a link building [campaign](https://ahrefs.com/blog/fast-link-building/). You’ve collected the URL, domain, and first and last names of the authors you want to contact. Now you want to find their emails.

The inefficient method is to go through them one by one in a web app or Chrome Extension. The better way would be to code something in [App Scripts](https://www.google.com/script/start/) to connect to an email-finding API, like [Hunter.io](https://hunter.io/).

We can use ChatGPT to write the code. Here’s a sample prompt:

> Using Hunter.io’s “Email Finder” API, write a function called findEmail in Google Appscripts to return a person’s email address. If no email exists, then return “THEY DON’T WANT TO BE CONTACTED.” I will provide the first name, last name, and domain name. BTW, my API key is [MUTED]. Go!

Then, we’ll take the generated code and open App Scripts:

- First, paste in the code, save the file, and go back to the Google Sheets.
- In the email column, type in “findEmail,” open parentheses, click the first name, last name, and the domain.
- Then hit enter.
- As for the rest of the list, just drag the formula down.

This is merely the tip of the iceberg. There are plenty more you can do—for example, SEOs are combining it with Python to do tons of cool stuff:

> Playing with the ChatGPT API. Wrote a python script that grabs the top ranking pages for a query, grabs related search terms, feeds all that content to chatGPT and has it create content ideas. Just a proof of concept. cooler stuff coming soon. [#ChatGPT](https://twitter.com/hashtag/ChatGPT?src=hash&ref_src=twsrc%5Etfw) [#seo](https://twitter.com/hashtag/seo?src=hash&ref_src=twsrc%5Etfw) [#Python](https://twitter.com/hashtag/Python?src=hash&ref_src=twsrc%5Etfw) [pic.twitter.com/ZEOIXczUZt](https://t.co/ZEOIXczUZt)
>
> — Ryan Jones (@RyanJones) [February 2, 2023](https://twitter.com/RyanJones/status/1621279103977492482?ref_src=twsrc%5Etfw)

Further reading

- [Hey ChatGPT, Automate These Tasks Using Python](https://medium.com/geekculture/hey-chatgpt-solve-these-coding-tasks-using-python-b2e7482f2c18)

### 3. Whip up quick snippets of code

ChatGPT’s ability to write code means you can use it to quickly create snippets of code, such as [schema markup](https://ahrefs.com/blog/schema-markup/):

And [hreflang](https://ahrefs.com/blog/hreflang-tags/) snippets:

More examples in the article below.

Further reading

- [5 Powerful ChatGPT Prompts for Technical SEO](https://hallanalysis.com/5-powerful-chatgpt-prompts-for-technical-seo/)

### 4. Write click-worthy titles

Writing the perfect headline can take longer than you think. So we can use ChatGPT to create click-worthy titles in seconds—and it outperforms human-written titles:

https://twitter.com/GaelBreton/status/1620330632516898816

You can use ChatGPT to write click-worthy titles for your blog posts, podcasts, or YouTube videos. For best results, give it a working title.

Here’s a sample prompt:

> Write 10 click-worthy titles for my blog post on the best marketing books. My working title is Best Marketing Books.

You can also ask ChatGPT to front-load keywords or make your titles sound like someone else. So let’s ask ChatGPT to make the above titles sound like [Tim Ferriss](https://twitter.com/tferriss):

Pretty cool.

### 5. Create quick outlines

If you like any of the titles ChatGPT suggested, you can ask it to create an outline. I’m sure many SEOs are salivating at the thought of using ChatGPT to create content briefs (or even blog posts—more on that later). But my point is this: think of ChatGPT as your [creative sparring partner](https://www.animalz.co/blog/the-content-cyborg/).

I like #7 from the above example, so let’s ask ChatGPT to expand on it:

It’s a decent outline, but there’s a problem: It’s repetitive. For example, I won’t organize the outline like this. Instead, I’ll probably make each book the H2, then go into the details (summary of the book, some key takeaways, how I used the takeaway to improve my marketing and career, etc.).

The suggested intro seems boring too—I’ll probably start with the story of my transformation rather than sound so academic and prescriptive.

By the way, I’m interested in ChatGPT’s book recommendations, so I’ll ask it to expand on II:

Again, decent suggestions that you’ll find on many marketing booklists. I agree with the recommendations, but my honest opinion is that everyone probably already knows these books. Of course, you don’t want to lie if these books *really* transformed your career. But if there are lesser-known ones, you’ll do better highlighting them.

Otherwise, you’re just like everyone else, and there’s no point in reading your content.

In summary, use ChatGPT as your ideation partner, but don’t rely on its suggested content 100%.

### 6. Suggest seed keywords

We don’t recommend using ChatGPT to do keyword research (more on that later), but that’s not to say it isn’t a good way to gather potential [seed keywords](https://ahrefs.com/blog/seed-keywords/).

For example, we can ask ChatGPT to give us “technical terms related to coffee”:

We can then use these terms as “seed keywords” to find more keyword ideas in Ahrefs’ [Keywords Explorer](https://ahrefs.com/keywords-explorer):

Sidenote.

[H/T to Gael Breton and Mark Webster](https://www.authorityhacker.com/chatgpt-prompts/) from AuthorityHacker for this tip.

### 7. Generate short-form content

No matter how much you love writing, some types of content are just boring to create. Examples include meta descriptions, [product descriptions](https://ahrefs.com/blog/product-descriptions-creation/), ad copy variations, and more.

For example, we have almost 300 pages on our site that don’t have [meta descriptions](https://ahrefs.com/blog/meta-description/).

So rather than bother someone on our marketing team to spend their day crafting meta descriptions, we can ask ChatGPT to do it for us. Let’s ask it to write a meta description for our page on “how to use [Keywords Explorer](https://ahrefs.com/keywords-explorer)”:

Pretty good!

### 8. Proofreading

If you work with [freelance writers](https://ahrefs.com/blog/hiring-freelance-writers/) regularly, you can use ChatGPT to proofread their work.

For example, in 2022, [we tested the quality](https://www.youtube.com/watch?v=LCmcW2kpLjg&t=2s) of a few freelance writers based on their rates.

So let’s say we like the general direction of the writer’s work, except that their language is lacking. We can take parts of the post and ask ChatGPT to proofread it. And voila, in a few seconds, ChatGPT has improved it.

### 9. Rewrite sentences

Novelist Vladimir Nabokov once said:

> I have rewritten—often several times—every word I have ever published. My pencils outlast their erasers.

We don’t use pencils and erasers today, but the sentiment remains the same—the act of creating content is simply the magic of rewriting sentences over and over again.

Again, we can use ChatGPT as our creative sparring partner. Ask it to rewrite our sentences in various ways so we can see different perspectives on how to communicate ideas:

https://twitter.com/dickiebush/status/1619681274368610304

For example, I’m a huge fan of [Kurt Vonnegut](https://en.wikipedia.org/wiki/Kurt_Vonnegut), so let’s ask ChatGPT to rewrite my intro like the American writer:

True to the style of fiction writing, the language is more flowery and ChatGPT uses more adjectives. Interesting, but not the tone of Ahrefs. Let’s try again and, this time ‘round, we’ll ask ChatGPT to be more persuasive:

Now my content feels more rah-rah. It’s pretty cool to know that your writing is just one of many options you can choose from.

Finally, let’s ask ChatGPT to rewrite it in a sarcastic tone:

Maybe I’m secretly British, but I like this. I don’t think I’ll use it. But, again, it helps spark new ideas.

## Less-than-ideal use cases

Although ChatGPT has a number of good use cases for SEO, it also has a few less-than-ideal use cases (at least for now).

Here are some examples:

### 10. Content creation

Many SEOs are excited over the fact that ChatGPT can create content. Some SEOs believe they can now unleash a deluge of AI content and hope to rank high on Google.

But there are a few problems with this:

**First,** when you ask ChatGPT to write you a full article, the content is almost always going to come out as boilerplate content. For example, when we asked ChatGPT to create a 1,500-word blog post on the same topic, it generates this:

It’s no surprise—after all, that’s how it was trained; it basically summarizes the internet.

There’s nothing wrong with this. Many freelance writers do the same too—they create content by “summarizing” the top-ranking pages. So ChatGPT can now do the same at a fraction of the speed and cost.

But it doesn’t mean it’s a good thing. Sure, you can now create hundreds of copycat articles in a few hours, but what’s the business value behind doing this?

SEO is ultimately a [marketing channel](https://ahrefs.com/blog/marketing-channels/)—it exists to drive customers to your business. So even if your AI content ranks high on Google but your target audience never consumes it and never takes the next steps to convert, is there a point?

> Seeing lots of threads on “how to use AI for writing!“
>
> Haven’t seen any AI-written writing worth reading.
>
> — Nat Eliason (@nateliason) [January 25, 2023](https://twitter.com/nateliason/status/1618240676889776128?ref_src=twsrc%5Etfw)

https://twitter.com/GaelBreton/status/1614226477809274882

**Second,** ChatGPT lacks expertise, experience, and originality. If you look at the generated article, it’s clear that it’s generic and helps no one. With Google now focusing on [E-E-A-T](https://www.searchenginejournal.com/google-e-e-a-t-how-to-demonstrate-first-hand-experience/474446/), you’ll have to make sure your content demonstrates first-hand experience and expertise—both ChatGPT can’t do (yet).

Your content also needs to stand out. Everyone’s using ChatGPT to create the same ol’ boring content. Why should anyone choose to read, link, or share your content over the rest? Ultimately, you still need human intervention and originality—you need to inject [“information gain”](https://www.animalz.co/blog/information-gain/):

- **Personal perspectives and experiences** – We did this for our [post on email outreach](https://ahrefs.com/blog/email-outreach).
- **Unique data, e.g., surveys and polls** – We did this for our [post on SEO pricing](https://ahrefs.com/blog/seo-pricing/).
- **Subject-matter expert quotes** – We interviewed experts for our [post on international link building](https://ahrefs.com/blog/international-link-building/).

 And more.

**Third,** the danger of getting ChatGPT to create content is that you may end up plagiarizing. Major sites like CNET and Bankrate were [experimenting with publishing AI content](https://futurism.com/the-byte/cnet-publishing-articles-by-ai) as-is and were [caught plagiarizing](https://futurism.com/cnet-ai-plagiarism):

**Fourth,** ChatGPT is perfectly capable of making up information. There are plenty of examples where ChatGPT:

- [Fooled scientists with fake abstracts](https://www.nature.com/articles/d41586-023-00056-7).
- [Spread pandemic-related untruths](https://techcrunch.com/2023/02/08/ai-is-eating-itself-bings-ai-quotes-covid-disinfo-sourced-from-chatgpt/).
- [Shared conspiracy theories](https://futurism.com/the-byte/chatgpt-minsinformation-newsguard).
- [Made up fake academic papers](https://twitter.com/dsmerdon/status/1618816703923912704) ([more here](https://twitter.com/search?q=none%20of%20these%20papers%20exist&src=typed_query&f=top)).
- [Invented fake citations](https://scholarlykitchen.sspnet.org/2023/01/26/guest-post-the-efficacy-of-chatgpt-is-it-time-for-the-librarians-to-go-home/).
- [Created new information with perfect confidence](https://twitter.com/greglescoe/status/1619909283482841088).
- [Generated fake quotes, fake articles, and fake positions](https://noahpinion.substack.com/p/why-does-chatgpt-constantly-lie).

Finally, ChatGPT is more than often providing out-of-date information. The limits of its current training are only up till 2021, which means it (theoretically) can’t know about the latest happenings:

Sidenote.

It may not be true, as it’s [proven](https://www.reddit.com/r/OpenAI/comments/10arqg2/chat_gpt_is_learning_about_things_after_2021/) that ChatGPT *is* learning things after 2021.

### 11. Keyword research

A popular use case among SEOs is to ask ChatGPT for [long-tail queries](https://ahrefs.com/blog/long-tail-keywords/).

For example, here are 10 long-tail keywords for the “golf” niche suggested by ChatGPT:

It looks decent at first glance, but plugging them into Ahrefs’ [Keywords Explorer](https://ahrefs.com/keywords-explorer) shows us that none of them have any search demand:

Even Google Trends shows no data:

That is not to say you can’t target them. Plenty of SEOs believe in targeting “[zero-volume keywords](https://ahrefs.com/blog/zero-volume-keywords/).” However, bear in mind that the chance of a low- or zero-volume keyword getting significantly more searches than estimated is extremely low.

So if you want [quality data](https://ahrefs.com/big-data), your best bet is still to use a professional keyword tool like [Keywords Explorer](https://ahrefs.com/keywords-explorer). If you’re looking for a few random ideas, then ChatGPT can fit that use case.

Another popular keyword research prompt is to ask ChatGPT for “easy to rank for” queries. In our opinion, that is a bad prompt because [keyword difficulty](https://ahrefs.com/blog/keyword-difficulty/) involves [analyzing the SERPs](https://ahrefs.com/blog/serp-analysis/), the competition, the quantity and quality of backlinks, and the actual content of the top-ranking pages.

Unfortunately, ChatGPT can neither browse the SERPs nor the web:

So it cannot accurately analyze ranking difficulty based on its limitations.

### 12. Search intent classification

To identify [search intent](https://ahrefs.com/blog/search-intent/) accurately, you need to *actually* look at the SERPs themselves—you’ll have to analyze the top-ranking pages and their content, look at [SERP features](https://ahrefs.com/seo/glossary/serp-features), and more—to come to a reasonable conclusion on intent class.

The first problem is this: As seen above, ChatGPT can’t browse SERPs.

The second issue: SEOs who do this analysis don’t always agree with each other. For example, in 2022, three of our marketers ([Sam Oh](https://ahrefs.com/blog/author/sam-oh/), [Patrick Stox](https://ahrefs.com/blog/author/patrick-stox/), and [Joshua Hardwick](https://ahrefs.com/blog/author/joshua-hardwick/page/2/)) [picked five random keywords](https://www.youtube.com/watch?v=KGm17ERgqTw&t=673s) and attempted to assign an “intent bucket” to the keywords.

All of them had slightly different opinions on each keyword.

The four search intent classifications are Informational [I], Navigational [N], Commercial investigation [C], and Transactional [T].

So we can’t rely on ChatGPT to provide “intent analysis” as an authoritative source when even experienced SEOs disagree with each other.

Finally, since ChatGPT’s training data only goes up till 2021, it can’t (theoretically) update itself on changes in search intent beyond that period. For example, there have been significant changes on the SERPs for “bird flu”—with intent fracturing to feature more of the latest news:

NOTE

When we put ChatGPT to the same test, it did OK (3 out of 5 for the same keywords):

Since ChatGPT can’t browse the SERPs, it doesn’t realize that an acronym like “AMA”—which has multiple meanings—is navigational. The same goes for “crockpot.”

However, here’s the incredible part. In the original test, ChatGPT had a lot of difficulty identifying navigational queries.

But when I tested it again a few months later, it learned:

It may not be perfectly ideal for now, but it’s learning and improving over time and could become a good tool to identify search intent.

### 13. Local SEO

Miriam Ellis, a local SEO expert, asked ChatGPT a few common local SEO questions. It offered less-than-ideal answers, such as encouraging her to violate Yelp’s guidelines, promulgate persistent local SEO myths, and more.

I highly recommend reading [her article](https://moz.com/blog/chatgpt-steered-me-wrong) to find out why ChatGPT isn’t ideal for local SEO.

## Final thoughts

Now that we have handpicked the best SEO use cases for you, your next step is to start implementing these tactics and use ChatGPT as your ideation partner or to improve your [SEO processes](https://ahrefs.com/blog/seo-process/).

Did I miss out on any prompts or use cases? Let me know [on Twitter](https://twitter.com/siquanong) or [LinkedIn](https://www.linkedin.com/in/si-quan-ong/).
