---
title: "Cumulative Layout Shift: What It Is & How to Improve Your Score"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "cumulative-layout-shift"
url: "https://www.semrush.com/blog/cumulative-layout-shift/"
canonical: "https://www.semrush.com/blog/cumulative-layout-shift/"
author: "Sydney Go, Chris Hanna, Boris Mustapic"
published: "2024-04-26T09:59:00+00:00"
updated: "2024-04-26T09:59:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2024_watch"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T14:55:34+00:00"
status_code: 200
html_hash: "18b1730127ec0f42e0cefcc96f02220ba5293d1f93348fac15d3cf3cfbe89627"
clean_word_count: 2712
clean_char_count: 19725
---
# Cumulative Layout Shift: What It Is & How to Improve Your Score

## What Is Cumulative Layout Shift (CLS)?

Cumulative Layout Shift (CLS) measures the visual stability of your webpage’s content as a user views it. This metric takes into account unexpected movement of elements in the viewport as the page loads.

These kinds of layout shifts can frustrate users because they occur without warning. Making for a poor user experience.

For example, imagine you’re looking to buy new shoes, so you visit a product page for a pair you like. The page begins to load, and you know you want the pair so you go to click or tap the buy button.

But then an ad loads at the top of the screen, and the buy button shifts down. Just as you were about to click it. So you end up clicking on the ad instead.

That's an unexpected layout shift.

![Example diagram of cumulative layout shift showing a buy button on a page being unexpectedly shifted down by an ad that appears after 0.5 seconds of additional page loading time.](https://static.semrush.com/blog/uploads/media/fc/3b/fc3b2f0a4531d6ff3fa98d3834f20642/c245541fcf359339783061845bb2ebd9/xasajBEriCHsDR5Vw2ul__7KiPYezHcF933tIphd-2aMwfV5CtcekOj3MxTLJ_uaAcUAFwBX36odD01yz8rwmNWOfyd_oi0_fO4e-nY3etCm5G0g4RvOy0-m-hRtmIK0z7Fv8lF1MyxhhKxiJQCeqqM.png)

CLS is only concerned with unexpected layout shifts above the fold. Layout shifts that happen outside of the viewport are not factored into your CLS score.

Cumulative Layout Shift is one of Google’s [Core Web Vitals](https://www.semrush.com/blog/core-web-vitals/) (CWVs). These are metrics Google uses to measure your website’s user experience.

Besides CLS, there are two other Core Web Vitals:

- [**Largest Contentful Paint**](https://www.semrush.com/blog/lcp/) **(LCP)**: Measures your page’s perceived load speed
- **Interaction to Next Paint (INP)**: Assesses how responsive your page is

Core Web Vitals are page experience signals that can affect your rankings. So, adhering to Google’s recommendations in line with good CWV scores can lead to better performance in search results.

For CLS specifically, that generally involves limiting the number and extent of shifts of different elements on the page.

## How to Measure Cumulative Layout Shift

There are a few ways to measure your Cumulative Layout Shift score:

### Google’s PageSpeed Insights

[PageSpeed Insights](https://pagespeed.web.dev/) analyzes your website’s CLS on both mobile and desktop.

To find your score, simply input your website’s URL (or a specific page you want to test) in the tool and click the “**Analyze**” button.

![PageSpeed Insights interface with "https://yourdomain.com/" entered in the search bar.](https://static.semrush.com/blog/uploads/media/6a/c6/6ac6b8a863680af1ef670a56a33681d9/42eb1b9cb34d1eb10bf1a3bb9dd776b8/0aIcn3ncrYoWMm1gMK_F8qRfnQm5srg1BgC2kDhl916ikroNu108ZuJ3Z3RmzENYArZI0US0RdcEx1T80DN-B2nVdtj6Ez4eiY8MmLxOYyGK_Rmm3YWutvFCwbvpz68HyaFHEEV3extu0lW0-7FEUNw.png)

You’ll see a report of your CLS performance and other Core Web Vitals.

![Core Web Vitals display in PageSpeed Insights showing the website is failing.](https://static.semrush.com/blog/uploads/media/a7/34/a73491dfce6851d4aaf865c52aba9431/3bb29ab16b4bce36b649cb23fed951a2/nDChO0ShAPI0Ai6lu94ld2uZ9vrhtvnQApVIEyCHpkDBiu6ybKYaStR_vWg9SAK4-3Ag8fJokM2c2S0Pa2N6xkHy29-M2e4hvDUQFODyJxbTyD1ijAAr1Qut8-0JpvF_ppLtDrGiY7oFfQrkEirwpNA.png)

Scroll down to the “Diagnostics” section and select the “**CLS**” filter to see recommendations specifically regarding Cumulative Layout Shift.

![Diagnostics area of PageSpeed Insights showing the CLS filter applied.](https://static.semrush.com/blog/uploads/media/73/da/73dacdfc4de448223b97cc1091ab3244/9e2b33dd6aebe90e0b883151a1dc5565/9dXZPx-vfngPP1Sxd2XvJI4igfh3d3noF0PU6VKuKwL3NCjKH0GvnyTh3mvm5wSLYBnp2Ze6QqFJm8I9Iq3yes20LNyWDBEzMG7MXpaxBplB7Zf00NrrIv59RA4qNy-1mIk1QXdrugmEoAuSeU_3W-M.png)

Note that PageSpeed Insights can only analyze **one page at a time**.

You can also use Lighthouse within Chrome’s DevTools. Bear in mind that this data may provide slightly different results. But you can access it without leaving the page you’re looking to analyze.

Just right click anywhere on the page and select “**Inspect**” (or use Ctrl+Shift+I on Windows, or Cmd+Option+I on Mac).

![Semrush Technical SEO Tools page with right click menu shown and the inspect option highlighted.](https://static.semrush.com/blog/uploads/media/69/4a/694a54c4461bd7b143530511bbf2cdbc/83efb6bcf175cf091be878d44cd0942a/z0yVjkO1ZQTrxh9PynMbu3OXqYOROfHSjRxOddIQkoCqptwHopXSUB4nZ69wr8XaKejbSE7rg3UoZJOGu8zrKYKB8ZDxRAj5A_MpVduig2KD-8IiowSMW172QBvg3gvf6m_WahpVsEhpCnWlbOUBtJQ.png)

In the window that appears, click the “**Lighthouse**” tab. Change any relevant settings and click “**Analyze page load**.”

![Lighthouse interface within DevTools.](https://static.semrush.com/blog/uploads/media/b2/69/b269c439af9351c1852aebac7736547c/326d206110542021c1f1c6ea48031a4d/xrJvEfLEWhEk6NfCbmV_BbJwkLIppm7Ej_KEU1q81ueebIR3NH36p6mttr8P4ikR9WjMt0mZ318lIOE7ojEqJm3hIcLTlEaljNjgWkZBQujvuDh_WPqLi0hW_WTNBcdDUvbM4e4ifvnsUC99vnwKrMA.png)

You’ll then see a similar set of results as you would in PageSpeed Insights.

![Lighthouse performance screen showing a 98 performance score and passing of Core Web Vitals.](https://static.semrush.com/blog/uploads/media/75/e6/75e6cb62c23c7af4200318ad4c40726d/7dedfd52ef878ffd3f13f841b4ca0dae/O3WRh4YrQr1_I6ADtklWLLI5VERW3KTiFeUXlxnl6rA5uQ41-y_ALcx_tFL-SWdRog3GbPSGlPejjFLWFYj0dRNeL3UxKoRevA9UlVb65pa9TKaljMcbX9fcNb_CgrtFPnavFQtuHvKYylzAknv5RU8.png)

As with the PageSpeed Insights tool, you can only use Lighthouse to analyze one page at a time.

### Semrush’s Site Audit Tool

Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool lets you check your Cumulative Layout Shift score for multiple website pages at once.

Simply enter your domain name, and click the “**Start Audit**” button.

![Site Audit domain selection interface.](https://static.semrush.com/blog/uploads/media/a5/ea/a5ea0e6c3b88ff97e3870f037a36109d/1efb8001090858e3d84523a79ee81a4c/so2_inRM_BwaIQ-dIQr7ciXuZKYYKW63sjxQbGvWeZpa4he2k-S15Q6LlnyxbUjttLQWR8dfTml1YXYWMtvcTtV_2fw5g5h1C3tRBywPoM9Xnwxlf7b21ACYCVlUJ9oIp5WhsAndacvyw0W6sRbwZwY.png)

Then, configure the tool’s settings according to your preferences. And click on “**Start Site Audit**” to generate your report.

![Site Audit settings configuration screen.](https://static.semrush.com/blog/uploads/media/c8/39/c839d9528c8dffb2403b3de6a229a1cf/1aceecc13e62212d7bfb220a9784c233/Hl-gKwz8bScwCIZXtYGLwvirM69UbWS01hkxblyf_-WveqxNQVaDmWgjL8vD7vdwPTeICcQOr5PvwMsfDEQuykUAA5UYOyEw2KxzAufeyQ9C_cqlXDwYHOHROrhnOjPnqSgv39gyVOOnMKGWj3vD7j0.png)

In the “Thematic Reports” widget, click “**View details**” under “Core Web Vitals.”

![Site Audit Thematic Reports widget showing the Core Web Vitals report option.](https://static.semrush.com/blog/uploads/media/92/f0/92f05248aeb5672b7c54ea0a376d40ad/c95563f21d643b9a6e163ed8227b7aaa/k14chmOyt6Aq0NGpJ6vZQrbIDrT6qh3eBTkW9T7T7mRbZfCuHQDltOBnKPt9QgxAdH_KD2hOsXm5c_x1hgJ0WUKQDqBkiTHoOwRKPKb3VlWkUn2p5HXmio72wBznnXtqW3mt95CynVMLSWA0_DKTREw.png)

Scroll down to see an overview of your Cumulative Layout Shift scores.

![Site Audit Core Web Vitals interface showing Cumulative Layout Shift scores.](https://static.semrush.com/blog/uploads/media/f5/de/f5ded59229e97de1a077458a4d2ff4bd/37c1d9222a76f1e9713b964359aa72c6/G32KMnTJM50sWM_NXZEnq3oHPVZMmwXkt5-zVCfupn4iDgMUlxvlkiLHD1L_TUJUKeqN5Yq3zkrPyke3JWzJiN_45CFyIqvGkZZuOvg7g2h1gR0HDS3bEQmVfmd6bqL3qxIIuvqTF47O0t36Wzm1jQ8.png)

Click on an issue under the “Top Improvements” area to get more information and recommendations. The tool also shows the number of pages each issue affects.

![Site Audit Core Web Vitals report showing recommendations for improving Cumulative Layout Shift score.](https://static.semrush.com/blog/uploads/media/4e/da/4edaee59f5041527f0d2c1bbb9108759/3626b70d1a017d5f31f9384d3150a386/hp5KNVTEo53fLsl_cGY7dXm4mot7UOpezVAI9t34R7WiQpfr6X8quRSxOMsX3qiCg-9r1TgAQvpYyrbebPAWlnuK_vXeneaYh1jKwBRfJeNUns3jP3qyV3DcWjcDHSN0-yFu850mKnCZSvDww3mZldw.png)

Scroll down to the “Analyzed Pages” table to see which pages Site Audit analyzed for your Core Web Vitals. Click **“Edit list**” and add up to 10 pages you want to analyze.

![Site Audit tool Analyzed Pages section of the Core Web Vitals report showing the 10 pages analyzed.](https://static.semrush.com/blog/uploads/media/93/fe/93feea9beed8cdc7e68c2cf4c0faf60a/cb589f46d8d366995fc14ef2eeb14a78/8K2ne7z6nzpUnfHINjlQ_I1GYPQzFsOX4SBj9SyJss7oGORRW1ThVhYiIYqEJWFfaMihBAqgPQw-s0SCjFXyT6tkkb5hZ86iOHqU2wBBOA_uTgJF3wF8i1iDfTR3pNLSL7Sz5oXLXevS1kwQYuQigv0.png)

The changes will come into effect when you run the audit again.

## What Is a Good CLS Score?

A good CLS score is 0.1 or lower. This means your layout remains stable as it loads. So, visitors can easily read, click, and interact with your content without unexpected shifts disrupting their experience.

Here’s the performance scale:

![Cumulative Layout Shift score scale showing Good is anything up to 0.1, Needs Improvement is up to 0.25, and Poor is above 0.25.](https://static.semrush.com/blog/uploads/media/92/06/92066d98a3ac8add9eea8ed36b55461a/08f6741c1b42a41cf8acc472692b6ed6/QVnaFyFREGu7GNXYtrv94BS65gDdKDIS0n1lIMrZu_9U4Hf0NC7v_MymvhVP8Y2KwyPh1LtmyISl3sygMnqq4LwubRGO_TNV8vv9b_wBu4hHOGPhiQMUAcGnLD8OxKQb9LsgMhBKcKN5rdP1CIC2B9U.png)

Your Cumulative Layout Shift score is a measure of the largest burst of layout shift scores for unexpected layout shifts as your page loads. And layout shift shift scores are made up of two components:

1. Impact fraction
2. Distance fraction

Where:

`Layout shift score = impact fraction x distance fraction`

This means that the larger the elements that shift and the further they shift, the higher your CLS score will be. Likewise, lots of layout shifts of any magnitude that occur in quick succession will lead to higher CLS scores.

## Common Issues That Cause a Poor CLS Score

### Images Without Dimensions

When you add images to your webpage without specifying their width and height, the browser doesn't know how much space to allocate until they finish loading. This can cause other elements on the page to shift unexpectedly.

Imagine you click on a link to a blog post. The title and text load in, and just as you start reading, all the text shifts down because a large image loads below the title but above the body text. This is an unexpected layout shift due to the creator not specifying image dimensions.

![Top illustration showing how layout shifts arise from not specifying image dimensions, with a bottom diagram showing how the layout doesn’t shift when you specify dimensions.](https://static.semrush.com/blog/uploads/media/58/52/5852a519753ab9b48f216bf4223b1000/ffe07a65bff420a7af080ac5186c51a6/-mM15-FxzdU8nQJ6WDilgKt7O-M4cLoFrTuKoaSIfaP9ehSk25qOOUaN1g-wbF887GpH-CFxGanV88RDlw9XOsV_xJMF5Iubdc9KTXn2k9uw_VAkUcoAFcvtoPayF8W6wdVEqGfhvnzU-cLK56DBO1E.png)

### Ads, Embeds, and iFrames Without Dimensions

Ads, embeds, and iframes without set dimensions can also cause layout shifts. These elements can push content around as they load, leading to a poor user experience.

This is common with third-party ads in particular. As you may have limited control over the sizes of ads your network inserts into your content.

### Dynamically Injected Content

When you dynamically add content (like a banner of related posts or a form widget) to a page without first relying on user interaction, you can cause unexpected layout shifts.

Dynamically added content can include:

- Images or videos that load in response to user actions
- Banners that appear after a certain amount of time on the page
- Ads that appear as you scroll
- Social media feeds that load more posts automatically
- Comment sections that expand

When dynamically injected content appears in a way that pushes other elements around on the page, it results in unexpected layout shifts. Affecting your CLS score.

### Web Fonts Causing FOIT/FOUT

Flash of Invisible Text (FOIT) and Flash of Unstyled Text (FOUT) can occur when custom web fonts load. With FOIT, the text is invisible until the main font loads. But the space taken up is based on the fallback font (which may be styled differently to the font you want to show), meaning the layout can shift.

While FOUT shows text in a fallback font and then switches to the web font once it loads. If the two fonts are sufficiently different in style, it can affect the layout of other elements.

![Top illustration showing how flash of invisible text leads to an unexpected layout shift, with the bottom illustration showing how a flash of unstyled text can lead to an unexpected layout shift.](https://static.semrush.com/blog/uploads/media/e3/21/e321d80f15c67042daa107fa0e154dd6/1c7c26810753b99ecee7a3f7ccb405cc/faZDm40WzOA95qGVZ4-pgbFx68vD6b2JrpYxmugoEHD2Jw8zLNm4avgGgfUsWkBtPBEjOHA6Fjx04VGkUL6p9om_EyqqOEKseGIiRVP26r-eIitBd5WK7SgDrKDn_ItchthgtOWoaBGIc56l3NlxqhE.png)

### Improperly Implemented Animations

Certain CSS properties can lead to unexpected layout shifts if you don’t use them correctly. Typically, these are properties like “box-shadow” and “box-sizing,” along with “top” and “left.”

Some properties can trigger a re-layout of a page. While others can lead to layout shifts even if the element that shifts is on its own layer.

## How to Improve Your Cumulative Layout Shift Score

Improving your CLS score can provide users with a better experience. And it could influence your rankings too. Here are a few ways to do this:

### Specify Image Dimensions

Always set width and height attributes for your images, video embeds, and other media. This tells the browser how much space to reserve for these elements.

Defining these dimensions lets the browser allocate space in the document layout **before** the image or video fully loads. Minimizing unexpected layout shifts.

Let’s say you add a website banner for desktop users. If the banner’s image dimensions are 1200 x 400 pixels, add the code below to your website HTML code:

`<img src="banner.jpg" width="1200" height="400" alt="Example banner image.">`

### Use CSS Aspect Ratio Boxes

Implement aspect ratio boxes in your CSS to maintain the same width-to-height ratio regardless of screen size. This ensures your content scales without layout shifts. Ideal for mobile responsiveness.

Aspect ratio boxes work by creating a container with a predefined size ratio. This prevents the content from expanding or contracting in a way that could shift other page elements.

To create a responsive aspect ratio box for a video, you could use something like this:

`.video-container {
position: relative;
padding-bottom: 56.25%;
height: 0;
}
.video-container iframe {
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
}`

The above code keeps your video in a designated area of your webpage and maintains its proper shape. It won't shift or cause layout changes as your page loads.

A more modern approach (on modern browsers that support it) would be something like this:

`.video-container {
aspect-ratio: 16 / 9;
width: 100%;
}
.video-container iframe {
width: 100%;
height: 100%;
}`

### Reserve Space for Dynamic Content

Anticipate and reserve space for dynamic content like ads to prevent them from pushing content around when they load. When the dynamic content loads, it fits into the allocated space without affecting the layout of other page elements.

For example, if you plan to display an ad at the top of an article, include a placeholder the same size as the ad.

Add a div element where you want the ad to appear in your article. Give this div an ID or class you can refer to in your CSS. Like this:

`<div id="ad-placeholder"></div>`

Place this div at the top of your article where the ad will load.

Use CSS properties to specify the dimensions of this placeholder. Ensure these dimensions match the ad size that will load in this space. For example, if the ad is 728 x 90 pixels, add the following CSS code:

`#ad-placeholder {
width: 728px;
height: 90px;
background-color: #f0f0f0;
}`

The above CSS code will make the placeholder div occupy the amount of space intended for the ad before it loads. The background color is a visual cue to notify the user that something will appear there.

To make it responsive, use percentages for width and maintain the aspect ratio with padding. Typically, ads have fixed sizes depending on the device.

Use media queries to adjust the placeholder's size based on the screen size. This way, your placeholder adapts to various screen sizes but remains ready for a specific ad size when viewed on larger screens.

`#ad-placeholder {
width: 100%;
height: 0;
padding-bottom: 12.5%;
background-color: #f0f0f0;
}
@media (min-width: 768px) {
#ad-placeholder {
width: 728px;
height: 90px;
padding-bottom: 0;
}
}`

### Avoid Adding New Content Above Existing Content

Adding content above what's currently on the screen can push everything down, disrupting the user's reading or browsing flow.

Instead of dynamically inserting a promotional banner at the top of a page the user is viewing, consider adding it to a section the user hasn't scrolled to yet. Or, insert it after a user action, like clicking a button.

### Handle Fonts Properly to Prevent FOIT/FOUT

Minimize the impact of web fonts by preloading essential fonts and using the font-display CSS feature to control how and when fonts display.

Preload fonts and set font-display to "optional" to reduce the likelihood of text being invisible (FOIT) or abruptly changing style (FOUT). The “optional” display attribute lets the browser choose to use a fallback font if your main font takes too long to load.

To preload critical web fonts, use a line of code like this:

`<link rel="preload" href="https://example.com/fonts/mywebfont.woff2" as="font" type="font/woff2" crossorigin>`

Use the following in your CSS to ensure the text remains visible during font loading and prevent layout shifts:

`@font-face {
font-family: 'MyWebFont';
src: url('/mywebfont.woff2') format('woff2');
font-display: optional;
}`

### Use the Transform CSS Property for Animations

Finally, if you find animations are leading to poor CLS scores, consider using the “transform” CSS property. This lets you animate elements on the page without leading to unexpected layout shifts.

As with adding image dimensions, this is something your website builder might do for you. But if not, you can use “transform: scale()” instead of changing the height and width properties.

And you can move elements around with “transform: translate(). Rather than changing the top, right, bottom, or left properties.

## Improve Your CLS Score with Semrush

Want a quick snapshot before you dig in? Run a [free SEO check](https://www.semrush.com/siteaudit/) from Semrush for an instant read.

For full-site monitoring, the Site Audit tool identifies your website's CLS issues and provides tailored advice to improve your Cumulative Layout Shift score. And it does the same for other Core Web Vitals too.

Plus, running subsequent audits at regular intervals allows you to monitor improvements over time.

![Site Audit Core Web Vitals overview showing Page Status and Historical Data.](https://static.semrush.com/blog/uploads/media/c4/c1/c4c105298ef412cc32128adcc29a1333/7e0b32a6748aa216e4cb995a701fa362/iwepKmy10zbXYqgl7wvyHOzSkHyC8b-ZKOKabR0vhAAmSo0IGxnLBQ00cZkggJaNhQiW55o0FZ04EOeirLCT_8dZewzJAA92poMN9pbGZJpdG9ycdL_AxEXtCweWL8HmLFMgnYzVVAsajCyZwuktCX0.png)

Try Site Audit today to access a comprehensive performance report with over 140 on-page and technical SEO checks.

*This post was updated in 2024. Excerpts from the original article by Luke Harsel may remain.*
