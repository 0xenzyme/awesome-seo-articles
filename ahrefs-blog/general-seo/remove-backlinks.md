---
title: "How To Remove Backlinks (And Clean up Your Link Profile)"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "remove-backlinks"
url: "https://ahrefs.com/blog/remove-backlinks/"
canonical: "https://ahrefs.com/blog/remove-backlinks/"
author: "Chris Haines"
published: "2024-02-13T14:53:32+00:00"
updated: "2024-06-18T11:31:35+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "date_2024_watch"
fetched_at: "2026-06-12T11:59:21+00:00"
status_code: 200
html_hash: "fb90e434cc228b5842c86d3abbdd9dfb052eef55f5aa128c55c876e1d8201591"
clean_word_count: 2459
clean_char_count: 14675
---
# How To Remove Backlinks (And Clean up Your Link Profile)

So, you’ve got some bad backlinks? Maybe you’ve paid for some shady links, or a competitor has targeted your website with [link spam](https://ahrefs.com/seo/glossary/link-spam). Whatever the cause, you’ll want to know what to do next—especially if you’ve received a [manual action.](https://ahrefs.com/seo/glossary/manual-action)

In this article, I’ll share how to remove backlinks and consider the different approaches for cleaning up your link profile—depending on your circumstances.

## How to remove backlinks—if you’ve got a manual action

[Google says](https://support.google.com/webmasters/answer/2648487?hl=en) if you have a [manual action](https://ahrefs.com/seo/glossary/manual-action) for [unnatural links](https://ahrefs.com/seo/glossary/unnatural-links), you should first try to remove the links from the other site and *then* disavow any that you can’t get removed:

> *“If you have a manual action against your site for unnatural links to your site, or if you think you’re about to get such a manual action (because of paid links or other link schemes that violate our* [*quality guidelines*](https://support.google.com/webmasters/answer/35769)*), you should try to remove the links from the other site to your site.”*
>
> Google Search Console Help

Here’s an overview of what you need to do to remove backlinks if you have a manual action for unnatural links, according to Google:

![what-to-do-if-you-need-to-remove-backlinks](https://ahrefs.com/blog/wp-content/uploads/2024/02/1-remove-backlinks.png)

### Check GSC for a manual action and start a backlink audit

If you’ve got a manual action (also known as a manual penalty), you’ll see it by logging into Google Search Console (GSC). Expand the **Security & Manual Actions** tab and click on **Manual actions**.

If there’s an issue, you’ll see a screen like this:

Assuming you have a manual action, the first step is to list all the domains you want to remove.

Start by heading to Google Search Console, exporting all the links, and adding them to a spreadsheet. These are the links that Google sees, so there’s no need to use a third-party tool at this point.

### Find the unnatural backlinks you want to remove

Once you’ve got your domain list in your spreadsheet, you’ll need to start a [backlink audit](https://ahrefs.com/blog/backlink-audit/) to identify the unnatural links. In your backlink audit, you don’t have to remove every spammy link, but it’s a good idea to look for common patterns to identify what caused the penalty.

Tip

If you aren’t confident in completing a backlink audit, ask a reputable [SEO consultant](https://ahrefs.com/blog/seo-consultant/) or an [SEO agency](https://ahrefs.com/blog/what-does-an-seo-agency-do/) to do one for you.

What constitutes an unnatural link, according to Google? In short, it’s any link that is intended to manipulate rankings in Google’s search results.

Such as:

- Paid links
- Excessive link exchanges
- Automated linking
- Requiring links as part of your ToS
- Low-quality directory or bookmark site links
- Keyword rich low-quality links embedded in widgets
- Widely distributed links in the footers or templates of sites
- Forum comments with optimized links

For a current list, check [Google’s spam policies](https://developers.google.com/search/docs/essentials/spam-policies#link-spam).

You can use a tool like Ahrefs’ [Site Explorer](https://ahrefs.com/site-explorer) to help find spammy or unnatural-looking links.

Here are a few checks you can make:

#### Are there any spammy-looking or over-optimized anchors?

In Ahrefs’ [Site Explorer](https://ahrefs.com/site-explorer), you can check the **Anchors** report in the sidebar. If there’s an issue—it can be fairly obvious from this report. Here’s an extreme example of easy-to-spot spammy-looking anchors in a digital marketing website’s link profile that looks unnatural within the link profile’s context.

#### Assess the overall quality of the domains

Does it look like a site that Google would approve of based on their quality guidelines?

Google has a whole section dedicated to defining link spam, but one of the core considerations is whether you’ve paid for links to manipulate Google’s rankings.

### Contact site owners to request they remove the links

Once you’ve identified the unnatural links, you’ll need to collect the email addresses for these domains. Usually, there’s a contact form or an email on the contact page, or you could try the [[email protected]](/cdn-cgi/l/email-protection#791f100b0a0d1718141c5715180a0d1718141c390d111c100b1d1614181017571a1614) approach. You can also use a tool like [Hunter](https://hunter.io/email-finder), or simply run a quick search on social media.

You should then request that they remove the links from their site.

Here’s an example of the type of email you can use to request removal – keep it short and to the point, and remember to send it from an email address that has your domain name in the email.

> Hi {site\_owner’s name},
>
> I’m currently reviewing links on my website, and I need your help to remove this link:
>
> {Their\_URL}
>
> It links to my website here:
>
> {Your\_URL}
>
> When you have removed the link, I would be grateful if you could respond to this email.
>
> Thank you,
>
> {Your name}
>
> {[[email protected]](/cdn-cgi/l/email-protection)}

Sidenote.

You can also ask site owners to add a nofollow tag to the links, but I’ve often found getting them to remove the link is easier.

Once you’ve removed a few links, you can start updating your list. Some site owners will not reply to your email. Others will agree to remove the link but charge a fee for the link removal.

In this situation, John Mueller has said:

> *“If there are some links that you can’t remove yourself, or some that require payment to be removed, then having those in the disavow file is fine as well.”*
>
>
>
> John Mueller, Search Advocate,

### Disavow any links you can’t remove

If you’ve tried to get the backlinks removed, but they can’t be removed, then you should [disavow the links](https://ahrefs.com/blog/google-disavow-links/).

[Google says](https://search.google.com/search-console/disavow-links):

> *“We recommend that you only disavow backlinks if you believe that there are a considerable number of spammy, artificial, or low-quality links pointing to your site, and if you are confident that the links are causing issues for you.”*
>
> Google Search Console Help

In a [now-deleted tweet](https://web.archive.org/web/20220106103717/https://twitter.com/JohnMu/status/1479038061275226112), John Mueller confirmed this by saying if you paid for links and can’t remove them, disavow them.

If you choose the disavow route, please heed these words of caution from Gary Illyes:

> *“We said multiple times that the disavow tool is a very heavy gun. And if you don’t know what you are doing, you can shoot yourself in the foot with it.”*
>
>
>
> Gary Illyes, Webmaster Trends Analyst, [Google](https://www.google.com)

There’s a risk with a disavow that you can tank your site’s rankings by disavowing the wrong links. So it’s important to be sure that the links you’re adding to the disavow file are causing issues for your site.

Google also [provides detailed guidelines](https://support.google.com/webmasters/answer/2648487?__hstc=20629287.57e7bd95bd4900ae1d1ba7b76587b39e.1692108714070.1705329078096.1706619298694.20&__hssc=20629287.1.1706619298694&__hsfp=501235727) for preparing your disavow .txt file, which you should follow.

Once you’ve got a list of domains that you think are unnatural, you should format your disavow file in this style:

```
# Two pages to disavow
http://spam.example.com/stuff/comments.html
http://spam.example.com/stuff/paid-links.html

# One domain to disavow
Domain:shadyseo.com
```

Then it’s just a matter of uploading your .txt file to [this page](https://search.google.com/search-console/disavow-links) in GSC.

Sidenote.

If you already have a disavow file, download it and update it instead. If you try to upload a new one, it will overwrite the old one instead of adding to it.

### Request a review

Once you’ve tried removing as many unnatural links as possible and uploaded your disavow file to GSC, you can request a review. You can do this by clicking the button **Request review**.

If Google decides you’ve done a good enough job, they’ll remove the manual action. If not, you may have to repeat the process until the manual action is removed.

Further reading

- [What is a reconsideration request](https://ahrefs.com/seo/glossary/reconsideration-request)
- [Fery Kaszoni - How to remove a Google manual penalty with one reconsideration request](https://x.com/FeryKaszoni/status/1756065638080991694?s=20)

## Should you remove backlinks if you don’t have a manual action?

If you don’t have a link-based manual action but you have links you want to remove, this is where it can become a gray area—and different SEOs will have different opinions on whether or not to remove backlinks.

Here’s an example of a blogger who says he had lots of “spammy” links but did nothing—and saw no negative impact:

> I started this site When Its spam scored 75 in Moz. Since then I just published articles, and I did not create any backlinks, No disavow or remove any links. [pic.twitter.com/wVBCI0HJL7](https://t.co/wVBCI0HJL7)
>
> — Fahim Foysal Prince (@FahimFoysalFFP) [July 29, 2023](https://twitter.com/FahimFoysalFFP/status/1685158483661139968?ref_src=twsrc%5Etfw)

Here’s another example where [Patrick Stox](https://ahrefs.com/blog/author/patrick-stox/) showed the [impact of disavowing links](https://ahrefs.com/blog/impact-of-links/) on Ahrefs’ blog.

This shows that disavowing links without a manual action can potentially reduce your site’s organic traffic and that links still play a significant role in rankings.

When [I asked SEOs on LinkedIn](https://www.linkedin.com/posts/chris-haines-seo_seos-how-do-you-deal-with-low-quality-activity-7154066182667464704--xMY?utm_source=share&utm_medium=member_desktop) how they deal with low-quality links, most said they either do nothing or disavow them.

The poll showed that only 8% of SEOs remove low-quality backlinks from the source. Most preferred to either do nothing or disavow them. This is not surprising because, as we’ve already seen, removing backlinks is not easy and takes time.

The approach of “I do nothing” may surprise some, but with [Fabrice Canel](https://twitter.com/facan) of Bing announcing [in 2023](https://blogs.bing.com/webmaster/september-2023/Bing-Webmaster-Tools-to-Remove-Disavow-Links-Feature-in-October-2023) that they’re retiring Bing’s disavow links feature, it seems likely Google will follow suit soon.

Fabrice said:

> *“We can now differentiate between natural and unnatural links, and we can ignore or discount the latter without affecting the former.”*
>
>
>
> Fabrice Canel, Principal Program Manager, [Bing Webmaster Tools](https://blogs.bing.com/webmaster/september-2023/Bing-Webmaster-Tools-to-Remove-Disavow-Links-Feature-in-October-2023)

So the question really is—how much do you trust search engines to make the right decision?

Let’s consider the following scenarios:

### 1. No manual action, but have seen a serious drop in traffic

- Start with a [backlink audit](https://ahrefs.com/blog/backlink-audit/) to see if there is any issue with the links if you believe you are at risk
- A drop in traffic could be caused by many things, not just links—check your technical SEO for any issues or any [Google algorithm updates](https://ahrefs.com/google-algorithm-updates)
- If there is a serious issue with links that you believe may violate Google’s quality guidelines, then you can remove or disavow them. Run a [Site Audit](https://ahrefs.com/site-audit) crawl to eliminate any [technical SEO](https://ahrefs.com/seo/technical-seo) issues.

### 2. A third-party tool says you have “toxic” links

- [John Mueller](https://twitter.com/JohnMu) said the concept of “toxic” links is made up, and his advice was to move on to more serious SEO tools:

https://twitter.com/JohnMu/status/1533697837703348224?s=20

- If you have used a third-party tool to categorize links in this way, it doesn’t mean that the links are necessarily bad for your website
- If there is a serious issue with links that you believe may violate Google’s quality guidelines, then you can remove or disavow them

### 3. You have many low DR links on your site you don’t recognize

- If you have a lot of low **Domain Rating** (DR) links that you don’t recognize, it’s usually nothing to be worried about
- Low-authority websites can and do naturally link to your website—just because they are low DR, it doesn’t mean that they should be removed or are “bad”
- If you are determined to remove or disavow, always manually review the sites in question before pulling the trigger
- In most cases, no action is required. Google and other search engines will deal with these types of links.

### 4. You paid for links and don’t have a manual penalty but have seen a drop in traffic

- If you’ve paid for links but *haven’t* got a link-based manual penalty, the best thing at this stage is probably to do nothing
- If you can’t sleep at night due to the guilt of your paid links, then you can disavow or remove them, but in most cases, consider what else could be the issue first.
- Run a [Site Audit](https://ahrefs.com/site-audit) crawl to check for technical SEO issues before you take any action with links. Do a backlink audit to work out if there is a link-based issue.

### 5. You’re the victim of a link-based negative SEO attack

- If you believe there are many spammy, artificial, or low-quality links pointing to your site, and you believe they are causing issues.
- In basic attacks, Google should be able to understand what is and isn’t a natural link. For more advanced attacks, you may need to remove or disavow.
- If you are at all unsure, always seek advice from an SEO professional before removing or disavowing any links.

## Final thoughts

Removing backlinks isn’t most people’s idea of fun—it often involves the same amount of blood, sweat, tears, and toil as building links, but minus the dopamine hit of getting a high DR link.

By contrast, a disavow can be updated quickly, so if you know what you’re doing, it’s not hard to see why some SEOs opt for this option.

And, of course, the simplest option is to kick back, relax, and do nothing—but to do so, you have to have faith in Google’s algorithms to figure it all out—but do you?

Got more questions? Ping me [on X](https://twitter.com/chris_at_b449) 🙂
