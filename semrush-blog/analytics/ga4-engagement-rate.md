---
title: "What Is Engagement Rate in GA4? + How to Improve It"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "ga4-engagement-rate"
url: "https://www.semrush.com/blog/ga4-engagement-rate/"
canonical: "https://www.semrush.com/blog/ga4-engagement-rate/"
author: "Zack Duncan, Christine Skopec, Simon Fogg"
published: "2024-11-04T10:31:00+00:00"
updated: "2024-11-04T10:31:00+00:00"
categories:
  - "Analytics"
freshness_reasons:
  - "date_2024_watch"
  - "time_sensitive_title"
schema_genre: "Analytics"
fetched_at: "2026-06-12T15:27:46+00:00"
status_code: 200
html_hash: "58de5ada0a6434cd8c1fc0550c9a36040d7529b3a00566509473989beb20012f"
clean_word_count: 2732
clean_char_count: 20663
---
# What Is Engagement Rate in GA4? + How to Improve It

## What Is Engagement Rate in GA4?

The Google Analytics 4 (GA4) engagement rate metric is the number of engaged sessions relative to the total number of sessions on your website—expressed as a percentage.

Here’s what the formula looks like:

**Engagement rate = (number of engaged sessions / total number of sessions) x 100**

A session is a visit. And an engaged session is a visit when the user interacts with your site in a meaningful way by meeting at least one of these criteria:

- The session includes a key event (the name for [GA4 conversions](https://www.semrush.com/blog/ga4-conversions/))
- The session includes two or more [pageviews](https://www.semrush.com/blog/pageviews/)
- The session lasts for at least 10 seconds

Let’s say your website has 1,000 sessions over a period of time and 546 of those sessions meet one or more of those three criteria. Your engagement rate is 54.6% ((546 engaged sessions / 1,000 sessions) x 100).

### Engagement Rate vs. Bounce Rate

Engagement rate is the primary way that [Google Analytics 4](https://www.semrush.com/blog/google-analytics/) measures user engagement.

[Bounce rate](https://www.semrush.com/blog/bounce-rate/) is another user engagement metric, but it takes the opposite approach. And measures the percentage of sessions that are **not** engaged.

**Bounce rate = (number of sessions that are not engaged / total number of sessions) x 100**

A session must either be engaged or not engaged.

So, in the example above, we know that 454 sessions didn’t meet any of the three criteria to qualify as an engaged session (1,000 sessions - 546 engaged sessions = 456 unengaged sessions). Meaning your bounce rate is 45.4% ((454 unengaged sessions / 1,000 sessions) x 100).

## Why Is Engagement Rate Important?

Engagement rate matters for two main reasons:

### Site-Wide Performance Insights

Monitoring your overall engagement rate helps you spot whether there are problems users are having on your website, so you can quickly address them.

To understand how, take a look at this GA4 graph showing a website’s daily engagement rate from January 2024 through August 2024.

The engagement rate mostly ranges from about 45% to 75%. But the number dipped below 20% in late March. Which likely indicates a user experience problem that was quickly addressed.

![Report on GA4 showing engagement rate over time to be between 45% to 75% except for a dip below 20% in late March which is highlighted.](https://static.semrush.com/blog/uploads/media/01/63/01631a6a278c9d18cb0e4a92d19587db/5c5db2dfcd029e2532d89c84f1c3c573/AD_4nXdTuudTzFwp_rC6tXgP3Bxx3xJtkJjm4huUB3XuQVP5rTTkSfCxWhhVQoGuTgOXZVcAKPo8DuLizl7MxzdScu7Mxyx_6Aa2Q7pt4WLBodc0A9tvyq1qlcR6Fk2ZcqehQdCKXgwTjGBhUjLVEricTIS0S-vs)

When engagement declines like this across your entire website, you should check for technical issues related to [page speed](https://www.semrush.com/blog/page-speed/), link implementation, etc. (We’ll go over how to find these later in this guide.)

Some other common user experience issues that could cause declining engagement include:

- **Too many** [**display ads**](https://www.semrush.com/blog/display-ads/): If you run ads on your site, a declining change in the engagement rate can help you spot when you’re showing too many advertisements
- **Site redesign problems**: You may have recently redesigned your site with the best intentions. But if you didn’t do adequate testing before launch, a declining engagement rate may tell you the new design is confusing your visitors.

### Page-Specific Performance Insights

You can also analyze engagement rates for individual pages and compare these data points against your site’s total engagement rate to spot poor-performers that need to be improved.

Here are the top 10 pages from a website with an average engagement rate of 47.59%. You can see that each individual page has its own engagement rate.

![Page path and screen class report on GA4 with the engagement rate column highlighted.](https://static.semrush.com/blog/uploads/media/bf/a0/bfa03cad6b5567091444fd15ac73a985/686ea4e21c3612a8233cd1b4d31c79c9/AD_4nXd0LojElsFWocr82tG9Os9P9jXv9v5SKaPPkbPsAb_uJ44QPOHQ29RrfHHiTeFzi1ibL-rIWhv4SR9JwG0BqKsOjnOkftBNEZxZCqrFahFb-EX66HBk5b1BuVGFsYfEVtNRI3nFiA8sKrfOho_uA940izH1)

Later, you’ll learn how to create this same report and how you can improve the engagement rates of your low-performers. And that can lead to better retention and more conversions.

## What Is a Good Engagement Rate in GA4?

The standard of a good engagement varies by industry and changes based on content type as well.

For example, you’d expect a higher engagement rate on a contact page than a highly technical blog post.

Across all industries and content types, the median site-wide engagement rate is [56.23%](https://databox.com/google-analytics-4-industry-benchmarks), according to a comprehensive benchmarking study from Databox.

That study included engagement rate data by industry. The lowest engagement rates were in consulting and professional services as well as SaaS industries. And the highest engagement rates were in health/wellness and ecommerce/marketplaces.

Here are average engagement rates by industry, ranging from lowest to highest

- Consulting and professional services 52.43%
- SaaS: 52.43%
- IT and software: 52.64%
- Food: 53.74%
- Real estate: 54.13%
- Technology: 54.71%
- Construction: 54.92%
- Education: 57.19%
- Manufacturing: 58.33%
- Healthcare: 59.97%
- Apparel and footwear 60.23%
- Automotive: 60.36%
- Travel and leisure 61.55%
- Health and wellness: 62.22%
- Ecommerce and marketplaces 63.86%

## How Can You See Engagement Rate in GA4?

In GA4, you can view the average engagement rate for your entire site as well as specific engagement rates for each page.

You’ll find your site-wide engagement rate in your Traffic acquisition report. And you can customize that report to focus your analysis on engagement rate.

Here’s how:

In the left-hand navigation, click “**Reports**” > “**Acquisition**” > “**Traffic acquisition**.”

![Navigating to the Traffic acquisition report on GA4 by clicking on "Reports" and selecting it from the "Acquisition" drop-down.](https://static.semrush.com/blog/uploads/media/14/50/14502883c175aa5a296262183a4beda9/b9f0b2ae8ec571dd3c064083a8a1a5b0/AD_4nXf2S5-xm4pQarKErkjjB4xMKj1S6mU_M-N_u4ivVAFwk8ZFvbFTAW42aGoMJ1xGsAJLwC__iWgk41bHQHZzW1egltGpmGwqrViHYghExA94w4330pf1F8LcH57oY8Z0va51VmPve1CqBs2gB9gH66NSVRIq)

You’ll see the following report that shows how your website acquires visitors (indicated as “Sessions”).

The small drop-down arrow to the left of the “Sessions” column header indicates that this metric is sorting the data table and is what’s being displayed in the graph.

![Traffic Acquisition report on GA4 with the sorting arrow next to "Engagement rate" highlighted.](https://static.semrush.com/blog/uploads/media/a7/8f/a78febedd60971cc81ae3531e20f405b/53527ac2d161d125e88a811ca920efdb/AD_4nXfHU0l-tL6b2eCv-p5SRBRE3w43akC8Kj45Gs_qBJRQhcPKZf_sRCZPlOKs_HNo_t8KOxmTYVnotpPxAemDOIjGCzlHdv53b2Tecy55V0nULZ5DNHIQ4pPzc6p696jkDymNYvI_hoeXjjBHeXhsSDU3H_BO)

Click to the left of “**Engagement rate**” to sort by that metric instead.

Now, uncheck all the boxes except for the one to the left of “Total.” Then click the “**Plot rows**” button.

![Traffic Acquisition report on GA4 with the "Plot rows" button clicked.](https://static.semrush.com/blog/uploads/media/ac/a7/aca7671be88cc53fb434a233beae6eab/1a96057a5b8379711736392ddd98c730/AD_4nXcjxlFKovsFBWY5kHoGJSo5kfeh139WeP5Ku1_3JMW41QuKk9NBK9upfOVuRKVmMaw4BpnDenDf-QnSisN6IKM7lcNoBb_fEGwT5_I6k2O1iwejUMDWuYG9hWgfISXmRFViiTX6XeauPdazE9HJF-LpX7k)

You’ve built a graph that displays the total engagement rate of your whole site over time. And you can click on the date range in the upper right to analyze specific periods you’re interested in.

![A graph showing the total engagement rate of a site over time with the date range filter in the upper right corner highlighted.](https://static.semrush.com/blog/uploads/media/82/f2/82f29b408652fa9389bd4fa334697fac/7e48a932329321a32e9943a034744f1b/AD_4nXfiiiRsAs2vmYlZHgnVQIvYUzZaMImqHBrq24wQPSOfodzX5aasCjUz_jzP6PrDBR3SDz4iWzbhOx_xDn8s-P_wk83pKb8GfFi8FQIkoe89aZwjSX3W34NBd4M1e2ZrqP_9HmEZ84oaDQBVjcnvOwIHhOrr)

A box appears where you can select your date range. You can manually enter the date range you’d like to view or choose from the list of predefined date options.

Click “**Apply**” when you’ve selected your desired range.

![Date range filter on GA4 with "This year" selected from the list of predefined date options and "Apply" clicked.](https://static.semrush.com/blog/uploads/media/47/10/47100f79ee364a7f4f16c21402e2d523/862c27e29d8b53daf98a10267245dc0a/AD_4nXc0ScE_KPMgM-IsBSJ2K8ltjvdoK9AvWfuCwLm3hIyUFg5eKp498u1n-wfAyvUSVD0WlcJP1g58QKe17VMEZGnIkZ2l_1iId2aJh-apPCwFe2jCOyV8uvxrzj-EGbxJMFj8fkN_IYN7hJdA4MQ5GADnGPrj)

Your engagement rate graph will rebuild.

For further customization, click the box below the data range selector to choose whether to graph your engagement rate data at the daily, weekly, or monthly level.

![A graph showing the total engagement rate of a site for the last year with the data range selector highlighted.](https://static.semrush.com/blog/uploads/media/15/73/1573796237cdbafd1f0fe6ba7a1c5e1f/4db55afeb0cda6d7573cd988fa32d208/AD_4nXfBfKDIFG0aEtVz3iErn0jZ31QdGMwSDOPjowBeQlVSnwGd_nG_fuYUO49sfCk2WtfQ1va_oyouQpheaj06aLMLLbitDgbuyOaJmSwn-LZaHGPTb6lTYicSqhV6Pu5hW75Tl1ppiyrNrOwBp-ghngC22F6S)

To see your page-level engagement rate, go to “**Reports**” > “**Engagement**” > “**Pages and screens**.”

![Navigating to the Pages and screens report on GA4 by clicking on "Reports" and selecting it from the "Engagement" drop-down.](https://static.semrush.com/blog/uploads/media/a2/0c/a20c399053acf7d3f439de577b8afbb9/3c72a0825d994eef6069e9e6c53a7e4b/AD_4nXcS5FCKY0WFpnmbE1tUWCUOpb62VGT91dgYIhiAV5yRVKmrLW8LstVLMhwjlVdDM8Pf8UuigQeXrGr5s5xfxOwyDL9yAMgRK9ShkCEv2oF-yTiiEFwRhoF8G7FLIIdPdlOBBkUtWyeGtqckbn66wiLQa6Ix)

You’ll see a report like this showing your top pages.

Click the pencil icon in the upper right corner to customize the report and add engagement rate (GA4 will then always show that metric in this report).

![Page path and screen class report on GA4 with the pencil icon, to customize the report, on the top-right corner highlighted.](https://static.semrush.com/blog/uploads/media/af/ab/afab0ab60757f506d84eea15473e3862/b2f69c091c222296fbf21646a70567fa/AD_4nXeSbtHkSGdqTQzQye1kIAcDIGpdRfFOLs7YnzAxJl86w2itJnRP2eAj2Ec4XTrZSMNBRRzYna_WyvzruOCNPW_2pfdQFnQMbihCZnAWEDO4X3FM3T26jCwdIKAg29WGgCtI2lofursP1jMRORlCJblitIof)

Now, click “**Metrics**.”

!["Metrics" selected from the "Customise report" menu on GA4.](https://static.semrush.com/blog/uploads/media/97/43/97431b6e24fd8bed6df9765374edcc37/dacff73cbbe83b1ab80b5f02f09efa44/AD_4nXdw8Jy1cJMG9IXEWiLN2pr-_b0QuzRnCt2gGr2Bz3wiVU0s2wvrijbGiEl6mQNoptwjDqEs7sMScfZ_YjBUIaREzN593MwvnT20Oz5wvDsoE-jCungkICIrkONUZX31QSGrV9HypBZ5gW4B4okcnsPuZClu)

You’ll see the list of metrics available in your report.

Click “**Add metric**,” begin typing “Engagement rate” and select it in the drop-down once it is available.

!["Add metric" clicked, "engagement" typed, and "Engagement rate" selected from the drop-down in the "Customise report" window on GA4.](https://static.semrush.com/blog/uploads/media/70/b4/70b45ed6088a7513c557e872589bf8c3/a592954527edf84074dd73eaa6ee030d/AD_4nXc8uVAG5cITBQ0NJlgeAuBNECqLDw9_hI9ufAUOtp-iaqHTpuiYtV8cJKnmy-R60APqRkDYsJcNB3IVc39aE1jqzN3Lzd_ab0LyxqSkys_X3a__5b0JYolHpfbFYtt1pGBMqZhudXOgllz4HaH-nGjH7by0)

Once you’ve added engagement rate to the report, click and hold the “Engagement rate” metric and drag it toward the top of your list of metrics and place it just below “Views.”

Now, click “**Apply**.”

!["Engagement rate" moved to the top of the list of metrics just below "Views" and "Apply" clicked in the "Customise report" window on GA4.](https://static.semrush.com/blog/uploads/media/62/10/62106a295ff16e204c866dbe0645f4a3/ff7a6689e1a0d2719d57e31b31b4f40f/AD_4nXflbn6WnQlh-YhEM4R9jy8iKXploKekxws5Rb39ejJ0CP2TcdA_s3W1g6f926jMkz6K6QRmby2Z1Nu7DgYNVRRcIaoKX5FRenjMGswD7UQIFS_eCPXDvNzZDsHTCEqIo97QuWFmKsPG50GtNYFqb9-dxyOp)

Click “**Save**” followed by “**Save changes to current report**” at the top of your report to make the change permanent.

!["Save" clicked and “Save changes to current report” selected from the drop-down to make permanent changes to a report on GA4.](https://static.semrush.com/blog/uploads/media/61/50/6150934b1e3c60b594fac0c48a55f03b/706441684d69cd0d6fddf21afd011fb3/AD_4nXcTrcE3s13Uky9SEiHFC6GXaLCj3Zkdu50S2jou7U1Z7zeymGGErhQuDH9PoYKol9pQs6xRBmPM2skV58jLuWJO8emCv3VXHvBKbnqjO_vEVcnqrrkXkhCRVxxh_YIoBJPsc5BHmmj0Ba2dxceM8VDCPCar)

And click “**Save**” again.

![Window you see after clicking “Save changes to current report” with the "Save" button in the bottom-right corner clicked.](https://static.semrush.com/blog/uploads/media/e5/00/e500fcc801a371ecff450bcb753ec036/66f7192411e11e088ca5d0c33095cb60/AD_4nXc67NhR55uW066A_KT_ImHKkCK5eEAwCImjw059nY4atsmJMaPKodD28NKtsdXYfEH91GniUG5xUE5pm7-sWYFETXRS3dZsRKzmzd09psdT6jL4AgaqWaOlKTGqaitHXI025lDAmfCOWAT-chUyqp7W46yA)

Now that you’ve added engagement rate, Google Analytics enables you to compare performance across pages.

## 4 Ways to Improve Your Engagement Rate

A healthy engagement rate makes for a healthy website that can turn visitors into customers.

Here’s how to use engagement rate data to improve performance:

### Improve Your Low-Engagement Pages

Now that you’re able to see engagement rates for different URLs, focus on pages that are viewed often but have low engagement rates. These represent great opportunities to improve your entire site’s performance.

In the table below, you can see that the second and third pages listed have engagement rates far lower than the site’s average.

![Engagement rates for different pages of a site with two pages with engagement rates lower than the site's average highlighted.](https://static.semrush.com/blog/uploads/media/cd/41/cd41bebbc8e92433992b641cfc931c4e/194b6c140e842b884c1f9c0f8bf20e2b/AD_4nXeM6Q-n6cK2nn4wyTVMhvUayWoNkixEy1ocSx6MWktAo24tgt1lA3WQvqCZdWREIJfgWiMOObwwQpXmbhaG64cCnwLgHl4lLrUuM_OYm2dR9VbIunyqs5QDWrVV7fGgPnYF-2dxArU956qYQ8jfCEsdXUQ)

Once you spot candidates like these for improvement, it’s time to fix them.

Visit those pages and study them carefully. To identify potential pain points your visitors are facing.

Based on what you see, you could:

- Update your H1 to make sure it accurately reflects your page
- Revise your introduction to make sure it’s as short and helpful as possible. You can even remove it entirely if it doesn’t add value.
- Add images and increase whitespace. Pages with a high text density tend to have low engagement.
- Add relevant [calls to action](https://www.semrush.com/blog/what-is-a-call-to-action/%20x) (CTAs) on the page. Keep in mind that a click to another page on your site automatically makes a session engaged. And review your links’ anchor text, so they grab attention.

As you implement page-specific enhancements, you’ll see engagement rates climb.

### Fix Technical Website Problems

Technical issues like broken links or slow page speed can keep your visitors from having a positive interaction with your site. Which means fixing these kinds of problems leads to higher engagement rates and happier visitors.

How do you discover these problems?

Use our [free SEO checker](https://www.semrush.com/siteaudit/) to run a quick check and spot any red flags. For a full scan on your entire website, use Semrush Site Audit. This tool performs over 140 checks to analyze your website's health.

It catalogs your website problems into errors (the most important to fix), warnings, and notices. And it includes the “Site Performance” report (click “**View details**” to go to it), which shows you how to improve your site speed.

!["View details" under "Site Performance" on the Site Audit report clicked.](https://static.semrush.com/blog/uploads/media/88/75/8875a73de63d465e48c18a30a7e0dfe7/6d4efc525b5ce99e3224306229f9b800/AD_4nXf0QRyLazDB5-twJBiUQ1blpXVAn3Vz0zlMpOGj_TGxTcO0xMXPHSHhTkEM0pECYvaCyR29cDmntLFgjr-b-cRRbS_QvfFvMBImQAzD0dX2Pl8nQYCKe6dy_qbWRSQ23dEvoEfgVj7Xewjh9cHy7C_Gi34)

It groups those performance opportunities into the same errors, warnings, and notices categories. And keeps track of your average page load speed over time, so you can see your average page speed increase as you implement fixes.

![Site Performance report on Semrush showing performance issues for a site along with metrics like page load speed over time.](https://static.semrush.com/blog/uploads/media/88/f6/88f6ef37680b70dde7260b61ff762192/e99f4a63969603faf79dd17330b96ed9/AD_4nXcAO3s2WPjfBoSDa4EyrL1kNhSlzRWpDPphpjdCgcSXBDiWO63YKLIZpNwvlNI6EYmykTyU41uvcCAZNNXqxgzjQMTuocyCKuRwbFJlvhaSUV-UDJaQ4Gw0Q_fAArAIThpTsE8jK60MFPZuGm_wRsUa1B9J)

Faster site speed is better for the user experience (UX), and improved [UX can help SEO](https://www.semrush.com/blog/ux-and-seo/). So, you could be helping more visitors to find your site.

### Create New, Relevant Content

Publishing for the sake of publishing is unlikely to lead to positive results. But focusing on new content centered on topics your [target audience](https://www.semrush.com/blog/target-audience/) actually cares about is a great way to get more organic traffic and boost engagement.

Use [Topic Research](https://www.semrush.com/topic-research/) to generate content ideas.

Just enter a general topic your business is focused on and click “**Get content ideas**.”

![Topic Research tool start with "google analytics 4" entered and "Get content ideas" clicked.](https://static.semrush.com/blog/uploads/media/e5/34/e534974a25485c2375e70d9fe378f976/b732832d0085605543c82ebf961b436e/AD_4nXccGd3OO_EAEYGVypjLhaDV62clyvinLxrAjj4WC7hNL6MuWPjGZyq5MEgyr9qpW8ltKVHD0zkVSGe8uppLH1MM0ZkpSnNZO7Vi4zjKaSaO8_iBh98x5kBo-PlozrpI_G7t9rHgiyL831YyGlXEvHuPxnEV)

Here, you can see a bunch of related subtopics. Along with information about the [keyword search volume](https://www.semrush.com/blog/keyword-search-volume/), top headlines, etc., for each subtopic.

Keep an eye out for any cards that are green rather than blue. They represent topics with high topic efficiency—which measures search volume relative to ranking difficulty to help you find promising opportunities.

![Content Ideas on Topic Research showing related subtopics for a seed term along with keyword search volume, top headlines, etc.](https://static.semrush.com/blog/uploads/media/8d/23/8d236cbe02620232f863dad94cb12244/2f2646170643569083ac45ff5c2fb09e/AD_4nXdKfrPph3Vivwj4AVWtlaXDMt_KMf9TsDcWnGbhQAWuw3imVLqR-ZkBAkR0l4dVUSJD6287dDBGoxGdO2Lpt8C_dbgdmj_ohX85gOpv56T4YNIn0jLFf3HtTD820kDCtGCaJRl6skafOOaeJWIHpWVoY9Jm)

And keep [search intent](https://www.semrush.com/blog/search-intent/) (what the user is trying to achieve with their search) in mind, so you can write with an eye toward what your audience is looking for.

### Make Sure All Your Content Is High Quality

[High-quality content](https://www.semrush.com/blog/quality-content/) is accurate, clear, and helpful to your audience. And it’s key for keeping your audience interested.

[SEO Writing Assistant](https://www.semrush.com/swa/) (SWA) can help you create great content.

It grades your writing for readability, originality, tone of voice, and SEO. And comes with AI features to help rephrase and compose your text—which you can then review and adjust to save time while you write.

![Text entered on SEO Writing Assistant with grades for the content on readability, originality, tone of voice, and SEO.](https://static.semrush.com/blog/uploads/media/e4/55/e455ca19889653391f256739820a1cb9/ca93e1d56b780a7d7aae2d63fc08cf0b/AD_4nXffnlGlKOTfnso8eYfSZ6YZJOsES_dxJopQUTA0heYL7hILMMW-dqeWOPk_AiuhY5fIQqhK0vmJEL8a8akmtBT9nNdjStVADc1L5gZX912upG7EILP3hBhlJWmJIlOW9ZsxxjbXp71egY-aFN-DEcIL1VXp)

You can also use the SEO Writing Assistant to improve existing pages that need complete rewrites. Copy the text into SWA and use the AI Smart Writer features to improve your content quality and possibly boost engagement.

## Make Your Site More Engaging

An engaging website makes it easy for visitors to interact in ways that lead to conversions, which means it ultimately benefits your business.

Semrush offers a variety of tools that make it easy to create new, high-quality content and improve your existing pages, both of which will likely improve your average engagement rate.

Ready to try it out?

Start your [free trial](https://www.semrush.com/signup/get-free-trial/) today.
