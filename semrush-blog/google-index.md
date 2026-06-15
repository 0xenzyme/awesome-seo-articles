---
title: "How to get your website indexed by Google"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "google-index"
url: "https://www.semrush.com/blog/google-index/"
canonical: "https://www.semrush.com/blog/google-index/"
author: "Carlos Silva, Christine Skopec"
published: "2020-12-28T14:21:00+00:00"
updated: "2026-06-02T14:59:00+00:00"
categories:
  - "General SEO"
freshness_reasons: []
schema_genre: "General SEO"
fetched_at: "2026-06-12T15:48:56+00:00"
status_code: 200
html_hash: "cdc348252767b724ac40c32b5f45970285e0d5dfa5f94eb412e60ba23782bf02"
clean_word_count: 3160
clean_char_count: 21352
---
# How to get your website indexed by Google

Getting your website indexed by Google is necessary if you want to appear in Google’s organic or AI search results.

Today, we’ll show you different ways to confirm if Google has indexed your website. We’ll also cover common indexing issues like:

- Mistakes with your robots.txt file
- Accidental use of noindex tags
- Improper canonical tags
- Internal link problems
- URLs returning 404 errors
- Duplicate content
- Poor site quality

After reading, you’ll know how to find and fix indexing issues and confirm whether Google has indexed your most important pages.

## What is the Google index?

The Google index is a massive database of webpages that Google has crawled.

The index is a structured database that allows Google to instantly match search queries with relevant results. This means if your webpages aren’t in Google's index, they won’t appear in organic search results, [AI Overviews](https://www.semrush.com/blog/ai-overviews/), AI Mode, or Gemini.

Being absent from Google’s index could even impact your visibility in AI tools like ChatGPT. We know that [those AI systems rely on Google](https://www.semrush.com/blog/chatgpt-definitely-uses-google/) at least some of the time.

The indexing process follows this sequence when no issues occur:

- **Crawling**: [Googlebot](https://www.semrush.com/blog/googlebot/) discovers new or updated pages across the web
- **Indexing**: Google analyzes pages and stores them in its database
- **Selecting**: Google's algorithm chooses the most relevant pages from its index for search results

While Google’s own algorithms control indexing, website owners can take steps to influence the process.

## How do you check if Google has indexed your site?

Check if Google has indexed your site with the "site:search" operator or using Google Search Console.

### Use "site:search" operator

The "site:search" operator displays indexed pages from a particular website in search results.

Here’s how to use to to see if your own pages are indexed:

1. Go to Google
2. Type "site:[yourdomain.com]" in the search bar

After searching, you'll see indexed pages as search results. To see the total number, click the “**Tools**” drop-down to see an approximate number of results. Zero results indicate no indexed pages.

![Google search results for site:backlinko.com with indexed page count highlighted in Tools menu](https://static.semrush.com/blog/uploads/media/6a/82/6a82bdc94e154f1f4a22f33bf29d56e7/fc043db17df584cd6fdaa5d1f39d1e35/image.png)

While the "site:search" operator works for identifying whether your pages are indexed, it doesn’t allow you to identify pages that haven’t been indexed. You’ll need to identify those pages using [Google Search Console](https://search.google.com/search-console/) (GSC).

### Use Google Search Console

Google Search Console’s "Page indexing" report shows you which pages on your site are indexed and which ones aren’t.

Open your GSC account and head to "**Pages**" (under "Indexing"). Click "**View data about indexed pages**" for a sample list of indexed pages.

![Google Search Console Page Indexing report with "View data about indexed pages" section highlighted](https://static.semrush.com/blog/uploads/media/b0/a5/b0a58281289ae841daab7f7ee7d5498f/59ac9ee2941bbeb448430201a9aa2265/image.png)

The "Indexed pages" report may not show all indexed pages if you exceed the limit of 1,000 items. Or if something was added after the most recent crawl.

![Google Search Console Indexed Pages report showing 91 indexed pages and example URLs](https://static.semrush.com/blog/uploads/media/c1/e4/c1e49fd781cec83dca4fa4eaf87f7995/d6c05448269db80d449c968f1a743992/image.png)

Go back to the "Page indexing" report to view pages that aren’t indexed by scrolling down. In that table, GSC lists reasons why your pages aren’t indexed. Click a reason to see a list of affected pages.

![Google Search Console report showing reasons pages aren’t indexed, including robots.txt blocks](https://static.semrush.com/blog/uploads/media/d8/cd/d8cdf1373a46e25a11a1b0ae10cce74c/d2673849403624ac4d85318695b7c788/image.png)

Each status corresponds to a specific problem. The table below explains some common [Google Search Console errors](https://www.semrush.com/blog/google-search-console-errors/) related to indexation and what to do about each one.

| **Status** | **What it means** | **What to do** |
| --- | --- | --- |
| **Discovered – currently not indexed** | Google knows the page exists but hasn't crawled it yet. This often happens when Google thinks crawling the page will overload the site. | Request indexing, strengthen internal linking to the page, or minimize duplicate/thin pages consuming [crawl budget](https://www.semrush.com/blog/crawl-budget/) |
| **Crawled – currently not indexed** | Google visited the page but chose not to index it. This often signals a quality problem. | Improve page quality by adding original content and ensuring the page fully answers readers’ questions |
| **Blocked by robots.txt** | A [robots.txt](https://www.semrush.com/blog/beginners-guide-robots-txt/) (a file that tells bots what they should and shouldn’t crawl) directive is telling Googlebot not to crawl the URL | Open your robots.txt file and check for rules telling crawlers to avoid the page. Remove or adjust the rule if the page should be indexed. |
| **Duplicate, Google chose different canonical than user** | Google found multiple versions of this page and decided a different URL is the main version | Ensure you’ve used canonical tags on all versions that point to your preferred URL |
| **Excluded by 'noindex' tag** | A <meta name="robots" content="noindex"> tag in the HTML is explicitly telling Google not to index the page | Remove the noindex tag from the page's source code if you want it indexed |
| **Not found (404)** | The URL returns a [404 error](https://www.semrush.com/blog/404-error/), which means the page doesn't exist at this address | Restore the page if deleted, correct the URL if wrong, or set up a [301 redirect](https://www.semrush.com/blog/301-redirects/) (a permanent redirect) to the current version of the content |

## How do you get Google to index your site?

You don’t need to do anything aside from wait for Google to index your site, but you can speed up the process by creating and submitting a sitemap or by using the URL inspection tool in Google Search Console.

### Create and submit a sitemap

Creating and submitting a [sitemap](https://www.semrush.com/blog/website-sitemap/) — a file that includes all your important URLs and indicates how they relate to each other — helps crawlers find your priority pages more quickly.

A sitemap looks something like this:

![Semrush Sitemap index file showing URLs in XML format](https://static.semrush.com/blog/uploads/media/d8/2c/d82c58ae590cfa89f29a287dd42f43a3/6aa9a334f685fa0058222a39891531a3/image.png)

If you don’t know your sitemap URL, find it by reviewing your robots.txt file. Enter your "https://[yourdomain.com]/robots.txt" and look for your sitemap URL (you might have to scroll down).

![Browser view of a robots.txt file with sitemap URL highlighted](https://static.semrush.com/blog/uploads/media/e7/4f/e74f04d9f7f29753c2eb894cfa968fb1/140ec9001d2847a796ff1bee84ebfbc6/image.png)

If you lack a sitemap, consult our guide for [creating an XML sitemap](https://www.semrush.com/blog/xml-sitemap/).

To submit your sitemap in GSC:

1. Navigate to "**Sitemaps**" under the "Indexing" section in GSC's menu
2. Enter your sitemap URL under "Add a new sitemap"
3. Click "**Submit**"

![Google Search Console Sitemaps page with sitemap_index.xml submission field highlighted](https://static.semrush.com/blog/uploads/media/14/aa/14aa08e6143510737d008c9edbc6aa81/4f37e1c68bcc9be7ef467128c0f8de86/image.png)

Processing typically takes a couple of days. Upon completion, you'll see your sitemap link with a green "Success" status.

![Submitted sitemap report in Google Search Console showing successful sitemap status](https://static.semrush.com/blog/uploads/media/4d/21/4d212d5c8f88b5af5e978bba313d2164/9311041c675758da1bbbf53cf22aec50/image.png)

### Use the URL inspection tool

The URL inspection tool in GSC allows you to request indexation for a specific page.

Enter the URL in the top search bar in GSC and press enter. If you see “URL is on Google” near the top, it means the specified page has been indexed already. You can also see information about when Google last crawled the page, whether the page is Google’s selected canonical, and whether the page is your specified canonical.

![Google Search Console URL Inspection report showing page is indexed and on Google](https://static.semrush.com/blog/uploads/media/1c/b8/1cb8c4f85c4fd3656939dfb083c1a087/543af60db6b7b351a735772734fa99ab/image.png)

A "URL is not on Google" status means the URL isn't indexed and won't appear in search results. Review the provided reason and address the issue.

![Google Search Console URL Inspection report showing page is crawled but not indexed](https://static.semrush.com/blog/uploads/media/1a/e3/1ae3d6119bb975899091d93988c86060/2579a5821816aa6b4a848eb705dbb1ae/image.png)

After addressing the issue listed, click the "**Request Indexing**" link to ask Google to prioritize crawling it. This doesn’t guarantee immediate indexing, but Google typically processes these requests within a few weeks. Periodically check the page with the URL inspection tool to confirm Google has indexed the page.

![Google Search Console URL Inspection page with Request Indexing button highlighted](https://static.semrush.com/blog/uploads/media/19/0a/190a24612fdc985d324869b497416364/3ffc19cc42026e719291a3c4b869cfd8/image.png)

## Common indexing issues to find and fix

Common indexing issues to find and fix include errors in your robots.txt file, lack of mobile usability, slow loading speeds, and redirect issues.

Find indexing issues specific to your site with Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool. After [configuring Site Audit](https://www.semrush.com/kb/539-configuring-site-audit), click "**Issues**" and filter the issues by "**Crawlability**" to see issues that prevent search engines from crawling your site.

Click a specific error to see the affected pages, and "**How to fix**" for tips on resolving each error.

![Semrush Site Audit report filtered for Crawlability issues with broken internal links issue details expanded](https://static.semrush.com/blog/uploads/media/95/a7/95a763e1532d7f1143529fdcf8cb6776/69a3d45bcf491a31deeac22200260a46/image.png)

Let’s go over some of the most common indexing issues in greater detail:

### Mistakes with your robots.txt file

Mistakes with your robots.txt file can tell Google to avoid crawling certain pages or even your entire site.

The robots.txt file below tells one bot to avoid crawling the entire site. If that directive targeted Googlebot instead, Google would avoid crawling the site.

![Robots.txt file showing rules allowing and disallowing specific user agents from crawling the site](https://static.semrush.com/blog/uploads/media/9d/dc/9ddcc042b840ebad1bbf5d480d1be060/10c9bb1a8a62131235a4ea6a669a8a1c/image.png)

Find your robots.txt at “https://[yourdomain.com]/robots.txt.” Consult our [robots.txt guide](https://www.semrush.com/blog/beginners-guide-robots-txt/#how-to-create-a-robots-txt-file) if you lack one and need directions on how to create one.

You can use directives to tell crawlers to avoid duplicate pages, private content, or resource files. However, if your robots.txt tells bots to avoid crawling completely, indexing is highly unlikely.

Here’s an example that tells all bots to avoid crawling the entire website:

`User-agent: *
Disallow: /`

So, review your robots.txt to ensure no directive prevents Google from crawling pages you want indexed.

### Accidental use of noindex tags

Accidentally using the "noindex" [robots meta tag](https://www.semrush.com/blog/robots-meta/) (an HTML tag within a page) tells crawlers not to index a page.

A noindex tag looks like this:

`<meta name="robots" content="noindex">`

Check which pages have noindex tags in GSC:

1. Click "**Pages**" under "Indexing" in the left menu
2. Scroll to "Why pages aren't indexed"
3. Click "**Excluded by 'noindex' tag**" if present

![Google Search Console report highlighting pages excluded by noindex tag](https://static.semrush.com/blog/uploads/media/ad/80/ad80dcd9477086b076dd97d9de5174e0/4869135ce3c2a76fc42b47075e2bd5bd/image.png)

Remove the noindex tag from any pages in the list that you want to appear in Google’s index.

[Site Audit](https://www.semrush.com/siteaudit/) warns about pages blocked via robots.txt or noindex.

![Semrush Site Audit notice showing pages blocked from crawling](https://static.semrush.com/blog/uploads/media/50/2f/502f9d8d3bde4317b09c47c3db362bcb/55f663668561a99d73f7b039b2c2f460/image.png)

Site Audit also notifies you about resources that are blocked by x-robots-tag, which is typically used for non-HTML documents like PDFs.

![Site Audit report showing X-Robots-Tag noindex HTTP header notice](https://static.semrush.com/blog/uploads/media/39/40/39404cb60829741682f9915297209e2b/03cc6efc3c79e6ecf47e3e9aae71accf/image.png)

### Improper canonical tags

Improper canonical tags that point Google to the wrong URL can prevent your intended page from appearing in search results.

Find improper canonical tags within GSC's "Page indexing" report:

1. Scroll to "Why pages aren't indexed"
2. Click "**Alternate page with proper canonical tag**"

![Google Search Console report showing alternate page with proper canonical tag reason](https://static.semrush.com/blog/uploads/media/a1/3f/a13f1253d7878e75dc3b71a5b17dd508/1703f7d846abf52b41678f2da9d2c8de/image.png)

Review the affected pages list. If there’s a page you want to have indexed (meaning the canonical is used incorrectly), adjust the canonical tags on all versions of the page to point to your preferred version.

### Internal link problems

Internal link problems prevent crawlers from discovering pages, which can keep those pages out of Google's index.

Find internal linking issues in Site Audit’s “Internal Linking” thematic report. You’ll see a list of internal linking issues. Click any issue count link to see affected pages.

![Semrush Internal Linking report showing broken links and crawl depth issues](https://static.semrush.com/blog/uploads/media/9e/b6/9eb65a0a4c1e69c2ef957ffd6f1f3a47/d0657e9264fd3090e889d15c0fa0eeef/image.png)

These are some of the most important issues to address when it comes to crawling and indexing:

1. **Nofollow attributes in outgoing internal links**: Nofollow links generally tell Google not to follow a link or pass [authority](https://www.semrush.com/blog/pagerank/) to it, so Google might ignore pages on your site if you’ve used nofollow links to them internally
2. **Page Crawl Depth more than 3 clicks**: If pages need more than three clicks to be reached from the homepage, there's a chance they won't be crawled and indexed. Add more internal links to these pages (and review your [website architecture](https://www.semrush.com/blog/website-structure/)).
3. **Orphaned sitemap pages**: Pages that have no internal links pointing to them are known as "orphaned pages." They’re rarely indexed as Google may struggle to find them. Fix this issue by linking to any orphaned pages.

When building internal links, prioritize linking to your most important pages. And also actively work to link to new pages to accelerate indexing.

### 404 errors

A 404 error occurs when a server can’t locate a page, and it prevents Google from finding and indexing pages.

Plus, 404 errors harm the user experience.

Find your site’s 404 errors within Site Audit’s "**Issues**" tab. Click the link in "**# pages returned a 4XX status code**."

![Semrush Site Audit issues report highlighting pages returning 4XX status codes](https://static.semrush.com/blog/uploads/media/35/15/35155d33e9a7a2d0ffd87306d74721ad/c203d1ff32c93a5a53b3da925b529649/image.png)

For each "404" page, click "**View broken links**" to see pages linking to it.

!["View broken links" highlighted](https://static.semrush.com/blog/uploads/media/16/13/16135f5296f5df3c9c556b1a9dc8565a/4ddb11a24327646d23d7be1f8b0634f4/image.png)

Fix 404 errors by correcting URL typos, updating links to new page locations, or replacing links with relevant substitutes if content no longer exists.

### Duplicate content

Duplicate content — identical or very similar content across multiple URLs — confuses search engines and may result in undesired pages being indexed.

Click "**Issues**" in [Site Audit](https://www.semrush.com/siteaudit/) and search for "duplicate." Click the hyperlink in "# pages have duplicate content issues."

![Semrush Site Audit issues filtered for duplicate content problems](https://static.semrush.com/blog/uploads/media/b1/3b/b13ba5cc5760b597e81f8f8c58580916/0a2e960aeeaec96972531a69d0af949c/image.png)

Fix duplicate content issues by:

- **Eliminating unneeded duplicates**: Consolidate content onto the main page, delete duplicates, and implement [301 redirects](https://www.semrush.com/blog/301-redirects/) to the primary page
- **Keeping necessary duplicates**: Use canonical tags to indicate your preferred version

### Poor site quality

Poor site quality can hurt your chances of being indexed as Google prioritizes crawling and indexing sites it deems high quality.

Here are three ways to make your site appear trustworthy to Google:

#### Create high-quality content

Creating high-quality content that genuinely helps readers improves your chances of being indexed and shown in search results.

Follow these tips for creating quality content:

- **Address user needs**: Solve relevant problems and answer key questions with actionable solutions
- **Demonstrate expertise**: Publish content authored by subject matter experts with real-life examples and first-party data
- **Keep content current**: Maintain relevance through regular updates that address gaps and outdated information

#### Build relevant backlinks

[Building relevant backlinks](https://www.semrush.com/blog/how-to-get-backlinks/) from quality websites that are relevant to you provides more ways for Google to discover your pages and also signals authority.

Here are some link building tactics:

- **Guest articles**: Write for reputable sites in your niche to reach new audiences and potentially gain backlink
- **Expert contributor pitching**: Identify publications or podcasts that feature competitor voices, then pitch yourself as an expert source. Many publications are happy to link to sources’ websites.
- **Content replacement**: Find competitor content that's earned links, create a demonstrably better version, and pitch it as the upgrade to those same publications
- [**Competitor backlink analysis**](https://www.semrush.com/blog/competitor-backlinks/): Find where competitors are earning links and replicate the best opportunities through outreach

Use [Backlink Gap](https://www.semrush.com/analytics/gap/backlinks/) to do a competitor backlink analysis. Just enter your domain and up to four competitors' domains, then click "**Find prospects**"

![Semrush Backlink Gap tool start with 5 domains entered and arrow pointing to Find prospects button](https://static.semrush.com/blog/uploads/media/cf/e9/cfe904f4cc5e2972490f4593e74d5179/488ee43fd86dd2186ccfd1221a5450af/image.png)

The "**Best**" tab within Backlink Gap shows websites linking to all competitors but not you. These sites are often worth pitching. There’s a good chance they’ll link to you if they’re already linking to all your rivals.

![Prospects for table with Referring Domain column highlighted](https://static.semrush.com/blog/uploads/media/59/99/59999f87f7b85ae51e02f36d8975edca/cabf415d121883b5f9f42186f7b8efdf/image.png)

#### Prioritize E-E-A-T

Focusing on Experience, Expertise, Authority, and Trustworthiness ([E-E-A-T](https://www.semrush.com/blog/eeat/)) — the criteria Google's human quality raters use to assess page quality — helps you align with what Google defines as good content.

E-E-A-T is not a Google ranking factor, but following the E-E-A-T framework helps you create good content.

To strengthen your E-E-A-T, aim to:

- **Provide transparent author information**. Highlight your contributors’ personal experiences and expertise concerning the topics they write about.
- **Collaborate with subject matter experts**. Include insights from industry experts. Or hire them to review your content for accuracy.
- **Support the claims you make**. Cite credible sources across all your published content, so readers know the information you provide is reputable.

## Monitor your site for indexing issues

Monitor your site for indexing issues by scheduling periodic audits that let you check your site for any issues as soon as they pop up.

With [Site Audit](https://www.semrush.com/siteaudit/), you can schedule audits weekly or daily, so you’re alerted of new issues right away.

![Semrush Site Audit settings with weekly crawl schedule dropdown open](https://static.semrush.com/blog/uploads/media/e6/b1/e6b194b2fb06b529197b0ea87c735896/4e0852edac5ef95a476805d5375a68fc/image.png)

Ready to find and fix indexing issues? Try Site Audit today.
