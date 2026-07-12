---
title: "HTML Link Code: How to Create Hyperlinks with HTML (+ 9 Examples)"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "html-link-code"
url: "https://www.semrush.com/blog/html-link-code/"
canonical: "https://www.semrush.com/blog/html-link-code/"
author: "Dana Nicole"
published: "2021-10-04T14:29:00+00:00"
updated: "2023-09-19T09:56:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2023_aging"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T16:56:24+00:00"
status_code: 200
html_hash: "7bf84048cb83e988a027f30dc7a5b3829acef3d38b0f4362743fa6fa06e767cc"
clean_word_count: 2299
clean_char_count: 15376
---
# HTML Link Code: How to Create Hyperlinks with HTML (+ 9 Examples)

HTML link code lets you turn elements on your website—like text and images—into clickable hyperlinks.

These hyperlinks help users navigate the web.

And when you use them correctly for internal links—links from one page on your site to another page on your site—they can provide SEO benefits, too.

This guide shows you how to code a variety of HTML links. And how to style your links with simple CSS.

Let’s get started.

## What Is a Hyperlink?

A hyperlink, often called a link, is a reference linking one resource to another. It includes a clickable element like a word, phrase, image, or icon.

Clicking a hyperlink initiates an action. Like taking users to a different webpage. Or launching a phone call.

And coding your own hyperlinks is easy. As long as you understand the syntax of an [anchor element](https://www.semrush.com/blog/html-anchor/) (also known as an [<a> tag](https://www.semrush.com/blog/html-a-tag/)).

## Anchor Element Syntax

Anchor elements have four components:

1. **An opening tag:** This is the start of the anchor element and signifies the beginning of the link element
2. **Tag attributes + attribute values:** Within the opening tag, you can include different attributes. Attributes provide extra information, like how the link should behave or where it should take users. (We’ll dive into different attributes later on.)
3. **Anchor text or other content:** This is the content users click
4. **A closing tag:** This signifies the end of the link element

Let’s tie all four points together with a simple example. The below example uses an [href attribute](https://www.semrush.com/blog/ahref-link). It specifies the destination of the link—in this case, Semrush’s homepage.

![An example of using an href attribute](https://static.semrush.com/blog/uploads/media/d3/31/d331b86b8414a4fea858c7ed8e69637d/rR9ff5HDVozcI5ixhwfrTwi3nuncwjPwmaXTHJxfDQ3K62q15V-7Iw3fFmylpULXGfbqTk7oZ-A4ngeHw1LC4DToj5ajYkSKeThau_S3cZ93ZFONwPFSKwsujX2PQQL71iluXR2TTImK2Qqwl1xxZrQ.png)

The destination can also be a specific place on a webpage or a downloadable document.

***Note:** You can use one or more attributes in your anchor elements.*

## How to Code a Link in HTML

Let’s walk through how to code a simple link to your website’s homepage in HTML.

First, start with your anchor tag:

`<a> </a>`

Next, add your homepage’s URL using the href attribute:

`<a href="https://www.yourhomepage.com"> </a>`

Now, add the anchor text people will click to go to your link:

`<a href="https://www.yourhomepage.com">Visit our homepage</a>`

Your [anchor text](https://www.semrush.com/blog/anchor-text/) should be descriptive. So users will know where they’ll end up when they click your link.

Search engines also use anchor text to understand the page you’re linking to. So good anchor text can improve your SEO.

Take the below anchor text of “newsletter best practice” from ConvertKit. Readers and search engines know that if they visit the link, they’ll end up on a page about newsletter best practices.

![Anchor text of “newsletter best practice” from ConvertKit](https://static.semrush.com/blog/uploads/media/18/01/1801f38aeb965c0cf75e5755c51a3908/TzEmyq7JmMKXgHh0Hto8kbigHi1jplxQ94enUYv_j-b35cs82MsJKj27ZuAm8kirI0Ph_OQQk5UOsOBfh89e1CBpvUJ9i78PfzvnIohU4mOZ2eixfdN5HwAbG0kJMFs7wt9w_748JKn_evbrDKu_QZU.png)

Something non-descriptive like “click here” doesn’t give enough context. Making it confusing to people and search engines.

Semrush’s [Site Audit](https://www.semrush.com/siteaudit/) tool can check your website for links with non-descriptive anchor text.

First, set up your site audit by clicking the “**+ Create project**” button.

![“+ Create project” button highlighted](https://static.semrush.com/blog/uploads/media/ae/df/aedf8e4d88f7dce91a51a6b8d819526e/ESOQJ-b_3s97JiU7sXKdjK2Rh4uJN6Dhy4QoFttXWQ--DwLT7B7ydpBIuKFEjiwu414qn1iQlNAtJJ5I6wD0BXcJgcgZeczdy1B5PCKl9MroRTWWQ5B-Fj8cXtnZYFtjglbBASCGD7Pr5OaOHYru3pU.png)

Enter your domain and give your project a name. Then click “**Create project**.”

!["Create project" window in Site Audit](https://static.semrush.com/blog/uploads/media/81/aa/81aa6f569fff76c8b7092cc69b3163d9/_8uDNTAWgkXMn6nys04Gyxrb6kjCgbpKHF56qlBDncOnMxFdY-XivwKMXx7m0lWcsVXc4qxJdBX3PtY2lFiBsjdYIhj9C18XkpaYlP0o_kOzPzc0JFdWiY4KPGDK1mAMJA_jLfqKnIBKDrbLbZ7kNmo.png)

Next, configure your settings. [This Site Audit configuration guide](https://www.semrush.com/kb/539-configuring-site-audit) gives you a detailed walkthrough if you need help.

![Site Audit configuration page](https://static.semrush.com/blog/uploads/media/d1/6b/d16b3cfb45880a42a588daa1a38ced22/jKqZcYTYmCovfG4ZVK3ZWCU7wvPeAE4G8bqsuTZMEKYmTtIGx6cUQomsUHRrkIlorLjsnyLxhysTkNKbf6ISbwb9p5TiW8M-Fg9m3wnCzUE5139AmjlmFEcasArK_qQ0sl-dn46M7JBwALyVfZxDHiQ.png)

Then, click “**Issues**” and search “descriptive.” This shows a report for links with non-descriptive anchor text:

![A report for links with non-descriptive anchor text in "Issues" tab](https://static.semrush.com/blog/uploads/media/a5/04/a50437ae75a2cf1d42569dccd81591fa/8jAVTlNcMyL9WT__Z0KGUCqM6dtCliv-7qM0ih3OR59S9hReL39O21PVXthapyE7BCjOJIRsWjCUltmVbqyJSpO4iVd3IcWTiRSer9ozh1reJL8Mzsg4uhpNhwAoZxfS6dJ3-vLyYsXCVrF2cZVusKQ.png)

Click the links to review a list of non-descriptive links and links with no anchor text.

Then, update the anchor text of the links listed to help users and search engines better understand what the linked pages are about.

Now that you know how to code a basic link, let’s dive into additional attributes and values you can add to your HTML link code.

## 1. Linking with Images and Media

You can make media like images or GIFs clickable by adding a source to your anchor tag:

`<a href="https://www.example.com"><img src="https://www.example.com/filename.jpg" alt="a description of the media"></a>`

Here, you include a link to the media (an image in this case) instead of anchor text.

In the above code:

- **src** stands for “source” and specifies the location/URL of your media
- **alt** contains the [alt text](https://www.semrush.com/blog/alt-text/)—descriptive text used by screen readers and displayed when an image doesn’t load—if using an image as a link (below)

![Alt text showing where the image didn’t load](https://static.semrush.com/blog/uploads/media/0a/56/0a56d9551919210103e46a09a95c1f44/fg516gCll5hhsPx1K1_Ofr37l9Qd4eaHkMB-Fo8IYngkziUzVOFXBOnRzbLU-pQdARoHKUlJQBLjcCIP7UHfDU15OfJgvAyi5dE_RwjsL7YmXOsbJVtc785BUD7EeJZpr0hyJU_SJas-1kz40_YL1bM.png)

## 2. Linking to Specific Page Sections (Anchor Links)

Anchor links—also called jump links—take users to a specific place on the page with this code:

`<a href="https://www.example.com/blog/#seo-tips">SEO tips</a>`

They help readers navigate the page better to find what they need (like a table of contents).

To start, label the anchor—the place the link will take the reader—by giving it an ID in the opening tag. Like this:

`<h2 id="seo-tips">`

You can assign an ID to any [HTML element](https://www.semrush.com/blog/html-tags-list/). In the example above, we assigned it to an <h2> heading tag.

Now, test the ID to make sure it works. Add the ID to the end of your URL with a hash like this:

![An example of a header ID "#seo-tips"](https://static.semrush.com/blog/uploads/media/30/ee/30eee925811c9b169d4693d7be72828a/RoRV21SC4Wdyf-EUgn0qfceQ_JKdECwA69KTPtjKYj3K3SHqEX3mzVXmlGgr437ZhBc_lF4YoPda4Z1qtT5FNfyq_YkFeDvyQ1vUxJDloQOJ0KLDbRasl0xPq9om8EXapkPNzLD749UcTO1nVNrHT30.png)

Paste the link in your browser's address bar. Press enter to ensure it directs you to the assigned ID location on the page.

If it works, you can add the link to the href attribute.

## 3. Opening Links in New Windows/Tabs

You can choose whether your links open in the same window or a new tab with the target attribute.

For the same window, use the target=”\_self” attribute value like this:

`<a href="https://www.example.com" target="_self">Anchor text</a>`

Links open in the same window by default. So, using “\_self” isn’t necessary. But it can help you clarify the intent of specific hyperlinks.

To open links in a new tab, replace “\_self” with “\_blank”:

`<a href="https://www.example.com" target="_blank">Anchor text</a>`

It’s usually best for links to open in the same tab for accessibility reasons.

## 4. Linking to Email Addresses

Adding the mailto value opens your user’s email provider when they click your link:

`<a href="mailto:mail@semrush.com">Email Us</a>`

For example, link to your support email so customers can easily submit their questions.

![Email pop-up to: mail@semrush.com](https://static.semrush.com/blog/uploads/media/e9/11/e91108725a766f3bbe7f6d9e208cc3c0/aDVU3Z8mxH_WDDBp2h6erPp_cn21NEW53o5AVPmKKNcXpB_6ZhXwYSJ5lUXgYElLQnAY_Da2WGU4DM-VcvPZxAHhP01KGwMRub1_eV3NamTH9uKQeye4zdhsLiw2Kj3KZUQFB_NHwSrBIBKmPfq3-hM.png)

Just make sure your anchor text indicates an email application will open from clicking the link. Something like “Email us” or “Send an email” conveys the message clearly.

This way, users won’t be caught off guard when an unexpected application opens.

## 5. Linking to Phone Numbers

### Initiate a Call

Linking a phone number initiates a call. You can link to a phone number using the tel value:

`<a href="tel:+1-123-456-7890">Call Us</a>`

### Initiate a Text Message

You can also initiate a text message by using the “sms” value:

`<a href="sms:123-456-7890">Send SMS</a>`

As with the email attribute, make sure the user knows a phone call or text message will initiate when clicked.

## 6. Creating Download Links

The HTML code for creating downloads is similar to linking to a URL and looks like this:

`<a href="https://www.example.com/path/to/file.pdf" download>Download the PDF (175kB) now</a>`

When users click the link, their device will automatically download the file.

When choosing which files to use for your links, keep a few things in mind:

- Include the file type in the anchor text so users know what they’re downloading
- Use file types that are widely supported so users don’t need additional software to open them
- Mention the file size so you user can determine if they have enough space for the file

## 7. Linking with Accessibility Attributes

The aria-label attribute lets you describe links to screen readers. Like this:

`<a href="https://www.example.com" aria-label="Read more about building a brand">Read more</a>`

It’s useful when the anchor text isn’t descriptive.

For example, let’s say you display snippets of content and include a “read more” link:

![An example of a “Read more” link](https://static.semrush.com/blog/uploads/media/90/8d/908ddf9f8ddec2192915ff055381ca90/fWuSc6qsvyUle8wz7jzIV3U6Cfzk0r0t2ZPNVHO_mniwTtxpLE9UDmmq8DMH8ERdGn-0ph4EkFifwe34gVneRA2g-5Jz6Ggi15QjizX6CsNHBiLbzylVxp9NP3LD-d3QZ768Z9M8kSeGX9fIUvEWcmI.png)

With the “aria-label” you can add more context behind the “read more” link.

This way, people who use screen readers will know what the link is for.

## 8. Linking with Title Attributes

The title attribute shows text when users hover over a link:

![Hovering over a link shows text](https://static.semrush.com/blog/uploads/media/0c/c7/0cc737518c1a0e3191d2062276821f44/bcRAS5Vj5agTFTR0SydooVAZQtDYPKhQcjey4q9E1XiUFIcKT_yojGdSHrnYiY37_qQcAOXNTJe-ATRQ6ozDYBZv9XEZZO1w-Vm47TyVT_9sEd2TcaiWDKdKZmpqI8JaCZnHw8XvT3jeOnytK8249js.png)

And you get this text by adding in the title attribute:

`<a href="https://www.example.com" title="Read more about this topic by clicking this link">Anchor text</a>`

Use it to give additional context to your links.

For example, tell users where they’ll end up if they click the link. In this example, the title text could say something like, “click this link for an in-depth guide on this topic at www.example.com.”

## 9. Adding Relationships to Your Links

Adding a relationship to your links helps search engines and browsers understand the connection between the linked document and the current one.

For example, if you collaborated with another business, you’d add the rel=”sponsored” attribute value to your anchor element, like this:

`<a href="https://www.example.com" rel="sponsored">Anchor text</a>`

This tells search engines that the link is part of an advertising/sponsorship collaboration.

Here are some other common relationship attributes:

- **[nofollow](https://www.semrush.com/blog/nofollow-links):** Instructs search engines to ignore the link for search ranking purposes. Use when you're linking to content that you don't necessarily endorse or when you want to prevent search engines from passing link equity to the linked page.
- **noopener:** A security measure that prevents the opened page from accessing information from the original page. Use when you use the target=”\_blank” attribute value. It helps protect your site from potential security vulnerabilities.
- **noreferrer:** Stops browsers from sending the original page’s address as a referrer. Use when you don’t want the linked page to track referral traffic from your site.

## Styling and Designing Links with CSS

With CSS, you can style your links to match your brand by changing their colors and design.

CSS stands for cascading style sheets. It’s a stylesheet language that tells web browsers how to display web documents written in markup languages like HTML.

We’ll discuss two ways to edit the CSS:

1. Inline CSS
2. An external CSS file

### Inline CSS

Inline CSS lets you add styling right into the HTML code for a single element.

Just add a style attribute. Like this:

`<a href="https://www.example.com" style="color: red;">Anchor text</a>`

In this code, we use “style” to add color.

You can change the color using:

- Color keywords (like red)
- HEX codes
- RGB and RGBA values
- HSL values

If you want to remove the hyperlink’s underline, you can use the “text-decoration:none;” property. Like this:

`<a href="https://www.example.com" style="color: red; text-decoration: none;">Anchor text</a>`

Inline CSS works when you need to make one hyperlink look different than the rest.

For example, say your links are all green. But you have a downloadable file, and you want the link to be orange. For that, use inline CSS.

### External CSS File

An external CSS file lets you set global styles.

In your external CSS file, add this code:

`a {
color: red; /* Change this to your desired color */
text-decoration: none; /*Remove this line to keep the link’s underline */
}`

As with inline CSS, you can use color keywords, HEX codes, RGB and RGBA values, or HSL values to set your links’ color.

## Check Your Hyperlinks with Site Audit

To give users a great experience, make sure your hyperlinks work at all times.

This way, users won’t hit dead ends and can find what they need.

Use Semrush’s [Site Audit](https://www.semrush.com/siteaudit/) tool to check your website for broken links.

Click “**Issues**” and search “broken.”

![Site Audit tool finds broken links on your website](https://static.semrush.com/blog/uploads/media/66/3e/663eee3331fc7a846f761cdefe3e0b92/cv6VWsge3u8wxi8RNfhgve5mLo71axVMIQezsKLp6HvNH5iY6IQ1kzHO0pZLI6lC0ANhX6EqS7LcJ-DEymHzQ08wTlix1-6-ZaWYdSzeeg0gun5FHqsrljGQBzFuFjrTTuZQpemdXwCiOnkA1w2SDLA.png)

This shows you which links need your attention. Fix them so users can navigate your site—and click links to external sites—with ease.

Try Site Audit for free today.
