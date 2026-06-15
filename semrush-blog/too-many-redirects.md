---
title: "What Is the ‘Too Many Redirects’ Error? & How to Fix It"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "too-many-redirects"
url: "https://www.semrush.com/blog/too-many-redirects/"
canonical: "https://www.semrush.com/blog/too-many-redirects/"
author: "Zach Paruch, Christine Skopec"
published: "2021-08-13T15:59:00+00:00"
updated: "2025-07-10T09:50:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons: []
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T20:08:43+00:00"
status_code: 200
html_hash: "2bf8b911aeb73ba2f17e1dd48b5f53934e77729fe9160858c6917d2ccb933202"
clean_word_count: 3221
clean_char_count: 26095
---
# What Is the ‘Too Many Redirects’ Error? & How to Fix It

## What Is the ‘Too Many Redirects’ Error?

The “too many redirects” error means your website has incorrectly configured redirects that create an infinite loop and prevent the page from loading. Which hurts SEO and the user experience because search engines and users won’t be able to access the page.

For example, let’s say URL X [redirects](https://www.semrush.com/blog/redirects/) to URL Y. Then URL Y redirects back to URL X.

That creates a loop. And the browser keeps going back and forth between those two pages until it gives up.

![A redirect loop between two web pages—Page A redirects to Page B, and Page B redirects back to Page A—creating an endless cycle](https://static.semrush.com/blog/uploads/media/e3/43/e3434992c2eeda445ccfdd17d5f452e7/c47402a8669689e776d5d241d34ecc7f/AD_4nXeZiXNQRfzwEYcTuygSFhv_9yze3ftx9f2rsYoHYch8_3QX1aX0apxaxFwz-xZgwMd2NbH4WaeUWxgW8q0qgyw9LcpsNbTJquUzzmR4wL0WjB8tzwFt-sRbiegeqtXSrm747deI.png)

Most browsers will follow up to about 20 redirects. If they can’t reach a final page by then, they stop and show an error instead.

For example, Chrome says this site redirected too many times and suggests clearing cookies.

![A broken page on Chrome with the error message reading "This page isn't working" because the site redirected the user too many times.](https://static.semrush.com/blog/uploads/media/4b/7f/4b7f8e8a25c837aceb0395687bc0c48f/6a665af7428de06035eb4f1a41e662d4/AD_4nXf5sxP9pkXVkAi6rNGigKAQckEGkRS_TeKjDhoGulfe5YgXw9HR0fQJk5jMHJaD4cPcbQpRlVZXCr9NJgCQ_GL0ksY6UbToUc16ghDZqI-ip2WOBeccWKWM9t4TtXI15oz18gR8.jpeg)

## What Causes the ‘Too Many Redirects’ Error?

The “too many redirects” error is caused by the browser being stuck in a loop that keeps going in circles without reaching a final page.

[Dan Taylor](https://www.linkedin.com/in/danielrwtaylor/), Partner & Head of Technical SEO at SALT.agency, says the most common cause he sees is cookie or cache mismanagement.

> "From my experience, it’s usually down to cache or cookie issues—things like session affinity, session control, or incorrect cache control headers. Ten years ago, when HTTPS adoption was more the ‘hype,’ changes in the HTTP/HTTPS protocol caused conflicts, but that’s much less common now."

Here are some other common causes behind redirect loops:

- **Outdated server cache**: Your server might still be showing an old version of your site that includes broken redirect instructions
- **Content delivery network (CDN) cache issues**: Your CDN might be serving outdated versions of your site with incorrect redirect rules
- **Third-party tools or plugins**: If two tools (like a firewall and a plugin) are trying to handle redirects in different ways, they can create a conflict

## How to Check Your Website for ‘Too Many Redirects’ Errors

You can check for the ERR\_TOO\_MANY\_REDIRECTS error manually by visiting your site in different browsers.

Dan says his first step is to check redirect rules directly:

> “I’ll start by reviewing the .htaccess or server configuration files to make sure there are no conflicting or incorrect redirect rules in place."

He then checks that redirects between HTTP and HTTPS pages and www and non-www pages are set up properly and consistently.

You can crawl your site for redirect issues caused by misconfigured rules with Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool:

Open the tool and follow the prompts to configure your project.

Once the audit is done, go to the “**Issues**” tab and search “redirect.”

![Issues on Site Audit with "redirect" entered and the "1,632 redirect chains and loops" error highlighted.](https://static.semrush.com/blog/uploads/media/9d/10/9d10e6c59639cddc793c26f59d06e0e3/30460ee5a4f7e7847ffffff195314ec2/AD_4nXc1yMNiv5mySPSzJ1jQrG01v_E2RyDZI9cjgeWPNz88y4iEaDQuvWoUqrzY-ywx8rzTACFbvtHi66JPFJAYfDU2K1t5E-_JANmPe2_PM_IJ73cIJufux0IBU-Edn4z03LGo1Wgv1g.jpeg)

If your website has redirect loops (and/or chains), you’ll see the “**# redirect chains and loops**” error.

Click on it to see the list of affected URLs.

![A list of pages with redirect chains and loops errors along with the initial redirect URL, final destination URL, redirect type, and length.](https://static.semrush.com/blog/uploads/media/d6/a8/d6a8d4c0046a0699468a3320d7844131/5d45b8e9cf05853b76bc5a0485599aa6/AD_4nXck5gDRjHZ1zOG_DW8TfNM-oSPsqZvxRVoBM05hbdCOFa7un4BabiAdbvVX36C8o_zI6Ga6YuJ_X2kD43AvT7SUjng09_tPIBaV1xeMzzxUOLWV9SZrTlM8Yu-yFgPC4D3BezNp0w.jpeg)

Just know that this specifically uncovers loops resulting from incorrect redirect rules.

Other issues can get in the way as well. So let’s go over how to fix them.

## 8 Ways to Fix the ‘Too Many Redirects’ Error

### 1. Clear Browser Cache and Cookies

Clearing your cache and cookies removes outdated data that might be causing your browser to load an old redirect path.

Dan says he always includes this step when debugging redirect loops:

> “I’ll clear the cache and cookies in my browser to rule out any stored redirect data that might be causing the loop.”

This is a good place to start if you're seeing the error yourself, but others aren’t. Or if one user reports it, but no one else is affected.

Here are the steps to do this in different browsers:

#### Google Chrome

Click the three dots in the top right corner and select "**Settings**."

![The three dots icon clicked in the top right corner of the Chrome browser and "Settings" selected from the list.](https://static.semrush.com/blog/uploads/media/2b/e8/2be860f2b135e6f604e0be4486140e2f/d0d42718f3280489bbd58c810e8f17ed/AD_4nXdpeu8DF_yzFdO_6SSJcdGl6As2KP_nIYq7RHrI5O7S0Z0qwHny61mUFjv2KQjhMNtKOxq0bu5N0N6ned8giZBunInE8M3GzElOErct0dXbJ17Bchnvgw_iD0v6MU332zkt55dw.jpeg)

Navigate to "**Privacy and security**" and click "**Delete browsing data**."

!["Privacy and security" settings on Chrome with "Delete browsing data" clicked.](https://static.semrush.com/blog/uploads/media/cf/e4/cfe4614a12203ee52a463d107d4e03fb/ef69c40e1e3b4c3eae2558254f362f93/AD_4nXdSwiOJiekygoF2FRyq-9AgRlKuh5m6ppJlyAudgauJKWvXRbm-20jZk0p0wMHxCEOA4fG0BAOt8szcgLItu7zlMLPFMEgrAq0cMfbmjHDIDVDLo1QWqf7LQUEG2scz215s-Oac.jpeg)

Select both the checkboxes next to "Cookies and other site data" and "Cached images and files." You can uncheck the box next to “Browsing history.”

Set the time range to “**All time**.” And click “**Delete data**.”

![The "Delete browsing data" window on Chrome with "Delete data" clicked.](https://static.semrush.com/blog/uploads/media/1c/8b/1c8be740a7612bcc64155620a649bed4/5404bf7ea46193d337c3d51d493d330e/AD_4nXer3Cg2EdoEbuZ6NOX1xZ87ZBK-WwsQvYY9qrnaqeSWreoJo8OJc5lZp1BSM_wx1GZgXhnUUwtSvSYD3KYJcNmhpWvmUWP6SxGsbg6POnHUUQRkLXaP4lfwiz9ammG3WgM6azTw.jpeg)

#### Firefox

Click the menu button (three lines) in the top right and select "**Settings**."

![The three lines icon clicked in the top right corner of the Firefox browser and "Settings" selected from the list.](https://static.semrush.com/blog/uploads/media/f1/c4/f1c4bcafd3aad1032b8bb19f06a11d6d/a585600e668f874e1b0902d54068f28a/AD_4nXdnLfIOvTA_yaYxbYLXHP33AlKynqJzFdAuRc5zyOcAVoe6oorB707T0fjZX5hD7qYgNJ-3K8IHmBiY91JX7WnyLSD0HCCwOtxlo8fhlZqiARqkF94n99mlRhK3SDHUduZnpHoG.jpeg)

Go to "**Privacy & Security**," scroll to the "Cookies and Site Data" section, and click "**Clear Data…**"

!["Privacy and Security" settings on Firefox with "Clear Data..." under "Cookies and Site Data" clicked.](https://static.semrush.com/blog/uploads/media/99/3e/993e0ff79360fca94af70bc7490921d5/200f978877dc92005fa5916eec40bce8/AD_4nXf98H3tRhR1KepwbH1AkDQ-SFWGDm9DOTgSGgxHxQlORhQ55w5JwOfEPpX4XpVtA0fzW3SqFvtnUUXPnddD8MyVG1Jd1ocl7xdQnBBO80kGs_CBHJisQeVe41AOJ2YzVhkeFQEqtw.jpeg)

Select the checkboxes next to "Cookies and site data" and "Temporary cached files and pages**.**" You can leave other options unchecked.

Choose “**Everything**” as the timeframe. Then click "**Clear**."

!["Clear browsing data and cookies" window on Firefox with cookies & site data and temporary cached files & pages selected.](https://static.semrush.com/blog/uploads/media/bf/18/bf18cee1c896e15c37bbcfb53a71524d/465e413802cd8f231e9dae87e348fe80/AD_4nXch3kw70ihziSYFOXJeFH5DKI_fCJyO4UjUVXvCJ4lLuDdTmGiHUSSnKE1FhzxiC27doSdqxsDget100HzeheAaouTIZV9BcQu1tY7eK1ZCUwnHyw2P0W8GWLeOoODtBsJRZTvWpQ.jpeg)

#### Safari

Click the “**Safari**” tab in the top menu, then select “**Settings…**”

![The "Safari" button clicked in the top menu of the browser and "Settings" selected from the list.](https://static.semrush.com/blog/uploads/media/6e/c5/6ec513083f2198a36c9b213265a6d806/5f6d469ebc0b99a1b6aac08604b3af69/AD_4nXcGadmMaaUOIF1_GgYwPoNe3sjQpk7xEfTJoa7ViyOx-RgWBn6wjPcmQt-uWWEJpmSoS12meO7bxuxZoKbXZoOPb_q3gd-Fb-UD5tS9vXS5DoSuEkkC-M98bx9sW9AUuWs5lBDiHw.jpeg)

Go to the “**Advanced**” tab and enable “Show features for web developers.”

![The "Advanced" tab on Safari settings with the “Show features for web developers” box checked.](https://static.semrush.com/blog/uploads/media/3c/71/3c71c3085e9753e54eb8e9411c26ce87/524059e4ef942c8c2b8e1864f0d4a6e7/AD_4nXe04Q2oVeQ5JN9ZtkN8HVO5-ul0menIIkKoCZ5hjKR81mqPx1mGC03w2H2fjBz4TkRoNG0dd6MDl1-E9PIxMHyeSf7MVBf9h-1uHNZnF4jVwquO2f1JxvF9F9ls5MX2lMkirHxHiw.jpeg)

Click the new “**Develop**” tab that appears in the top menu and choose “**Empty Caches**.”

!["Develop" clicked in the top menu of Safari and "Empty Caches" selected from the dropdown list.](https://static.semrush.com/blog/uploads/media/e6/ea/e6ea22f06b9700054b34242278b99ed5/41430d481a1e8c6a9c3432fc57927030/AD_4nXeDHNnau3v9tH7l_5qFIMHlD5SiE7Fi0KuV0QCY4rzk8heRtXBbL_RfViCi6aowthyINFRqx5-H_Ea3mHJmBc0Cqj9gcNrjkPvd2hzFPAVUYTB-0VJJjqcj-gVJhL7126eMoyhT.jpeg)

To clear cookies, go to the settings again.

Go to the "**Privacy**" tab and click "**Manage Website Data…**"

!["Privacy" tab on Safari settings with "Manage Website Data..." clicked.](https://static.semrush.com/blog/uploads/media/b0/66/b0668c638c07bd60e7873a7807c2fc4b/8568a19b35ca803edeb4cb22573ab46b/AD_4nXee-Bvul7bc4s3A8w2JRCjrOczy2z0H5alvKLVL7zjOtCyzcFeTzv1Y_KBHl8r-jQjXatSd5xRDxy_iwnE4TIv1lAaVpT4aIKgu9JVBj0fZpKWcpaq_CE_EKWl6Oz-fVrSEp4Dg-g.jpeg)

Click "**Remove All**" and confirm by clicking "**Remove Now**" when prompted.

!["Manage Website Data" window on Safari with "Remove All" and then "Remove Now" clicked when prompted.](https://static.semrush.com/blog/uploads/media/02/c0/02c0dbc7e199573f6dd629733358122f/70a01a3e38589a38a7f535bce2c36bc6/AD_4nXcOlPJTgHl7O1CsPO8hNkKZ6tgxBPJCLBtHjJRt1bwUMLchTuwtg8PPKjnSwrn1TqwyfMcFr5cWEUu6g2J9OEAQ_ZoV75HHSC9IcSyNvX-2N4Ky4ToU3obp9metxekHCL-PoOlEmw.jpeg)

#### Microsoft Edge

Click the three dots in the corner and choose “**Settings**.”

![The three lines icon clicked in the top right corner of the Microsoft Edge browser and "Settings" selected from the list.](https://static.semrush.com/blog/uploads/media/29/29/292987406f1684e02c2438e84cd483d0/dc504ff53434082576ed466495216fcf/AD_4nXc--TjvBukBJpEPGxF6DFzWbQnO0MoMWsUW-wpyEmfxhpx6sz_L2s0YuHUoGolAyYOazA89AUyQA2LGzZC1F364wgxME34ylDenpuu5BIVlS6-txfbW0K7ibxMr0ikVmZRbhtKs.jpeg)

Go to “**Privacy, search, and services**” in the sidebar. Click “**Clear browsing data**.”

!["Privacy, search, and services" window on Edge with "Clear browsing data" clicked.](https://static.semrush.com/blog/uploads/media/ba/53/ba53b61c804e6c870abf9445dcda6ea7/57cf6fb459379763c927e9f8ca11a69d/AD_4nXePBHlZrVfVBLHRyaUWff06T-3YdoewfiwWqtqP3l3GJHT_yuWhK2ULgJWWUb9RX3RH81M7N-e-Ps3aAhEZpShPXW3Ytg2HmN9otFZ3fSODLQ-ygBCFqxFgy48S8GU9XHs1fM5dwQ.jpeg)

Select the checkboxes next to "Cookies and other site data" and "Cached images and files." You can leave other boxes unchecked.

Select “**All time**” as the time range. Click "**Clear now**."

!["Delete browsing data" window on Edge with "Clear now" clicked.](https://static.semrush.com/blog/uploads/media/15/53/1553ca053f552ec8b0660bad2b3487b9/79729415318f6e91e1220229fb2277db/AD_4nXfKKDrg7f_Em_IB_E3HkunEE8XcDB9ucx7TeUQBiNxvqILVI443-bbJLcrEOHYOxqg7YGm1OeSaT-XEUaw3uWzK35Q1hL-LrcfWeA8-YaI9HQDnV_tj3pPkXS7LC9XfvAmEbAse5g.jpeg)

### 2. Clear Your Website Cache from the CMS

Clearing your website cache removes outdated redirect instructions that your content management system (CMS) or plugins may still be serving.

If you're using WordPress, you may have a caching plugin like [WP Super Cache](https://wordpress.org/plugins/wp-super-cache/) installed.

To clear the cache using this plugin, go to your WordPress dashboard, click "**Settings**" in the left menu, and select "**WP Super Cache**" in the submenu.

!["WP Super Cache" clicked from the "Settings" submenu on WordPress.](https://static.semrush.com/blog/uploads/media/29/6f/296f9fab22f543fcf3997a8e92ae31f3/7a1ae15b1def5864f6083dc496d866c6/AD_4nXcrVy2ssrnhWmU955BoRrj0rrKEw6KboqjiDahXR6hFpNljL--KFtikK1Ruf4gpbga0uiNQAMzWItdu2jpI0hpXS0Pvth2NWknIMtS9l_8UyzJluUo_E-z379d2hXn1-4nq7MPo.jpeg)

Scroll down to find the "Delete Cached Pages" section and click the "**Delete Cache**" button.

![The "Delete Cache" button clicked in the "Delete Cached Pages" section on WordPress.](https://static.semrush.com/blog/uploads/media/8a/9e/8a9e951458a2c5e80df35e974525d614/fce35025f992f5f32e3d0aaccb83bcd2/AD_4nXfk4ChC_oUhOXJrK_YmNVHEo2e0vb_kS_vszeA9mVxupfCd5iEv12lKm4Nnv-bqOTtig0eyTVGRaokeb41G3UQdBWdVaut2lcIgjxpIwvun077Zs7oKkFWNAzuLHosv0FLHmhRm4A.jpeg)

If you're using a different CMS, follow the steps in the appropriate help documentation:

- [Drupal](https://www.drupal.org/docs/user_guide/en/prevent-cache-clear.html)
- [Joomla](https://docs.joomla.org/Cache)
- [OpenCart](https://forum.opencart.com/viewtopic.php?t=212414)

### 3. Clear Cached Files from Your Server

Clearing your server cache ensures your server isn’t using outdated files that have redirect errors.

Most hosting providers offer tools to clear the server cache through their control panels.

Let’s say you’re using Kinsta to host a WordPress website.

Go to your dashboard, click "**WordPress sites**," and select the checkbox next to your site.

Click the "**Actions**" button in the top right corner and choose "**Clear cache**."

![Kinsta dashboard with two WordPress sites selected, "Actions" clicked, and "Clear cache" selected from the list.](https://static.semrush.com/blog/uploads/media/0d/cd/0dcdb5bb52dc2aa1f2dba03a32633abe/ab7445404d77438b76a591b290cbb201/AD_4nXc5tGdXsafCPEbjV1FxoNqMtn67CmFC7XBsNL12tMGcBNg-TFhBMZppPqg8YP-c-3uafd0G5NTLkeRy6IfPaM_1m0JWpAZ6oYMSgS3hOeQNGIZwYr8peRz0_orTXSf_cOt59CAxgg.jpeg)

Select the checkbox next to “Clear server cache” and click “**Clear cache**.”

!["Clear cache" window on Kinsta with the box next to "Clear server cache" checked and "Clear cache" clicked.](https://static.semrush.com/blog/uploads/media/b4/c3/b4c386e34220adaddecc9d7c58d6f07a/f48eece1598454ab300aa3840f85f2d6/AD_4nXdyycL376-pj_qc5RdADm9mCwXAWp4hNpGy_-BG5Gw8hkTBvemU2IevTQWq49zfS0w_0iYniP5lMK5a2W974l3O6oiTfW_6BOSPPCJFp4PfcSBX5mmw3HaiKW1dD1mvHyT6E1KA.jpeg)

Other hosting providers also have built-in cache-related tools. If you’re having trouble, reach out to your provider’s support team for help.

### 4. Clear Old Redirects from Your CDN

A content delivery network (CDN) speeds up your site by saving copies of it in different places around the world. But if those copies have old redirect settings, they can keep causing the loop.

Let's say you use Cloudflare as your CDN.

Go to your Cloudflare dashboard, choose your account and your site, click "**Caching**" in the left menu, and select “**Configuration**.”

![Cloudfare dashboard with "Configuration" selected from the "Caching" submenu.](https://static.semrush.com/blog/uploads/media/71/af/71afd14a0eaff1667b9477554c77cb7a/dca96413ea522bbbf5cc3d68c26751a2/AD_4nXcWMAIdxoPAbl2-B7JpiCG-NuHH9_USkmxJebutaLwcKy4D50mh47KWdp6iaOBlHwNemvGEMIqstM1D6lOWP5-wnQY4SWct7xdX-Bn_bahJrtsJ6GtH_0w0WorrnMJzfD3wzYc7cA.jpeg)

Click "**Purge Everything**."

!["Configuration" settings on Cloudfare with "Purge Everything" clicked.](https://static.semrush.com/blog/uploads/media/dd/1c/dd1c646f8e4f9ef60292e2997a71f05d/e44a0c04327437410c3e3721c2566d73/AD_4nXcEXXfwofUythCwdVqPYQ2FKnBp5uuSzcxhTC7uASM8PZ6IH046FkCFsgR2-yE880MMVD51G4jv0KLr414wUnS_ose2YKRdEoKzNuLpKq6vWcAfpRk2WV8lecOBqzVbm3lRqM8WJQ.jpeg)

For other CDNs, follow the appropriate documentation:

- [Fastly](https://www.fastly.com/documentation/reference/api/purging/)
- [Akamai](https://techdocs.akamai.com/purge-cache/docs/welcome-purge)
- [Azure CDN](https://learn.microsoft.com/en-us/answers/questions/1460982/how-to-purge-cache-in-azure-cdn)

### 5. Check for HTTPS-Related Problems

Making sure you have a properly implemented SSL certificate (which verifies your site’s identity and enables you to use HTTPS) and that you aren’t trying to force HTTPS without one can fix redirect loops.

Use an SSL checker like [SSL Shopper](https://www.sslshopper.com/ssl-checker.html) to confirm your certificate is valid and installed correctly.

![A domain entered on SSL Checker showing details about the SSL certificate like who it was issued by, when it expires, the domain listed, etc.](https://static.semrush.com/blog/uploads/media/c1/36/c136d0912195c8aa04aa943d9630cdf8/21d35ef54e374899ecd6a53ae7046c08/AD_4nXfFoorgb6P_4B-vFaAsPXIjsDZ_NsRMZaSftOE1YjOiMGmp1FKzF489fPmkkBYWcHEQgswGDRW7vcCoJw4pDbN_-KFEaITbanGrb3uOATgt1ewjLS4z2nZK1DsMfUfHoqfSV8bSUQ.jpeg)

If there’s a problem, ask your hosting provider for help.

You can also find HTTPS issues using Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool.

Go to your “**Overview**” report, find the HTTPS section, and click “**View details**.”

![Site Audit Overview with "View details" under "HTTPS" clicked.](https://static.semrush.com/blog/uploads/media/fc/98/fc983b30ede89e5386e99425ea018015/b81d271b35a4acdeb6f6273446cddfb1/AD_4nXcmtugfYXuP91NErWTWxjvKuX30w5DCtpf_nqKfDw3dHXg2quA3cFB8yWMcn4AfSEJEB-CpPwUMA9vJGyz1FGBdVbSWmeTnd7PxOd-kHACz8jvDiO-l-URHUEuXedYmgk_j4o0S.jpeg)

***Further reading****:* [*How to Redirect HTTP to HTTPS (4 Methods)*](https://www.semrush.com/blog/redirect-http-to-https/)

### 6. Review and Fix Redirect Rules

Conflicting redirect rules can create loops that trigger ERR\_TOO\_MANY\_REDIRECTS error.

You can see these loops in your [Site Audit](https://www.semrush.com/siteaudit/) Issues report:

![A list of pages with redirect chains and loops errors along with the initial redirect URL, final destination URL, redirect type, and length.](https://static.semrush.com/blog/uploads/media/e3/6f/e36fe0898f4c46b67911a2871b8bf802/ff6dcc517638c612acd40c25d021165b/AD_4nXfgMrMuAEELYP7TtpEkDmbmOqx4du2pp1jpu2iTJZb8KWrilV_Og4Fl1Z5CK2--2k-A9zCd36-soMDKvRLy--x_t9bqg6h0u8k6A2dB3wZWxDmesOLOj1pWbO41CWcEIoMof9lpKQ.jpeg)

To fix the issue, update or remove the conflicting redirect rules using whatever tool or platform you used to set them up.

This could be a plugin, your CMS settings, or a server config file.

For example, if you're using WordPress with the [Redirection](https://wordpress.org/plugins/redirection/) plugin, you can view all active redirect rules in the plugin's dashboard.

Edit or delete any rule causing loops.

![The "Redirection" plugin dashboard on WordPress with options to edit, delete, or disable rules causing redirect loops.](https://static.semrush.com/blog/uploads/media/a8/d0/a8d0f09d5bada7526b0a00ce923979cd/4eb8a71ecafca77c7f3d6d1b70a5c567/AD_4nXfZyUNu0saby9yxuBAkMf74E_g-vKhMaXnB2oVsiiwzKVd76AIJq4i4GR0SdIaI2vcDFvM6bAjpjnXj5ws9eJmmPDH0IHZ2adHJ1hO0nkmBxez9N_WKzwCsbObv10rKobESvHz3Cg.jpeg)

If you’re on an Apache server, your redirect rules might live in a file called .htaccess.

You can reset this file to remove problematic rules.

But only do this if you're confident editing server files or have help from a developer.

To reset it, access your website files through your hosting provider’s File Manager or connect using FTP.

Let’s say you're using Bluehost. Go to your cPanel and click “**File Manager**.”

![The "Advanced" tab on the Bluehost dashboard with "File Manager" under "Files" selected.](https://static.semrush.com/blog/uploads/media/14/09/140954e6459e057872fc89d7c1836582/fb3814a2c380c5545cd0bd9d4e46c34a/AD_4nXeghjQQiEGqIshsNWr_9N8PVTzeXTQg3aoNwM1pykXP8whql05a5R82N0vA00oHfXfc3XdKSDnN10KLBSVAxw3NQgHhny-gu8hBUSflZF2yZupTk_uFT3hLRkO0Dn4FCxm3Ns9P.jpeg)

Navigate to your website's root directory (usually named "public\_html," "www," or "htdocs").

!["public_html" selected from the left-hand side menu of the "File Manager" on cPanel.](https://static.semrush.com/blog/uploads/media/48/c8/48c8585689a6af73f1814730c673e8c2/e37960a4a35f5c7d157b447fee909717/AD_4nXefgaP_y53eXs1I75bf7GVLHn4ZaUSVx0Sfi6t-j4VbvRGZLVc9Ac1VhCIqNzVCF74wJUvQLDpZuMiFjDabEJFpEWeSC84F07agpifx_PcmcfD-vm8C9NUG3ogVNGTK29q_GL5Pug.jpeg)

Find the .htaccess file

Before editing, download a copy to back it up. Right-click the file and choose “**Download**.”

![The ".htaccess" file on cPanel right-clicked and "Download" selected from the options that appear.](https://static.semrush.com/blog/uploads/media/0a/cf/0acf6aff36217056129c82601226a6d9/23327cf41425fc79e61b6bb6b9a61a79/AD_4nXe7ODoGXTeuiFO1cuq6TTSkDpnJCNie5eXz1w9mgSBz1_7lTGhVzbqUKdh080WwhWFyD_OtMWk9H-JQNf9Ypcjs5fT1DZf-aq2UxpMUV_bYTFqE-haZktjayhPE1i-UjddbrH2AAg.jpeg)

Then, right-click on the .htaccess file again and select "**Edit**."

![The ".htaccess" file on cPanel right-clicked and "Edit" selected from the options that appear.](https://static.semrush.com/blog/uploads/media/19/2e/192e8bd0b5ae4bc3785f6ad41e552100/64384bbce3f0f0a2da027f2314713920/AD_4nXfYqbplNO9YF8cqBwQu8wVCDZfsg01MTVttxuaCaHwNUYBCruY6h1pFBnwOy0BjGqUYQgBArs0vBrOBmY4zp3C2HikE0r1jVKT35xSAnghX2--AAnj3la7wStOoCQJK2idwfKIN.jpeg)

Replace the entire content with this [default WordPress .htaccess configuration](https://wordpress.org/documentation/article/htaccess/):

`# BEGIN WordPress
RewriteEngine On
RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]
RewriteBase /
RewriteRule ^index\.php$ - [L]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.php [L]

Save your changes and check if the redirect error is resolved.

If your site uses Nginx or another server type, contact your hosting provider or developer for help.

### 7. Check URL Settings in Your CMS

Redirect loops can happen when your CMS uses two slightly different versions of your site’s URL.

If you use WordPress, go to “**Settings**” > “**General**.”

Look at the "WordPress Address (URL)" and "Site Address (URL)" fields. These should match.

!["WordPress Address (URL)" and "Site Address (URL)" fields highlighted on WordPress settings.](https://static.semrush.com/blog/uploads/media/32/1c/321cbd03d8b262242b823cffef088387/148c949d86e6870caf83f27210b64ea6/AD_4nXc0IcWNCyE82q6-2y8e9jlLin1p4Bx2mNSHblRJhoE2a6CR6cQgBGaN5uf7KuZMCQD9DmABCVnIe3QXO-4IOdhrhEHFC9qHOJdpjIAY4gMDDIJFVuBBtjud1xidYB-Jx_qd99_wHw.jpeg)

For example:

- If one uses http:// and the other uses https://, it can create a loop
- If one includes “www” and the other doesn’t, that mismatch can also trigger the error

Update both fields to match.

If you're using a different platform, check their help documentation for how to update your site's main URL.

After updating these settings, save your changes.

### 8. Disable or Adjust Plugins and Extensions

If you're using a CMS, one of your installed plugins or extensions might be creating the conflict.

Deactivate them to find which one might be the culprit.

In WordPress, go to “**Plugins**” > “**Installed Plugins**” and select the checkbox next to each plugin.

!["Installed Plugins" on WordPress with the boxes next to all plugins checked.](https://static.semrush.com/blog/uploads/media/2e/63/2e63118b1500f780fb6a68df72a9af86/8293fdf1604b1eafc0e7e330f79d7964/AD_4nXda26FPltCU39AVnnrSMA4hZ5MQymOG_opqlXMmgcjzC0gg_n-Ofb6H9Vy5EA_BUwDXuCc0IwMSVh3lg9bw-lLp9AjC2K1UOmBs6-0ouU2taqKUSQc1bT9Vl81N4TZzMcIG6sat.jpeg)

Select the “**Bulk Actions**” drop-down, choose "**Deactivate**," and click “**Apply**.” This will turn off all plugins.

![Plugins on WordPress with "Bulk Actions" clicked, "Deactivate" selected from the dropdown, and "Apply" clicked.](https://static.semrush.com/blog/uploads/media/35/f1/35f192445e7604883e3e271efd2175d0/7b1d7ca9e199de94b04b63276c4bf9f1/AD_4nXdmzo3YL5EpbMp7ZhzKz--Oki98f3gXP2XGvLWuUpE8F5YE7URTTc8J8CktcKi2G9J0ZMxLEvVbFiI01eNaLcNIDEvxFN_zNxQUGwsmMDgr417KIZV53JaCsgHlSwgepstKQkKGzQ.jpeg)

If the error disappears, one of the plugins was responsible.

Reactivate your plugins one at a time. And check your site after each one to find the one creating the loop.

You can use a similar process if you use another CMS or website platform.

Once you find the plugin causing the issue, consider switching to an alternative. And let the plugin’s developers know so they can investigate.

## How to Prevent ‘Too Many Redirects’ Errors in the Future

You can prevent most redirect loops by testing changes carefully before pushing them live.

Dan recommends doing proper QA and analysis whenever you make deployments that affect URLs, redirects, cookies, or asset delivery.

Which means reviewing how URLs, redirects, cookies, and asset delivery are handled after changes to catch any unexpected behavior before it causes loops.

How?

- **Check common redirect paths manually.** After making updates to your site, visit key pages to check that redirects go to the correct destinations without bouncing between versions. And try multiple browsers and devices.
- **Check plugins or custom scripts.** Make sure these options aren’t causing redirect problems. Some tools set their own rules, which can accidentally create conflicts and lead to loops.

- **Audit redirects after major site changes.** Things like redesigns, migrations, or domain updates can unintentionally create redirect loops. So, run a full site audit after any major updates using Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool to find redirect loops.

You should also do a full technical audit of your site regularly to catch issues before they hurt your [SEO rankings](https://www.semrush.com/blog/seo-ranking/) or [organic traffic](https://www.semrush.com/blog/organic-traffic/).

Run your first audit now.
