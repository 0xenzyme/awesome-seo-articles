---
title: "Updating Search Console users and permissions management"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2023-02-search-console-user-permissions-update"
url: "https://developers.google.com/search/blog/2023/02/search-console-user-permissions-update"
canonical: "https://developers.google.com/search/blog/2023/02/search-console-user-permissions-update"
author: "Nir Kalush"
published: "2023-02-22T00:00:00+00:00"
updated: "2023-02-22T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2023_aging"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:41:38+00:00"
status_code: 200
html_hash: "b8a7bc635d5d78f3315b518002b669f59be1b60cad8c6c68d775eeb1cc1eb855"
clean_word_count: 414
clean_char_count: 2876
---
# Updating Search Console users and permissions management

Starting today, we're updating [Search
Console's user and permissions](https://search.google.com/search-console/users) to incorporate functionality related to ownership and user management.
Historically, these functionalities were only available in the previous Webmaster Tools experience.

The Webmaster verification tool has served our community well over the years. This launch takes us a
step closer towards our goal of [migrating
functionality to Search Console](/search/blog/2018/01/introducing-new-search-console), ensuring our users have a better, faster, and modernized experience.

## New user management features in Search Console

The functionalities added to Search Console's user and permissions management include:

- Distinguishing between verified and delegated owners
- Easier, immediate removal of verified owners (no need to remove their ownership token)
- Ability to change delegated owners' permissions levels (owner, full, restricted)
- Ability to see your property's verification tokens for all current and previous users and specifically
  see tokens leftover by previous owners
- Ownership events history

## Best practices

As a reminder, here are some best practices for managing user permissions in Search Console.

First, grant users only the [permission
level](https://support.google.com/webmasters/answer/7687615#permissions) that they need to do their work. You can change permission levels for non-verified owners
with the **More actions** menu. Make sure to revoke or change permission levels from users
who no longer work on a property, and regularly audit and update permissions through the
[users and permissions](https://search.google.com/search-console/users) page in Search Console.

![Search Console users and permissions settings page](/static/search/blog/images/search-console-users-and-permissions.png)

When removing a previously verified owner, be sure to [remove
all verification tokens for that user](https://support.google.com/webmasters/answer/7687615#manage-users). This is one of the updates we're rolling out today, you
can now review the leftover ownership tokens so that removed owners cannot regain access to the property.

![Search Console settings page showing leftover ownership tokens](/static/search/blog/images/search-console-leftover-ownership-tokens.png)

Remember that if you just want to share a specific Search Console report on a one-off basis, you can always
click **Share link** on that page instead of adding users to Search Console.

We will be sunsetting the standalone Webmaster Central verification tool in the coming months. As always,
we love to hear feedback from our users. You can use the feedback form within Search Console or the
[help forums](https://support.google.com/webmasters/go/community)
to ask questions or submit feedback.
