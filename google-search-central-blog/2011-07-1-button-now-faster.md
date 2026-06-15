---
title: "The +1 Button: Now Faster"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-07-1-button-now-faster"
url: "https://developers.google.com/search/blog/2011/07/1-button-now-faster"
canonical: "https://developers.google.com/search/blog/2011/07/1-button-now-faster"
author: "David Byttow"
published: "2011-07-26T00:00:00+00:00"
updated: "2011-07-26T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:14:03+00:00"
status_code: 200
html_hash: "fdc17882638f25efb9d59f693a3fc1be61d056c7754aa6b95bb34493734bf5ff"
clean_word_count: 508
clean_char_count: 3014
---
# The +1 Button: Now Faster

One of the
[10 things we hold to be true](https://www.google.com/about/corporate/company/tenthings)
here at Google is that fast is better than slow. We keep speed in mind in all things that we do,
and the +1 button is no exception. Since the button's
[launch](/search/blog/2011/06/add-1-to-help-your-site-stand-out), we have been hard at
work improving its load time. Today, we're proud to announce two updates that will make both the
+1 button and the page loading it, faster.

First, we've begun to roll out out a set of changes that will make the button render up to 3x
faster on your site. No action is required on your part, so just sit back, relax, and watch as
the button loads more quickly than before.

In addition to the improvements made to the button, we're also introducing a new asynchronous
snippet, allowing you to make the +1 experience even faster. The async snippet allows your web
page to continue loading while your browser downloads the +1 JavaScript. By loading these elements
in parallel, we're ensuring the HTTP request to get the +1 button JavaScript doesn't lead to an
increase in your page load time. For those of you who have already implemented the button, you'll
need to update the code to the new async snippet, and then you should see an overall improvement
in your page load time.

To generate the new async snippet, use our
[+1 Configuration Tool](https://www.google.com/webmasters/+1/button/).
Below, you'll find an example of the code, which should be included below the last tag on your
page for best performance.

```
<-- Place this tag where you want the +1 button to render ->
<g:plusone></g:plusone>
<!-- Place this tag after the last plusone tag->
<script> (function() {
var po = document.createElement('script'); po.type = 'text/javascript, po.async = true; po src="https://apis.google.com/js/plusone.js',
var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
})();
</script>
```

![The +1 tag generator in action](/static/search/blog/images/archived_async_2Bsnippet.png)

If you haven't already implemented the +1 button on your site, we're excited for your first
experience to be a fast one. This is a great opportunity to allow your users to recommend your
site to their friends, potentially bringing in more qualified traffic from Google search. To
those that already have the button, we hope that you enjoy the improvements in speed. Our team
will continue to work hard to enhance the +1 button experience as we know that "fast is better
than slow" is as true today as it's ever been.

If you have any questions, please join us in the
[Webmaster forum](https://support.google.com/webmasters/community/label?lid=1f91cc0e87a8ed93).
To receive updates about the +1 button, please subscribe to the
[Google Publisher Buttons Announce Group](https://groups.google.com/group/google-publisher-buttons/subscribe).
For advanced tips and tricks, check our
[Google Code](https://code.google.com/apis/+1button) site.
