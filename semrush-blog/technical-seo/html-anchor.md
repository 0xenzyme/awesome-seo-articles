---
title: "HTML Anchor Element: What Are Anchor Links & How to Use Them"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "html-anchor"
url: "https://www.semrush.com/blog/html-anchor/"
canonical: "https://www.semrush.com/blog/html-anchor/"
author: "Carlos Silva"
published: "2021-10-18T20:43:00+00:00"
updated: "2023-03-30T10:00:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2023_aging"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T16:55:23+00:00"
status_code: 200
html_hash: "262f4a52692d15870a414a347ff4c5f2916ccf0f1f526ba7d613748e9e31e48e"
clean_word_count: 2151
clean_char_count: 14911
---
# HTML Anchor Element: What Are Anchor Links & How to Use Them

## What Are Anchor Tags in HTML?

Anchor tags in HTML code are HTML elements used to create hyperlinks in webpages. They allow you to link to another webpage, a specific section of a page, an email address, a file, or any other URL. They are also known as anchor elements or <a> tags.

A complete anchor element or <a> tag looks like this:

![anchor tag in HTML](https://static.semrush.com/blog/uploads/media/59/fc/59fc528eecc00e43b1a3ed5d9b9933ee/4YA3vCJ_Hw6DucoVZ40FbKFRppAReJVOkLKHcZlDkO-9geydLO6tw9uzFJFZf5nam3QcT7p0hRdpFyL2uPhoDISD8CPZwfPE5GTqgpH53q9M99QWgDVhjgQrCMOlQI9fA1T2dCxJ5T2goCV3k1wo-Jc.png)

The element starts with “**<a**,” ends with “**</a>**.” And contains various attributes that make up the full tag.

We’ll get into the attributes below.

You can also use the [anchor tag](https://www.semrush.com/blog/html-a-tag/) to create anchor links. Anchor links (or “jump” links) link to different sections of the same webpage.

When you create text links with the “a” tag, you’ll need to use some kind of [anchor text](https://www.semrush.com/blog/anchor-text/). Anchor text is the part of the link that’s clickable. Google uses this text to learn more about the link and the content it points to.

Your site probably has a lot of anchor tag links already. Use a tool like [Site Audit](https://www.semrush.com/siteaudit/) to identify them and fix any issues that they might have.

[Configure the tool](https://www.semrush.com/kb/539-configuring-site-audit) and run your first crawl.

After that, go to the “Issues” tab and select “**Links**” from the “**Category**” drop-down.

![“Issues” tab in the Site Audit tool](https://static.semrush.com/blog/uploads/media/61/85/6185769814b2449778b5fceb52fece8c/sO9jSnuFCs59tVs3Zqw81b-UaMQ83j7NKJW_eZ9DePbrbcvKW44slAWEmj3Hfgc6ax53cPIIMHgtRzavILEABKw6XeVEcn9LY1U_ULln8TPh424sZYlU1houCL62AwmSeHTfmoNb9Vbl66Xd3AD4XvY.png)

You’ll see if there are any issues detected.

![find detected issues in the “Issues” tab of the Site Audit tool](https://static.semrush.com/blog/uploads/media/95/28/9528ac8c569ca1ab2a2a0cc370256a48/FqEe0aOnwLTBkEJz83IA_E0W1GS-annLlYr0meWq3XNu3BhBn1ckU3oC-hbw7CCa90H1KCPchv81G-UpsKFndy_MA4WRrMDyaQlCGmr5j4J39y6_QpWOVlsDCOEj2YSS-_GWihe-SrpTPvJpxFnhkTo.png)

The tool also offers advice on how to fix each issue. Just click on the “**Why and how to fix it**” link.

![an example of “Why and how to fix it” section in the Site Audit tool](https://static.semrush.com/blog/uploads/media/ca/23/ca238dfee88d48bc8d4f7c0ede4c7b39/qM2_63aBCHUmGef_1bsBzZFEeKwmvWaovTKkoxRmUKuGzDbGfxz5N00uMmPMGMULQlxAHrBPCEjd8cYJ1uYWxMG4e8GPffLLnN0qqe6Xn3prXUY9Zqs1IRQ4SF1Ack2LVV1q_mGvxq32f1me0snn0aM.png)

## HTML Anchor Element Attributes

You can add different attributes to your anchor tags to specify what you want to happen when a user clicks.

And to add semantic meaning for browsers and [web crawlers](https://www.semrush.com/blog/website-crawler/).

Here are the most important attributes:

### Href

[The “href,”](https://www.semrush.com/blog/ahref-link/) short for hypertext reference, attribute specifies the target for the anchor element.

Like this:

`<a href="URL">`

It’s commonly used to define the URL of the page the tag links to. But you can also use it to link to files, email addresses, phone numbers, and more.

For example, a link to a webpage would use the following snippet of code:

`<a href="https://example.com">Website</a>`

The href anchor tag is the URL between quotation marks. And the word “Website” is the anchor text: the visible and clickable text of the link.

### Hreflang

The “hreflang” attribute indicates the language of the linked resource using the [ISO 639-1 two-letter language code](https://hreflang.org/list-of-hreflang-codes/).

It looks like this:

`<a hreflang="language_code">`

If you want to specify English as the page’s language, use the following snippet of code:

`<a href="https://example.com" hreflang="en">Website</a>`

The [hreflang](https://www.semrush.com/blog/hreflang-attribute-101/) attribute is the two-letter country code: “en” wrapped in quotation marks.

**Note:** You can only use the hreflang attribute if you’ve also used the [href attribute](https://www.semrush.com/blog/ahref-link/).

### Download

The “download” attribute tells the browser to download the linked resource instead of opening it.

Like this:

`<a download="filename">`

For example, if the resource is a PDF, use the following code:

`<a href="example.pdf" download="Example">`

The attribute is the name of the file. In this case, “Example.”

If you don’t specify a filename, it will pull the document’s original filename.

### Rel

The “rel” attribute specifies the relationship between the current and linked resource.

Like this:

`<a rel="value">`

The most common “rel” attribute values include the following:

- rel=“alternate”: To identify the linked resource as an alternate version of the current resource

- rel=“author”: To provide a link to the author of the resource

- rel=“bookmark”: To indicate the URL is permanent and can be used for bookmarking. Often used to quickly navigate to a specific section of a long article, for example.

- rel=“help”: To state the link contains a help document for the current page

- rel=“next”: To specify the link is the next page in the series. For articles, news, or photo galleries, for example.

- rel=“prev”: To specify the link is the previous page in the series

- rel=“[nofollow](https://www.semrush.com/blog/nofollow-links/)”: To indicate to search engines not to follow the link. In other words, you don’t wish to endorse the link

- rel=“search”: To specify the linked page can be used to search for content on the page or site

And others.

For example, you can use the following code to indicate the link is a page about the author of the article:

`Article written by <a href="https://example.com/+AuthorName"
rel="author">Author Name</a>.`

**Note:** Search engines like Google use the “rel” attribute to get more information about a link.

### Target

The “target” attribute tells the browser where to open the link, such as in the same tab, a new tab, a new window, or an iframe.

It looks like this:

`<a target="value">`

The different values include:

- “\_self”: To open the link in the same frame (often the same tab or window)

- “\_blank”: To open the link in a new tab or window. This is the most common approach

- “\_parent”: To open the link within the next-level-up frame, known as a parent frame

- “\_ top”: Ignores all frames and opens the link as the top document in the same browser window

- “framename”: To open the link in the named frame, such as a video playing within an iframe.

![The a target attribute](https://static.semrush.com/blog/uploads/media/b9/eb/b9ebbeb193a23d04c303b25f410b43b7/Penya2ZKdhsHrol3gX0XIxR_OfwDZv9-24JRVDeG8YyjjOMv9fFGY_Nl6X1AAbZS4VcLrEZ-8nKbnTrMER6O42k6W0y_FRKkZrEXwXh_flbAjJ4XU7B9WVTvAxy3tKO11854s0MeHoElXHBIhlVFuMQ.png)

For example, if we want the link to open in a new tab, we can write:

`<a href="https://example.com" target="_blank">Website</a>`

## Anchor Tag Examples

Let’s consider a few examples of where and how to use anchor tags.

### Link to an Element on the Same Page

You can use anchor tags to link to elements on the same page. And help users better navigate and consume your content.

Start with the following:

1. Attach an “id”attribute to the section you want to link to
2. Add the “id” attribute to the anchor tag you’re linking from

For example, say we’re writing an article about SEO and want to link to the heading “Local SEO.”

Go to the heading and attach an “id”attribute to it.

Like this:

`<a id="LocalSEO"><h2>Local SEO</h2></a>`

Go to the text you want to add a link from and add an “href”attribute to create the anchor link.

However, instead of adding a link to a webpage, add the anchor ID with a pound sign (#).

Like this:

`<a href="#LocalSEO">local SEO</a>`

When the reader clicks on the link, they’ll “jump” to the H2 header with the "LocalSEO" id.

### Link to an Email Address

You can also have a link that directs users to send an email to a specific address.

When a user clicks a link, the browser will open the computer’s default email client, such as the Apple Mail app on a Macbook laptop. And auto-populate the recipient address with the one specified in the attribute.

This is called the “mailto”protocol. It’s added to the “href” attribute’s value.

Like so:

`<a href="mailto:person@example.com">Send email to person</a>`

If someone clicks the link above, the default email client will open with the email address indicated in the “To” field.

![Writing email box](https://static.semrush.com/blog/uploads/media/71/a4/71a4b9169d8fbc61cd3cfb95c52da3c9/XNZQJFBQYmO5_3CSeLJ6NPH_rkzMRNn648lj9iRUM_LqBNlw-uWKs3RAKfUN60sq3UKtWay6HJesrMBqs4aDkvpRj1GbCj03NzbBjjRVzm2KQqv7L5x4n06LcYthU9GbceCgazL9gQVhebSr6B1LUEo.png)

### Link to a Phone Number

Just as you can link to an email address, you can also link to a phone number.

Add the “tel” protocol followed by the phone number.

Like this:

`<a href="tel:+34673245198">+34673245198</a>`

Clicking the link will call the number on capable devices (such as phones or on computers with Skype or FaceTime).

### Link to a File Download

Use the “download” attribute to make the link download a file directly.

For example, you might use it to help readers download an infographic or PDF.

To implement it, set the “href” attribute. Its value is the actual file.

Like this:

`<a href="/images/infographic.jpg" download="infographic">`

Clicking the link will download the infographic.

**Note:** You can add the name of the file as the value of the “download” attribute. But it’s optional. If you don’t, the browser will use the original filename.

## Are Anchor Links Good for User Experience?

Anchor links can help improve user experience (UX). Readers use them to navigate, and they can provide a better browsing experience.

Anchor links are commonly used in a table of contents, for example, to help navigate long or visually dense pages.

When readers land on a page, they want to know whether the information is useful or relevant to their search query.

A table of contents that includes clear, clickable anchor links summarizes your page and helps readers “jump” to the section they’re most interested in.

## Are Anchor Links Good for SEO?

Anchor links help improve [page experience](https://www.semrush.com/blog/google-page-experience-signal/). And can earn [featured snippets](https://www.semrush.com/blog/featured-snippets/). Both of which can help improve your rankings over time.

Google can also include anchor links in your page’s search snippet.

Like this:

![Page’s search snippet example](https://static.semrush.com/blog/uploads/media/da/fc/dafc8aac9edcc319954fb7c2880f290c/3BK8VVIRDlOs3XDe4mxBhnEi6xzS4uEGfJPlPb4Vr6JUUB0ix8dpmwoyXBjhAt1hlLfQ117gahMyRdLHd9o_qYMxtu6Fz9Uj2G4V1gzLsq_3D9XilkuYHbw0vjXG2MA7vVdd7XxMWn9CfDAdQvf0JhE.png)

Google includes an anchor link to “Plot” and “Cast” on a page about John Wick, the movie. Which helps searchers “jump” directly to that section from the search engine results page (SERP).

Which means:

It can be worth including anchor links on your page.

Use them to tell Google more about your content. And help readers find and jump to the sections they want to read.

## Audit Your Site’s Links to Improve Your SEO Ranking

One of the most important SEO best practices is regularly auditing your site. Audits can help you find and fix issues holding your site back from ranking.

You can also audit to find specific issues. Like issues with links, in this case.

Semrush’s [Site Audit tool](https://www.semrush.com/siteaudit/) crawls your entire website and helps you resolve these issues.

Open the tool, enter your domain name, and click “**Start** **Audit**."

![Semrush’s Site Audit tool](https://static.semrush.com/blog/uploads/media/8d/6d/8d6d296dd8379b1083bc66f47994a87c/IgJUUnFg5i3awD7B5gkPsV25uGBj5rf411W041-LzS6iP7cWbRtTh2yOUTLx-vbGbI0yrSsK4BoiL1FZnXHbR9UdXfhR2K4gf7jk2VFHYo5PfMyxbEgr83C9hKcq2iOf6prHHTp1miz-oaWKhTDRjmI.png)

The “Site Audit Settings” pop-up will appear.

![Site Audit Settings](https://static.semrush.com/blog/uploads/media/ab/70/ab70e6f97846b8bdb077fb0d051af66d/bQaGzJuIaGThiOkxE01yqtFyieqyIFZR02R63aenr9dPtrkK0jfw3UumnxQ2aZ8KAvYyd4v1cdkVYCvK96NW_k5JF543JTd-lPs7nnqboeVwUaJ21LaU1C5pYG9jQZbfcr52p93hp90qcBtNC_fwvJQ.png)

Configure the basic settings and click “**Start Site Audit**."

After the audit is complete, navigate to the “**Issues**” tab.

![Issues button in Site Audit tool](https://static.semrush.com/blog/uploads/media/1a/05/1a0595a23a69cd74e9e2eb285b7e4daa/bWXf4cS2J0hLoWSiG62nVu0F2udhRsmSwzjQ3c9175_7_MHdo0kQZ_d8GkGO2XnlqigQb_5NosvZ82Jufd_sKncr3kdMCwKZT4gOhuIHzJ4FXi8XIbaIBu26-HQPLudHZGlrWZAX0zrD9iFcNisd1I8.png)

To see link-specific issues, click the “**Category**” drop-down, and select “**Links**.”

![Navigation to Links in Site Audit tool](https://static.semrush.com/blog/uploads/media/ed/0c/ed0c675e27b86ac7592ec874015b7780/WMvRwy3uVwcR5XHycIFOTG8bSqP1ABPfEuOLFS_76hdUdtUzcBaU-H_AvDqd7SBR9S8jJZnof6cVl_FKo4my4VI26cNJuCV65acvTAHIdxEn1hrxJwRpWwij4RqDwIl8_G3v6VktRhKRgABWoMQkEbk.png)

These are all the errors, warnings, and notices pertaining to your site’s links.

![site’s links errors, warnings, and notices](https://static.semrush.com/blog/uploads/media/a1/74/a1747fcd5e90304429357d85b668c607/ZlVhXKNm_DtCBLGKwBI9MCoHUaCkaSRi-37vl74oAVifWVkq_mUmzmyUnvHEOMxRNitAe6uIxWhEccaQc6ZzN9IZK9Q-MGapXdMPshPxnCqMFXxPdBCKyLQkAOMZ0YdtQnHsCX14rDeVSr5ie76ik0A.png)

Click on the “**Why and how to fix it**” link to learn more about each issue and how to address it.

![Why and how to fix it section](https://static.semrush.com/blog/uploads/media/c3/71/c3714841a97448cd7e82eae186b0c5f5/gohgFqZIIL5ho2CRV95wSCy89zfPOiPO_lwqHmzJlJuMBmYyDt0rLOefIUkTOzVNxyaGOTy0jZiX3hUoGLAa70pr1jaC1QTCoYkY2HiGy4crmnq_IHCNMbL9gJDX2tT7UpyHLI4waVCCm9EjEJck1zk.png)

Plus, you can schedule audits to run automatically.

To do so, click the gear icon on the top-right corner. Scroll down to the audit settings, and click on “**Schedule**.”

!["Manage site audit" section](https://static.semrush.com/blog/uploads/media/7b/32/7b321840769f44edd4d69d650b374033/E57E253ezT4d7JmzeKLylv7yNjRGmgC7vPgiZCYBmWj8l6tZLMCD7pchJEhjLDQ33OriUxvqmW1pt0rBqXhfjMvGTZQqXR3px99Z-3OrOU1o6k-XUyMe1FajQAe64oIFuSk3ibiwjZifYVlTgzF0qaQ.png)

Then, click the drop-down to schedule the audit to run on your preferred day of the week.

Click “**Save**.”

![Save Site Audit settings](https://static.semrush.com/blog/uploads/media/b2/31/b23116bc09a48d43be96299ea84b674e/oljuLE3Sdlz7uhgCeoGEl-LwLYqrZldlp9doiSLY_yYj6GEBbPZlxEeG2g-TwMchJnS-93wfQ6rfxuUPIbfVf5tvKHIoT9Dsjzv72RiGm-r4XSFC0oFFjKm5pim7DAtioKrwAysTl_8-55Z0iOB3tfo.png)

Pay close attention to your link issues. And fix them as soon as possible.
