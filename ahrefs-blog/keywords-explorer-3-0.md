---
title: "Ahrefs Keywords Explorer 3.0: Re-Built From Scratch (With More Data)"
source: ahrefs-blog
content_type: "product_blog"
freshness_risk: "medium"
slug: "keywords-explorer-3-0"
url: "https://ahrefs.com/blog/keywords-explorer-3-0/"
canonical: "https://ahrefs.com/blog/keywords-explorer-3-0/"
author: "Tim Soulo"
published: "2019-02-04T12:32:56+00:00"
updated: "2023-06-19T21:14:29+00:00"
categories:
  - "Product Blog"
freshness_reasons:
  - "date_2023_aging"
  - "product_or_tool_content"
fetched_at: "2026-06-12T11:44:31+00:00"
status_code: 200
html_hash: "2166a596b179eb4359749b583c2343daaa44f74985ee497e684b35343f733083"
clean_word_count: 1241
clean_char_count: 7309
---
# Ahrefs Keywords Explorer 3.0: Re-Built From Scratch (With More Data)

In 2016 we invested a ton of time and resources into creating one of the best (if not *the* best) keyword research tools in the industry: [Keywords Explorer](https://ahrefs.com/keywords-explorer).

In 2018 we rebuilt the whole thing from scratch.

This product update is different from that of [Keywords Explorer 2.0](https://ahrefs.com/blog/keyword-generator/) in the sense that most of the work this time around was done on the backend as opposed to the frontend. In other words, rather than adding a plethora of new UI features—as we did with KE 2.0—we instead added nine additional sources of data and rebuilt the entire thing with new technology.

## YouTube, Amazon, Bing, Yahoo, Baidu…

In Keywords Explorer 3.0, we’ve added 8 (!!!) more search engines:

1. YouTube
2. Amazon
3. Bing
4. Yahoo
5. Baidu
6. Daum
7. Naver
8. Seznam

Most SEOs and content marketers know that Google is not the only search engine; it’s merely the biggest. If you want to get more exposure for your work (or business), then you have to consider every opportunity at your disposal.

For me, the most important of the nine new search engines is YouTube.

I published [the very first video](https://www.youtube.com/watch?v=WikWn29F0sI) on the [Ahrefs YouTube channel](https://www.youtube.com/channel/UCWquNQV8Y0_defMKnGKrFOQ) on August 8th, 2015. Back then I was recording myself on my iPhone 5, and it took me nearly 4 hours to create that initial video because of how awful I was at talking on camera in a non-native language.

Fast-forward almost four years and, thanks to the incredible Sam Oh, we’ve now had more than 2 million views on our channel and currently have ~36k subscribers.

Even more impressive, we did this **without** a [keyword strategy](https://ahrefs.com/blog/keyword-strategy/).

However, now that we have YouTube keyword data, we’re excited and hopeful to achieve an even faster rate of growth for our video content in 2019.

### Data origins

Since we started teasing keyword data for YouTube and Amazon, many fellow SEOs have naturally asked where that data comes from.

It’s [clickstream](https://moz.com/blog/clickstream-data-revolution).

In case you’re unfamiliar with the term, clickstream data is collected via all sorts of software and applications (mostly the free ones) that people install on their computers. These applications (other than doing whatever they’re made to do) collect your browsing data, **anonymize it (!!!)** and re-sell to other companies.

From our clickstream data partner, we buy data on the **actual searches** that people around the world perform on the aforementioned “search engines.” We then use some maths to extrapolate these numbers and estimate the popularity of each search query.

**IMPORTANT:** To the best of our knowledge, no other keyword tool on the market today runs on clickstream data for YouTube, Amazon, Bing, etc. Thus, before comparing our data to that of any third-party tools, be sure to inquire about the origins of their data.

Being brutally honest, buying clickstream data for nine more search engines costs us an arm and a leg. However, judging by the feedback from the community thus far, we can already tell it was worth it.

## Taking product development to a whole new level

In early 2018, our Founder and CEO, [Dmitry](https://twitter.com/botsbreeder), made a bold move which caught me off guard.

He decided that instead of releasing new tools and features at the same pace as we did in 2017, we were instead going to take a step back and devote a whole year towards upgrading the technology on which our product runs.

Here’s what he said when asked about his thought process behind this decision:

> Being a company without VC funding, there’s no pressure for us to prioritize short-term growth over long-term product strategy. By 2020, we want Ahrefs to be *the* must-have tool for any company with a website. That’s our primary focus. I believe that for our product to stay relevant, we need a clean and modern UI. At the same time, we want to continue to be able to quickly add new features whilst maintaining a small team. For that reason, we’re more than happy to take a step back and invest time into improving our development process.
>
>
>
> Dmitry Gerasimenko, Founder & CEO [Ahrefs](https://ahrefs.com)

Twelve months later, and Keywords Explorer 3.0 now runs on [React](https://ahrefs.com/blog/react-seo/), ReasonML, and OCaml.

For the non-developers out there—which I assume is most of you—let me explain what this *geekery* means for you as an Ahrefs user:

### Faster tools

This new technology employs the latest advances in computer science and is way more efficient, which allows us to build tools that work noticeably faster.

That means less time waiting for reports to load and more time for the actual work that pays the bills.

### Faster development pace

Here’s an excerpt from [a fantastic article by Paul Graham](http://www.paulgraham.com/avg.html) that Dmitry shared with me to better explain his vision for Ahrefs:

> A company that gets software written faster and better will, all other things being equal, put its competitors out of business. […] In a startup, if you bet on the wrong technology, your competitors will crush you.
>
> […]
>
> We knew Lisp was a really good language for writing software quickly, and server-based applications magnify the effect of rapid development, because you can release software the minute it’s done. […] And because Lisp was so high-level, we wouldn’t need a big development team, so our costs would be lower.
>
>
>
> Paul Graham  [paulgraham.com](http://paulgraham.com/)

Replace “Lisp” with “OCaml + [ReasonML](https://reasonml.github.io/docs/en/what-and-why)” and you’ve got Dmitry’s tech vision for Ahrefs.

We’ve already experienced the competitive advantage of using the “right” technology for nine years, as we’ve been using [OCaml](https://ocaml.org) for our backend since 2010. That has allowed us to do things that our competitors can’t replicate.

Going forward, as a result of adopting these high-level programming languages, we’ll be able to:

- Build better and faster tools while maintaining a small team of developers (we only have ~45 employees)
- Ship new product updates much quicker than we did before.

In other words, you can expect to see a ton of new features/improvements added to Keywords Explorer throughout 2019 (don’t forget that we welcome you to [request features via Canny](https://ahrefs.canny.io/keywords-explorer?sort=top)).

You might also be wondering why we’re publicly sharing our tech stack, after stating how much of a competitive advantage it gives us. Well, here’s another excerpt from that same article:

> […] I didn’t need to be secretive, because even if our competitors had known we were using Lisp, they wouldn’t have understood why: “If they were that smart they’d already be programming in Lisp.”

So there’s *that*.

## It’s only the beginning…

Keywords Explorer 3.0 is a big step forward, and it provides a solid foundation for what’s to come next.

Armed with new technology and [valuable user feedback](https://ahrefs.canny.io/), let’s just say that 2019 is shaping up to be a fun year for both the Ahrefs team and our customers. 😉
