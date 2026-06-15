---
title: "New Study: How Often Do AI Assistants Hallucinate Links? (16 Million URLs Studied)"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "how-often-do-ai-assistants-hallucinate-links"
url: "https://ahrefs.com/blog/how-often-do-ai-assistants-hallucinate-links/"
canonical: "https://ahrefs.com/blog/how-often-do-ai-assistants-hallucinate-links/"
author: "Ryan Law"
published: "2025-09-02T09:32:10+00:00"
updated: "2026-05-31T14:22:14+00:00"
categories:
  - "AI Search"
  - "Data & Studies"
freshness_reasons:
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-12T11:36:59+00:00"
status_code: 200
html_hash: "cb85975d5ddddd5b58369df5bad172c225a0493f2c8b98da32a729f056b01ea3"
clean_word_count: 1850
clean_char_count: 11006
---
# New Study: How Often Do AI Assistants Hallucinate Links? (16 Million URLs Studied)

AI assistants like ChatGPT and Claude can hallucinate URLs and direct visitors to non-existent pages on your website. But how often does it happen?

To find out, we looked at the http status of 16 million unique URLs cited by ChatGPT, Perplexity, Copilot, Gemini, Claude, and Mistral.

![](https://ahrefs.com/blog/wp-content/uploads/2025/09/hallucinated-urls-2.jpg)

We found that AI assistants send visitors to 404 pages **2.87x more often** than Google Search.

ChatGPT is the greatest offender, with 1.01% of clicked URLs and 2.38% of all cited URLs returning a 404 status (compared to baseline 404 rates of 0.15% and 0.84% respectively).

Here’s what we found:

## Test 1: Analyzing clicked URLs in Web Analytics

For the first test, we used anonymized data from our free analytics tool, [Web Analytics](https://ahrefs.com/web-analytics). This allowed us to see actual visits to AI-recommended URLs on real websites.

Here’s the methodology:

- We used Web Analytics data to find all URLs with an AI assistant (like ChatGPT or Perplexity) as their referrer.
- We marked URLs as a possible 404 page if the page title contained either “404” or the phrase “not found”.
- For each AI assistant, we compared the number of possible 404 pages to the total number of referred URLs to find their 404 rate.

ChatGPT has the highest rate of 404 pages, with 1.01% of all cited URLs containing “404” or “not found” in their page title.

Claude follows with 0.58% of URLs, followed by Copilot (0.34%), Perplexity (0.31%), and Gemini (0.21%). Mistral has the lowest 404 rate (0.12%), but also sends the lowest amount of referral traffic, making it the smallest sample in this test.

| Referrer | Likely 404 Pages | Total Unique URLs | 404 Rate |
| --- | --- | --- | --- |
| ChatGPT | 84465 | 8332436 | 1.01% |
| Perplexity | 3529 | 1133084 | 0.31% |
| Copilot | 1466 | 431319 | 0.34% |
| Gemini | 734 | 351242 | 0.21% |
| Claude | 550 | 95293 | 0.58% |
| Mistral | 8 | 6760 | 0.12% |

### Google’s 404 base rate

This is not a perfect test. Some 404 pages may not include “404” or “not found” in the page title. And not all links hallucinated by AI assistants will receive clicks (and will therefore not appear in Web Analytics data), so it’s likely that we are under-reporting the total number of hallucinated URLs.

Some fraction of these 404 pages may also be genuine 404 pages, and not hallucinated URLs. We can add extra context to this data by comparing to a “base rate” of 404 pages. To do this, we looked at the 404 rate for all unique URLs with Google as their referrer (629M unique URLs). This 404 rate was 0.15%.

With this extra context, it’s obvious that the 404 rates of AI assistants are significantly higher than the “base” 404 rate for Google. It seems likely that ChatGPT, Claude, Copilot, Perplexity, and Gemini all create hallucinated URLs.

The average 404 rate across all AI assistants was 0.43%. Compared to the 404 rate to URLs referred by Google, AI assistants send visitors to 404 pages at **2.87x the rate of Google Search** (`0.43/0.15`).

## Test 2: Analyzing cited URLs in Brand Radar

We also ran a similar test using [Brand Radar](https://ahrefs.com/brand-radar), our massive searchable database of millions of AI assistant prompts and outputs. Using this data, we can see all URLs cited by AI assistants, and not just those that received a click.

- We found all URLs cited by ChatGPT, Perplexity, Copilot, and Gemini in our Brand Radar databases.
- For those URLs also stored in our crawler database (65% of total URLs), we retrieved the most recent http status.
- For each AI assistant, we calculated the 404 rate of cited URLs in our crawler database.

The 404 rate of cited URLs (and not just cited *and* clicked URLs) is much higher than in our previous test.

Again, ChatGPT has the highest rate of 404 pages (2.38%), followed by Perplexity (0.87%) and Gemini (0.86%) in close succession. Copilot has the lowest 404 rate, at 0.54%.

This test also has limitations. As before, some number of these 404 pages will [return a 404 status](https://ahrefs.com/seo/glossary/404-error) for some reason other than hallucination. We are also underestimating the total number of 404 URLs, because we can only see the http status for those URLs that are in our crawler database (and I’d expect a decent percentage of hallucinated URLs to be absent from our crawler database, because they have never existed).

As before, we wanted to compare these figures to a “baseline” 404 rate. To do that, we extracted all unique URLs from the top 20 positions of 400,000 SERPs.

67% of these URLs were also in our crawler database, allowing us to determine a 404 rate of 0.84%. (Or put simply, 0.84% of the URLs in Google’s top 20 return a 404 status.)

The 404 rates for Perplexity (0.87%) and Gemini (0.86%) are extremely close to the 404 rate for Google SERPs (0.84%).

This may be because Gemini and Perplexity use the Google Search index to retrieve URLs: their 404 rates reflect the 404 rate of URLs in the underlying source, Google. If so, it seems likely that they have a lower hallucination rate than ChatGPT.

Copilot uses the Bing search index, so it’s possible that Copilot’s 404 rate is reflective of Bing’s 404 rate.

| AI Assistant | Unique Cited URLs | URLs in Crawler DB | 404 Rate |
| --- | --- | --- | --- |
| ChatGPT | 2,452,776 | 1,524,277 | 2.38% |
| Perplexity | 3,471,754 | 2,450,016 | 0.87% |
| Copilot | 1,485,355 | 1,120,780 | 0.54% |
| Gemini | 1,354,171 | 641,603 | 0.86% |

## Why do AI assistants hallucinate links?

I suspect there are two main causes of hallucinated links.

Some portion of cited URLs *used* to be valid, but now return a 404 status. AI assistants use a combination of web search and their own internal knowledge. It’s possible that some of the URLs they cite may have existed at one time, but have since been deleted or moved (without [redirecting the original page](https://ahrefs.com/blog/redirects-for-seo/))—especially when relying solely on internal knowledge.

(This also explains why a high number of these 404 pages exist in our crawler database.)

Another portion of cited URLs are true hallucinations, in the sense that they fit the expected pattern of URLs for a given website, but don’t actually exist.

For the Ahrefs blog, the most commonly-visited hallucinated URLs are pages like `/blog/internal-links/`, and `/blog/newsletter/`. Given that we write about SEO topics on our blog, and have a newsletter, these URLs fit the pattern of typical Ahrefs blog pages—but they don’t actually exist.

Some of these hallucinated links may also be present in our crawler database. If published AI-generated content contains a hallucinated URL, our crawler will attempt to fetch it. With [74% of new webpages containing some amount of AI-generated content](https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/), this seems very possible.

## How to find your website’s hallucinated URLs

If you want to measure the impact of hallucinated URLs, the best datasource at your disposal is your own website analytics. Here’s how to test this for yourself:

### 1. Filter your website analytics to show AI traffic

Start by filtering your website analytics to show the visits received from AI assistants. If you use GA4, you’ll need to apply a regular expression to the Session source dimension within an Exploration report.

[Thierry Ngutegure at SALT.agency](https://salt.agency/blog/how-to-track-referral-traffic-from-ai-platforms-llms/) recommends the following regex. You’ll need to update the expression when new AI assistants appear, or they change their referrer information:

```
.*gpt.*|.*chatgpt.*|.*openai.*|.*writesonic.*|.*nimble.*|.*perplexity.*|.*claude.*|.*gemini.*google.*|.*copilot.*microsoft*|.*outrider.*|.*google.*bard.*|.*bard.*google.*|.*bard.*|.*deepseek.*|.*mistral.*|.*edgeservices.*|.*neeva.*
```

If you use Ahrefs’ [Web Analytics](https://ahrefs.com/web-analytics), just use the built-in “AI search” channel filter:

Select whatever time period you’re interested in, and export your data to Google Sheets.

### 2. Generate an Apps Script to return http status

Next, ask ChatGPT (or your AI assistant of choice) to generate an Apps Script to return the http status for URLs in a Google Sheet. Then, in your Google Sheet, navigate to *Extensions > Apps Script*, and paste and save your script.

Create a new column in your Google Sheet, call your script, target the cell containing your URL (e.g. =GetHttpStatus(A2)), and apply to the whole column.

(This can take a while if you have thousands of URLs—for big websites, it would be better to use a crawler instead.)

### 3. Filter to 404 status and >10 visitors

Next, filter your sheet to show just URLs returning a 404 status code **and** receiving visitors.

I set the threshold to URLs receiving greater than 10 visitors per month, but you can use whatever threshold makes sense for your website.

You can manually inspect some of these URLs to confirm that they’re hallucinated (and not real website pages that are unavailable for some other reason).

### 4. 301 redirect (if it makes sense)

If you have hallucinated pages receiving a sizeable number of visits, it might be worth [301 redirecting](https://ahrefs.com/blog/301-redirects/) the hallucinated URL to a relevant page on your website (if you have one).

You’ll need to guess what the hallucinated page may have been about, but often, the URL alone will be enough to make an educated guess (visitors to the hallucinated URL `/blog/keywords/` will probably benefit from our real guide to keyword research).

Or, if you don’t want to create a spiderweb of 301 redirects, you could update your 404 page to include a list of useful resources that disappointed LLM visitors might find helpful (like your most popular content, or your newsletter subscription page).

## Should I care about this?

At our last measure, AI assistants (primarily ChatGPT) accounted for [0.25% of a total website’s traffic](https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/), compared to Google at 39.35%. With 1.01% of ChatGPT’s referred traffic leading to a 404 page, hallucinated URLs impact a small percentage of an already-small-percentage of an average website’s traffic.

This is a useful exercise for understanding another idiosyncracy of AI search, but it doesn’t represent some huge growth lever. If you can minimize the impact of hallucinated URLs with *very little effort*, it’s probably worthwhile.

For that reason, we’re about to add a new filter to [Web Analytics](https://ahrefs.com/web-analytics) that will help you find hallucinated URLs in just two clicks. If you’re looking for a simple Google Analytics alternative, free for up to 1 million events each month, check it out:

Questions or comments about this research? [Let me know on LinkedIn](https://www.linkedin.com/in/thinkingslow/).
