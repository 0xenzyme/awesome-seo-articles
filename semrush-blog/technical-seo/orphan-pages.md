---
title: "Orphan Pages: How They Affect SEO (And How to Fix Them)"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "orphan-pages"
url: "https://www.semrush.com/blog/orphan-pages/"
canonical: "https://www.semrush.com/blog/orphan-pages/"
author: "Semrush Team"
published: "2023-10-04T12:57:00+00:00"
updated: "2023-10-04T12:57:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2023_aging"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T18:23:43+00:00"
status_code: 200
html_hash: "8824830138e8ecfc5eaf1bbdf35c90e0c6fc8c79c946f109d69ea8162ca6d36a"
clean_word_count: 2566
clean_char_count: 18113
---
# Orphan Pages: How They Affect SEO (And How to Fix Them)

## What Are Orphan Pages?

Orphan pages are webpages that don’t have links from anywhere else on your site.

Think of them like little islands, separate from the mainland of your website.

![A visual representation of orphan pages](https://static.semrush.com/blog/uploads/media/f5/f0/f5f0e05e269ce3f58d118fe41950fa8b/Ann0J5xV7pjnzaIqS_YFW1M4evxCSGxHN8vIs9F9sS6SZhWexwYrxsFvMJexiP1L3nEAIdrf2Y8oNi0QAPAUTla1t9l9lKew0pip42teZ_FvvJMLsMw9C9XGlM_sKlNLWE7d6aXKFW391KL1iEStLZ4.png)

## How Orphan Pages Affect SEO

Orphan pages can have unintended consequences for your site.

Three main issues can arise:

### 1. Page Does Not Get Indexed

Because there are no links to an orphan page, search engine crawlers have no paths to follow to reach it.

If they can't reach the page, they [can’t crawl or index it](https://www.semrush.com/blog/crawlability-issues/). And if they can't index it, the page may not appear in search results.

However, search engine crawlers also reference your XML sitemap, which is a directory of all of the pages on your website.

So, in theory, the bot could still discover an orphan page through your sitemap even if you haven’t linked to that page elsewhere. But that doesn’t mean it’s not an issue you should address.

***Note**: Sitemap crawling is also why orphaning a page isn't an effective way to “hide” it from visitors or bots. More on that in the [FAQ section.](#frequently-asked-questions)*

### 2. Poor Search Rankings

Even if the page is crawled and indexed, having no internal links to a page can lower its rankings in the search engine results pages ([SERPs](https://www.semrush.com/blog/serp/)) and hurt your site’s organic search traffic.

Because of [PageRank](https://www.semrush.com/blog/pagerank/).

PageRank is a Google algorithm that uses inbound links as a ranking factor.

Think of each inbound link as a vote for that page’s quality and authority. The value passed by links is called “link equity.”

Building internal links is a tactic to spread link equity throughout your website.

If a page doesn’t have any inbound internal links, it won’t receive any link equity from other pages on your site.

Hence, it may not rank well in search engines and may not receive much—if any—organic traffic.

### 3. Poor User Experience

Without inbound links from navigation menus or other pages, orphan pages are also virtually invisible to visitors.

The only way a user can visit an orphan page is by entering the URL directly. And the user can't do this if they don't know the page exists.

If the orphan page contains information that would be helpful to your audience, it's not doing them any good if it's effectively hidden from their view.

## How to Fix Orphan Pages

To fix an orphan page, you simply need to **add a link from a relevant page on your website**. Or from a navigation menu, if appropriate.

Just make sure you're not linking to an orphan page from another orphan page.

As long as there is a link from another relevant (non-orphan) location on your site, it will become part of your overall site structure. Problem solved.

That’s the easy part.

The more difficult part is finding orphan pages on your site.

## How to Find Orphan Pages on Your Site

The easiest way to find orphan pages is to use Semrush [Site Audit](https://www.semrush.com/siteaudit/) tool.

The process of uncovering orphan pages is notoriously tricky. Because if the page is not linked anywhere, it may not be discovered by most SEO tools or crawlers.

If you can’t discover the page, you can’t identify it as an orphan.

It’s a self-perpetuating issue.

Site Audit crawls your website in much the same way a search engine bot does. It starts with your homepage, and navigates through every link in the page's code to discover new pages.

Then, if you have an XML sitemap and have connected your Google Analytics account, Site Audit can gather more data.

It will compare the list of URLs in the sitemap against the pages that have received traffic.

If there are any discrepancies—if pages appear in the sitemap but haven’t received traffic or vice versa—Site Audit will identify these as “missing” and confirm these pages as orphans.

Here’s how to use it:

Log in to Semrush and click “**Site Audit**” under “On Page & Tech SEO.”

![“Site Audit” in Semrush menu](https://static.semrush.com/blog/uploads/media/f6/3e/f63e23e1a5324507acc5d7e8319d23b9/Ntvc5fLUImPcH6O23okBMerL-FKHSHpijvQgjjYgKYtnJc3NBNleWsjfqY_0K7TOFvcpkVSLfIByCO4ub3JLzzVxfjXtZ0fTcTIWot9QDOi5P-d5gGs3FvbJ7y7prftWOGm3I01VzR1XotD2WvzWQuo.png)

Enter your website's domain and click “**Start Audit**.”

***Note**: If you don't already have a project set up in Semrush, click “**Create** **project**” to add a new project and run a new audit.*

!["example.com" entered into Start Audit search bar](https://static.semrush.com/blog/uploads/media/fb/40/fb40f31a7fc7d2089bcbf91398a32f47/P2gK4BoHmhfj60yAXawgw8dZQ8TYas_dVE8yoJG2XbaYODunTj2P006LqLRFwO5bIUMSOGcQcLsRFlpj32UY-qchv3wFz09erQu4QByMosr3aacgyposbkmn8BTUGcLA6bq0IYT2mS8ZAJFb_ajkGQ4.png)

You’ll see the “Site Audit Settings” dialogue. Click the drop-down menu, and select the number of pages to audit. Click “**Start** **Site** **Audit**.”

***Note**: Free accounts can crawl up to 100 pages.*

![Start Audit Settings popup window](https://static.semrush.com/blog/uploads/media/24/b0/24b0fb3b5a9588188e239b2c8f18c5de/JNXMSAS7AFIlw7nyF-VjrRsoLYlJT6Mi3yEIJgDAi0mW7HtC6ENfMk1Ruf8h0FGV0I-4_dI530zvGOp68Y05jiYy3Ps0fwP8fXgx3IQr1-8Zs-Yxkq2xzxKbz6qVy4TSaMgInSpwvAa_n0qq9l_VpSo.png)

***Pro tip**: More advanced users can customize the settings in this dialogue to adjust how the site crawl operates.*

Now the Site Audit crawl bot will traverse all of your site’s pages, analyzing the content, images, and links.

Then you’ll receive a report.

Once the Site Audit is complete, click the domain to see the results.

!["example.com" domain in Start Audit results](https://static.semrush.com/blog/uploads/media/08/d0/08d076f0fa47fbdafee60d57f949dbb7/2VmUcfdH1glpZ6W-HfqFwE1g-rXz8G8As3S59Vu1fSG7n07MtI1bqnafuWir03h7yJPdJ3NaLfzVcT2P9qDjtc-q-cohqwnf-hRJOlGCtB0buyPOP3tn6n5vbNCAZXwv-4EjybNHMCxUaN5BaJCNrRQ.png)

Then click the “**Issues**” tab.

![Start Audit's "Issues" tab](https://static.semrush.com/blog/uploads/media/31/a4/31a4fd290573e72d6eeeac81a9df543b/dyp_swaUCe0m9Yr512T0pAI7LWx99TK09sr9Bd1LDI_L7bTS6_13hvP_N3a67EmhFoMW1oYbURW85b-NrM7XdocODj_iqFscgyLQtPNhsz0iHfBTzLHz4Wox1VblTnjA2r2MMvG-Xbpv994mFbzM6JU.png)

Type “orphan” into the “Search by check” bar to find the two sections related to orphan pages. The first item looks for orphan pages based on your sitemap.

![Start Audit results show "0 orphaned pages in sitemaps"](https://static.semrush.com/blog/uploads/media/fd/d4/fdd40cca698948e896aca2d91a968d42/qAFyftsn9rTVZkv10mUgR6ZIEHljzECLV0HtDxS9_egAVup-HrS0Osw5w8zhJlqA26JpD1I0abbeC5tua_BYJ-ICTUjtnrgihllPuo3g0QhqKOlGkiI0giQ7J1yJmpz7giciu1iKW_ET7J70nf-ARmg.png)

If you don’t have an XML sitemap, the Site Audit crawler couldn’t find it, or you want to do an additional check for orphan pages, you can use Google Analytics data for the second check. To do this, you’ll need to connect your Google Analytics account.

Click “**Connect** **GA**” or the “**Connect your Google Analytics**” account link.

![“Connect GA” button highlighted](https://static.semrush.com/blog/uploads/media/71/96/7196a6731224b5b28d9a0bc903324afe/wF14HTfIrp9js8dRz7cqNnLopQOUpoMoWdz8wklQcXA7nXCLA8L5QTtNRPGrZIbLwDfvcUTd8KgK4CDH3-LcnR4LXRw4LnKr2cfeXbdhyX3dERlLchtUSmpGpiQYnIIOftr_0aOeB39ZE9VHK-mgAOM.png)

You’ll see a new window that prompts you to connect your Google account to grant Semrush access to Google Analytics. Select the Google account that’s connected to your Google Analytics profile for the website you're auditing.

!["Sign in with Google" popup window](https://static.semrush.com/blog/uploads/media/de/1a/de1a8976ab83da4bc3a0736acbb8efeb/34yXCDeE3y1NG4kynZ4lZ6sYASmHnXFXKPgnw3-w21xGaE6fK-qgw1EmKY7uyQyaFt6oRDzDgtpnl48Qflb9KWCx5nJutgj3-T7SGCf1PAhCSxA82Rzy_zNnkfEhq_upGVgEOHkrbFrisjLuzkpSkx0.png)

On the next screen, scroll down and click “**Allow**.”

!["Allow" button highlighted](https://static.semrush.com/blog/uploads/media/1a/06/1a0669f359151c44601b26b1a9d8316b/YmmDceNeAVlOZRnHX5fHpmWAnRagftFT6lVi-vQvpj-kTK3ZUbaitfOc5zq5uQyuLGeetjdavlsrEniCAiOr4jn0h2qTn87b7-yugXU7LBj8mZGLlXEU8kMUzJwg-6CTmiVVCch2fFqXJHzJPn6_L6I.png)

Now you’ll return to the Site Audit Settings in Semrush. Click the drop-down next to “Account” and choose the account you just connected.

!["Account" drop-down menu in Site Audit Settings](https://static.semrush.com/blog/uploads/media/23/39/233948ce4532250c1a40bd0d5a0e5a15/_ccp8cw9qi8BKu3YIj9LWfn_hlzlWaxnJAeMftL5dp86BL-oo5d-90AYc1trT-5qVX_lz2XiOi3Vm0-xuIPEpqlSkE4OjkBhzCpeUzmyPIJc49A2UDWE4N2QFPU0rcUfg7PytzonGpLDJKtRRnOBeEM.png)

Now select from each of the drop-down menus to choose the Profile, Property, and View for the Google Analytics account associated with this website. Click “**Save**.”

![Profile, Property, and View section in Site Audit Settings](https://static.semrush.com/blog/uploads/media/c7/93/c7933240b506b01fcaa4bca7f1e32130/DvRAsMcHJj8DSxk-a0BnmR6nrR4poXoaPuWkVr4fptKGKfW0QAMfVyDkzLHdirky890pYNsxryhilk8PgR0aQClqmTm0aejz2t8gz7cbDNaH3fEpU_YhJEJ2WWq-u3X008lG6wHY8BRKENXKxH3qlhY.png)

Return to the Audit Report. Refresh the page, and type “orphan” into the search box under the “Issues'' tab. Now you’ll see only the issues related to orphan pages.

![Search for “orphan” in "Issues" tab](https://static.semrush.com/blog/uploads/media/57/ed/57ed289a7e4b27982c06bfe1f3b01b02/LaNF-sSBF5bIs33OmFdfVZTk-J7fZEQwyCMC1PEr4XDTDz34hIOojXkZOV58dE4bRyv2oPRk-S9oSTVKHvKyeVwcYKqf_xCaltIjvLGlAQz5ld4SWxMxKSIKDerj9JJ8xrLK6Wvrw7U5ef63Edez6j0.jpeg)

Click the “**3,498 orphaned pages**” text to drill down into the orphan pages discovered.

![“3,498 orphaned pages” highlighted](https://static.semrush.com/blog/uploads/media/66/37/663777b0f5a577bbd5b775cab4d01aeb/b26hAK_AhKINjaFlPhqyS8sTnw4DkrkQAMpyVqgCEAKQkFeOeKOpbM5Hy0LbCJQweTZSHgyEdqwNMH1s1lHHV0OpDKaxbkW_cWWUc-r3mmnfd0Ma8K0rzp1lpEEKMVcy88O2lNLaOTUxJJY112hd89A.jpeg)

Here you’ll find a list of any orphan pages identified by comparing the number of pages in your Google Analytics account.

![“3,498 orphaned pages in Google Analytics” page](https://static.semrush.com/blog/uploads/media/53/2a/532a9ac1bf47e55aaac203b0c188ca69/_AoE5nyEnC0VDsTvfYpXavmqyJC40Ba5ARnJZgSaBHa0hOfd54x3A_oRxCZxPGMuNa3zWqKOHYxBWl_Eesam7GvJg-0Us4vrhz4TS4iaylgEq2-i5yLD_75_XQDX6YZPAseTmUCkyIb_HUdEBKsmMGk.png)

Once you’ve found the orphan pages, you can integrate them into your site structure by adding links from relevant pages or your website’s navigation.

## Other Ways to Address Orphan Pages

In some circumstances, the orphan pages you uncover may warrant a different approach.

### Set Up a Redirect

If the orphan page is an old page that’s been replaced with something new, you’ll want to implement a 301 redirect on the page.

A 301 redirect signals that the page no longer exists and its contents have been permanently removed or moved elsewhere. It will direct any traffic and bots from the orphan page to the updated or more relevant page, ensuring a smooth user experience and preserving any link equity.

For example, if you performed a site migration but an old URL is still live, redirect the old URL to the new page.

For more details, read our full [guide to using 301 redirects](https://www.semrush.com/blog/301-redirects/#how-to-use-301-redirects-to-boost-your-seo-performance).

### No-Index the Page

If the page was intentionally excluded from your website’s structure and navigation, consider applying a “noindex” tag.

“Noindex” refers to a snippet of HTML added to your page that tells search engines you don’t want them to index it.

The code looks like this:

`<meta name="robots" content="noindex">`

You might use this if, for example, you have multiple versions of a landing page that you’ve created for different ad campaigns. These pages aren’t meant to be navigable by normal website users, and they could be viewed as duplicate versions of other pages on your site.

This is a better alternative than simply “hiding” the page by not linking to it on your website. As we discussed previously, Google can still crawl and index pages via your sitemap.xml file or any other external sites linking to the page.

For more information on no-indexing content, read our full [guide to meta robot tags](https://www.semrush.com/blog/robots-meta/).

### Delete the Page

If the orphan page doesn't provide any value and doesn't align with your site's content, it might be best to delete it.

Review the orphan page to confirm it doesn't provide value to your site or users.

Keep in mind that if the page is simply outdated or has been superseded by a more recent page, you should consider the 301 redirect option above. This will help preserve any backlinks pointing to the orphan page as the link equity will be passed to the redirect target page.

## Monitoring Orphan Pages

You’ll want to regularly check for new orphan pages on your website.

Many normal activities, such as updating your site, launching new ad campaigns, or moving content around can inadvertently create new orphan pages without your realizing it.

This is one reason why Site Audit is set up to regularly re-crawl the website by default.

Following the instructions in the [How to Find Orphan Pages](#how-to-find-orphan-pages-on-your-site) section will create a report that runs automatically once a week.

But you can also customize the crawl schedule.

To do that, click “**Site Audit**” under “On Page & Tech SEO.”

![“Site Audit” in Semrush menu](https://static.semrush.com/blog/uploads/media/fd/80/fd80955584857508b7d43b6b21597d09/E-4cQz00QZccEEQtwaptU4fO-Il2pkY_LkF-Hpfk39bWt68wzdg4KZpGMtesGgcuV2jyo3J3fhMoaJQnCtbE4wTUmG9wZodhaqlrqaCYcco_CPt50bgZMH2DaPGD7MgmCqmoLUYQ8FYc7eS30O92ZY8.png)

You should see a list of websites that you’ve added to Semrush. Click the domain of the site from the list.

!["example.com" domain in Start Audit results](https://static.semrush.com/blog/uploads/media/e2/6e/e26e7e47aae9c0f66492bdf5f1a04820/wkVRAYafDP3VZud5X6q-Rb077H6mwGuuVifL0uuRSqd2UUhuJsHzSQfkVvgJXZYAZQ00yj_wO9Ux2mJ0tjdE4Oli16b1rn6xpGSfXtVk9o71cIA4Sxx6GLREdyqn6GeQWnxTV16jeySlNclx4VPI2P0.png)

From the “Site Audit” report page, click the campaign settings menu (gray button with a cog). Scroll down under the “Site Audit settings” section and click “**Schedule: Weekly, Every Monday**.”

![Campaign settings menu in Site Audit report page](https://static.semrush.com/blog/uploads/media/50/04/5004919f7a57277dce4dd991cf71ddf5/hxLYhbIL8fj60lNKnYs7AFkMyVpYcSdn2pyXZxYl7sTVaGduq2JKB-RGGZwPkMEIJt0bf0eyFU4AF3N__JpMjBAQweE88MGI2T99oun9Tq7TjwDWMp3oCJ_4Dl3qhaqCDYaFUZVDqqYRgMlljilN-ZU.png)

Now you’ll see the “Site Audit Settings” dialogue box. Click the drop-down that says “**Weekly, Every Monday**” to choose a new schedule. You can choose a different day for the crawl to run, choose to run an audit every single day (“**Daily**”) or turn off the recurring crawl by selecting “**Once**.” Click “**Save**.”

![“Site Audit Settings” schedule page](https://static.semrush.com/blog/uploads/media/c5/d1/c5d15dc7ae113e3d149bb2b56ca7e220/fNH_Q6UyN8goExL8goCyeAq5uyiUbFZqqBc8S3ibm7p9m2rL7V-nMyGxzQKkvEnqGemh3KXWTRrqrkDV_Dw4SUqQfklnq-zFaGTMKTIMXnR-HVW9U4C1EQgbeiSfFFMJIEpa8JUBRsDCaZZQzEJfDus.png)

Now Semrush will automatically crawl your website and look for orphan pages according to the chosen schedule.

The Site Audit tool isn’t just for finding orphan pages, though. It helps identify 140-plus other on-page and technical SEO issues. HTTP status code problems, meta tags, canonical URLs, and more.

## Frequently Asked Questions

### Are Orphan Pages Bad?

Orphan pages can create unintended SEO consequences for your website that can hurt your overall organic search traffic. Having pages that cannot be easily crawled could result in them not showing up in search results.

Plus, it can create a poor user experience.

### Should You Ever Create Orphan Pages Intentionally?

Yes. In some cases, it makes sense to create and maintain pages outside of your normal website structure. For instance, you may have special pages that you don’t want people to be able to find or access from your public website. These may include: landing pages for short-term marketing or sales campaigns; pages with downloadables shared exclusively with your mailing list; or sign-up pages for one-time events.

Keep in mind that these pages could still be accessed from other channels or by users typing in the URL directly.

### Can I Intentionally Create an Orphan Page to “Hide” It From Google?

No. Not linking to a page on your website does not guarantee that Google will not find or index that page. The page may still appear in your sitemap, which would allow Google to find and index it.

If you don’t want the page to show up in search results, apply a no-index tag instead.

### Are “Dead End” Pages the Same Thing as Orphan Pages?

No. Dead end pages are pages that don’t contain any outbound links, whether internal or external.

But unlike orphan pages, they do have inbound links. However, dead end pages are often considered to create a poor user experience and may be worth addressing as well.

### Can I Find Orphan Pages Without an Automated Tool?

Technically, yes. You could uncover orphan pages by downloading data from Google Analytics, Google Search Console, or your website’s log files, and doing a manual analysis. This process would likely be difficult and time consuming, depending on the size of your website.

### How Often Should I Check for Orphan Pages?

There's no fixed rule, but running the Site Audit tool on a weekly basis should catch most issues. Regular audits are an important part of your overall SEO strategy, and the Semrush Site Audit Tool can help.

Otherwise, it's good practice to perform an orphan page check whenever you make significant changes to your site, such as adding or removing pages, or restructuring your website.
