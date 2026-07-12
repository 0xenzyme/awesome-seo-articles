---
title: "13 Most Common Hreflang Mistakes [Semrush Study]"
source: semrush-blog
content_type: "product_or_tool"
freshness_risk: "high"
slug: "the-most-common-hreflang-mistakes-infographic"
url: "https://www.semrush.com/blog/the-most-common-hreflang-mistakes-infographic/"
canonical: "https://www.semrush.com/blog/the-most-common-hreflang-mistakes-infographic/"
author: "Elena Terenteva"
published: "2017-02-15T03:00:00+00:00"
updated: "2017-02-15T03:00:00+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "date_2017_very_old"
  - "product_or_tool_content"
  - "time_sensitive_title"
schema_genre: "General SEO"
fetched_at: "2026-06-12T20:05:17+00:00"
status_code: 200
html_hash: "949ddb3c05d1d0ab613e6ec69895d7dc5d0d35276e02d617e5bb30e6fb88f409"
clean_word_count: 1527
clean_char_count: 9085
---
# 13 Most Common Hreflang Mistakes [Semrush Study]

Technical SEO mistakes can result in not only a bad user experience for your website, but eventually, your rankings, online visibility, and traffic will suffer. When it comes to international SEO, it turns out that [hreflang](https://www.semrush.com/blog/hreflang-attribute-101/) implementation mistakes, in particular, can be extremely harmful. We want to prove this to you with our new research on the most common implementation mistakes.

The results of this research were quite expected, yet at the same time, they surprised us a lot. Let me explain:

If you’ve ever dealt with hreflangs, you know how many details need to be considered and how many pages need to be analyzed. During our research, we found out that the average multilingual website has around seven language versions; so we are talking about websites with a vast amount of pages here. Naturally, we expected that the frequency of mistakes would be high.

What really surprised us was that the number of href lang mistakes would be so high!

Last year, the SEMrush team conducted research on [the most common on-site SEO issues](https://www.semrush.com/blog/semrush-study-on-site-seo-issues/), which led to a huge debate: “Does it matter how many times I have one or another small mistake on my website--for example, a missing ALT attribute--if it has nothing to do with my rankings whatsoever?”

Okay, missing ALT tags can be forgiven, but [hreflang mistakes](https://www.semrush.com/blog/hreflang-errors/), no matter how ‘small’ they are, can’t! Your goal is to reduce your bounce rate and improve your conversions by ensuring that your target audience lands on the version of your page that is most suitable for them.

However, without proper implementation, you are unable to clearly indicate to Google which page to index and display for a particular region. These factors have a direct impact on your visibility and traffic in the region.

It’s quite surprising to see that the percentage of websites with the simplest issue - “wrong country code in a hreflang value”--is the same as the percentage of websites that have missing ALT tags on at least one page! But the consequences of these mistakes are dramatically different.

Therefore, we hope this research will call attention to hreflang mistakes and help you to understand and estimate the potential danger of them. Also, we want to give you a hint as to which mistakes on your website should be fixed first.

## How did we collect all this data?

We analyzed 20,000 websites that have multiple language versions using the [SEMrush Site Audit tool](https://www.semrush.com/features/site-audit/?utm_source=blog&utm_medium=hreflang-research&utm_campaign=international-seo) - a powerful site auditor that checks websites according to approximately 50 parameters.

The SEMrush Site Audit tool offers 13 checks for hreflang attribute and is developed based on [Google’s standards](https://support.google.com/webmasters/answer/189077?hl=en). Below you’ll see the percentage of websites with common mistakes and issues which were detected on at least one page.

![SEMrush research about hreflangs](https://static.semrush.com/blog/uploads/media/71/8f/718f2ab046380ffbecb53a43b941b830/55bb2a11235e7034c57009d00570777c/eng-infographics.png)

## 1. Issues with hreflang values

In this attribute values seem to be the easiest part. All you have to do is use [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) format for the language code and [ISO 3166-1 Alpha 2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format for the country code. But these mistakes can be easily made by accident, even if you are very well versed in the subject of tech SEO. No one is immune to making a typo. You can use the [hreflang tags generator tool by Aleyda Solis](http://www.aleydasolis.com/en/international-seo-tools/hreflang-tags-generator/) to prevent any mistakes.

There is a variety of these codes, so we decided to split them into 5 different categories.

### Unknown language code

The language code in your hreflang attribute must be in ISO 639-1 format. Otherwise, Google will ignore it. Abbreviated terms we’re used to in everyday life are not working here. For example, “eng” would be a mistake, “en” should be used instead.

### Unknown country code

There is another format for the country code --ISO 3166-1 Alpha 2.

The same - familiar abbreviations are not working in hreflangs. “UK” for United Kingdom? Nope, the correct code is “GB” (for Great Britain). So, if you are not sure which code to use, it’s best to double check.

### Underscores used

Using underscores to separate language and country values is not valid. Developers and webmasters use underscores a lot, but hyphens should be used instead.

### Only country code is used

It’s Google’s standard that when using a country code, you must always provide a correct language code as well. Country code alone is not valid.

### Invalid order of values

We also found that in certain cases, values in hreflang attribute are specified in reverse order. A language code must always precede a country code. It’s not always the typo, but it could come from a misunderstanding of Google’s basic requirements. Fortunately, it’s rarely made.

## 2. Hreflang conflicts within a page source code

In this section, we collected hreflang mistakes related to the conflicts in a page’s source code. They are difficult to detect manually because to identify them the entire page code should be examined, not just a single line of code. We detected these issues on 58% of all analyzed websites.

### No self-referencing hreflang tag

This is the most common issue in this section. We found out that if a website has a conflict within a page source code, in 96% of cases, the page doesn’t contain a self-referencing hreflang. That means that those attributes may be ignored or interpreted incorrectly.

To fix this mistake, make sure to include the page’s URL and language code in your set of attributes.

### Conflicting hreflang and rel=canonical tags

When using canonical tags on a webpage, you should make sure to specify a self-referential canonical tag.

### More than one URL is specified

If more than one URL is specified for the same language and country, Googlebot will ignore all of them because there is no clear message about which page should be indexed for this language version.

To fix this mistake, remove all conflicting hreflang URLs and make sure that you only have one URL specified for a particular language and country.

## 3. Issues with incorrect hreflang links

The second group of mistakes is related to incorrect hreflang links. You have to point Google in the right direction to index all your pages. If the href lang points to the page that doesn’t exist (4xx HTTP status code) or redirected, or you are using a relative URL instead of an absolute URL, these pages could be indexed incorrectly, or not indexed at all.

### Redirected page

If your hreflang link points to a page that is redirected, the new page may not get indexed or even appear in search results.

### Broken link

If your hreflang link points to a URL that returns a 4xx or 5xx HTTP status code, obviously it will be ignored by search engines.

### Relative links

Relative URLs can be misinterpreted by Googlebot, so they might not be indexed.

Try to avoid them and give crawlers the correct path.

## 4. Potentially missing hreflangs

When you have a multilingual site, it’s very easy to forget to specify a language for some of the pages.

We noticed that about 32% of the websites have different sets of languages for different pages. We understand that some hreflangs may not be specified on your pages deliberately, but this is not true in all 32% of cases.

If you want to double check that all your pages have required attributes, you need to check all of the pages manually. However, the **SEMrush International SEO report** enables you to check your website in a glance.

## 5. Hreflang language mismatch

When you specify a page’s language, it’s very easy to make a typo or use a wrong language code, thereby giving Google a wrong signal. For example, if you write a “fi” instead of “fr”, Googlebot will think that this page (written in French) must be shown to users who speak Finnish.

During the research, we saw that on 21% of all the analyzed websites page’s language, value is different from the detected page’s language (at least on one page).

## Conclusion

As you can see, the majority of hreflang mistakes have pretty serious consequences: they can lead search engines to a dead end, therefore, confusing them by preventing pages and even URL sets from being indexed. We hope that this data will help you to begin improving your international SEO and avoid making new mistakes in the future. Keep your website healthy and don't forget to run a site audit!

We’d love to hear your comments about what kind of hreflang mistakes you are dealing with most of all! Which ones cause the most difficult problems? Please share your experience!
