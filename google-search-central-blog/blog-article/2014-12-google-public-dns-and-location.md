---
title: "Google Public DNS and Location-Sensitive DNS Responses"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2014-12-google-public-dns-and-location"
url: "https://developers.google.com/search/blog/2014/12/google-public-dns-and-location"
canonical: "https://developers.google.com/search/blog/2014/12/google-public-dns-and-location"
author: "Yunhong Gu, Tech Lead, Google Public DNS"
published: "2014-12-15T00:00:00+00:00"
updated: "2014-12-15T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2014_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:25:49+00:00"
status_code: 200
html_hash: "9659a58c68837ffc2d8d2f54e2eb5609e6679be4632cc6fd8c3d0a1ca0a7331d"
clean_word_count: 359
clean_char_count: 2404
---
# Google Public DNS and Location-Sensitive DNS Responses

Recently the Google Public DNS team, in collaboration with Akamai, reached an important milestone:
Google Public DNS now propagates client location information to Akamai nameservers. This effort
significantly improves the accuracy of approximately 30% of the location-sensitive DNS responses
returned by Google Public DNS. In other words, client requests to Akamai hosted content can be
routed to closer servers with lower latency and greater data transfer throughput. Overall, Google
Public DNS resolvers serve 400 billion responses per day and more than 50% of them are
location-sensitive.

DNS is often used by Content Distribution Networks (CDNs) such as Akamai to achieve location-based
load balancing by constructing responses based on clients' IP addresses. However, CDNs usually see
the DNS resolvers' IP address instead of the actual clients' and are therefore forced to assume
that the resolvers are close to the clients. Unfortunately, the assumption is not always true.
Many resolvers, especially those open to the Internet at large, are not deployed at every single
local network.

To solve this issue, a group of DNS and content providers, including Google,
[proposed an approach](https://googlecode.blogspot.com/2010/01/proposal-to-extend-dns-protocol.html)
to allow resolvers to forward the client's subnet to CDN nameservers in an extension field in the
DNS request. The subnet is a portion of the client's IP address, truncated to preserve privacy.
The approach is officially named
[edns-client-subnet](https://www.afasterinternet.com/ietfdraft.htm)
or ECS.

This solution requires that both resolvers and CDNs adopt the new DNS extension. Google Public
DNS resolvers automatically probe to discover ECS-aware nameservers and have observed the
footprint of ECS support from CDNs expanding steadily over the past years. By now, more than 4000
nameservers from approximately 300 content providers support ECS. The Google-Akamai collaboration
marks a significant milestone in our ongoing efforts to ensure DNS contributes to keeping the
Internet fast. We encourage more CDNs to join us by supporting the ECS option.

For more information about Google Public DNS, please visit
[our website](/speed/public-dns). For CDN operators, please also visit
"[A Faster Internet](https://www.afasterinternet.com/)" for more
technical details.
