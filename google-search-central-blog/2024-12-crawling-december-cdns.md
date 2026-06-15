---
title: "Crawling December: CDNs and crawling"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "2024-12-crawling-december-cdns"
url: "https://developers.google.com/search/blog/2024/12/crawling-december-cdns"
canonical: "https://developers.google.com/search/blog/2024/12/crawling-december-cdns"
author: "Martin Splitt, Gary Illyes"
published: "2024-12-24T00:00:00+00:00"
updated: "2024-12-24T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2024_watch"
  - "news_or_research"
fetched_at: "2026-06-14T13:44:27+00:00"
status_code: 200
html_hash: "3d3f1dd0e5c551b49bcd0f2deb6f35c268677ba09574d3e6bcf85dd6115719f7"
clean_word_count: 1996
clean_char_count: 12154
---
# Crawling December: CDNs and crawling

Content delivery networks (CDNs) are particularly well suited for decreasing latency of your
website and in general keeping web traffic-related headaches away. This is their primary purpose
after all: speedy delivery of your content even if your site is getting loads of traffic. The "D"
in CDN is for delivering or distributing the content across the world, so transfer times to your
users is also lower than just hosting in one data center somewhere. In this post we're going to
explore how to make use of CDNs in a way that improves crawling and users' experience on your
site, and we also look at some nuances of crawling CDN-backed sites.

## Recap: What is a CDN?

CDNs are basically an intermediary between your origin server (where your website lives) and the
end user, and serves (some) files for them. Historically,
**CDNs' biggest focus is caching**, meaning that once a user requested a URL from
your site, CDNs will store the contents of that URL in their caches for a time so your server
doesn't have to serve that file again for a while.

**CDNs can drastically speed up your site** by serving users from a location that's
close to them. Say, if a user in Australia is accessing a site hosted in Germany, a CDN will serve
that user from their caches in Australia, cutting down the roundtrip across the globe. Lightspeed
or not,
[the distance is still quite large](https://www.youtube.com/watch?v=gYqF6-h9Cvg).

And finally,
**CDNs are a fantastic tool to protect your site from being overloaded and some security threats**.
With the amount of global traffic CDNs manage, they can construct reliable traffic models to
detect traffic anomalies and block accesses that seem excessive or malicious. For example, on
October 21, 2024,
[Cloudflare's systems](https://blog.cloudflare.com/ddos-threat-report-for-2024-q3/)
autonomously detected and mitigated a 4.2
[Tbps](https://wikipedia.org/wiki/Data-rate_units#Terabit_per_second)
*(ed: that's a lot)* DDoS attack that lasted around a minute.

## How CDNs can help your site

You might have the fastest servers and the best uplink money can buy and you might not think you
need to speed up anything, but CDNs can save you money in the long run, especially if your site is
big:

- **Caching on the CDN**: If resources like media, JavaScript, and CSS, or even your
  HTML are served from a CDN's caches, your servers don't have to spend compute and bandwidth on
  serving those resources, reducing server load in the process. This usually also means that pages
  load faster in users' browsers, which
  [correlates with better conversions](https://www.thinkwithgoogle.com/_qs/documents/9757/Milliseconds_Make_Millions_report_hQYAbZJ.pdf).
- **Traffic flood protection**: CDNs are particularly good at identifying and
  blocking excessive or malicious traffic, letting your users visit your site even when
  misbehaving bots or no-good-doers would overload your servers.
  Besides flood protection, the same controls that are used to block bad traffic can also be used
  for blocking traffic that you simply don't want, be that certain crawlers, clients that fit in a
  certain pattern, or just trolls that keep using the same IP address. While you can do this on
  your server or firewall too, it's usually much easier to use a CDN's user interface.
- **Reliability**: Some CDNs can serve your site to users even if your site is down.
  This of course might only work for static content, but that might already be enough to ensure
  they don't take their business somewhere else.

In short, CDNs are your friend and if your site is large or you're expecting (or even already
receiving!) large amounts of traffic, you might want to find one that fits your needs based on
factors such as price, performance, reliability, security, customer support, scalability, future
expansion. Check with your hosting or CMS provider, to learn your options (and whether you already
use one).

## How crawling affects sites with CDNs

On the crawling front, CDNs can also be helpful, but they can cause some crawling issues (albeit
rarely). Stay with us.

### CDNs' effect on crawl rate

Our crawling infrastructure is designed to allow higher crawl rates on sites that are backed by a
CDN, which is inferred from the IP address of the service that's serving the URLs our crawlers are
accessing. This works well, at least most of the time.

Say, you start a stock photo site today and happen to have 1,000,007 pictures in... stock. You
launch your website with a landing page, category pages, and detail pages for all of your stuff
— so you end up with a lot of pages. We explain in our documentation on
[crawl capacity limit](/crawling/docs/crawl-budget#crawl-capacity-limit)
that while Google Search would like to crawl all of these pages as quickly as possible, crawling
should also not overwhelm your servers. If your server starts responding slowly when facing an
increased number of crawling requests, throttling is applied on Google's side to prevent your
server from getting overloaded. The threshold for this throttling is much higher when our crawling
infrastructure detects that your site is backed by a CDN, and assumes that it's fine to send more
simultaneous requests because your server most likely can handle it, thus crawling your webshop
faster.

However, on the first access of a URL the CDN's cache is "cold", meaning that since no one has
requested that URL yet, its contents weren't cached by the CDN yet, so your origin server will
still need serve that URL at least once to "warm up" the CDN's cache. This is very similar to
[how HTTP caching works](/search/blog/2024/12/crawling-december-caching), too.

In short, even if your webshop is backed by a CDN, your server will need to serve those 1,000,007
URLs at least once. Only after that initial serve can your CDN help you with its caches. That's a
significant burden on your "crawl budget" and the crawl rate will likely be high for a few days;
keep that in mind if you're planning to launch many URLs at once.

### CDNs' effect on rendering

As we explained in our first
[Crawling December blog post about resource crawling](/search/blog/2024/12/crawling-december-resources),
splitting out resources to their own hostname or a CDN hostname (`cdn.example.com`) may
allow our Web Rendering Service (WRS) to render your pages more efficiently. This comes with a
caveat though: this practice may negatively affect page performance due to the overhead of a
connection to a different hostname, so you need to carefully consider
[page experience](/search/docs/appearance/page-experience) with rendering performance.

If you back your main host with a CDN, then you avoid this problem: one hostname to query, and the
critical rendering resources are likely served from the CDN's cache so your server doesn't need to
serve them (and no hit on page experience).

In the end, choose the solution that works best for your business: have a separate hostname
(`cdn.example.com`) for static resources, back your main hostname with a CDN, or do
both. Google's crawling infrastructure supports either option without issues.

## When CDNs are overprotective

Due to the CDNs' flood protection and how crawlers, well, crawl, occasionally the bots that you do
want on your site may end up in your CDN's blocklist, typically in their Web Application Firewall
(WAF). This prevents crawlers from accessing your site, which ultimately may prevent your site
from showing up in search results. The block can happen in various ways, some more harmful for a
site's presence in Google's search results than others, and it can be tricky (or impossible) for
you to control since they happen on the CDN's end. For the purpose of this blog post we put them
in two buckets: hard blocks and soft blocks.

### Hard blocks

Hard blocks are when the CDN sends a response to a crawl request that's an error in some form.
These can be:

- **HTTP `503`/`429` status codes**: Sending
  [these status codes is the preferred way](/crawling/docs/troubleshooting/http-status-codes#5xx-server-errors)
  to signal a temporary blockage. It will give you some time to react to unintended blocks by the
  CDN.
- **Network timeouts**: Network timeouts from the CDN will cause the affected URLs to
  be removed from Google's search index, as these
  [network errors are considered terminal, "hard" errors](/crawling/docs/troubleshooting/dns-network-errors).
  Additionally they may also considerably affect your site's crawl rate because they signal our
  crawl infrastructure that the site is overloaded.
- **Random error message with an HTTP `200` status code**: Also known as
  [soft errors](/search/docs/crawling-indexing/troubleshoot-crawling-errors#soft-404-errors),
  this is particularly bad. If the error message is equated on Google's end to a "hard" error
  (say, an HTTP `500`), Google will remove the URL from Search. If Google couldn't
  detect the error messages as "hard" errors, all the pages with the same error message may be
  eliminated as duplicates from Google's search index. Since Google indexing has little incentive
  to request a recrawl of duplicate URLs, recovering from this may take more time.

### Soft blocks

A similar issue may pop up (pun very much intended) when your CDN shows those "are you sure you're
a human" interstitials.

![Crawley confused about being called a human](/static/search/blog/images/crawling-december-crawley-confused.png)

Our crawlers are in fact convinced that they're NOT human and they're not pretending to be one.
They just wanna crawl. However when the interstitial shows up, that's all they see, not your
awesome site. In case of these bot-verification interstitials, we strongly recommend sending a
clear signal in the form of a 503 HTTP status code to automated clients like crawlers that the
content is temporarily unavailable. This will ensure that the content is not removed from Google's
index automatically.

### Debugging blockages

In case of both hard and soft blockages, the easiest way to check if things are working correctly
is to use the
[URL Inspection tool in Search Console](https://support.google.com/webmasters/answer/9012289)
and observe the rendered image: if it shows your page, you're good; if it shows an empty page, an
error, or a page with a bot challenge, you might want to talk to your CDN about it.

Additionally, to help with these unintended blockages, Google, other search engines, and other
crawler operators publish
[our IP addresses](/search/docs/crawling-indexing/verifying-googlebot) to help you to
identify our crawlers and, if you feel that's appropriate, remove the blocked IPs from the WAF
rules, or even allowlist them. Where you can do this depends on the CDN you're using; fortunately
most CDNs and standalone WAFs have fantastic documentation. Here's some we could find with a
little searching (as of publication of this post):

- Cloudflare: <https://developers.cloudflare.com/bots/get-started/free/#visibility>
- Akamai: <https://www.akamai.com/products/bot-manager>
- Fastly: <https://www.fastly.com/products/bot-management>
- F5: <https://clouddocs.f5.com/bigip-next/20-2-0/waf_management/waf_bot_protection.html>
- Google Cloud: <https://cloud.google.com/armor/docs/bot-management>

If you need your site to show up in search engines, we strongly recommend checking whether the
crawlers you care about can access your site. Remember that the IPs may end up on a blocklist
automatically, without you knowing, so checking in on the blocklists every now and then is a good
idea for your site's success in search and beyond. If the blocklist is very long (not unlike this
blog post), try to look for just the first few segments of the IP ranges, for example, instead of
looking for `192.168.0.101` you can just look for `192.168`.

This was the last post in our
[Crawling December blog post series](/search/blog#crawling-december),
we hope you enjoyed them as much as we loved writing them. If you have... blah blah blah... you
know the drill.

---

## Want to learn more about crawling? Check out the entire Crawling December series:
