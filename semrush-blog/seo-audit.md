---
title: "How to Perform a Complete SEO Audit in 20 Steps"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "seo-audit"
url: "https://www.semrush.com/blog/seo-audit/"
canonical: "https://www.semrush.com/blog/seo-audit/"
author: "Tushar Pol, Faizan Ali, Cecilia Meis"
published: "2020-06-01T11:00:00+00:00"
updated: "2026-04-22T09:43:00+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "time_sensitive_title"
schema_genre: "General SEO"
fetched_at: "2026-06-12T19:11:49+00:00"
status_code: 200
html_hash: "c7f386a86ff725bafcdb6c45603f8da0383e20ee29b77e6163a02ffe8082679b"
clean_word_count: 10539
clean_char_count: 72446
---
# How to Perform a Complete SEO Audit in 20 Steps

An SEO audit is the starting point of every optimization strategy. It shows you what's working, what's broken, and where the biggest growth opportunities are in both traditional search and AI-driven discovery.

But knowing how to do an SEO audit today is different from even a year ago — because what you're auditing for has changed.

When someone searches on Google, they no longer see only blue links. They may see [AI Overviews](https://www.semrush.com/blog/ai-overviews/), [AI Mode](https://www.semrush.com/blog/google-ai-mode/) responses, video results, shopping features, and user-generated content before traditional organic listings.

And Google isn’t the only discovery platform anymore.

People now turn to tools like ChatGPT, Perplexity, Gemini, and Claude to research products, compare services, and get recommendations. These systems don't just rank websites; they summarize, cite, and recommend brands.

That means your SEO audit can’t focus only on rankings.

It needs to answer bigger questions:

- Can search engines crawl and understand your site?
- Does your content deserve to rank—and to be cited?
- Are AI systems referencing your brand?
- Are competitors earning visibility you’re missing?

This guide walks you through a complete 20-step SEO audit covering technical SEO, content, backlinks, SERP features, and AI visibility — with the tools you need for each step.

## What is an SEO audit?

An SEO audit is a structured evaluation of how well your website is optimized for visibility across both traditional search engines and AI-driven large language models (LLMs).

It helps you understand where you stand, what’s holding you back, and what to fix first.

A complete SEO audit looks at:

- [**Crawlability and indexability**](https://www.semrush.com/blog/what-are-crawlability-and-indexability-of-a-website/): Whether search engines and AI crawlers can access and understand your pages
- **Technical performance**: Site speed, mobile-friendliness, [Core Web Vitals](https://www.semrush.com/blog/core-web-vitals/), and overall usability
- **Content quality and intent match**: How fully your content satisfies what users (and AI systems) are looking for
- **Search visibility**: How you perform in organic search results, SERP features, and AI-generated responses
- **Brand representation**: How AI platforms describe, cite, and connect your brand to key topics
- **Authority signals**: Your [backlink](https://www.semrush.com/blog/what-are-backlinks/) profile, brand mentions, and competitive gaps

Think of an SEO audit as a website health check. It reveals strategic opportunities to increase rankings, earn citations, and strengthen your authority everywhere people search for answers online.

You don’t need to run a massive audit every week. But conducting one quarterly helps you stay proactive instead of reacting to traffic drops after they happen.

## What tools do you need for an SEO audit?

You can’t run a proper SEO audit without data. And that means using the right tools.

At minimum, you’ll need tools to analyze:

- Technical health
- Search performance
- Content and keyword gaps
- Backlinks and authority
- AI visibility

Here’s the core toolkit.

### Semrush tools

If you’re using Semrush, you can complete almost every part of this audit with its core tools:

|  |  |
| --- | --- |
| **Tool** | **What It’s Used For** |
| [Site Audit](https://www.semrush.com/siteaudit/) | Crawl your site to find technical errors, crawl issues, broken links, and performance problems |
| [On Page SEO Checker](https://www.semrush.com/on-page-seo-checker/) | Get optimization ideas for specific pages based on target keywords |
| [Backlinks](https://www.semrush.com/analytics/backlinks/) | Analyze your backlink profile, referring domains, and link quality |
| [Backlink Gap](https://www.semrush.com/analytics/gap/backlinks/) | Find backlink opportunities your competitors have that you don’t |
| [Position Tracking](https://www.semrush.com/position-tracking/) | Monitor rankings and SERP feature visibility for target keywords |
| [AI Visibility Toolkit](https://www.semrush.com/ai-seo/overview/) | Track how often your brand is mentioned or cited in AI-generated answers |
| [Topic Research](https://www.semrush.com/topic-research/) | Discover subtopics, questions, and content ideas to expand coverage |

You’ll see these tools used throughout this guide. In most cases, multiple tools work together to give you a complete picture of your site’s performance.

### Google tools

You’ll also need first-party data from Google:

- [Google Search Console](https://search.google.com/search-console/about) (GSC): Monitor impressions, clicks, index coverage, and search queries
- [Google Analytics 4](https://developers.google.com/analytics) (GA4): Analyze traffic trends, engagement, and conversions

### Crawling tools

To get a deeper technical view of your site structure:

- [Screaming Frog SEO Spider](https://www.screamingfrog.co.uk/seo-spider/) – Crawl your site to analyze URLs, status codes, metadata, internal linking, and crawl depth

Many of these tools offer free versions or trials with limited access, so you can start auditing before committing to a paid plan.

In the next section, we’ll walk through exactly how to use them in a complete 20-step SEO audit.

## How to do an SEO audit: 20-step checklist

Below are the steps I follow when performing a thorough SEO audit.

### 1. Make sure crawlers can access your site

Before anything else, confirm that your pages are accessible and discoverable. If crawlers can’t reach your site, nothing else in this audit matters.

Start by checking your [robots.txt](https://www.semrush.com/blog/beginners-guide-robots-txt/) file.

Visit **yourdomain.com/robots.txt** in your browser. You’ll see a file that looks something like this:

`User-agent: *
Allow: /
Disallow: /admin/`

Look for any Disallow directives that might be blocking important sections of your site. Staging rules and accidental sitewide blocks get left in place more often than you’d think.

You can validate robots.txt settings in [Google Search Console (GSC)](https://www.semrush.com/blog/google-search-console/) or review crawl results in Semrush’s [Site Audit](https://www.semrush.com/siteaudit/) tool.

![Site Audit Overview report with the "Crawled Pages" widget highlighted.](https://static.semrush.com/blog/uploads/media/5e/2c/5e2c73e03ea2ba5679b69a8dc7ed9300/70d43608678a0d9319280c163c78be1a/image.jpeg)

Make sure you’re not accidentally blocking these crawlers:

- **Googlebot**: Google’s main search crawler
- **BingBot**: Bing’s search crawler (also influences Copilot results)
- **OAI-SearchBot**: Used by OpenAI for real-time search and citations in ChatGPT
- **PerplexityBot**: Perplexity’s search crawler
- **Claude-SearchBot:** Used by Anthropic for real-time retrieval and citations in Claude

You can also choose whether to allow the training crawlers below. Blocking them keeps your content out of future AI model training; allowing them means your content may be used to train these models:

- **Google-Extended:** Google's AI model training (Gemini)
- **GPTBot:** OpenAI model training
- **ClaudeBot:** Anthropic's Claude model training

If you see a block like the one below, you’re preventing a specific AI platform from accessing your site entirely:

*User-agent: GPTBot
Disallow: /*

Next, review your [XML sitemap](https://www.semrush.com/blog/xml-sitemap/).

It should include your most important indexable pages and exclude broken, redirected, or noindex URLs.

Make sure it’s submitted in GSC and reflects your current site structure. [Site Audit](https://www.semrush.com/siteaudit/) can flag sitemap errors automatically and show mismatches between submitted and indexed URLs.

![The "Issues" tab on Site Audit with "sitemap" entered showing a list of sitemap errors and warnings.](https://static.semrush.com/blog/uploads/media/5a/3f/5a3f4983d760fcae1d0ae842523a15d7/9f43000055aac64f83ea86e0e21a3383/image.jpeg)

Look for any crawl-blocking errors, like important pages returning 404 errors or server errors, as these can prevent crawlers from accessing key content. (You’ll audit and fix these in detail in [Step 7](#h-7-crawl-your-site-for-technical-errors).)

Finally, consider how your content is rendered.

While Google can process [JavaScript](https://www.semrush.com/blog/javascript/), heavy client-side rendering can delay or limit crawling. Make sure critical content is visible in the initial HTML where possible.

For a deeper dive, see our [guide to JavaScript rendering](https://www.semrush.com/blog/js-rendering/).

### 2. Check your site architecture and crawl depth

With crawl access confirmed, focus on making your site easy to navigate through strong internal linking and [site architecture](https://www.semrush.com/blog/website-structure/).

A well-structured site:

- Helps crawlers discover content faster
- Distributes authority across important pages
- Improves user experience
- Makes it easier for AI systems to understand topical relationships

One of the most important concepts here is crawl depth, or how many clicks it takes to reach a page from your homepage.

In general:

- Important pages should be within three clicks of the homepage
- Pages buried deeper than that are harder to crawl and may not rank as well

If key pages are five or six clicks deep, they’re harder for search engines to prioritize (or for users to find).

To check crawl depth, use [Site Audit](https://www.semrush.com/siteaudit/).

Run a crawl, scroll down to "**Thematic Reports**" and click the "**Internal Linking**" report to see how deep your pages are within your site architecture.

![Thematic Reports on Site Audit with "View details" clicked on the Internal Linking widget.](https://static.semrush.com/blog/uploads/media/41/b5/41b50baf7ed003bc09bc3e6f8702f37f/96e558436bffac55e4b9dec8e458ca55/image.jpeg)

Look for important pages that require 4+ clicks to reach, as these may be harder for crawlers to discover and prioritize.

![The "Pages Crawl Depth" widget on the Internal Linking report with pages requiring 4+ clicks highlighted.](https://static.semrush.com/blog/uploads/media/a1/c4/a1c4f1d1e6f285470f8ce6cb9ca9c086/4a7b3e9f017ef72550481ce4e3a96d01/image.jpeg)

Check out our [internal linking guide](https://www.semrush.com/blog/internal-links/) to learn the best way to add more links to these pages.

If you need more granular control, you can also use Screaming Frog. Run a crawl and sort by the “**Crawl Depth**” column to identify pages that are buried too deep in your site structure.

![Screaming Frog with the "Crawl Depth" column highlighted showing pages sorted from high to low crawl depth.](https://static.semrush.com/blog/uploads/media/02/3c/023c3864a6cf9d2813e816282a0518ab/6f2cec5b3cf2e64329b862c500d12646/image.jpeg)

Next, review your overall site structure.

Ask yourself:

- Does your site follow a logical hierarchy (Homepage → Category → Subcategory → Page)?
- Are related pages grouped together?
- Are important commercial or high-value pages easy to reach?

Messy architecture creates crawling inefficiencies and weakens authority distribution.

You should also check for pages that are isolated in the structure, overly complex navigation, important pages linked only from footers, and deep blog posts with no contextual internal links.

Here’s an example of solid site structure:

![Optimized website architecture with the home page divided into category pages, subcategory pages, and finally sub-subcategory pages.](https://static.semrush.com/blog/uploads/media/41/9c/419cc0e3323e00ef2e507c1532ac9b66/33c1a5464b5b4252a6923596566bd8f0/image.png)

A clean architecture makes your site easier to crawl, easier to understand, and easier to trust.

### 3. Check for duplicate versions of your site

Having multiple versions of your website accessible to search engines can seriously dilute your SEO efforts and confuse search engines about which version to rank or cite.

I’ve seen this issue most often on newly launched websites that haven’t standardized their URL structure. As a result, the site may exist at multiple URL versions (depending on whether there's www in the domain and whether the site uses HTTPS).

Google may see each version as a separate website, splitting your authority (ranking potential) between them. This can lead to poor performance.

To identify whether duplicate versions of your pages exist, try accessing your site through these URLs:

- http://yourdomain.com
- https://yourdomain.com
- http://www.yourdomain.com
- https://www.yourdomain.com

Only one version should be accessible and all others should redirect to it using [301 redirects](https://www.semrush.com/blog/301-redirects/).

You should use the HTTPS version because it encrypts data between your server and users' browsers. This improves security, user trust, and can give you a slight visibility boost in search.

As for whether you use WWW or not, it’s a personal preference, and it doesn’t matter for SEO as long as only one version is accessible.

### 4. Ensure your site is mobile-friendly

More than half of web traffic [comes from mobile devices](https://www.statista.com/statistics/277125/share-of-website-traffic-coming-from-mobile-devices/), and Google knows it. Google primarily [uses the mobile version](https://www.semrush.com/blog/mobile-first-indexiing/) of your site for indexing and ranking.

But mobile-friendliness isn’t just a ranking factor. It’s also a [user experience (UX) factor](https://www.semrush.com/blog/ux-and-seo/), and UX directly impacts how search engines and AI systems evaluate your site.

If users land on your page and quickly bounce because it’s hard to read or navigate on mobile, that sends negative engagement signals.

To fix this, start by checking whether your site is truly responsive.

Resize your browser window and watch how the layout adjusts. Text, images, and navigation should adapt smoothly to different screen sizes without overlapping, shrinking awkwardly, or breaking entirely.

![Responsive design showing how the same page can be optimized for different devices like an iPhone, tablet, and laptop/desktop.](https://static.semrush.com/blog/uploads/media/8b/05/8b05515ebf4213448ee957c4bacae8ce/990e51c5bd16ede76c7f0c27d9100744/image.jpeg)

Then check Bing’s [Mobile Friendliness Test Tool](https://www.bing.com/webmaster/tools/mobile-friendliness). Enter your website URL, and the tool will analyze the page to see if it meets mobile usability standards.

![Bing’s Mobile Friendliness Test Tool with "backlinko.com" entered, "Analyze" clicked, and the result "This page is mobile friendly" highlighted.](https://static.semrush.com/blog/uploads/media/88/1a/881a1698afa21ec744e601aad3fd68cb/9cbb0d918f009b24391679c23ce78772/image.jpeg)

If you discover mobile issues, the fixes are often straightforward:

- **Text readability**: Make sure the content is easy to read without zooming
- **Tap targets**: Make sure buttons and links are large enough to tap precisely
- [**Viewport configuration**](https://www.semrush.com/blog/viewport-meta-tag/): Ensure the site can properly scale according to different device sizes
- **Media playback**: Make sure videos and interactive elements work properly on mobile devices
- **Load time**: Optimize your site to load quickly on mobile networks

If you're on WordPress, plugins like [WP Rocket](https://wp-rocket.me/) (caching and performance) and [ShortPixel](https://shortpixel.com/) (image compression) can help with load-time issues specifically. For other platforms, look for built-in performance optimization settings or consult your platform's documentation.

Lastly, simplifying navigation menus can also improve usability on smaller screens.

### 5. Evaluate your site speed

Test your site speed using Google’s [PageSpeed Insights Tool](https://pagespeed.web.dev/) and prioritize fixes for any page scoring below the mid-80s.

Site speed is a small Google ranking factor, but it’s one of the most impactful elements of user experience. A fast-loading site tends to have lower [bounce rates](https://www.semrush.com/blog/bounce-rate/) and better engagement. Slow pages frustrate users regardless of how they found you, including visitors arriving from AI-generated answers.

To analyze your site speed, enter your URL, click “Analyze,” and Google will return:

- A speed score (out of 100) for both mobile and desktop
- Specific recommendations to improve performance

![Google Page Speed Insights showing a performance score along with recommendations to improve performance.](https://static.semrush.com/blog/uploads/media/52/73/527391c6709110d8627cace516bc049d/4afaf436d508f039d10d176a181eb018/image.jpeg)

Work with a developer to resolve major issues causing delays. Then tackle the rest.

And don’t stress about achieving a perfect score from PageSpeed Insights. If you get your score to the mid-80s, you're usually in great shape. I haven’t seen noticeable SEO gains from pushing scores much higher than that.

### 6. Check Core Web Vitals

Google uses the [Core Web Vitals](https://www.semrush.com/blog/core-web-vitals/) to measure real-world user experience and to help determine rankings.

The three Core Web Vitals metrics are:

- **Largest Contentful Paint (**[**LCP**](https://www.semrush.com/blog/lcp/)**)**: Measures how long it takes to load the largest element on the page. It should ideally load within 2.5 seconds.
- **Interaction to Next Paint (**[**INP**](https://www.semrush.com/blog/google-inp/)**)**: Measures how long it takes for a site to respond to user interactions. Aim for less than 200 milliseconds.
- **Cumulative Layout Shift (**[**CLS**](https://www.semrush.com/blog/cumulative-layout-shift/)**)**: Measures how much the layout of the page shifts unexpectedly for the user. A score of less than 0.1 is ideal.

Sites that score well across all Core Web Vitals typically have better engagement metrics (longer time on site and lower bounce rates) than those that don’t meet these benchmarks.

Check Core Web Vitals performance in [Google Search Console](https://search.google.com/search-console/about) from the sidebar menu.

![Google Search Console with "Core web vitals" clicked on the sidebar menu.](https://static.semrush.com/blog/uploads/media/ae/28/ae28f76ddc348d4570edb0ee6c88cde9/753cab7ee28763838bc3285ea839f14f/image.jpeg)

Here, you'll find separate reports for “Desktop” and “Mobile.” Click “**Open Report**” at the top of either chart for more details.

![Core web vitals on Google Search Console showing reports for desktop and mobile.](https://static.semrush.com/blog/uploads/media/b5/79/b57954c146da183c0d30dd661fc7228d/d062a17fe6e1f26c21ea6fdc5e79b589/image.jpeg)

The Google Search Console reports label pages as "**Good**," "**Need improvement**," or "**Poor**." Click each rating to see the affected pages.

![Core web vitals report on GSC categorizing pages as poor, need improvement, or good.](https://static.semrush.com/blog/uploads/media/50/1e/501e4cae692d424f4cca58654e49952a/130c97b798a0d650bda557fbd98a3736/image.jpeg)

To fix the issues affecting your Core Web Vitals performance, take these steps:

- **For LCP issues**: Optimize the hero image and other elements that load [above the fold](https://www.semrush.com/blog/above-the-fold/), improve server response times, and eliminate render-blocking resources like unnecessary CSS or JavaScript files
- **For INP concerns**: Minimize JavaScript execution time, optimize event handlers, and remove unnecessary third-party scripts
- **For CLS problems**: Always specify width and height attributes for images and videos and use fixed-sized containers for dynamic content like ads

Core Web Vitals optimizations are highly technical. So consider working with a developer who can analyze each page, implement the fixes, and thoroughly test the changes.

### 7. Crawl your site for technical errors

Run a full site crawl to identify technical issues affecting your site’s performance.

Start with the [Page Indexing report](https://support.google.com/webmasters/answer/7440203?hl=en) (under “Indexing” in the left sidebar) in GSC. This shows which pages are indexed, which aren’t, and why.

Look for:

- **Pages marked as “Crawled – currently not indexed”** (Google can access the page but chose not to index it—often due to low quality, thin content, or unclear value)
- **“Discovered – currently not indexed”** (Google knows the page exists but hasn’t crawled it yet—this can indicate crawl budget issues or low priority)
- **“Blocked by robots.txt”** (the page is being intentionally or accidentally blocked from crawling—check your robots.txt rules)
- **“Alternate page with proper canonical tag”** (Google sees this as a duplicate and is indexing a different version—usually fine unless the canonical is incorrect)
- **“Duplicate without user-selected canonical”** (Google found similar pages but you haven’t specified which one should be indexed—add a canonical tag to clarify)

These statuses often reveal crawl, duplication, or indexing problems that need attention.

![Page indexing report on GSC categorizing pages as indexed or not indexed along with a "Why pages aren't indexed" widget.](https://static.semrush.com/blog/uploads/media/d6/be/d6be03e4073f68166b189d513c132c76/6f1cb0b8823d1a9368e2db04eb125119/image.jpeg)

Next, use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289?hl=en) to analyze specific pages. Enter a URL and review:

- Whether the page is indexed
- Crawl status
- Canonical selection
- Last crawl date
- Any detected enhancements or issues

This helps confirm whether Google is accessing and interpreting your content correctly.

![URL Inspection report on GSC showing if a URL is indexed on Google along with indexing details.](https://static.semrush.com/blog/uploads/media/f9/01/f901b2471fcc8d632abb162dad5ae1ed/4c517bbebca11f9377874e43b0d4ae57/image.jpeg)

This is a solid start, but if you’re serious about SEO, I recommend using a dedicated SEO crawling tool.

Semrush’s [Site Audit](https://www.semrush.com/siteaudit/) tool is my personal favorite, as it checks for over 140 technical issues—making it one of the most comprehensive solutions in the industry.

To get started, create a project in the tool and [configure the audit](https://www.semrush.com/kb/539-configuring-site-audit).

![Site Audit configuration settings along with "Start audit" clicked.](https://static.semrush.com/blog/uploads/media/9a/c2/9ac29a4408ecc174bdd914ff9580af2f/b1e780ea9559a46404f41edf6e58d985/image.jpeg)

Then, click “**Start Site Audit**.”

When the audit is done, you'll get an SEO audit report that displays your “**Site Health**” score. It’s an overall indicator of your website’s SEO health that’s based on the number and severity of issues found.

![Site Audit Overview with the "Site Health" score highlighted.](https://static.semrush.com/blog/uploads/media/0e/26/0e26fd9f9fcf321a4eb4e44bc95d6f5f/0cd3b1a5f1dbb37c3e8ed727f1bf876b/image.jpeg)

Common errors include:

- **Broken internal links**: Links pointing to non-existent pages, causing 404 errors
- **Redirect loops and chains**: Multiple redirects that create cycles or unnecessarily long chains
- [**Orphan pages**](https://www.semrush.com/blog/orphan-pages/): Pages that aren’t linked to from other pages on your site, making them hard for search engines to find
- [**Sitemap**](https://www.semrush.com/blog/website-sitemap/) **issues**: Some incorrect pages were found in your sitemap (a file on your website that contains a list of all your important pages)
- [**Duplicate content**](https://www.semrush.com/blog/duplicate-content/): Similar or identical content accessible through different URLs, which can confuse search engines

Click “**How to fix”** for explanations and instructions for addressing any issue.

![Site Audit Issues with "How to fix" next to an error clicked showing more information about the issue.](https://static.semrush.com/blog/uploads/media/a9/63/a963deb3bfd047b002bf3fc3365eb6d8/fe118acd91ed620efa26936a2f0843da/image.jpeg)

If you need help, see [our guide to setting up a Site Audit](https://www.semrush.com/kb/1184-audit-your-website).

### 8. Validate structured data

Check that your key pages have correct, present structured data (also known as [schema markup](https://www.semrush.com/blog/schema-markup/)).

Validate a single URL with Google's [Rich Results Test](https://search.google.com/test/rich-results) or our free [website audit](https://www.semrush.com/siteaudit/). For site-wide schema monitoring, use Semrush Site Audit.

Structured data labels important information on your pages, such as products, FAQs, reviews, and step-by-step instructions, so search engines and AI systems don’t have to guess what something means.

When implemented correctly, it can make your pages eligible for rich results in search and improve click-through rates.

Clear schema markup also makes it easier for AI systems to extract and reference details about your brand, products, and expertise.

Start by checking whether schema is present on important pages.

Enter your URL into the Rich Results Test to see which structured data types are detected and whether there are errors.

![Rich Results Test showing which structured data types are detected for a page.](https://static.semrush.com/blog/uploads/media/15/f0/15f0b5c6462ca45e272bf107b30addcb/abb8b11a38285892cecbf4dbc7c72f3f/image.jpeg)

Next, make sure your schema is valid and matches what’s visible on the page.

If you mark up FAQs that aren't actually shown to users, or include misleading product data, you risk losing eligibility for rich results or even receiving a manual action.

The most common schema types I see during audits include:

- FAQ schema for question-and-answer sections
- HowTo schema for step-by-step guides
- Product schema for ecommerce pages
- Article schema for blog content
- [Review schema](https://www.semrush.com/blog/review-schema/) for ratings and testimonials

Product schema is especially important for ecommerce sites. It helps search engines understand pricing, availability, SKUs, and review data.

And, as more people use AI systems to compare products and make decisions directly in search, clear product markup becomes even more valuable.

As agentic commerce grows (where AI-powered systems research, compare, and even purchase products on behalf of users), clean product schema becomes essential. These AI agents rely on structured data to understand pricing, availability, and reviews accurately enough to make recommendations or complete transactions.

If your product details (like price, availability, and reviews) are structured properly, AI platforms are more likely to understand and accurately present your information.

Finally, I’ll run a crawl in Site Audit to identify pages missing structured data or containing implementation issues.

![The Markup report on Site Audit showing pages with markup, pages by markup type, and structured data by pages.](https://static.semrush.com/blog/uploads/media/4b/51/4b51abf8491f9122101ead44984936b3/b5650b1727b4109cf6d7054977f65768/image.jpeg)

Structured data won’t guarantee rich results or AI citations, but it removes ambiguity. And in search (especially AI search), clarity matters.

### 9. Analyze your organic traffic

Start in [Google Search Console](https://search.google.com/search-console/about) to review your clicks, impressions, and traffic trends, and then cross-reference with GA4 for deeper behavioral insights.

[Organic traffic](https://www.semrush.com/blog/organic-traffic/) (visits from unpaid search results) is one of the most important metrics for measuring SEO success.

In GSC, go to **Performance** to view clicks, impressions, and overall trends.

![The "Performance" report on Google Search Console showing clicks, impressions, CTR, and position metrics.](https://static.semrush.com/blog/uploads/media/85/22/85227b971a0ba50333be270dbfb4da74/18ce1a91a410307f6fe3bd975a17cc9d/image.jpeg)

The **Clicks** metric shows how many visits you’re getting from Google Search, including traditional listings and AI-driven features like AI Overviews and AI Mode (though most clicks still come from standard results).

![The "Performance" report on Google Search Console with "Total clicks" selected.](https://static.semrush.com/blog/uploads/media/f8/7b/f87b3391d77180f3dac81a88a3ad9fae/d5d4b16d255309958c11796eb10cb6a0/image.jpeg)

To analyze trends, click the date filter at the top and compare time ranges. I typically compare the last 28 days to the previous period or compare year-over-year performance to spot larger shifts.

Look for:

- Sudden drops
- Gradual declines
- Sharp spikes
- Rising impressions with flat or declining clicks

If clicks are down but impressions are steady or rising, that can indicate increased SERP competition, or the presence of an AI Overview reducing click-through rates.

When AI Overviews (AIO) appear in the SERP, users may get answers without clicking. That can lower clicks even if your content is being surfaced or referenced. This is why tracking AI visibility is becoming just as important as tracking traditional rankings.

On the other hand, if impressions are rising and direct or branded traffic is increasing, that can actually be a positive signal. It may indicate growing brand awareness—even if click-through behavior is changing.

Now switch to [Google Analytics 4](https://developers.google.com/analytics) (GA4) for deeper behavioral insights.

In GA4, go to:

**Reports → Acquisition → Traffic acquisition**

Then filter the session default channel group to “Organic Search.”

![Traffic acquisition report on Google Analytics showing data for "Organic Search".](https://static.semrush.com/blog/uploads/media/4e/0d/4e0de0d5528fb49e4508c36eb2dd6890/159918077bb74177f27560547ec4ee34/image.jpeg)

Here, review:

- Sessions
- Engagement rate
- Average engagement time
- Conversions

Use the date comparison feature in the top-right corner to compare time ranges, just like in GSC. If organic sessions are stable but engagement is dropping, that may indicate UX or content quality issues.

You can also compare performance by device (mobile vs. desktop) to spot usability gaps.

![The "Tech details: Platform" report on GA4 showing performance on Android, iOS, web.](https://static.semrush.com/blog/uploads/media/5b/41/5b41e3ef2e27204b8f476babe24e8faf/9c18220a58961a4eb2fedc309785211c/image.jpeg)

If you notice significant drops in organic traffic, identify what might have caused them. Sharp or sustained traffic declines are often caused by:

- [Algorithm updates](https://www.semrush.com/blog/google-algorithm-update/)
- Manual actions
- Major SERP changes (like expanded AI Overviews or new AI Mode rollouts)

Google updates its algorithm regularly. Most updates are minor, but major core updates can significantly impact rankings. Google typically announces these on its [Search Central Blog](https://developers.google.com/search/blog).

If you notice a significant traffic drop, it may be related to a Google algorithm update or broader changes in the search results. Check Google’s Search Central Blog for recent updates and compare timelines.

Also [check for manual actions in GSC](https://support.google.com/webmasters/answer/9044175?hl=en) under **Security & Manual Actions → Manual actions**. If any issues appear, you’ll need to resolve them and request reconsideration.

!["No issues detected" message on the Manual actions report of GSC.](https://static.semrush.com/blog/uploads/media/0b/8f/0b8fd7b0738f722a3d69b19e7272e76c/68c3fd764e6d37c66b6990bddc42c467/image.png)

### 10. Benchmark SEO performance against competitors

Analyzing your competitors can reveal valuable opportunities for improvement: why they're outperforming you, and the structural, authority, and distribution advantages they have.

Start by identifying your top organic competitors.

These aren't always your direct business competitors. They're the sites consistently ranking for the keywords you care about.

You can use Semrush’s [Domain Overview](https://www.semrush.com/analytics/overview/) tool to find competitors based on keyword overlap. Enter your website URL and click "**Search**."

![Domain Overview with "chewy.com" entered as the domain and "Search" clicked.](https://static.semrush.com/blog/uploads/media/10/14/1014040842851e4a060a199898d245e0/b5cb912d216d42d59318b15c3bfc49dc/image.jpeg)

Scroll down and you’ll see the “**Main Organic Competitors**” section. This is a list of domains who rank for similar keywords to your domain.

![The Main Organic Competitors” section on Domain Overview.](https://static.semrush.com/blog/uploads/media/5a/00/5a003f83850e76ae179d309a17776f71/2d886da43144cbc78b7b25e8e4c7a632/image.jpeg)

Once you’ve identified key competitors, look closely at how their top-ranking pages are built.

Go beyond keywords and study their structure:

- What topics do they cover that you don’t?
- How comprehensive are their guides?
- How are their pages organized?
- Do they use comparison tables, templates, tools, or interactive elements?
- Are they answering multiple related search intents on a single page?

Often, competitors win because their pages are more complete, better structured, and more helpful.

But sometimes, competitors win because they have better [backlinks](https://www.semrush.com/blog/what-are-backlinks/). So next, I would compare backlink profiles.

Use Semrush’s free [Backlinks](https://www.semrush.com/analytics/backlinks/) tool to evaluate total referring domains, link growth trends, authority distribution, and topical relevance.

![Backlink report showing data like referring domains, backlinks, visits, traffic, and outbound domains.](https://static.semrush.com/blog/uploads/media/a7/87/a787a95a5ed261b4f92445b0d8390940/6a05dbf78c39aa26701c2b4c39074873/image.jpeg)

Don't just look at quantity. Look at quality and relevance.

Where are they earning links from? Industry blogs? SaaS directories? News publications? Research reports? Universities? If competitors consistently earn links from authoritative and relevant sources, that often explains their ability to rank.

Finally, SEO doesn’t exist in isolation. Strong off-site presence increases brand recognition, trust, and authority signals. So, I always evaluate off-site visibility as well.

Search your core keywords and examine the SERPs.

Are competitors appearing on Reddit threads, YouTube videos, industry forums, LinkedIn discussions, or niche communities? Are they being cited in roundups or mentioned in trusted publications?

![Google SERP showing a brand, "Photoshop", with mentions on a roundup by a publication, a YouTube video, and on their own site.](https://static.semrush.com/blog/uploads/media/20/ae/20ae396d1d4a2a462392e4d7c93f583c/56fa10727597b8df92c381abebd1459b/image.jpeg)

After reviewing content, backlinks, and off-site presence, step back and identify the two or three biggest gaps between you and your top competitors.

These usually fall into one of three categories:

- A **content gap**, where they cover topics more comprehensively or structure pages more effectively.
- An **authority gap**, where they have stronger or more relevant backlinks.
- A **distribution gap**, where they have greater visibility across third-party platforms and communities.

You don’t need to fix everything at once. Prioritize the gap that will drive the fastest results.

### 11. Find keywords and prompts you're missing out on

Identifying keyword gaps is one of the fastest ways to uncover growth opportunities.

You can find competitors' keywords with Semrush's [Keyword Gap](https://www.semrush.com/analytics/keywordgap/) tool. Just enter your domain and the domains of your competitors.

![Keyword Gap tool with two competing domains entered and "Compare" clicked.](https://static.semrush.com/blog/uploads/media/32/7d/327dfbef99bd28204689d6b49af786b8/3e7e33f8b877b960efdf555641846090/image.jpeg)

After you click “**Compare**,” Keyword Gap will compare the sets of keywords the analyzed domains are ranking for in traditional search results.

Scroll down to the list of keywords and take a good look at the “**Missing**” and “**Weak**” tabs:

- **Missing**: Keywords the analyzed competitors rank for but you don't
- **Weak**: Keywords the analyzed competitors rank for higher than you

![Keyword Gap report with the "Missing" and "Weak" tabs highlighted.](https://static.semrush.com/blog/uploads/media/ac/76/ac766e90f3a17d1c193a254b9e749338/1318a178827cdb3ca6ae580b54ebbf05/image.jpeg)

But don’t think of this step as “keywords only.”

Modern SEO is about topics, not isolated phrases.

Instead of asking, “What keywords am I missing?” ask, “What topics are my competitors covering that I’m not?”

For example, if a competitor ranks for multiple variations of "technical SEO audit," that likely signals they've built a comprehensive [topic cluster](https://www.semrush.com/blog/topic-clusters/). The cluster probably covers subtopics like crawl depth, internal linking, schema validation, and site speed. If you only have one surface-level article, you may need to expand it or create supporting content.

To explore topics more deeply, use Semrush’s [Topic Research](https://www.semrush.com/topic-research/) tool. Enter a topic and click “**Get content ideas**” to see:

- Related subtopics
- Popular headlines
- Frequently asked questions
- Related ideas and angles

![Topic Research tool start with "seo audit" entered and "Get content ideas" clicked.](https://static.semrush.com/blog/uploads/media/22/4c/224c544ceb2f5123b0626b9d4951fdeb/6cbe8e2fe7dfcfc13cf1938c5d911a39/image.jpeg)![Topic Research tool showing a list of related content ideas based on a seed term.](https://static.semrush.com/blog/uploads/media/8b/3a/8b3a9a4f98c6266c7bd38b757ccf2b14/aaf7d7c1ef85367c75c53c2752424bf5/image.jpeg)

This helps you build pages that fully cover search intent rather than targeting a single phrase.

During my SEO audits, I also pay close attention to [long-tail](https://www.semrush.com/blog/how-to-choose-long-tail-keywords/) and conversational queries.

Search behavior is shifting toward natural language searches and AI-style prompts. For example, instead of typing “seo audit checklist,” users might search:

- “How do I run an SEO audit for a small construction website?”
- “What’s included in a technical SEO audit for a dentist’s website?”
- “How long does it take to do an SEO audit for a client?”

These longer queries often have lower competition and clearer intent.

You can uncover these using the [Keyword Magic Tool](https://www.semrush.com/analytics/keywordmagic/). Filter by “**Questions**” to surface conversational queries and natural language searches.

![Keyword Magic Tool with "Questions" selected showing question-based keyword ideas.](https://static.semrush.com/blog/uploads/media/d6/0b/d60bfa3e30829036e36f27a26cc30649/fae53f066ec31afb5c30798062b835ee/image.jpeg)

For an even deeper look at how people are searching through AI platforms specifically, use Semrush’s [Prompt Research](https://www.semrush.com/ai-seo/prompt-research/) tool. Think of it as keyword research for AI. It shows you the actual prompts and topics people are asking AI platforms, along with volume, difficulty, and which brands are being mentioned.

Enter a topic to see related AI prompts, then identify gaps where your brand isn’t showing up but should be.

![Prompt Research showing data like topics, prompts, intent, brands mentioned, and source domains.](https://static.semrush.com/blog/uploads/media/dd/ba/ddbad21eae4c9db4083f957d7dccd923/ee4cd09ab5fc010b4e8bdae778d01858/image.jpeg)

Optimizing for long-tail and topic clusters does two things:

1. It increases your chances of ranking for multiple variations of a theme.
2. It improves your chances of being cited in AI-generated responses, since AI systems often synthesize answers from well-structured, comprehensive content.

The goal is to identify the most valuable topic gaps and build content that fully satisfies user intent across traditional *and* AI search.

### 12. Check for duplicate content and keyword cannibalization

Cleaning up [keyword cannibalization](https://www.semrush.com/blog/keyword-cannibalization-guide/) strengthens your authority, stabilizes rankings, and makes your content structure easier for both traditional and AI search systems to interpret.

Cannibalization happens when multiple pages on your site target the same keyword and search intent. Instead of strengthening your visibility, those pages split authority and confuse search engines about which URL should rank.

To fix this, start by looking for pages that cover very similar topics. Ask yourself:

- Do I have multiple blog posts targeting the same phrase?
- Have I published updated versions of older content without consolidating them?
- Do category pages and blog posts overlap in intent?
- Are similar service pages targeting the same keyword in different ways?

To help answer these questions, I check Google Search Console to see whether multiple URLs are ranking for the same query. In GSC, click “**Search results**” in the Performance section.

![Google Search Console with "Performance" selected from the sidebar menu.](https://static.semrush.com/blog/uploads/media/41/2c/412cc19bc29852a00e7568ae055735dc/ee95f1e7001a762884399e36145e574a/image.jpeg)

Click on a query you care about. This will take you to the “Pages” tab.

If you see multiple URLs receiving impressions or clicks for the same query, that’s often a sign of cannibalization.

![The "Pages" tab on the Performance report of GSC showing multiple URLs receiving impressions for the same query.](https://static.semrush.com/blog/uploads/media/1f/31/1f3133f40c58de5206aa9bcbad81f751/c6aef7ea4c01a317810c413457bd7399/image.jpeg)

This doesn’t always mean there’s a problem. But if those pages target the same [intent](https://www.semrush.com/blog/keyword-intent/), you may need to consolidate or differentiate them.

Another issue to look for is true [duplicate or near-duplicate content](https://www.semrush.com/blog/duplicate-content/).

Run a crawl in [Site Audit](https://www.semrush.com/siteaudit/) and check the “**Issues**” tab for duplicate [title tags](https://www.semrush.com/blog/title-tag/), duplicate [meta descriptions](https://www.semrush.com/blog/meta-description/), and duplicate content warnings.

![Site Audit Issues with "duplicate" entered showing a list of duplicate content issues.](https://static.semrush.com/blog/uploads/media/dc/cd/dccd4cf57c70726a81d1506561e79485/024566777e2eaf5f6a6936e3f1f8d99f/image.jpeg)

Duplicate content often happens when:

- [HTTP and HTTPS](https://www.semrush.com/blog/http-vs-https/) versions both exist
- Trailing slash variations (e.g., example.com/page and example.com/page/) are indexed
- Filtered or [parameter URLs](https://www.semrush.com/blog/url-parameters/) create similar versions of pages
- Content is reused across multiple pages with minimal changes

If you identify cannibalization or duplication, your options typically include:

- [Merging similar pages](https://www.semrush.com/blog/content-pruning/) into one stronger resource
- [Redirecting](https://www.semrush.com/blog/301-redirects/) weaker pages to the primary version
- Rewriting content to target distinct intent
- Adding [canonical tags](https://www.semrush.com/blog/canonical-url-guide/) where appropriate

The goal is clarity.

Each important keyword or topic should have one clear, authoritative page representing it. When search engines see multiple competing versions, they have to choose. And they don’t always choose the one you want; so choose for them.

### 13. Check your site's on-page SEO

On-page SEO helps search engines and AI understand your content and surface it for relevant queries.

On-page SEO elements include:

- [Title tags](https://www.semrush.com/blog/title-tag/)
- [Meta descriptions](https://www.semrush.com/blog/meta-description/)
- [Header tags](https://www.semrush.com/blog/header-tag/) (H1, H2, etc.)
- [URL slugs](https://www.semrush.com/blog/what-is-a-url-slug/)

While these elements might seem basic, I'm consistently surprised how frequently websites get these fundamentals wrong.

You can use Semrush's [On Page SEO Checker](https://www.semrush.com/on-page-seo-checker/) to audit your on-page elements at the click of a button.

To start, [set up a project](https://www.semrush.com/kb/563-configuring-on-page-seo-checker) for your website, then let the On Page SEO Checker analyze your site. When it’s done, you’ll see a list of pages with recommendations for each.

![Optimization Ideas on the On Page SEO Checker.](https://static.semrush.com/blog/uploads/media/7a/02/7a02f7ba60e2303f163db6d8505ae0bc/382206d5d1d6584672e46418bd7c2803/image.jpeg)

Implement the on-page SEO recommendations to help your pages perform better.

![Content optimization ideas for a page on the On Page SEO Checker.](https://static.semrush.com/blog/uploads/media/c0/6f/c06fa4ccdc18737ad3fba1acd1d9c6df/c5d3d1a2da6e61bd55d7e7ea713edfde/image.jpeg)

Alternatively, you can review the source code to manually check pages individually. Open it in the Google Chrome browser, right-click, and choose “**View Page Source**.”

!["View Page Source" selected from the menu after right-clicking a page on Google Chrome.](https://static.semrush.com/blog/uploads/media/e2/95/e2951a2852f1edc5b70c8bcca2f07ab4/da096963cac73ef85e170593972a25e9/image.jpeg)

When inspecting a page on your site, look for:

- A concise title tag (under ~55 characters) that includes your main keyword
- A unique meta description (~105 characters) that accurately summarizes the page
- A single H1 tag that clearly communicates the main topic
- Subheadings (H2s, H3s, etc.) used logically to structure the content
- Descriptive [alt text](https://www.semrush.com/blog/alt-text/) for all images that add meaning to the content
- Clean, descriptive, and keyword-rich URL structures

### 14. Review content quality

Not every ranking issue is technical. Sometimes the content just isn’t strong enough.

Start by checking if your content matches [search intent](https://www.semrush.com/blog/search-intent/) (a user’s main goal when they enter a query into a search engine). To do this, search your target keyword(s) and study the top results.

Focus on your most important pages first. In [Google Search Console](https://search.google.com/search-console/about) the “Search results” report shows which pages are getting the most impressions and clicks.

Sort pages by impressions, then identify pages with:

- High impressions but low clicks (click-thru rate issue)
- Declining clicks over time
- Stable impressions but dropping average position

![The "Pages" tab on the Performance report of GSC with pages sorted by impressions.](https://static.semrush.com/blog/uploads/media/1d/b8/1db8453d9693f4f8101e9577759f90bb/07e7decf681c854fc925038b5d402c7f/image.jpeg)

Next, switch to [GA4](https://developers.google.com/analytics). Go to **Reports → Engagement → Pages and screens**. Filter by organic traffic.

Look for pages with:

- Low engagement rate
- Short average engagement time
- High exit rates
- Low conversion rate (if applicable)

![The "Pages and screens" report on GA4 showing page-level data like views, active users, engagement time, and event count.](https://static.semrush.com/blog/uploads/media/2e/67/2e670b82c369eebad962470de1010af8/c9ee7773ca129d416e467340006448c6/image.jpeg)

This tells you how users behave after landing on the page. If traffic is steady but engagement is weak, the issue is likely content quality or UX, not rankings.

Next, I like to cross-check in Semrush. Use [Position Tracking](https://www.semrush.com/position-tracking/) to see:

- Pages losing keyword positions
- Keywords slipping from page 1 to page 2
- Competitors overtaking you

![Rankings Overview on the Position Tracking tool showing declining keyword positions.](https://static.semrush.com/blog/uploads/media/e7/db/e7db58242ef6d98f5af3206e38743448/fb8e8d6321f38f5d4637ae99fc47e8bb/image.jpeg)

Finally, check your [E-E-A-T](https://www.semrush.com/blog/eeat/).

E-E-A-T stands for Experience, Expertise, Authoritativeness, and Trustworthiness. While it’s [not a direct ranking factor](https://www.seroundtable.com/google-eeat-factors-36879.html), it’s part of [how Google evaluates content quality](https://www.semrush.com/blog/how-does-google-algorithm-work/), especially for topics related to health, finance, or important life decisions.

Today, E-E-A-T is also increasingly relevant for AI visibility. AI systems prioritize content that appears credible, well-sourced, and written by knowledgeable authors.

So, during your audit, check whether your pages demonstrate:

- Real experience or firsthand insight
- Clear expertise from the author
- Credible references or sources
- Transparent author information
- Accurate and up-to-date information

If content lacks these elements, it may struggle to rank or be cited.

When a page fails E-E-A-T, you generally have two options:

1. Improve it by adding original examples, firsthand experience, expert insights, updated data, references, and clear author bios
2. Or, if the page can’t be made valuable, consider merging it into a stronger resource or removing it entirely

And remember: not every page deserves to exist. If you can’t sufficiently improve a page, [deleting it entirely](https://www.semrush.com/blog/content-pruning/) is also an option.

As you’re reviewing your content, decide what to do with each page:

|  |  |
| --- | --- |
| **Situation** | **What to Do** |
| Content is solid but outdated or lacks depth | [**Update the page**](https://www.semrush.com/blog/when-to-update-blog-content/). Add new sections, examples, data, visuals, and stronger internal links |
| Search intent is mismatched or the page lacks unique value | **Rewrite the page**. Align it with what’s currently ranking and improve clarity, depth, and usefulness |
| Multiple pages target the same keyword or intent | **Merge and redirect**. Combine them into one stronger resource and 301 redirect the weaker URL |
| Page has no traffic, no backlinks, and no strategic value | **Delete or** [**noindex**](https://www.semrush.com/blog/noindex/) it. Not every page needs to stay indexed |

### 15. Benchmark your current AI visibility

Benchmarking your AI visibility means measuring how often your brand appears in AI-generated answers across the platforms and topics you care about.

Start by identifying a small set of important queries or prompts (typically your highest-value keywords or core topics). These might include product comparisons, “best of” searches, or how-to queries related to your niche.

Then check whether your brand is:

- Mentioned in AI answers
- Explicitly cited as a source
- Not present at all

Compare your performance against your competitors.

Run the same queries for two or three competing brands and examine who is cited more frequently, and for which topics. This reveals whether competitors dominate certain subject areas or formats.

If a competitor is consistently cited for “best tools” lists or data-driven research pages, that’s a strong signal about what AI systems prefer when answering those types of prompts.

The easiest way to track this at scale is with Semrush’s [AI Visibility Toolkit](https://www.semrush.com/ai-seo/overview/). Open the tool, enter your domain, and click “**Check AI Visibility**.”

![AI Visibility tool start with "monday.com" entered as the domain and "Check AI Visibility" entered.](https://static.semrush.com/blog/uploads/media/aa/0e/aa0e7e7b45666e21a69579c381449346/656d7910d34a72804ca622d9b439ca9b/image.jpeg)

The tool will show you key metrics, including:

- **AI Visibility Score**: An overall measure of how visible your brand is in AI-generated responses compared to competitors, expressed on a scale out of 100. The higher the score, the better visibility you have.
- **Mentions**: The number of times your brand name has been referenced in AI-generated responses
- **Cited Pages**: Specific URLs from your site that AI platforms have used as sources

![Visibility Overview report showing metrics like AI visibility score, mentions & citations, distribution by LLM, and mentions by country.](https://static.semrush.com/blog/uploads/media/96/c6/96c64446aee2f6cde376952a6031508a/37a0dc8dc3be9fd59a5e7d09670d2f7f/image.jpeg)

Check if your visibility is trending up or down. This helps you understand whether recent optimization efforts are having a positive impact on your visibility.

Look closely at the Cited Pages report to identify which of your URLs are referenced most often.

![The "Cited Pages" tab on the Topics & Sources section of the Visibility Overview report showing a list of referenced URLs.](https://static.semrush.com/blog/uploads/media/13/c4/13c41dd4e1452f5a4aad245df3b8022e/c556a5558337c0ac195d3d9678965447/image.jpeg)

This reveals patterns. You may find that AI platforms favor:

- Comprehensive how-to guides
- “Best of” comparison pages
- Original research
- Clearly structured educational content

Citations matter because they function as a trust signal. When an AI system cites a page, it indicates that the system relied on that source to construct its answer. The more frequently your pages are cited, the more likely your brand becomes the referenced authority for that topic.

There are many tactics you can use to improve AI visibility. We have a dedicated [AI optimization guide](https://www.semrush.com/blog/how-to-optimize-content-for-ai-search-engines/) that outlines specific strategies in more detail.

### 16. See what AI is already saying about your brand (and if it's true)

Check what AI says about your brand, products, or services to spot any errors or misinformation that might mislead potential customers.

Test different AI platforms by entering relevant queries and reviewing how they describe your brand, products, and services. Try queries like:

- "What does [your company] do?"
- "What products/services does [your company] offer?"
- "How much does [your product/service] cost?"
- "Where is [your company] based?"
- "Who founded [your company]?"
- "What are the features of [your product]?"
- "[your company] vs. [competitor]"

Document any instances of the following in AI-generated answers about you:

- **Factual inaccuracies**: For example, incorrect product descriptions or misattributed features
- **Outdated information**: For example, old pricing or discontinued products
- **Incomplete answers**: For example, missing key products, services, or differentiators
- **Competitor confusion**: Your features or accomplishments attributed to competitors (or vice versa)
- **Hallucinations**: Completely fabricated information

If you discover inaccurate information about you in AI-generated answers, find out which sources AI cited to understand where the misinformation lies, and then:

- **Fix inconsistencies on your own properties**: Make sure your website, social media profiles, and business listings all reflect accurate, up-to-date information. AI relies heavily on your primary sources (especially for brand-related queries).
- **Reach out to fix third-party misinformation**: If AI cites external content with outdated or wrong information, contact the authors or site owners, provide them with accurate details, and ask for corrections
- **​​Fill content gaps on your website**: If AI generates vague or incorrect answers because your site lacks specific information, create content to provide that information clearly and fill the gaps.

### 17. Track whether AI connects your brand to key topics

Make sure your brand shows up for the topics your potential customers are asking about.

For example, if you sell project management software but AI only mentions you for queries related to "collaboration tools" and never for queries related to "project tracking" or "project management," you're invisible for those relevant queries.

Semrush's [AI Visibility Toolkit](https://www.semrush.com/ai-seo/overview/) can show you which queries trigger mentions of your brand and which topics you're most strongly associated with.

![Your Performing Topics on the Visibility Overview tool with the "Topics" and "Prompts" tabs highlighted.](https://static.semrush.com/blog/uploads/media/88/af/88aff4b333e7db93561b8f8b892491df/c549bb5da463fb70bfd46f5b5e32ac98/image.jpeg)

If AI doesn't connect your brand to key topics, it's usually because:

- Your website lacks content on those topics
- Your messaging isn’t clear
- Competitors have more authoritative content in that space
- Your content doesn't clearly position you within that category

To start showing up in AI responses in all relevant subjects, create targeted content that establishes your expertise in the missing topic areas.

### 18. Analyze your brand mentions and backlinks

Review your [brand mentions](https://www.semrush.com/blog/brand-mentions/) and backlinks to understand your authority, spot risks, and find opportunities to grow.

There are two types of mentions that both matter for search rankings and AI visibility:

- **Linked mentions**: References to your brand that include a clickable link to your website. These are commonly known as backlinks and pass authority to your site.
- **Unlinked mentions**: References to your brand name without a link. While they don’t pass authority directly, they still reinforce brand recognition and trust signals that AI systems may factor in.

You can also earn backlinks that don’t include your brand name in the anchor text. These are still valuable for rankings and can strengthen overall authority.

Start by analyzing your backlink profile during an audit using Semrush’s [Backlinks](https://www.semrush.com/analytics/backlinks/) tool. Enter your domain and click “**Analyze**.”

![Backlink Checker with "chewy.com" entered as the domain and "Analyze" clicked.](https://static.semrush.com/blog/uploads/media/77/cb/77cb74cc1f22fb25f95852cfa7c64ec6/9174d0be4cca57cf7cd4c0194d911859/image.jpeg)

First, review link quantity and growth trends. Look at the referring domains graph to see how your backlink profile has grown over time.

![The "Referring Domains" widget on the Backlink Checker showing how a backlink profile has grown over time.](https://static.semrush.com/blog/uploads/media/5b/c5/5bc5b63e6dd8c7f3cb50ce66b9e7124d/3f6a36f63f8008912819ebe3d57e7853/image.jpeg)

A steady upward trend is a positive sign. Sudden drops may indicate lost links or site-wide link removals. Flat growth over a long period may suggest you’re not actively earning authority compared to competitors.

If growth has stalled, consider:

- Publishing link-worthy assets (original research, tools, in-depth guides)
- Digital PR campaigns
- Guest contributions on relevant sites
- Reclaiming unlinked brand mentions

I also recommend checking the "**Backlinks**" tab to assess link quality and toxicity. Sort your backlinks by Authority Score to put the lowest quality links at the top:

![Backlinks report showing a list of backlinks sorted by authority score.](https://static.semrush.com/blog/uploads/media/b0/84/b0842befb97d5676b231d275561623e9/566088c857d0de3d9f1e15e454e56ab5/image.jpeg)

It’s normal to have some low-quality links. Every site does. But watch for clusters of spammy directories, irrelevant foreign domains, or [obviously manipulative link patterns](https://developers.google.com/search/docs/essentials/spam-policies).

If you identify clearly toxic links:

- Try contacting site owners to request removal
- Use [Google’s disavow tool](https://support.google.com/webmasters/answer/2648487?hl=en) carefully if removal isn’t possible

Avoid overusing disavow. It should be a last resort for genuinely harmful patterns, and should only be done if you’re confident that the links are spammy.

After that, review niche relevance.

Go to the “**Referring Domains**” tab and analyze where your links come from.

![The Referring Domains report showing a graph of new and lost domains along with a list of referring domains.](https://static.semrush.com/blog/uploads/media/a4/fb/a4fbbf0a986739b04ddd93c96b3758cc/014fd9fff28fcc18f18f6b7e7885ee84/image.jpeg)

Are most links from sites related to your industry? Or are they from unrelated blogs, directories, or random sites?

Topical relevance matters. A smaller number of links from highly relevant industry sites is often more valuable than a large number of unrelated links.

If you see weak relevance overall, focus on [building links](https://www.semrush.com/blog/how-to-get-backlinks/) from:

- Industry blogs
- Trade publications
- Niche communities
- Relevant SaaS or partner ecosystems

Then evaluate [anchor text](https://www.semrush.com/blog/anchor-text/) distribution.

Look at the Top Anchors report to see how other sites link to you.

![The "Top Anchors" widget on the Backlink Checker app showing how other sites link to a domain.](https://static.semrush.com/blog/uploads/media/af/6c/af6c7e8f55c065af82e0c7b4e0487e25/6095c0df36b464291b74c08d5cc94dcd/image.jpeg)

Your anchor profile should look natural. If it’s overly optimized with keyword-heavy anchors, focus on earning more branded and editorial links to balance it out.

Finally, analyze unlinked brand mentions using the [Brand Monitoring](https://www.semrush.com/apps/brand-monitoring/) app. This tool shows where your brand is being discussed online.

![The Brand Monitoring report showing a list of brand mentions across platforms.](https://static.semrush.com/blog/uploads/media/f5/63/f563811a90bfc422a43c11dd422db96f/84cf28f619321e91bc08c0017d9894e2/image.jpeg)

Pay special attention to high-authority sites and communities (like Reddit, Quora, and industry forums) that often surface in search and AI-generated answers.

If you find strong unlinked mentions, consider reaching out and requesting a link.

### 19. Find missing backlink opportunities

Look for backlink opportunities your competitors have capitalized on that you haven't yet to boost your authority.

Sites that link to your competitors are excellent prospects since they've already shown interest in your niche. You can use Semrush’s [Backlink Gap](https://www.semrush.com/analytics/gap/backlinks/) tool to find these sites.

Just enter your domain and the domains of up to four competitors:

![Backlink Gap report with two competing domains entered and "Find prospects" clicked.](https://static.semrush.com/blog/uploads/media/51/a9/51a9cb046bdfa6341799c9b64ff6429a/b170fab19857e77fc951a3b14dc9e181/image.jpeg)

The tool will show a list of domains that link to the analyzed competitors but not to you:

![Backlink Gap report showing a list of domains linking to a domain's competitor but not to the domain itself.](https://static.semrush.com/blog/uploads/media/86/8d/868de8b0c6e1e1fb408b683f10727348/0a3a492c7ff09cd078d7a785d8d5d9da/image.jpeg)

The domains shown in Backlink Gap are much more likely to link to your website since they're already linking to similar websites (your competitors).

Click the arrow next to the number of backlinks from a domain to expand the view. You'll see the specific pages that link to your competitors, along with the anchor text and target URLs.

![The specific pages linking to a competitor along with the anchor text and target URLs.](https://static.semrush.com/blog/uploads/media/96/e9/96e9ad7749ec905ed4384a917741c386/1ac44dc8cc54271a6a3a91b119c20e05/image.jpeg)

Now, you can try to replicate these backlinks. Select the ones that are relevant to your website and click the "**Start outreach**" button in the top-right corner. Semrush will send the selected prospects to the [Link Building Tool](https://www.semrush.com/link_building/), where you can set up a new project for your domain.

![Link Building prospects with a domain selected and "Start outreach" clicked.](https://static.semrush.com/blog/uploads/media/cd/a9/cda9ebfc02e451a4bed860d924f1476e/2e59ce5bf57be5a5752d626c9498b5a3/image.jpeg)

The Link Building Tool will help you:

- Find even more backlink prospects from various sources
- Reach out to the domain owners and ask them for backlinks
- Keep track of the progress of your outreach campaigns

![Link Building tool showing domains prospects, domains in progress, and monitored domains.](https://static.semrush.com/blog/uploads/media/90/a1/90a1a96d4bbf6072dfd7313a4b15c08f/a41dfc2e1e39829deb9bd55e0f7a9d4b/image.jpeg)

Another powerful tactic is [broken link building](https://www.semrush.com/blog/broken-link-building/).

Sometimes competitors earn links from pages that later become unavailable or return a 404 error. If a site is linking to a broken competitor page, that’s an opportunity for you to step in with a working, relevant alternative.

To find those opportunities, use the [Backlinks](https://www.semrush.com/analytics/backlinks/) tool and enter a competitor’s domain.

Go to the "**Indexed Pages**" report and check off "**Broken Pages**." You're looking for competitor pages that are being linked to but no longer exist.

![The "Indexed Pages" report with "Broken Pages" selected.](https://static.semrush.com/blog/uploads/media/b4/59/b4598e4dea5af495e1ef07480e31e379/9217f8ca2bb9becaf351279f2e1fc097/image.jpeg)

Finally, review which domains are linking to those broken pages. These linking sites may not realize they’re sending users to a dead resource.

If you have a similar (or better) page covering the same topic, you can reach out and suggest your page as a replacement.

If your own site has 404 pages with backlinks pointing to them, prioritize fixing those first. Either restore the content or implement a 301 redirect to the most relevant page. This helps you reclaim lost authority immediately.

To learn more, check out this guide on [how to start a link building campaign](https://www.semrush.com/kb/843-how-to-start-a-link-building-campaign) with the Link Building Tool.

### 20. Check your presence in SERP features

Appearing in [SERP features](https://www.semrush.com/blog/serp-features-guide/) can significantly impact your visibility and click-through rates.

SERP features are the special search result formats that appear on the search results page. These include:

- [Featured snippet](https://www.semrush.com/blog/featured-snippets/): A concise answer displayed near the top of the search results
- [People Also Ask (PAA)](https://www.semrush.com/blog/people-also-ask/) box: A box that shows related questions and answers
- [AI Overviews (AIO)](https://www.semrush.com/blog/ai-overviews/): AI-generated summaries that synthesize information from multiple sources
- AI Mode responses: Conversational, AI-driven search experiences
- [Image pack](https://www.semrush.com/kb/1337-serp-features-images): A group of images that appears in the search results
- Video snippets: Video results that appear prominently, often with key moments highlighted
- [User-generated content (UGC)](https://www.semrush.com/blog/user-generated-content/): Results from platforms like Reddit, forums, and Q&A sites
- [Local pack](https://www.semrush.com/blog/google-local-pack/): A map with local business listings
- Shopping and ecommerce features: Product listings, reviews, pricing, availability, and merchant panels

These are some of the most common SERP features, but Google regularly introduces new formats and layouts.

To check how often you appear in SERP features, use Semrush's [Position Tracking](https://www.semrush.com/position-tracking/) tool to [set up a project](https://www.semrush.com/kb/548-configuring-position-tracking) for your domain. Then wait for the tool to collect data on your rankings.

Once the data is collected in Position Tracking, go to the “**Overview**” tab. Here, you can see which SERP features appear for your target keywords and whether your site is featured in them.

![Rankings Overview on the Position Tracking tool showing SERP features for a keyword along with the ranking position.](https://static.semrush.com/blog/uploads/media/e8/f2/e8f25ada870a9d1a40fecad42afd527e/d11a01aee140e75320e6c395843e4184/image.jpeg)

Pay special attention to features that significantly reduce traditional click-through rates, such as AI Overviews and Featured Snippets. If your site is not being surfaced in these areas, you may still rank organically but receive fewer clicks.

For ecommerce sites, also check whether your products appear in shopping results. Missing product schema, incomplete pricing information, or weak reviews can prevent eligibility for these features.

Once you know which SERP features you're missing, take action:

- **For Featured Snippets and PAA**: Structure content with clear headings and provide direct, concise answers immediately below them
- **For AI Overviews and AI Mode**: Focus on well-structured, authoritative content that clearly answers common questions. Use FAQ and HowTo schema where relevant, include clear source attributions, and consolidate topic clusters so AI systems can find your most authoritative page per topic.
- **For rich results**: Add and validate structured data (e.g., FAQ, HowTo, Product schema)
- **For video snippets**: Create helpful video content and optimize titles, descriptions, and timestamps
- **For shopping features**: Ensure product data is complete (price, availability, reviews) and properly marked up

## SEO audit FAQs

### How often should you do an SEO audit?

At minimum, perform a full SEO audit once or twice per year.

For most sites, it’s better to run lighter audits quarterly and monitor key issues (like technical errors and traffic drops) on an ongoing basis. If you publish content frequently or run an ecommerce site, more frequent audits can help you catch issues early.

### How long does an SEO audit take?

A basic SEO audit can take a few hours, while a comprehensive audit may take several days.

The exact timing depends on your site size and depth of analysis. Small sites with a few dozen pages can be audited quickly, while large sites with thousands of pages require more time to review technical issues, content, and backlinks.

### Can you do an SEO audit for free?

Yes, you can run a basic SEO audit for free using tools like Google Search Console and Google Analytics.

However, dedicated SEO tools (like Semrush) make the process much faster and easier by automatically identifying issues, prioritizing fixes, and tracking your progress over time.

### What’s the difference between a technical SEO audit and a full SEO audit?

A technical SEO audit focuses on how your site is built—things like crawlability, site speed, indexing, and errors.

A full SEO audit goes further. It includes technical SEO plus content quality, keyword coverage, backlinks, user experience, and visibility in both traditional search and AI-driven results.

### How has AI changed SEO audits?

Modern SEO audits now include AI visibility: whether AI platforms mention, cite, and correctly describe your brand. That means auditing AI crawler access (OAI-SearchBot, PerplexityBot, Claude-SearchBot), benchmarking your brand's presence in AI answers, and checking whether AI systems connect you to your key topics. The technical and content fundamentals still matter, but they're no longer sufficient on their own.

## Putting your SEO audit into action

An SEO audit is just the starting point. The real results come from fixing what you find.

We’ve covered a lot in this guide. Use this simple framework to prioritize:

- **Tier 1 (fix first)**: Crawl and indexing issues, broken pages, and critical technical errors
- **Tier 2**: Content quality, keyword gaps, and pages that drive the most traffic
- **Tier 3**: Backlinks, brand mentions, and AI visibility improvements

Work through issues in that order and track your impact as you go.

Run a free [SEO check](https://www.semrush.com/siteaudit/) to surface what's affecting a page right now.

For ongoing work across your full site, the easiest way to stay on top of this process is with Semrush Site Audit.

It helps you:

- Identify and prioritize issues
- Monitor your Site Health score
- Re-crawl your site to confirm fixes
- Track progress over time

SEO isn't a one-time task, especially in the age of AI search. Run your audit, prioritize your fixes, and keep improving.
