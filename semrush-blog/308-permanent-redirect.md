---
title: "308 Permanent Redirect: What It Means & When to Use It"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "308-permanent-redirect"
url: "https://www.semrush.com/blog/308-permanent-redirect/"
canonical: "https://www.semrush.com/blog/308-permanent-redirect/"
author: "Dana Nicole"
published: "2023-11-20T09:24:00+00:00"
updated: "2023-11-20T09:24:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2023_aging"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T13:17:53+00:00"
status_code: 200
html_hash: "526908cc1aae2648d2cecc5543809a60b8ca9adb467d2046010df929685f2d8d"
clean_word_count: 1557
clean_char_count: 11097
---
# 308 Permanent Redirect: What It Means & When to Use It

## What Is a 308 Permanent Redirect?

A 308 Permanent Redirect is an [HTTP response status code](https://www.semrush.com/blog/http-status-codes/)—a three-digit number sent by a web server in response to a client's request—that tells browsers and search engines that a resource has permanently moved to a new URL.

Other HTTP response status codes you might be familiar with include the [404 error](https://www.semrush.com/blog/what-does-error-404-not-found-mean/), which means the server can’t find the requested page.

As a user, it’s usually obvious when you encounter a 404 HTTP response status code. You’ll see an error page (like the one pictured below).

![404 error page from Upflex](https://static.semrush.com/blog/uploads/media/81/84/818466145e1aa1423a57639048b260b5/ae067dc2456eb7ef21c89771a58884a3/6StlegrDm5KHeHR-_URnWTnWFOJLoK_txXNibLrULZ3BWfrlWW6vTCp9FnvvR5-JVnEsW7BGrTQHA2Kh3qLYtm9bS7gN6IA6H8naesHALoN3QI5oGSNGTF3VZbMr3-XKiSBZ65OraeLM4aJOotNGIyA.png)

But you typically won’t notice a 308 HTTP response status code.

That’s because when you encounter a 308 Permanent Redirect, the browser redirects you to the correct URL automatically.

![An image showing a redirect from "Dog Toys 2010" to "Dog Toys 2022" page](https://static.semrush.com/blog/uploads/media/88/fc/88fcf77784b82b7fe7b0ece6915e4de6/c49a105fb003825a9d6a7597f07292d1/3OMWfDp7Dx06DdGgqcqb8zKCZP0H6Ea1yECxjYqZwEg5qhHD1mWa9zHlKWEeYGVb9OU5Tpb_P3oV_s844AUTg5XCWn2oHQv5CoG4_wuLge3m8cl7ZHuKcIglLWGgN_zvKWgAY724vs8ntfbIhqLjdcs.png)

And in terms of SEO, link equity—the value passed by links—and authority may be passed on to the new page as well.

## How to Check Your Website for 308 Permanent Redirects

To see if you have any 308 Permanent Redirects on your site, use Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool.

To start, [set up a new project](https://www.semrush.com/kb/539-configuring-site-audit) or click on the project you’d like to check your redirects for.

!["Create project" pop up window in Site Audit tool](https://static.semrush.com/blog/uploads/media/dc/ea/dcead57103d9e482e5f8d3bcfb02bb64/2d59bb75f6aac16b116954cfcab4636b/FpGIWZYA68zPs6ZD5U7R-k4tYGw6dtXiMRKYHGVRE-xlWisKDfVURjQ9sJk4hhT25rWaYzMdGlIbU9rnPSoJTFlH4ZpGvuWywIs32srhQ9r4yoLVWdOHACOpVAgSypSfHfH4pEIHIlBTLccRRl_8WGo.png)

After the audit loads, click the number beside “Redirects.”

!["Redirects" highlighted under Crawled Pages section](https://static.semrush.com/blog/uploads/media/2c/1b/2c1b8c80f6604035ca7859f5a81dc2e5/36632239d87d62637f345c7b63a74ce6/G3y919RFf9gMogLWK98onjiJRV7Oj7vkKR9A5ebCAESkVZ9i-KFW8CSElAD7qNrL6xyHebX5_YxNKcogDUYtemvbarJ-3U51dIBQfqZyekr4gZHCKgGaUx3ZMKnUZbGif8Czjo7r-o1ibv_a0KJTt3Y.png)

This report lists all your redirects, including their HTTP status codes.

![Redirects report in Site Audit tool](https://static.semrush.com/blog/uploads/media/63/c9/63c98a9a02b36f25b848ddbc87d9ab59/1153ecd278ecc8f13420911ac54a3e22/8TvuqPc8d3RAZuvr2t5SSbFJ-FYOAdwUWFVFzC05ct25RAOlbztd8hfwMuK3X3bjlEPPFftcWxYSF6VVqaVfwR4Q6P9-IQV_AH0EWf8g6QCxbBRql-uPcbMKMuOA_5FYKygGk0KPAHCq8jtNNyPYHIA.png)

Review this report and make note of which pages use 308 Permanent Redirects.

Later, we’ll go over when you should use a 308 Permanent Redirect. You can refer back to your Site Audit to ensure you’ve used the 308 properly.

## 308 vs. Other 3xx Redirects

A 3XX [redirect](https://www.semrush.com/blog/redirects/) is a type of HTTP status code that instructs browsers and search engines to go to a new URL.

Each 3XX redirect represents a specific type of redirect with distinct purposes. Which may include indicating whether the redirection is temporary or permanent.

A 3XX also determines if the browser can change the request method (POST/GET) upon redirection.

(We’ll go over POST and GET request methods in the next section.)

With that in mind, here’s what a few different 3XX redirects mean:

- **[301 Moved Permanently](https://www.semrush.com/blog/301-redirects/)****:** Signifies that a resource has been permanently relocated, and it allows for a conversion of the original request method from POST to GET. Search engines will update their links to the new resource.
- **[302 Found](https://www.semrush.com/blog/302-redirect/)****:** Indicates that a resource has been temporarily moved, and it advises maintaining the original request method of POST or GET. Search engines don’t update their links to the temporary resource.
- **307 Temporary Redirect****:** Specifies a temporary resource relocation and advises preserving the original request method of POST or GET. Search engines don’t update their links to the temporary resource.
- **308 Permanent Redirect****:** Conveys a permanent resource relocation and advises preserving the original request method of POST or GET. Search engines will update their links to the new resource.

![Different types of redirects and what they mean](https://static.semrush.com/blog/uploads/media/9f/9b/9f9bac9e540c233e3900ed7176a6a254/3ec8cde1556b2079ffb4b93132aa0d27/wU7BFzNeCc2ZzW93bqaU9NPEecGLO_HcwoxzvCHvWv8J6jcEAu0zjWd_vY5H9Ij9c3HIARKFEQ2BbyLkphkmDTwHd2IQXF4V36o_bPjF30V6l8-UjrI2lsKUx84NufZHiocx7jEGriGi4LjTTphquP0.png)

### 301 vs. 308 Permanent Redirects

301 and 308 redirects are both permanent redirects with one distinction—whether the browser can change the request method.

So, what does that mean?

Request methods, also known as HTTP request methods, are commands used to specify the desired action to perform on a resource.

Common HTTP request methods include POST and GET, as noted above in the different types of 3XX redirects.

The GET method retrieves data.

For example, when you enter a URL in your web browser and press “Enter,” your browser typically sends a GET request to the server that hosts the website.

The server then sends back the website. And your browser displays it.

The POST method submits data. It’s more secure than the GET method.

For example, when you fill out a form on a website and click a submit button, your browser sends a POST request to the server.

Then, the server processes the information you submitted (like your name and email address).

When you specify a 308 Permanent Redirect, you forbid the browser to change the HTTPS request method.

In other words, if the client made the original request using the POST method, the browser should continue to use the POST method when following the redirect.

Maintaining a POST request method is important if you want to secure and safeguard data, like login credentials. Or if you want to save data, like order information.

#### Which Redirect Is Better for SEO: 308 or 301?

Google’s John Mueller explains that Google generally treats 308 and 301 redirects the same (as long as you use a 308 to indicate a permanent move).

![John Mueller's reply to weather 308 redirects get treated the same as 301 redirects](https://static.semrush.com/blog/uploads/media/67/ec/67ec5770743bbb411b603987652b8569/3833b6fdb54fbdbd6c41a117a5a0a31b/ZI6ITpLM7GL6HZwv3oLc2zR5DNjrNiuYosxGITV9hqBj0wB3LcW2PA2THdqELYh0eez_2EG19YqiM3r-EZeKgcu5_JdmvfXBIbniye8RsYhEAcS4y627U5kBOKj_vCSrEZMrj11ma6azUFXgZkrU51o.png)

In [another post](https://twitter.com/JohnMu/status/1458090738185646097), he adds that 308s can be cleaner if you’re unsure which request the site gets:

![John Mueller's reply to why did 308 redirects become more popular](https://static.semrush.com/blog/uploads/media/43/59/4359954560c0e6ef1f79854723a62e89/f2535aca23b5d5e163b29ac5b9dc0788/JCcqEhx1eMUC6gpt76U6QcGrvfTXjiqbeHJWMuUoIdgvLA5PeaX-lnapjHJB7a4VsRF3nSsv_t4sdtapM6kWNBjUGz0Rr3FL0VrGGg3smIQanJ3M1vBE4QQiYMk2UGdsQX0MQH1bfoM8Sb3UhVTcKwg.png)

If you’re unsure which to use, here are a few examples of when a 308 Permanent Redirect is the right choice:

## When Should You Use a 308 Permanent Redirect?

You should use 308 Permanent Redirects when you want to maintain the original HTTP request method (like POST or GET) throughout a permanent redirect.

Here’s an example:

Imagine you have an ecommerce website. A user adds items to their shopping cart, and when they’re ready to complete their purchase, they click “check out.” The website uses the POST method to securely process and submit their order.

However, because the user isn’t logged in, you first want to redirect them to a login/registration page before they can proceed with the checkout.

To ensure items stay in the user's shopping cart throughout the login/registration process, you can implement a 308 to a login page.

This way, you can maintain the original POST request method.

Then, when the user successfully logs in or registers, your site directs them back to their shopping cart page, and their items remain in the cart. This ensures a seamless shopping experience.

![Shopping cart pages leading to a a login/registration page](https://static.semrush.com/blog/uploads/media/30/f8/30f828a2671ce4e39760c6a4e73bfa08/cb9fa1ce1371d6b20e171ef1a0dc1e5a/u2_GBQprwqSYK475mZQuHSyoXJsoOVCEvaxhHwjme8ecR2-ME_Pb5T3fMS4ugUSFZQ8nA53c-olzbSTRmFVThsHMo5Gtyp1y1iyHK_9EdFPyzawvYhO0ar0V0BMS_5ZXTRa2rLdYin6I9M__7bLAWZU.png)

In this example, a 308 preserves the original HTTP request method so the user doesn’t lose the items in their cart. If the site had a 301 redirect (and the request method was changed), the user might lose the items.

Another example of when to use a 308 is for registration pages.

Say users register to use your site. After users fill out their details, your website directs them to a confirmation page with the URL example.com/thank-you.

On the confirmation page, you tell the user to check their email and input the code they received to activate their account.

![A confirmation page, with "Please verify your email" message](https://static.semrush.com/blog/uploads/media/2b/df/2bdfe3f9680123e6e1cfe7e85bf4e20b/898939dd8a14dfb3c584860b52751e48/uGp_sXDyZxYD-lRnVTBVALD0ZjwCEuFCG7mmi4saG-oiPHiu_AOHNwu0FOGV7cFeDQKwlqH-fKl3BjTiyYDjvJB45t2ATvZ_wG-w7lZEmb-2geow6eYuohEKSmTB8BXdiEz4QBPUhqjkbNNHPfpDTLo.png)

Now, suppose you want to change the confirmation page’s URL from example.com/thank-you to example.com/confirmation.

To ensure the user’s registration data remains intact and transferable, you could use a 308 Permanent Redirect.

That way, the information (from when the user registered for your site) is preserved and transferred as your site directs users to the new confirmation page. And they can activate their accounts without running into any issues.

## Managing Your Redirects

Use [Site Audit](https://www.semrush.com/siteaudit/) to go through and make sure your site uses the proper redirect every time.

Pay attention to pages that process user information.

Like a login page. Or a shopping cart.

Make sure these pages use a 308 to ensure your site processes their data properly. And doesn’t lose it throughout the redirection.

Using the proper redirect for your pages ensures visitors end up on the right page with no interruptions.

And when you’ve used the right redirect, search engines can more easily understand and pass link equity to the new destination.
