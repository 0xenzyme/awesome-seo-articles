---
title: "Work smarter, not harder, with site health"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-09-work-smarter-not-harder-with-site"
url: "https://developers.google.com/search/blog/2011/09/work-smarter-not-harder-with-site"
canonical: "https://developers.google.com/search/blog/2011/09/work-smarter-not-harder-with-site"
author: "Susan Moskwa"
published: "2011-09-29T00:00:00+00:00"
updated: "2011-09-29T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:15:26+00:00"
status_code: 200
html_hash: "5642ee2f08161b487b16d97615b7f92891c5eba255cb4977db80985a99db97a7"
clean_word_count: 708
clean_char_count: 4097
---
# Work smarter, not harder, with site health

We consistently hear from webmasters that they have to prioritize their time. Some manage dozens
or hundreds of clients' sites; others run their own business and may only have an hour to spend on
website maintenance in between managing finances and inventory. To help you prioritize your
efforts, Webmaster Tools is introducing the idea of "site health," and we've redesigned the
Webmaster Tools home page to highlight your sites with health problems. This should allow you to
easily see what needs your attention the most, without having to click through all of the reports
in Webmaster Tools for every site you manage.

Here's what the new home page looks like:

![Webmaster tools dashboard showing all the sites in the user's account](/static/search/blog/images/archived_1_home page.png)

You can see that sites with health problems are shown at the top of the list. (If you prefer, you
can always switch back to listing your sites alphabetically.) To see the specific issues we
detected on a site, click the site health icon
![](/static/search/blog/images/archived_1_warning-icon.png)
or the "Check site health" link next to that site:

![The site health popup provides critical information about an individual site](/static/search/blog/images/archived_1_health-popup.png)

This new home page is currently only available if you have 100 or fewer sites in your Webmaster
Tools account (either verified or unverified). We're working on making it available to all
accounts in the future. If you have more than 100 sites, you can see site health information at
the top of the Dashboard for each of your sites.

Right now we include three issues in your site's health check:

1. Have we detected malware on the site?
2. Have any important pages been removed via our
   [URL removal tool](https://www.google.com/support/webmasters/bin/answer.py?answer=164734)?
3. Are any of your important pages blocked from crawling in robots.txt?

You can click on any of these items to get more details about what we detected on your site. If
the site health icon and the "Check site health" link don't appear next to a site, it means that
we didn't detect any of these issues on that site (congratulations!).

A word about "important pages": as you know, you can get a comprehensive list of all URLs that
have been removed by going to *Site configuration >
Crawler access > Remove URL*; and
you can see all the URLs that we couldn't crawl because of robots.txt by going to
*Diagnostics > Crawl errors
> Restricted by robots.txt*. But since webmasters often
block or remove content on purpose, we only wanted to indicate a potential site health issue if we
think you may have blocked or removed a page you didn't mean to, which is why we're focusing on
"important pages." Right now we're looking at the number of clicks pages get (which you can see in
*Your site on the web > Search queries*) to determine
importance, and we may incorporate other factors in the future as our site health checks evolve.

Obviously these three issues—malware, removed URLs, and blocked URLs—aren't the only things that
can make a website "unhealthy;" in the future we're hoping to expand the checks we use to
determine a site's health, and of course there's no substitute for your own good judgment and
knowledge of what's going on with your site. But we hope that these changes make it easier for you
to quickly spot major problems with your sites without having to dig down into all the data and
reports.

After you've resolved any site health issues we've flagged, it will usually take several days for
the warning to disappear from your Webmaster Tools account, since we have to recrawl the site, see
the changes you've made, and then process that information through our Web Search and Webmaster
Tools pipelines. If you continue to see a site health warning for that site after a week or so,
the issue may not have been resolved. You can ask for help tracking it down in our
[Webmaster Help Forum](https://support.google.com/webmasters/community)
and let us know what you think!
