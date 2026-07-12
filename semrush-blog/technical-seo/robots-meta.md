---
title: "Meta Robots Tag & X-Robots-Tag Explained"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "robots-meta"
url: "https://www.semrush.com/blog/robots-meta/"
canonical: "https://www.semrush.com/blog/robots-meta/"
author: "Yannick Weiler, Chris Hanna, Boris Mustapic"
published: "2020-12-16T14:16:00+00:00"
updated: "2024-08-14T09:56:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2024_watch"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T18:57:25+00:00"
status_code: 200
html_hash: "4a241f7ce368bbea701d63f7163b1dc5c501c69599177bce5afb6324cdae7411"
clean_word_count: 2142
clean_char_count: 17660
---
# Meta Robots Tag & X-Robots-Tag Explained

## What Is a Meta Robots Tag?

A meta robots tag is an HTML element that tells search engine robots how to crawl, index, and display a page’s content. The meta robots tag goes in the <head> section of the page and can look like:

<meta name="robots" content="noindex">

This example tells search engine crawlers not to index the page. Robots meta tags can control many other crawler behaviors. They’re important for SEO because they let you specify which content should appear in search results.

![AD_4nXfaNdDzKXiJX9j1IJvL1ygbEPUpOGRW2FDElrkBn2kk03m9n0NtoHMeegFt01835QVegR0FiOiM6gaeTLnvo4sYZw36hen9U8nCpndZ3-_IE71iRjcMFexqNb6uq5cBlu2ItcClSA?key=h46gGSEY9dRpbZe5N8G3bbbR](https://static.semrush.com/blog/uploads/media/ef/2b/ef2bcbf7c62254d612c060b1c82f5730/9463ae1c2e50c4b0ca36b09138a11023/AD_4nXfaNdDzKXiJX9j1IJvL1ygbEPUpOGRW2FDElrkBn2kk03m9n0NtoHMeegFt01835QVegR0FiOiM6gaeTLnvo4sYZw36hen9U8nCpndZ3-_IE71iRjcMFexqNb6uq5cBlu2ItcClSA.png)

## Meta Robots vs. Robots.txt

Meta robots tags and robots.txt files both influence how search engines crawl pages. However, each works differently:

- A [robots.txt](https://www.semrush.com/blog/beginners-guide-robots-txt/) file is a single text file that applies to the entire site. It instructs search engines which pages to crawl.
- A **meta robots tag** applies only to the page it appears on. It tells search engines how to index (or not index) that specific page’s content.

## What Are Robots Meta Tags Used For?

Robots meta tags help you control how Google and other search engines handle a page’s content. You can specify whether to:

- Include a page in the search results
- [Follow the links](https://www.semrush.com/blog/nofollow-links/) on the page
- Index images on the page
- Show cached results in search results pages (SERPs)
- Show a snippet of the page in SERPs

Next, this article explains which attributes you can use to instruct search engines. But first, learn why robots meta tags are important and how they affect SEO.

**How Do Robots Meta Tags Affect SEO?**

Robots meta tags let search engines crawl and index your pages efficiently. This is especially useful for large or frequently updated sites. You may not want every page to rank in search results, such as:

- Staging or development pages
- Confirmation pages, like thank-you pages
- Admin or login pages
- Internal search result pages
- Pages with [duplicate content](https://www.semrush.com/blog/duplicate-content/)

Combining robots meta tags with other directives (like sitemaps and robots.txt) is helpful for [technical SEO](https://www.semrush.com/blog/technical-seo/). It can prevent crawl and index issues that harm performance.

**What Are the Name and Content Specifications for Meta Robots Tags?**

Meta robots tags contain two attributes: **name** and **content**. Both are required.

### Name Attribute

The “name” attribute indicates which [crawler](https://www.semrush.com/blog/website-crawler/) the instructions apply to. For example:

name="crawler"

To address all crawlers, set name="robots". This attribute is not case-sensitive, so “robots,” “ROBOTS,” and “Robots” all work.

To target specific search engines, use their crawler names (e.g., Googlebot, Bingbot). Note that not all bots respect meta robots tags, so avoid using them for security.

### Content Attribute

The “content” attribute contains instructions for the crawler, such as:

content="instruction"

This attribute is also not case-sensitive. Google supports several “content” values:

#### Default Content Values

If there is no meta robots tag, crawlers index content and follow links by default. This is the same as adding content="all".

#### Noindex

<meta name="robots" content="noindex">

Tells crawlers not to index or display the page in search results. Commonly used for cart or checkout pages.

#### Nofollow

<meta name="robots" content="nofollow">

Tells crawlers not to follow any links on the page. The nofollow attribute is useful if you don’t control the links on a page, such as in user-generated content.

#### Noarchive

<meta name="robots" content="noarchive">

Prevents Google from showing a cached copy of your page in search results. Useful for time-sensitive or internal documents.

#### Noimageindex

<meta name="robots" content="noimageindex">

Stops Google from indexing images on the page. Users can still see images on the page itself, so use caution if you want image-based traffic.

#### Notranslate

<meta name="robots" content="notranslate">

Prevents Google from offering translations of the page. Useful if you don’t want product names or important terms auto-translated.

#### Nositelinkssearchbox

<meta name="robots" content="nositelinkssearchbox">

Prevents Google from generating a search box for your site in search results.

#### Nosnippet

<meta name="robots" content="nosnippet">

Prevents Google from showing text or video snippets. Also prevents content from appearing as a direct input for AI Overviews. But it also removes meta descriptions and rich snippets.

You can alternatively prevent only certain sections from showing by using the data-nosnippet attribute:

<p>This text could be shown

<span data-nosnippet>but this part would not be shown</span>.</p>

#### Max-snippet

<meta name="robots" content="max-snippet:100">

Specifies the maximum character length for text snippets.

- 0 means no snippets.
- -1 means no limit.

#### Max-image-preview

<meta name="robots" content="max-image-preview:large">

Controls the maximum size of preview images. Values can be “none,” “standard,” or “large.”

#### Max-video-preview

<meta name="robots" content="max-video-preview:10">

Controls the maximum length of a video snippet in seconds.

- 0 means no video snippets.
- -1 means no limit.

#### Indexifembedded

<meta name="robots" content="noindex, indexifembedded">

Lets Google index a page’s content if it’s embedded in another page through iframes. This helps media publishers who don’t want direct indexing of media pages, but do want indexing when the media is embedded elsewhere. Not all search engines support this.

#### Unavailable\_after

<meta name="robots" content="unavailable\_after: 2024-10-21">

Tells Google to stop showing the page in SERPs after the specified date or time. Use RFC 822, RFC 850, or ISO 8601 formats. This functions like a timed noindex.

## Combining Robots Meta Tag Rules

You can combine rules in two ways:

**Multiple Values in One “content” Attribute**
<meta name="robots" content="noindex, nofollow">

1. This example tells crawlers not to index the page or follow links. You can also use content="none" to combine noindex and nofollow together, but some search engines (like Bing) do not support this keyword.
    If conflicting directives appear, Google applies the most restrictive one.

**Multiple Robots Meta Elements**
<meta name="robots" content="nofollow">

<meta name="YandexBot" content="noindex">

2. This example tells all crawlers to avoid following links, but also instructs Yandex to not index the page at all.

### Search Engine Support for Meta Robots Tags

|  |  |  |  |
| --- | --- | --- | --- |
| **Value** | **Google** | **Bing** | **Yandex** |
| noindex | Y | Y | Y |
| noimageindex | Y | N | N |
| nofollow | Y | N | Y |
| noarchive | Y | Y | Y |
| nocache | N | Y | N |
| nosnippet | Y | Y | N |
| nositelinkssearchbox | Y | N | N |
| notranslate | Y | N | N |
| max-snippet | Y | Y | N |
| max-video-preview | Y | Y | N |
| max-image-preview | Y | Y | N |
| indexifembedded | Y | N | N |
| unavailable\_after | Y | N | N |

**How to Implement Robots Meta Tags**

### Adding Robots Meta Tags to Your HTML Code

Place meta robots tags in the <head> section of the page:

<meta name="robots" content="noindex, nofollow">

### Implementing Robots Meta Tags in WordPress

If you use Yoast SEO:

1. In the page editor, open the “Advanced” tab.

![AD_4nXcrFp6Et6wOysG4ckKZfn0xLNHbb-Hmfh2tTLyQ4oPr08GQGKFX7JxcUJPTQVrxIRIqWJK-VQclkCOp5okd2i3qOjJmhv8UGr2Tqc4Oa6Rv0DLvynnwRKvwdbcpHQvdk1hSbsPd?key=h46gGSEY9dRpbZe5N8G3bbbR](https://static.semrush.com/blog/uploads/media/aa/ab/aaab4da5a313f7308b4bb2919bc4fabb/2a69f10f5f5024fa85e75da0c5161ded/AD_4nXcrFp6Et6wOysG4ckKZfn0xLNHbb-Hmfh2tTLyQ4oPr08GQGKFX7JxcUJPTQVrxIRIqWJK-VQclkCOp5okd2i3qOjJmhv8UGr2Tqc4Oa6Rv0DLvynnwRKvwdbcpHQvdk1hSbsPd.png)

2. Set “Allow search engines to show this page in search results?” to “No” for noindex.

![AD_4nXcg2UHB1-J4-MCbENel8Jd-sYXTPcvkvBiMGPcScRj8SV5vE2xGktCxNl9KKh_-DefhP6Okb8MvFC64yasUUMic78SnxYdN7MoTl0RINtJUM-p0ziUGu-55qMxY5Y1bGbI5H4F9Hw?key=h46gGSEY9dRpbZe5N8G3bbbR](https://static.semrush.com/blog/uploads/media/b6/c6/b6c60806349ac23180c99a6acab9b497/c7f24091924d2ef10b4ee78218de4a4a/AD_4nXcg2UHB1-J4-MCbENel8Jd-sYXTPcvkvBiMGPcScRj8SV5vE2xGktCxNl9KKh_-DefhP6Okb8MvFC64yasUUMic78SnxYdN7MoTl0RINtJUM-p0ziUGu-55qMxY5Y1bGbI5H4F9Hw.png)

3. Set “Should search engines follow links on this page?” to “No” for nofollow.

![AD_4nXd5trmmpNXsmfLPb7ed56DOec9sCTJoGdGokOSItWkCy9R7-0Vu1xgbAmpo41FwYbFDuo-NkssWM2ZzfSVmVkCyVMisvNBfaMTBLouUkt36GTrMoLZ7A44xMpMhscB-avsn9Fkt8A?key=h46gGSEY9dRpbZe5N8G3bbbR](https://static.semrush.com/blog/uploads/media/79/48/794822c5c8a03b23e2fc77bc6b2fd242/454dc54f0bc77d0a5dfb16949e940c63/AD_4nXd5trmmpNXsmfLPb7ed56DOec9sCTJoGdGokOSItWkCy9R7-0Vu1xgbAmpo41FwYbFDuo-NkssWM2ZzfSVmVkCyVMisvNBfaMTBLouUkt36GTrMoLZ7A44xMpMhscB-avsn9Fkt8A.png)

4. For other directives, use the “Meta robots advanced” field.

![AD_4nXeOSZbK7nMCAWa6QVOXe3MWpW7DtLYEFbH7Ar-ASVAbnJp2ULnFOtJrry86ccanv7Mz_JUsMdlzgV3WiYjAsjDVgVlShOVcl25_lrnEIBdRLkLDSEhzTdcvK2Dt8Lhkwj3Fw8qZ_g?key=h46gGSEY9dRpbZe5N8G3bbbR](https://static.semrush.com/blog/uploads/media/c8/01/c801c48cdafbae3d14f721fcc8c4c9b4/b02c3cd412ee6a9a13eb64c29742e499/AD_4nXeOSZbK7nMCAWa6QVOXe3MWpW7DtLYEFbH7Ar-ASVAbnJp2ULnFOtJrry86ccanv7Mz_JUsMdlzgV3WiYjAsjDVgVlShOVcl25_lrnEIBdRLkLDSEhzTdcvK2Dt8Lhkwj3Fw8qZ_g.png)

If you use Rank Math:

1. Go to the “Advanced” tab in the meta box.
2. Choose the directives from the provided checkboxes or fields.

![AD_4nXcD6SevtamrW5nWqTGSQGvuGMU3jxFlD1gVNpMNpqimH8SeThaXr7AHY8FHvX-go3SnyrnNCXDdfM9m7G4RC8S_8_Rl6dyDfCw6ePUcVCLFAVMyLQTUrDP75vZligUQNOT14o6C?key=h46gGSEY9dRpbZe5N8G3bbbR](https://static.semrush.com/blog/uploads/media/d5/77/d5774fc91f4d02c260ef417d5ea9cb31/d5acd8230d735fd7db8862701ab34948/AD_4nXcD6SevtamrW5nWqTGSQGvuGMU3jxFlD1gVNpMNpqimH8SeThaXr7AHY8FHvX-go3SnyrnNCXDdfM9m7G4RC8S_8_Rl6dyDfCw6ePUcVCLFAVMyLQTUrDP75vZligUQNOT14o6C.png)

### Adding Robots Meta Tags in Shopify

Edit the <head> section of your theme.liquid layout file.

![where to find <head> section of the theme.liquid layout file for robots meta tags in Shopify](https://static.semrush.com/blog/uploads/media/5f/fa/5ffa1ae209fb2eff4c6e3ec106bcdcd8/fa8bd5a8b2c11df19deafa2cd08ec31d/AD_4nXc7trcL2Cm2EnuxEGp6YeMRhMYhaex3ZnWi1HsXJvqc9rfmzJrvry2_KxO-Iq9HMF6OAU04wa4kbbaS4HjqLlV81Ul5FIxMk6pxEErxowlAw43YO-a9I8bauGRJarL41SdF2N7K.png)

For a specific page:

{% if handle contains 'page-name' %}

  <meta name="robots" content="noindex">

{% endif %}

Use separate entries for different pages. Edit theme files carefully or consult a developer.

### Implementing Robots Meta Tags in Wix

1. Open your Wix dashboard and click “Edit Site.”

![AD_4nXeedq3PNRb_nY0zZwHYi_z5AWxNjVeGLy6ESiRrdDXk26qRuIdf7ieManuL7qsbbjC99fVVUidDuVrR9F9-j6bDC9aCPiDB8k4frTjeIXd3nTJhV8cyvz8obZwPmIC2quFQS18G?key=h46gGSEY9dRpbZe5N8G3bbbR](https://static.semrush.com/blog/uploads/media/76/ad/76ade7181d84a24735a4517ddd8515b2/1a86d275b10cc2c71456fd655e3b29a5/AD_4nXeedq3PNRb_nY0zZwHYi_z5AWxNjVeGLy6ESiRrdDXk26qRuIdf7ieManuL7qsbbjC99fVVUidDuVrR9F9-j6bDC9aCPiDB8k4frTjeIXd3nTJhV8cyvz8obZwPmIC2quFQS18G.png)

2. Click “Pages & Menu.”
3. Next to the desired page, click “...” → “SEO basics.”

![AD_4nXcOwTtteCtCbeK9xSkxNikbrPsq1Hn7D-dU-m77wQU7fSFatZaUw6AYvgqhv9PEsDi1kFOx8zQUGjPQdtJVy4SD0NHzjSuBCnYuUcNAYlR3jli_m_JxWDcsGMd1AguD2GwWA-t55Q?key=h46gGSEY9dRpbZe5N8G3bbbR](https://static.semrush.com/blog/uploads/media/66/31/66315c008c71ac2c40d449f75d6b4162/4270c3bfbb7e784541ae31ae5dbcf7c9/AD_4nXcOwTtteCtCbeK9xSkxNikbrPsq1Hn7D-dU-m77wQU7fSFatZaUw6AYvgqhv9PEsDi1kFOx8zQUGjPQdtJVy4SD0NHzjSuBCnYuUcNAYlR3jli_m_JxWDcsGMd1AguD2GwWA-t55Q.png)

4. Under “Advanced SEO,” open “Robots meta tag.”

![AD_4nXd6SNPrMOji_aesbH6Nq1ugMzAthz5FUNafCp2zW0yeurO_8eXGK9AZkqWYVaWngukPBm-rZh3CCxrTFXfW8tPWQGx22wIPlZ2XR7Qua8-NfoP2cZrWILpX1dlvS1K1vUpcI65b0w?key=h46gGSEY9dRpbZe5N8G3bbbR](https://static.semrush.com/blog/uploads/media/e6/6e/e66e85a3b08eab92a310d3ba818b32ae/8f3e20e2afee5a2838cc0ca5dc8c68a3/AD_4nXd6SNPrMOji_aesbH6Nq1ugMzAthz5FUNafCp2zW0yeurO_8eXGK9AZkqWYVaWngukPBm-rZh3CCxrTFXfW8tPWQGx22wIPlZ2XR7Qua8-NfoP2cZrWILpX1dlvS1K1vUpcI65b0w.png)

5. Select the relevant robots meta tags via checkboxes. For directives like notranslate or nositelinkssearchbox, click “Additional tags” → “Add New Tags.”

Now, you can paste your meta tag in HTML format.

!["add new tag" option highlighted with "new meta tag" popup](https://static.semrush.com/blog/uploads/media/a0/75/a075923e28da2863dfbafca727b3bd66/8066d71f10d3078f6044fc89030d2f49/AD_4nXcbP5KqNGrgbjA05QxsMvt4nRsvm__3cw28E-zNA3GDA2syMnM5SS4-Kp4EpbGf6zZNnQI9wHA1x3-9Q3F02VOHzpL7qPT5a-6EfTOrwbhCYXZyZOYlM2Mu2XVL0CWp2KzpN8XImw.png)

## What Is the X-Robots-Tag?

An x-robots-tag instructs crawlers how to index non-HTML resources (such as PDFs or images). It goes in the HTTP header response:

makefile

X-Robots-Tag: noindex, nofollow

You can use the same rules as meta robots tags. However, you must edit server configuration files like .htaccess on Apache or .conf on Nginx.

## How to Implement X-Robots-Tags

### Using X-Robots-Tag on an Apache Server

In your site’s .htaccess or httpd.conf, add:

arduino

<Files ~ "\.pdf$">

  Header set X-Robots-Tag "noindex, nofollow"

</Files>

This instructs crawlers not to index or follow links on any PDF across the entire site.

### Using X-Robots-Tag on an Nginx Server

In your site’s .conf file, add:

ruby

location ~\* \.pdf$ {

  add\_header X-Robots-Tag "noindex, nofollow";

}

This applies noindex, nofollow to all PDFs on the site.

## Common Meta Robots Tag Mistakes to Avoid

- **Using Meta Robots on a Page Blocked by Robots.txt:** If a page is disallowed in robots.txt, search engine bots will never see the meta robots tag on that page.
- **Adding Robots Directives to Robots.txt:** Google no longer supports noindex rules in robots.txt. Use meta robots tags or x-robots-tags instead.
- **Removing Pages with Noindex from Sitemaps Too Early:** Keep the page in your sitemap until it’s deindexed. Otherwise, deindexing may be delayed.
- **Forgetting to Remove Staging ‘Noindex’:** When you move a site from staging to production, remove any noindex directives to avoid blocking the entire live site from indexing.

### How to Check Your Website for Meta Robots Tag Issues

One of the best ways to check your website for meta robots tag issues is to use Semrush’s **Site Audit** tool:

1. Enter your domain and click “Start Audit.”

![AD_4nXc2QKFT9GELunTsoQwi3fVTaH1liLW2_khy9icIcgql0Mgi_GFRQ78YbI8yWTa-rq7ugCUjTn1LcD-jadqMkzcXX8iSTWkJSIfvimvovGr01xsxuHiNlBAMPxwOibSuLegE34mkvw?key=h46gGSEY9dRpbZe5N8G3bbbR](https://static.semrush.com/blog/uploads/media/9b/93/9b93470528ac7bba03fb1d636d4b5044/0bc075309f1a08e97df52c257b2f71db/AD_4nXc2QKFT9GELunTsoQwi3fVTaH1liLW2_khy9icIcgql0Mgi_GFRQ78YbI8yWTa-rq7ugCUjTn1LcD-jadqMkzcXX8iSTWkJSIfvimvovGr01xsxuHiNlBAMPxwOibSuLegE34mkvw.png)

2. Adjust settings if needed, then run the audit.

![AD_4nXdRtePZbfysOxQXLW3dMRB5tmLSb5WfHu6BR6ILGruwtGI7FtDYv5bkQ2ttk6GW9a9GY-yOyY-_xTneY83FgMp8GywyLHdpIwdazAnysSEQJgZtG3xlhHZj6fewBt0kKFsm_JNjyw?key=h46gGSEY9dRpbZe5N8G3bbbR](https://static.semrush.com/blog/uploads/media/3d/56/3d56215a09879b06e31f380df7456872/455816db614e619b1ed47250197d6a12/AD_4nXdRtePZbfysOxQXLW3dMRB5tmLSb5WfHu6BR6ILGruwtGI7FtDYv5bkQ2ttk6GW9a9GY-yOyY-_xTneY83FgMp8GywyLHdpIwdazAnysSEQJgZtG3xlhHZj6fewBt0kKFsm_JNjyw.png)

3. In the “Issues” tab, search for “blocked from crawling” or other errors related to meta robots tags.

![AD_4nXfx4gakXBJbqz9URoHiVdqnz2falrhhZBLfXiMP8wvcBRuGvsHIavoq51Rm4HC2kOE5wj7m1ZUVJwfUbBktLamZMFOs5oS-b_Pv3sx0Q2zYIBduERn_4MZN9MMDVfW_iNufW3eJzA?key=h46gGSEY9dRpbZe5N8G3bbbR](https://static.semrush.com/blog/uploads/media/3d/69/3d690dd21f48e304b0972dcff7b15765/3abe09591003e60c278e3d61160a2245/AD_4nXfx4gakXBJbqz9URoHiVdqnz2falrhhZBLfXiMP8wvcBRuGvsHIavoq51Rm4HC2kOE5wj7m1ZUVJwfUbBktLamZMFOs5oS-b_Pv3sx0Q2zYIBduERn_4MZN9MMDVfW_iNufW3eJzA.png)

4. Review “Why and how to fix it” for each issue.
5. Correct these issues to improve crawlability.

## FAQs

### When Should You Use the Robots Meta Tag vs. X-Robots-Tag?

Use the **robots meta tag** for HTML pages and the **x-robots-tag** for non-HTML resources. You can technically use x-robots-tag for HTML pages, but meta tags are simpler. X-robots-tags also allow bulk rules for file types like PDF.

### Do You Need to Use Both Meta Robots Tag and X-Robots-Tag?

No. One is enough. Using both does not increase the likelihood that crawlers will follow your directives.

### What Is the Easiest Way to Implement Robots Meta Tags?

A plugin is typically the easiest method. It avoids manual code edits. The best plugin depends on your content management system (CMS).

## Use Meta Robots Tags Correctly to Avoid Indexing Issues

Robots meta tags ensure that important content is indexed. Without proper indexing, your pages will not drive any [organic traffic](https://www.semrush.com/blog/organic-traffic/). Directives like noindex and nofollow are crucial for controlling your site’s search presence. Check that you have implemented them properly with Semrush Site Audit.
