---
title: "How to Redirect HTTP to HTTPS (4 Methods)"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "redirect-http-to-https"
url: "https://www.semrush.com/blog/redirect-http-to-https/"
canonical: "https://www.semrush.com/blog/redirect-http-to-https/"
author: "Connor Lahey, Sydney Go"
published: "2021-06-03T20:05:00+00:00"
updated: "2025-02-20T10:11:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons: []
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T18:51:58+00:00"
status_code: 200
html_hash: "ee4e39d0054165b1433971b7ebf7d345bf0b85d6aef43475812a86be26f662c9"
clean_word_count: 2116
clean_char_count: 15654
---
# How to Redirect HTTP to HTTPS (4 Methods)

## What Are HTTP and HTTPS?

Hypertext Transfer Protocol (HTTP) and Hypertext Transfer Protocol Secure (HTTPS) are protocols that allow computers to send and receive information, such as text, images, or videos, over the internet.

For example, a website visitor’s browser uses HTTP or HTTPS to request the page and its content from the website’s server. The server sends the data back, and the browser displays the website.

HTTPS is the secure version of HTTP and uses an SSL Secure Sockets Layer (SSL) or Transport Layer Security (TLS) certificate to encrypt data.

Encryption protects data (like passwords or credit card numbers) during transfer.

Here’s an illustration of how [HTTPS](https://www.semrush.com/blog/what-is-https/) works:

![A browser connects to a server with a user ID and password. With HTTPS, a hacker sees an encrypted user ID and password.](https://static.semrush.com/blog/uploads/media/51/c3/51c3f1a9dc4955985a9ba8259de9a859/5de47cbcdd88f25a23526094fda9dc0d/AD_4nXco_TbirCWd5nUw3nijjM3XCwhRdr6qloXERTDDhbVKCNYaCD16dNUYGqhXOv3a1xZHyrHFnxQE68G3-0y6SJfIfE3GL5k-zZ_7yAs3fNEEzrvrJN4MCXKWBRDVNaAIjCqQc9HunA.png)

## Why Should You Redirect HTTP to HTTPS?

You should redirect [HTTP to HTTPS](https://www.semrush.com/blog/http-vs-https/) because it protects sensitive information and can boost your website’s ability to rank (appear) high in [search engine results pages (SERPs)](https://www.semrush.com/blog/serp/).

A proper redirect sends traffic from the non-secure HTTP version of your site to the secure HTTPS one.

If you buy an SSL certificate from your hosting provider, your host will usually handle the redirect automatically.

But you might need to force the redirect manually if you have a custom setup.

The exact process can vary based on the type of server you use, so we’ll go over a handful of ways to do this.

## How to Redirect HTTP to HTTPS in WordPress

You can redirect HTTP to HTTPS in WordPress with a plugin or by editing your files manually.

Here’s how to do both:

### Using a Plugin

WordPress plugins like [Really Simple Security](https://en-ca.wordpress.org/plugins/really-simple-ssl/) offer no-code solutions to redirect from HTTP to HTTPS.

Here’s how to use it:

Log in to your WordPress account. Head to “**Plugins**” and search for “Really Simple Security.”

Click “**Install Now**” and activate the plugin after installation is complete.

![AD_4nXeAUWTrMvBPDjKd5CI3h9q0pprtajAbfPfs8ehjEuuaA--pGXIIyGGg-6dxK7jF21uLlfKIEbgMkCWyXogitdh31X_VKMA5ckBqEqyvH7xIVPUXE-igAjTHjYZaOTgWh_HlGoovGA?key=slCHbKjVXUUuIXzUZmE_M-EU](https://static.semrush.com/blog/uploads/media/01/64/0164d3ec1598903ed0115f644153e4aa/4e4aaf315b11a1bc0d2949f164f09843/AD_4nXeAUWTrMvBPDjKd5CI3h9q0pprtajAbfPfs8ehjEuuaA--pGXIIyGGg-6dxK7jF21uLlfKIEbgMkCWyXogitdh31X_VKMA5ckBqEqyvH7xIVPUXE-igAjTHjYZaOTgWh_HlGoovGA.png)

Follow the plugin’s onboarding wizard. It will ask you to provide information like your host and email address to test the configuration.

![The setup wizard detects an SSL certificate.](https://static.semrush.com/blog/uploads/media/5f/2f/5f2f4836b7740303f025dd621b2287fd/b979a78276a10ef5eea35fb8b86af3d3/AD_4nXep41eq_VAKc4qvXsHMMcjjurEYqusU4OmD1SmlY8UdsAtQ6XD-Rg5PzhRr427Ar_zwWxGL4z67BwxMNMgFCMDTcsvsTNpHAGzYZrM1p1onJcEVIeLKqPhKNiSR0vBkfejdo9B6Jg.png)

Your site should automatically forward users and search engines to the HTTPS version of your site once you’ve completed the onboarding flow.

### Editing WordPress Files Manually

Edit WordPress files manually if you prefer a hands-on approach or if your hosting environment won’t allow a plugin.

Go to your WordPress dashboard to get started.

Click “**Settings**,” select “**General**,” and locate “WordPress Address (URL)” and “Site Address (URL).”

Replace “http://” with “https://” in both URL fields.

![To redirect http to https in WordPress, the URL is updated.](https://static.semrush.com/blog/uploads/media/84/37/84371d1a7c132100374d0cdf815ace79/22637db442492b24656a8e83bea7d99f/AD_4nXfsqRo8tIbkjlyQSOKDflMlq1qsBejCRXJFvjYRh5zYVx4AVfdKmIBcrYQKHLw20L0nmm1_QgUA2b8lcLgDOe-cguJokaEA-B5aUsRsBEGMA0UIGh4RPE0zr2FSoz2Ja86ISsH8tg.png)

Click “**Save Changes**.”

Then, you’ll need to edit your configuration files (i.e., files used to customize your web server).

Then file you need to edit depends on which server hosts your website:

- **For an Apache server**: Edit your [.htaccess file](https://www.semrush.com/blog/htaccess-file/) (a configuration file often found in your root folder) with this code:

`RewriteEngine On
RewriteCond %{HTTPS} !=on
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]`

- **For a Windows IIS server**: Update the web.config file (a configuration file usually found in your root directory)

`<configuration>
<system.webServer>
<rewrite>
<rules>
<rule name="Force HTTPS" stopProcessing="true">
<match url="(.*)" />
<conditions>
<add input="{HTTPS}" pattern="^OFF$" />
</conditions>
<action type="Redirect" url="https://{HTTP_HOST}/{R:1}" redirectType="Permanent" />
</rule>
</rules>
</rewrite>
</system.webServer>
</configuration>`

## How to Set Up an HTTP Redirect in Nginx

You can set up redirects for Nginx (an open-source web server software) by adding rules to your configuration files.

Here are two different ways to set up redirects in Nginx:

### Redirecting All HTTP Sites to HTTPS

Redirecting all HTTP sites to HTTPS is ideal when you have multiple domains under a particular Nginx configuration and multiple SSL certificates.

Follow these instructions:

1. Open your Nginx configuration (nginx.conf) file or the relevant server block file, usually found in “/etc/nginx/.” If the file doesn’t exist, you may need to create a new one.

2. Add a server block (code) to the configuration file to catch all traffic on port 80 (traffic coming through the HTTP version of your sites) and redirect traffic to the HTTPS version:

`server {
listen 80 default_server;
server_name _;
return 301 https://$host$request_uri;
}`

3. Add another server block listening on port 443 with your SSL certificate details for each domain:

`server {
listen 443 ssl;
server_name www.example.com;
ssl_certificate www.example.com.crt;
ssl_certificate_key www.example.com.key;
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers HIGH:!aNULL:!MD5;
...
}`

4. Locate your server’s terminal and test your configuration by running the command `sudo nginx -t`. The output will show you if you have any errors, so you know what to fix.

5. If your test is successful, reload Nginx, so your changes take effect by running the command `sudo systemctl reload nginx`

### Redirecting Specific Sites

Redirect specific sites if you have multiple apps or sites and don’t require an SSL certificate for each one.

Here’s how:

1. Open your Nginx configuration (nginx.conf) file or the relevant server block file, usually found in “/etc/nginx/.’ If the file doesn’t exist, you may need to create a new one.

2. Add this server block to the configuration file to redirect HTTP traffic to HTTPS

`server {
listen 80;
server_name example.com;
return 301 https://example.com$request_uri;
}`

3. Locate your server’s terminal and test your configuration by running the command `sudo nginx -t`. The output will show you if you have any errors so you know what to fix.

4. If your test is successful, reload Nginx, so your changes take effect by running the command `sudo systemctl reload nginx`

## How to Redirect to HTTPS in Windows IIS

Redirect HTTP to HTTP in Windows IIS (a web software server from Microsoft) by editing your web.config file.

Follow these steps:

1. Download and install the (download the [IIS URL Rewrite Module](https://www.iis.net/downloads/microsoft/url-rewrite) if you haven’t installed it). Then, open your IIS manager.

2. Select your site in the menu to the left. And click “**URL Rewrite**.”

![AD_4nXc9AaC4N64kTtVID6rD9rzPFIIjWdZINg7sdOumfWUKz6MRX-rWpfu03CVY5rax333xUnzxdB5EmpvkV5IClzNjmWmh5NqynhyywEIEDVca-ZWtO6xyQ_lTZ2Zbydu3-cwJ3bFkZA?key=slCHbKjVXUUuIXzUZmE_M-EU](https://static.semrush.com/blog/uploads/media/e1/8c/e18cd0367fdb8ca3709aa8b9b4b9975a/4080ea6ac47ff07cc4ec8ca15e2820c8/AD_4nXc9AaC4N64kTtVID6rD9rzPFIIjWdZINg7sdOumfWUKz6MRX-rWpfu03CVY5rax333xUnzxdB5EmpvkV5IClzNjmWmh5NqynhyywEIEDVca-ZWtO6xyQ_lTZ2Zbydu3-cwJ3bFkZA.png)

3. Click “**Add Rule(s)…**,” choose “**Blank Rule**,” then name your rule.

4. Set the fields to “**Matches the Pattern**,” “**Regular Expressions**,” and “(.\*)” And check the box next to “Ignore case.”

![Name the inbound rule, "HTTP to HTTPS."](https://static.semrush.com/blog/uploads/media/46/82/4682eb37a36f08d2e0e07ebc7898e253/9544c8281bd51ca703883c5f2cef0929/AD_4nXf1rlJ5RrwjhpkURpHzLdNrkqPuN6xnf49q9KgQsmp4uDqrX8JevzKuOCN2qiqVuUPWTPuPV8znE7LbWyKw8v07xrxYQiWqfhQD1BTiLdBBMfKkb6zKEG56uzDv6Dtu1rywJF0E.png)

5. In the next window, set the fields to “{HTTPS},” “**Matches the Pattern**,” and “^OFF$.” And check the box next to “Ignore case.”

6. Once you get to the “Action” section, choose “**Redirect**” under “Action type” and set the destination to “https://{HTTP\_HOST}/{R:1}.” And check the box next to “Append query string.”

![Redirect type is set to permanent 301.](https://static.semrush.com/blog/uploads/media/1b/81/1b8134cb800bc82264415f8e1e7d2aa0/417a674b85f1ee329be99ab9531685a1/AD_4nXcjSqSWBCAIZ3bTzE8IfrVCg1p-c8FnU2p9q-xkLAEN6xX_FejgpJuVpCaxKupHVGpwxIfrRnThvorgtMFyFYXgmeMqghlIS1G9q3Chk3yQcDHSekVzLDe6-UwnSskExEEt3Hlp7g.png)

7. Click “**Apply**.”

## How to Do an HTTP Redirect in Apache

Set up HTTPS redirection in Apache by using an Apache Virtual Host or modifying the .htaccess file.

### Redirecting with Apache Virtual Host

Redirect with Apache Virtual Host if you have full control over your server’s configuration files and want to manage files at the server level.

Here’s how:

1. Open your Virtual Host file in a text editor. Virtual Host files are usually found in “/etc/apache2/sites-available/.” The file name often corresponds to your domain (e.g., “yourdomain.conf”)

2. Set up a Virtual Host on port 80 by adding this block to your file:

`<VirtualHost *:80>
ServerName yourdomain.com
Redirect 301 / https://yourdomain.com/
</VirtualHost>`

3. Make sure a Virtual Host block with your SSL certificate details exists. This block may be in the same file you're working on or in a separate file. Add this block if you don’t have a Virtual Host block:

`<VirtualHost *:443>
ServerName yourdomain.com
SSLEngine on
SSLCertificateFile /path/to/your/certificate.crt
SSLCertificateKeyFile /path/to/your/certificate.key /path/to/your/certificate.key </VirtualHost>`

4. Save and close the configuration file

5. Restart Apache for the changes to take effect

### Redirecting with .htaccess

You can redirect HTTP to HTTPS with an .htaccess file if you don’t have access to your server’s configuration files.

Follow these steps:

1. Locate the .htaccess file in your site’s root directory

![The root directory in this example is public_html. Then, choose .htaccess.](https://static.semrush.com/blog/uploads/media/26/ca/26ca5ccfd88e6367d4ee77ddbdaa6623/f1b26aa37277e73e84f1a0d3f1b6c7fc/AD_4nXfIWApqQmpwYozYCwigJUnQzXsNJPVGdBtbY5ncmiE6iKxb5nei_TWiUaGPF-5HuuBMObb3cdBTlufnTVI6gvheJ_hwDMperg79NkQoPRapMd-7eQ1vikdIY1WUQY2K0TYzguQ_.png)

2. Open the file and add this code:

`RewriteEngine On
RewriteCond %{HTTPS} !=on
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]`

3. Save the file and check to make sure the redirect works. If it doesn’t, you may need to speak with your host and ask them to configure your server to allow .htaccess overrides in Apache’s main configuration file.

## How to Verify the HTTPS Version of Your Site

Verifying the HTTPS version of your site ensures that the redirect works and will point both users and search engines to the correct version.

To do this, enter both the HTTP and HTTPS versions of your domain into a browser bar. You should end up on the HTTPS version in either case.

Next, verify the HTTPS version of your site in [Google Search Console](https://search.google.com/search-console/about) to make sure you can properly track performance:

1. Go to Search Console, sign in, and add a new property using your HTTPS URL prefix (for example, “https://yourdomain.com/”). Then click “**Continue**.”

![AD_4nXfipANy6uan5wjSKHi5EAdeP3H5Clau4oXidcl7FBshb6eZnex5tTU8BzRqszsbEcQOpj3toKUjwGDiXqYUpfMyDLF8qaOaVG3qOTx-gibhafbrLE5_Io2Wl3ZyGlSqJ82zZoNJvw?key=slCHbKjVXUUuIXzUZmE_M-EU](https://static.semrush.com/blog/uploads/media/8b/e4/8be424bd35881ae55a02e559623f626f/ee17d594fca15af1969a4bb2e6367977/AD_4nXfipANy6uan5wjSKHi5EAdeP3H5Clau4oXidcl7FBshb6eZnex5tTU8BzRqszsbEcQOpj3toKUjwGDiXqYUpfMyDLF8qaOaVG3qOTx-gibhafbrLE5_Io2Wl3ZyGlSqJ82zZoNJvw.png)

2. Complete ownership verification using the recommended method

![The recommended method is via HTML file. Steps say to download the file, upload to your site, then click Verify to continue.](https://static.semrush.com/blog/uploads/media/a2/9f/a29f2a8b45ac805462a6438629f2f698/87141d303b8ccece3b91f6d25520a8fe/AD_4nXdDTVqFu9BWY_tl88ff5My7X0A_lw_P1ZAzF0dnPpfg_u1No_CbEWpyynQO57fWP2bZIGpMA7LQ5SwyfSsK3o5w5I2UPeTHAshnz-gB9hbKKn5nyYuUPi_sRlhsJbMo9ryOZL63Zw.png)

3. Click the drop-down to see that your website has been verified. Verified sites appear at the top of the list.

![In Google Search Console, verified and not verified properties are shown.](https://static.semrush.com/blog/uploads/media/4a/2f/4a2ffad4fd087b3e41f0fef942a48674/8b94f2984724b0c1cb823a963287bf68/AD_4nXfv6rQ_DYx0OdLqW6qXFAK9Mjls-VcGIrZWBjT2pK3uO5fIMbJXAhlaqlFCwRyPxubRSLZdwq4W_91KNfvixto4NXUAR_lrzojfAmbxaZ9Zn1MUcNTV86nYg6XWxWly3iZVMNXvJA.png)

## Check Your HTTPS Implementation for Issues

Moving to HTTPS can sometimes lead to unexpected problems like mixed content (when content loads in HTTP and HTTPS), which you can find with Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool.

After [configuring Site Audit](https://www.semrush.com/kb/539-configuring-site-audit), click “**View details**” under HTTPS.

![Site Audit overview shows reports, site health, technical SEO errors, and HTTPS specific issues.](https://static.semrush.com/blog/uploads/media/62/2c/622ce26ecec239c596d3b3d84a836d69/2425df6f3dfe3e126a11ad9de425773d/AD_4nXdi8Tp6LURF5aIJOt2tk32T7UBbjJDsjAZ4T-D-woQJEFc48khfnxvBXD9Bpk1OG56vTk0nCAem-CrJtjuZ8B7vrvZFcuv5Z7gPBytjEUeIGOeU2FQGMM2MgbTf2QtC7Ri2cwfDzA.png)

The tool will bring you to a page with a list of issues you may want to fix.

For example, the audit below shows the site has an HTTP URL in its [sitemap](https://www.semrush.com/blog/website-sitemap/) (i.e., a file outlining the structure of the site).

![The error says, "1 HTTP URL in sitemap.xml for HTTPS site."](https://static.semrush.com/blog/uploads/media/f5/03/f503da2caab63f2095494c6f76abb762/be3dda1a4b813acbc64ecebcc4b66a9e/AD_4nXdMR5ohdjHONKmXU05Psrb2tGGgIQylOWDlYvP8huU-6jJH5HvATdtK6UzTj90chrxIbqlvjdCjZQvzmj8uCuv7MFIC-uTiTAccGUClTnT3GuiYLVyBtrupipUnMj10qxK5Yp37XQ.png)

Click “**Why and how to fix it**” next to any issue that’s flagged to learn about it and how to address the problem.

![The pop up explains the issue and says to replace all HTTP URLs in your sitemap with HTTPS URLs.](https://static.semrush.com/blog/uploads/media/a6/b0/a6b0a39102fd7ca7484f26e05097edde/51c8b8a06df74b8f2f99de69064f9175/AD_4nXfFsfv0ClODcc1RjfvwROLxRJoFcb-lCE4TT-7ZO6nQpcKaOXiU7jQ34zz6OtSr6E0Ijv7Xdz5icPTk9buzPlovRX0yPr06sr_UqqSHyop4A1timhcD2_37kaS2UNXAXmSckOR5KQ.png)

Regular audits like this can ensure your site remains secure, fully optimized, and reliable for your visitors.

Want to check your HTTPS implementation?

Try Site Audit for free.
