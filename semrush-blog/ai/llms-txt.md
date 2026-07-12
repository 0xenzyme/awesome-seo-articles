---
title: "What Is LLMs.txt & Should You Use It?"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "llms-txt"
url: "https://www.semrush.com/blog/llms-txt/"
canonical: "https://www.semrush.com/blog/llms-txt/"
author: "Tushar Pol, Christine Skopec, Connor Lahey"
published: "2025-11-26T07:30:00+00:00"
updated: "2025-11-26T07:30:00+00:00"
categories:
  - "AI"
freshness_reasons: []
schema_genre: "AI"
fetched_at: "2026-06-12T17:29:34+00:00"
status_code: 200
html_hash: "14385fae9ab08135b826283025ea36feed306756422397d3525e43b3a0bd0bfe"
clean_word_count: 2126
clean_char_count: 14253
---
# What Is LLMs.txt & Should You Use It?

## What Is LLMs.txt?

The llms.txt file is a proposed standard meant to help large language models (LLMs) better understand and use content from websites.

Here’s the [official specification](https://llmstxt.org/):

![The background for the specification says, "Large language models increasingly rely on website information, but face a critical limitation: context windows are too small to handle most websites in their entirety. Converting complex HTML pages with navigation, ads, and JavaScript into LLM-friendly plain text is both difficult and imprecise. While websites serve both human readers and LLMs, the latter benefit from more concise, expert-level information gathered in a single, accessible location. This is particularly important for use cases like development environments, where LLMs need quick access to programming documentation and APIs."](https://static.semrush.com/blog/uploads/media/09/8a/098a9aed7d200395fc96a4c51588426e/6c6f329f69e650d18952af36bdd48b83/AD_4nXebf8je8Pwgxns_G-KPhE7EH2RHP1mHta3lmgXCDwdPTgwtm58-50kqNwMwAZnM6s9E8SWGPKipdali9aqSjzVIrvhxEVPIG_1GT_0s2qPfn-To_bCZ6-hBUaLOUNEginCTn81DVw.png)

The idea is pretty straightforward: Instead of letting AI crawlers wander around your site, you give them a curated list of your most important content. To tell AI what content on your site it should actually pay attention to.

We already have standards like [robots.txt](https://www.semrush.com/blog/beginners-guide-robots-txt/) and [sitemaps](https://www.semrush.com/blog/xml-sitemap/) to help search engines navigate websites more efficiently. What’s different about llms.txt is that it’s specifically designed for AI models that might use your content to answer questions or generate responses for users.

There’s also speculation that implementing llms.txt could give websites more visibility in AI-generated responses and potentially drive more referral traffic.

Before we unpack llms.txt and determine whether it’s worth implementing, let's understand why there’s even a need to create another web standard.

## What Problem Is LLMs.txt Trying to Solve?

llms.txt is designed to help AI crawlers browse websites more effectively. Right now, these crawlers run into two major challenges:

- **Modern websites are hard to read.** Most AI crawlers can only read your pages’ basic HTML—not content that gets loaded by JavaScript. That means llms.txt provides a clear, structured format that helps AI crawlers quickly digest the information.
- **Most websites have an overabundance of information.** When AI crawlers visit your website, they don't necessarily know what's important. If they spend time scraping pages that aren’t useful (like older blog posts), they may generate responses based on suboptimal information—llms.txt helps solve this problem.

llms.txt may also reduce the inefficiencies in large language model training.

There’s a massive computational cost involved in training LLMs. With llms.txt guidance, LLMs are less likely to waste resources on irrelevant content.

## How Are LLMs.txt Files Structured?

According to the proposed standard, llms.txt files should be structured and formatted in Markdown.

Markdown is a lightweight markup language that uses plain text formatting syntax to create structured documents. (It's the same format developers use in GitHub README files, and it’s easily parseable by AI systems.)

Some common Markdown elements you'll use in your llms.txt file include:

- # for the H1 heading, ## for H2s, ### for H3s, and so on
- > for blockquotes to highlight important descriptions
- - or \* for bullet points in unordered lists
- [text](url) for hyperlinks to your content
- : for adding descriptions next to links to help explain what they lead to
- ``` for code blocks when sharing technical examples

The official llms.txt specification provides a very basic example of how your file might look. But if your website is large or complex, you might want to add more structure—using H3s and H4s to create subsections, incorporating tables to organize data, or including code snippets to demonstrate API use.

There's nothing wrong with that. Markdown files are completely readable by AI crawlers, so you’re safe as long as you're using valid syntax. The additional structure might actually give AI crawlers more context.

Here's a simple example following the basic specification:

`# Company Name
> Brief description of what your company does

## Products
- [Product 1](https://example.com/product-1): Description of this product
- [Product 2](https://example.com/product-2): Description of this product

## Documentation
- [Getting Started](https://example.com/docs/getting-started): Introduction to our platform
- [API Reference](https://example.com/api): Complete API documentation`

## Are Brands Using the LLMs.txt Standard?

Yes, some SaaS and developer-focused companies are already using llms.txt files on their websites.

However, the overall adoption is pretty niche. According to NerdyData, only [951 domains](https://www.nerdydata.com/reports/llms.txt/b012b7e8-c50d-45e3-8719-0d72f097c3db) (a tiny fraction of the web) had published an llms.txt file as of July 2025.

Here are some example companies:

|  |  |  |
| --- | --- | --- |
| **Brand** | **What the File Focuses on** | **The Overall Structure** |
| [Hugging Face](https://huggingface-projects-docs-llms-txt.hf.space/diffusers/llms.txt) | Developer docs | Uses multiple levels of headings (#, ##, ###, ####) to break content into separate sections. It also includes full code examples, lots of links, and helpful notes throughout. Overall, it feels like a comprehensive knowledge base. |
| [Vercel](https://ai-sdk.dev/llms.txt) | Developer docs | Starts with descriptive lines at the top, such as title:, description:, and tags: to give an idea about the particular documentation that follows. And it uses clear headers (#, ##, ###) to organize content into logical sections. Under each section, you’ll find step-by-step instructions and practical code examples. |
| [Zapier](https://docs.zapier.com/llms.txt) | Developer docs | Uses a small number of headings and creates a very basic structure. It mostly consists of a long list of links and descriptions next to them to help explain what they lead to. |
| [Cal.com](https://cal.com/docs/llms.txt) | Developer docs | Uses headings at the top (#, ##) and then jumps straight into a very long list of links. The links aren’t grouped into sections, and there are no subheadings, summaries, or descriptions. |

Notice how differently each company approaches their llms.txt file. They each use a different structure.

There’s nothing wrong with this. As long as they’re using valid Markdown, the file is machine-readable and can be easily processed by AI systems.

Also, none of these companies has a file that’s focused on their website as a whole. That’s a personal choice they made. You can create a file that’s focused on your entire site or just one specific section.

## Should You Use LLMs.txt on Your Site?

Using llms.txt is probably not worth your time right now, unless you’re just curious and want to experiment.

llms.txt is currently just a proposed standard rather than something that's actually being used by the major AI companies.

None of the LLM companies like OpenAI, Google, or Anthropic have officially said they're following these files when they crawl websites.

Google’s John Mueller also confirmed this on Bluesky:

![The post says, "FWIW no AI system currently uses llms.txt."](https://static.semrush.com/blog/uploads/media/2e/68/2e683e321e6aa33760da8663e08a25c3/9de776ec93f3ae35592578abcfd1a148/AD_4nXdm1njLH-b0vtNGsfy4QrTqrseHaiU0fjeKTJ-nLBSlQkGa1W2U-v0EscGD88RP-euCGtDqJppyKKRPgAaEDcNe_NhaZLRjBcEcBgkPgPlPnFNXKfKdCmBtW6RZBfmkRIfOrP6aNA.png)

That said, there are some interesting signals.

For example, Anthropic has published an llms.txt file on their own website. That doesn’t mean their AI crawler is actually using these files—but it suggests they’re probably at least open to the idea.

We're still in the early speculation phase where people are implementing the file and hoping it might become useful someday.

Back in March 2025, we implemented this file on one of our sister sites, Search Engine Land, to see whether it offers any meaningful advantages in terms of AI visibility and traffic.

In our testing, we didn't find a correlation between implementing llms.txt and improved performance in AI results.

LLM traffic to Search Engine Land has grown over the last couple of months, but that's due to other factors rather than the llms.txt file.

We also analyzed the server logs to see whether AI crawlers were actually accessing the file. From mid-August to late October 2025, the llms.txt page received **zero visits** from Google-Extended bot (Google's AI crawler), GPTbot (OpenAI's crawler), PerplexityBot, or ClaudeBot.

While traditional crawlers like Googlebot and Bingbot did visit the file, the file received only a few hits. That means they didn’t treat the file with any special importance.

If you also want to experiment with llms.txt on your own site, follow the step-by-step instructions below on how to implement it.

## How to Create an LLMs.txt File (Step by Step)

This is technical, so it’s best to involve a developer in the process as you follow these three steps:

### 1. Decide What Content You Want to Feature

Before creating a file, determine which pages or sections of your website should be highlighted for AI crawlers.

Let's say you want to create an llms.txt file for your whole website. At the very least, consider your:

- Product or service pages
- Up-to-date blog posts
- Pricing page
- About us page
- Contact page

These are typically the pages that will give AI a good idea of what your business does and how you help customers.

### 2. Create the File

Open a text editor like Notepad or Visual Studio Code and create a new file named llms.txt.

You need to format the file using Markdown. Again, developers are helpful for creating the file.

Here’s how the file’s structure could look:

`# Website Name
> Brief description of your website

Important notes:
- Key differentiator or important detail about your business
- Another important note about what you do or don't do
- Third key point that helps define your offering

## Products
- [Product name 1](https://example.com/product-1): Short description of your product's main feature and benefit
- [Product name 2](https://example.com/product-2): Short description of your product's main feature and benefit
- [Product name 3](https://example.com/product-3): Short description of your product's main feature and benefit

## Blog Content
- [Blog post title 1](https://example.com/blog-post-1): Brief description of what this blog post covers and why it's useful
- [Blog post title 2](https://example.com/blog-post-2): Brief description of what this blog post covers and why it's useful
- [Blog post title 3](https://example.com/blog-post-3): Brief description of what this blog post covers and why it's useful

## Company
- [About us](https://example.com/about): Company background, mission, and team information
- [Contact](https://example.com/contact): How to reach our team and get in touch
- [Pricing](https://example.com/pricing): Overview of plans, features, and costs for using our products`

### 3. Upload the File to Your Website

Place your completed file in the right location so AI crawlers can theoretically find it.

The exact location depends on the scope of your llms.txt file:

- If it covers your entire website, upload it to your root directory (i.e., “https://[yourdomain].com”) so it's accessible at “https://[yourdomain.com]/llms.txt”
- If the file is specifically about documentation, place it in the corresponding subdirectory (e.g., “https://[docs.yourdomain.com]/llms.txt)

You’ll need a developer’s help to actually upload the file. This file has to be placed on your server—usually through your web hosting control panel, such as cPanel.

Log in to your hosting provider and then navigate to cPanel > File Manager.

![File manager option is highlighted.](https://static.semrush.com/blog/uploads/media/51/5a/515a5e1a1845d19bd59437332c07f514/924c21e96fc0d929bf18a2ac57e8f763/AD_4nXeHJ7-kCcYuVT490lK-f91vhIagwoxiTmVpEUdReat0uAJlGCtnvj9BCsJaybZsozmM90AFX1nWmgNHqqiX52K8Ehw3r0UkWFvkvpTvAzGXwXO9W3saMUGZnVCpkTuJig4UB6zZEA.png)

Then go to the correct directory. If your llms.txt file is meant for the whole site, go to the public\_html/ folder. (That’s the root directory for most domains.)

If it’s for a subdomain like “https://[docs.yourdomain.com],” navigate to the folder assigned to that subdomain—often named /docs/ or similar.

![The public_html folder is highlighted.](https://static.semrush.com/blog/uploads/media/8d/2b/8d2bbe5cc15acfe12a5777ae38c4fd45/1a04da4a6c16db7215b0e4c7608c37ed/AD_4nXc-Zy2ZpdxZ3FYTuJh2ztZZ2mTchIL_-IRsD275897BlJ7Bg4mZBn99zSCb4wxAGmqLLhFKs-kXcL9J1UNxkl3eG67gn-oHZIRFqg7_NUS1tH-PosPJ-k2aRRCu_6XZPoFfHHl3qw.png)

Upload your llms.txt file there and save the changes.

![The upload button is highlighted.](https://static.semrush.com/blog/uploads/media/da/47/da476bd2981786d5dd80388ea60453df/54d53b91bec094586bf013860073caec/AD_4nXe4llBJ__rt6a57HYtRNPOkOe6fqbAVK55AEetN0Fo-M8-zp1ekBORzm8QAte5I77W2vR5fU93HktgiXt5KyOdIMGoSKjxVxMyGeEZ6JU41KqekiJz4P-oN3q5nnrmokGUVcHmQ.png)

Once the file is uploaded, confirm everything is working by opening a new tab and visiting the URL directly.

You can also run a quick audit of your website in Semrush’s [Site Audit](https://www.semrush.com/siteaudit/) tool to confirm that your llms.txt is being picked up correctly.

![llms.txt file was crawled and found.](https://static.semrush.com/blog/uploads/media/31/b8/31b81d95dbf370f1c986e193588345a8/2d71a24d7f782918d5faf6f21a400584/AD_4nXec03MlEXvoiAMOqAnAN8Psi_vdiRcJhX9v3JaDG9IdOp4mXzyouQigErnxoGE1bP_7vOvLrR6-rDRI4C-UxwjZTjFaeEj49STi6cRrcz8r0FFr_EH_n4Bhrc3RAfcLF6lYSX_DjA.png)

In this case, an llms.txt file is found, so the “Not found” notice is inactive (grayed out).

Also, don’t forget to keep the file updated over time. Regularly review the links to remove outdated pages. And add links to the new content you add to the website.
