---
title: "Robots.txt Explained: Syntax, Best Practices, & SEO"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "beginners-guide-robots-txt"
url: "https://www.semrush.com/blog/beginners-guide-robots-txt/"
canonical: "https://www.semrush.com/blog/beginners-guide-robots-txt/"
author: "Vlado Pavlik, Christine Skopec"
published: "2018-07-10T11:00:00+00:00"
updated: "2025-07-30T10:11:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "time_sensitive_title"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T13:55:56+00:00"
status_code: 200
html_hash: "025866f1b9de22320732a6a7c6ff39a2a68e293644138eca96b4e6def65ad25a"
clean_word_count: 2807
clean_char_count: 18923
---
# Robots.txt Explained: Syntax, Best Practices, & SEO

## What Is a Robots.txt File?

A robots.txt file is a set of rules that tells web crawlers which pages or sections of a website they should crawl and which to avoid.

It looks like this:

![Robots.txt file shows lines of code listing user agents and allowed/disallowed file paths.](https://static.semrush.com/blog/uploads/media/12/23/12232eb64e0bdd5c723294a4dca6c5b1/c1a910b3c336e57ae7cd92525cf752fd/AD_4nXexYoPmL6Kk2qE0PNsRZz2dZ10kxKDpccBgr62xmZGhoHtKEoGL3ZKY25lAmSn2llAM__Dmw0ys6GN_PIGrPJeCXmyr2q8V3cuW78miJ-PtwT41YqbXbHo9imabr-9k_6f_GtCL.png)

Robots.txt files may look complicated.

But the syntax (computer language) is straightforward—“Allow” means the [web crawler](https://www.semrush.com/blog/website-crawler/) **should** crawl it, while “disallow” means the crawler should **not** crawl it.

But keep in mind:

While robots.txt **guides** crawler behavior, it doesn’t guarantee that a page won’t appear in search results. Other factors (like external links) can still cause it to be [indexed by Google](https://www.semrush.com/blog/google-index/).

To block indexing, you should use Meta Robots and X-Robots-Tag.

### Robots.txt vs. Meta Robots vs. X-Robots

Robots.txt tells search engines **what not to crawl—**[meta robots tags and s-tobots-tags](https://www.semrush.com/blog/robots-meta/) tell them **what not to index**.

Knowing the difference helps you apply the right tool for the right situation.

Here’s how they compare:

- **Robots.txt**: This file is located in the website’s root directory and provides site-wide instructions to search engine crawlers on which areas of the site they should and shouldn’t crawl
- **Meta robots tags**: These tags are snippets of code in the <head> sections of individual webpages and provide page-specific instructions to search engines on whether to index (include in search results) and follow (crawl the links on) each page
- **X-robot tags**: These code snippets are used primarily for non-HTML files (like PDFs and images) and are implemented in the file’s HTTP header

If you want to keep something out of search results, use a [noindex meta tag](https://www.semrush.com/blog/noindex/) (on a crawlable page) or password-protect the page.

## Why Does Robots.txt Matter?

A robots.txt file helps control how bots interact with your site.

SEOs often use it to manage crawl load and improve efficiency by blocking unimportant or duplicate pages. It can also be used to deter scraping and prevent content from being used to train AI models.

Here’s a breakdown of why robots.txt files matter specifically for SEO:

### It Optimizes Your Crawl Budget

A robots.txt file helps search engines focus their [crawl budgets](https://www.semrush.com/blog/crawl-budget/) on your most valuable pages.

Blocking low-value pages (like cart, login, or filter pages) helps bots prioritize crawling content that actually drives traffic and rankings, especially on large sites with thousands of URLs.

For example:

Blocking “/cart/” or “/login/” pages helps bots focus on your blog posts or product pages instead.

### It Can Be Used to Control Search Appearance

Robots.txt gives you some control over how your site appears in search by managing what gets crawled.

While it doesn't directly affect indexing, it works with the below to guide search engines toward your important content:

- [**Sitemap**](https://www.semrush.com/blog/website-sitemap/): A file that lists the important pages on your site to help search engines discover and crawl them more efficiently
- [**Canonical tags**](https://www.semrush.com/blog/canonical-url-guide/): An HTML tag that tells search engines which version of a page is the preferred one to index when duplicate or similar content exists
- **Noindex directives**: A signal (via a [meta tag](https://www.semrush.com/blog/meta-tag/) or HTTP header) that tells search engines not to include a specific page or pages in the index used for search results

### It Helps Deter Scrapers and Unwanted Bots

Robots.txt is the first line of defense against unwanted crawlers, such as scrapers or bots harvesting content for training AI models.

For example, many sites now disallow AI bots’ user-agents via robots.txt.

This sends a clear signal to bots that respect the protocol and helps reduce server load from non-essential crawlers.

We partnered with SEO Consultant [Bill Widmer](https://www.linkedin.com/in/billwidmer/) to run a quick experiment and demonstrate how robots.txt rules impact crawler behavior in real-world conditions.

Here’s what happened:

Bill had a rule in his robots.txt file blocking a number of crawlers.

He used Semrush’s [Site Audit](https://www.semrush.com/siteaudit/) tool to crawl the entire site, setting the crawl limit high enough to catch all live pages.

But his website wasn’t crawled due to the robots.txt directives.

![Warning shows the audit was interrupted because the robots.txt file forbids the crawler.](https://static.semrush.com/blog/uploads/media/f3/79/f3797ad3020521d32a0a1ebf1c73460a/9d84824781af8e602c8d44a4902d9084/AD_4nXcACziDYEjiV3wXj98SSeZWjeVkArp1gqWSR_0LlbA2CzinwVPUz4B-gfuYTROxYGtBOjSsTyLWQ_87zeH18e2oQQkq_QIdZFy2ojuGq823Egu_ojRYale-15QVY0TILWsLO9PI4A.png)

After adjusting the robots.txt file, he ran the crawl again.

This time, his website was successfully crawled and included in the report.

![Semrush Site Audit dashboard shows the number of crawled pages and any issues with them.](https://static.semrush.com/blog/uploads/media/23/d2/23d201b5ee08995707327459c30c4c9f/550b383718012991aff2e5dffcc82234/AD_4nXdT7GDh0EDavFV_MJK7PMdcyUzdnyWfKPTl1DmqewQSQN215wI3ZqzsbF7orqvcFpU3ypYy2h-scdIWAn8JaftVi1BpvN_yFJgS8o8XoCPp3biigSNU09CX6tCJSFFcKckSrBOsYw.png)

## How to Create a Robots.txt File

A robots.txt file is easy to create—decide what to block, write your rules in a text file, and upload it to your site’s root directory.

Just follow these steps:

### 1. Decide What to Control

Identify which parts of your site should or shouldn’t be crawled.

Consider blocking:

- **Login and user account pages** (e.g., /login/) that don’t offer public value and can waste crawl budget
- **Cart and checkout pages** (e.g., /cart/) you don’t want in search results
- **Thank-you pages or form submission confirmation screens** (e.g., /thank-you/) that aren’t useful to searchers

If you’re unsure, it’s best to err on the side of allowing rather than disallowing.

Incorrect disallow rules can cause search engines to miss important content or fail to render your pages correctly.

### 2. Target Specific Bots (Optional)

You can write rules for all bots (User-agent: \*) or target specific ones like [Googlebot](https://www.semrush.com/blog/googlebot/) (User-agent: Googlebot) or Bingbot (User-agent: Bingbot), depending on your specific needs.

Here are two situations when this makes sense:

1. **Controlling aggressive or less important bots**: Some bots crawl frequently and can put an unnecessary load on your server. You might want to limit or block these types of bots.
2. **Blocking AI crawlers used for training generative models**: If you don’t want your content included in the training data for tools like ChatGPT or other LLMs, you can block their crawlers (e.g., GPTBot) in your robots.txt file.

### 3. Create a Robots.txt File and Add Directives

Use a simple text editor like Notepad (Windows) or TextEdit (Mac) to create your file and save it as “robots.txt.”

In this file, you’ll add your directives—the syntax that tells search engine crawlers which parts of your site they should and shouldn’t access.

A robots.txt file contains one or more groups of directives, and each group includes multiple lines of instructions.

Each group starts with a user-agent and specifies:

- Which user-agent(s) the group applies to
- Which directories (pages) or files the user-agent(s) should access
- Which directories or files the user-agent(s) shouldn’t access

Optionally, include a sitemap to tell search engines which pages and files are most important. Just don’t forget to [submit your sitemap](https://www.semrush.com/blog/submit-sitemap-to-google/) directly in Google Search Console.

Imagine you don’t want Google to crawl your “/clients/” directory because it's primarily for internal use and doesn't provide value for searchers.

The first group in your file would look like this block:

`User-agent: Googlebot
Disallow: /clients/`

You can add more instructions for Google after that, like this:

`User-agent: Googlebot
Disallow: /clients/
Disallow: /not-for-google`

Then press enter twice to start a new group of directives.

For example, to prevent access to “/archive/” and “/support/” directories for all search engines.

Here’s a block preventing access to those directories:

`User-agent: *
Disallow: /archive/
Disallow: /support/`

Once you’re finished, add your sitemap:

`User-agent: Googlebot
Disallow: /clients/
Disallow: /not-for-google

User-agent: *
Disallow: /archive/
Disallow: /support/

Sitemap: https://www.yourwebsite.com/sitemap.xml`

Feeling unsure?

Use a free [robots.txt generator](https://www.seoptimer.com/robots-txt-generator) to help you generate the text for your robots.txt file. Then, copy and paste the output to a text editor.

![Robots.txt file maker has field for crawl delay, sitemap, and allow/disallow for search robots.](https://static.semrush.com/blog/uploads/media/a5/4c/a54ce261336d0cd215aab52a92b9fcb2/557084628f691c47eaa733df97c35999/AD_4nXc_pdaM2A_UnmGKSepJXRBgBVr68jXUnMSbUGj-8VFpvLc7Tslj4WdrG7FfSNHqsOUVYW2btyppGbN-yW9glo5X_ViSNmxlaFaWxTK5WrC1VCujWtYfXAERcSJh6MXx5pxPVK2O.png)

### 4. Upload the File to Your Site’s Root Directory

Search engines will only read your robots.txt file if it’s placed in the root directory of your domain.

This means the file must be at the top level of your site—not in a subfolder.

To upload the file correctly, use your web hosting file manager, FTP client, or CMS settings to upload the file to the root directory (usually called “public\_html” or “/www”).

If you're using WordPress, you can use a plugin like [Yoast SEO](https://yoast.com/) or [Rank Math](https://rankmath.com/) to upload the file to your site’s root directory for you.

Just open the plugin’s settings, navigate to the robots.txt option, and upload your file.

![Create robots.txt file button is shown by navigating to Yoast SEO, tools, and robots.txt.](https://static.semrush.com/blog/uploads/media/8c/18/8c180485b557113aa3578d89db93dac5/2193bc0b0dcbf1a301658ce040762a7e/AD_4nXcVNzaMbWz-ItlIqOPCieak6YUNnaRHDXXPLtUKWQz9Ugyl32oHR0N4hyzzfJbBRghD5V21rOfnXNaKw0Uci9-8lhNBf5pDvItA0aAz1hfG6VM6JXHRe0V01FqIttjTcEpWPdUy.png)

### 5. Confirm the File Was Uploaded Successfully

Use [Google’s robots.txt report](https://support.google.com/webmasters/answer/6062598?hl=en) in [Search Console](https://www.semrush.com/blog/google-search-console/) to check for errors and confirm your rules work as intended.

In Search Console, navigate to the “**Settings**” page and click “**Open Report**” next to “robots.txt.”

![Option shown in Google Search Console.](https://static.semrush.com/blog/uploads/media/8a/46/8a46d4c0735ea2e1501a6cc15cd32bfb/0337fc63137e116c5d1ede3ec14fb60b/AD_4nXc3votE82D2bYDEb3yPdbk2xkTYOFOXn4JpD-xmP4lIrcUQ_jDIE-eFs4cN3FJhRobq--YaPmMdq1tliGE1xkUECEba5ZheaDmasDWJhhGBntWQ48qfRsFFYgqrnz6whsIaZZD6EA.png)

It should have a green checkmark next to “Fetched” under the status column.

But if there was an error, you’ll see a red exclamation mark next to “Not Fetched.” In that case, check [Google’s guidelines](https://support.google.com/webmasters/answer/6062598?hl=en#check-status) to determine what the error was and how to fix it.

It can be difficult to understand Google’s solutions to errors if you’re new to robots.txt.

If you want an easier way, run a free [SEO check](https://www.semrush.com/siteaudit/) for a quick robots.txt review on your site.

For a deeper, site-wide analysis with detailed fix instructions, use the Semrush Site Audit tool.

[Set up a project](https://www.semrush.com/kb/539-configuring-site-audit) and run an audit.

When the tool is ready, navigate to the “**Issues**” tab and search for “robots.txt.”

![Robots.txt is entered in the search bar.](https://static.semrush.com/blog/uploads/media/3a/9c/3a9ca287b601a7a7ca2717adb96970dc/0001af8f51034db7900d374fd64d42e4/AD_4nXeafEjVhOj7Oe5YB27mosH_Rz_hKYMt0fZBjCfFMM9nC_Pa_T8orF5rQTxH7m0kGo4zJ1EMZwRJSvN5ah4iLlHbK2uG5SW0OTwvZ8pG396Yn4POwML4yDpt_n5WBhi8s343qmHK.png)

Click “**Robots.txt file has format errors**” if it appears.

![The error appears in our list.](https://static.semrush.com/blog/uploads/media/c0/be/c0be5fa02f8debdf7eb5eedf24282304/7d7c1219718e8857b6c18028df200d62/AD_4nXeB8Csdn9mqf-sCJ01EmK9GC5JRe7lYIh2SA7QOnZet5wHusNyitrEy7y3otqtR3sQv3O_RmOBUQ7mdq_idP-6ygHwdvXMksnLa5InLO6_CvjLoajJhfoUEKjdM_AJTpTKWgAdzkQ.png)

View the list of invalid lines to determine exactly what needs to be addressed.

![The invalid line in this example shows a request rate is at odds with maximum rate of one page every 10 seconds.](https://static.semrush.com/blog/uploads/media/8b/cb/8bcb8170bd77f4b62532c5e0aefab3b3/6a04272d232d76e5c8fa9fc69db6cfdc/AD_4nXceBHUcfILVSVFiHchhubpkmQV0DyQFPVAxRYCZsncK-7v9VwWF4mouNh2WaIN_ddAlfZ9ArPDGDfMlBFupOb1iep9ZQ5k8s5u8_3ECse74SD6uAQgSDR032V6Na2xVUg.png)

Check your robots.txt file regularly. Even small errors can affect your site’s indexability.

## Robots.txt Best Practices

Follow these best practices to ensure your robots.txt file helps your SEO and site performance:

### Use Wildcards Carefully

Wildcards (\* and $) let you match broad patterns in URLs, and using them precisely is important to avoid accidentally blocking important pages.

- **\* matches any sequence of characters**, including slashes. It’s used to block multiple URLs that share a pattern. (Example: “Disallow: /search\*” blocks “/search,” “/search?q=shoes,” and “/search/results/page/2.”)
- **$ matches the end of a URL**. It’s used when you want to block only URLs that end in a specific way. (Example: “Disallow: /thank-you$” blocks “/thank-you” but not /thank-you/page.)

Here are some examples of how **not** to use them:

**Disallow: /\*.php** blocks every URL ending in “.php,” which could include important pages like “/product.php” or “/blog-post.php”

**Disallow: /.html$** blocks all pages ending in “.html,” which might include all your main site content

If you’re unsure, it’s wise to consult a professional before using wildcards in your robots.txt file.

### Avoid Blocking Important Resources

Don’t block CSS, JavaScript, or API endpoints required to render your site. Google needs them to understand layout, functionality, and mobile-readiness.

So, let crawlers access:

- /assets/
- /js/
- /css/
- /api/

Blocking these could cause Google to see a broken version of your pages and hurt your rankings.

Always test your site in [Google’s URL Inspection Tool](https://search.google.com/search-console?action=inspect) to ensure blocked assets aren’t interfering with rendering.

Enter a URL you want to test.

You should see a green checkmark if it’s done properly. If you see “Blocked by robots.txt,” the page (or an asset it depends on) is blocked from crawling.

![The URL is on Google and displays a green checkmark.](https://static.semrush.com/blog/uploads/media/9d/b5/9db5234f6cbdd71fd1802a7bcd83b1ec/00ed02bf733cf86e2d8ff7a417695b31/AD_4nXc6VhWqHuTFb1nc2rTTgD4xfqGD4swSIGoPOQF_WnFh_mktvXEZ77cfbfbiv4ky6mLqpu6xOeB9pWf2wSqa2qteq4R5wWflqDfMuta3vwajJkij-igryuiKSKUaHo0f84dGtpN1eA.png)

### Don’t Use Robots.txt to Keep Pages Out of Search Results

If a URL is linked from elsewhere, Google can still index it and show it in search results—even if you’ve disallowed it in robots.txt.

That means you shouldn’t rely on robots.txt to hide:

- Sensitive or private data (e.g., admin dashboards, internal reports)
- Duplicate content (e.g., filtered or paginated URLs)
- Staging or test sites
- Any page you don’t want appearing in Google

### Add Comments

Use comments to document your rules, so others (or future you) can understand your intentions.

Start a comment by adding a “#”. Anything after it on the same line will be ignored by crawlers.

For example:

`# Block internal search results but allow all other pages for all crawlers
User-agent: *
Disallow: /search/
Allow: /`

Comments are especially important for growing teams and complex sites.

## Robots.txt and AI: Should You Block LLMs?

AI tools like ChatGPT and those built on other large language models (LLMs) are trained on web content—and your robots.txt file is the primary way for you to manage how they crawl your site.

To allow or block AI crawlers used to train models, add user-agent directives to your robots.txt file just like you would for Googlebot.

For example, [OpenAI’s GPTBot](https://platform.openai.com/docs/bots) is used to collect publicly available data that can be used for training large language models. To block it, you can include a line like “User-agent: GPTBot” followed by your chosen disallow rule.

When should you allow or block AI crawlers?

**You should allow AI crawlers if**:

- You want to increase exposure and don't mind your content being used in generative tools
- You believe the benefits of increased visibility and brand awareness outweigh control over how your content is used to train generative AI tools

**You should consider blocking AI crawlers if**:

- You’re concerned about your intellectual property
- You want to maintain full control over how your content is used

Note that a new file called [llms.txt](https://searchengineland.com/llms-txt-proposed-standard-453676) is being proposed to help AI models understand what your site is about and what content is most important. But it's not exactly a translation of robots.txt for AI models.

We wanted to see how many .com websites have an llms.txt file to see how commonly used this new file type is.

This rough experiment shows that only ~2,830 of .com websites indexed in Google have an llms.txt file.

![A Google search for inurl:.com/llms.txt shows 2,830 results.](https://static.semrush.com/blog/uploads/media/e9/fd/e9fda5aa2942f443cb55e2518a851bef/a9b0dc96a3698bb9513d64d0836f415c/AD_4nXdj_1SO5VZSgM34oLm6os6_F8bPFe9IUVyNtKP6UC0LEZZHdXOzZYKNhZ4gpkSWJq7FbtUqCBoN-iVieJF0K5fVkpfiorpvJ76V6GrDDWBUQGODfzQJ4rAKFrYaVotnPyuhUM3pDw.png)

As new updates come out, llms.txt files may become more important. Only time will tell.

## Check Your Website for Robots.txt and Other Technical Issues

A well-configured robots.txt file is a powerful tool for guiding search engines, protecting your resources, and keeping your site efficient.

But it’s important to ensure your file is free from technical errors.

Use our [free SEO checker](https://www.semrush.com/siteaudit/) to automatically look for robots.txt errors, crawl issues, broken links, and other technical SEO issues.
