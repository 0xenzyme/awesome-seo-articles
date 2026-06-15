---
title: "A new tool to disavow links"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2012-10-a-new-tool-to-disavow-links"
url: "https://developers.google.com/search/blog/2012/10/a-new-tool-to-disavow-links"
canonical: "https://developers.google.com/search/blog/2012/10/a-new-tool-to-disavow-links"
author: "Jonathan Simon"
published: "2012-10-16T00:00:00+00:00"
updated: "2012-10-16T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T13:20:12+00:00"
status_code: 200
html_hash: "26aea6cfc1a6e59ddaa91caa93fe34c0a24ec0769ea2acbb1fa0ab2f53e89909"
clean_word_count: 1732
clean_char_count: 10042
---
# A new tool to disavow links

Today we're introducing a tool that enables you to disavow links to your site. If you've been
notified of a manual spam action based on "unnatural links" pointing to your site, this tool can
help you address the issue. If you haven't gotten this notification, this tool generally isn't
something you need to worry about.

First, a quick refresher. Links are one of the most well-known signals we use to order search
results. By looking at the links between pages, we can get a sense of which pages are reputable
and important, and thus more likely to be relevant to our users. This is the basis of
[PageRank](https://en.wikipedia.org/wiki/PageRank),
which is one of more than 200 signals we rely on to determine rankings. Since PageRank is so
well-known, it's also a target for spammers, and we fight linkspam constantly with algorithms and
by taking manual action.

If you've ever been caught up in linkspam, you may have seen a message in Webmaster Tools about
"unnatural links" pointing to your site. We send you this message when we see evidence of
[paid links](/search/docs/essentials/spam-policies#link-spam), link exchanges, or other
[link schemes](/search/docs/essentials/spam-policies#link-spam)
that violate our
[quality guidelines](/search/docs/essentials/spam-policies).
If you get this message, we recommend that you remove from the web as many spammy or low-quality
links to your site as possible. This is the best approach because it addresses the problem at
the root. By removing the bad links directly, you're helping to prevent Google (and other search
engines) from taking action again in the future. You're also helping to protect your site's
image, since people will no longer find spammy links pointing to your site on the web and jump
to conclusions about your website or business.

If you've done as much as you can to remove the problematic links, and there are still some
links you just can't seem to get down, that's a good time to visit our new
[Disavow links](https://www.google.com/webmasters/tools/disavow-links-main)
page. When you arrive, you'll first select your site.

![](/static/search/blog/images/archived_1_img1.png)

You'll then be prompted to upload a file containing the links you want to disavow.

![](/static/search/blog/images/archived_1_img2.png)

The format is straightforward. All you need is a plain text file with one URL per line. An
excerpt of a valid file might look like the following:

```
domain:spamdomain1.com
https://www.spamdomain2.com/contentA.html
https://www.spamdomain2.com/contentB.html
https://www.spamdomain2.com/contentC.html
```

In this example, lines that begin with a pound sign (#) are considered comments and Google
ignores them. The `domain:` tag indicates that you'd like to disavow links from all
pages on a particular site (in this case, "spamdomain1.com"). You can also request to disavow
links on specific pages (in this case, three individual pages on spamdomain2.com). We currently
support one disavowal file per site and the file is shared among site owners in Webmaster
Tools. If you want to update the file, you'll need to download the existing file, modify it,
and upload the new one. The file size limit is 2MB.

One great place to start looking for bad links is the "Links to Your Site" feature in Webmaster
Tools. From the home page, select the site you want, navigate to
Traffic
> Links to Your Site
> Who links the most
> More, then click one of the
download buttons. This file lists pages that link to your site. If you click "Download latest
links," you'll see dates as well. This can be a great place to start your investigation, but be
sure you don't upload the entire list of links to your site—you don't want to disavow all
your links!

To learn more about the feature, check out our
[Help Center](https://support.google.com/webmasters/bin/answer.py?answer=2648487),
and we'd welcome your comments and questions in our
[forum](https://support.google.com/webmasters/threads?hl=en&thread_filter=(category:search_console)).
You'll also find a video about the tool and a quick Q&A below.

We would reiterate that we built this tool for advanced webmasters only. We don't recommend using
this tool unless you are sure that you need to disavow some links to your site and you know
exactly what you're doing.

**Q: Will most sites need to use this tool?**
A: No. The vast, vast majority of sites do not need to use this tool in any way. If you're not
sure what the tool does or whether you need to use it, you probably shouldn't use it.

**Q: If I disavow links, what exactly does that do? Does Google definitely ignore them?**
A: This tool allows you to indicate to Google which links you would like to disavow, and Google
will typically ignore those links. Much like with
[`rel="canonical"`](/search/docs/crawling-indexing/consolidate-duplicate-urls),
this is a strong suggestion rather than a command - Google reserves the right to trust our own
judgment for corner cases, for example - but we will typically use that indication from you when
we assess links.

**Q: How soon after I upload a file will the links be ignored?**
A: We need to recrawl and reindex the URLs you disavowed before your disavowals go into effect,
which can take multiple weeks.

**Q: Can this tool be used if I'm worried about "negative SEO"?**
A: The primary purpose of this tool is to help clean up if you've hired a bad SEO or made
mistakes in your own link-building. If you know of
[bad link-building](/search/docs/essentials/spam-policies#link-spam)
done on your behalf (for example, paid posts or paid links that pass PageRank), we recommend that
you contact the sites that link to you and try to get links taken off the public web first. You're
also helping to protect your site's image, since people will no longer find spammy links and jump
to conclusions about your website or business. If, despite your best efforts, you're unable to
get a few backlinks taken down, that's a good time to use the Disavow Links tool.

In general, Google works hard to prevent other webmasters from being able to harm your ranking.
However, if you're worried that some backlinks might be affecting your site's reputation, you can
use the Disavow Links tool to indicate to Google that those links should be ignored. Again, we
build our algorithms with an eye to preventing negative SEO, so the vast majority of webmasters
don't need to worry about negative SEO at all.

**Q: I didn't create many of the links I'm seeing. Do I still have to do the work to clean up
these links?**
A: Typically not. Google normally gives links appropriate weight, and under normal circumstances
you don't need to give Google any additional information about your links. A typical use case for
this tool is if you've done link building that violates our
[quality guidelines](/search/docs/essentials/spam-policies),
Google has sent you a warning about
[unnatural links](/search/blog/2012/07/new-notifications-about-inbound-links), and
despite your best efforts there are some links that you still can't get taken down.

**Q: I uploaded some good links. How can I undo uploading links by mistake?**
A: To modify which links you would like to ignore, download the current file of disavowed links,
change it to include only links you would like to ignore, and then re-upload the file. Please
allow time for the new file to propagate through our crawling/indexing system, which can take
several weeks.

**Q: Should I create a links file as a preventative measure even if I haven't gotten a
notification about unnatural links to my site?**
A: If your site was affected by the
[Penguin algorithm](https://insidesearch.blogspot.com/2012/04/another-step-to-reward-high-quality)
update and you believe it might be because you built spammy or low-quality links to your site,
you may want to look at your site's backlinks and disavow links that are the result of
[link schemes that violate Google's guidelines](/search/docs/essentials/spam-policies#link-spam).

**Q: If I upload a file, do I still need to file a reconsideration request?**
A: Yes, if you've received notice that you have a manual action on your site. The purpose of the
Disavow Links tool is to tell Google which links you would like ignored. If you've received a
message about a manual action on your site, you should clean things up as much as you can (which
includes taking down any spammy links you have built on the web). Once you've gotten as many
spammy links taken down from the web as possible, you can use the Disavow Links tool to indicate
to Google which leftover links you weren't able to take down. Wait for some time to let the
disavowed links make their way into our system. Finally, submit a reconsideration request so the
manual webspam team can check whether your site is now within Google's quality guidelines, and
if so, remove any manual actions from your site.

**Q: Do I need to disavow links from example.com and example.co.uk if they're the same company?**
A: Yes. If you want to disavow links from multiple domains, you'll need to add an entry for each
domain.

**Q: What about www.example.com vs. example.com (without the "www")?**
A: Technically these are different URLs. The disavow links feature tries to be granular. If
content that you want to disavow occurs on multiple URLs on a site, you should disavow each URL
that has the link that you want to disavow. You can always disavow an entire domain, of course.

**Q: Can I disavow something.example.com to ignore only links from that subdomain?**
A: For the most part, yes. For most well-known hosting services that are available without payment
(for example, wordpress.com, blogspot.com, tumblr.com, and many others), disavowing
"`domain:something.example.com`" will disavow links only
from that subdomain. If a hosting service is very new or rare, we may interpret this as a request
to disavow all links from the entire domain. But if you list a subdomain, most of the time we will
be able to ignore links only from that subdomain.
