---
title: "Updating our site reputation abuse policy"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "medium"
slug: "2024-11-site-reputation-abuse"
url: "https://developers.google.com/search/blog/2024/11/site-reputation-abuse"
canonical: "https://developers.google.com/search/blog/2024/11/site-reputation-abuse"
author: "Chris Nelson"
published: "2024-11-19T00:00:00+00:00"
updated: "2024-11-19T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2024_watch"
  - "news_or_research"
fetched_at: "2026-06-14T13:44:22+00:00"
status_code: 200
html_hash: "917d590a0f0c59878178cfd1655da59ec6a62e987ab0ec59c28de4a5e121eced"
clean_word_count: 1320
clean_char_count: 8645
---
# Updating our site reputation abuse policy

Earlier this [year](/search/blog/2024/03/core-update-spam-policies), as part of our
work to fight spam and deliver a great Search experience, we launched a spam policy to combat
[site reputation abuse](/search/docs/essentials/spam-policies#site-reputation).
This is a tactic where third-party content is published on a host site in an attempt to take
advantage of the host's already-established ranking signals. The goal of this tactic is for
the content to rank better than it could otherwise on a different site, and leads to a bad
search experience for users.

Since launching the policy, we've reviewed situations where there might be varying degrees of
first-party involvement, such as cooperation with white-label services, licensing agreements,
partial ownership agreements, and other complex business arrangements. Our evaluation of numerous
cases has shown that no amount of first-party involvement alters the fundamental third-party
nature of the content or the unfair, exploitative nature of attempting to take advantage of the
host's sites ranking signals.

We're clarifying our policy language to further target this type of spammy behavior.
We're making it clear that using third-party content on a site in an attempt to exploit the
site's ranking signals is a violation of this policy — regardless of whether there is
first-party involvement or oversight of the content. Our updated policy language, effective
today, is:

> Site reputation abuse is the practice of publishing third-party pages on a site in an attempt
> to abuse search rankings by taking advantage of the host site's ranking signals.

When evaluating for policy violations, we take into account many different considerations
(and we don't simply take a site's claims about how the content was produced at face value)
to determine if third-party content is being used in an abusive way. Site owners who receive a
[spam manual
action](https://support.google.com/webmasters/answer/9044175) will be notified through their registered
[Search Console](https://search.google.com/search-console/about)
account and can submit a
[reconsideration
request](https://support.google.com/webmasters/answer/9044175).

It's important to note that not all third-party content violates this policy. We go into detail
on our [spam policies page](/search/docs/essentials/spam-policies#site-reputation)
about what is and isn't site reputation abuse.

Aside from site reputation abuse issues, we also have systems and methods designed to
understand if a section of a site is independent or starkly different from the main content
of the site. By treating these areas as if they are standalone sites, it better ensures a
level playing field, so that sub-sections of sites don't get a ranking boost just because of
the reputation of the main site. As we continue to work to improve these systems, this helps us
deliver the most useful information from a range of sites.

Our efforts to understand differences in sections of sites can lead to traffic changes if
sub-sections no longer benefit from
[site-wide signals](/search/docs/appearance/ranking-systems-guide).
This doesn't mean that these sub-sections have somehow been demoted or are in violation of our
spam policies. It means we're measuring them independently, even if they are located
within a site.

This clarification to our site reputation abuse policy will help surface the most useful search
results, combat manipulative practices, and ensure that all sites have an equal opportunity
to rank based on the quality of their content. We encourage site owners to familiarize
themselves with this updated policy and focus on building high-quality websites that prioritize
[content created to benefit people, not to gain search engine rankings](/search/docs/fundamentals/creating-helpful-content).

## FAQ

### What is third-party content?

Third-party content is content created by a separate entity than the host site. Examples of
separate entities include users of that site, freelancers, white-label services, content created
by people not employed directly by the host site, and other examples listed in the
[site reputation policy](/search/docs/essentials/spam-policies#site-reputation).

### Does the use of any third-party content violate the site reputation abuse policy?

No, having third-party content alone is not a violation of the site reputation abuse policy. It's
only a violation if the content is being published in an attempt to
[abuse search rankings](#abuse-search-rankings) by taking advantage of the host site's
ranking signals. Our [policy page](/search/docs/essentials/spam-policies#site-reputation)
has examples of third-party content use that doesn't violate the policy.

### Does freelance content violate the site reputation abuse policy?

No, while freelance content is third-party content, freelance content alone is not a violation of
the site reputation abuse policy. It is only a violation if there is **ALSO** an
attempt to [abuse search rankings](#abuse-search-rankings) by taking advantage of the
host site's ranking signals.

### Does affiliate content violate the site reputation abuse policy?

No, the policy is not about targeting affiliate content. The
[documentation](/search/docs/essentials/spam-policies#site-reputation) about the policy
notes that affiliate links [marked appropriately](/search/docs/crawling-indexing/qualify-outbound-links)
aren't considered site reputation abuse.

### What does it mean to abuse search rankings by taking advantage of the host site's ranking signals?

This is when third-party content is being placed on an established site to take advantage of that
site's ranking signals — which the site has earned primarily from its first party content
— rather than placing the content on a separate site that lacks the same signals.

### If I [`noindex`](/search/docs/crawling-indexing/block-indexing) the content, does that mean the manual action automatically gets removed?

No. You still need to reply to the manual action in Search Console and explain that the content
has been noindexed. We recommend doing this rather than letting the manual action remain against
your site.

### If I move content that's received a manual action to a new location, will that resolve the site reputation abuse issue?

Maybe, but it depends on where you move it to:

- **Moving content to a subdirectory or subdomain within the same site's domain name**: This
  doesn't resolve the underlying issue and may be viewed as an
  [attempt to circumvent](/search/docs/essentials/spam-policies#policy-circumvension)
  our spam policy, which may lead to broader actions against a site in Google Search.
- **Moving content to another established site**: This will resolve the site reputation abuse
  issue for the site it was removed from, as the site reputation of that site is no longer being
  abused. However, it may introduce a site reputation abuse issue to the site the content is moved
  to if the established site has its own reputation and the third-party nature is unchanged.
- **Moving content to a new domain**: This is far less likely to be an issue if the new
  domain has no established reputation and you follow our
  [spam policies](/search/docs/essentials/spam-policies).

Remember if you move content, you need to also submit a reconsideration request to remove the
manual action.

### If I move policy-violating content, can I redirect from the old site to the new site?

If you move content that received a manual action, you shouldn't [redirect URLs](/search/docs/crawling-indexing/301-redirects)
from the old site to the new site, as this may introduce the site reputation abuse issue again.

### If I move policy-violating content, can I link from the old site to the new site?

If you link from the old site to the new site, make use of the
[`nofollow` attribute](/search/docs/crawling-indexing/qualify-outbound-links)
for those links on the old site.

---

## Updates

- **Update on December 6, 2024**: Added [FAQs](#faq) to address some new questions
  we've had come in from site owners about our site reputation abuse policy.
- **Update on January 21, 2025**: Based on feedback on the FAQ, we updated the [site reputation abuse policy](/search/docs/essentials/spam-policies#site-reputation)
  language and [manual actions report documentation](https://support.google.com/webmasters/answer/9044175#site-reputation-abuse&zippy=%2Csite-reputation-abuse)
  to include guidance from the FAQ. These are editorial changes to make the policy wording
  clearer; there's no substantive change to the policy itself.
