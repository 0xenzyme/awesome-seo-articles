---
title: "15 Crawlability Problems & How to Fix Them"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "crawlability-issues"
url: "https://www.semrush.com/blog/crawlability-issues/"
canonical: "https://www.semrush.com/blog/crawlability-issues/"
author: "Elena Terenteva, Zach Paruch, Tushar Pol, Christine Skopec"
published: "2016-09-15T13:09:15+00:00"
updated: "2024-11-28T15:33:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2024_watch"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T14:52:49+00:00"
status_code: 200
html_hash: "c94fc87447df06e8f3ca3a6afb95d7d47ad8fa0451da59df572ba6c41910e9c8"
clean_word_count: 3202
clean_char_count: 24956
---
# 15 Crawlability Problems & How to Fix Them

Ever wonder why some of your pages don't appear in Google's search results?

Crawlability problems might be the reason.

In this guide, we'll explain what crawlability problems are, how they affect SEO, and how to fix them.

Let's begin.

## What Are Crawlability Problems?

Crawlability problems prevent search engines from accessing your website's pages.

Search engines like Google use automated bots to read and analyze your pages. This process is called crawling.

![infographic by Semrush illustrating a website and search engine bot](https://static.semrush.com/blog/uploads/media/66/47/66475ddafcf197cbae93cc71032656ba/c0259976823fac982b65b6bee06b863c/AD_4nXdo9r4vv11iRoakhLFgEXR1NTH_RE_mjlDalw1kyBOZNwLxuop1AlhuESvSYZbZVR2yiDIAU939BM3jHq0XlHyKx28iDrjdYNgaHCFPr9XPgIw2qGF-f8KrRruL0x70JNFPk7EziA)

If crawlability problems exist, these bots may encounter obstacles that hinder their ability to access your pages properly.

Common crawlability problems include:

- **Nofollow links** (which tell Google not to follow the link or pass ranking strength to that page)
- **Redirect loops** (when two pages redirect to each other, creating an infinite loop)
- **Bad site structure**
- **Slow site speed**

## How Do Crawlability Issues Affect SEO?

Crawlability problems can significantly harm your SEO performance by making some or all of your pages invisible to search engines.

If search engines can’t find your pages, they can’t index them—that is, they can’t save them to a database to later display in relevant search results.

![infographic explaining "How search engines work"](https://static.semrush.com/blog/uploads/media/be/6a/be6ad1c4eca43b79a515834e706dab1f/1904424571c61ea68db29af1cc1581c4/AD_4nXcKfTA5wBW7fOV8CNUHe5dWJ_bgOHPjsKMSR-mDyZr8pAza7HDXJxL0KS3Wsf5SHwDJ34Im-ys4ashPlY9iSn64FowrsEiYhgm_nZJQyzhbLXKn9DXEV4DxkEwkFwmN4eLuE9wgYA)

This leads to a potential loss of organic traffic and conversions.

Your pages must be both [crawlable and indexable](https://www.semrush.com/blog/what-are-crawlability-and-indexability-of-a-website/) to rank in search engines.

## 15 Crawlability Problems & How to Fix Them

### 1. Pages Blocked In Robots.txt

Search engines first check your [robots.txt](https://www.semrush.com/blog/beginners-guide-robots-txt/) file to determine which pages they should or shouldn’t crawl.

If your robots.txt file looks like this, your entire website is blocked from crawling:

`User-agent: *
Disallow: /`

To fix this problem, replace the “Disallow” directive with “Allow,” enabling search engines to access your entire website:

`User-agent: *
Allow: /`

In some cases, only specific pages or sections are blocked. For example:

`User-agent: *
Disallow: /products/`

Here, all pages in the “/products/” subfolder are blocked from crawling.

To solve this problem, remove the specified subfolder or page from the “Disallow” directive.

An empty “Disallow” directive tells search engines there are no pages to disallow:

`User-agent: *
Disallow:`

Alternatively, use the “Allow” directive instead of “Disallow” to instruct search engines to crawl your entire site, as shown earlier.

### 2. Nofollow Links

The nofollow tag tells search engines not to crawl the links on a webpage.

The tag looks like this:

`<meta name="robots" content="nofollow">`

If this tag is present on your pages, search engines might not crawl the pages you link to, creating crawlability problems on your site.

To check for nofollow links using Semrush's [Site Audit](https://www.semrush.com/siteaudit/) tool:

1. Open the tool, enter your website, and click “**Start Audit**.”

![Site Audit tool with "Start audit" button highlighted](https://static.semrush.com/blog/uploads/media/bf/f8/bff8b7d2d00dcc86ff83a8e74e3acd5d/3707f92db747751340090f5fa69a2f4f/AD_4nXeXCIte08Hi7vB_j-mevMOdOpkkC71scVP4NZS-ubEDFifXgbmRPMOn8tkTZDoT2FVblfrdiDWuFTvhzXZUZcIlTDtoytfxMwb1cXyxnQ7qS2Umvxmovwhye1ziafCtxckxhRVs)

2. The **Site Audit Settings** window will appear. Configure the basic settings and click “**Start Site Audit**.”

![“Site Audit Settings” window](https://static.semrush.com/blog/uploads/media/94/6e/946e6785f0f26d902a3bae626cffbd19/b4940f408442c4b456ebfa2a8b736434/AD_4nXfT8LTCjhiKrjrQTR1cV0TwqmYoWy-VoXieT-oelvK38BASUOC9n_-B-pgqXf3fBYjgeU8lnuqExQsmt2G9w1djQ1-fUApVxj1fIa9UoLAqGkoUzyaF7sfAMvbRBmek2Pt2uo6IGw)

3. After the audit completes, go to the “**Issues**” tab and search for "nofollow."

![“Issues” tab with “nofollow” search](https://static.semrush.com/blog/uploads/media/5e/7b/5e7b58d5ffdd580df90da7b13d1179d5/968fdf183c69fd6f12279596d85f2863/AD_4nXfSzDfwbWTdDWyUaLR6ZCIrJ2yjwQOlgb1jT-8MW_ab76NBJprW4xcqO1x-NUrWgAc5N6Wt7ws8Qum2251-c3Z_TqvponhMZF2bJZaicXg3gKlXBN95xHFLSd_lGBWkUWZIww1HQA)

4. If nofollow links are detected, click “**# outgoing internal links contain nofollow attribute**” to see a list of pages with the nofollow tag.

![page with “902 outgoing internal links contain nofollow attribute”](https://static.semrush.com/blog/uploads/media/6d/da/6dda7f274347885ce301549092388261/7ec82a05e797b07af0043673261f3ac9/AD_4nXd-wLyf1J3lI70VPhOZW9aveaa5F15IPGkykGFEsBeMuMSP0w25wuIhfkBUKFT8Q-0c-vVLxcxbCNw8sqxcnu0s3DSEgAi9glPaL2o-RRHEBspctTlclaTeriXoBIi39Xd3QVpAmA)

5. Review the pages and remove the nofollow tags if they shouldn’t be there.

### 3. Bad Site Architecture

[Site architecture](https://www.semrush.com/blog/website-structure/) refers to how your pages are organized across your website.

A good site architecture ensures every page is just a few clicks away from the homepage and that there are no orphan pages (pages with no [internal links](https://www.semrush.com/blog/internal-links/) pointing to them).

This helps search engines easily access all pages.

![Site architecture infographic](https://static.semrush.com/blog/uploads/media/07/d2/07d294f081c44495731a348e8b3051cd/f45d516600b38366df49b720b8435d89/AD_4nXdPhMKNwko9QoCJl448ELSq0xcNW8jzUY2pHNTrCIeRtpu7on8f-3fgFtWWcmD-_asltVANnJv76vCF3GKwTJX4CvA-masWozSKSPGPSY_SWDITp5ienKjjf6GI4QUzNRTap71s)

However, a bad site architecture can create crawlability issues.

Consider the example site structure shown below. It has orphan pages.

Because there’s no linked path from the homepage to these pages, search engines may not find them when crawling the site.

!["Orphan pages" infographic](https://static.semrush.com/blog/uploads/media/50/92/50928a61bfdd19de90b24342a580e769/83198e53200999c383f88701b49e6bfb/AD_4nXfACh3QDFQfrjO6Mylus6VwmVrg_MN_2rThbtFGoruTBxAPZG58_3l99J-PphBtLdrPzVdL8bJlJPUSfnCY5cOMyQX1ukSgB-NOfP7Kj_6yKrzY2QGPa9kAMsQ3FvgWQKqTaHh4)

The solution is straightforward: Create a site structure that logically organizes your pages in a hierarchy through internal links.

Like this:

!["SEO-friendly site architecture" infographic](https://static.semrush.com/blog/uploads/media/af/78/af78dc5592ab08186b0be651463a9ea1/391d5c13e9e342b3393a455a297094c5/AD_4nXdfPLx5Gldq1t2w0NLujF915UX3W0Wf2Lm3itGTKstgUrEuMIjBBYtOIiGAScC8vEH0ArIbcfb6g6fy40-Wb101oW33PxQix3NmI9AaUOL727gzw0fZbf3KtDFgh7NKo-gyDqywqA)

In the example above, the homepage links to category pages, which then link to individual pages on your site.

This provides a clear path for crawlers to find all your important pages.

### 4. Lack of Internal Links

Pages without internal links can create crawlability problems.

Search engines have trouble discovering pages that lack internal links.

To avoid these issues, identify your orphan pages and add internal links to them.

How can you find orphan pages?

Use Semrush's [Site Audit](https://www.semrush.com/siteaudit/) tool.

[Configure the tool](https://www.semrush.com/kb/539-configuring-site-audit) to run an audit. Then, go to the "**Issues**" tab and search for "orphan."

The tool will display any orphan pages on your site.

![“Issues” tab with “orphan” search](https://static.semrush.com/blog/uploads/media/44/b8/44b86eb6b56bd8047822861bb3d7bb1d/515bb2322f713e7df14357f60b8109e4/AD_4nXdbTZo9N2KOApixpNzqCgymJWZZICgP1ZebY9QRxfZSgS2ucASfb6GZOIkf1jGWmCzr1Sz5WCv1_cUbwdIPsuMlvum0IggMp92H64wdftidBGXhGSQEV2dx-GlTZP7DLEftxd5W)

To fix this problem, add internal links to orphan pages from other relevant pages on your site.

### 5. Bad Sitemap Management

A [sitemap](https://www.semrush.com/blog/website-sitemap/) lists the pages on your site that you want search engines to crawl, index, and rank.

If your sitemap excludes any pages you want found, those pages might go unnoticed, leading to crawlability issues.

Use a tool like [XML Sitemaps Generator](https://www.xml-sitemaps.com/) to include all pages meant to be crawled.

To generate a sitemap, enter your website URL into the tool. It will automatically create the sitemap for you.

![XML Sitemaps Generator search bar](https://static.semrush.com/blog/uploads/media/60/55/60551bc55da8b7dbed15f7bae88e7f2e/f8e112d0cd995fcca8728aa49fc013b3/AD_4nXeDYO-_sMfDWGEmVaSzvfwW6T4hSB1R4Gdgs4pqMJiyQ2w2RdliGe4d8KA0ksUIbRJJCDjyEB7BEYFVwmx9UJlzBfs53cmah96JaD2DRtOv8y3n_Kt_KBI2yE1vhY26NsIGDbLpQA)

Save the file as "sitemap.xml" and upload it to the root directory of your website.

For example, if your website is www.example.com, your sitemap URL should be www.example.com/sitemap.xml.

Finally, submit your sitemap to Google through your [Google Search Console](https://www.semrush.com/blog/google-search-console/) account.

[Access your account](https://search.google.com/search-console), click "**Sitemaps**" in the left-hand menu, enter your sitemap URL, and click "**Submit**."

!["Add a new sitemap" in Google Search Console](https://static.semrush.com/blog/uploads/media/e6/da/e6da63568716762729af947d9a33bb5b/f7eca7d5c03e92704a9a7633499487b1/AD_4nXci80NAuJ8Ce-nCCmB4dzGh_4N5yUMN7e2TwBYu_MhZ23PP_abRNCo8S2KvKccdEOa0x1rcc2TeNdLZSl95oJBpw8I_6XYZzKMWFsUZ8UEQmnHZn9K57zftUmNGpuA8ba8K928byg)

### 6. ‘Noindex’ Tags

A “noindex” [meta robots tag](https://www.semrush.com/blog/meta-tag/) instructs search engines not to index a page.

The tag looks like this:

`<meta name="robots" content="noindex">`

While the noindex tag is intended to control indexing, it can create crawlability issues if left on your pages for a long time.

Google treats [long-term "noindex" tags](https://www.youtube.com/watch?v=9GNg8R-X8LQ&t=54m51s) as nofollow tags, as confirmed by Google's John Mueller.

Over time, Google will stop crawling the links on those pages entirely.

If your pages aren’t getting crawled, long-term noindex tags might be the culprit.

Identify these pages using Semrush's [Site Audit](https://www.semrush.com/siteaudit/) tool. [Set up a project](https://www.semrush.com/kb/539-configuring-site-audit) in the tool to run a crawl. Once complete, go to the "Issues" tab and search for "noindex."

The tool will list pages on your site with a "noindex" tag.

![“Issues” tab with “noindex” search](https://static.semrush.com/blog/uploads/media/85/4c/854ccc8e69b61305cb6e9ae658d24170/fbfa86348b0f16d6f1e2578e83866c36/AD_4nXdhaUAjCDhhn4Zi2qShav4I6pq1faKbUrMhg-GwC9llwcteIgDz3YrQTKqSnixAI9VZLGrmylyiLxN1FN6dffptPrJcwsQ5C2TdPjTofwOTGqNQpLEnAtYVuhBuY_E1dYp5yMSTOA)

Review these pages and remove the "noindex" tag where appropriate.

### 7. Slow Site Speed

Search engine bots have limited time and resources to crawl your site, known as a [crawl budget](https://www.semrush.com/blog/crawl-budget/).

Slow site speed causes pages to load slowly, reducing the number of pages bots can crawl in a session. As a result, important pages might be excluded.

To solve this problem, improve your website's overall performance and speed.

Start with our guide to [page speed optimization](https://www.semrush.com/blog/page-speed/).

### 8. Internal Broken Links

Internal [broken links](https://www.semrush.com/blog/broken-link/) are hyperlinks that point to dead pages on your site.

They return a 404 error page.

![example of “404 error” page](https://static.semrush.com/blog/uploads/media/8a/75/8a75874710b280dbb50c00d2f117c21e/49d72582ab1cbe7cf4026b670a0d9ca6/AD_4nXcLBqgDAQxej5NARVhDtFh592KQxVTcmnS_PROcDVqW8V_CLbtmys9kvEe9H8QjuCKcCQX21BHlQG7fWiLOLnsgATMJ_TRroRDsSyVnjcaIWrJpEbpqw5mVOLWZzb-1_gOetjqjQQ)

Broken links can significantly impact website crawlability because they prevent search engine bots from accessing the linked pages.

To find broken links on your site, use the [Site Audit](https://www.semrush.com/siteaudit/) tool.

Navigate to the "**Issues**" tab and search for "broken."

![“Issues” tab with “broken” search](https://static.semrush.com/blog/uploads/media/d3/76/d37656c532efde148eed1a0692687707/c75c7d8f10c58f842184694f474203dc/AD_4nXcnl6GwtuzI6kfEkXnHgGP16g0HKBsx8Lvj2wmj3wCnNAzrT4lHlGHNTdbrrO6ekxflTPbF-BZu8yih_oEdmScZ0QLx8ExEYY_c-E3k7nwlsMnKKcte_AEWBUVCwX_ZIqWK5JSC)

Click “**# internal links are broken**,” and you’ll see a report listing all your broken links.

![report listing “4 internal links are broken”](https://static.semrush.com/blog/uploads/media/70/49/70493f3b6e2735a90f91c7cbab196862/22ea2fc1cdaa57f48f9f44572e1754d8/AD_4nXetbfF0mbw1oTEkcWHN85Zg7kLrpWrd7IN4EPtF-h3zzaAWcL6bqVSMOjaNVw9JZrxN4tD2vTe-Kmk6OYhvc4OtFERSppKPO7tmsthXOTHj13d5igB2ijd0b0EMGCJuQAD4vd1ELQ)

To fix these broken links, substitute a different link, restore the missing page, or add a [301 redirect](https://www.semrush.com/blog/301-redirects/) to another relevant page on your site.

### 9. Server-Side Errors

Server-side errors, such as [500 HTTP status codes](https://www.semrush.com/blog/http-status-codes/), disrupt the crawling process because the server couldn't fulfill the request.

This makes it difficult for bots to crawl your website's content.

To identify and fix server-side errors, use Semrush's [Site Audit](https://www.semrush.com/siteaudit/) tool. Navigate to the "**Issues**" tab and search for "5xx."

If errors are present, click on "**# pages returned a 5XX status code**" to view a complete list of affected pages.

![“Issues” tab with “5xx” in the search bar](https://static.semrush.com/blog/uploads/media/86/11/8611c39503772030604125be3672b11f/699416252bea96781465329e27596716/AD_4nXeGntHQJ_RhMdYsViymXV8hLdy6Ravsrh9qbJnXxxDOHcTFcqJpkTcoYeBKEn130NBtkS-Q5aLQIyOpWA0gyCP611p5QEPveUEARvgb4u-tEV_JWbIludsO1svgYourz7_cZYCg3Q)

Then, send this list to your developer to configure the server properly.

### 10. Redirect Loops

A redirect loop occurs when one page redirects to another page, which then redirects back to the original page, creating a continuous loop.

!["What is a redirect loop" infographic](https://static.semrush.com/blog/uploads/media/c4/82/c48236c1180237e633c54a6230f16752/24ca55c3c4d3cd699c8eac327efac61d/AD_4nXd1l1g_PKwLO4fyIXoTjDo0xpj6fFw1qhyZAfbrDlK60Z-KSbxz6s0nlDz0deRbk8RqluJBVk5S-fxv23XG2_tKQj0ePskyK8bChrLGnd6aHhIzujkGtsO1e4vnys5LOlomJLpMBA)

Redirect loops prevent search engine bots from reaching the final destination because they become trapped in an endless cycle of redirects between two or more pages, wasting valuable crawl budget time that could be spent on important pages.

To identify and fix redirect loops on your site, use the [Site Audit](https://www.semrush.com/siteaudit/) tool.

Navigate to the "**Issues**" tab and search for "redirect."

![“Issues” tab with “redirect” search](https://static.semrush.com/blog/uploads/media/ce/ea/ceeaca64fcde409e41614cd9031cefd8/fa20c21307932f839ceed8e4bfa984c7/AD_4nXeE44m4fM4B-B_Mje1ALei6tzypn8L3j52-SnacAKLyC4imy50oORENwbITgoTYkrhzumYc5yrrqyNZPLhPcGDjB7zhOERiwKCCGH4zVu45IMiD6rzQmwnEGSV92GVafMdcqIOy7w)

The tool will display any redirect loops and offer advice on how to address them when you click on "**Why and how to fix it**."

![results show redirect loops with advice on how to fix them](https://static.semrush.com/blog/uploads/media/a5/47/a54767e9212621f69e94b92c22ce3e88/eed63870cf1424c7e1f2bf511eea4b0c/AD_4nXdrw7YnVt4Jxv3D0pS37aG0goRsrM7OCO57mZ75xHM4gn7z5cwhvOEuAUsiztmkYAvs3TvAiUrpGk6ohs3G3y65nyM_9AOUx0tkQWdm8EH2utDj-e8PMk3k4FxRtlDaipNXB65J)

### 11. Access Restrictions

Pages with access restrictions, such as those behind login forms or paywalls, can prevent search engine bots from crawling them.

As a result, these pages may not appear in search results, limiting their visibility to users.

In some cases, restricting access to certain pages makes sense.

For example, membership-based websites or subscription platforms often restrict pages to paying members or registered users.

This allows the site to provide exclusive content, special offers, or personalized experiences, creating a sense of value and incentivizing users to subscribe or become members.

However, if significant portions of your website are restricted, this becomes a crawlability mistake.

Assess the need for restricted access for each page, and keep restrictions only on pages that truly require them.

Remove restrictions from those that don’t.

### 12. URL Parameters

[URL parameters](https://www.semrush.com/blog/url-parameters/), also known as query strings, are parts of a URL that follow a question mark (?) and help with tracking and organization.

For example: example.com/shoes?color=blue.

**How can URL parameters impact your website's crawlability?**

URL parameters can create an almost infinite number of URL variations.

This often occurs on ecommerce category pages; when you apply filters like size, color, or brand, the URL changes to reflect these selections.

If your website has a large catalog, you may end up with thousands or even millions of URLs.

If these parameterized URLs aren’t managed well, Google may waste crawl budget on them, which may result in some of your important pages not being crawled.

You need to decide which URL parameters are helpful for search and should be crawled.

You can do this by understanding whether people are searching for the specific content generated when a parameter is applied.

For example, when shopping online, people often search by color, such as "black shoes."

![Keyword Overview tool's dashboard showing metrics for "black shoes"](https://static.semrush.com/blog/uploads/media/60/c8/60c85b5dd5039b88c1bba5ffaa8f1725/7e428bc692d714f6a25e27c65a391be5/AD_4nXf__UPxfSGqDNsXaXiV7Svwjiria8B5jE_ezOFAZtH_POm8p5-vgdCp0GRNiAM1_76bbOYIfLB2Q3vvNPkYugFyjGxf7WFWR8MRVCpWiKhCNMeFsQVIcNNYCg8vb-vO8_X-REKasw)

This means the "color" parameter is helpful, and a URL like example.com/shoes?color=black should be crawled.

However, some parameters aren’t helpful for search and shouldn’t be crawled.

For example, the "rating" parameter filters products by customer ratings, such as example.com/shoes?rating=5.

Few people search for shoes by customer rating.

![Keyword Overview tool's dashboard for "5 start rated shoes" shows no results](https://static.semrush.com/blog/uploads/media/72/bb/72bb02c3a7d706369080e3ebd880dbc6/2fe526ff3cf07412476b8c6f454922aa/AD_4nXeP1ODMzhPaC_i8wxplNpUlCUeHEQCyXo1tDPrf8If_Wwu4PDzMp15vES2GzQylI7AnKcsyEe0brWA6c7_VsmGirA24od-RAGzqB-6auYTIk1Sw6gbjCI9yni6mWIzAp9hqjKeeyw)

Therefore, you should prevent URLs that aren’t helpful for search from being crawled, either by using a robots.txt file or by adding the nofollow tag to internal links pointing to those parameterized URLs.

This will ensure your crawl budget is spent efficiently and on the right pages.

### 13. JavaScript Resources Blocked in Robots.txt

Many modern websites use [JavaScript](https://www.semrush.com/blog/javascript-cheat-sheet/), which is contained in .js files.

Blocking access to these .js files via robots.txt can create crawlability issues, especially if you block essential JavaScript files.

For example, if you block a JavaScript file that loads the main content of a page, crawlers may not be able to see that content.

Review your robots.txt file to ensure you’re not blocking important JavaScript files.

Alternatively, use Semrush's [Site Audit](https://www.semrush.com/siteaudit/) tool. Navigate to the "**Issues**" tab and search for "blocked."

If issues are detected, click on the blue links.

![Issues with blocked internal and external resources in robots.txt found in Site Audit tool](https://static.semrush.com/blog/uploads/media/eb/4d/eb4d33eb0ab1eecf0962fce623f25765/1b56851d55c00699cb981587bb1d9157/AD_4nXeFVExCH7cfFc-pP4l2-svUWjWXrR4y0rZRVN96b7ulWDYM7_oBVBeRNfhhD2wr1EiNcK-u7R1eEfe3DItkoDOgFLW5699-K1JK6Hg2mFCxWmi97hxmGO-J8r7WMHavTssLQvrgwA)

 You’ll see the exact resources that are blocked.

![A list of blocked resources in Site Audit tool](https://static.semrush.com/blog/uploads/media/35/95/3595781e7ce29130ccb43ad945d5fe3a/743a4bd21249caa50918031e92e72d06/AD_4nXcGxQIgBatbekNE2ZXEfA1ninaa7naTLsFRe07zRSByYKzSjSr1PeJxs5mgQPZIlpT_R-U2jkRA9BlhWkO5U3JlG9ccKQtMOscn5rJ370zc4Ka3QEPQeRgaaHAwmhy_QeQI0o13)

At this point, consult your developer.

They can identify which JavaScript files are critical for your website's functionality and content visibility, and shouldn’t be blocked.

### 14. Duplicate Content

Duplicate content refers to identical or nearly identical content that appears on multiple pages of your website.

Let’s say you publish a blog post that is accessible via multiple URLs:

- example.com/blog/your-post
- example.com/news/your-post
- example.com/articles/your-post

Even though the content is the same, the different URLs cause search engines to crawl all of them.

This wastes crawl budget that could be better spent on other important pages.

Use Semrush's [Site Audit](https://www.semrush.com/siteaudit/) tool to identify and eliminate these issues.

Go to the "**Issues**" tab and search for "duplicate content." The tool will show if any errors are detected.

![4 pages with duplicate content issues found in Site Audit](https://static.semrush.com/blog/uploads/media/98/46/9846c10b9640cfd93b4d4849e28ab8f5/a18463f29ef6cc871f5af7f353b5c8ab/AD_4nXfpq1xEcQ8ijtXuV5ZRPY7OuXXaXCxRUVkkoyheORUHHR8Si0Izd8JhrE_ZSdrx_hjn-zU-HJqpVLQ-14m-tzAyFZDEGkjQOz0Mzz-n6rC4wmTyHqRkcdgtTQ0LLtOFd5hZmFXU)

Click on the "**# pages have duplicate content issues**" link to see a list of all affected pages.

![A list of pages that have duplicate content issues](https://static.semrush.com/blog/uploads/media/e1/f0/e1f07069625214e4c273bf5d416cd048/343dd06de94aa6807b1c3691f8bb8001/AD_4nXeLzbtvijvX0end5Ldh5EFmFXpq-rktMRj2b8lBo0jVknaiAvNih-p0emKMmJ9e-mvfDupHxnUwF3RALIcc0Z3zAnTtkFPI5kf9Mhy1IPJDMzW6_kD3qrtFWv6zmh1VPMSyC17Lvg)

If the duplicates are mistakes, redirect those pages to the main URL you want to keep.

If the duplicates are necessary—for example, if you have intentionally placed the same content in multiple sections to address different audiences—you can implement [canonical tags](https://www.semrush.com/blog/canonical-url-guide/).

Canonical tags help search engines identify the main page you want to be indexed.

### 15. Poor Mobile Experience

Google uses [mobile-first indexing](https://www.semrush.com/blog/mobile-first-indexiing/), which means it looks at the mobile version of your site over the desktop version when crawling and indexing.

If your site takes a long time to load on mobile devices, it can affect your crawlability. Google may need to allocate more time and resources to crawl your entire site.

If your site is not responsive—that is, it does not adapt to different screen sizes or work properly on mobile devices—Google may find it harder to understand your content and access other pages.

To address this issue, review your site to see how it works on mobile devices.

Run a free [SEO check](https://www.semrush.com/siteaudit/) for a quick snapshot of your page speed. To find slow-loading pages across your entire site, use the Semrush Site Audit tool.

Navigate to the "**Issues**" tab and search for "speed."

The tool will show any errors if you have affected pages and offer advice on how to improve their speed.

![An example of why and how to fix a slow page load speed issue](https://static.semrush.com/blog/uploads/media/f0/cd/f0cdd6e3faf7ccd7a932c48d04558bbd/625675eb3c358fc2846e66b36dd19a3a/AD_4nXcKWyaY1OI5Gz5oBVfR7sg83R72HNzQYPPFsLDxoIPvaasiSo_OSjhaJTkZItajR90m3uZwU0iHprFYyecCnpkTFfQu93yanMPCynb2rL69qPihAesazmi4mRR6pDQLr_cXBqeobA)

## Stay Ahead of Crawlability Issues

Crawlability problems aren’t a one-time fix.

Even if you solve them now, they might recur in the future, especially if your website is large and undergoes frequent changes. Regularly monitoring your site's crawlability is essential.

Use the free [website audit](https://www.semrush.com/siteaudit/) for a quick crawlability check on your homepage. Or, schedule automatic weekly audits across your entire site using the Semrush Site Audit tool.

Navigate to the audit settings for your site and turn on weekly audits.

![Schedule weekly audits under "Site Audit Settings" window](https://static.semrush.com/blog/uploads/media/f3/5c/f35c53017c81b9f056aec19d098829b0/fde0143391e80a105eb84081494e054d/AD_4nXdNO4Wd8IXMGC6Gcr-XrZt2i1nUkrcWFbAGHZ_zxqnmQ3EuPTOG51mmMg2hPXXp6ZJ-hbQfwPJp8cWNht-UDtmVvhPePP0zwUFfx7nuBJ5LDiEMbXuLKz1O9jLMSoc8FOfDjkGTsg)

This way, you can ensure that any crawlability issues are promptly identified.
