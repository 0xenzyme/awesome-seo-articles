---
title: "What is hreflang and how does it work?"
source: semrush-blog
content_type: "faq_short"
freshness_risk: "low"
slug: "what-is-hreflang-and-how-does-it-work"
url: "https://www.semrush.com/blog/what-is-hreflang-and-how-does-it-work/"
canonical: "https://www.semrush.com/blog/what-is-hreflang-and-how-does-it-work/"
author: "Semrush Team"
published: "2025-09-16T10:47:00+00:00"
updated: "2025-09-16T10:47:00+00:00"
categories:
  - "Frequently Asked Questions"
freshness_reasons: []
schema_genre: "Frequently Asked Questions"
fetched_at: "2026-06-12T21:04:28+00:00"
status_code: 200
html_hash: "4eb7959e95ecc5c40a573bbaa3b1f03cbbb8da7d6fc9e8e2e3ec4fe1f08fa780"
clean_word_count: 400
clean_char_count: 2672
---
# What is hreflang and how does it work?

[Hreflang](https://www.semrush.com/blog/hreflang-attribute-101/) is an HTML attribute that tells search engines which language and regional version of a webpage to display to users based on their location and language preferences.

Hreflang works by including a code within a page’s HTML that indicates the specific language and region targeting for that page. Search engines then use this information to serve the correct version to users, improving user experience.

Here’s how you might see hreflang implemented on a webpage:

`<link rel="alternate" hreflang="en-US" href="https://example.com/us/">
<link rel="alternate" hreflang="en-GB" href="https://example.com/uk/">
<link rel="alternate" hreflang="fr-ca" href="https://example.com/fr-ca/">
<link rel="alternate" hreflang="x-default" href="https://example.com/">`

The above tags tell search engines that you have US, UK, and Spanish versions of your page, plus a default version for users who don’t match any of the listed languages or regions.

Here are the key things you should know about hreflang:

- **Hreflang prevents duplicate content issues**. When you have similar content in different languages or for different regions, hreflang signals to search engines that these are intentional variations rather than duplicate content. This prevents any unintended consequences, such as a drop in rankings.
- **It uses ISO language and country codes**. The attribute format is hreflang="language-country" such as en-us for English speakers in the United States or fr-ca for French speakers in Canada.
- **Implementation requires reciprocal linking**. Each language version must include hreflang tags pointing to all other versions, including itself.
- **You can implement hreflang in multiple ways.** Add it to HTML head sections, [XML sitemaps](https://www.semrush.com/blog/xml-sitemap/), or HTTP headers, with XML sitemaps often being the cleanest approach for large international sites.
- **Self-referencing hreflang tags are required.** Each page must include an hreflang tag pointing to itself, such as a US page including hreflang="en-US" pointing to its own URL.
- **Include x-default for international users.** Specify a fallback page for users whose language/location doesn't match any specific version.

Proper hreflang implementation ensures search engines serve the right content to the right users, improving both SEO performance and user satisfaction for international websites.

Confirm your hreflang tags are present with a free [SEO check](https://www.semrush.com/siteaudit/). To validate your implementation and catch errors, use Semrush Site Audit tool.
