---
title: "Collaboration and user management in the new Search Console"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2018-08-collaboration-and-user-management-in"
url: "https://developers.google.com/search/blog/2018/08/collaboration-and-user-management-in"
canonical: "https://developers.google.com/search/blog/2018/08/collaboration-and-user-management-in"
author: "John Mueller"
published: "2018-08-29T00:00:00+00:00"
updated: "2018-08-29T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2018_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:32:46+00:00"
status_code: 200
html_hash: "2b0819255c94beff13f4524e164d843c486baa990361f87e20cd3765c0798176"
clean_word_count: 444
clean_char_count: 2844
---
# Collaboration and user management in the new Search Console

As part of our reinvention of Search Console, we have been rethinking the models of facilitating
cooperation and accountability for our users. We decided to redesign the product around
cooperative team usage and transparency of action history. The new Search Console will gradually
provide better history tracking to show who performed which significant property-affecting
modifications, such as changing a setting, validating an issue or submitting a new sitemap. In
that spirit we also plan to enable all users to see critical site messages.

## New features

- User management is now an integral part of Search Console.
- The new Search Console enables you to
  [share a read-only view](https://support.google.com/webmasters/answer/7440203#sharing_the_report)
  of many reports, including Index coverage, AMP, and Mobile Usability.
- A new user management interface that enables all users to see and (if appropriate), manage user
  roles for all property users.

## New Role definition

In order to provide a simpler permission model, we are planning to limit the "restricted" user
role to read-only status. While being able to see all information, read-only users will no
longer be able to perform any state-changing actions, including starting a fix validation or
sharing an issue.

## Best practices

As a reminder, here are some best practices for managing user permissions in Search Console:

- Grant users only the permission level that they need to do their work.
  [See the permissions descriptions](https://support.google.com/webmasters/answer/7687615#permissions).
- If you need to share an issue details report, click the Share link on that page.
- Revoke permissions from users who no longer work on a property.
- When removing a previous verified owner, be sure to
  [remove all verification tokens for that user](https://support.google.com/webmasters/answer/7687615#manage-users).
- Regularly audit and update the user permissions using the
  [Users and Permissions](https://search.google.com/search-console/users)
  page in new Search Console.

## User feedback

As part of our Beta exploration, we released visibility of the user management interface to all
user roles. Some users reached out to request more time to prepare for the updated user management
model, including the ability of restricted and full users to easily see a list of other
collaborators on the site. We've taken that feedback and will hold off on that part of the launch.
Stay tuned for more updates relating to collaboration tools and changes on our permission models.

As always, we love to hear feedback from our users. You can use the feedback form within Search
Console, and we welcome your discussions in our
[help forums](https://support.google.com/webmasters/go/community)
as well!
