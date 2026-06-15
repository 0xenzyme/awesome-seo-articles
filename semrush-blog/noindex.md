---
title: "What Is Noindex Used for? An Overview + Best Practices"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "noindex"
url: "https://www.semrush.com/blog/noindex/"
canonical: "https://www.semrush.com/blog/noindex/"
author: "Sydney Go, Christine Skopec, Simon Fogg"
published: "2024-07-31T12:14:00+00:00"
updated: "2024-07-31T12:14:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2024_watch"
  - "time_sensitive_title"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T18:11:15+00:00"
status_code: 200
html_hash: "1383c9c4708b715829c7a50716b52b3a6c8cc4c11bea7dd1a2e9e4e1de870f84"
clean_word_count: 2003
clean_char_count: 14682
---
# What Is Noindex Used for? An Overview + Best Practices

## What Is Noindex?

Noindex is a rule that tells search engines like Google not to index a given webpage—to prevent it from being stored in a database that’s drawn from to show search results.

This means that when you noindex a page, search engines won’t save that page. And it won't show up in search results when people look for information online.

You might noindex pages you don't want the public to see. Like private content or PDF pages on your site.

In this post, we'll cover everything you need to know about using the noindex rule effectively.

But first, let’s go over why you should care about the noindex directive in the first place.

## Why Is Noindexing Important in SEO?

The noindex rule helps you control which pages are indexed by search engines. And that allows you to impact your site's search engine optimization (SEO) performance.

For example, let’s say you have thin pages (those that offer little value) that you’re unable to remove for one reason or another.

Using noindex rules on these low-quality pages can prevent them from negatively impacting your site's SEO performance. And instead focus search engines' attention on other, more important pages.

That said, you don’t want to accidentally noindex any important pages on your site. If you do, they won’t rank in search results. Harming your visibility and traffic.

So, always double-check your noindex implementation.

## When to Use the Noindex Directive

Various types of content are prime candidates for using the noindex rule. These include:

- **Thin pages**: These pages don't offer much value to users, so they can harm your SEO performance
- **Pages in a staging environment**: These pages aren't meant for the public to see or use. They're meant for your team to make updates and check things.
- **Internal admin pages**: These pages are meant for you and your team. So, you don’t want them to appear in search results.
- **Thank you pages**: These pages are displayed to users after they’ve completed an action like downloading something or making a purchase. You don't want people finding these pages directly from search results because it might confuse them.
- **Downloadable content**: These pages are resources that users are meant to access by filling out a form. So, you don’t want potential prospects finding them without having to provide their contact information.

## How to Noindex a Page

Now that you know which pages need to be noindexed, it’s time to get to the actual implementation.

There are two ways to implement the noindex rule:

1. As an X-Robots-Tag in the HTTP response header, which is useful for non-HTML files like PDFs, images, and videos
2. As a meta tag in your HTML, which is useful for most webpages

Implementing a noindex rule via the HTTP header method is quite technical and requires server-level changes.

Basically, you need to add a line of code to one of your server configuration files (usually [.htaccess](https://www.semrush.com/blog/htaccess-file/)).

For Apache servers (one of the most widely used web servers), the code looks like this if you want to noindex all PDF files across your entire website.

`<Files ~ "\.pdf$">
Header set X-Robots-Tag "noindex"
</Files>`

Given the complexity and potential risks involved, we recommend seeking help from a developer. Because even a small syntax error can break your website.

As for the meta tag noindex method, it's relatively simpler and can be implemented directly in your pages’ HTML.

The tag goes in the <head> section and looks like this:

`<meta name="robots" content="noindex">`

If you're using a content management system (CMS) like WordPress, you can often use SEO plugins to implement noindex meta tags without directly editing code.

To do that using the [Yoast SEO plugin](https://wordpress.org/plugins/wordpress-seo/), open the page you want to noindex in the editor, scroll down to the Yoast SEO section, and click the “**Advanced**” tab.

![advanced tab in yoast seo](https://static.semrush.com/blog/uploads/media/13/b3/13b30eeade76250fa9640da15bd2b1da/819d800744c6da301c0a4ed3738b6a67/AD_4nXdwtUB6lGJI6p_vMUsqzSs2GP3bWVdyR42sZNwAJ8O0GuoRk8sXNrbAoeTP4fp77EPqio9cTzOpXKfuICIokU8SJfiC1b2nOVrepNnBeGWi3w4FwpeZG88wZzVoZ4aCPFTpzI08Yjhuk1tG5IrexvrW1-s.png)

Under “Allow search engines to show this content in search results?,” select “**No**” from the drop-down.

![no option selected to clock search engines from indexing the page](https://static.semrush.com/blog/uploads/media/2e/13/2e1384b4f50545784583ee21ab7053f3/26381fd0dbd4a87bfc0aec45ed5666e2/AD_4nXc_I_N3E6PG2goB-67BV8uXZf5loUlZWwO53QLKruQro-MzZxO8uDYldg9kHkuVZFjLYMSYgDmTHDmbNSQ8g2AvXoHG6dZnrJ8_k6z7JGhaOzGIdQwLdk9FEq9t6-YwPV7rdrcCoosizIm9V3NTHDx81loR.png)

Then, save the post.

To use the [Rank Math SEO plugin](https://wordpress.org/plugins/seo-by-rank-math/), open the page you want to modify in the editor, go to the Rank Math SEO section, and click the “**Advanced**” tab.

Under "Robots Meta," uncheck the box next to "Index" and check the one next to "No Index" instead.

![no index option selected](https://static.semrush.com/blog/uploads/media/e5/6b/e56b8e7cced39791a0303049a9863099/42e6093fc3a57d24666887d6503bc5c0/AD_4nXeTpSn77iVrO3785KjCIR6nsTWfBJxqTtqJ8gYLeemsrsW0tnhmZn7K-r2WD16UPVfgcdZe1awwSzayJkCy7-GVm3pGXil7jXMqcyZiBDHIMc2eUMq6vX6JxWUxlcBUwMqGYOd32j6uSwUWNjK57GZtFhlu.png)

Save the post to update your settings.

## Best Practices for Using Noindex Rules

Here are some best practices to keep in mind while you’re working with noindex directives.

### 1. Don’t Noindex Pages You Want to Appear in Search Results

The noindex rule prevents a page from getting indexed and shown in search results. So, if you want a page to be found through search, don't noindex it.

Run our free [website audit](https://www.semrush.com/siteaudit/) to quickly check noindex status. To make sure you haven't accidentally noindexed important pages across your entire site, use Semrush Site Audit.

Open the tool, enter your domain name, and click “**Start Audit**.”

![domain entered into Site Audit tool](https://static.semrush.com/blog/uploads/media/ee/40/ee409b9c0781aa293ecdc8706a499c56/c7105335e5ff0473322621b245c07a1f/AD_4nXcmtoa1u1U7VyyfsfWvSY94F_2NAIgw9MLi1tTW2B7qHGgAKtoHKLdU90yrV6kLS_FpUujMKdYp1KMwtvZu7CaA0UOK_Vr6iOsFWbVp8URlIaXC0O6jfDfmiLbRc5gtMwOVOQf2zK2Pn1G5oBFXeJ9aq2N_.png)

Follow the prompts to configure your settings.

When you’re done, click “**Start Site Audit**.”

![site audit settings pop up](https://static.semrush.com/blog/uploads/media/08/fd/08fd1a224154b66705adc61965094a2d/18fd41afaf53cc923050f09582511a05/AD_4nXfuMLP90KgEKvE-4-VaPMBDwraIQ7DF2zHCSQ4wYMsSVuttNwc9mPMFOm1yFSb4GPVhxpfcPQzU3e2EINEt1_P4czxmcECpcFZcWywpFHp1K39Q82G8mauwEUdCG6SBt8yZUsnW1xz3v_gueHkBfR-UoAU.png)

After the audit is complete, head to the “**Issues**” tab. And use the search bar to enter “noindex.”

You’ll see the number of pages blocked by noindex tags or [robots.txt](https://www.semrush.com/blog/beginners-guide-robots-txt/) (this file tells search engines which pages should and shouldn’t be crawled). You’ll also see whether any pages are noindexed using the X-Robots-Tag method.

![search for noindex issues shows 210 pages are blocked from crawling](https://static.semrush.com/blog/uploads/media/a7/c0/a7c0c2ea050af1d065b029a7c0c8b266/4046c12515c872ce5d41aa7f4183ab1a/AD_4nXfwfaAbmDkQPybmIX8EEkRq4rMJVWs_HN62i9X5S0JvUuntuB3dN_C2rfkvh6C4o43jiXT5g67D_27bSTntoes_232UywKTwXIZAQSgcRGjZb8O5rzqge4kbchUzuqBTB8KoPD_Nw1X2zfJUnUknx4c7W2V.png)

Click the blue number in either issue to view the list of affected pages. And verify that none of those pages have accidentally been noindexed.

![page urls blocked from crawling](https://static.semrush.com/blog/uploads/media/53/b7/53b7f1404177dbd9a010b5e180857bbd/fb79e8bee1390b5184a089498f7ff6e1/AD_4nXfu1LVsxAbyJjasWHUBU41TJrz5MVxhfFUk429q3OcyyaxEOleFeoeNaQrCnpnYe1IE4waXOL2jw7tAYo4L77RWSS2NbI2Y9zoI5JFiIwRo6eWiIrykX-jLMiL2J5RSqIAJvXmwZB_jnicwOyJln_7tFk2T.png)

### 2. Don’t Try to Prevent Indexing Using Your Robots.txt File

The robots.txt file tells search engines which pages to crawl—not which pages to index.

Even if you block a page in robots.txt, search engines might still index it if they find links to it from other pages.

Plus, you actually need search engines to be able to crawl your pages for them to see the noindex tag.

Check your robots.txt file to make sure it's not blocking pages you want to noindex.

You can do this by visiting “[yourdomain.com]/robots.txt.”

Look for the "Disallow" directives in your robots.txt file.

![youtube's robots.txt file disallows indexing /login, /signup, /verify_age, and more pages](https://static.semrush.com/blog/uploads/media/15/1b/151bb9179716ebe91ef40825d215d5ae/0b56a85ab75279d41b9b9a8a2b1ac6ee/AD_4nXcr-bLVALuGcMf0OkYZTPFkgl8Fj6pDDJ5lhNgmclTNrUakRAbw5sa4fVxhgPWZ9bUcC6CVr1acj6shTdZEccoc8Rs5JPIcKfm-hEt6KkhKkjBf9K-brPNxX6hqcXOAjpWfzx_H70_QhXhi2x69OB3acLtc.png)

These tell search engines which pages or directories they shouldn't access. So, make sure the pages you want to noindex aren't listed here.

### 3. Take Steps to Address Nofollow Issues That Might Arise

Noindexing can harm your SEO if the webpages you’re blocking from appearing in search results are among the only links pointing to some of your other pages.

How?

Search engines will only follow links on a noindexed page for a while. And eventually treat those links as nofollow (i.e., that they shouldn’t be followed or pass ranking strength).

If there are other pages on your site with few internal links and some of those links are from your noindexed content, it can become more difficult for search engines to find those other pages.

So, they may not appear in search results. Even if you want them to.

Use [Site Audit](https://www.semrush.com/siteaudit/) to look for the “# pages have only one incoming internal link” notice and click the blue number.

![site audit shows 26 pages have only one incoming internal link for this example domain](https://static.semrush.com/blog/uploads/media/d2/8a/d28a6c3b8fd709d9595abbdf3edeaae2/80720a3c2e831bf181cd77c8bbd71134/AD_4nXcMp9IgtWutiWI9qGOE5uuHEoxiSudX2Cre93WCD_sxIzLi3QPnNVbg-lF0SkIDB5cB6NMV_uGlx49Arv8Yc-_2LOluEU_9mBHRKpYfFmRrhaB9c4OoI7SL1ahvhTZEw7AScHnxl8dGUOqi3k2qR_xZrSCW.png)

You’ll then see the affected pages.

![list of pages with only one incoming internal link](https://static.semrush.com/blog/uploads/media/14/99/14992f06506772aa410c147fb72af086/e224b23b1e440cb5ab86ab10a621a939/AD_4nXeYCOz8hvneJPzw5jRrxEKd-5OAWPjHed-iameQ-xrTv92L2DU7zhE7BUTcICMue6plYaFApzHxnoxSiW6laE6sLSuYp2otcFyouhWP6MtibhcsMvUslHHEU768I42ggvPDVs_eJia4bAi91nVL4WggGP_z.png)

Work to incorporate more links to these pages across your site.

This is a good idea even if the only incoming internal link isn’t from a noindexed page.

### 4. Don’t Use a Noindex Directive for Duplicate Content

[Duplicate content](https://www.semrush.com/blog/duplicate-content/) is when you have two or more pages that have exactly the same or very similar content. Which makes it hard for search engines to decide which version to index and rank in search results.

![original content vs copied word for word vs slightly rewritten all affect seo](https://static.semrush.com/blog/uploads/media/d4/44/d4442e62c127211def44559ce6fc3137/b170c06dde2b619d14485d7ab9ed0c85/AD_4nXeLlGsFVLCTP-FhgmRWDPCzY9QfPiRkysK8WfGvurTAx9eES-ejXpW6KkLnx2YODpezxbaVW43Yyc21dayoJwO7vSnXxLyzaUsiEoFWzMkkkfm7IZCmg1w7FK6SuVVU88-6s3mzJFF-OZQ94eLF5PGJ77Hr.png)

It might seem like using noindex tags on duplicate pages is a good option, but this isn’t the best solution.

Instead, consider using [canonical tags](https://www.semrush.com/blog/canonical-url-guide/).

They tell search engines which version of a page is the main one and should be indexed. Most importantly, they also consolidate ranking strength from all versions to the main page.

### 5. Request a Recrawl if Noindexed Pages Still Appear in Search Results

Noindexed pages might still appear in search results if Google hasn’t recrawled the page since you added the noindex tag. But you can speed up the process by manually requesting a recrawl.

To do this, use [Google Search Console](https://www.semrush.com/blog/google-search-console/) (GSC).

[Log in to GSC](https://search.google.com/search-console) and click “**URL inspection**” in the left-hand menu.

![url inspection tab](https://static.semrush.com/blog/uploads/media/4b/ad/4badd932d96a8ce8a9622787a1fb2f41/e0d6ea9ec9c5ed21e6698a33817612ec/AD_4nXcAuWK-z226d7T40Kmv6xtzZXX7f_fnUWEcPwyYrxovRBgE35nBzWA3a6q-pwMiicSzsKOEOw7c5zRIZclu3wsUivs5pOLMOrYoYCiAthpO045LNXPsfjhVwgjIiAdKQbnmRCeyblq5d6_Ezt359ftCVYo.png)

Now, paste the URL of the page you want Google to recrawl. And hit return.

![url entered into google search console search bar](https://static.semrush.com/blog/uploads/media/9f/a5/9fa58f46d2ee935911a6e5ef9f3216d0/9dc04888e9e505e7bfa54770df6842a4/AD_4nXeeGJLqOn7Q3qC_C4fVrZlxQMGG7f5sXqDv4y1MRCbPamok0Zipg_VLobBtTfeQuLY3kmft6RnqAskdIQOd0MnY7VgvTwA4uVbxX2PaHmT0orcJb1ILFoN5qxa5IBc_UYVep9cLaTWlm06jHy4flcidPZ15.png)

And click "**Request Indexing**."

![request indexing button highlighted](https://static.semrush.com/blog/uploads/media/fe/52/fe52b5341bb0c71e9514a535977dc7ae/f961fe04303a3f28c8ef6a6306b6a1ea/AD_4nXeTKB0f-95_EsJZBZYNTipu_6DMU7AY2lvGWDvp5uJ6n2_8yADLFeroIwWE-5DHNGlSS6OxslW4_6w6xi1yup7-5kmwZMke2T1UcsKNAViO5jGe0EjJUcqnAB7-bHQtDji2g6lxf7aOQdOi9f3_dQ5IpB2d.png)

Google will then recrawl this page.

### 6. Regularly Review Your Noindexed Pages

It's important to check your noindexed pages from time to time. Because mistakes can happen without you noticing. Like if someone on your team accidentally noindexed a page.

By monitoring your noindexed pages regularly, you can find and fix these mistakes quickly. So you don’t see a dip in performance.

Keep track of your noindexed pages using the [Site Audit](https://www.semrush.com/siteaudit/) tool.

To make things even easier, schedule regular scans.

Just go to the “**Schedule**” tab during setup. And select the option to monitor your website on a weekly basis before clicking “**Start Site Audit**.”

![site audit schedule tab highlighted with option to run the audit weekly, every sunday.](https://static.semrush.com/blog/uploads/media/0a/61/0a61b9efdbbbc866d383f7a3248569ab/2f199caa57867e644814927d76d70ec2/AD_4nXcaoYo3upRIzu8hqs3cIfv0Ye7aOC7sxKn1DqGKvCE_wRAs2q9SRn7Qha9nD4Ow-YTBC5ARUlj6Wr40kTRNTuF3vlz_cknVDlNvftov7224Hx2SawaaQO3a2afCt0gnAHdiskIEmyCG3UKUfau3AEuGpwg.png)

This audit will run on a weekly basis. So you can stay on top of any issues that might crop up in the future.
