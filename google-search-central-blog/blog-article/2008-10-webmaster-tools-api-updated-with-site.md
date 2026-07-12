---
title: "Webmaster Tools API updated with Site Settings"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-10-webmaster-tools-api-updated-with-site"
url: "https://developers.google.com/search/blog/2008/10/webmaster-tools-api-updated-with-site"
canonical: "https://developers.google.com/search/blog/2008/10/webmaster-tools-api-updated-with-site"
author: "Written by Javier Tordable, Software Engineer"
published: "2008-10-13T00:00:00+00:00"
updated: "2008-10-13T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
  - "time_sensitive_title"
fetched_at: "2026-06-14T12:55:20+00:00"
status_code: 200
html_hash: "adaadcfcf6e0f5ff34f5dc111f0e1608fdea2af9f9abf2a1daadc425736b1602"
clean_word_count: 680
clean_char_count: 4423
---
# Webmaster Tools API updated with Site Settings

The
[Webmaster Tools GData API](https://code.google.com/apis/webmastertools/)
has been updated to allow you to get even more out of Webmaster Tools, such as
[setting a geographic location](https://www.google.com/support/webmasters/bin/answer.py?answer=62399)
or your
[preferred domain](https://www.google.com/support/webmasters/bin/answer.py?answer=44231).
For those of you that aren't familiar with
[GData](https://code.google.com/apis/gdata/),
it's a protocol for reading and writing data on the web. GData makes it very easy to communicate
with many Google services, like Webmaster Tools. The Webmaster Tools GData API already allows you
to add and verify sites for your account and to submit Sitemaps programmatically. Now you can also
access and update site-specific information. This is especially useful if you have a large number
of sites. With the Webmaster Tools API, you can perform hundreds of operations in the time that it
would take to add and verify a single site through the web interface.

## What can I do?

We've included four new features in the API. You can see and update these settings for each site
that you have verified. The features are:

- **Crawl Rate:** You can request that Googlebot crawl your site slower or faster than it
  normally would (the details can be found in our
  [Help Center article about crawl rate control](https://www.google.com/support/webmasters/bin/answer.py?answer=48620)).
  If many of your sites are hosted on the same server and you know your server's capacity, you
  may want to update all sites at the same time. This now a trivial task using the Webmaster
  Tools GData API.
- **Geographic Location:** If your site is targeted towards a particular geographic location
  but your domain doesn't reflect that (for example with a .com domain), you can
  [provide information](https://www.google.com/support/webmasters/bin/answer.py?answer=62399)
  to help us determine where your target users are located.
- **Preferred Domain:** You can select which is the canonical domain to use to index your
  pages. For example, if you have a site like www.example.com, you can set either example.com or
  www.example.com as the preferred domain to use. This avoids the
  [risk of treating both sites differently](https://www.google.com/support/webmasters/bin/answer.py?answer=44231).
- **Enhanced Image Search:** Tools like the
  [Google Image Labeler](https://images.google.com/imagelabeler/)
  allow users to tag images in order to improve Image Search results. Now you can opt in or out
  for all your sites in a breeze using the Webmaster Tools API.

## How do I do it?

We provide you with
[Java code samples](https://code.google.com/p/gdata-java-client/)
for all the current Webmaster Tools API functionality. Here's a sample snippet of code that takes
a list of sites and updates the geographic location of all of them:

```
// Authenticate against the Webmaster Tools service
WebmasterToolsService service;
try {
  service = new WebmasterToolsService("exampleCo-exampleApp-1");
  service.setUserCredentials(USERNAME, PASSWORD);
} catch (AuthenticationException e) {
  System.out.println("Error while authenticating.");
  return;
}

// Read sites and geolocations from your database
readSitesAndGeolocations(sitesList, geolocationsList);

// Update all sites
Iterator sites = sitesList.iterator();
Iterator geolocations = geolocationsList.iterator();
while (sites.hasNext() && geolocations.hasNext()) {
  // Create a blank entry and add the updated information
  SitesEntry updateEntry = new SitesEntry();
  updateEntry.setGeolocation(geolocations.next());

  // Get the URL to update the site
  String encodedSiteId = URLEncoder.encode(sites.next(), "UTF-8");
  URL siteUrl = new URL("https://www.google.com/webmasters/tools/feeds/sites/" + encodedSiteId);
  // Update the site
  service.update(siteUrl, updateEntry);
}
```

## Where do I get it?

The main page for the
[Webmaster Tools GData API](https://code.google.com/apis/webmastertools/)
explains all the details of the API. It has a detailed reference guide and also many code
snippets that explain how to use the Java client library, which is
[available for download](https://code.google.com/p/gdata-java-client/).
You can find more details about GData and all the different Google APIs in the
[Google Data API home page](https://code.google.com/apis/gdata/).
