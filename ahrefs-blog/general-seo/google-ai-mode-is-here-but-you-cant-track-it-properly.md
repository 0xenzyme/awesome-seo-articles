---
title: "Google Made It So You Can't Track Clicks From AI Mode (Partially Fixed)"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "google-ai-mode-is-here-but-you-cant-track-it-properly"
url: "https://ahrefs.com/blog/google-ai-mode-is-here-but-you-cant-track-it-properly/"
canonical: "https://ahrefs.com/blog/google-ai-mode-is-here-but-you-cant-track-it-properly/"
author: "Patrick Stox"
published: "2025-05-21T20:17:20+00:00"
updated: "2025-05-31T17:39:02+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "ai_search_topic"
fetched_at: "2026-06-12T11:32:36+00:00"
status_code: 200
html_hash: "e18536b83998a027dc89582a5d5c68bad0d2039de67897d52e53dc6c1ba83958"
clean_word_count: 651
clean_char_count: 3666
---
# Google Made It So You Can’t Track Clicks From AI Mode (Partially Fixed)

Google just [rolled out AI Mode to US users](https://blog.google/products/search/google-search-ai-mode-update).

I was testing if the clicks would show in Google Search Console, but they aren’t showing up. A [post by Tom Critchlow on LinkedIn](https://www.linkedin.com/posts/tomcritchlow_im-right-in-saying-that-clicks-from-ai-mode-activity-7330997507012886529-90mi?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAMO5mUBX0XPZ9sSJQmgODr6I0IiBaukMSs) made me wonder how a click on a link in AI Mode would be recorded in analytics.

The tl;dr is that clicks to links in AI mode are not being recorded at all in Google Search Console, and they’re not sending a referrer value when you click. They’re treated as Unknown or Direct, depending on your analytics system.

Update May 31st: The noreferrer bug was fixed. This now records as Google / organic or Google / search. I tested this in GA4 and Ahrefs Analytics. The GSC issue still remains, but they updated the documentation to say “Note: AI Mode reporting isn’t live in Search Console yet, but we expect this soon as part of the AI Mode rollout.”

![](https://ahrefs.com/blog/wp-content/uploads/2025/05/GsC-vxtXIAAhpna.png)

Update May 27th: Google has said they’re tracking the noreferrer issue as a bug + they updated the documentation to say “Note: AI Mode reporting isn’t live in Search Console yet, but we expect this soon as part of the AI Mode rollout.”

That’s a big problem if we don’t have correct attribution. Does Google not want us to be able to track these?

Here’s the test, which I’ve repeated several times to ensure accuracy.

Pick a URL that doesn’t get any traffic on your site and paste it into AI mode. It will generate some info and a link to your URL which you can click.

After I clicked I checked [Ahrefs Web Analytics](https://ahrefs.com/web-analytics) for the page, which has real-time information, but you can check in Google Analytics or whatever analytics program you use.

As you can see below, this is classified as coming from an Unknown location. In other analytics systems like Google Analytics, this would show as Direct.

What’s going on?

The link itself is marked with [noreferrer](https://ahrefs.com/seo/glossary/noreferrer) in the code of the page. You can verify this by using inspect in your browser. This means that the referrer value is stripped, leading it to be treated as unknown.

As I mentioned earlier, for the last couple days I’ve been testing a few pages to see if clicks to links in AI Mode will show in Google Search Console. The answer, unfortunately, is no.

Here’s one from yesterday where I searched “what are accelerated mobile pages from ahrefs?” and clicked. As you can see, I show no clicks in GSC.

Looking at the code, I see the normal tracking info that indicates where and how a link is displayed and the ping which I believe sends it over to Google’s tracking systems.

Even though the link was tagged, the data doesn’t seem to be in Google Search Console. This could indicate that AI Mode tracking is coming soon though, possibly as a separate classification.

## Final Thoughts

Attribution is important, and we don’t have it yet. It makes me suspicious that there’s something Google doesn’t want us to know about this traffic. Is it that bad for website owners that they won’t even show it to us?

I’m hoping Google will remove the noreferrer tag from these links so they’re recorded properly in analytics systems, and I’m also hopeful that we will get data for AI Mode. For now, be aware that this data is missing in GSC and incorrectly classified in analytics.
