---
title: "Are you a robot? Introducing \"No CAPTCHA reCAPTCHA\""
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2014-12-are-you-robot-introducing-no-captcha"
url: "https://developers.google.com/search/blog/2014/12/are-you-robot-introducing-no-captcha"
canonical: "https://developers.google.com/search/blog/2014/12/are-you-robot-introducing-no-captcha"
author: "Vinay Shet, Product Manager, reCAPTCHA"
published: "2014-12-03T00:00:00+00:00"
updated: "2014-12-03T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2014_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:25:46+00:00"
status_code: 200
html_hash: "18d0b091cec04adfae33ff87116bbaf9fba5b23f3f8c0600804975f737906fe2"
clean_word_count: 669
clean_char_count: 4234
---
# Are you a robot? Introducing "No CAPTCHA reCAPTCHA"

[reCAPTCHA](https://www.google.com/recaptcha) protects the websites
you love from spam and abuse. So, when you go online—say, for some last-minute holiday
shopping—you won't be competing with robots and abusive scripts to access sites. For years,
we've prompted users to confirm they aren't robots by asking them to read distorted text and type
it into a box, like this:

![](/static/search/blog/images/import/955d64dfbe32876956a44b890b23cbf7.png)

But, we figured it would be easier to just directly ask our users whether or not they are
robots—so, we did! We've begun rolling out a new API that radically simplifies the
reCAPTCHA experience. We're calling it the "No CAPTCHA reCAPTCHA" and this is how it looks:

![](/static/search/blog/images/import/725d5f8228341d55d83628a2bc1e789e.gif)

On websites using this new API, a significant number of users will be able to securely and easily
verify they're human without actually having to solve a CAPTCHA. Instead, with just a single
click, they'll confirm they are not a robot.

While the new reCAPTCHA API may sound simple, there is a high degree of sophistication behind
that modest checkbox. CAPTCHAs have long relied on the inability of robots to solve distorted
text. However,
[our research recently showed](https://googleonlinesecurity.blogspot.com/2014/04/street-view-and-recaptcha-technology.html)
that today's Artificial Intelligence technology can solve even the most difficult variant of
distorted text at 99.8% accuracy. Thus distorted text, on its own, is no longer a dependable test.

To counter this, last year we
[developed](https://googleonlinesecurity.blogspot.com/2013/10/recaptcha-just-got-easier-but-only-if.html)
an Advanced Risk Analysis backend for reCAPTCHA that actively considers a user's entire engagement
with the CAPTCHA—before, during, and after—to determine whether that user is a human. This enables
us to rely less on typing distorted text and, in turn, offer a better experience for users. We
talked about this in our
[Valentine's Day post](https://googleonlinesecurity.blogspot.com/2014/02/captchas-that-capture-your-heart.html)
earlier this year.

The new API is the next step in this steady evolution. Now, humans can just check the box and in
most cases, they're through the challenge.

## Are you *sure* you're not a robot?

However, CAPTCHAs aren't going away just yet. In cases when the risk analysis engine can't
confidently predict whether a user is a human or an abusive agent, it will prompt a CAPTCHA to
elicit more cues, increasing the number of security checkpoints to confirm the user is valid.

![](/static/search/blog/images/import/421de63595f33c14d8310ff9458e7aa1.png)

This new API also lets us experiment with new types of challenges that are easier for us humans to
use, particularly on mobile devices. In the example below, you can see a CAPTCHA based on a
classic
[Computer Vision](https://en.wikipedia.org/wiki/Computer_vision)
problem of image labeling. In this version of the CAPTCHA challenge, you're asked to select all of
the images that correspond with the clue. It's much easier to tap photos of cats or turkeys than
to tediously type a line of distorted text on your phone.

![](/static/search/blog/images/import/2121e5645b352c2ae6ea9fa6cff68b0c.png)
![](/static/search/blog/images/import/d59ea75fcad43b4e9850c089e16a2717.png)

## Adopting the new API on your site

As more websites adopt the new API, more people will see "No CAPTCHA reCAPTCHAs". Early adopters,
like [Snapchat](https://support.snapchat.com/login2?next=/),
[WordPress](https://wordpress.org/support/register.php),
[Humble Bundle](https://www.humblebundle.com/), and several others are
already seeing great results with this new API. For example, in the last week, more than 60% of
WordPress' traffic and more than 80% of Humble Bundle's traffic on reCAPTCHA encountered the No
CAPTCHA experience—users got to these sites faster. To adopt the new reCAPTCHA for your website,
[visit our site](https://www.google.com/recaptcha)
to learn more.

Humans, we'll continue our work to keep the Internet safe and easy to use. Abusive bots and
scripts, it'll only get worse—sorry we're (still) not sorry.
