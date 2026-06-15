---
title: "Googlebot and the 15 MB thing"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2022-06-googlebot-15mb"
url: "https://developers.google.com/search/blog/2022/06/googlebot-15mb"
canonical: "https://developers.google.com/search/blog/2022/06/googlebot-15mb"
author: "Gary Illyes"
published: "2022-06-28T00:00:00+00:00"
updated: "2022-06-28T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2022_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:40:37+00:00"
status_code: 200
html_hash: "3c7df5a5c20361967051d68fdd5c2a06c9a0fadc8639b20633f24979a427524a"
clean_word_count: 639
clean_char_count: 3859
---
# Googlebot and the 15 MB thing

Over the last few days we've received a great deal of questions about a recent update to
[our documentation about Googlebot](/search/docs/crawling-indexing/googlebot).
Namely, we've documented that Googlebot only ever "sees" the first 15
[megabytes](https://en.wikipedia.org/wiki/Megabyte#-_-) (MB)
when fetching
[certain file types](/search/docs/crawling-indexing/indexable-file-types).
This threshold is not new; it's been around for many years. We just added it to our documentation
because it might be helpful for some folks when debugging, and because it rarely ever changes.

This limit only applies to the
[bytes](https://en.wikipedia.org/wiki/Byte#;)) (content)
received for the initial request Googlebot makes, not the referenced resources within the page.

For example, when you open `https://example.com/puppies.html`, your browser will
initially download the bytes of the HTML file, and based on those bytes it might make further
requests for external JavaScript, images, or whatever else is referenced with a URL in the HTML.
Googlebot does the same thing.

**What does this 15 MB limit mean to me?**
Most likely nothing. There are
[very few pages](https://twitter.com/paulcalvano/status/1541402096897069056)
on the internet that are bigger in size. You, dear reader, are unlikely to be the owner of one,
since the
[median size of a HTML file is about 500 times smaller](https://httparchive.org/reports/page-weight#bytesHtml):
30 [kilobytes (kB)](https://en.m.wikipedia.org/wiki/Kilobyte).
However, if you are the owner of an HTML page that's over 15 MB, perhaps you could at least move
some inline scripts and CSS dust to external files, pretty please.

**What happens to the content after 15 MB?**
The content after the first 15 MB is dropped by Googlebot, and only the first 15 MB gets forwarded
to indexing.

**What content types does the 15 MB limit apply to?**
The 15 MB limit applies to fetches made by Googlebot (Googlebot Smartphone and Googlebot Desktop)
when fetching
[file types supported by Google Search](/search/docs/crawling-indexing/indexable-file-types).

**Does this mean Googlebot doesn't see my image or video?**
No. Googlebot fetches videos and images that are referenced in the HTML with a URL (for example,
`<img src="https://example.com/images/puppy.jpg" alt="cute puppy looking very disappointed" />`
separately with consecutive fetches.

**Do data URIs add to the HTML file size?**
Yes. Using
[data URIs](https://en.wikipedia.org/wiki/Data_URI_scheme)
will contribute to the HTML file size since they are in the HTML file.

**How can I look up the size of a page?**
There are a number of ways, but the easiest is probably using your own browser and its Developer
Tools. Load the page as you normally would, then launch the Developer Tools and switch to the
Network tab. Reload the page, and you should see all the requests your browser had to make to
render the page. The top request is what you're looking for, with the byte size of the page in
the Size column.

For example, in the
[Chrome Developer Tools](https://developer.chrome.com/docs/devtools)
might look something like this, with 150 kB in the size column:

![The Network tab in Chrome Developer Tools](/static/search/blog/images/scsh-googlebot15mb.png)

If you're more adventurous, you can use [cURL](https://curl.se/)
from a command line:

```
curl \
-A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36" \
-so /dev/null https://example.com/puppies.html -w '%{size_download}'
```

If you have more questions, you can find us on
[Twitter](https://twitter.com/googlesearchc)
and in the
[Search Central Forums](https://support.google.com/webmasters/community),
and if you need more clarification about our documentation, leave us feedback on the pages
themselves.
