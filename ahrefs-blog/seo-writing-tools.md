---
title: "SEO Writing Tools (Do You Really Need Them?)"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "seo-writing-tools"
url: "https://ahrefs.com/blog/seo-writing-tools/"
canonical: "https://ahrefs.com/blog/seo-writing-tools/"
author: "Chris Haines"
published: "2023-04-11T06:22:52+00:00"
updated: "2023-08-02T12:06:18+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "date_2023_aging"
  - "time_sensitive_title"
fetched_at: "2026-06-12T12:09:18+00:00"
status_code: 200
html_hash: "085c83dddae22988aa4b1c5663c88b04e8c1c5ab3833e0ad969a993b94dbd97e"
clean_word_count: 2615
clean_char_count: 15468
---
# SEO Writing Tools (Do You Really Need Them?)

SEO writing tools help you improve your content. Here are the top reasons why you need them and the tools I use to improve my writing.

## 1. To find the best keywords to target

If your goal is to rank high on Google, writing content without targeting any keywords is risky. You can get lucky, but ranking in Google without proper targeting will be hard.

A better approach is to analyze keyword data using a tool like [Ahrefs](https://ahrefs.com/) and write your content using that knowledge.

Below, I’ll outline four ways you can use Ahrefs to help identify the best keywords to target.

### 1. To understand the keyword difficulty and competition

The first method I’d suggest is to add your keyword to Ahrefs’ [Keywords Explorer](https://ahrefs.com/keywords-explorer) and look at the **Keyword Difficulty** **(KD)** of the keyword.

For this example, I’ve used the keyword “typewriter.”

![KD data for "typewriter," via Ahrefs' Keywords Explorer](https://ahrefs.com/blog/wp-content/uploads/2023/04/image3-3.png)

Ahrefs estimates it’s a hard keyword to rank for. We’ll need backlinks from ~77 websites just to rank on the first page of Google for this keyword.

Let’s contrast this with a more specific search. Let’s say we’re looking for [this typewriter song](https://youtu.be/rVFR7wDZT9A); we might then enter “leroy anderson typewriter.”

Ahrefs estimates that this is a much easier keyword to rank for. We’ll need backlinks from only ~two websites to rank on the first page of Google.

The bottom line here is that not all keywords are created equal. So choose your battles (and your keywords) carefully.

### 2. To identify low-competition keywords

Let’s return to [Keywords Explorer](https://ahrefs.com/keywords-explorer), plug in a keyword phrase, and head over to the **Matching terms** report.

In this example, for the keyword “kimchi recipe,” we can’t see many low-competition keywords.

To get the lowest competition keywords, we’ll need to add a filter and set the KDto 20.

![Keyword Difficulty filter, via Ahrefs' Keywords Explorer

Once we have applied the filter, we can see more green KD scores—meaning these keywords are lower competition.

If we wrote articles about these specific keyword topics, we’d have a better chance of ranking than simply writing about “kimchi recipe” and all the initial matching terms.

### 3. To identify high traffic potential keywords

Open up a new instance of [Keywords Explorer](https://ahrefs.com/keywords-explorer), plug in the keyword “kimchi recipe,” and head over to the **Matching terms** report.

Then add a **Traffic Potential** filter from 0 to 30,000.

Once we have done this, we can see the keywords with the highest organic **TP.**

![Keywords with the highest Traffic Potential, via Ahrefs' Keywords Explorer

Let’s say we wanted to take it further and filter for the lowest **KD** keywords in this list.

We can do that by adding a **KD** filter with a max score of 20. Once we have done that, we’ll get the following list.

![Results with KD filter applied, via Ahrefs' Keywords Explorer

Having keywords to target that have a low **KD** and a high **TP** means that you will stand a good chance of ranking for them in Google.

### 4. To identify content gaps

Another way you can find opportunities for content is to use Ahrefs’ [Content Gap tool](https://ahrefs.com/content-gap).

For the next example, I’m going to stick with the “kimchi recipes” keyword. I’ll pretend I’m the BBC Good Food website, and I want to expand the Korean food content.

To do this, I’ve entered the top competitors of the “kimchi recipes” SERP into the **Content Gap** report and clicked the “Show keywords” button.

![Content Gap tool, via Ahrefs' Site Explorer

Once the report has been generated, I’ll filter it again using the keyword “korean,” as I only want to filter by Korean food content.

Here’s what it looks like:

![Content Gap report results with filter applied, via Ahrefs' Site Explorer

We can see how easy it is to find keyword opportunities that other websites rank for, but your website doesn’t.

## 2. To write basic content

Should you use SEO writing tools to create content? Well, it depends.

Writing content with SEO writing tools is still a contentious topic—especially if we are talking about AI tools like [ChatGPT](https://openai.com/blog/chatgpt).

Here’s why I think you should be cautious when using these tools:

- They don’t always fact-check.
- They make up the data sometimes.
- Sometimes they’ll lie if they don’t know the answer.
- They draw from internet sources that are often incorrect themselves.
- They aren’t always good with technical content.

If these bullet points were describing a potential content writer—you probably wouldn’t hire them.

But before you cancel your AI subscriptions, it’s worth noting that there’s a place for tools like these. But they are best used cautiously, in my opinion.

Here are three examples of where I *would* use SEO writing tools to help write basic content.

### 1. To create article outlines

SEO writing tools can help give you a framework to build your content around, but they typically need a lot of tweaking.

Here’s an example of me using [NeuralText](https://www.neuraltext.com/) to create an article outline:

And let’s repeat this with ChatGPT:

![ChatGPT's article outline example

We can see that with NeuralText, it’s gone for a standard structure. With ChatGPT, it’s not that different but provides a bit more detail.

If we compare this against the structure of the top-ranking pages in Google, we can see that the structure of the top-ranking pages is different.

![Top-ranking pages analysis, via Ahrefs' SEO Toolbar

In this particular example, it’s ~2000 words on the best SEO content writing tools. There’s no definition or importance of the tools; it’s just straight into the list of the top tools.

So should you use AI tools for outlines? Or is it better to write your own from scratch? It depends on how technical the writing is.

If your writing is non-technical, then an outline that covers the *definition*, *importance of*, and *role of* may be more than enough. But more specific details are often needed for more technical topics like [SEO](https://ahrefs.com/seo).

### 2. To create meta descriptions at scale

When it comes to writing basic content like meta descriptions, tools like ChatGPT—and, more specifically, [the OpenAI API](https://openai.com/blog/openai-api) can help you speed up the content creation process.

Here’s a quick example of some [meta descriptions](https://ahrefs.com/blog/seo-meta-tags/#meta-description) I generated programmatically using a [Google Apps script](https://gist.github.com/abi/94ffd06cf654038c75f56ff59ef2f086) I found on GitHub.

Assuming your content is in cell A2, you can drag the formula below down, and it will automatically generate the meta descriptions for you using the API.

Place the following code in cell B2 after running the script:

**`=AI("write an interesting meta description for cell("&[TITLE CELL NUMBER]&"))")`**

Replace [TITLE CELL NUMBER] with your cell reference. You can change the part stating “write an interesting meta description for cell” to any prompt, but I’ve kept it very basic.

Here’s the output:

| **Title** | **Meta description** |
| --- | --- |
| How many seats does a Tesla have? | Find out how many seats are in a Tesla car! Learn about the different models and their seating capacity to determine the perfect car for your needs. |
| How many seats does a Tesla Model X have? | Discover how many seats the Tesla Model X has and learn more about this revolutionary electric vehicle. Get the facts and find out why the Tesla Model X is the perfect car for your family. |
| How many teeth does a megalodon have? | This article explores the fascinating world of the megalodon, the largest shark to ever exist. Learn about how many teeth it had and how it compares to modern sharks. |
| How many numbers does a credit card have? | This article answers the question of how many numbers are on a credit card. Learn the answer, plus other interesting facts about credit cards and their uses. |
| How many parameters does a normal distribution have? | Discover the answer to the question “How many parameters does a normal distribution have?” and learn more about the fascinating world of cell distributions. |

Again, I’m not saying these are the greatest meta descriptions in the world, but if you have a large website, this can be an efficient (and cost-effective) way to write them at scale.

But what does Google think about this? Well, it is completely fine with [programmatically made meta descriptions](https://developers.google.com/search/docs/appearance/snippet#programmatically-generate-descriptions). But as always, remember to follow its general guidelines around [this topic](https://developers.google.com/search/docs/appearance/snippet).

### 3. To create newsletters or email templates

Another example of basic content is newsletters and email templates. Creating structured newsletters or emails with a tool like ChatGPT is a breeze.

Here’s an example of it in action:

![Newsletter template example, via ChatGPT

And you can also use it for email templates as well.

Here’s a quick example:

![Email template example, via ChatGPT

As we saw with the outlines, the content here is basic and likely needs improving. But for simple frameworks, it can be useful.

## 3. To make your content more readable

My favorite SEO writing tool for making my content more readable is Grammarly.

Here’s what I like about it.

### Grammarly

It’s a [paid tool](https://www.grammarly.com/plans) that helps improve your grammar. I find it helpful to use while writing or editing my content.

When creating a new document, you are encouraged to set goals. This allows the tool to tailor its suggestions based on your goals and audience.

![Setting goals, via Grammarly

Once you’ve set your preferences, Grammarly will score your writing and provide suggestions on clarity, engagement, style, delivery, and correctness.

![Demo document and suggestions, via Grammarly

It’s a helpful writing tool that many content teams have built into their proofreading process.

Once you have checked a few documents using Grammarly, you can get an analytics breakdown.

![Analytics breakdown of sessions, via Grammarly

It shows how many sessions you have improved. It has helped me improve 68% of my sessions—quite a lot.

I’ve used Grammarly a lot in the last year or so, and I can testify that it’s usually accurate. But I noticed once that it suggested replacing “links” with “sausages.”

https://twitter.com/chris\_at\_b449/status/1619272353178963968

This is a good example of where you still have to moderate the output and not blindly accept the AI suggestions all of the time.

### Hemingway

![Hemingway App editor example

Hemingway is another SEO writing tool you can use to help make your writing clearer and more concise. To get started, head over to [Hemingway’s website](https://hemingwayapp.com/), paste in your content, and it will analyze it for readability.

What I like about this tool is that it is clean, clear, and simple to use. Also, all the key information I need is in the right-hand column, meaning I don’t have to check word count through a menu or use other tools to analyze the writing.

In my opinion, any SEO writing tool that significantly helps improve your content’s quality is worth learning how to use.

## 4. To get creative inspiration

Another use for SEO writing tools is as a creative sparring partner.

Sometimes, it’s hard to get that spark of inspiration when writing.

But what if you could ask someone influential to write for you? Well, you can do this with AI—almost.

### Get some tone of voice inspiration

Here’s an example of me asking ChatGPT to write in the style of [David Ogilvy](https://en.wikipedia.org/wiki/David_Ogilvy_(businessman)):

![Copywriting example in the style of David Ogilvy, via ChatGPT

Using this type of prompt in ChatGPT allows you to get creative inspiration from famous copywriters or any other distinctive personalities you can think of.

Here’s a more extreme example of the same prompt in the style of [Gordon Ramsay](https://en.wikipedia.org/wiki/Gordon_Ramsay):

![Copywriting example in the style of Gordon Ramsay, via ChatGPT

The options here are limitless, and your writing’s tone of voice is only limited by your imagination and creativity.

The bottom line is that ChatGPT can help you develop interesting ideas you might not have thought of initially.

## 5. To level up your content process

Traditional content writing can be slow. It can sometimes be painful.

And it can take a lot of time.

But using SEO writing tools helps keep the momentum going.

You’ll likely get better results if you target your keywords correctly, write basic content, and proofread it using SEO writing tools.

### Become the “content cyborg”

[The folks at Animalz were the first to coin this phrase](https://www.animalz.co/blog/the-content-cyborg/), to my knowledge. And it’s one that has been stuck in my head this past year.

The content cyborg refers to the use of AI tools, but my definition goes broader—to SEO writing tools in general.

I think you should use tools that help you improve your content process and make it more efficient without sacrificing your overall content quality.

If you can speed up your content process, you will increase your output and work more efficiently.

Most of you won’t dream of using a typewriter to write blog content these days—it just doesn’t make sense. It’s too slow, inefficient, and not connected to the internet!

So when it comes to SEO writing tools, the question is not whether you should or should not use them, in my opinion. It’s more about *how* you can use them to increase the efficiency of your work to achieve better quality output.

## 6. To get more organic traffic

Ahrefs’ blog has had an impressive increase in organic traffic over the past year.

![Ahrefs Blog's organic traffic 2022–2023, via Ahrefs' Site Explorer

Looking at last year’s **Organic traffic** report in [Site Explorer](https://ahrefs.com/site-explorer), we can see we have increased our blog traffic by ~108% year on year.

But how much of this success is due to the SEO writing tools we use? Well, it’s hard to say exactly. But we do know that we use them to help create our content.

The most measurable example of us using SEO writing tools to improve our content is likely Grammarly.

![Grammarly analytics showing stats on writing sessions

According to its analytics report, its suggestions have positively impacted 65% of our writers’ sessions in the last month alone.

Although we can’t directly attribute any traffic increase to any particular SEO writing tool, it’s likely to have contributed to a positive experience for our readers. This, in turn, might have helped to drive more traffic to the site in the last year.

## Final thoughts

SEO writing tools are useful for many tasks. But you need to know *how* to use them effectively to get results.

But do you really need SEO writing tools? Well, yes, you do. But only if you use them properly. They can help you become more efficient at writing, increase output, and enhance content in ways you wouldn’t have thought of before.

Got more questions? Ping me [on Twitter](https://twitter.com/chris_at_b449). 🙂
