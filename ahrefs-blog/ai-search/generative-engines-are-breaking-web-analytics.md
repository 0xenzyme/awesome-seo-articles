---
title: "AI Assistants Are Breaking Web Analytics and Hurting Their Future"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "generative-engines-are-breaking-web-analytics"
url: "https://ahrefs.com/blog/generative-engines-are-breaking-web-analytics/"
canonical: "https://ahrefs.com/blog/generative-engines-are-breaking-web-analytics/"
author: "Patrick Stox"
published: "2025-05-26T16:39:21+00:00"
updated: "2026-05-31T08:56:10+00:00"
categories:
  - "AI Search"
  - "General Marketing"
freshness_reasons: []
fetched_at: "2026-06-12T11:32:07+00:00"
status_code: 200
html_hash: "c03d297bfd10ce23799160304297613277b29e8de6f92c7fde8d1a3c01d79a43"
clean_word_count: 1331
clean_char_count: 8000
---
# AI Assistants Are Breaking Web Analytics and Hurting Their Future

Search is moving from traditional search engines to AI assistants, but traffic from many of these sites isn’t being tracked properly in analytics. It’s their fault, not yours.

I was looking at our LLM filter in [Ahrefs Web Analytics](https://ahrefs.com/web-analytics) and noticed some common AI assistants missing from the list. They’re in our filters, but we aren’t seeing any data from them for sites.

![Ahrefs Web Analytics filtered to LLM traffic](https://ahrefs.com/blog/wp-content/uploads/2025/05/ahrefs-web-analytics-filtered-to-llm-traffic.png)

This invisible traffic problem comes from these systems stripping the referral value. I first noticed this [problem with AI Mode in Google](https://ahrefs.com/blog/google-ai-mode-is-here-but-you-cant-track-it-properly/), but it’s a common problem for AI assistants.

This is most likely a mistake on their part, but in some cases may be intentional. Some of these tools probably want more market share and just made a mistake, while others may not want you to be able to measure traffic from the systems. Google has said the clicks from AI Search are higher quality, but we have no way to verify that.

If you have a website that sends traffic to other sites, you should want it to be tracked properly. In the case of AI assistants, I warned that these AI bots need to send that info in order to [fulfill their social contract](https://ahrefs.com/blog/ai-bot-block-rates/), where they provide traffic to websites, and websites allow these bots to crawl and their data to be used.

> > There’s a cost to bots crawling your websites and there’s a social contract between search engines and website owners, where search engines add value by sending referral traffic to websites. This is what keeps most websites from blocking search engines like Google, even as Google seems intent on taking more of that traffic for themselves. This social contract extends to AI assistants.
> >
> > I think many site owners want to let these bots learn about their brand, their business, and their products and offerings. But while many people are betting that these systems are the future, they currently run the risk of not adding enough value for website owners.
> >
> > The first LLM to add more value to users by showing impressions and clicks to website owners will likely have a big advantage. Companies will report on the metrics from that LLM, which will likely increase adoption and prevent more websites from blocking their bot.

The same sentiment is true for attribution. If these AI assistants want to win market share, they need to be present in reporting to companies. So far, many are not doing a great job.

## Methodology and findings

I was checking the referrer value by typing “document.referrer” in Chrome Dev Tools Console to see if the referrer was passed. If it is, it outputs a value saying where it came from, and if not, it’s blank.

Some of the AI assistants send the referrals, others don’t send them at all, and some send them for certain things and not others. I’ve marked those with a warning to indicate partial results.

## ChatGPT **⚠️**

An in-content link in my paid account of ChatGPT has a [noreferrer attribute](https://ahrefs.com/seo/glossary/noreferrer) on the link. This would prevent the referral value from being sent.

As expected, there is no referrer shown in the Chrome Dev Tools Console. It comes back empty.

```
document.referrer
''
```

In [Ahrefs Web Analytics](https://ahrefs.com/web-analytics), this is recorded as Unknown, but in Google Analytics it would be classified as Direct. Google lumps traffic from unknown sources and internal website traffic together as Direct, whereas we separate them into Unknown and Internal.

What’s interesting is that when I looked at the same type of link in a free account, it did not have the noreferrer attribute. It’s tracked properly.

For lists of links, they were also tracked properly.

The links to Sources in the content and at the bottom of the response are also tracked properly, and they add a [URL parameter](https://ahrefs.com/blog/url-parameters/) “?utm\_source=chatgpt.com” to the URLs as well.

### Web Search

Most of the links in Web Search mode had the referrer. I did run into an interesting example when there are multiple references. The top one had a referrer, the other 2 did not.

### DeepResearch

For DeepResearch mode, in-content links were attributed properly, but the sources at the end were marked with noreferrer.

### HTTP Headers

If you look at the HTTP Headers, you’ll sometimes find a [Referrer-Policy header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referrer-Policy) to specify what and how much information gets passed in the referrer. You can use the [Ahrefs SEO Toolbar](https://ahrefs.com/seo-toolbar) to view this information by going to the HTTP headers tab.

For ChatGPT, they’ve set a referrer-policy value of “strict-origin-when-cross-origin”. In this case, the downgrade from HTTPS to HTTP would drop the referrer. Any links to pages using HTTP wouldn’t be attributed properly.

## Google Gemini ⚠️

Most of the contextual and cited links within Gemini did have the referrer.

The one case that didn’t was the “Researching websites” section in Deep Research mode. These are marked as noreferrer.

### AI Mode

The new AI Mode in Google Search is also powered by Gemini. You might have seen my recent article showing that [AI Mode is marked with noreferrer](https://ahrefs.com/blog/google-ai-mode-is-here-but-you-cant-track-it-properly/).

John Mueller from Google has since confirmed it’s a bug and that they will likely fix it.

## Microsoft Copilot Web ✅ Windows ❌

In a previous article, [Louise Linehan](https://ahrefs.com/blog/author/louise-linehan/) mentioned that we may be [underestimating AI traffic](https://ahrefs.com/blog/ai-traffic-study/#underestimating-ai-traffic). She specifically mentioned how Copilot disappeared from our analytics tracking system. Since that time, the traffic has returned.

What I suspect is that these links were marked as noreferrer during that time period. This shows how code changes can impact your global tracking.

Everything here seemed to be tracked properly now.

That’s not the case with Copilot in Windows. I found no cases where the referrer was passed.

## Perplexity Web ✅ Desktop ❌

Their website seemed to send referrers on everything.

Their desktop app doesn’t seem to send referrers on anything. I did not try the mobile app.

## Claude ✅

Claude seems to have the referrer for all the links in all the areas I tested.

## Grok ❌

Grok doesn’t seem to pass the referrer at all. I tried the standalone Grok and the version on X.

## DeepSeek **⚠️**

The normal DeepSeek and Deep Research didn’t pass the referrer.

For web search, the individual citations passed the referrer, but the links at the end did not.

## Meta AI ✅

Meta AI passed the referrer for the web version. I didn’t test this on any of the social media platforms.

## Mistral ✅

Mistral passed the referrer in all instances I checked.

## Final thoughts

Attribution issues aren’t unique to AI assistants. Lots of traffic gets attributed to Unknown or Direct in your analytics. That traffic came from somewhere.

There’s a good chunk of website traffic that’s never recorded in analytics because of people blocking analytics or JavaScript, some sites wait for cookie acceptance before firing, or people leave a page before your analytics tag even fires.

Attribution is getting harder every year. If you’re a AI assistant and want to make sure people know they’re getting traffic from you, test all your links to make sure the data is being sent. Your very survival might depend on your reputation in the marketing community and the visibility you have in marketing reports.

If you have questions, ask me on [LinkedIn](https://www.linkedin.com/in/patrickstox/) or [X](https://x.com/patrickstox).
