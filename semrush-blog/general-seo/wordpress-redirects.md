---
title: "How to Redirect URLs on WordPress"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "wordpress-redirects"
url: "https://www.semrush.com/blog/wordpress-redirects/"
canonical: "https://www.semrush.com/blog/wordpress-redirects/"
author: "Carlos Silva"
published: "2021-09-22T19:55:00+00:00"
updated: "2025-01-21T11:21:00+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "time_sensitive_title"
schema_genre: "General SEO"
fetched_at: "2026-06-12T21:24:03+00:00"
status_code: 200
html_hash: "8bbf197c71a93482a419cda21fc153fd769707e22752b482c98921f743ebbdc5"
clean_word_count: 2084
clean_char_count: 15720
---
# How to Redirect URLs on WordPress

Redirecting URLs is an important part of your website’s SEO. Redirects help you avoid duplicate content, improve user experience, and direct traffic and authority to relevant pages.

In this guide, learn how to redirect URLs on WordPress.

Let’s get started.

## What Is a Redirect?

A redirect is a way to automatically send users and search engines from one URL to another, ensuring visitors and search engines reach the correct page.

For example, if you delete a page on your site without setting up a redirect, the user sees a 404 error response, which can harm your SEO.

Search engines don’t index pages that return a 404. Plus, any [backlinks](https://www.semrush.com/blog/what-are-backlinks/) (also called “inbound links”) pointing to a broken or deleted page lose their value.

So, when you delete a page, first set up a 301 redirect to redirect users to a similar page that serves the same intent.

This way, you’ll retain the old page’s backlinks and [authority](https://www.semrush.com/blog/how-to-build-website-authority/) and ensure users don’t get 404 messages.

You can easily find broken pages and incomplete redirects using a tool like [Site Audit](https://www.semrush.com/siteaudit/).

![search for "redirect" in Site Audit "Issues" tab to find broken pages and incomplete redirects](https://static.semrush.com/blog/uploads/media/b6/3e/b63e37487db227271d69a56d220a1e2d/7oG4cL2OZB6w3Ku5v_bIAj8hodMEGt64KeJU1iuVCkNX04M9YzqR0DZzWp6nbL4NMdHKblRE4S72CbqvCLNDM72iZzo9qeIyPlBYSzbc2m4PHssXcCGtRxFv3P-2YkpFIslPdBA5qwSTWAG-GJ7DpF4.png)

### How to Use Redirects

Use [redirects](https://www.semrush.com/blog/redirects/) whenever you do a major website update, migrate your site to a new server, change page URLs, or update your website navigation.

You can also use redirects to avoid creating duplicate content and fix [keyword cannibalization](https://www.semrush.com/blog/keyword-cannibalization-guide/) issues.

When you move content to a new page with a new [URL](https://www.semrush.com/blog/what-is-a-url/), you can set a redirect so users land on the new page instead of the old one.

## Types of Redirects

- **301**: A permanent redirect. Use a [301 redirect](https://www.semrush.com/blog/301-redirects/) when a page has moved to a new destination permanently. 301 redirects pass the most link equity (or “link juice”) and work best for SEO.
- [**302**](https://www.semrush.com/blog/302-redirect/)**/**[**307**](https://www.semrush.com/blog/307-redirect/): Temporary redirects. Use temporary redirects when briefly moving a page to a new location, or when you want to redirect users to a new page or website temporarily (e.g., a sales page for a limited-time offer).
- **Meta refresh**: Also known as an [HTML redirect](https://www.semrush.com/blog/html-redirect/). A meta refresh is implemented client-side (i.e., in the user’s browser), not on your server. It sends users to a new page after a set time. HTML redirects have several drawbacks and aren’t recommended for SEO.
- [**HTTP to HTTPS**](https://www.semrush.com/blog/redirect-http-to-https/): A type of 301 redirect that forces browsers to display the secure HTTPS version of a page

Redirects fall into two main categories:

- **Client-side redirects**: The browser processes these redirects. A user can trigger a client-side redirect when selecting a link. For example, if you see a message like “Click on this link if you’re not redirected in 5 seconds,” that’s a client-side redirect.
- **Server-side redirects**: This redirect occurs when the server sends a redirect status code. When a user clicks on an old link and automatically lands on a new page, a server-side redirect is taking place.

## How to Redirect a URL on WordPress via .htaccess

An .htaccess file is a configuration file that tells your server how to display pages from the WordPress root directory.

Use this method only if you’re a web developer, or if you’re very familiar with your WordPress CMS’s technical backend.

### WordPress Redirects via .htaccess File

To redirect a URL using your .htaccess file, first verify your web host’s .htaccess editing rules. Check that you have edit-level access.

Back up your site and create a copy of your current .htaccess file. This way, you can revert to your original file if something goes wrong.

In the root directory, add this line of code at the top:

`Redirect 301 /current-page.html http://www.yoursite.com/new-page/`

***Further reading**:* [*Complete .htaccess File Tutorial: What It Is & How to Use It*](https://www.semrush.com/blog/htaccess-file/#what-is-an--htaccess-file)

## How to Redirect a URL on WordPress with a Plugin

Using a plugin is an easy way to implement redirects in WordPress. Many plugins are available, and they reduce the chance of errors.

Most follow the same basic process:

1. Download and install the plugin
2. Go to the “redirects” section
3. Add the old URL and the new, target URL
4. Test the redirect

Below are examples using three plugins: Yoast SEO, Redirection, and 301 Redirects.

### Yoast SEO

Yoast SEO is a trusted WordPress plugin for various SEO tasks, including redirects.

Start by logging into the backend of your website and backing up your site.

Download the [Yoast SEO plugin](https://yoast.com/wordpress/plugins/seo/) from the WordPress plugin directory.

![YoastSEO plugin install page](https://static.semrush.com/blog/uploads/media/62/de/62def69d3361a74b085f2727be214bc4/eidLNdvE_T4J_JwwvMYKXdroFYco_iobPnGSvMjf_6pVkrGSkRUpa6Mt5Qcawet88BQQ6yEYviGJrhcNeHxKA6LqaZHjdSgYfZ8dJtkQ9obbwuCfvxt9mqQDzOlPEc-vqnMWuXicWhu0bF9cyByQx0E.jpeg)

After installation, go to the “Plugins” page and click “**Activate**.”

In the left-hand toolbar, select the Yoast menu (“SEO” next to the “Y” symbol). Then, select “**Redirects**.”

![“Redirects” button highlighted in the left-hand toolbar](https://static.semrush.com/blog/uploads/media/86/d9/86d90fd93b505bfd2a1788e520bb0b28/DLsQ2ZqBZBuhAfudtsjU-h0k0Y43dSIr9Y6L1Y8rQX2gY-KJLnOCFRHsw5MQQmQKw0-mmmHhlWWzJeQKgX5KMfUhHfnYPcPj6KP1L4AJ3q2MSxlnLG2G1XvUW2LN9IwmJ5bfLp08qXEmWQzKX8j-EOo.png)

Choose the type of redirect:

- **301**: Permanently moved, the final destination
- **302**: Found but moved temporarily
- **307**: Temporarily redirected
- **410**: Content deleted (for old, outdated content you want to delete)
- **451**: Unavailable for legal reasons

![drop-down menu with different redirect types](https://static.semrush.com/blog/uploads/media/32/46/3246e9499fef61a1830e44842715d7f1/oTkjbQT9Vtdp1zfUuYz-WIkOnULQM4eCjHehxpC85dfCyUwxE0hY3AHPCHDVBrmp-wepHeQkuTHuwhgYlr_kGB2xnD76i-JlnN3UhHW6skC-8j50xjO0vYIgzRQVpMTj62IrVDDTpt5UwnbfRgznm90.png)

Enter the old URL slug and the new destination URL. Click “**Add Redirect**.”

!["old URL" and "URL" fields](https://static.semrush.com/blog/uploads/media/1d/9a/1d9a8023f20869e66b7940bd500c26c0/uep9Wq4Q9LwtWoNUH3A7p4Nc_y9Rn0eo4PGVOb_sVjiBrfa-dXewzSSkT99a9NP2xV8f0K8neDBnK7t2I44gXheKITZP2lNg6x0SuhA6tPpHuDliSSWMIih_qRgxLhFLqmfAzVyJ3NGUmfS0VP6_MoM.png)

Test the redirect by typing the URL into your browser. If the redirect fails, clear your browser cache and try again.

### Redirection

[Redirection](https://wordpress.org/plugins/redirection/) is a user-friendly plugin created by John Goodley for WordPress URL redirects.

As with Yoast, back up your site before installing a new plugin.

Download and install the Redirection plugin from the WordPress plugin directory.

![Redirection plugin install page](https://static.semrush.com/blog/uploads/media/ef/77/ef774bfd6543dcac4933e266872cc62f/FhF7tcbYocTatt5DF3nSUVAZzhzT8g8SriWTKMvb7cjZ4PTgNNmETdFT9VoAA5IblR8MQqqrvTqLEYNNKdS_SEmVW2ZEbjAD1oPsc6v2KoCU6hGaRkaXsI4wvk_-53nr1gs8_FUaZrkLQVIyNiZKpeQ.jpeg)

In the left-side menu panel, go to “Tools” and select “**Redirection**.”

![“Redirection” button highlighted in the "Tools" section of the menu](https://static.semrush.com/blog/uploads/media/1a/4d/1a4defffb6f2e31fe771ce5491e709b9/ZFb-FgqhLB-toAVJCBjOVVPbGQN3Kwo4EGtYxdes6Q4p5CesXOl6mvMSnDTDGkY8-klRTt7lvsA_T5S5ITonGX1tX1g6HgZ0uAO_U-4kwiMW4yW4vdhWwibTFkbwuQ6XFyF755EVbHBMnGq-QH8_JM8.png)

Click “**Add New**” at the top of the page.

Enter the slug of the old URL in the “Source URL” field.

Enter the new URL slug in the “Target URL” field and click “**Add Redirect**.”

!["Add new redirection" page](https://static.semrush.com/blog/uploads/media/16/a5/16a50703ff9233f825e9ecc50ae66e19/CJ1srVj6udAQyBStyCgWqqm77Equ8UD1Xk75tMMnEljN6lgn_BGKan-UmsFBvW8xaq-xs55cEo-6App8wt4CAXQUReOoi_1S9IOoiI8fWNfZjk0_Mc6o_AyWDJt5TfhyreOY96qt3zCyEntPnsEf0Ew.png)

Test the redirect by visiting the old URL. If the page doesn’t redirect you, clear your browser’s cache and try again.

### 301 Redirects

[301 Redirects](https://wordpress.org/plugins/301-redirects/) is another plugin that makes it easy to redirect URLs in WordPress.

Back up your site. Then download, install, and activate the 301 Redirects plugin.

![301 Redirects plugin](https://static.semrush.com/blog/uploads/media/a7/59/a759aceb1e65f0e5ff1a987fdbf3defa/bfoOCoz2vPaTH5pz0lAQNk2mtFy3myEgy-dcQgpSrLowmlfnlprdt7ZKZC2guKEjkm1QqnDqTQffLBo9I3Hhbnugbj7SYiNUxIxiWFHIapRLSM_nkVVkg2brAWgQq7mLP7XP1qHH9iFicTNyf6ZtjJE.png)

Go to the “Plugins” page. Under “301 Redirects,” select “**Manage Redirects**.”

!["Manage Redirects” highlighted in 301 Redirects plugin](https://static.semrush.com/blog/uploads/media/32/08/32088cc914ccae2ab9469fd08f67a48c/63eA2HPeeDUpjGqND14Kmn1Jtmi_X57JFAJsKN-RFu1fU1uAHYzfox0kHaXkLvjWMtA0D_uKQcpDi8RWwiyEL-8ISYMzINfMrrL-MctDmCOh_0yuIMPGUkMYX9Ih9KjwlVsYSe-AHVn5haq7T86Zj4Y.png)

Choose the ID or redirect type (301, 302, or 307).

Add the slug of the old URL in the “Redirect From” field.

Next, enter the new URL in the “Redirect To” field. Click “**Save**.”

!["Redirect Rules" section](https://static.semrush.com/blog/uploads/media/33/87/3387ed3d2c299128a622f629336b14b3/nqDnJgU9vxkdzjdxV5lpmAIzqDoseyI1FlJZPqoiIREgiUQFkwFnS4CpZbFPoTf1rxaHlXTnKDuQ0nPMrnV-MPnixDSLBpLKV3ABZAprEKWtZ6LL6RJ1t81lsiTiQHn8_gKbM95eWW3y5jR7i3upiUY.png)

The 301 redirect is now live. Test it by visiting the old URL. If the redirect fails, clear your cache and try again.

## Find & Fix Broken Links

Find and fix broken links and redirect errors as soon as possible.

Here’s why:

If a user clicks on a link and encounters a [4xx error](https://www.semrush.com/blog/400-bad-request/), they might leave the page—and your website.

This poor user experience also affects your SEO.

Running regular [website audits](https://www.semrush.com/blog/seo-audit/) can help you find any problems that arise as you update your site. For instance, if you move a page and forget to add a redirect, a site auditing tool can discover the resulting error.

To audit your site for broken links, use [Site Audit](https://www.semrush.com/siteaudit/).

Enter your domain into the tool and click “**Start Audit**.”

![Site Audit search bar](https://static.semrush.com/blog/uploads/media/96/eb/96ebff4237c8b4e943d3c015001778c8/UiH30WSwnmj6c3wTaDHN8JvdMK9IDNSaUOZ9wxNSU1S5roddYjlbibenH3UWq2ych7tKIYoO7zBUAMz5cAdyDBekG-nuv2QLdHnlB1z1Qa3sgQoCQQ6uReRoaQf_IMitgtXCmMNTuiEtooCpPwppBIY.png)

After [configuring your settings](https://www.semrush.com/kb/539-configuring-site-audit), click “**Start Site Audit**.”

!["Site Audit Settings" page](https://static.semrush.com/blog/uploads/media/55/82/55826fb696dbf6432ecccf6538c2ae60/4wRohohVKzux_q0IjqZuWM34_xd898sKDZD6053VFTLgfybN2wpV4XwENLJUbawTTz9FUMxKOViZRKV7QGpa7VCW4hC78hFPYQuaQQ33Y2uMqb24fTqJs1ES66VRDS3I9Iu60CiNM17TyHYBZ_wxbQ4.png)

In the dashboard, go to the “**Issues**” tab and type “broken” in the search bar.

Like this:

![search for “broken” in Site Audit "Issues" tab](https://static.semrush.com/blog/uploads/media/1a/4a/1a4a082892db970ae4c4e69bb444b389/zTvHe9rvaeRFgLuqkRxMWj_PhHiHwTXLtJ0J9I3qK-BiOSRtoyPhSxEZaivioLXVLnyITp5rvSBy00_oFPiDhyedziotnyXoK-6xtpT4tG0xe64ivOd7uHbehAnn6BhIv0AhvQMLlSX_AUoF0ZZZVm8.png)

You’ll see all the “Errors,” “Warnings,” and “Notices” about broken links on your site.

Fix as many issues as possible, starting with “Errors.”

### Issue: Pages with Temporary Redirects

Temporary redirects aren’t fully SEO-friendly.

Search engines may index the redirected page, but the new page won’t receive page authority from the old page’s backlinks. Losing these backlinks can negatively affect the page’s ranking and traffic.

To check for temporary redirect issues, open your Site Audit report. Click the “**Issues**” tab, and type “redirect” in the search bar.

You’ll see a list of all the “Errors,” “Warnings,” and “Notices” on your site related to redirect issues.

Click “**Why and how to fix it**” beside each issue and follow the instructions.

![search for “redirect” in Site Audit "Issues" tab](https://static.semrush.com/blog/uploads/media/c7/8e/c78e429c0a211783af8eefa1c852df26/NqSY8ScNSazr8UdNlv6G3rNft6aYq_guMOI28GIXkbvNw-HXZNelxWXKPFxDF_HGroIR-aNgx8jrU6XAMVQXM3hhC7Z-82sXQ8dlQBYdme16J4G5uD7HXzxCvBxJuVdpmH6sWbNMHSQT3bDzMLswklU.png)

### Issue: Broken Internal Links

[Broken internal links](https://www.semrush.com/blog/broken-link/) occur when a page on your website links to another page on your site that’s moved or no longer exists.

Use Site Audit to find broken internal links on your site.

Open the “**Issues**” tab and type “internal” in the search bar.

You’ll see a list of related “Errors,” “Warnings,” and “Notices.”

Click on the blue link in the issue description for a full list of affected pages. Replace each link to a broken page with a link to another relevant page.

![search for “internal” in Site Audit "Issues" tab](https://static.semrush.com/blog/uploads/media/15/fe/15fe7fffb6f98fa6d691e541e1116359/NffjmNUrIfAqJiHSsOqTdRUv_z5yJy31IsMUgbAloTyvikSKlFxJR3g1LP-dUJBjypGjeQrbN_Ye085h1Yk7kqJtYGZ0C_ICQj4dXo8moiIvkRXtT0wvjDVvGhKspIOKOBIk9nMzv8NH2wh6XOXG20I.png)

## Set Up Recurring Redirect Audits

Set up recurring redirect audits to find and fix redirect issues quickly and keep your site maintenance manageable.

Broken links and pages can harm your SEO. Redirecting is an easy way to prevent negative effects on your rankings.

Luckily, redirects are simple to implement or fix when you run audits regularly to catch broken links early.

To schedule automatic audits, click the gear icon in the top-right corner of the [Site Audit](https://www.semrush.com/siteaudit/) dashboard.

![“settings” icon highlighted in the top right of the Site Audit dashboard](https://static.semrush.com/blog/uploads/media/82/f5/82f562506201b466eb67c5eb602783a4/AemOj2LLuNxXwMmp2FUgt-tOECanDGwzHfNXthKcY5l6BLk-zgyWUH8sgqfowh2mpxlP3qXBRwhKHpc4xfr0Rc2JDepe9yFGZX0I4Qqf4mfFtug9f0yA_IddzFoxymKbE1dclnLRcb-yN04bgh56wa4.png)

Under “Site Audit settings,” scroll down and click “**Schedule: Weekly, Every Tuesday**.”

![Site Audit Settings](https://static.semrush.com/blog/uploads/media/64/ce/64cea5d729e390d033558df0ea48ce54/YxwLM7VjuwX07W-A8hCfCk36lfQ--ZL7sRtTCdSTITmHT64BhGIEG_lXU9Et8h3W6rKRnA8uSsYWD7Tb40DoWOIizLs27HtNqK5aLe8HsxHfThFqEbWsRxKUlOMteVg2EDoH1b9xC2WfPWMzA9LGTDc.png)

Select your preferred day of the week from the drop-down in the “Site Audit Settings” popup.

Check “Send an email every time an audit is complete.”

And hit “**Save**.”

![schedule how often should the tool audit your site in Site Audit Settings](https://static.semrush.com/blog/uploads/media/d7/31/d731a8ed5ec28f9698eab5f37663e1c5/STXQ15-Css-Hn2beZc8UHAERxXZpuFzdK8oGgZXWFBg0lq84Rg-CiVmLE2X_zbptuJFuL5ZwTU374ZWUMz2lzQKG-HrthEnNDd7KwBNfRGKt3ArGiIgS14Y8r28zJXYIDYDpXNyndhGGXW4xPMZFRvs.png)

Fix any redirect issues on your WordPress site as soon as they appear.

Redirect traffic—and page authority—to relevant pages that work. And give your site’s user experience and search rankings a boost.
