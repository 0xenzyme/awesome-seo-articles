---
title: "Holiday source code maintenance: Website clinic for non-profits"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2010-12-holiday-source-code-housekeeping"
url: "https://developers.google.com/search/blog/2010/12/holiday-source-code-housekeeping"
canonical: "https://developers.google.com/search/blog/2010/12/holiday-source-code-housekeeping"
author: "Charlene Perez, Michael Wyszomierski"
published: "2010-12-21T00:00:00+00:00"
updated: "2010-12-21T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2010_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:10:23+00:00"
status_code: 200
html_hash: "f8a2aedfd8ae2302f901a8a17872d1b135a04f53c5b6332808f5bb102a538bed"
clean_word_count: 982
clean_char_count: 6353
---
# Holiday source code maintenance: Website clinic for non-profits

*Cross-posted on the
[Google Grants Blog](https://googlegrants.blogspot.com/2010/12/holiday-source-code-housekeeping)*

As the holiday season comes around, we all have a bit of maintenance to do. This is precisely why
we wanted to focus the second post in our
[site clinic series](/search/blog/2010/12/helping-holiday-hand-website-clinic-for)
on cleaning up your source code. Throughout our analysis of submitted non-profit websites, we
noticed some confusion about what HTML markup, or tags, to use where, and what content to place
within them, both of which could have significant impact on users and how your website looks on
the search results page.

## Before you deck the halls, deck out your `<title>`elements

**Out of all the submitted non-profit websites, 27% were misusing their `<title>`
elements, which are critical in letting both Google and users know what's important to your
website. Typically, a search engine will display ~60 characters from your title element; this
is valuable real estate, so you should use it! Before getting into the actual code, let's first
take a look at how a great title element from one of our submitted sites,
[Sharp](https://www.sharp.com/index.cfm),
will appear in the search results page:**
![A single search result with the title link highlighted](/static/search/blog/images/import/c748314da82d9e0cc4080261acfa9baf.png)

Ideally, a great `<title>` element will include the name of the organization,
along with a descriptive tag line. Let's take a look at some submitted examples:

|  |  |  |  |
| --- | --- | --- | --- |
| Organization | `<title>` source code | User Friendliness | Tag Behavior |
| [Sharp](https://www.sharp.com/index.cfm) | `<title>Top San Diego Doctors and Hospitals - Sharp HealthCare</title>` | Best | Includes organization's name and a descriptive tag line |
| [Interieur](https://www.interieur.be/) | `<title>Interieur 2010 - 15-24 October Kortrijk, Belgium</title>` | Good | Includes the organization's name and a non-descriptive tag line |
| [VAMS International](https://www.vamsinternational.org/) | `<title>Visual Arts and Music for Society | VAMS International</title>` | Okay | Includes only the organization's name |

If you don't specify a `<title>` tag, then Google will try to create a title for
you. You can probably do better than our best guess, so go for it: take control of your
`<title>` tag! It's a simple fix that can make a huge difference. Using specific
`<title>` tags for your deeper URLs is also important, and we'll address that in
our next site clinic post.

## Keep an eye on your description `meta` tags

[Description `meta` tags](/search/blog/2007/09/improve-snippets-with-meta-description)
weren't being utilized to their full potential in 54% of submitted sites. These tags are often
used to populate the two-line snippet provided to users in the search results page. With a
solid snippet, you can get your potential readers excited and ready to learn more about your
organization. Let's take another look at a good example from among the submitted sites,
[Tales of Aussie Rescue](https://www.aussierescueil.com/):

![A search result for the Tales of Aussie Rescue home page](/static/search/blog/images/import/a67ab9e167ca7849f4c2e16469f7e29d.png)

If description `meta` tags are absent or not relevant, a snippet will be chosen from the page's
content automatically. If you're lucky and have a good snippet auto-selected, keep in mind
that search engines vary in the way that they select snippets, so it's better to keep things
consistent and relevant by writing a solid description `meta` tag.

## Keep your `<h>` elements in their place

Another quick fix is to assure your website makes proper use of heading
tags. In our non-profit study, nearly 19% of submitted sites had room for improvement with
heading elements. The most common problem in heading tags was the tendency to initiate
headers with an `<h2>` or `<h3>` tag while not including an
`<h1>` tag, presumably for aesthetic reasons.

Headings give you the opportunity to tell both Google and users what's important to you and
your website. The lower the number on your heading tag, the more important the text, in the
eyes of Google and your users. Take advantage of that `<h1>` tag! If you don't
like how an `<h1>` tag is rendered visually, you can always alter its appearance
in your CSS.

## Use alt text for images

Everyone is always proud to display their family photos come holiday season, but don't forget
to tell us what they're all about. Over 37% of analyzed sites were not making appropriate use
of the image alt attribute. If used properly, this attribute can:

- Help Google understand what your image is
- Allow users on text-only browsers, with accessibility problems, or on limited devices to
  understand your images

Keep in mind, rich and descriptive alt text is the key here. Let's take another look at some
of our submitted sites and their alt attribute usage:

|  |  |  |  |
| --- | --- | --- | --- |
| Organization | Source Code | User Friendliness | Tag Behavior |
| [Sponsor A Puppy](https://www.guidedogsgiving.org.uk/sponsorapuppy/) | `<img alt="Sponsor a Puppy logo" src="..." />` | Best: the alt text specifies the image is the organization's main logo | Uses rich, descriptive alt text to describe images, buttons, and logos |
| [Philanthropedia](https://www.myphilanthropedia.org/) | `<img alt="Logo" height="..." />` | Good: the alt text specifies the image is a logo, but does not further describe it by the organization or its behavior | Uses non-descriptive alt text for images, buttons, and logos, or uses alt text only sporadically |
| [Coastal Community Foundation](https://www.coastalcommunityfoundation.org/) | `<img src="..." />` | Not ideal: alt text not present | No use of alt text, or use of text that does not add meaning (often seen in numbering the images) |

## A little window shopping for your New Year's resolution

Google has some great resources to further address best practices in your source code. For
starters, you can use our
[HTML Suggestion Tool](https://www.google.com/support/webmasters/bin/answer.py?answer=80407)
in Webmaster Tools. Also, it's always a good practice to make your site
[accessible](https://www.google.com/accessibility/) to all viewers.
