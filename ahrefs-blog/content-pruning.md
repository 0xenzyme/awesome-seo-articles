---
title: "Content Pruning: Why It Works, and How to Do It"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "content-pruning"
url: "https://ahrefs.com/blog/content-pruning/"
canonical: "https://ahrefs.com/blog/content-pruning/"
author: "Ryan Law"
published: "2024-03-27T10:01:33+00:00"
updated: "2024-07-17T12:58:37+00:00"
categories:
  - "Content Marketing"
  - "General SEO"
freshness_reasons:
  - "date_2024_watch"
fetched_at: "2026-06-12T11:25:21+00:00"
status_code: 200
html_hash: "40a528a13baf8e472ac81419ef430006f616efb3a56089db4f70bfaa7e772635"
clean_word_count: 1884
clean_char_count: 11885
---
# Content Pruning: Why It Works, and How to Do It

Content pruning is removing low-relevance or low-quality pages to improve website performance.

Content pruning sounds pretty appealing: delete a ton of content and see your organic traffic improve. But pruning has risks (like deleting useful pages and useful backlinks), and benefits are not guaranteed:

https://twitter.com/timsoulo/status/1757341161327342075?s=20

So how does pruning actually work? And when is the risk worth it?

## How content pruning works (with real examples)

There are a few mechanisms through which content pruning might improve your website performance:

### Pruning pages can help make better use of your crawl budget

Google allocates a certain amount of time and resources to crawling a website, known as [crawl budget](https://ahrefs.com/blog/crawl-budget/). On really big websites, it’s possible that some pages won’t get crawled (and appear in search) because your crawl budget just isn’t big enough.

In these cases, content pruning could allow you to make better use of your crawl budget. By pruning content that you don’t want indexed, you’re reducing the total amount of pages that need to be crawled and increasing the likelihood that other, more important pages, end up crawled and indexed.

When SEO Consultant [Francesco Baldini](https://www.linkedin.com/in/francescobaldini/) and team audited a vehicle valuation platform, he found that most of the website’s crawl budget was used on low-quality [programmatic pages](https://ahrefs.com/blog/programmatic-seo/) which resulted in no search visits or conversions.

When they deleted almost 5 *million* pages (going from 4,860,000 pages to just 1,500), organic visits increased by 160% and conversions by 105% in a matter of weeks:

![](https://ahrefs.com/blog/wp-content/uploads/2024/03/word-image-173536-1.png)

In case the mechanism of action is in doubt (did deleting pages really improve indexing?), it’s worth reading about Victor Pan’s experience [deleting 3,000 pages](https://blog.hubspot.com/marketing/remove-outdated-content) from the HubSpot sitemap:

> “*As of two weeks ago, we’re able to submit content, get it indexed, and start driving traffic from Google search in just a matter of minutes or an hour. For context, indexation often takes hours and days for the average website.”*
>
>
>
> Victor Pan, Principal Marketing Manager, SEO, [HubSpot](https://www.linkedin.com/in/victorpan/)

It’s worth pointing out that both of these examples feature *extremely* big websites—crawl budget is not an issue for most smaller sites.

Further reading

- [What Is Crawl Budget & Why Most SEOs Shouldn’t Worry About It](https://ahrefs.com/blog/crawl-budget/)

### Removing low-quality pages might help the remaining content rank better

Some of Google’s systems—like Helpful Content—look at your website as a whole to help influence where your content is ranked.

As [Google explains](https://developers.google.com/search/docs/appearance/helpful-content-system):

> *“Having relatively high amounts of unhelpful content might cause other content on the site to perform less well in Search, to a varying degree.* ***Removing unhelpful content might contribute to your other pages performing better.****”*

When [Eugene Zatiychuk](https://www.linkedin.com/in/yevgen-zatiychuk/), SEO Lead at [Belkins](https://belkins.io/), started a content pruning exercise, his focus was removing low-quality content: *“duplicates (targeting same search intent); low-quality writing, including both cheap writers and AI-generated; and content written for the wrong target audience.”*

Here’s an example of a pruned page, an [AI-generated article](https://ahrefs.com/blog/ai-content-is-short-term-arbitrage/) about sales lead job descriptions that didn’t include a job description anywhere on the page:

After pruning 400 pages of low-quality content (almost two-thirds of the entire site), traffic began to climb steadily from 3,000 organic visits per month to almost 10,000:

Eugene points out that he started on other improvements alongside the prune (like reducing the site’s reliance on [JavaScript rendering](https://ahrefs.com/blog/javascript-seo/) about a month after the prune started), but he’s confident that pruning helped improve the performance of the remaining pages.

### Simpler, smarter navigation makes for a better visitor experience

Content pruning can help by simplifying the user journey and making it easier to navigate to important pages.

That was the primary motivation behind [Bryan Casey](https://www.linkedin.com/in/bryan-f-casey/)’s initiative to prune over 1,000 pages from IBM’s main site navigation. As Bryan explained, *“these pages were a small percentage of our traffic and our site footprint, but responsible for a large percentage of our complexity.”*

> *“We were determined to change the structure of the site and flattening it to one menu was a key part of that. Our product footprint was another huge chunk of the site and had consistent page types and so we analyzed all the “types” within the product footprint and decided that we could a) eliminate entire page types (details, FAQ) and b) aggressively consolidate across parts of the portfolio (ie go from 5 pages to 1 for a product).”*
>
>
>
> Bryan Casey, Director, Digital Marketing, [IBM](https://www.linkedin.com/in/bryan-f-casey/)

By way of example, I used the Wayback Machine to see how many clicks it used to take to find the main landing page for one of IBM’s products, robotic process automation.

My journey from the homepage spanned five pages: */us-en → /cloud/automation → /cloud/automation/technology → /cloud/learn/rpa → /products/robotic-process-automation*:

After pruning and consolidating, the current journey requires covers just two pages: */us-en → /products/robotic-process-automation*:

Traffic growth wasn’t the goal of this pruning exercise—Bryan was happy that the team ensured no change to site traffic. Instead, it was the subjective experience of visitors using the site that Bryan cared about, as measured by [Net Promoter Score](https://ahrefs.com/blog/marketing-kpis/):

> “NPS of nav on ibm.com improved by 30% immediately. And the really cool thing was that our experience scores around content quality improved by the same amount. It proved our hypothesis that the structure of the site impacts your perception of everything on it.”
>
>
>
> Bryan Casey, Director, Digital Marketing, [IBM](https://www.linkedin.com/in/bryan-f-casey/)

## How to prune content

The hard part of content pruning isn’t the pruning itself: it’s the decision-making process that determines what you’ll prune. There are tons of factors to consider, and it’s important to avoid setting arbitrary targets for what you will and won’t delete:

- **Page traffic:** how much traffic does the page get from search, and from other sources?
- **Backlinks**: how many websites link to the page?
- **Non-traffic benefit**: is the page important for other reasons? Does it contain important information, or help close sales? Does it serve as a historical record—like a newspaper article?
- **Age**: has the article had long enough to perform?
- **Relevance:** is the page still relevant to the audience you target and the products you sell?
- **Cannibalizing pages**: does the page compete with others?

This decision-making process is called a content audit, and we walk you through the [whole process here](https://ahrefs.com/blog/content-audit/).

Further reading

- [Follow Our Content Audit Process for 2023 (Template Included)](https://ahrefs.com/blog/content-audit/)

### 1. Get buy-in

Content pruning is most useful for big websites, and big websites generally mean lots of people who care about the different pages: the SEO/content team, the product team, the sales team, separate business units, you name it.

If you’re planning a prune, it’s worth sharing your plans (and justification) with everyone involved, and hearing out their concerns. At IBM, Bryan went to the trouble of scheduling a week of meetings with every impacted team:

> “Our mental model was to go into every meeting and get 80% of what we wanted in terms of simplification. We never wanted to get all of it because it was important our stakeholders felt like all their priorities were protected. Even if you personally do not agree with something, you have to be ok ‘losing’ on some percentage of things to keep everyone at the table. If the room turns on you, game over.”
>
>
>
> Bryan Casey, Director, Digital Marketing, [IBM](https://x.com/bryanfcasey/status/1659942013658169344?s=20)

Further reading

- [How to Get SEO Buy-In: 7 Actionable Tips](https://ahrefs.com/blog/seo-buy-in/)

### 2. Delete in batches

As with any risky change, it’s a good idea to prune pages in batches and monitor their impact before making a sweeping change. If anything goes wrong—organic traffic plummets unexpectedly, or [key pages become orphaned](https://ahrefs.com/blog/orphan-pages/)—it’s relatively easy to contain the impact and roll back your changes.

From January to March of 2023, Eugene at Belkins deleted one subfolder per week, monitoring the impact as he went (more on that below):

### 3. 301 redirect to the closest matching page

If a pruned page has backlinks or traffic, it’s a good idea to [redirect the old URL](https://ahrefs.com/blog/301-redirects/) to a close-matching page somewhere else on the site. Close-matching usually means a page on a similar topic—something that wouldn’t feel out of place to visitors who clicked the old URL.

Here’s an example from Belkins: an article about the number of leads required to make a sale is 301 redirected to another about lead generation conversion rates:

Further reading

- [301 Redirects Explained: How They Impact SEO](https://ahrefs.com/blog/301-redirects/)

### 4. Consolidate or repurpose deleted content

Even bad pages can contain [good content](https://ahrefs.com/blog/how-to-write-great-content/), so it can be worth keeping it around in some format. That can mean:

- **Consolidating**: taking related information from multiple pruned pages and combining them on another page. (This has the benefit of making it much easier to 301 redirect deleted pages to close matches—your new consolidated content).
- **Repurposing**: finding a new, more useful format for the information, whether that’s turning it into an email sequence, social media content, or a downloadable ebook.

Further reading

- [13 Smart Ways to Repurpose Content](https://ahrefs.com/blog/repurposing-content/)

### 5. Measure the impact

Depending on your motivation for the prune, you’ll want to [measure before/after values](https://ahrefs.com/blog/seo-performance-results/) for metrics like:

- **Indexing:** what percentage of important pages are indexed? Does indexing happen faster?
- **Search traffic**: has search traffic to your remaining pages improved?
- **Visitor experience**: is your website easier to navigate? Is high-quality content easier to find?

Importantly, it can be hard to categorically show the impact of a prune: pruning usually happens as part of a batch of search improvements. (And nobody is going to suggest pausing content production for a quarter just to isolate the impact.)

But you don’t need perfect data: you’re looking for relatively quick changes that can’t be easily explained by other initiatives.

Further reading

- [How to Measure SEO Performance & Results (The Right Way)](https://ahrefs.com/blog/seo-performance-results/)

## Final thoughts

Content pruning is a relatively niche tool in the SEO toolkit, best suited to (very) big websites, or those with a ton of irrelevant or low-quality content.

But if you find yourself in either situation, taking the shears to your least helpful pages can improve the performance of the content that’s left behind. Or put another way, care of *The Office:*
