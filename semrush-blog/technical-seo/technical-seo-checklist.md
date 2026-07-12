---
title: "Full Technical SEO Checklist (from Start to Finish)"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "technical-seo-checklist"
url: "https://www.semrush.com/blog/technical-seo-checklist/"
canonical: "https://www.semrush.com/blog/technical-seo-checklist/"
author: "Tushar Pol, Christine Skopec"
published: "2024-09-18T14:13:00+00:00"
updated: "2025-07-31T09:49:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons: []
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T20:02:13+00:00"
status_code: 200
html_hash: "c82b070527a28124c49233792aa6a003f39414074701db7d76dd782c8d1a0696"
clean_word_count: 4699
clean_char_count: 34583
---
# Full Technical SEO Checklist (from Start to Finish)

Technical SEO is mainly about making sure search engines can find, understand, and properly index (save) your site, but it goes beyond that. Technical SEO also involves creating a seamless user experience for your visitors.

Technical SEO is the foundation on which your SEO success relies. Because many of these activities need to occur before your other SEO tactics have a chance of driving results.

When approaching technical SEO for any website, following a structured process is helpful. That’s why we’ve put together this SEO’s technical checklist.

![The full technical SEO checklist covers crawling and indexing issues, optimizing for user experience, working on your website navigation, meeting other technical requirements, and resolving content-specific-technical issues.](https://static.semrush.com/blog/uploads/media/8d/11/8d11a5ce431cd77050d57e3f34a3dbd7/4137798b001c2e9c94a23a49b715fc8c/AD_4nXdwB1L0-odjYVJnmj6f_CNmLdPRVgwfo7a2E5FMpmw0bDWERFhdjpWVr-XIbQ4mHXFZ4covrFjpURzrVcON1EgoLRc6QwccNUcLfPxBUWDgZAydafjuSbZ9ffn5yLpQ4OjlFuKKWg.png)

While creating this checklist, we also analyzed over 50,000 domains to see how common some of these issues are. We'll share specific data points from our research as we go.

Now, let’s look at the checklist items, one by one.

## 1. Look for Crawling and Indexing Issues

Make sure search engines like Google are able to discover (crawl) and save (index) your site properly to ensure your pages can rank in search results.

### Check Whether Your Site Is Indexed

This is the absolute first thing you need to do because your site won’t show in search results if it isn’t indexed.

The best way to check your indexing status is through Google Search Console (GSC).

In [GSC](https://search.google.com/search-console/about), head to the "**Pages**" report. This will show you exactly which pages are indexed and which are excluded.

![Pages report shows bar graph of not indexed and indexed pages.](https://static.semrush.com/blog/uploads/media/97/46/9746a615436699c425fd253113485a34/2e7c3c1e0bb84e325d40101abee4a40b/AD_4nXe5XJ5l4Oz2oxktfHq9h4u2HZzXM0xYZG-Bll9mdfArGjU1bSIlnS2Lygvhtf2i6ecbPxqgZbYmZPkS4ZmDeX2YtGp7fWrzC3NP9HH1cXX8ayaZpMOxyMpBZOIr0d6UTYRD-QWAgg.png)

The pages that aren’t indexed will be grouped by the specific reason.

![Report shows a section for why pages aren't indexed, including the reason, source, validation, trend, and number of pages.](https://static.semrush.com/blog/uploads/media/16/a4/16a49cc24183b8866add3eec91dc0acd/a401a73ebce2d665b51bd48e1d04d9c3/AD_4nXeCcH-YO94Gx_rKxsNrwA5N_wypHkRZ7m4wL4K5mrvfaYPyPQM7Ww81PGNgjmLsqho42TcpU23rxVl7U75wk6r889bEnGUkJTHqCoSIpzcP-ohh7P6GbA5F6J79UWItHgCM-wNLKA.png)

Here are a few reasons you might see:

- **Crawled - currently not indexed**: Google actually looked at these pages but decided they weren't worth indexing. This usually means the content is low quality or the pages are too similar to existing pages.
- **Blocked by** [**robots.txt**](https://www.semrush.com/blog/beginners-guide-robots-txt/): Your robots.txt file is telling Google not to crawl these pages. Double-check your robots.txt file to make sure you're not accidentally blocking important content.
- **Excluded by** [**‘noindex’ tag**](https://www.semrush.com/blog/noindex/): You might have accidentally added noindex tags to your pages. This explicitly tells Google, "Don't put these pages in search results." Remove this tag from important pages you want to be indexed.

Fix these issues, then use the "**Validate Fix**" button that corresponds to a given issue to ask Google to recrawl your pages.

![After clicking an issue, you can click to learn more and validate fix.](https://static.semrush.com/blog/uploads/media/dd/9d/dd9d0c0537be99255d40c6227e940087/64eecd19536a962c24dde16efa8af692/AD_4nXdoIQ8ARC213AycZTabx1Mk28KwmM9Da8tZFJNIlrcQ_J6XVjucTTt3QLyxF7oLHwHPQz9887LS2PhwGe7YrjxtDk0uoiBwdL9PBjpKsoK2uT4Bk4ldI9hzg9ywTgOGRpgC5svF.png)

### Check for Any Duplicates of Your Website

Having duplicate versions of your site can harm your SEO efforts because search engines view these as separate websites, even though they display the same content. Because they’re all **technically** different versions.

How often do sites run into this issue?

In our study of over 50,000 domains, we found that 27% of websites had both HTTP and HTTPS versions accessible at the same time. Which means this issue is quite common on the web.

For example, your website might be accessible at:

- https://yourdomain.com
- https://www.yourdomain.com
- http://yourdomain.com
- http://www.yourdomain.com

Check if your site is accessible through multiple URLs by entering each variation in your browser.

If multiple versions load, you need to pick one preferred version and redirect all others to it.

Use the HTTPS version as your primary URL (either with or without www—that's your preference). Then implement a [301 permanent redirect](https://www.semrush.com/blog/301-redirects/), so users and search engines are forwarded to your preferred version.

### Make Sure Your Robots.txt File Is Accurately Set Up

An incorrectly configured [robots.txt](https://www.semrush.com/blog/beginners-guide-robots-txt/) file can block important pages from being crawled, so review your robots.txt file to make sure it’s properly configured.

From our dataset, only 2% of websites had robots.txt configuration issues. That’s not a lot of websites, but the consequences can be severe if you happen to have this issue.

A robots.txt file is a plain text file that tells search engine crawlers which parts of your site they’re allowed to access—and which parts to avoid.

The file contains lines that can look like this:

`User-agent: *
Disallow: /admin/
Disallow: /login/
Allow: /`

Your robots.txt file will be located at “yourdomain.com/robots.txt.” Check the "Disallow" directives specifically to make sure you’re not blocking important folders or pages.

### Fix Redirect Chains & Loops

Redirect chains and loops hurt your SEO because they slow things down for users, waste [crawl budget](https://www.semrush.com/blog/crawl-budget/) (search engine resources used to crawl your site), and make it harder for search engines to pass full ranking power to your pages.

So, you should check for and fix these redirect issues to keep your site running smoothly.

A redirect chain occurs when a URL redirects to another URL and then to another, instead of directly reaching the final destination.

![This redirect chain example shows URL A redirect to URL B which redirects to URL C.](https://static.semrush.com/blog/uploads/media/2a/4e/2a4e75e2c221d2affd0b1b7a96ca386c/167fd9d324ce248be9f4c19f569cedf7/AD_4nXcSWCPTX4ARXNR6ajOS83VPeAOCMHpieahSOKphhHRAbDpxUgZRlE00WRE2Xt2wCuLUkxVcz0SyBPgTx2JoVVBIeLMSkCg9J1v_nWzEGHpKMPtRiaC7FgDoWmh1r-08AKdOMsWZqg.png)

A loop happens when a URL redirects to a URL that redirects back to the original, creating an infinite loop.

![In this example, URL Y redirects to URL X which redirects to URL Y.](https://static.semrush.com/blog/uploads/media/33/d9/33d98257925e4ff1e7ca14b73823f64c/2412d2bfca0da5b443e4a3207626b479/AD_4nXf1hX8_yPD3hAdITK5aVqBoVwUvxgrQqHKJryC8q8yNRSRzlw4c11mvxE7b1Duy8aPo_CPlF4hGplUX_Rj_SjCjAbfn1MpZpANmLXJAPxoo-eXVlVT0Gqwuc5eezAJViJzGOblZsQ.png)

Both of these issues occur due to ongoing changes to your website, such as when you restructure URLs and don’t carefully manage redirects during the process.

How common is this problem?

About 12% of websites in our study had redirect chains or loops affecting their performance.

Use Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool to find redirect-related issues on your site.

[Set up a project](https://www.semrush.com/kb/539-configuring-site-audit) in the tool to run a full audit. (It only takes a few minutes for most sites.)

Then, go to the "**Issues**" tab and search for "redirect" in the search bar to see any redirect chains or loops.

![Site Audit shows number of pages with redirect chains and loops.](https://static.semrush.com/blog/uploads/media/a9/a6/a9a65770819a77107ce176d79886bb59/4fa5e0411674e0e13f9e18023f633320/AD_4nXfJSupdGdr8XaJisXL7QtS7QLm7iVjoA-LJDReMybE3oK-sSFRTwhpN93tx_mkb6Uo5Il0VcUBYI7k9XcneQwNGU0DhpAFkRt1nTT6K1YGlPIQvPGvgtqejdYOH4R_YAHE71cCKhw.png)

And the specific URLs involved:

![Page URLs with redirect link issues also shows the chain.](https://static.semrush.com/blog/uploads/media/fb/2b/fb2b29f6db6c50491be49f80aec35bfb/0013d5452b57fac071fb40e3e384b053/AD_4nXc4X6cPNam86rvTy__qKhS3bBBL6EFE2ihpjsBuYBJ2qUjXk98ephu9SjPYxb3-Q27sx75mUpS9aFxFyEDvm_5x2dLGmFq5YOZf3n5bp9094N7ZoT2envLklpLUwVLMnAgO0wOU9w.png)

Fixing these issues is simple:

- **For chains**, update any links or redirects to point directly to the final destination URL
- **For loops**, make sure URLs don’t redirect back to themselves

### Fix Broken Links

Broken internal links direct users to webpages that no longer exist, leading to 404 error pages when they’re clicked. This results in a poor user experience and can signal to search engines that your site isn't well-maintained.

![404 error page says, "We got lost. It looks like the page doesn't exist."](https://static.semrush.com/blog/uploads/media/1c/c7/1cc7be74ea392cafcc47772f3f184e0d/f84e617681b4e6e356ea6437f65f8fa8/AD_4nXdXk0YMECF-ppo8OL7GQQ_zKK6hfYGfvDQBZu0IPaeANQhjslxpWedQ6z0m9UetOsuI9GKi6Q_umRCFbVDEVZi6uDqNH-zUP8EYJITPVOrF_Cf-MecgVwivmJMv-85ZY1LfMh-5NQ.png)

Broken links can be either internal links to your own content or external links pointing to other websites.

In our analysis of over 50,000 domains, we discovered that 52% of websites had broken internal/external links that needed fixing.

The [Site Audit](https://www.semrush.com/siteaudit/) tool can help you easily spot if this issue exists for your site. Go to the “**Issues**” tab and search for “broken.”

You’ll see errors if broken links are present.

![Internal broken link and 4xx status code issues are highlighted.](https://static.semrush.com/blog/uploads/media/1f/6b/1f6b550b13edff7d7baad1e18af102c4/dbc1a8b2f036e38454e34833fe6d6502/AD_4nXepT7FvBTswnGjhcK3IGCBOGhDkMLmS_1vKtF6Ljz_GkWt2PWeG9V_r44z6RFdhTS_Zaiw_EPAT7K7qTM9jg0wQSH3ilprXZ_-1q4XVCz0BkWhBmw5uQxpbjnkGyUFhilkRM-9o.png)

If you click on the detected items, you’ll see the affected pages:

![Page URLs are listed with their HTTP status code.](https://static.semrush.com/blog/uploads/media/3c/89/3c89bb757b693cb7fb61b9aff5b0dcca/1e6360b351070b8b466de13bdb16dc40/AD_4nXeC--CEe4e9nl-6KDbBXKB-JSFRfpTVt-GSI6IXdIQIieBGAL3_M53KfzUl-wNiB4m7vKuKCh0dqKlxIZ-TIZolMLXEtvT-eACOoz0aJilgMFGmuobv4KU8S2iBT4frrpFLvSBlnw.png)

Once you've identified broken links, you have different options depending on the type:

**For broken internal links**:

- Restore the deleted page if possible
- Set up a 301 redirect to send users to a similar relevant page

**For broken external links**:

- Replace the link with an updated version of the page if it exists elsewhere
- Remove the link entirely if no suitable replacement exists
- Find an alternative resource that provides similar information and link to it instead

It’s a good idea to schedule a broken link check every week. It's surprising how quickly these can pile up, especially on larger sites.

You can set up automated crawls with Site Audit.

![In general settings, you can choose Site Audit frequency as a particular day of the week, daily, or once.](https://static.semrush.com/blog/uploads/media/8d/a3/8da3f58a7e7f0140d7ab0160c975e5fc/32fca8a5b09325dda898e41325a22ea9/AD_4nXcia9zUtEmf5VT_V5GynkHWgX7oVPazVmx9RjydNQ7RkSXzQKIf8QoLxnc4I7McmSFK64W16mXmbJVFkM4EVlbj0UGdOuvMJQ3Oli_IGqvXXMyu2PHbQp-4dNk5DVa44LufaN8JMg.png)

### Fix Server Errors

Server errors (5xx errors) are problematic because they prevent search engines from crawling and indexing your content.

A server error indicates that there is something wrong with the server itself. Our technical SEO study revealed that about 10% of websites experience some sort of server error on a regular basis.

One of the most common server errors is the 500 Internal Server Error, which is essentially your server's way of saying, "Something went wrong, but I'm not sure what."

![This 500 error page says, "This page isn't working. This site is currently unable to handle this request."](https://static.semrush.com/blog/uploads/media/02/01/020178fd70a65b42293d42b7e00f29d1/393407c83572bcd96502ce2c43cfb763/AD_4nXdXGHZolQrRbD9JIHt68uvwLXpfQNPWeMFAxzkVNwt72sCgtOwU740nm-XtLDqxFt1H5hEJyau3Gra-s8N8a2DMdZgM0FzIZWO-auvJLHCDZr7ZS66W7FZMwDtlaOLKgrDs0NSxGw.png)

Other server errors include:

- **502 Bad Gateway**: This occurs when your server tries to communicate with another server to fulfill a request, but receives an invalid response
- **503 Service Unavailable**: This typically occurs when the server is overloaded with requests or is currently under maintenance
- **504 Gateway Timeout**: This happens when the server doesn’t respond in time

You can check for server errors on your own by searching for “5xx” errors in [Site Audit](https://www.semrush.com/siteaudit/).

![The tool shows the number of pages that returned 5xx status code.](https://static.semrush.com/blog/uploads/media/4f/02/4f028e9a96a0fef4829adf91bef32968/c60705094e5c113b3d9bec7d7ae92e12/AD_4nXdPZbL8vgH15gIk-JRQJS-rtOQIle4cM9kzsOH3rtCj8e_q3fA5sL8j0bR8Nb3liMFB5nkUbBh5j5QzHAFai-L0YbPtOVwG7G40uT69APqyggOohe3iI476sGJ_5TphWG4iRsI0ew.png)

If you see any errors, click on the link to see the problematic pages and the specific error codes they’re returning. This information will be crucial for troubleshooting.

![Page URLs are listed with their 5xx status code.](https://static.semrush.com/blog/uploads/media/c2/c6/c2c6bd46295b3ceb3739862d34b61ca2/4f03b4ded47ac7cf4d6538272ec24920/AD_4nXcvpNXDLY2cJadHRE4rS2GieLdCHvwEtViNdKefUzm70LBee-Uzcf3NpLeZCzWW3MpitL1XdD1nOJqeAE2YbtI_R3M7opn5jzZrUVXWdkLIZ4QhlJ40KF4My332X5I-7SLp2CNOlw.png)

Fixing server errors requires technical expertise. So work with your developer or hosting provider to resolve them.

## 2. Optimize for User Experience

Search engines tend to reward websites that prioritize a good user experience (UX). Plus, a good experience keeps visitors engaged and encourages them to explore your content.

Here are the main aspects to address:

### Make Sure Your Site Is Mobile-Friendly

Search engines primarily use the mobile version of your site for ranking and indexing, so you should make sure your website displays and functions properly on smartphones.

To check your site's mobile-friendliness, use the [Website Grader](https://website.grader.com/) tool. Just enter your domain and email address, and the tool will analyze whether your site is optimized for mobile.

![The Website Grader tool checks legible font size, tap targets, and responsiveness.](https://static.semrush.com/blog/uploads/media/5e/21/5e217142bc18636ecce4553ef6bdf8c6/31f186dd5a4ff8e981714fd1b61919ff/AD_4nXdb4IkWd5J0r26Ka2-IoFpL9Jnq0a0PHqq7Yc2PGVK7tH5rZhL-8MTJ88C0wio5Aa819sW0lHYcO_Xpf4glY9uwFtiiqlANGyKt4o-fMmF01FZ6PVuQpbGHWIAx93Ae1jS84X2Pig.png)

The tool will show you exactly where your mobile experience falls short and what needs fixing. So you can work alongside your developer team to make the necessary changes.

### Improve Your Core Web Vitals

Improve your [Core Web Vitals](https://www.semrush.com/blog/core-web-vitals/). Google uses them as a ranking factor.

The Core Web Vitals are a set of three main metrics that evaluate your webpage’s overall user experience.

The actual metrics are:

- **Largest Contentful Paint (LCP)**: Measures how quickly the main content of your page loads and becomes visible to users. Google wants this to happen within 2.5 seconds for a good user experience.
- **Interaction to Next Paint (INP)**: Measures how quickly your page responds visually after a user interacts with it (like clicking a button or tapping a link). Specifically, it tracks the time from when you click something to when you see the page update or change. This should happen in less than 200 milliseconds for a good experience.
- **Cumulative Layout Shift (CLS)**: Measures visual stability (i.e., how much elements jump around as the page loads). Google wants your CLS score under 0.1.

Not many websites are fully optimized for these metrics.

According to our study, 96% of websites had at least one page that failed the Core Web Vitals assessment test.

You can use Google Search Console to see your Core Web Vitals performance.

In [GSC](https://search.google.com/search-console/about), navigate to “**Core Web Vitals**” from the sidebar and click "**Open Report**” to see the data.

![The mobile report shows a line graph of poor URLs, URLs needing improvement, and good URLs.](https://static.semrush.com/blog/uploads/media/91/fa/91fae4ffc09672cb53191e2c8d9da94a/68cacd8c65a02373dcd3d704527603bb/AD_4nXeF2fsyk8yXYH4qtDDkQI7IhJ56kRw_IDVTzEuSYKbMXmTPWENYbLA-rpVUG-II-rpGJ7V4Eka0wHonutP8AcS9ca09XUgFV_W-jh1m11CKKMe7yRkgptmaZE386X4IZpa4s-ti.png)

Then, look for pages marked as "Poor" or "Needs Improvement." These pages have failed the Core Web Vitals assessment test and need optimization.

![A section for why URLs aren't considered good shows the severity and number of affected URLs.](https://static.semrush.com/blog/uploads/media/50/8a/508abfccdaf32795ecbdc69c219ef707/3325ac6d21daf2c436df511847416b6e/AD_4nXdx7y85JKX9vhz0S0t0e_O6DaJPShaHfrGCgoqh6kbJOl45xOHmM5JAQknm-YvAePPwqtUndci82mcaReLFXo_Lf3M_j5g1GZAlLKTbZNeT3d0xmA1sAS2i60Xh7fIKij7wQbjQ.png)

Take those URLs and run them through Google’s [PageSpeed Insights](https://pagespeed.web.dev/) tool to get specific recommendations on how to fix the issues.

Like this:

![Diagnostics section of the report shows things reducing unused JavaScript, defer offscreen images, and more.](https://static.semrush.com/blog/uploads/media/72/a7/72a7857a2e47cfdf924b08dbd6ad758f/5d19f501f88ff4880793fa4e8a9fcfc4/AD_4nXeA24yiu5m6IP3Z8a2-5SUuSzdfRpZR2DLkIg0uTp8LrQewlcu3SCLbmIlDp-RQBDvHC4sS5moUfz9W-Ap5FXoU9thBPILsEI51AC8ryJUTMGAyOGj2tKvTwQevYzDL9PRTg4Wa.png)

Work with your developer to implement the suggested fixes.

### Avoid Intrusive Interstitials

Avoid intrusive interstitials because they create a poor user experience, especially on mobile devices with limited screen space.

Intrusive interstitials are pop-ups or overlays that cover a significant portion of your content, making it difficult for users to access the information they came for.

![Intrusive pop-up example shows how an interstitial makes content hard to read on mobile.](https://static.semrush.com/blog/uploads/media/7b/f1/7bf19e9a1b5f3cffa3d97e066f7f1d1e/d76aa34e421cf20bd0d02c4670dd75c1/AD_4nXcZFZ9G5gdL1udDQADOh0hdU6hqRgQA6yrBlACOvyZFwTFLoeATt-L2s1QuDmDfvgCLac7NkSVcr0-RP9OhbC3AT2OUrp-PUnhTaLZpFoGCaOY_D_PEaFkZ2mJ6wBz-tSEy0uk2sQ.png)

What exactly counts as an intrusive interstitial? Here are a few examples:

- Full screen pop-ups that cover the main content immediately after a user lands on your page
- Stand-alone interstitials that users must dismiss before accessing your content
- Layouts where the [above-the-fold](https://www.semrush.com/blog/above-the-fold/) area is occupied by an ad, but the main content is actually underneath

Not all interstitials are problematic, though. Google makes exceptions for:

- Legal obligations like cookie notices or age verification dialogs
- Login dialogs on sites where content is behind a paywall
- Small banners that use a reasonable amount of screen space and can be easily dismissed
- Exit-intent pop-ups that appear when someone is about to leave
- Small pop-ups that appear after a user has been on the page for a while

## 3. Work On Your Website Navigation

Make sure your site has a fairly simple navigation system that will allow users to find important content easily and help search engines understand your site.

### Improve Your Website Structure

A well-structured website is crucial for search engines and users because it determines how efficiently search engines can crawl and understand your content and how easily visitors can navigate your site.

The ideal structure resembles a hierarchy that makes logical sense. Your homepage is at the top, followed by main category pages, then subcategories, and finally individual pages.

This creates clear paths for both users and search engines to follow.

![Ideal site structure shows a tree diagram, starting with homepage and branching into category pages, sub-category pages, and product pages.](https://static.semrush.com/blog/uploads/media/8c/4e/8c4e3c4417346c685c0e8348fd223375/fb77ed973eb2d5778e19f407527bddd5/AD_4nXfz9YR6J4rnRzilc0UIlU3Dq7OItv0Tw3YL4gnJMrvD6Qyki64zuTyEPYD8zbAeLb7JGeh1lfMJcy92r3YGMJ9-JKLZmKQEGJ8tO9vtGzTBV7qOKNcV3gBYH1es41wFh-UhDLmGOA.png)

Each page should be accessible within three or four clicks from your homepage. As you can see in the example above.

### Interlink Your Pages

[Internal linking](https://www.semrush.com/blog/internal-links/) creates pathways between different pages on your site, allowing search engine crawlers to discover your content while helping users find related information.

![A webpage with a highlighted link pointing to another page within the same website.](https://static.semrush.com/blog/uploads/media/35/65/3565fbceb955fa88c5d017e508f27732/4a81a7dfef663b189f8b1d892d006f37/AD_4nXcozA4m8VDadLr9de1mGGGm0OcY8XcYFSja1dg9bAoG5iB9zJq9BNsSRTrTfuPwgTLnn_8pT0K_x9Z6nSFvC6Xfh7ubM7ncThui079ZOsKO0DUczU_4BSllf0qlvZ8Eyrtl9sHwJw.png)

Look for opportunities to add contextual links within your content. When adding links, use descriptive [anchor text](https://www.semrush.com/blog/anchor-text/) rather than generic "click here" or "read more" phrases.

The text you use for the link lets users know where they’re about to go and helps Google understand what the linked page is about.

Some other effective internal linking tactics include:

- Linking from your navigation menu to your most important pages to give them extra authority
- Creating [hub pages](https://www.semrush.com/blog/content-hub/) (main topic pages) that bring together and link to all your related content in one place
- Adding "related posts" sections at the end of articles

Don't go overboard, though. Too many internal links on a page can look spammy.

### Use Breadcrumbs

[Breadcrumbs](https://www.semrush.com/blog/breadcrumbs-for-websites/) improve navigation and help both users and search engines better understand your site’s structure.

They appear at the top of a page and show the path to that page within your site. Users can click on them to easily go back to previous sections.

![Product page has breadcrumbs in the upper left corner. For example, back, home, basketball, shoes.](https://static.semrush.com/blog/uploads/media/3f/ba/3fba96a06582d857bd94c5f521ba2efe/b9f13c95e93e6676e00c0820427ea567/AD_4nXe0WtIP9ujk6QHkXdL64TWrAFgOq5pVyIlqn5Jkul0pjctyO2XIdGp3Q81jOneaGfCny1HqkmR9s1362wJdVLlyzpxTYPlHrgSvMd5I8yI6e0MeVeaQ-hH7OYu__YGa-7_53sRUkw.png)

However, not all sites need to use breadcrumbs.

Breadcrumbs are only worth implementing if your site is relatively large with multiple layers of hierarchical content (like ecommerce stores).

### Fix Orphan Pages

Fix [orphan pages](https://www.semrush.com/blog/orphan-pages/) because they’re difficult for users and search engines to discover—they have no incoming internal links.

![A chart of interconnected pages with three disconnected pages labeled "orphan pages."](https://static.semrush.com/blog/uploads/media/65/30/653072abdcf53ddb91fc2360912b7ab2/45e2d4cdf5666bbe9acaea1d6d6dae96/AD_4nXew3Dtx91-X_d8kNyaaNi80nDcY5m9KUMWWkq-0hqlKICxnRY4DsZk_xsb93v6FA-oNi73ZTHqh9eCEMVmzpVS1hORVbutyVfEgingk72zIEQa-viEtMmxiwGuEDX3j0lnxnMLB.png)

These pages tend to accumulate on larger sites pretty easily.

In our analysis of over 50,000 domains, we found that 69% of those websites had at least one orphan page. So, this issue is quite common.

You can check if your site has any orphan pages using Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool. Go to the “**Issues**” tab and search for “orphan.”

![Site Audit lists orphaned pages in Google Analytics and orphaned pages in sitemaps.](https://static.semrush.com/blog/uploads/media/fc/a3/fca3671dabd3101092b8d77610a8899c/43f257a038967dbb9153dfee0f1fef02/AD_4nXd2qVQ7PANe4fzrWXJpfdxvbnea0AtYSCVYdS5oMWZgK3tFed0kTaNo3EUnc-uHQrYRV1sMJPqWeOFdiebaXwmenROKIC2uizaXXcTBqk5S7Hwq0TVa03qQdFJNmUVvRodjA12VnA.png)

Fix the issue by adding links to the orphan page from other relevant pages.

## 4. Meet Other Technical Requirements

There are many other general best practices that Google wants you to follow for your site.

### Use HTTPS

[Hypertext transfer protocol secure](https://www.semrush.com/blog/what-is-https/) (HTTPS) is the secure version of HTTP that encrypts the connection between the user's browser and your website. To protect sensitive information like login credentials, payment details, and other personal data.

Google has used HTTPS as a ranking signal since 2014, giving a slight SEO advantage to secure sites.

More importantly, modern browsers mark non-HTTPS sites as "Not Secure," which can erode user trust and increase [bounce rates](https://www.semrush.com/blog/bounce-rate/).

![Not Secure message says, "Your connection is not private. Attackers might be trying to steal your information..."](https://static.semrush.com/blog/uploads/media/81/5e/815e1f0329db7a70e8b5bfb94a009d91/01774c6888a2d24e4fcc51a8b5b8d5fd/AD_4nXdbD5z9N-1-pYTkiNgTlLYqUYwM7uaa1KvqXhl0QYoB-7rOu2b39T1uUZzUwB_Dt_3Lp-qbAtrEySbJGJ4Sjy7-5NIrGF4tD6z00lhk3UF66QoVpZ7SNBN6x2bXJL2eKxP8Bi7Qag.png)

You can implement HTTPS on your site by acquiring a Secure Sockets Layer (SSL) certificate. Many web hosting services offer this when you sign up, often for free.

This is more of an advanced technical SEO task, so talk to your development team to get this implemented if it’s not already.

### Implement Hreflang for International Pages

[Hreflang tags](https://www.semrush.com/blog/hreflang-attribute-101/) are used for multilingual or multiregional sites to tell search engines which language and region each version of your page is intended for, ensuring users see the most relevant version in search results.

For example, if we search for the official Disney site in the U.S., we see the American English version:

![Disney's homepage is listed on the search engine results page.](https://static.semrush.com/blog/uploads/media/93/34/933487563c092abf7ee028a45681ff9a/166997c61672c61f2209c4a0d96b63a4/AD_4nXeeOleS3YYsez48IGMlC4AEiKXnF6P6F6TS3Z9cA41hkKN0h3F_PrVNnM_93pAMxPlxMTIR_m9s0kAy8R5oNNSyZEEVr7UGaDEdMv0aJkkQ0LLOHZK_zRuWaWzMH5qLqi6cZ80RRw.png)

If we do the same in Germany, we see German version of the page:

![Disney is listed on the SERP as Disney Deutschland.](https://static.semrush.com/blog/uploads/media/82/52/8252d5c65a6553d0c4be5507cfea345e/84c502937e0a756cf069edbebb1ed69e/AD_4nXdjDBkc5aftEAwCtDjQUZhFWumUeO9rNm6JlJIoysgusRY8CqtPM58sKGt_KV4s1KYLm06HdO0Nja51_GPnxYhldVt87yUVnaEIlpU7qGcDHgffX1h2bLxvdqm6HgHyVxxuCpzObA.png)

Implementing hreflang is simple. Just add the appropriate tags to the <head> section of each language/country-specific version of your page.

For example, if your website targets audiences in the United States, Germany, and Japan, add these hreflang tags to all three versions:

`<link rel="alternate" hreflang="x-default" href="https://yourwebsite.com" />
<link rel="alternate" hreflang="en-us" href="https://yourwebsite.com" />
<link rel="alternate" hreflang="de-de" href="https://yourwebsite.com/de/" />
<link rel="alternate" hreflang="ja-jp" href="https://yourwebsite.com/jp/" />`

The first tag indicates the default or fallback page that should be shown to users when no other variant is appropriate.

Other tags specify the different language or country versions available on your site, ensuring Google serves the right one based on a user's location and language settings.

### Add Schema Markup

[Schema markup](https://www.semrush.com/blog/schema-markup/) is a type of code that helps search engines understand the content on your pages more clearly.

While it's not a direct ranking factor, schema markup enables rich results (special listings on search results pages), which can improve click-through rates.

There are many types of schema markup, but you should focus on the most relevant ones for your specific content types. Which may include:

- Organization (for your homepage)
- Product (for ecommerce product pages)
- Article (for blog posts or news)
- Event (for event pages)
- Recipe (for food sites)
- Review (for product or service reviews)

The easiest way to generate schema is to use a [Schema Markup Generator](https://technicalseo.com/tools/schema-markup-generator/).

To get started:

1. Select the type of markup you need
2. Fill out the form you see on the left-hand side
3. The tool will automatically generate the code for you

![A local business's details like phone number and opening hours are added to schema markup.](https://static.semrush.com/blog/uploads/media/5d/5d/5d5ddb9c479a090ce7e83b762f7551f9/d637abfab4acb325f77a0a1a5f471cb3/AD_4nXcvnSJlPdmJZUk1dX1el01O8ZTwH4s2dxnsgSCGebTurH4ri01ov7EJubcTjE4WNxGUFZuoBBQaSGNQha84OCnCRKGymrunyC1Rg7b81Ey2u8GLHHnatBm0NRU40kNgbZr_-Ic7_w.png)

Once the code is generated, you can add it to the <head> section of your page’s HTML.

After implementation, use Google's [Rich Results Test](https://search.google.com/test/rich-results) tool to verify that your schema is implemented correctly.

![Valid items are detected for the local business and organization.](https://static.semrush.com/blog/uploads/media/22/96/2296bd0aed989a972c702f19cbfbf62f/8e2ed378a00d11abdc25df6177c6c1ff/AD_4nXeE8wQr8-chJeSK6CDMW7qJr0-HQil7I_I6buk9FfmUoXtehvRZb1aNHq4-UBzzfiE03XiJ8KRBm6klyzqmOgfiDDEu2xSWDRSBp9rSpj87Hsexhg39uLJCAWTWS48UBK3AXIaT.png)

## 5. Resolve Content-Specific Technical Issues

This section of our tech SEO checklist addresses how to resolve common content-specific technical issues that can affect your SEO performance.

### Address Duplicate Content

Address [duplicate content](https://www.semrush.com/blog/duplicate-content/) issues because they can hurt your site’s credibility and make it harder for Google to index and rank your content for relevant search terms.

Duplicate content is content that’s identical or highly similar to content that exists elsewhere on your website or on another website.

About 41% of websites had internal duplicate content issues, according to our analysis of over 50,000 domains.

Use [Site Audit](https://www.semrush.com/siteaudit/) to quickly find out if you have duplicate content on your own site.

Just search for “Duplicate” under the “Issues” tab.

![Duplicate content issues are highlighted in the tool.](https://static.semrush.com/blog/uploads/media/3b/73/3b73c11c587b8e8107ba29b7d556b545/9694b53463c6f938041104b198a0c848/AD_4nXdZ-W9jWjPHI4v8pcMX-cs0B-21YtGalux8uvAvuVOiK_51gTQNamOT0bG0gXd76abDejlSxq3xYN5sbEYp-fIClmTwbRX9T8MuhlzgAc1-zen07gYEu7x-J_T7WF-Z9P2T_qhu.png)

Address duplicate content issues by:

- Adding [canonical tags](https://www.semrush.com/blog/canonical-url-guide/) to identify the primary version of your content
- Consolidating duplicate pages into a single, main page and setting up 301 redirects from the old URLs to the main one

### Fix Thin Content

Identify and improve [thin content](https://www.semrush.com/blog/thin-content/) because it can negatively impact your search engine rankings and user experience.

Thin content is a term search engines use to describe pages that offer little to no value to users.

To identify thin content on your site, look for pages that are:

- Poorly written and don’t deliver valuable information
- Copied from other sites
- Filled with ads or spammy links
- Auto-generated using AI or a programmatic method

Once you've identified thin content, take action to improve it:

First, remove or rewrite any directly copied content.

This is the most serious issue. Plagiarism isn't just an SEO problem—it's an ethical one, too.

For the content that’s thin but original, beef it up with meaningful insights, examples, or practical tips that actually help your audience.

For pages overwhelmed with ads, reduce promotions and focus on the user experience.

For auto-generated fluff, either rework it into something useful or get rid of it entirely.

### Ensure All Pages Have Metadata

Metadata helps search engines understand your content and match it to relevant search queries, and it's what users see in search results when deciding whether to click on your page.

So you should ensure all your pages have complete, optimized metadata to improve your search visibility and click-through rates.

Metadata includes elements like the title tag and [meta description](https://www.semrush.com/blog/meta-description/), which summarize the page’s content and purpose. And can be displayed in search results.

(Technically, the title tag isn’t a [meta tag](https://www.semrush.com/blog/meta-tag/) from an HTML perspective. But it’s important for your SEO and worth discussing alongside other metadata.)

Run a free [website audit](https://www.semrush.com/siteaudit/) for a quick meta tag review. To find missing meta descriptions or title tags across your entire site, use Semrush Site Audit tool.

Just filter your results for “Meta tags” from the “Issues” tab. Click the number next to an issue for a full list of pages with that problem.

![Filter for meta tags shows issues like duplicate title tags, pages without title tags, too much or too little text in title tags, and more.](https://static.semrush.com/blog/uploads/media/3c/5a/3c5a7557198b188924305b3f68dcabda/1c2d1a797213f1f9b0f664076f1a253d/AD_4nXc3Zg6k-sr0dntiMHN2f7ZqDebnFkuTFaLO4izoS52zEDck5vQik7Mc3kePOvoACNAmd7wNqdXMyDRViU6AUmicKl7gRWaRAn9EDQhl-A7jqiy_RXeIVhOXb8Q5BNifzcEwSCihEQ.png)

Then, go through and fix each issue. To improve your visibility (and possibly your appearance) in search results.

From what we've seen, issues with meta tags are quite common across the web.

In our analysis of more than 50,000 websites, we discovered that a staggering 70% were missing meta descriptions, and 10% didn't even have a title tag on some of their pages.

## Put This Technical SEO Audit Checklist Into Action

Now that you know what technical SEO action items to prioritize, it’s time to execute.

Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool helps you identify and fix all the technical issues quickly and efficiently.

Sign up for a free account to get started today.
