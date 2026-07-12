---
title: "What Is an Href Link? 4 Best Practices You Need to Know"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "ahref-link"
url: "https://www.semrush.com/blog/ahref-link/"
canonical: "https://www.semrush.com/blog/ahref-link/"
author: "Sergei Bezdorozhev, Christine Skopec"
published: "2021-06-10T17:02:00+00:00"
updated: "2025-07-03T11:24:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "time_sensitive_title"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T13:26:33+00:00"
status_code: 200
html_hash: "687169f464a9a75854fa8003633f03fe6941542d833b946bd1f972a8435e30cc"
clean_word_count: 1490
clean_char_count: 9968
---
# What Is an Href Link? 4 Best Practices You Need to Know

## What Is an Href Link?

An href link (also called an “a href link”) is an HTML attribute within an <a> tag that creates a clickable hyperlink and specifies the link’s URL.

Href links connect webpages, guide users, and help search engines discover content that might be used for search results.

Below is an example of an href link that creates the clickable text “Semrush.”

![Opening anchor tag includes the ahref link. Closing anchor tag appears after the anchor text.](https://static.semrush.com/blog/uploads/media/07/75/0775d06fa3ae6310e8c62c828831d79a/7a8763af86dde5127b9c5ce689d28f43/AD_4nXf0VLVALEbtuwnta04E2Xq2QEEHEWgHIlBhy92HC02YZLxqQXsCo-yFxxB050nJcpsRlFzsvzd-IIZDn_lJJgCw_ZgNjRXco5PQ26CVMJdvjVgvZGEyTcltE0YopFqeFcUaY2pkQA.png)

Href values can include:

- **Relative URLs (e.g., href="/about")**: Relative URLs are partial URLs that are often useful for [internal links](https://www.semrush.com/blog/internal-links/) (links to other pages on your site). They’re useful if you ever change your domain name because you won’t need to update your internal links.
- **Absolute URLs (e.g., href="https://example.com")**: Absolute URLs are full web addresses and are required when linking to external sites
- **Anchor links (e.g., href="https://example.com/#section")**: Anchor links jump to specific sections on a page that have CSS IDs (unique identifiers added to HTML elements). They help users skip to relevant content. Like links to subheadings shown in a table of contents.
- **Mailto links (e.g., href="mailto:info@example.com")**: Mailto links open a new email draft in the user's default email client. So they can contact you directly without copying and pasting your email address.
- **Tel links (e.g., href="tel:+1234567890")**: Tel links dial a phone number on supported devices and are ideal for mobile users who want to initiate a call with a single tap

Content management systems (like WordPress) have tools that eliminate the need to code href links manually.

But it’s helpful to know these details in case you want to make manual adjustments.

## Common Attribute-Value Combinations for <a> Tags

The <a> tag includes several attributes (instructions that control how a link behaves) and values (the specific settings for those instructions) that together define how a link works for users and search engines.

### target=“\_blank”

Using target=“\_blank” opens a link in a new browser tab, which can help keep users on your site for longer (when linking to an external site).

[Zachary Rischitelli](https://www.linkedin.com/in/zachary-rischitelli/), Founder and Managing Director at Real FiG Advertising + Marketing, recommends using this attribute for external links and when linking to larger files or documents. So readers don’t lose your page if they click away.

The World Wide Web Consortium (an organization that develops guidelines to help people build an accessible web) advises [adding warning text beside links](https://www.w3.org/WAI/WCAG21/Techniques/general/G201) that open in new tabs like this. Such as adding “(opens in new tab.)”

That way, users who have difficulty perceiving visual content won’t be surprised when they click your links.

Example:

`<a href="https://example.com" target="_blank">Visit Example (opens in new tab)</a>`

### rel=“nofollow”

A rel=“nofollow” attribute tells search engines not to follow the link or pass any SEO value (link equity) to the linked page.

[Dorian Menard](https://www.linkedin.com/in/dorianmenard/), Founder and Director at Search Scope, says,

> “We use this with user-generated comment sections or sponsored content to ensure we stay within Google's guidelines.”

Dorian also mentions that “rel=”nofollow” is good to use when linking to untrusted content where you don’t want to endorse the destination. Like if you need to cite a questionable source.

Example:

`<a href="https://example.com" rel="nofollow">Visit Example</a>`

You can also use rel=”UGC” and rel=”sponsored” for linking to user-generated content like comments or sponsored content. These attributes are more specific and transparent for search engines.

### rel=“noopener”

The rel="noopener" attribute-value combination is a security feature that prevents pages opened in new tabs from interacting with the original page and helps protect users from potential security threats.

For example, say you accidentally link to a malicious site from a secure page where a user is logged in. And you don’t use rel="noopener."

Zachary clarifies you run some risks by doing so:

> “Without rel=”noopener,” a malicious site could change your page’s URL or run a script when the user interacts with it.”

And the original tab may no longer be safe when users return to it.

Because this type of attack only happens when links open in a new tab, rel="noopener" should always be used alongside target="\_blank."

Example:

`<a href="https://example.com" target="_blank" rel="noopener">Visit Example</a>`

### rel=“noreferrer”

Use rel="noreferrer" to prevent the destination site from seeing which URL traffic came from to maintain user and site privacy.

For example, say a user is reading an article about a specific anxiety disorder that’s mentioned in the URL and follows a link in the piece to a therapist’s website. Without rel="noreferrer" added, the external therapist site can see the full URL that referred the visitor.

That URL might not include personal details. But it can still reveal private health concerns, which may pose a potential privacy issue for users.

You might also use rel=”noreferrer” if you don’t want sites (like a competitor) to know you’ve linked to them.

Example:

`<a href="https://example.com" target="_blank" rel="noreferrer">Visit Example</a>`

## 4 Best Practices for Href Links

Follow these best practices for href links to ensure your hyperlinks work properly.

### 1. Use Correct Syntax

Using the correct syntax ensures your href links work as intended, so search engines and users find the information they need.

Here are the main steps to build an href link using proper syntax:

1. Start the a href link with “<a”
2. Add correctly formatted attributes inside the start tag (e.g., href="<https://example.com>")
3. Leave a space before each anchor tag attribute (e.g., <a href=”https://example.com” target="\_blank">, not <a href="https://example.com"target="\_blank">)
4. Close the start tag with > (e.g., <a href="https://example.com">)
5. Add your anchor content to form the clickable part of the link (e.g., <a href="https://example.com">Visit our site</a>)
6. End the tag with </a>

### 2. Use Descriptive Anchor Text

[Anchor text](https://www.semrush.com/blog/anchor-text/) is the clickable text that helps search engines and users understand what the linked page is about.

![The clickable text, or anchor text, in this example is "services" while the target link is "www.domain.com/services."](https://static.semrush.com/blog/uploads/media/5b/e7/5be7532af9aac712c57bee1d980f60b5/e938ee0a669a2c64bf216759445b961c/AD_4nXc9KGoVBB6IZMIv1I4ZRhnziK6YCZmLmKLalCii7IMB2B6q8iJ9A5n8af3fDGrvtj_U3wmI57yZpbq8DsDEU83gwpGL2kzOwl1ekbUDzh076bkVK5mEtOd6INunUYkhIB2noqU.png)

Instead of using generic text like “click here,” use descriptive text that helps users (and search engines) understand context about the linked page.

### 3. Limit the Number of Links on a Page

Including a thoughtful number of links helps people find the resources they need and provides a better user experience.

Whereas excessive links can make a page look spammy and potentially hurt your rankings.

Here’s an example from [Google](https://developers.google.com/search/docs/essentials/spam-policies?hl=en&visit_id=637920788399431426-4123737229&rd=1#link-spam) of what unnatural linking looks like:

![In Google's example, the phrases wedding rings, wedding, best ring, buy flowers, and wedding dress are all links within a three sentence span.](https://static.semrush.com/blog/uploads/media/49/9f/499f5cd3c791a88dae2064b45a2ef576/1aaec412ec42f97403cde80bc63d9e7a/AD_4nXeuwI4rAjbQANcdfPHpAGY2-JxQbcVvgXljjn2BrJuj08CCRoQCrWtch2lht7AG4oE9AYDyVOrV3YBhUMIoPcjP9wlTDHspWHd16kGxwpcwPXGGcpZ-J4WGTilsijklOVSkrJHHyw.png)

### 4. Audit Links Regularly

Regularly checking your href links ensures every path on your site leads somewhere useful.

And catching small errors can help you avoid broken links that lead visitors (and crawlers) to a dead end.

Run a quick general check with Semrush's [free SEO Checker](https://www.semrush.com/siteaudit/) to spot any obvious issues.

For full link issue detection across your site, use the Semrush Site Audit tool.

After setting it up, find the “Internal Linking” report and click “**View details**.”

![The internal linking report shows a score of 85%](https://static.semrush.com/blog/uploads/media/e4/04/e404a6de9b52563b03068f36d11b7a1b/2c1663b6cfa184f9d990c5a1d27a69a7/AD_4nXeBNjWCbF8Ro-IVCjuDHjp76C-WhTNTiiqzznEBjYF623g1EvjaghIsOOKZqkc6soyK0yQcIgdWW59nF8rYN6PfilRtWep_J3FXEWwV4WbFq6TABz0BuTJA9c7bR0kOkCl3F0Gd.png)

Then, look at the “Internal Link Issues” to see whether you have:

- [Broken links](https://www.semrush.com/blog/broken-link/) (links that point to a nonexistent destination)
- Too many on-page links (more than 3,000 links on a single page)
- Internal links with nofollow attributes
- Links with missing or non-descriptive anchor text

And many other issues.

Click “**Learn more**” or “**Why and how to fix it**” alongside any issue for more context.

Or click the “**# issues**” button to see the affected URLs.

![Internal Linking report shows broken internal links, page crawl depth, and more.](https://static.semrush.com/blog/uploads/media/c3/46/c346358597d961f63fb12aa4ebf94beb/c7fbe016a0c6f1ae89da02e56fbd1ef2/AD_4nXfCnoKE90nOs9Xn9BxI4lOiZkvwzx_aYoGJHIdbH02Blv1ZQbkJWF1GNfo6QLGm-qcMQQt1JPTf-uHcnNasx-PC8og3HuIzK1RRmVHA52gRbL4Psx41ufrS4UOYgBzYSsEcqn4pZA.png)

Try Site Audit today.
