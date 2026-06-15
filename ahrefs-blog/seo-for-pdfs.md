---
title: "How to Optimize PDFs for SEO (7 Steps)"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "seo-for-pdfs"
url: "https://ahrefs.com/blog/seo-for-pdfs/"
canonical: "https://ahrefs.com/blog/seo-for-pdfs/"
author: "Patrick Stox"
published: "2020-07-16T16:00:45+00:00"
updated: "2023-08-23T05:12:55+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "date_2023_aging"
fetched_at: "2026-06-12T12:04:57+00:00"
status_code: 200
html_hash: "78e88cc8424510247d27b287878a6045a3703e484b6c84cde3181afde758c458"
clean_word_count: 1803
clean_char_count: 10541
---
# How To Optimize PDFs For SEO, But You Should Make Pages Instead

Google [first started indexing PDFs in 2001](https://webmasters.googleblog.com/2011/09/pdfs-in-google-search-results.html). The format is commonly used in government, academia, and business environments.

PDFs are great for compatibility and consistency. They work on nearly any device and always maintain the same visual look. However, if you’re creating new content for the web, you should consider using web pages over PDFs.

If you still want to optimize your PDFs, I’ll show you how, but I don’t recommend it. Let’s explore:

- [How Google treats PDFs](#how-google-treats-pdfs)
- [Why PDFs aren’t great for SEO](#disadvantages-of-pdfs)
- [How to optimize PDFs](#how-to-optimize-pdfs)
- [How to track PDF views](#how-to-track-pdf-views)

## How Google treats PDFs

PDFs show in Google search results with a PDF tag.

PDFs are converted to and [indexed as HTML](https://twitter.com/JohnMu/status/1035077656625250304). For PDFs where there are images of text, Google uses [Optical Character Recognition (OCR)](https://googleblog.blogspot.com/2008/10/picture-of-thousand-words.html) technology to convert the image of text into text. Images in PDFs are also indexed in image search results.

Google chooses pages over PDFs if they’re duplicate. If you have pages and PDFs with the same content, Google tends to prefer the page version of the content as the lead version of the [duplicate cluster](https://ahrefs.com/blog/duplicate-content/). This means that signals will be consolidated to the page version and that will be the version that shows in search results.

I’m not sure if Google will index PDFs when embedded in another page. Many people want to do this in order to track clicks on the PDFs. There are better ways I will discuss later in the article.

I ran a couple tests using an ‘object’ tag and an <iframe> to embed a PDF into a webpage. At least with URL Inspection tool in Google Search Console, I didn’t see the content in the screenshot or the rendered HTML. However, this may just be a quirk with the URL Inspection tool. It typically won’t work for other types of content besides HTML. It’s possible that the part of the renderer that processes PDFs doesn’t run for the inspection test and that Google would actually index the embedded PDF, but I’d want to test that further before I would rely on it.

## Why PDFs aren’t great for SEO

Even though Google indexes and occasionally ranks PDFs, the format has a few disadvantages over web pages:

1. **Not mobile-friendly**. PDFs are made to have a consistent appearance across devices. That means there is no such thing as a mobile-friendly PDF.
2. **Lack of navigation**. Most PDFs do not include navigational elements, making it more difficult for people to explore other content.
3. **Lack of some SEO attributes**. PDF files have equivalent versions of many SEO elements, but there are also many elements missing like individual link attributes like [nofollow](https://ahrefs.com/blog/nofollow-links/), UGC, and sponsored.
4. **May not be crawled often**. Because PDFs rarely change, they tend to be crawled less often than pages that are updated more frequently.
5. **Tracking is more difficult**. Most common trackers run JavaScript on a web page and don’t work in PDF files.

That said, I’m well aware that there are some situations where there’s no way around using a PDF for your content. If that’s the case for you, keep reading to learn how to optimize your PDFs for search.

## How to optimize a PDF

Most [on-page SEO](https://ahrefs.com/seo/on-page-seo) elements that you’re used to seeing in HTML have an equivalent version in PDFs and are used in the same way you’re used to. Many are also there for accessibility reasons. So let’s discuss a few ways to optimize PDFs for SEO:

1. [Write good content](#write-good-content)
2. [Add an optimized title](#add-optimized-title)
3. [Add an optimized description](#add-optimized-description)
4. [Use a relevant filename](#use-relevant-filename)
5. [Include image alt attributes](#include-image-alt-text)
6. [Use headings](#use-headings)
7. [Include links](#include-links)

### 1. Write good content

Google’s company mission is to organize the world’s information. Even if it’s not a web page, [good content](https://ahrefs.com/blog/how-to-write-great-content/) is good content. I’ve seen lots of great content in PDFs like technical documentation, whitepapers, etc. Some of the best information on the web is buried in PDFs.

### 2. Add an optimized title

Just like web pages have [title tags](https://ahrefs.com/blog/title-tag-seo/), PDFs have titles. Note that many search engines use the title to describe the document in their search results. If a PDF does not have a title, the filename appears in the [SERP](https://ahrefs.com/blog/serps/) instead.

Here’s how to edit a PDFs title in Adobe Acrobat Pro:

1. Click *File > Properties*
2. Edit the *Title* field

### 3. Add an optimized description

As with [meta descriptions](https://ahrefs.com/blog/meta-description-study/) for web pages, this isn’t a [ranking factor](https://ahrefs.com/blog/google-ranking-factors/) but gives you a shot at controlling the text that appears in search results.

1. Click *File > Properties*
2. Click *Additional Metadata*
3. Edit Description

### 4. Use a relevant file name

The filename of the PDF will be part of the [URL](https://ahrefs.com/blog/seo-friendly-urls/). This will impact the URL shown in the search results and is a small ranking factor.

1. Click *File > Save As*
2. Edit File Name

### 5. Include image alt attributes

To help search engines understand the content of your images, you can add [alt text](https://ahrefs.com/blog/alt-text/) to the images in your PDF.

1. Click the Tags icon in the left sidebar
2. Find the image you want to add alt text for in the document hierarchy
3. Right-click on the image
4. Click *Properties*
5. Add relevant alternate text to the box

### 6. Use headings

Just like your heading tags (H1-H6) in web pages, you can specify that certain text in PDFs are headings.

1. Click the Tags icon in the left sidebar
2. Find the text you want to edit in the document hierarchy
3. Right-click on the tag
4. Click *Properties*
5. Select the relevant heading level from the dropdown

### 7. Include Links

Just like any page, [internal](https://ahrefs.com/blog/internal-links-for-seo/) and external links also impact rankings. Links pass [PageRank](https://ahrefs.com/blog/google-pagerank/) and their anchor text adds context. By including links to your PDF and links from your PDF to other pages, you are helping PageRank flow through your site rather than creating a dead end. Some PDFs get a lot of links. Larry Page [once said](https://books.google.com/books?id=eIR3AgAAQBAJ&pg=PA10&lpg=PA10&dq=%E2%80%9CIt+turns+out,+people+who+win+the+Nobel+Prize+have+citations+from+10,000+different+papers&source=bl&ots=kRcBS9yrk-&sig=ACfU3U1XTYFg0W-Zr1AyCE6XsZ7PrfgY9A&hl=en&sa=X&ved=2ahUKEwiOscuznPPpAhU5hXIEHZ-IDFsQ6AEwCnoECGYQAQ#v=onepage&q=%E2%80%9CIt%20turns%20out%2C%20people%20who%20win%20the%20Nobel%20Prize%20have%20citations%20from%2010%2C000%20different%20papers&f=false) “It turns out, people who win the Nobel Prize have citations from 10,000 different papers”

Check out this GDPR document. It has 77K links from 823 referring domains to it but does not link out at all. This is a missed opportunity and adding some internal links from this PDF to other pages on the site might help those pages rank better.

This example from Google is better. Their SEO Starter Guide PDF has 3.37K links from 754 referring domains and they do a good job of passing that value to other pages by linking out from the PDF.

To add links in a PDF:

1. Click the *Edit PDF* button on the right sidebar
2. Click the *Link* dropdown on the Edit menu
3. Click *Add/Edit Web or Document Link*
4. Draw a rectangle around the text you want to link
5. Set the *Link type* to *Invisible Rectangle*
6. Set the *Link Action* to *Open a web page*
7. Add your URL

Sidenote.

The screenshots and instructions above are for Acrobat Pro DC and may vary depending on the software you use.

## How to track PDF views

As we mentioned previously, PDFs are more difficult to track. Because of this, many marketing teams tend to gate PDFs or make them available only after a user fills out a form. By doing this, they shift the focus from tracking performance to lead generation. However, there are some options to track your PDFs including:

### Event tracking

You can track clicks on PDF links and send them to your analytics system. This allows you to see how many times people clicked on the PDF files to download or open them. You can find out how to set these up [here](https://support.google.com/analytics/answer/1012044?hl=en).

### Embeds

If you embed the PDF into a page using JavaScript or an iframe, you can just use the analytics data for the page itself.

### Intermediate tracking script

This is a complex solution, but it’s possible to send PDF clicks through an intermediate tracking script that sends data to your analytics system before sending people to your PDF. You can find one example [here](https://www.bounteous.com/insights/2013/06/04/tracking-pdfs-and-other-downloads-inside-google-analytics-server-side/).

### Server logs

Because PDF files are stored on a server, any access requests for the files will be recorded in your [log files](https://httpd.apache.org/docs/1.3/logs.html).

### 3rd-party data

Because PDFs are rarely tracked in analytics systems, sometimes the best data you have is from another source like Google Search Console or Ahrefs. Ahrefs can also give you data on which of your competitors’ PDFs get the most organic traffic. Just paste their domain into [Site Explorer](https://ahrefs.com/site-explorer), then go to the **Top Pages** report and search for URLs containing `.pdf`

## Final thoughts

Hopefully I’ve convinced you that in most cases you should create new content in web pages and not in PDFs, but what about old PDFs, should you optimize the PDF or change them into pages? In typical SEO fashion, I’m going to go with “it depends”. I really don’t think there’s a right or wrong way to do this. Do what is easier for you. Either way should show a positive impact, but depending on the effort and resources the answer could be optimize PDFs, change PDFs into pages, or do something else instead.

Have questions? Let me know on [Twitter](https://twitter.com/patrickstox).
