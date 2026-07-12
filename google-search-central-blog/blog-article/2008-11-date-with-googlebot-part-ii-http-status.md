---
title: "Date with Googlebot, Part II: HTTP status codes and If-Modified-Since"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-11-date-with-googlebot-part-ii-http-status"
url: "https://developers.google.com/search/blog/2008/11/date-with-googlebot-part-ii-http-status"
canonical: "https://developers.google.com/search/blog/2008/11/date-with-googlebot-part-ii-http-status"
author: "As told to Chewy [Trewhella], Developer Advocate"
published: "2008-11-27T00:00:00+00:00"
updated: "2008-11-27T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:55:36+00:00"
status_code: 200
html_hash: "4c7084029099b62194220ee40bbdd71a84c4f01177f98630a70d83bf85982dc5"
clean_word_count: 1505
clean_char_count: 8607
---
# Date with Googlebot, Part II: HTTP status codes and If-Modified-Since

Our
[date with Googlebot](/search/blog/2008/03/first-date-with-googlebot-headers-and)
was so wonderful, but it's hard to tell if we, the websites, said the right thing. We returned
`301` permanent redirect, but should we have responded with `302` temporary
redirect (so he knows we're playing hard to get)? If we sent a few new `404` errors,
will Googlebot ever call our site again? Should we support the header
`If-Modified-Since`? These questions can be confusing, just like young love. So
without further ado, let's ask the expert, Googlebot, and find out how they judged our response
(code).

![googlebot](/static/search/blog/images/import/d39ebf33ff9c3bae091f198064dc1961.jpg)

---

> Dearest Googlebot,
> Recently, I did some spring cleaning on my site and deleted a couple of old, orphaned pages.
> They now return the `404` "Page not found" code. Is this ok, or have I confused you?
>
> Frankie O'Fore

Dear Frankie,

`404` errors are the standard way of telling me that a page no longer exists. I won't
be upset—it's normal that old pages are pruned from websites, or updated to fresher content.
Most websites will show a handful of `404` errors in the Crawl Diagnostics over at
Webmaster Tools. It's really not a big deal. As long as you have good site architecture with
links to all your indexable content, I'll be happy, because it means I can find everything I need.

But don't forget, it's not just me who comes to your website—there may be humans seeing
these pages too. If you've only got a very simple '404 page not found' message, visitors who
aren't as savvy could be baffled. There are lots of ways to make your `404` page more
friendly; a quick one is our `404` widget over at Webmaster Tools, which will help
direct people to content which does exist. For more information, you can read the blog post. Most
web hosting companies, big and small, will let you customise your `404` page (and
other return codes too).

Love and kisses,
Googlebot

> Hey Googlebot,
> I was just reading your reply to Frankie above, and it raised a couple of questions.
> What if I have someone linking to a page that no longer exists? How can I make sure my visitors
> still find what they're after? Also, what if I just move some pages around? I'd like to better
> organise my site, but I'm worried you'll get confused. How can I help you?
>
> Yours hopefully,
> Little Jimmy

Hello Jimmy,

Let's pretend there are no anachronisms in your letter, and get to the meat of the matter.
Firstly, let's look at links coming from other sites. Obviously, these can be a great source of
traffic, and you don't want visitors presented with an unfriendly 'Page not found' message. So,
you can harness the power of the mighty redirect.

There are two types of redirect—`301` and `302`. Actually, there are
lots more, but these are the two we'll concern ourselves with now. Just like `404`,
`301` and `302` are different types of responses codes you can send to users
and search engine crawlers. They're both redirects, but a `301` is permanent and a
`302` is temporary. A `301` redirect tells me that whatever this page used
to be, now it lives somewhere else. This is perfect for when you're re-organising your site, and
also helps with links from offsite. Whenever I see a `301`, I'll update all references
to that old page with the new one you've told me about. Isn't that easy?

If you don't know where to begin with redirects, let me get you started. It depends on your
webserver, but here are some searches that may be helpful:

- **Apache:**
  [301 redirect apache](https://www.google.com/search?q=301+redirect+apache)
- **IIS:**
  [301 redirect iis](https://www.google.com/search?q=301+redirect+iis)

You can also check your manual, or the README files that came with your server.

As an alternative to a redirect, you can email the webmaster of the site linking to you and ask
them to update their link. Not sure what sites are linking to you? Don't despair—my human
co-workers have made that easy to figure out. In the "Links" portion of Webmaster Tools, you can
enter a specific URL on your site to determine who's linking to it.

My human co-workers also
[just released a tool](/search/blog/2008/10/webmaster-tools-shows-crawl-error)
which shows URLs linking to non-existent pages on your site.

Yours informationally,
Googlebot

> Darling Googlebot,
> I have a problem—I live in a very dynamic part of the web, and I keep changing my mind about
> things. When you ask me questions, I never respond the same way twice—my top threads change
> every hour, and I get new content all the time! You seem like a straightforward guy who wants
> straightforward answers. How can I tell you when things change without confusing you?
>
> Temp O'Rary

Dear Temp,

I just told little Jimmy that `301` redirects are the best way to tell a Googlebot
about your new address, but what you're looking for is a `302`.

Once you're indexed, it's the polite way to tell your visitors that your address is still the
right one, but that the content can temporarily be found elsewhere. In these situations, a
`302` (or the rarer `307` temporary redirect) would be better. For example,
orkut redirects from `https://orkut.com` to
`https://google.com/accounts/login?service=orkut`, which isn't a page that humans would
find particularly useful when searching for Orkut.

It's on a different domain, for starters. So, a `302` has been used to tell me that all
the content and linking properties of the URL shouldn't be updated to the target—it's just
a temporary page.

That's why when you search for orkut, you see orkut.com and not that longer URL.

Remember: simple communication is the key to any relationship.

Your friend,
Googlebot

> Captain Googlebot,
> I am the kind of site who likes to reinvent herself. I noticed that the links to me on my friends'
> sites are all to URLs I got rid of several redesigns ago! I had set up `301`
> redirects to my new URLs for those pages, but after that I `301` redirected the newer
> URLs to my next version. Now I'm afraid that if you follow their directions when you come to
> crawl, you'll end up following a string of `301` redirects so long that by the end you
> won't come calling any more.
>
> Ethel Binky

Dear Ethel,
It sounds like you have set up some URLs that redirect to more redirects to... well, goodness! In
small amounts, these "repeat redirects" are understandable, but it may be worth considering why
you're using them in the first place. If you remove the `301` redirects in the middle
and send me straight to the final destination on all of them, you'll save the both of us a bunch
of time and HTTP requests. But don't just think of us. Other people get tired of seeing that same
old 'contacting.... loading ... contacting...' game in their status bar.

Put yourself in their shoes—if your string of redirects starts to look rather long, users
might fear that you have set them off into an infinite loop! Bots and humans alike can get
scared by that kind of "eternal commitment." Instead, try to get rid of those chained redirects,
or at least keep 'em short. Think of the humans!

Yours thoughtfully,
Googlebot

> Dear Googlebot,
> I know you must like me—you even ask me for unmodified files, like my college thesis that
> hasn't changed in 10 years. It's starting to be a real hassle! Is there anything I can do to
> prevent your taking up my lovely bandwidth?
>
> Janet Crinklenose

Janet, Janet, Janet,
It sounds like you might want to learn a new phrase— `304 (Not Modified)`. If
I've seen a URL before, I insert an `If-Modified-Since` in my request's header. This
line also includes an HTTP-formatted date string. If you don't want to send me yet another copy of
that file, stand up for yourself and send back a normal HTTP header with the status
`304 (Not Modified)`! I like information, and this qualifies too. When you do that,
there's no need to send me a copy of the file—which means you don't waste your bandwidth,
and I don't feel like you're palming me off with the same old stuff.

You'll probably notice that a lot of browsers and proxies will say `If-Modified-Since`
in their headers, too. You can be well on your way to curbing that pesky bandwidth bill.

Now go out there and save some bandwidth!
Good ol' Googlebot

---

Googlebot has been so helpful! Now we know how to best respond to users and search engines. The
next time we get together, though, it's time to sit down for a good long heart-to-heart with the
robot (Date with Googlebot: Part III, is coming soon!).
