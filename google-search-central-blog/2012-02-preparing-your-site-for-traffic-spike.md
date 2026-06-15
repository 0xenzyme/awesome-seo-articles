---
title: "Preparing your site for a traffic spike"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2012-02-preparing-your-site-for-traffic-spike"
url: "https://developers.google.com/search/blog/2012/02/preparing-your-site-for-traffic-spike"
canonical: "https://developers.google.com/search/blog/2012/02/preparing-your-site-for-traffic-spike"
author: "Susan Moskwa"
published: "2012-02-09T00:00:00+00:00"
updated: "2012-02-09T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2012_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:17:44+00:00"
status_code: 200
html_hash: "a26434cabce154192bbd69d62a052e1e6950298809c1e958202896d45a3f55ba"
clean_word_count: 670
clean_char_count: 3965
---
# Preparing your site for a traffic spike

It's a moment any site owner both looks forward to, and dreads: a huge surge in traffic to your
site (yay!) can often cause your site to crash (boo!). Maybe you'll create a piece of viral
content, or get Slashdotted, or maybe Larry Page will get a tattoo and your site on tech tattoos
will be suddenly in vogue.

Many people go online immediately after a noteworthy event—a political debate, the death of a
celebrity, or a natural disaster—to get news and information about that event. This can cause a
rapid increase in traffic to websites that provide relevant information, and may even cause sites
to crash at the moment they're becoming most popular. While it's not always possible to anticipate
such events, you can prepare your site in a variety of ways so that you'll be ready to handle a
sudden surge in traffic if one should occur:

- **Prepare a lightweight version of your site.** Consider maintaining a lightweight version
  of your website; you can then switch all of your traffic over to this lightweight version if you
  start to experience a spike in traffic. One good way to do this is to have a mobile version of
  your site, and to make the mobile site available to desktop/PC users during periods of high
  traffic. Another low-effort option is to just maintain a lightweight version of your home page,
  since the home page is often the most-requested page of a site as visitors start there and then
  navigate out to the specific area of the site that they're interested in. If a particular
  article or picture on your site has gone viral, you could similarly create a lightweight version
  of just that page.
  A couple tips for creating lightweight pages:

- Exclude decorative elements like images or Flash wherever possible; use text instead of
  images in the site navigation and chrome, and put most of the content in HTML.
- Use static HTML pages rather than dynamic ones; the latter place more load on your servers.
  You can also cache the static output of dynamic pages to reduce server load.

- **Take advantage of stable third-party services.** Another alternative is to host a copy of
  your site on a third-party service that you know will be able to withstand a heavy stream of
  traffic. For example, you could create a copy of your site—or a pared-down version with a focus
  on information relevant to the spike—on a platform like
  [Google Sites](https://sites.google.com/) or
  [Blogger](https://www.blogger.com/); use services like
  [Google Docs](https://docs.google.com/) to host documents or
  forms; or use a
  [content delivery network](https://www.google.com/search?q=content+delivery+network)
  (CDN).
- **Use lightweight file formats.** If you offer downloadable information, try to make the
  downloaded files as small as possible by using lightweight file formats. For example, offering
  the same data as a plain text file rather than a PDF can allow users to download the exact same
  content at a fraction of the filesize (thereby lightening the load on your servers). Also keep
  in mind that, if it's not possible to use plain text files, PDFs generated from textual content
  are more lightweight than PDFs with images in them. Text-based PDFs are also
  [easier for Google to understand and index fully](/search/blog/2011/09/pdfs-in-google-search-results).
- **Make tabular data available in CSV and XML formats.** If you offer numerical or tabular
  data (data displayed in tables), we recommend also providing it in CSV and/or XML format. These
  filetypes are relatively lightweight and make it easy for external developers to use your data
  in external applications or services in cases where you want the data to reach as many people as
  possible, such as in the wake of a natural disaster.

We'd love to hear your tips and tricks for weathering traffic spikes—come join us in our
[Webmaster Help Forum](https://support.google.com/webmasters/community).
