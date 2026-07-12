---
title: "Message Center info through our API"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2008-12-message-center-info-through-our-api"
url: "https://developers.google.com/search/blog/2008/12/message-center-info-through-our-api"
canonical: "https://developers.google.com/search/blog/2008/12/message-center-info-through-our-api"
author: "Written by Javier Tordable, Software Engineer"
published: "2008-12-10T00:00:00+00:00"
updated: "2008-12-10T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2008_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:56:03+00:00"
status_code: 200
html_hash: "59a7f3c3f4ada4183dafa2764189bb3ffcc9d513bbae4863b33adafa5f89c986"
clean_word_count: 680
clean_char_count: 4583
---
# Message Center info through our API

Recently we [mentioned](/search/blog/2008/10/webmaster-tools-api-updated-with-site)
some updates in the
[Webmaster Tools GData API](https://code.google.com/apis/webmastertools/):
we've just launched a whole new API, the
[Message Center](/search/blog/2007/07/message-center-let-us-communicate-with) GData
API, as part of the Webmaster Tools API. The Message Center is the way that Google communicates to
webmasters important issues regarding their sites—for example, if there's a
[problem crawling your site](https://www.google.com/support/webmasters/bin/answer.py?answer=76401),
or if someone has requested a
[change in crawl rate](https://www.google.com/support/webmasters/bin/answer.py?answer=48620).
Until now it was only possible to access these messages through the Message Center section of
Webmaster Tools; but now you can also use
[GData](https://code.google.com/apis/gdata/)
to access it as a feed. This way you don't need to continually check your messages in Webmaster
Tools, you can retrieve the messages feed automatically and be informed as soon as possible of
any critical issues regarding your site.

## What can I do?

The Message Center GData API lets you retrieve all messages, mark the messages as read or unread,
and delete messages. You can do these tasks using the provided
[Java client libraries](https://code.google.com/p/gdata-java-client/),
or you can create your own client code based on the
[protocol information](https://code.google.com/apis/webmastertools/docs/developers_guide).

- **Retrieve messages:** The messages feed contains all the messages sent to your account.
  These messages have important information about your verified sites. Examples of messages
  include [infinite spaces warnings](/search/blog/2008/08/to-infinity-and-beyond-no)
  and
  [crawl rate change](https://www.google.com/support/webmasters/bin/answer.py?answer=48620&topic=10082)
  notifications.
- **Mark messages as read or unread:** In order to keep track of new communications from
  Google, you can mark your messages as read or unread, the same way that you would manage your
  inbox. If you retrieve a single message, this message will be automatically marked as read.
- **Delete messages:** It's possible to delete messages using the GData API. However, be
  careful because if you delete a message through the API it will also be deleted in your
  Webmaster Tools account, as both interfaces share the same data.

## How do I do it?

You can download
[code samples in Java](https://code.google.com/p/gdata-java-client/source/browse/trunk/java/sample/webmastertools/)
for all these new features. These samples provide simple ways to use the messages feed. The
following snippet shows how to retrieve the messages feed in a
[supported language](/search/blog/2008/05/webmaster-tools-now-in-26-languages) and
print all the messages:

```
// Connect with the service and authenticate
WebmasterToolsService service
    = new WebmasterToolsService("exampleCo-exampleApp-1");
try {
  service.setUserCredentials(USERNAME, PASSWORD);
} catch (AuthenticationException e) {
  System.out.println("Username or password invalid");
  return;
}
// Retrieve messages feed
MessagesFeed messages;
try {
  URL feedUrl;
  if (USER_LANGUAGE == null) {
    feedUrl = new URL(MESSAGES_FEED_URI);
  } else {
    feedUrl = new URL(MESSAGES_FEED_URI
        + "?hl=" + USER_LANGUAGE);
  }
  messages = service.getFeed(feedUrl, MessagesFeed.class);
} catch (IOException e) {
  System.out.println("There was a network error.");
  return;
} catch (ServiceException e) {
  System.out.println("The service is not available.");
  return;
}
// Print the messages feed
System.out.println(messages.getTitle().getPlainText());
for (MessageEntry entry : messages.getEntries()) {
  if (entry.getRead()) {
    System.out.print("   \t");
  } else {
    System.out.print("new\t");
  }
  System.out.print(entry.getDate().toUiString() + "\t");
  System.out.println(entry.getSubject());
}
```

## Where do I get it?

If you want to know more about GData, you may want to start by checking out the
[GData website](https://code.google.com/apis/gdata/). The home page of the
[Webmaster Tools GData API](https://code.google.com/apis/webmastertools/)
contains a section on the messages feed, with details about the protocol. You can also download
the sample Message Center client form the
[GData download site](https://code.google.com/p/gdata-java-client/source/browse/trunk/java/sample/webmastertools/).
It will show you how to use all the Message Center GData API features.
