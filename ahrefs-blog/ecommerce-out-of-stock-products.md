---
title: "How Should You Handle Out-of-Stock Products? It Depends"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "ecommerce-out-of-stock-products"
url: "https://ahrefs.com/blog/ecommerce-out-of-stock-products/"
canonical: "https://ahrefs.com/blog/ecommerce-out-of-stock-products/"
author: "Patrick Stox"
published: "2022-03-16T05:08:28+00:00"
updated: "2024-02-02T17:03:22+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2024_watch"
fetched_at: "2026-06-12T11:28:15+00:00"
status_code: 200
html_hash: "e19d23f8401ed4d5a26000253d5159b486b7f15a305c2b73f1ae4e4e45211fb3"
clean_word_count: 1429
clean_char_count: 8072
---
# How Should You Handle Out-of-Stock Products? It Depends

An out-of-stock (OOS) event, or stockout, happens when a business runs out of inventory for a product that a customer wants to purchase. This can happen online or in physical stores.

Though it’s a joke in the SEO community, “it depends” is really the answer when dealing with out-of-stock products on e-commerce websites. There are many situational decisions, with each having trade-offs, when it comes to SEO and user experience.

Many content management systems have built-in rules for handling out-of-stock products, but that logic can often be changed. Some setups may have no built-in logic at all. In these cases, you get to make the rules and work with your developers to implement what you want.

Let’s look at the different scenarios.

## Permanently out of stock

With permanently out-of-stock products, you know the products are gone and won’t be back. Does that mean you should get rid of the pages? Not necessarily. You have a few options here.

### Option 1. Redirect the page

If you have a similar product that you want to push people toward, you may want to [301 redirect](https://ahrefs.com/blog/301-redirects/) the old product to the new product. This will also maintain any link value if the pages are similar enough.

If the pages are not similar enough or you redirect to a category page or your homepage, then these pages may be treated as a soft 404 and the value from links may not be preserved. If these other locations are where you want users to go, then do the redirect anyway. It’s possible the links will still pass value.

Because most websites have removed many products in the past, you may want to see if there are any opportunities to redirect old pages to relevant, current pages and reclaim the value from the links.

Here’s how to find those opportunities:

1. Paste your domain into Ahrefs’ [Site Explorer](https://ahrefs.com/site-explorer) (also accessible for free in [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools))
2. Go to the **Best by links** report
3. Use the response code filter and check “404 not found” and “410 gone”

I usually sort this by “Referring domains” or “UR” to look for top opportunities.

**Best** **by links** report.

When redirecting a page, many systems will automatically remove [internal links](https://ahrefs.com/blog/internal-links-for-seo/) from categories, [facets](https://ahrefs.com/blog/faceted-navigation/), [sitemaps](https://ahrefs.com/seo/glossary/sitemap/), and internal search pages. In some systems, you may need to remove these links manually or there may be additional links from blog pages or elsewhere that you’ll want to remove.

To find these links, check the **Links** report in Ahrefs’ [Site Audit](https://ahrefs.com/site-audit), which is also free if you sign up for [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools). Click into the area marked “Redirect” on internal links to get a list of the redirected links and the pages that have those links.

Internal links that redirect.

### Option 2. Delete the page

If you are removing a page and there is no relevant, current product, you may want to simply delete the page and return a [404 or 410 status code](https://ahrefs.com/blog/http-status-codes/).

As we mentioned in the first option, you also want to make sure that internal links to these pages are removed. This removal often happens automatically for many of the links to the page (but probably not all of them), so check for any remaining ones by crawling your site.

To find these links, check the **Links** report in Ahrefs’ [Site Audit](https://ahrefs.com/site-audit). Look for “Broken” on internal links. You can click into this chart to get a list of the broken links and the pages that link to them.

Broken internal links.

### Option 3. Leave the page live

The product is gone, and most people will want to get rid of the page either by deleting it or redirecting it. But there are plenty of valid reasons to leave a page live.

It could have useful resources, such as documentation, that may take some burden off a support team. Perhaps, the page is still getting a decent amount of search traffic that you want to funnel into other products you offer. You can use Ahrefs’ [Site Explorer](https://ahrefs.com/site-explorer) to check the organic search traffic for the page.

If you’re leaving the page live for now, I don’t recommend removing internal links like you would in the other options. Removing the links can hurt your rankings.

This is also when potential SEO benefits clash with user experience. Landing on a page—where there’s nothing to buy—either from the internal search or from a category page won’t be a great experience for a user.

You may want to add a filter so users can remove out-of-stock products. Or you may want to show these products last in any listings. Deprioritizing the pages like this means they may also not rank as well, but I generally recommend it.

Eventually, you may consider these pages to no longer be useful and, accordingly, may want to redirect or delete them.

## Temporarily out of stock, coming back soon

You want to leave these pages live. If so, there are some useful actions you can take or automate in your system.

There are features that may be useful to you and your customers, such as estimates of when a product will be back in stock, a wait list, or a way to sign up to be notified when a product has been restocked. Some stores are even offering their customers lotteries to purchase items when they’re back in stock, e.g., the Newegg shuffle program.

## Temporarily out of stock, may not be coming back

Sometimes, you have a product that you just don’t know when or if you’ll be carrying again. In all of these cases, I’d make the product less visible on the website so users are less likely to see them. Let’s look at the options.

### Option 1. Leave it live

As I mentioned before, there are several reasons you may want to leave a page live, including capturing search traffic to funnel people to other products or using the page for support or documentation purposes.

Don’t delete the internal links in this situation. Eventually, you may want to redirect or delete these pages when you realize the relevant products are not going to come back or the pages are no longer useful.

### Option 2. Noindex

I’ll say that using noindex is not my favorite option, and I don’t typically recommend it. It’s usually not the best idea to do this because it can cut off the flow of [PageRank](https://ahrefs.com/blog/google-pagerank/).

I only mention it because, in some systems, noindex is used as the trigger to stop the product from being shown to users. On the bright side, products marked noindex will come back in search results pretty quickly after Google recrawls the page.

### Option 3. Leave it live for a while and delete or redirect it later

At some point, you may just want to make a decision to treat this product as if it’s not coming back and delete or redirect it. When you do this is up to you, but a lot of people use logic based on the demand or when a certain amount of time has passed. In the short term, I’d keep the internal links live—but you’ll want to clean them up later.

## How to find out-of-stock products

You should have a list of out-of-stock products from some data source that handles your product inventory or possibly within the content management system’s backend. In case you don’t have that list, you may want to crawl the website with Ahrefs’ [Site Audit](https://ahrefs.com/site-audit) and search the HTML code to find pages that have your out-of-stock message.

Search for out-of-stock products.

## Final thoughts

As you’ve seen, you have a lot of options when it comes to out-of-stock products. What I generally recommend is you set some rules that you’re comfortable with and just go with them. The logic you use is really up to you. Ultimately, there’s no perfect solution.

Message me [on Twitter](https://twitter.com/patrickstox) if you have any questions.
