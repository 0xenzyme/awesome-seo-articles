---
title: "Prepare for mobile-first indexing (with a little extra time)"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2020-07-prepare-for-mobile-first-indexing-with"
url: "https://developers.google.com/search/blog/2020/07/prepare-for-mobile-first-indexing-with"
canonical: "https://developers.google.com/search/blog/2020/07/prepare-for-mobile-first-indexing-with"
author: "Yingxi Wu (吴萤西)"
published: "2020-07-22T00:00:00+00:00"
updated: "2020-07-22T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2020_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:37:02+00:00"
status_code: 200
html_hash: "a7f97123bc4d268bdcc32033ac49fa37569c4382b06b9d983b1c9214c8baa7bf"
clean_word_count: 1422
clean_char_count: 9005
---
# Prepare for mobile-first indexing (with a little extra time)

[Mobile-first indexing](/search/blog/2016/11/mobile-first-indexing) has been an
ongoing effort of Google for several years. We've enabled mobile-first indexing for most
currently crawled sites, and
[enabled it by default for
all the new sites](/search/blog/2019/05/mobile-first-indexing-by-default-for). Our initial plan was to
[enable mobile-first indexing for all sites in Search](/search/blog/2020/03/announcing-mobile-first-indexing-for)
in September 2020. We realize that in these uncertain times, it's not always easy to focus on
work as otherwise, so we've decided to extend the timeframe to the end of March 2021. At that
time, we're planning on switching our indexing over to mobile-first indexing.

For the sites that are not yet ready for mobile-first indexing, we've already mentioned some
issues blocking your sites in
[previous blog posts](/search/blog/2018/12/mobile-first-indexing-structured-data).
Now that we've done more testing and evaluation, we have seen a few more issues that are worth
mentioning to [better prepare your sites](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing).

## Make sure Googlebot can see your content

In mobile-first indexing, we will only get the information of your site from the mobile version,
so make sure Googlebot can see the full content and all resources there. Here are some things to
pay attention to:

### Robots `meta` tags on mobile version

You should use the same [robots `meta` tags](/search/docs/crawling-indexing/robots-meta-tag) on the
mobile version as those on the desktop version. If you use a different one on the mobile version
(such as `noindex` or `nofollow`), Google
may fail to index or follow links on your page when your site is enabled for mobile-first
indexing.

### Lazy-loading on mobile version

Lazy-loading is more common on mobile than on desktop, especially for loading images and videos.
We recommend following [lazy-loading best practices](/search/docs/crawling-indexing/javascript/lazy-loading).
In particular, avoid lazy-loading your primary content based on user interactions (like swiping,
clicking, or typing), because Googlebot won't trigger these user interactions.

For example, if your page has 10 primary images on the desktop version, and the mobile version
only has 2 of them, with the other 8 images loaded from the server only when the user clicks the
`+` button:

![desktop version with 10 thumbnails / mobile version with 2 thumbnails](/static/search/blog/images/import/23d844e245ad4882bd2b3cbf2fd65c2e.png)

In this case, Googlebot won't click the button to load the 8 images, so Google won't see those
images. The result is that they won't be indexed or shown in Google Images. Follow
[Google's lazy-loading best practices](/search/docs/crawling-indexing/javascript/lazy-loading), and lazy
load content automatically based on its visibility in the viewport.

### Be aware of what you block

Some resources have different URLs on the mobile version from those on the desktop version,
sometimes they are served on different hosts. If you want Google to crawl your URLs, make sure
you're not disallowing crawling of them with your
[robots.txt file](/search/docs/crawling-indexing/robots/intro).

For example, blocking the URLs of `.css` files will prevent Googlebot
from rendering your pages correctly, which can harm the ranking of your pages in Search.
Similarly, blocking the URLs of images will make these images disappear from Google Images.

## Make sure primary content is the same on desktop and mobile

If your mobile version has less content than your desktop version, you should consider updating
your mobile version so that its primary content (the content you want to rank with, or the
reason for users to come to your site) is equivalent. Only the content shown on the mobile
version will be used for indexing and ranking in Search. If it's your intention that the mobile
version has less content than the desktop version, your site may lose some traffic when Google
enables mobile-first indexing for your site, since Google won't be able to get the full
information anymore.

Use the same clear and meaningful headings on your mobile version as on the desktop version.
Missing meaningful headings may negatively affect your page's visibility in Search, because we
might not be able to fully understand the page.

For example, if your desktop version has the following tag for the heading of the page:

```
<h1>Photos of cute puppies on a blanket</h1>
```

Your mobile version should also use the same heading tag with the same words for it, rather than
using headings like:

```
<h1>Photos</h1>
```

(not clear and meaningful)

```
<div>Photos of cute puppies on a blanket</div>
```

(not using a heading tag)

## Check your images and videos

Make sure the images and videos on your mobile version follow
[image best practices](/search/docs/appearance/google-images) and
[video best practices](/search/docs/appearance/video). In
particular, we recommend that you perform the following checks:

### Image quality

Don't use images that are too small or have a low resolution on the mobile version. Small or
low-quality images might not be selected for inclusion in Google Images, or shown as favorably
when indexed.

For example, if your page has 10 primary images on the desktop version, and they are normal,
good quality images. On the mobile version, a bad practice is to use very small thumbnails for
these images to make them all fit in the smaller screen:

![desktop version with normal thumbnails / mobile version tiny thumbnails](/static/search/blog/images/import/8ebc2a3122fb22a2c80b2ef8aa041fa5.png)

In this case, these thumbnails may be considered "low quality" by Google because they are too
small and in a low resolution.

### Alt attributes for images

As [previously mentioned](/search/blog/2018/12/mobile-first-indexing-structured-data),
remember that using less-meaningful alt attributes might negatively affect how your images are
shown in Google Images.

For example, a good practice is like the following (meaningful alt text):

```
<img src="dogs.jpg" alt="A photo of cute puppies on a blanket" />
```

While bad practices are like the following (empty alt text):

```
<img src="dogs.jpg" alt="alt" />
```

Here's an example where the alt text isn't meaningful:

```
<img src="dogs.jpg" alt="Photo" />
```

### Different image URLs between desktop and mobile version

If your site uses different image URLs for the desktop and mobile version, you may see a
temporary traffic loss from Google Images while your site transitions to mobile-first indexing.
This is because the image URLs on the mobile version are new to the Google indexing system, and
it takes some time for the new image URLs to be understood appropriately. To minimize a
temporary traffic loss from search, review whether you can retain the image URLs used by desktop.

### Video markup

If your desktop version uses schema.org's
`VideoObject structured data`
to describe videos, make sure the mobile version also includes the
`VideoObject`, with equivalent information provided. Otherwise our
video indexing systems may have trouble getting enough information about your videos, resulting
in them not being shown as visibly in Search.

### Video and image placement

Make sure to position videos and images in an easy to find location on the mobile version of
your pages. Videos or images not placed well could affect user experience on mobile devices,
making it possible that Google would not show these as visibly in search.

For example, assume you have a video embedded in your content in an easy to find location on desktop:

![easy to find video on desktop](/static/search/blog/images/import/3761a0a4ef0fef972abdf5de171862ee.png)

On mobile, you place an ad near the top of the page which takes up a large part of the page.
This can result your video being moved off the page, requiring users to scroll down a lot to
find the video:

![video on mobile is much less visible to users](/static/search/blog/images/import/248fd61c343805b8035d72303552ea9b.png)

In this case, the page might not be deemed a useful video landing page by our algorithms,
resulting in the video not being shown in Search.

You can find more information and more best practices in our
[developer guide for mobile-first indexing](/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing).

Mobile-first indexing has come a long way. It's great to see how the web has evolved from
desktop to mobile, and how webmasters have helped to allow crawling and indexing to match how
users interact with the web! We appreciate all your work over the years, which has helped to
make this transition fairly smooth. We'll continue to monitor and evaluate these changes
carefully. If you have any questions, please drop by our
[forums](https://support.google.com/webmasters/go/community) or our
[public events](/search/events).
