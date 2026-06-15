---
title: "Complete .htaccess File Tutorial: What It Is & How to Use It"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "htaccess-file"
url: "https://www.semrush.com/blog/htaccess-file/"
canonical: "https://www.semrush.com/blog/htaccess-file/"
author: "Dana Nicole, Chris Hanna, Sara Borghi"
published: "2021-10-06T19:45:00+00:00"
updated: "2024-04-26T10:25:00+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "date_2024_watch"
schema_genre: "General SEO"
fetched_at: "2026-06-12T16:54:42+00:00"
status_code: 200
html_hash: "726336fb77745d7cf5715f60560ba3527cfabfec4400a126e5fda74174cecc80"
clean_word_count: 3744
clean_char_count: 28747
---
# Complete .htaccess File Tutorial: What It Is & How to Use It

## What Is an .htaccess File?

An .htaccess file is a website file used to configure certain aspects of your site. Like redirects, customized error pages, and more. All without having to edit the main server configuration files.

It’s used on servers that run Apache, an open-source web server software. If your website runs on Nginx instead, you won’t have an .htaccess file.

Here’s an example of what an .htaccess file might look like for a WordPress website:

![.htaccess file of a WordPress website showing various lines of code including rewrite rules and conditions.](https://static.semrush.com/blog/uploads/media/ad/bb/adbbdee4064e0517adff4752f3192de6/d4cbf09e096b009ec58005b938d77f24/fm673LgVdSqk4OL9S8i98WIKGVG6DNVheLuUaAZtnKiGNq6WWfvfAUDktEJiZ-bXLKBAmILI_vfUGFSyt70f6Hil8liBjaBJzL_SGM5eSrRpnZ_vDDuaLhjNr7HlchC5hUEa_Z84awV9.png)

## Where Is the .htaccess File?

Your .htaccess file is usually located in the root directory of your website whether you’re using a [content management system](https://www.semrush.com/blog/best-cms-for-seo/) like WordPress or you created the site from scratch.

One way to access your site’s root directory is through your web host, typically through a file manager interface. Which is a directory within your web host where you can access and edit your site’s files—like your .htaccess file.

Your web host’s server files might look similar to the file folders you have on your computer:

![Website hosting account file manager.](https://static.semrush.com/blog/uploads/media/ae/d8/aed8a30059d20b7cf63c0c3ad9593af2/0457fc09fbb8cfb6d25eb24a653530bc/DSYb8gjd0eFTNltRCeA5JeVYgJz96o-RsCUaDJR806eFKpJ58JfEmeHkuMwzX7IKBxpBMyjtskhPohoElk9nbB_ZORJjblB2JrHT_7XX2OPq2Qg2zrcnA11t3teXc1JxqmO-Ymue083G.png)

But the exact location of an .htaccess file depends on its purpose.

For example, say you have an .htaccess file in the “image” directory of your website. The directives within that .htaccess file would **only affect files in that directory**.

But if your .htaccess file is in the root directory of your website—the folder that contains your main website files—the file’s directives would apply to all the files (and pages) on your site.

![Website host file manager showing the .htaccess file is inside the public_html folder, or root directory.](https://static.semrush.com/blog/uploads/media/b1/17/b117ae1fdd41483a09d76463d69c3a92/595acc3df20ee92e9c14abdf963f4ca1/oVu0J6GiX3ce9X-d0LHjLLLHShTZNXhN21sTD3LDKQvCrBcxnF8TS0GEOLWg8BFSgOtnUP1GT6CtztqjUqUxsatwLeDNt4kDq5kTYKy9z23dLlGnr3nBXeF5xGx_VfyVFgqogvaYoA98.png)

## How to Edit Your .htaccess File

If you’re using WordPress, an .htaccess file should already have been generated when you installed WordPress (we’ll go over what to do if this isn’t the case in the next section.)

And there are three main ways to edit it:

### 1. File Manager

Many web hosts offer the ability to access key website files through a file manager.

To do this, log in to your host, head to your file manager, and locate your .htaccess file.

Your .htaccess file is likely located in your root folder. The root folder is titled “**public\_html**” in our example below:

![Website hosting file manager showing .htaccess file under the public_html root directory.](https://static.semrush.com/blog/uploads/media/fc/36/fc3659a6f7bdaea7e7fdaad7eff5818d/91da4ea70092af0d5613d3c9e831c0c6/cznYW2GylIKH_QSHURNn0RCMfi8ls4U3A9BPZkg3yS_aJ2FQRMWupRC5RWm9aG4Mms_Jnb_ueAy3V-uCyVsFlKgO-HYGHu_qVZgXWsxC3dD-1ioO2-Kpa0r68CM0700C9tSFU6fYHEc2.png)

Double click “**.htaccess**” to open the plain text editor.

Then, make any changes—like adding or removing directives—and hit the save button.

![.htaccess file editor within a web host's file manager.](https://static.semrush.com/blog/uploads/media/a8/c6/a8c69e236f916e10a6aa2de9e56e718a/b602f3300de20c56fc326c6058647c57/43FSUixUDqUC1IqfioNnZHG8DJDtk1mcGynTaVmxXfS3gd_g-ecsXfHvQpBqTdrdcxlTLYm2eAMtYUWvERtBSQFfLYqBLn1oNbUrLn99fVQEhQYZQIVco1iScyNgWWpgli07mTXarY9k.png)

### 2. FTP Client

A file transfer protocol (FTP) client is an application that lets you transfer files between your computer and your website. [Cyberduck](https://cyberduck.io/) is an example of an FTP client.

You need to set up an FTP client if you don’t have one. Which may entail reaching out to your host for the details you need to connect to it.

Once you’re set up with an FTP client, you can log in to your site via FTP. We’ll use Cyberduck for our example.

Click “**Open Connection**” and enter your login details. Your web host usually provides these.

![Cyberduck FTP client interface showing ability to open a connection to a website's files and an area to input login credentials.](https://static.semrush.com/blog/uploads/media/24/c2/24c2936e7a463da094e7f546fc2884b9/7024fd0748b0b2f036b3c7844dd477ef/bxjmng4bG849vKOB--81l1QzXaNp22BBV_IfyaDkn2SZb6LcOfzDQYtQxSj0T6K1TvaunZTdcI6sfVkxSpgEZDiBWyJy5Q7xEkcGvjpZ7LTXJWO7biYwzZKd9jZ_YRn3wbjrrGJLvQFk.png)

Next, enable hidden files. Any files that begin with a dot (like the .htaccess file) are hidden by default. Meaning you can’t view—or edit—them.

To show hidden files in Cyberduck, go to “**Edit**” > “**Preferences**” > “**Browser**” and check the box next to “Show hidden files.”

![Cyberduck FTP client browser with the option to show hidden files.](https://static.semrush.com/blog/uploads/media/08/61/08612cc088ae5ce5e99c9e188003d1a4/ee808f97d568218ef6970957f811c3bf/rUPyWYNDKCyvX_8NmFIunVDXlmBIl6Q3Up4E7Us2pBhoqaksVZaWoFbxjYcnhNJOl9aVJHMMi33JZ6yj9yTSyRR7Xk02bsVNttYp_nDdGwX_20UbKsnBM_W8YjkZF1gAkfq8pAfnaXif.png)

Exit out of the preferences. Then, locate your .htaccess file. Again, it’s likely in your root folder.

Select the file and click “**Edit**.”

![Cyberduck FTP client interface with access to a website's public_html files.](https://static.semrush.com/blog/uploads/media/01/20/0120bde872a8616494ce924b13a26bef/1b18b0b93459f4b7a95688e65d23c54a/XDQb4MbodiHfOWoAS-iEubHCrkjMA4FyvT03ExBsU7EVEskCShAoO4U5ZWboA1OKVm8PbZwTZe319BTiF8_cnMnWZAqx48zBIRP8avOizwzHjVjcBgMeskIexB_KCsdeV6ceg6-MUMle.png)

This opens your .htaccess file on your computer as a plain text file.

Make any edits directly in the file and hit save. Your saved changes are automatically added to your .htaccess file.

### 3. WordPress Plugin

Plugins like [Yoast](https://yoast.com/wordpress/plugins/seo/) make it easy to edit your .htaccess file from your site’s backend.

Log in to WordPress to download and activate the Yoast plugin.

Then click “**Yoast****SEO**” and select “**Tools**.”

![Yoast SEO WordPress plugin sidebar menu.](https://static.semrush.com/blog/uploads/media/8c/88/8c8852d673ca7139d4e19f6f581627f8/93e89810f15602a740f6c76b1f626bbb/zIg6aMSmLoWiMLSB5ohqBjIHuuIZnHLGClItPHFMxzqiohROT9BQquIfYraaWf_D6HhC_daZPUVBc3osl2u5HnJevDCCjh3Ow0INDi04yEi2wzyeToP9jFcdcuoGCX9Pm5Fzwdy8XA4Y.png)

Click “**File editor**.”

![Yoast SEO WordPress plugin option to edit files.](https://static.semrush.com/blog/uploads/media/fd/1f/fd1f5fe57978b340f7449c9ed378799a/81a18f1a89acdef463030e2a0fbcd756/cMypZNbDgnfY8a3TVR-ISYmHczZI3qD5qH7WlCQnCEFeWWwykCTXf34CkTkfb6jq8umSjS41hgof012wgnnSiHSBimQv34GgIGuMRtK8lFxYfe_S3_z0K1h9f_faejVbj2dai1uXPI7a.png)

Scroll to the .htaccess file area and make your edits directly in the text box. And save them by clicking “**Save changes to .htaccess**.”

![Yoast SEO WordPress plugin .htaccess file editor screen.](https://static.semrush.com/blog/uploads/media/80/65/806551a8769592a9f74f8fedb52a02d8/1a2ec412fa2b306741df679cac3dbb21/1bcH5JvLr7Pxk9CnSCT3zr-nmytOWxVonWZ_-3byp90EFXWyu5pwhlMYjcq-qp4mTWsevCKuzwBB27eM3CL5Nwgqt6fpu2gtTi1IcXA4F0OjhrR1tBGaTS_E_XbVOxkshq0vZYEY8eL6.png)

## How to Create an .htaccess File

If you don’t already have an .htaccess file, follow the instructions below to create one yourself.

### File Manager

To create an .htaccess file in your host’s file manager, select the folder you’d like your .htaccess file to be in. And keep in mind that the .htaccess file can affect the directory you put it in **and its subdirectories**.

![Web host file manager screen showing selection of public_html files.](https://static.semrush.com/blog/uploads/media/d2/dd/d2dd90a32b4379a67200a2f44ab00adc/3e3fe1622b990447f967c506f0da703a/eFzfYLXbdZuZMn_EUWhTyNed4oP15TqJapI7-wYLVc9PUVOu6LDPq_uCV7IUwfCQiSLxFC8dpWp8zm7nYgb6C-XxEcGDvXoEuMiLYhlgaBDyv-wgKV2FhV-00PWt_C1M6fVXyGQIGZ8d.png)

Then click the new file button.

![Web host's file manager showing the option to create a new file within the root directory.](https://static.semrush.com/blog/uploads/media/7d/01/7d01e71a57404d4f40f18383dc9cda11/166f48d90979174b290c644824ec8561/8drOMO9Iocw_XhypPj7akITR4_54KxEeQjNFAoa4Os3PyQQVaU78p2NXjbgN6_CMEMZ-BQwh8Tat76NPDU-QAmj6UgfJyEDiQ8gjVLyutE4uSCI55HKhvQDB70-_j0qgXky-E2pwzKwS.png)

Next name your file “.htaccess” (with the dot). Click “**Confirm**.”

![Web host interface for creating a new file with the name ".htaccess."](https://static.semrush.com/blog/uploads/media/46/a6/46a60268783e4493c848eec7e252b823/717ed544f27751aaf4da25da404c45d2/KIZPFJ9k8_zpobpOzyeEWXhfHyACIUXBj6RkZhXEUOSlQMG7HMn768NJfdHzRqqOOpxOnDKFVJLELNXWlt4QU7AiLQRu2L4kH61pTZJIUctCyNoGjnqV-YpBn00YOrPcHZzin4Otp_1R.png)

You now have an .htaccess file ready to edit.

![Web host file manager showing a blank .htaccess file created from scratch.](https://static.semrush.com/blog/uploads/media/89/57/8957f5a902cecbe9b20a6a654588cc07/976c1661c29d28bed0de1aeb4929c061/-oA3hC5UHU9xuFEYvTUHPOdaTFyomyxx4nhPlj3Ck8q_Hznqs6MhuiCnJye7US9iKqFSTkntoVSp8VQAduoOkuRZbzwQQB3Rv8sOQia6n5xHJQuZXnmeCavUFJ2IMdGapkRHT0rvlXNL.png)

### FTP Client

To create an .htaccess file using your FTP client, save a plain text file on your computer as “.htaccess” (with the dot). You can create a plain text file using apps like the Notepad.

Then, within your chosen FTP client (we’re using Cyberduck), select the directory you want to place the .htaccess file in (like “public\_html”). And click “**Upload**” and select the .htaccess file saved to your computer.

![Cyberduck FTP client interface showing option to upload a new file.](https://static.semrush.com/blog/uploads/media/cc/d8/ccd85ccdcbb26d1f4be78ae8167921ed/a477cb02def14645823d2aa90d2d1247/-dEYTULHxBOT3R4RlG5rbYKmBrvkI8cSu1UTXr-KJHILm6UVvMYFDmPA_JKbXoWYwlhfasg0VC2GqixCCSCnBqmpZLHDC2Fz_4IVWvn9fAKZ9m9RjPxN5_4kqEEZF6P1uZ1SEzNswevU.png)

Your .htaccess file is now ready to use.

## 4 Common .htaccess Directives

These four .htaccess directives can help you improve and customize your site.

### 1. Add Redirects Using .htaccess

You can [redirect URLs](https://www.semrush.com/blog/redirects/) using .htaccess in several ways depending on what you want to redirect.

Before adding some types of redirects, you may need to load the RewriteEngine module by adding this directive to your .htaccess file:

`<IfModule mod_rewrite.c>
RewriteEngine On
</IfModule>`

Then, add your redirect directives under this module.

We’ll include the “RewriteEngine On” code where required in each example below for clarity. But depending on how your .htaccess file is set up, you may not need to include it each time.

#### Redirect Individual URLs

Redirect individual URLs with this directive:

`Redirect 301 /old-page/ https://www.yourdomain.com/new-page/`

The “old-page” should mention the URL path—the portion that comes after your domain. This should begin with a slash.

And the second part should be the new page’s **full** URL.

Users will be automatically redirected to the new page whenever they try to access the URL from the old page.

#### Redirect WWW URLs to Non-WWW URLs

If your domain uses the www subdomain, you can use your .htaccess file to redirect it to the non-www version with this directive:

`RewriteEngine On
RewriteCond %{HTTP_HOST} ^www.yourdomain.com [NC]
RewriteRule (.*) https://yourdomain.com/$1 [L,R=301]`

#### Redirect Subfolders to New Locations

A subfolder is a folder that exists within another folder on your site. For example, in “www.yourdomain.com/blog,” the “blog” part is a subfolder.

And you can redirect subfolders to different locations on your domain using the .htaccess file with this directive (using your URL paths):

`RewriteEngine On
RewriteRule ^/?blog/(.\*)$ /news/$1 [R,L]`

In the above example, any URL in the “blog” subfolder will be redirected to the “news” subfolder.

#### Redirect an Old Domain to a New Domain

You can also use the .htaccess file to redirect users from an old domain to a new one with this directive:

`RewriteEngine On
RewriteCond %{HTTP_HOST} ^(?:www\.)?oldsite\.com$ [NC]
RewriteRule ^(.*)$ https://newsite.com%{REQUEST_URI} [L,R=301]`

This redirects both the www and the non-www versions of your domain to the new one.

#### Other Ways to Redirect URLs

There are other ways to redirect URLs if you don’t want to edit your .htaccess file.

First, run an audit of your site to see which pages may need redirects.

The Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool can identify those pages for you.

Within the Site Audit tool, enter your URL and click “**Start Audit**.”

![Site Audit interface to add a domain name, with yourdomain.com entered.](https://static.semrush.com/blog/uploads/media/84/e7/84e7daf6ddd76fd17ccf1387859e55c1/fe3a7b6291be733dd57995c2705f38a9/q5IAa8Tx3FqqOJu8bTin0UcVM9Ea1vT-mltrlmT_i60HUqr41VppcRd2WnltQUheX2na2BiTkPO1CuEqEV5-L4Bkb3NEAIHuLw5wyYIQz1Vc1B_bYMEQBTEMvjroByLf3zDd42OqiqBy.png)

Configure your audit settings on the following page. Like how many pages you’d like to check during the audit. And how frequently you want to run the audit.

Click “**Start Site Audit**” after configuring your audit settings.

![Site Audit settings configuration screen.](https://static.semrush.com/blog/uploads/media/7d/4b/7d4b724ba742762c5e13c361838983ac/5defed58176975258e60ac8ddd2f00f2/pus_v7bQKrtOD58BFkWZ29s6Ope5-jbhbVKSNPzwXFmvzsK7kND7i3PEjE0VJ2WTrfbNUJoQEc6heXrF1rlRDlPMwxkJjZXnk7xgb16vX3mOLOBOesHxo55fbyjq_loG0Q750K_RJqTS.png)

When the audit is done, click “**Issues**” and look for “# pages returned 4XX status code.” Which means the server couldn’t reach those pages due to a client-side error.

Click the “**# pages**” to view each affected page.

![Site Audit results showing 2 pages with a 4xx status code error.](https://static.semrush.com/blog/uploads/media/74/f8/74f8a3808bcb6fc2947a6d5c323f8d76/cd4c8c82f0959dece16579f9a8f2e331/9SfYHQm12UwOxYSMYk0JwwXCTr2XHVXAIGyw9RfSy_14eZ6M5VQ99Zt8c-iiZwW-Nj4s-FL7Act0g29qDmcWTricXbmclVNsJdyG3itHaclLLF7ggFY7O1GEhE0RWO02IOcrLF-X93Lu.png)

Review which pages you need to redirect. And which ones (if any) you’d prefer to keep as 404 errors.

You might indeed want a page to display a 404 error if you’ve deleted the page and there isn’t any relevant page to redirect users to.

To implement redirects for these pages on WordPress without editing your .htaccess file, you can use a plugin like [Yoast](https://yoast.com/wordpress/plugins/seo/).

Click “**Yoast SEO**” and “**Redirects**” in the left-hand toolbar after installing and activating the plugin.

![Yoast SEO WordPress plugin side menu showing redirects option.](https://static.semrush.com/blog/uploads/media/40/79/4079f495749bc6cd305370b2aa2e8e8a/a0b880010aa36b60b20464788d5136b8/3XpGi4WrNLf8UjeSwhhdDdrzT9071UTlZvOSKq0WvCz6qcnUiOTqL10mNIRAAJ-I09xTIyPQIcFp-PP43LnBwnHtTxG8O4cx9jjf1CkzXPfzRyAi3gwWC36UN0NcGxxwo6np6GiIMY_H.png)

Select the type of redirect you want. We'll use 301 because we want to permanently redirect the old page to a new one.

![Yoast SEO WordPress plugin redirect type selection screen showing option for 301 Moved Permanently.](https://static.semrush.com/blog/uploads/media/e3/ea/e3ea02e2da2d3371f7153ebb21fe79e8/79020e220bf9bb62ef8ebc4d972e1762/iv03TBQLlTJNFA3DHlMzBh51vRqxxoIeOve59gNvD2yuG4SgkASXK5csF3-mNFigp_J9gCRkZsv5EqpUMk3FocetZ7Uu6NuO64SXL6W-m2XcrV7BNYtYyQYO_tRX6PM2GbuSA9eIYp2n.png)

Enter the old [URL slug](https://www.semrush.com/blog/what-is-a-url-slug/)—the last part of the URL—and the destination URL slug. And click “**Add Redirect**.”

![Yoast SEO WordPress plugin showing old URL redirecting to new URL.](https://static.semrush.com/blog/uploads/media/22/88/2288b2e9ab7ba8d21af286550a1628c3/6c2f8a5cb26f5478e0d415611870a4ef/hSUSd57O6ruNYn5ZIv4Evm1FvWtpDwErGALXNG7roJcOhM3qNDXweZfdrAaCGnW54euMCPGEgy0IP1o-Pd7Sjpp64bUokpw_8mVrckxBdz_RxiGS-8CnMGKz2WZJ--WFkTWDm-Rv7IjB.png)

Lastly, test the URL by entering the old URL into your address bar to make sure it redirects to the new page. You may want to clear your cache first.

### 2. Load Custom 404 Error Pages with .htaccess

Your .htaccess file also lets you load custom [404 error pages](https://www.semrush.com/blog/what-does-error-404-not-found-mean/)—the page that shows when the server cannot find a webpage at that URL. This can happen when the page no longer exists or if someone enters an incorrect URL.

You might want a 404 page that reflects your brand, and perhaps gives users directions to relevant content or pages.

For example, our 404 page looks like this:

![Semrush 404 page.](https://static.semrush.com/blog/uploads/media/a0/15/a015d09ce68c486751dc1e690a572281/7e649fb7291b633f0a6c278ecf4e1acf/4WISZ7rBlyUs924rD4GC0Wj-88ntkZRt2MA6gB6zFpsRZK0QqOpXZtxHxPEkPwBpFbqmI5ZjW6qn4lW_PVSTm_h_xb4ZQXP0pDH4g2qrU9rGHqBvyESFVkw92xbCY6fkzbUFsS7PVbU9.png)

First, create the page you’d like to load when someone encounters a 404 error.

Then, add this code to your .htaccess file:

`ErrorDocument 404 /404-page.html`

And update the path to reflect your custom 404 page’s path.

Your custom 404 page should then load any time someone visits a page on your site that doesn’t exist.

#### Other Ways to Create a Custom 404 Page

If you’re using WordPress, a plugin like the [Smart Custom 404 error page](https://wordpress.org/plugins/404page/) can help you create a 404 page fairly easily.

Here’s how:

Install and activate the plugin when logged into your WordPress site. Then head to “**Pages**” and “**Add****New Page**.”

![WordPress side menu showing option to Add New Page.](https://static.semrush.com/blog/uploads/media/7b/33/7b33035d7c0dfc148222a7bcc5589843/b5945d41691159484336ec6233b1ffaa/E65hzArjsu30dCe_VJVQK724CDYAGygHujWcz-KFIFjPJL-BddbERhj7uIKmvxL-18XpSissbuEcq1vU44sVvjQ5trgrWiUE95iR1k-SW6HQE_Pd4QkIqqQIs_NafPWkJOTcVSZG3y9G.png)

Create and publish your custom 404 error page within the editor.

![WordPress page editor showing example of a custom 404 page.](https://static.semrush.com/blog/uploads/media/2a/08/2a08b5863004cf583920814e80b57a48/7480cfe62aecf64d455b8e457b29ac22/qz3Px0ZZyXT_9TuYpopvz0-kQmJsKMv9QoZnbKfrzI6L7TxyVmSt-IbFWQTrnJrqn227VWOw-Dk0a8cOCh92fSCeszze_WenkyxEDhw5pCYqEnpciAG7KW2VTfEg8QRT-JmDNLrm4nKT.png)

After publishing your page, click “**Appearance**” and “**404 Error Page**” in the menu bar.

![WordPress side menu showing option to change 404 Error Page.](https://static.semrush.com/blog/uploads/media/52/b8/52b834274381ac60627736125a318c8d/39c1a2cd1f67d082ce4c826bb40e681e/J5xJ0Fmllp_HSuoDc3zA6saE-4VnIyna45GbA5IaTvOBOhhA4yW0xdYa4yXMbUH1rvbdTGbRLCpBJ1snjUfXkvadTYpfyy2gBaKY2UyEzMaP3s0ymtV-KaA9fcUI5s194sj6lC4mVWMv.png)

Select your error page from the drop-down menu and click “**Save Changes**.”

![Yoast SEO WordPress plugin interface for adding a custom 404 page.](https://static.semrush.com/blog/uploads/media/b5/23/b52363a9d26bd5195d07259e6993cd0a/1e954b4b3f3359f56865fb68aeda49cc/xzjp4W67Ld6IbI6bCtE--0qfTs9UcdEk7H_VWIvA5lfhsOKskobwK73KWp-2gNhK6U3xYvh2LKCfjljmYoDoVmfCPwUpMhaKpZRBzYYlGkxeTW6SIITi3UclldJM-4GyOqtA5kOie29G.png)

Test your 404 page by visiting a URL that doesn’t exist on your site. It should redirect to your new 404 page.

### 3. Force Your Site to Load with HTTPS Through .htaccess

Hypertext transfer protocol secure ([HTTPS](https://www.semrush.com/blog/what-is-https/)) encrypts communications between the browser and your website. Which secures data sent from the browser to the server.

Plus, HTTPS is a ranking signal. So, using it could have a positive impact on your rankings.

If your site has a secure sockets layer (SSL) certificate, you can force HTTPS instead of HTTP using your .htaccess file.

To do so, add these lines of code to your .htaccess file:

`RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]`

#### Other Ways to Use HTTPS Instead of HTTP

Your host can often help you switch to HTTPS.

Some even provide one-click options to force HTTPS:

![HTTPS Enforce screen within a web hosting dashboard.](https://static.semrush.com/blog/uploads/media/ee/76/ee769d3e687eb6dc6c90ec5d6f592ff8/94b00d2d6f32671bb90ae3be29ae9c41/SdL45LI8U2hNOfgI9g_J2QzaFlNBnpLhN5ajxOVdA8psl9_-4XZgVTK86vz7F_F21tX3tDm6ygGZx0_vOn-U-9cdgXkJgoZ1_hxno5CznmHAgfdMgvZ6q29f9nZvHvXP_EdkVqrJBp2U.png)

So, reach out to your host for help setting up HTTPS if you don’t want to edit your .htaccess file.

### 4. Enable Password Protection with Your .htaccess File

You can enable password protection on your site—or specific areas of your site—using your .htaccess file.

This may be useful if you’re making site updates and only want certain people to access your site. Like your web designer.

You’ll need two files to password-protect your site: **.htpasswd and .htaccess**.

First, head to your website host’s file manager.

Add a new file outside your root directory. Name it “.htpasswd” and click “**Confirm**.”

**Important**: It’s best to place your .htpasswd file outside of your root directory as this may be more secure.

![Web host interface showing ability to add a new file with the name ".htpasswd."](https://static.semrush.com/blog/uploads/media/5a/80/5a807ab4fb7c81e393383112d492e818/736f15398d65a693fb5c3252a865951a/2hTgYz3CCE_tjwjHWzgTTr2P9uK632Ksd_FVNTSCXIk6fo4WsVFVHkV4wG9V-Z1pJUxkQ_S4PaGnomI1uTYa9ofZw0kf15Fj4sqfCMKRGlA9l2kJxbRiQCCHCyhACxWqP_tVZQUo2uJb.png)

Double click your .htpasswd file to open and edit it. This is where you’ll add a username and password needed to access your site.

![Web host file manager screen showing .htpasswd file outside the root directory.](https://static.semrush.com/blog/uploads/media/83/bc/83bc606692e4236565620ca005c4bb97/b23a9a7219296c688c27a4e6120eb5c9/RK3ISK3CokLhoqYqN1sE7pIuh4OyFam7xaInYw_-6qd-8nY4I3a65jm5VRwI_EWHm1cZ1iM4YGVasCIvyu1ZwrzJz5kCTgE6wz05IQ2LoMfNpPTb4bliqwJVNxG99Q-hySlOgs-er21z.png)

You then need to encrypt your passwords (for security purposes). A free tool like [HTPasswd Generator](https://www.web2generators.com/apache-tools/htpasswd-generator) will encrypt your password for you.

Just enter your username, password, and click “**Generate .htpasswd file**.” And copy the output.

![HTPasswd Generator tool showing the encryption of a password.](https://static.semrush.com/blog/uploads/media/55/7e/557e2ed8ccca240d54dcdb1fc8b21e22/9d7498d480a2d6f801cfc2634902d82f/LtSjEUHdSThgfdsg8FFBRBsOMen5st3TYR6otggkIA6R_OJe5ZTOcLbwJA_6AyuqpMOg24mI_fjFdf0P3kXrdH7x5rwKgfhs9JlUUSVd58rgFTrDJYq1Wl9eU4U7noERwWqB9SKz6eAC.png)

Paste the output in your .htpasswd file and save your file.

![Encrypted password along with a username inside the .htpasswd file.](https://static.semrush.com/blog/uploads/media/7e/ec/7eec0cd56ec0a8e8d32a22eb2f69fe05/4de6b72e483a08b8740fa6ccec5dc705/qZQWdIRklQduik9WS9cOJqydXNM4qggP5DJQyxEVnEOEyEK6iMNI4V7ayp_zdfsFYjFeTfWGGJY90hfU3XrhtZKX2M_ZCtd7MhcuhNCPY1xKuSUrO43iGS1Aylh5EIs0dRX9R95FomvM.png)

Lastly, open your .htaccess file and add this directive:

`# Password protection
AuthType Basic
AuthName "Restricted Area"
AuthUserFile /path/to/.htpasswd
Require valid-user`

Make sure to change the path of the “AuthUserFile” line to the path of your .htpasswd file. And save the file.

Head to your website. Your site should display a prompt upon loading if the directive works.

Enter your username and password and click “**Sign in**” to access your site.

![Sign-in box on a webpage as a result of .htaccess password protection.](https://static.semrush.com/blog/uploads/media/9b/0f/9b0f90129b49454d082de007e4bc33af/4635b7a8bce57a837d79c5dd68fa2bb2/7be_JChQ0bldhxr6OEo4xXofCNv7ondWTOE_FY18zCfbdQ2Y6EgeTuFTcfJ0vHF3rnZ9pSRpNY-VMtlJHi0AiaN2Dkkg2p0XKctUjPMD3CmTRBSPWSdp8zmHy7IClWXqwfKSrZPNdDdT.png)

#### Other Ways to Password-Protect Your Site

If you’re using WordPress, an easier way to set up password-protected pages is by using the platform’s native password protection functionality.

Log in to your site and head to the page or post you want to set up password protection for.

Next to “Visibility,” click on “**Public**.”

![WordPress page with the visibility set to Public.](https://static.semrush.com/blog/uploads/media/87/88/87887a2442bbbb7b4db5cbe588cc5d15/252d06d306c6c074df216b59f1f9875b/XVasAtSC5QtOScPJGFa2debU0SQSpTpWBgIxF_3UFWQ6VUJjpst2I99J-poUW74PivjhvcqWiP6w3M5q83F8ZLG7t-pPUj8y-IazUvUXC67O0GafkF4P_l_D22nPMtAA0_yEaFQ_fry7.png)

Select the circle next to “Password protected” and enter the password you want to use. Then, exit out of the prompt and click “**Update**.”

![WordPress page visibility options showing space to enter a password for password protection.](https://static.semrush.com/blog/uploads/media/38/69/38692b4439536bb07db5a24bf740bf64/a266532fd3ca45259113c3039551102a/nAmPG7YpHF2-JLvIWn54Iz4nGbktOrmNonLt6-4HRDecUA7Ua3pnjpAhSS6eptZF5MB4r_1xEAHHOZPTRuDzgTbSuks1tIlJQcUsTYFunRQZSX9T4MziigmwM2q48vthP_6Zwxef2XMW.png)

Now when someone tries to access the page, they’ll see something that looks like this:

![Password protected WordPress page.](https://static.semrush.com/blog/uploads/media/77/10/7710abd4f08ac3e9fc2ebc044b14a24d/d6f5f63b31c33b6f762a21a0dfe5b002/-WPgNoE9nUuj00fICI8SUQJY7H7LJlpZSTlQM4Yzxx4tO-9Z1oQ3E5tTpuXwZF5JiE_TW6GQn8WTAbUY6_6LzsALC78bo8vK-50vsFSSdje6iUQQGU-Fw2JJINh2vqx0yC2gIQTlMvsD.png)

And they’ll need the password to access the content.

But this means you can only have one password for each page—you can’t have different passwords for different users.

For extra functionality, you may want to consider using WordPress plugins instead.

## Common Performance Issues Associated with .htaccess

Keep these issues in mind if you decide to rely on your .htaccess file to make specific changes to your site.

### Speed

Using many or very complex .htaccess files can impact your site’s performance. And cause it to run slowly.

Why?

Because Apache needs to read and interpret each directive every time a request is made to your server.

So, carefully consider what’s necessary to include in your .htaccess and what isn’t.

And keep it as concise as possible to avoid site performance issues. Since [page speed](https://www.semrush.com/blog/page-speed/) is a ranking factor, you want your site to load fast.

While there’s no ideal length for an .htaccess file, one way to determine if your .htaccess file is impacting side speed is to run speed tests before and after making any .htaccess file changes.

Free tools like Google’s [Page Speed Insights](https://pagespeed.web.dev/) let you test page speed by entering a URL:

![PageSpeed Insights for Semrush.com showing the site is passing Core Web Vitals.](https://static.semrush.com/blog/uploads/media/3c/fa/3cfaec8a32eace37540ca82242956662/43dfd9fc2f9eac6bdc978069848bf883/mJ6rmKxIRfxDIkLlLJ7XyQ9qSx1CYVz4HgN_WbZmctdqq48BICRp9x8k3SbpzV0Nq42opXvJuUJFrPCYafX8ea-yL4vDFPKhATjrCitfPJ-yNJ2_FAs97YXutmvAKdAISNuQ2QNKlcIM.png)

You may need to speak with a developer to review your .htaccess file if your page loads slowly after making updates.

### Security

Because .htaccess files let you redirect entire sites, someone who hacks your site can use the .htaccess file to redirect your site somewhere else.

So, check your .htaccess periodically for any directives you didn’t add.

Also maintain regular backups of your site. Ideally, your host will also do this for you, but you may want to keep your own backups as well.

That way, you can quickly revert your site to an older version (which includes the older version of your .htaccess file, too) if something happens.

### Accessibility

Improperly configured .htaccess directives can lead to accessibility issues. Like incorrect redirects that don’t take people to the right page.

Users are more likely to leave your site (and potentially head to a competitor) if they can’t find the content they want.

So, it’s important to keep an eye on any technical issues that might arise from improperly configured .htaccess directives.

## Spot Technical Issues on Your Site

Your .htaccess file allows you to make powerful changes to your site with relative ease.

But those edits can also cause unwanted errors.

Use Semrush’s [Site Audit](https://www.semrush.com/siteaudit/) tool to help keep your site error-free when editing your .htaccess file.

Site Audit monitors errors and sends you regular updates, so you don’t need to worry about keeping track of them yourself.

Try it today.
