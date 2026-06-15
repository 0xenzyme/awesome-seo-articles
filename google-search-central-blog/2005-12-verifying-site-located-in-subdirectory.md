---
title: "Verifying a site located in a subdirectory"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2005-12-verifying-site-located-in-subdirectory"
url: "https://developers.google.com/search/blog/2005/12/verifying-site-located-in-subdirectory"
canonical: "https://developers.google.com/search/blog/2005/12/verifying-site-located-in-subdirectory"
author: "Vanessa Fox"
published: "2005-12-19T00:00:00+00:00"
updated: "2005-12-19T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2005_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T12:44:25+00:00"
status_code: 200
html_hash: "c2cc6b5081993a09be3cd8595ed628a14da1429a8e52dd27598498938738fa46"
clean_word_count: 532
clean_char_count: 3130
---
# Verifying a site located in a subdirectory

If your site is located in a subdirectory, rather than at the root level of a domain (for
instance, at **https://www.example.com/site/**), you are given two choices when you verify.
You can either verify at the subdirectory level or at the root level.

![verification page in webmaster tools](/static/search/blog/images/import/42bfefc4fef833db3f256d94707d00bd.jpg)

If you verify at the root level (**https://www.example.com/**), we can show you a greater
variety of statistics.

If you are unable to upload a file at the root level, you can still view error information for the
subdirectory at which you've verified, as well as information about your Sitemaps. Verification
does not affect your Sitemap submission or the crawling or indexing of your site.

If you verify at the subdirectory level, some statistics are not available. Instead, some stats
pages provide a link for verifying at the root level.

![suggestion in the stats feature to verify the site at domain level in webmaster tools](/static/search/blog/images/import/76086485e3f4dab881d34df46c97e592.jpg)

If you have root-level access, simply click the verify link, place the requested verification
file in the root directory and then click **Verify**.

Some questions you may have about verifying at the subdirectory level:

## I verified successfully at https://www.example.com/site/. But when I access my stats, I see a message asking me to verify again. Why is it asking me this since I already verified?

That message is providing a link so you can verify at the root level. Rest assured that your site
is still verified at the subdirectory level and you can access all information that we have
available at this time for subdirectories (index stats, Sitemap details, and site errors).

## I verified successfully at https://www.example.com/site/. But I can still see the Verify tab. When I access that tab and click "Verify", I get a message that Google couldn't find my verification file and that my site isn't verified. The original verification file is still present at https://www.example.com/site/, so why am I getting this message?

If you are successfully verified at the subdirectory level, the Verify tab will still appear so
that you can later go back and verify at the root level. When you are already verified at the
subdirectory level, we look for the verification file in the root of the domain when you try to
verify again. You'll see an error message if we don't find it there.

## I can't verify at the root. Will this affect my listings in Google?

No. Verification at the root lets you see a greater variety of statistics for your site. It does
not affect how we use your Sitemap, how we crawl your site, your PageRank, or any other factor.

## A previous version let me verify at the subdirectory level. Why did you change it in this version?

You can still verify at the subdirectory level as you could before and see everything you could
before (everything listed under the Sitemaps tab and Errors tab). We've added the option of
verifying at the root, which lets you see root-level stats.
