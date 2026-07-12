---
title: "Server location, cross-linking, and Web 2.0 technology thoughts"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2007-08-server-location-cross-linking-and-web"
url: "https://developers.google.com/search/blog/2007/08/server-location-cross-linking-and-web"
canonical: "https://developers.google.com/search/blog/2007/08/server-location-cross-linking-and-web"
author: "Greg Grothaus"
published: "2007-08-02T00:00:00+00:00"
updated: "2007-08-02T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2007_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:50:00+00:00"
status_code: 200
html_hash: "18b812fb2121f2116695a9d2764791d295e042047435c160d3558ebbee6d082b"
clean_word_count: 502
clean_char_count: 2980
---
# Server location, cross-linking, and Web 2.0 technology thoughts

Held on June 27th,
[Searchnomics 2007](https://www.webguild.org/meetings/2007/searchnomics/)
gave us (Greg Grothaus and Shashi Thakur) a chance to meet webmasters and answer some of their
questions. As we're both engineers focused on improving search quality, the feedback was extremely
valuable.

Here's our take on the conference and a recap of some of what we talked about there.

Shashi: While I've worked at Google for over a year, this was my first time speaking at a
conference. I spoke on the "Search Engine Friendly Design" panel. The exchanges were hugely
valuable, helping me grasp some of the concerns of webmasters. Greg and I thought it would be
valuable to share our responses to a few questions:

**Does location of server matter? I use a .com domain but my content is for customers in the UK.** In our understanding of web content, Google considers both the IP address and the top-level
domain (for example, .com, .co.uk). Because we attempt to serve geographically relevant content,
we factor domains that have a regional significance. For example, ".co.uk" domains are likely
very relevant for user queries originating from the UK. In the absence of a significant top-level
domain, we often use the web server's IP address as an added hint in our understanding of content.

**I have many different sites. Can I cross-link between them?** Before you begin cross-linking
sites, consider the user's perspective and whether the crosslinks provide value. If the sites are
related in business—for example, an auto manual site linking to an auto parts retail site,
then it could make sense—the links are organic and useful. Cross-linking between dozens or
hundreds of sites, however, probably doesn't provide value, and I would not recommend it.

Greg: Like Shashi, this was also my first opportunity to speak at a conference as a Googler. It
was refreshing to hear feedback from the people who use the software we work every day to
perfect. The session also underscored the argument that we're just at the beginning of search and
have a long way to go. I spoke on the subject of Web 2.0 technologies. It was clear that many
people are intimidated by the challenges of building a Web 2.0 site with respect to search
engines. We understand these concerns. You should expect see more feedback from us on this
subject, both at conferences and through our blog.

**Any special guidance for DHTML/AJAX/Flash documents?** It's important to make sure that
content and navigation can be rendered/negotiated using only HTML. So long as the content and
navigation are the same for search crawlers and end users, you're more than welcome to use
advanced technologies such as Flash and/or JavaScript to improve the user experience using a
richer presentation. In
"[Best uses of Flash](/search/blog/2007/07/best-uses-of-flash)," we wrote in more
detail about this, and are working on a post about AJAX technology.
