---
title: "What Is HTTPS & How Does It Work? [Explained]"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "what-is-https"
url: "https://www.semrush.com/blog/what-is-https/"
canonical: "https://www.semrush.com/blog/what-is-https/"
author: "Tushar Pol, Christine Skopec, Zach Paruch"
published: "2020-07-31T13:00:00+00:00"
updated: "2024-01-22T09:59:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2024_watch"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T21:04:49+00:00"
status_code: 200
html_hash: "7b84b7953676c31b2a5c52e3da3b9e396bcf1d1b03c9fd92ff841912fbfa6587"
clean_word_count: 2131
clean_char_count: 16712
---
# What Is HTTPS & How Does It Work? [Explained]

## What Is HTTPS?

Hypertext transfer protocol secure (HTTPS) is an encrypted version of HTTP. Which is the protocol used to transfer data between web browsers (like Chrome) and servers (computers that host websites).

When you visit a website that uses HTTPS, the connection between your browser and the website's server is encrypted (meaning it’s scrambled)

This protects your data from being spied on by attackers.

![A visual of a browser and a website's server, with a secure data between them (HTTPS)](https://static.semrush.com/blog/uploads/media/c9/54/c954ffbcdc5a4355a7bbcce2f174bde3/cb61b9b1e7629220cf6b77b37ff5c157/aLSFsZSLoNtGxdzc2ZNLV15fN9GyEkYxZlXkpwUF8ThITFYzvowGH8gbYH4Cla_73vbAYCimR-v9fu0vuP7qjDAtjYdTmxRxjCnrM2jkFpk2Ju1sG3-u4Y73_zEpKb4a7VlG5so0WvFqSmowFg2wvBw.png)

That data includes all types of confidential information—login credentials, payment information, and browsing activity in general.

So, in other words:

The HTTPS protocol is fundamental for keeping your data private and secure when surfing the web.

But how does it work, exactly? And how is it different from HTTP?

Let’s find out.

## How Does HTTPS Work?

HTTPS works on a request-response model (meaning the browser sends a request and the server responds to that request), just like in HTTP.

But HTTPS uses a secure sockets layer (SSL) and transport layer security (TLS) certificate for encryption. (These are digital documents that prove the identity of a website. So an encrypted connection can be established.)

Here’s how the entire process works:

1. **Browser contacts website**: The user's web browser attempts to connect to a website using HTTPS

2. **SSL certificate sends**: The website's server responds by sending its SSL/TLS certificate to the browser. This certificate contains the website’s public key (encryption key) and is used to establish a secure connection.

![A website's server sending SSL/TLS certificate to a web browser attempting to connect to the website using HTTPS](https://static.semrush.com/blog/uploads/media/5e/fa/5efa02276f59f4edfebcc8254e75f88d/71dc95b01075afce7fdd48a7c0edfe75/haBJQA2lEdk-HxLfcvGx3ugI8R8uYdSzTYd3piGGBntFLww9rGEoUMzWxfGJIiav0AjpI-zwtp4zW7wkIyiwzln_qhgXvFN-OyHUg9rjPUY-21yVnz9Sd4sh_H6PpMd-t1Nfka65JRvOHGUXjg6REGg.png)

3. **Browser verifies certificate**: The browser checks the certificate to ensure it’s valid and is issued by a trusted certificate authority (like GoDaddy, DigiCert, Comodo, etc.). This step is crucial for confirming a website’s authenticity.

![Browser verifies SSL/TLS certificate](https://static.semrush.com/blog/uploads/media/9d/4e/9d4e677d3dd2f4131f2c9349ac7d59bc/b1c476982e7bd5a3c3b1094dedc97e33/wzVoLU_IhmwN3SC6Ne3YH1LqAPDGOgcYbWcT08_U3yYjR2z2H-18xem2QZDkxMIoNx65fISLBamUxbOI2iEIh3U3tMSnqVuJknAWXVJYL5bcFWAu-EZo0dKUso5jQGVfMPTgtTcOfGGJPFMEkjgNXx0.png)

4. **Encryption key exchange**: The browser and the server establish an encrypted connection by exchanging keys once the certificate is verified. The browser uses the server's public key to encrypt information, which can only be decrypted by the private key (i.e., the decryption key) the server holds.

![The browser and website's server exchange keys once the SSL/TLS certificate is verified](https://static.semrush.com/blog/uploads/media/ae/27/ae271d1b7da5cdf4857581cd2b0c868d/075b627cd2e4b32534c336f22922f22d/6e4b0ckg374hLCOtNo_zxOKjcETok65G9jkkCBJLP78pNn72w_alY-dkAzKRIkhQRi85R-iZhkuAjoVwkHcnv0HipoXA3tlbG-7lryK7yUqdYbvUKeuMIUoNBZ9mF8GhUOxDdAjQIvs6FF-6VxVS0j8.png)

5. **Encrypted data transfer**: All data transferred between the browser and the server is encrypted after the secure connection is established. Which ensures it can’t be read by anyone intercepting the data.

![The data between the browser and the server is encrypted](https://static.semrush.com/blog/uploads/media/4b/30/4b30307e90a5f5c7f6a727f552aeac75/ace5a77049e26168f5d88577e5c4a00e/0OlW8GCW0NoxzPo8OtRjXp-77MoDQfS46fg022xyy-woLoWx8jVcQTadNev91gm2mZ5NNBAJiCgTLoxp7Ln20ew0JqJ0n7661VkI4XTO1v9IY8VeiqgyyrI352RuoTXUcRgLvX6nDOU0HtqxyQ9n3YU.png)

6. **Data decryption and display**: The server decrypts the received data using the private key, processes it, and sends back the requested information. This data is also encrypted. The browser then decrypts the incoming data and displays the website content to the user.

![A browser displaying the website content to the user once the process is finished](https://static.semrush.com/blog/uploads/media/31/17/3117e66bc0a3e9c7df806ef5cd13cad6/cfac907acf4dc4cb99bfceac2e41d819/4WO4ydADsntrAKzhcPz8qtEGsG3_bxqzej_6PbZUfMn7u4VSTL9OSeSEoe_uErwHlkFWOJZl-refVE-nXuXMownsbISMfxhEzh20zD7irKROAhd80hA14DkpEfFPUBFB6TjytsdvItonTbNFmrzAw6g.png)

## HTTP vs. HTTPS

Now that you know how HTTPS works, let’s quickly go over how it’s different from HTTP.

HTTP works differently from HTTPS on several different levels:

### Encryption

HTTP transfers data as plain text. This means anyone can easily intercept and read it.

![HTTP transfers data as plain text, making the user id and password easy to intercept](https://static.semrush.com/blog/uploads/media/bd/aa/bdaa2f43e22b90b32dd39f4db21a7c48/f5e1aa017bbc02265a6267e31d9d0828/4q63NuK1ZE8WAq4RPKinB7dpeNFoBp-NcRDGEuu4MBkaCS2CsFTEICL5LxY5fVPCumoxOyaVZXEwzFvMxWSGuSNFI2MXiRNqWOOKlNryl-H_aDCMeAdeX0GhSSbpMhDeMMvVb0Q_TpGhPVHGxy11dUE.png)

HTTPS, on the other hand, leverages encryption to shield the data. So the information remains unintelligible and secure, even if it’s intercepted.

This means hackers would only see a scrambled sequence of characters rather than the actual information.

![HTTP transfers encrypted data, making the user id and password (from the example above) more secure](https://static.semrush.com/blog/uploads/media/4d/45/4d45bcd926b55bb284d5e080c8cf222f/9d7a4b04bd48dd92c2958aa707dd9c53/knk_I1snMteFaFc0gQZMWrwGjTU0QpojEu2WLlV-H7WaP-NOrXaeBZDCBnFm2VCYCKkUZ60MC5ZRp4jM5ymRv5iIamxrkSLtq9VTyCVaExhcDz2H05r3h1hqANKh3owaXc3EjDarN8__5h0lr2gF43g.png)

This is the main distinguishing factor between HTTP and HTTPS.

### Ports

Ports are like virtual doors information travels through between a browser and a website server. And each port is assigned a number.

Both HTTP and HTTPS use standard ports to facilitate communication.

HTTP typically uses port 80 as its default—this was established early in the development of the web for sending and receiving content.

HTTPS uses port 443. Which is reserved for encrypted traffic.

![HTTP typically uses port 80, while HTTPS uses port 443](https://static.semrush.com/blog/uploads/media/e7/a1/e7a1b33235f6d87837b0f0bd5966c83b/cd52ac337f7949da4d9205b3d762acf9/QusW5uZaKZm9amx_80uLemrejiHJnIFllq2RMUOCfwgLpJ9phRYkiHGz1YOWDEGrAyBMalvmS0Bf_hBouksrdmftfDm__o4Gq2AK04xtF6zgENfA4C_fEFuPIJPCf7kXEFh5iTW05fA22hSdqe9b394.png)

### URL Format

A uniform resource locator ([URL](https://www.semrush.com/blog/what-is-a-url/)) serves as the address for locating resources on the internet. And it’s formatted slightly differently for HTTP and HTTPS.

HTTPS URLs begin with “https://.” Which indicates a secure connection.

But HTTP URLs start with “http://.” And the missing “s” signifies the absence of security.

![HTTP URLs start with “http://.”, while HTTPS URLs begin with “https://.”](https://static.semrush.com/blog/uploads/media/8c/7d/8c7d225e9977f5504cc9f5b4880e5bf2/a5a1edccf5681ab0db7249902fd3d37d/oNQaee618HQ7ZvSat8iXGPssShtNCkiYgQlp46g3V8k87-AVwts_TPuUNwphVVvMtJWqKXzZ1silB1H8s1trWua2OnfLrEmcHwDqbUyIV2R1DzuY9ZbOnxoi2atgfNNPv_W0fc9GPxK2hD3F9OKIVj8.png)

### SSL/TLS Certificate

Keep in mind what we said earlier about how an SSL/TLS certificate is a digital document that proves a website’s identity and authenticity.

This added level of verification is only used in HTTPS communication—not in traditional HTTP communication.

![In HTTPS communication SSL/TLS certificate proves a website’s identity and authenticity](https://static.semrush.com/blog/uploads/media/c6/8c/c68c398de579ac227690a69a174f2e49/ae29cc49ff936b065082c7b9d4ffd3f3/RyLQYYnDfevxXq_APzPa-66NGlo9YMs6I1n1OmSBOPeGjHNCX73IQDmlHcPTKzQDZThHjk6NqDrd6bxV-oDHt6Z9MXzgRU4ESARLxxommtTbh9S7OA20omwsFB0aLAJ2zjpMfXGtnR6Hh-cBUEpta60.png)

***Further reading**: [HTTP vs. HTTPS: What’s the Difference?](https://www.semrush.com/blog/http-vs-https/)*

## Advantages of HTTPS

We’ve covered some of the benefits of HTTPS already, but here’s a quick refresher in case you need reminding (plus, some additional benefits):

### Enhanced Data Privacy

HTTPS protects users’ privacy. So their sensitive information (such as credit card numbers or login details) remains confidential and inaccessible to hackers.

Compare that to HTTP. Where the data is sent in clear text and can be easily intercepted. Which leaves users’ privacy at risk.

They’re vulnerable to attacks like [man-in-the-middle](https://en.wikipedia.org/wiki/Man-in-the-middle_attack), [packet sniffing](https://en.wikipedia.org/wiki/Sniffing_attack), and [session hijacking](https://en.wikipedia.org/wiki/Session_hijacking).

The encryption used in HTTPS connections prevents these attacks by fully securing data that flows between a browser and a website’s server.

### Enhanced User Experience

HTTPS positively impacts the user experience because it fosters a sense of trust in users when they’re browsing, shopping, or sharing information online.

Users are becoming increasingly aware that they should look for the padlock symbol to confirm whether a website is safe

!["Connection is secure" padlock next to the "semrush.com" in the browser’s address bar](https://static.semrush.com/blog/uploads/media/39/8c/398cf5aa1ecbfea6399603c3c68629dd/8241f3ab8817b048e2fe1a94662ec838/rYs59O05E6etyYbLkb79G5qGp6Ohr8kh5UiTuy06Ver4rEaQ3vJABnCrBCUDuN2TE57V87IuOwshJxWKlShMzzOGueY3a4k6pWwouB_Y0mqrjvBjbR4l96dqEWcyk6AfWLGZnZjk1IlKLFIy-eZScbM.png)

This means that websites using HTTPS could be more likely to retain visitors, reduce their [bounce rates](https://www.semrush.com/blog/bounce-rate/), and potentially increase conversion rates (as users feel more comfortable making transactions).

### Better SEO Rankings

HTTPS can boost your website’s ranking and visibility on search engines like Google.

Why?

Because Google uses HTTPS as a ranking signal. This means websites that use HTTPS are more likely to appear higher on search engine results pages (SERPs), attracting more organic traffic and potential customers.

If you’re serious about SEO, check your website for HTTPS issues. Which are common among sites that have recently migrated from HTTP to HTTPS.

These issues include:

- [Internal links](https://www.semrush.com/blog/internal-links/) (links on your pages that point to other pages on your site) that haven’t been updated to HTTPS (after migration)
- Mixed content issues where other resources on a webpage (such as images and CSS files) are still being served over HTTP
- A mismatch between the name your SSL/TLS certificate is registered under and the name displayed in the browser’s address bar

And more.

You can check your site for all these issues using Semrush’s [Site Audit](https://www.semrush.com/siteaudit/) tool.

Open the tool, enter your website URL, and click “**Start Audit**.”

![Site Audit tool search bar](https://static.semrush.com/blog/uploads/media/c6/ee/c6eec9439853cfa7f8643261ca24911e/14f7dfcca0ae194602690216824764d4/2ANHhOcrdPCTkUs6S63Fx2ugkcmaZW4e_Bwt_TKpn4PIV3axGxdmoz1gHqZI6gf2AmcUg_rrC48hRnGn-iv0NvkBKBT_aCJVdodPM6VjOCW1z9EjBw6WxPls9hx9kFIoUwPUXxRH6cmQQ_nMDJCD0G4.png)

The tool will prompt you to [set up a project](https://www.semrush.com/kb/539-configuring-site-audit). After everything is configured, it’ll start auditing your site.

Once the audit is complete, go to the “HTTPS” section under the “Thematics Reports” module in the “Overview” tab.

And click on the “**View details**” button.

![“HTTPS” widget highlighted under "Thematic Reports" section in Site Audit's overview report](https://static.semrush.com/blog/uploads/media/7f/a9/7fa9841c7d7f7e98302c02d99b08ebb8/e0b9d905a23813dec70d7d8a3cb843c4/ZmXupYvZtaxgrsqDp5XT1nWmv6UyrMSuY-xFYe0E6kJa-KJ2Fy0f_zDJYoo0n0zWe98zAxj4D3q32VKTxPwb64J-2Wr1rsuMlEAY_JTld_bHVrK8ooSJporLIW3n1_F2ou7Zkx2uAXWho0oklVYsPXM.png)

You’ll see how your site is doing across multiple HTTPS-related issues.

!["HTTPS Implementation" report in Site Audit tool](https://static.semrush.com/blog/uploads/media/87/1c/871ce6587f1b287461b8963d21a1db30/046ed738fb685a01f5f9cd8ff7154d53/MyVWrI_l4Zk6Yk1oBQpNwjw6_U76yJOvuyl7XSSXSVJDx_YI_0SJQzBU1J8IENP-UWn4mD2lFeHshFVcUmLQStV0XZ_iOC4mZxRQsFaWgjPGVinxcNu6jXjUOXVNcnxSs1WjsmtBVxqx0kgUgNfsT10.png)

Issues are highlighted with the exclamation mark symbol and the orange outline.

You can also learn more about a particular issue by clicking on the “**Learn more**” link or the “**Why and how to fix it**” link under each item.

From there, you can learn how to fix any specific issues.

![Why and how to fix HTTPS issue on your site](https://static.semrush.com/blog/uploads/media/72/da/72daa38a68182b61569d21dba2481bfe/157f24cdfda4c55e49ab24da43834b0d/Ow0rsSeU6TIdWKhbFGSAgYE_DsxwsOh7YKK98gO_kBexWX6cGhivaVax_9S2lE4T63wrboh-s6D743g4IfHmjxS7wkOoquvGrvXm-LOUIj3RYwM4d5A5xFn5voFTM7GeZbwOBYL1-vTtmuQF-0g0tFA.png)

Now, back to the benefits of HTTPS.

### Compatibility with Browsers

Major browsers like Chrome, Firefox, Microsoft Edge, and Safari have supported HTTPS encryption and the key security protocols involved for many years now.

So, there’s no need to worry about your website visitors not being able to access an HTTPS site—unless they’re using extremely outdated software. Which virtually no one does.

## FAQs

To wrap things up, we’ll cover some frequently asked questions about HTTPS.

### What Does HTTPS Stand For?

HTTPS stands for hypertext transfer protocol secure. It's the secure, encrypted version of the standard HTTP web protocol.

### Is HTTPS Better Than HTTP?

HTTPS is far superior to regular, unencrypted HTTP.

HTTPS connections are encrypted through SSL/TLS certificates. This means HTTPS ensures visitors connect to the real website and that their data is secure from hackers.

HTTP has no encryption at all. So, it leaves websites and visitors vulnerable to attacks.

### What Does the ‘S’ in HTTPS Stand For?

The "S" in HTTPS stands for secure. It differentiates the encrypted HTTPS protocol from regular, unencrypted HTTP communication.

### What Port Does HTTPS Use?

HTTPS uses port 443 by default instead of HTTP's port 80.

Port 443 lets you access websites securely with encryption.

### How Do You Know if Your Site Uses HTTPS?

To confirm that your site is running on HTTPS, click on the tune icon next to the URL in the browser’s address bar and look for the padlock sign. And ensure the URL begins with “https://” rather than “http://.”

!["Connection is secure" padlock next to the "semrush.com" in the browser’s address bar](https://static.semrush.com/blog/uploads/media/37/2d/372de8168cca8fba57ac0513581435b3/de7ff08572fe906ea315d5fd415611ce/rYs59O05E6etyYbLkb79G5qGp6Ohr8kh5UiTuy06Ver4rEaQ3vJABnCrBCUDuN2TE57V87IuOwshJxWKlShMzzOGueY3a4k6pWwouB_Y0mqrjvBjbR4l96dqEWcyk6AfWLGZnZjk1IlKLFIy-eZScbM.png)

Additionally, modern browsers may provide a “Not secure” warning if a site is served over HTTP.

![“Not secure” warning reading "Your connection is not private" followed by an explanation that attackers might be trying to steal your information](https://static.semrush.com/blog/uploads/media/d4/75/d475443aa76c1addd82983650a4890fb/499dca6449db2387fb98fbbda64bc934/Ec8f9a9lFjyVFTb8OXXYqBqfzSeSq69aobZ5mF__muHz6QYE0GmS-pl1tglDx0TgvyPNuG6M-YIFScPoiPcNBIQXIqLTZ9_k72TUnRwo94rJoa3zAmD6GaNhx4kGLk9sHDida32vYX0HwX9Nf1TXOWI.png)

### How Do You Check for HTTPS-Related Issues?

There are multiple tools that can help you find HTTPS-related issues on your website.

One option is [Site Audit](https://www.semrush.com/siteaudit/). It checks your site for 11 different HTTPS-related issues. And presents the results in a report like this:

!["HTTPS Implementation" issues overview in Site Audit tool](https://static.semrush.com/blog/uploads/media/87/1c/871ce6587f1b287461b8963d21a1db30/046ed738fb685a01f5f9cd8ff7154d53/MyVWrI_l4Zk6Yk1oBQpNwjw6_U76yJOvuyl7XSSXSVJDx_YI_0SJQzBU1J8IENP-UWn4mD2lFeHshFVcUmLQStV0XZ_iOC4mZxRQsFaWgjPGVinxcNu6jXjUOXVNcnxSs1WjsmtBVxqx0kgUgNfsT10.png)

## Next Steps

Now that you know what HTTPS is, how it works, and what benefits it offers, you might be wondering what to do next.

Try expanding your knowledge about HTTPS with these resources:

- [How to Redirect HTTP to HTTPS (+ Best Practices)](https://www.semrush.com/blog/redirect-http-to-https/)
- [A Complete Guide to Redirects](https://www.semrush.com/blog/redirects/)
