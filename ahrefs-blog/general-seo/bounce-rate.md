---
title: "What Is Bounce Rate? How to Interpret and Work with It"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "bounce-rate"
url: "https://ahrefs.com/blog/bounce-rate/"
canonical: "https://ahrefs.com/blog/bounce-rate/"
author: "Michal Pecánek"
published: "2020-11-03T16:00:22+00:00"
updated: "2023-05-15T07:55:51+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "date_2023_aging"
fetched_at: "2026-06-12T11:19:47+00:00"
status_code: 200
html_hash: "8e3e8337edbe69b3ddf483b4eb220ccc930c7169d7b2387d5f62484eed1093a9"
clean_word_count: 3073
clean_char_count: 18309
---
# What Is Bounce Rate? How to Interpret and Work with It

Bounce rate is the percentage of visitors that take no further action after landing on a website, like clicking through to another page, leaving a comment, or adding an item to their cart.

It’s a great metric to measure user engagement, but only if you know how to use it.

In this article, you’ll learn:

- [How Google Analytics calculates bounce rate](#bounce-rate-calculation)
- [Is bounce rate important?](#bounce-rate-importance)
- [Bounce rate vs. exit rate vs. dwell time](#bounce-rate-exit-rate-dwell-time)
- [How to interpret and use bounce rate](#interpreting-bounce-rate)
- [What is a good bounce rate?](#good-bounce-rate)
- [How to improve your bounce rate](#how-to-improve-your-bounce-rate)

**Spoiler alert:** The last two points are the wrong questions to ask. So, don’t bounce, and find out why.

## How Google Analytics calculates bounce rate

Every page on your website should have your Google Analytics tracking ID in the code. When someone visits your website, this code fires and triggers a session.

If a visitor leaves your site without further interaction, the session expires, and their visit is classed as a bounce. If they click through to another page or perform an action that triggers an event, like filling out a contact form, the code fires again and tells GA that it’s not a bounce.

However, things aren’t always this simple because many things affect if and how the code is fired. Your data is skewed one way or another by:

- **Ad blockers**. These usually prevent tracking codes from firing, so you won’t see these users in your analytics at all.
- **Slow-loading pages**: Impatient users might bounce before the tracking code loads.
- **Session timeouts**: There are [multiple ways](https://support.google.com/analytics/answer/2731565) sessions can expire even if the user plans to engage with the website further.
- **Improper tracking setup**: We’ll look into that later.

## Is bounce rate important?

Bounce rate is an important metric. It’s useful for assessing user engagement and indicating that there might be something wrong with your tracking setup.

But it’s also an overrated and often misused metric. To prove this point, try sorting the campaigns below from best to worst. For simplicity, assume that we spent the same on each of them and that the quality of leads (signups) is equal.

I used to give a slightly more elaborate version of this task to interviewees for marketing positions. Most considered bounce rate when making their decision.

In reality, bounce rate doesn’t matter here. What we care about is ROI. You can tell the ROI by comparing the percentage of users each campaign brought with the respective percentage of sign ups. But we can also calculate the conversion rates:

- **Campaign #1:** 0.07%
- **Campaign #2:** 0.22%
- **Campaign #3:** 0.94%
- **Campaign #4:** 1.03%
- **Campaign #5:** 5.02%
- **Campaign #6:** 0.79%

So, from best to worst: 5 > 4 > 3 > 6 > 2 > 1.

The point here is that campaigns #6 and #1 have the best bounce rates, but they’re terrible at directly converting the users.

## Differences between bounce rate, exit rate, and dwell time

Many people confuse these three metrics, and some even use them interchangeably. So let’s look at how both exit rate and dwell time compare with bounce rate.

### Exit rate

Exit rate shows the percentage of sessions that ended on a particular page.

For example, imagine that three people visit your website, and their sessions look like this:

All of the sessions started on page A, which has a bounce rate of 33%. Both B and C have bounce rates of 0% because no session started on those pages.

The exit rate looks different, though:

The exit rate for page A = 33%
 The exit rate for page B = 100%
 The exit rate for page C = 0%

None of the three visitors exited the site from page C, one exited on page A (from three sessions with A in them), and two exited on page B (from two sessions with B in them).

### Dwell time

[Dwell time](https://ahrefs.com/seo/glossary/dwell-time) is the amount of time between a user clicking on a search result and returning to the [SERP](https://ahrefs.com/blog/serps/). Unlike bounce rate, it’s not a metric you’ll find in Google Analytics. The SEO community created it because it’s thought to be a possible [ranking factor](https://ahrefs.com/blog/google-ranking-factors/).

You can technically set up [custom dwell time tracking](https://www.simoahava.com/analytics/measure-serp-bounce-time-with-gtm/) in GA, but that’s way out of the scope of this article.

## How to interpret and use bounce rate the right way

The rule of thumb with analytics is to know what you’re looking for and then use filters and segments to isolate and investigate that data. And that means looking at data with common traits.

For example, looking at bounce rates for different channels doesn’t make sense because it’s aggregated across all campaigns and landing pages.

Our advice is never to look at bounce rates on aggregated reports like this.

Bounce rates differ from page to page, so you’ll always want to include the landing page dimension into your reports, then choose a channel you want to analyze.

In my case, I went to the **Landing Pages** report (Behaviour > Site Content > Landing Pages), then removed the default “All Users” segment and applied an “Organic Traffic” segment instead:

To narrow things down further, we’ll look for a common trait in the “Landing Page” dimension and exclude statistically insignificant pages. We can do this by filtering for product pages with the word “apparel” in the URL (common trait), and excluding pages with one hundred sessions or fewer (statistically insignificant):

Sidenote.

You can use [Weighted Sort](https://support.google.com/analytics/answer/1042020?hl=en) instead of excluding low traffic pages when possible. It just doesn’t work for segmented reports like this one.

The result is a report where bounce rate analysis makes sense.

Still, it’s important not to get too carried away by your average bounce rate because popular pages skew that number. It’s better to check the median bounce rate, which is 46.78% here (the filtered report has 15 pages, so the 8th page contains the median value).

If a page has a higher than median bounce rates, it may be a sign that:

1. The page needs a better user experience (you’ll learn what to focus on later)
2. Your [title tag](https://ahrefs.com/blog/title-tag-seo/) and/or [meta description](https://ahrefs.com/blog/meta-description/) doesn’t align with your page’s content, so users leave. The same can apply to ad copy for your performance channels.
3. It’s a type of page where people bounce naturally.

Let me expand on the third point.

Imagine that you’re looking up contact information for a company. You Google “{company} contact,” click-through and write an email or call them. The page provided all you needed, yet you most likely bounced.

There are even categories of pages that will naturally generate bounces yet satisfy the user. Think about recipes. You usually look them up when you need them. You probably won’t jump from a carbonara recipe to a pizza dough recipe even if they’re linked together. You only want to cook the pasta.

You always need to think about the actual content on the page and why people land on it. But at the end of the day, you’re still doing quantitative analysis. You’ll get more insights by analyzing actual user behavior. We’ll touch more on the topic of qualitative analysis at the end of this article.

All in all, these tips apply to any metric, not just bounce rate. You need to know how they’re measured, what they really mean, and use them in the right context.

## What is a good bounce rate?

According to the general consensus, a bounce rate of 40 to 60% is considered average so anything below 40% would be good. However, there’s no evidence and reasoning behind those numbers. The reality is that there’s no such thing as a universally good bounce rate.

Bounce rates significantly differ between landing pages and their traffic sources as there are many marketing channels and multiple phases of the [customer journey](https://ahrefs.com/blog/marketing-funnels/).

For example, here’s the performance for Google’s Merchandise Store homepage segmented by marketing channel:

The bounce rates for “google / cpc” and “partners / affiliate” differ by 36 percentage points, or 133%. And there are bigger difference gaps than this, too.

If we look at things the other way around, we can see how landing page bounce rates differ for a particular traffic source:

Here, bounce rates fluctuate between 35% and 85% for “google / organic” on the ten most-visited landing pages.

The takeaway?

Forget about X% being good and Y% being bad. It’s about looking at the data from the right angle, as shown before.

### Why you can have a “bad bounce rate”

No, I’m not contradicting myself. It’s more like “wrong bounce rate” than “bad bounce rate” because data can sometimes be skewed and inaccurate. If you see bounce rates that seem way too high or low, this is probably the case, and you should investigate your analytics setup for [tracking mistakes](https://ahrefs.com/blog/google-analytics-tracking-mistakes/).

Here are just a few common problems:

1. **Duplicate tracking code.** Are all your bounce rates zero or close-to-zero? You almost certainly have an issue with duplicate tracking codes. [Here’s how to fix it](https://ahrefs.com/blog/google-analytics-tracking-mistakes/#missing-duplicate-ga-codes).
2. **Incorrectly set up interaction events.** Events in Google Analytics are interactive by default. If you use them, make sure to switch this off for minor events (e.g., scroll depth tracking). [Learn how to handle events properly here](https://ahrefs.com/blog/google-analytics-tracking-mistakes/#incorrect-interaction-event-setup).
3. **Not firing virtual pageviews on JavaScript-heavy websites.** You need to implement something called virtual pageviews if you don’t want your bounces to be skewed. [Learn more here](https://developers.google.com/analytics/devguides/collection/analyticsjs/single-page-applications#tracking_virtual_pageviews).

## How to improve your bounce rate

It’s a straightforward question, but not the best one to ask. That’s because bounce rate isn’t related to your marketing or business objectives. A better question to ask is how you improve user engagement. After all, the more engaged users are, the lower your bounce rates will be.

Here are seven actionable ways to improve user engagement, experience, and potentially bounce rates:

1. [Give people what they came for](#give-people-what-they-came-for)
2. [Improve your copywriting](#improve-copywriting)
3. [Be mobile-friendly](#be-mobile-friendly)
4. [Moderate your ads, pop-ups and interstitials](#moderate-ads)
5. [Improve your internal linking](#improve-internal-linking)
6. [Improve your site speed](#improve-site-speed)
7. [Focus on everything else related to user experience](#user-experience)

### 1. Give people what they came for

People are impatient. If they don’t feel that your page offers what they were looking for within seconds of landing there, they’ll hit the back button in search of one that does.

Improve your chances of people sticking around by giving them what they want, and fast.

Most recipe sites offer a prime example of what not to do here. Everyone’s there for the recipe, yet bloggers like to give you their life story first. You have to scroll past the history of the dish, a bunch of affiliated products, and a few not-so-humble brags about that time they visited Italy and had the most delicious carbonara ever and, yeah…. bounce!

Use the inverted pyramid method to stop yourself from falling into this trap. Start with the “need to know,” then cover the “nice to know” later.

### 2. Improve your copywriting

If users struggle to read your content easily, they’ll be more likely to bounce. Keep things simple, and don’t feel the need to use fancy words, complex sentences, and other jargon to make your content better. Most people won’t thank you for it.

**Recommended reading:** *[12 Easy SEO Copywriting Tips for Better Content and Higher Rankings](https://ahrefs.com/blog/seo-copywriting/)*

### 3. Be mobile-friendly

Most websites get the majority of their visitors from mobile, so it’s super-important that your site is optimized for smaller screens. That means having intuitive navigation, large font and image sizes, and as little clutter as possible.

Here’s a shameless plug of our own homepage viewed on mobile to show how to do it right:

### 4. Moderate your ads, pop-ups and interstitials

When I see something like this upon loading a page, I bounce right away:

This is the kind of clutter I mentioned in the previous point. It’s especially annoying on mobile, where it occupies most of the screen, and where it’s often near-impossible to hit the “X” button.

If you have these on your site and don’t want to give them up, at least moderate the number of advertisements and trigger the pop-ups and interstitials only after the user has completed specific actions.

For example, if you have a pop-up for your newsletter signup, show it to people only after they’ve consumed some of your content or when they’re about to leave your website. It’ll probably convert better that way too.

### 5. Improve your internal linking

Nobody will keep browsing your website unless you provide them with links to related useful resources. And that’s where [internal linking](https://ahrefs.com/blog/internal-links-for-seo/) comes in.

Internal links are clickable links from one page on a website to another. You’ll see them scattered throughout this post and most others on [our blog](https://ahrefs.com/blog/). They’re not only useful for enticing visitors to consume more content but are also helpful for SEO. Just make sure that you’re interlinking related pages using relevant words and phrases.

You can use the free **Internal link opportunities** report in [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools) to help with this. It scans your site for places where you might be missing relevant internal links.

For example, here, the report suggests that we might want to internally link from our post about [Ahrefs’ unique features](https://ahrefs.com/blog/unique-features-ahrefs/) to our post about [anchor text](https://ahrefs.com/blog/anchor-text/). It even suggests the words we might want to use for the link.

### 6. Improve your site speed

Slow-loading pages can often cause people to bounce. Of course, if a user bounces even before your tags fire, it won’t influence your GA numbers. But getting rid of these “hidden” bounces can be a huge step towards achieving your marketing goals.

[Improving your site speed](https://ahrefs.com/blog/core-web-vitals/) is a big topic on its own. I’ll only list a few things that can eliminate your hidden bounces due to slow page loading times:

- Get a better DNS provider.
- Get a better hosting provider.
- Get a good Content Delivery Network (CDN) if you have a geographically dispersed audience.
- Use [HTTPS](https://ahrefs.com/blog/what-is-https/) in combination with HTTP/2, server push, optimized resources prioritization and TLS 1.3 (all should be available with good hosting providers and CDNs)
- Use compression algorithms like gzip and Brotli (supported by most hosting providers and CDNs)
- [Optimize your images](https://ahrefs.com/blog/image-seo/) and load them only when needed (lazy loading)
- Load your scripts asynchronously with async or defer attributes

As I said, there’s much more to site speed than this. It’s a fairly advanced and technical topic. I’d encourage you to go through our articles ([site speed in general](https://ahrefs.com/blog/core-web-vitals/) /[site speed for WordPress](https://ahrefs.com/blog/speed-up-wordpress/)), test your website, and consult with experts.

Improving site speed can have a great impact on user experience, it will ensure more data in your analytics and it can move the needle in SEO if you have a truly slow website now.

You can use the **Performance** report in free [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools) to get an overview of your website speed metrics:

### 7. Focus on user experience

UX is a marketing discipline on its own. All of the previous points are either part or closely related to user experience.

Creating a website without user input is a lottery. You’re too biased and don’t represent real users. Don’t fall into the trap of thinking that you know your users unless you talk to them on a regular basis. That includes proper user testing.

Besides having people click on your website to provide feedback, there’s also a part of qualitative analysis that you can do on your own. I’m talking about analyzing user behavior via recordings and heatmaps to uncover pain points and bottlenecks. You can use behaviour analysis tools like [Hotjar](https://www.hotjar.com/) or [Smartlook](https://www.smartlook.com/) for this.

One method is to segment user recordings by parameters similar to Google Analytics. Those can be things like “user was in the cart but didn’t check out” or “bounced sessions from page XYZ.”

Another method is to check heatmaps for important pages. You might notice that people click on elements that are not clickable, fail to interact with actual links, don’t flow through the page like you intended to, and so on.

I only scratched the surface here. Take this high-level overview of user testing and behavior analytics as yet another point of direction on your journey for better UX, user engagement and ultimately bounce rates.

## Final thoughts

Don’t get too obsessed with bounce rate. It has its uses, but “trying to improve bounce rate” is rarely a good approach. It’s better to focus on improving UX, as that will usually indirectly improve bounce rate anyway.

We continuously have more data than ever before and working with it properly is one of the most important marketing skills to work on. So, I want to encourage you to get to know the in-and-outs of other analytics aspects as you just did with bounce rate.

Got any questions? Ping me on [Twitter](https://twitter.com/michalpecanek).
