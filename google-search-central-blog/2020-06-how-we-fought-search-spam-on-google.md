---
title: "How we fought Search spam on Google - Webspam Report 2019"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2020-06-how-we-fought-search-spam-on-google"
url: "https://developers.google.com/search/blog/2020/06/how-we-fought-search-spam-on-google"
canonical: "https://developers.google.com/search/blog/2020/06/how-we-fought-search-spam-on-google"
author: "Cherry Prommawin, Duy Nguyen"
published: "2020-06-09T00:00:00+00:00"
updated: "2020-06-09T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2020_very_old"
  - "news_or_research"
  - "time_sensitive_title"
  - "title_year_2019_before_2026"
fetched_at: "2026-06-14T13:36:56+00:00"
status_code: 200
html_hash: "fd64b148a40d594502b661dc288b44317754d17f8a2de3fdfa7d2bbc540b4ffe"
clean_word_count: 1380
clean_char_count: 8638
---
# How we fought Search spam on Google - Webspam Report 2019

![Googlebot presenting the 2019 webspam report](/static/search/blog/images/web-spam-report-2019.png)

Every search matters. That is why whenever you come to Google Search to find relevant and useful
information, it is our ongoing commitment to make sure users receive the highest quality results
possible.

Unfortunately, on the web there are some disruptive behaviors and content that we call "webspam"
that can degrade the experience for people coming to find helpful information. We have a number
of teams who work to prevent webspam from appearing in your search results, and it's a constant
challenge to stay ahead of the spammers. At the same time, we continue to engage with webmasters
to ensure they're following best practices and can find success on Search, making great content
available on the open web.

Looking back at last year, here's a snapshot of how we fought spam on Search in 2019, and how we
supported the webmaster community.

## Fighting Spam at Scale

With hundreds of billions of webpages in our index serving billions of queries every day,
perhaps it's not too surprising that there continue to be bad actors who try to manipulate
search ranking. In fact, we observed that **more than 25 Billion pages we discover each
day are spammy**. That's a lot of spam and it goes to show the scale, persistence, and
the lengths that spammers are willing to go. We're very serious about making sure that your
chance of encountering spammy pages in Search is as small as possible. Our efforts have helped
ensure that more than 99% of visits from our results lead to experiences without spam.

## Updates from last year

In 2018, we reported that we had reduced
[user-generated spam](/search/docs/advanced/guidelines/user-gen-spam) by 80%,
and we're happy to confirm that this type of abuse did not grow in 2019. Link spam continued to
be a popular form of spam, but our team was successful in containing its impact in 2019. More
than 90% of link spam was caught by our systems, and techniques such as paid links or link
exchange have been made less effective.

Hacked spam, while still a commonly observed challenge, has been more stable compared to
previous years. We continued to work on solutions to better detect and notify affected
webmasters and platforms and
[help them recover from hacked websites](/web/fundamentals/security/hacked).

## Spam Trends

One of our top priorities in 2019 was improving our spam fighting capabilities through machine
learning systems. Our machine learning solutions, combined with our proven and time-tested
manual enforcement capability, have been instrumental in identifying and preventing spammy
results from being served to users.

In the last few years, we've observed an increase in spammy sites with
[auto-generated](/search/docs/advanced/guidelines/auto-gen-content) and
[scraped content](/search/docs/advanced/guidelines/scraped-content)
with behaviors that annoy or harm searchers, such as fake buttons, overwhelming ads, suspicious
redirects and malware. These websites are often deceptive and offer no real value to people. In
2019, we were able to reduce the impact on Search users from this type of spam by more than 60%
compared to 2018.

As we improve our capability and efficiency in catching spam, we're continuously investing in
reducing broader types of harm, like scams and fraud. These sites trick people into thinking
they're visiting an official or authoritative site and in many cases, people can end up
disclosing sensitive personal information, losing money, or infecting their devices with
malware. We have been paying close attention to queries that are prone to scam and fraud and
we've worked to stay ahead of spam tactics in those spaces to protect users.

## Working with webmasters and developers for a better web

Much of the work we do to fight against spam is using automated systems to detect spammy
behavior, but those systems aren't perfect and can't catch everything. As someone who uses
Search, you can also help us fight spam and other issues by
[reporting spam on search](/search/docs/advanced/guidelines/report-spam),
[phishing](https://safebrowsing.google.com/safebrowsing/report_phish/) or
[malware](https://www.google.com/safebrowsing/report_badware/). We received nearly
230,000 reports of search spam in 2019, and we were able to take action on 82% of those reports
we processed. We appreciate all the reports you sent to us and your help in keeping search
results clean!

So what do we do when we get those reports or identify that something isn't quite right? An
important part of what we do is notifying webmasters when we detect something wrong with their
website. In 2019, we generated more than 90 million messages to website owners to let them know
about issues, problems that may affect their site's appearance on Search results and potential
improvements that can be implemented. Of all messages, about 4.3 million were related to
[manual actions](https://support.google.com/webmasters/answer/9044175), resulting
from violations of our Webmaster Guidelines.

And we're always looking for ways to better help site owners. There were many initiatives in
2019 aimed at improving communications, such as
[the new Search Console messages](/search/blog/2019/12/search-console-messages),
[Site Kit for WordPress sites](/search/blog/2019/10/site-kit-is-now-available-for-all)
or
[the Auto-DNS verification in the new Search Console](/search/blog/2019/09/auto-dns-verification).
We hope that these initiatives have equipped webmasters with more convenient ways to get their
sites verified and will continue to be helpful. We also hope this provides quicker access to
news and that webmasters will be able to fix webspam issues or hack issues more effectively and
efficiently.

While we deeply focused on cleaning up spam, we also didn't forget to keep up with the evolution
of the web and
[rethought how we wanted to
treat `"nofollow"` links](/search/blog/2019/09/evolving-nofollow-new-ways-to-identify). Originally introduced as a means to
help fight comment spam and annotate sponsored links, the `"nofollow"`
attribute has come a long way. But we're not stopping there. We believe it's time for it to
evolve even more, just as how our spam fighting capability has evolved. We introduced two new
link attributes, `rel="sponsored"` and `rel="ugc"`,
that provide webmasters with additional ways to identify to Google Search the nature of
particular links. Along with `rel="nofollow"`, we began treating these
as hints for us to incorporate for ranking purposes. We are very excited to see that these new
rel attributes were well received and adopted by webmasters around the world!

## Engaging with the community

As always, we're grateful for all the opportunities we had last year to connect with webmasters
around the world, helping them improve their presence in Search and hearing feedback. We
delivered more than 150 online office hours, online events and offline events in many cities
across the globe to a wide range of audience including SEOs, developers, online marketers and
business owners. Among those events, we have been delighted by
[the momentum behind our Webmaster Conferences](/search/blog/2019/09/join-us-at-webmaster-conference-in)
in 35 locations across 15 countries and 12 languages around the world, including the first
Product Summit version in Mountain View. While we're not currently able to host in-person
events, we look forward to more of these
[events](/search/events) and virtual
touchpoints in the future.

Webmasters continued to find solutions and tips on our
[Webmasters Help Community](https://support.google.com/webmasters/community)
with more than 30,000 threads in 2019 in more than a dozen languages. On YouTube, we
[launched #AskGoogleWebmasters](/search/blog/2019/08/you-askgooglewebmasters-we-answer)
as well as series such as
[SEO mythbusting](/search/blog/2019/06/a-new-series-on-seo-for-web-developers) to
ensure that your questions get answered and your uncertainties get clarified.

We know that our journey to better web with you is ongoing and we would love to continue this
with you in the year to come! Therefore, do keep in touch on
[Twitter](https://twitter.com/googlesearchc),
[YouTube](https://www.youtube.com/channel/UCWf2ZlNsCGDS89VBF_awNvA),
[blog](/search/blog),
[Help Community](https://support.google.com/webmasters/community) or see you in
person at one of
[our conferences](/search/events) near you!

![A cartoon image showing people high-fiving](/static/search/blog/images/web-spam-report-2019-footer.png)
