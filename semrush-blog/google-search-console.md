---
title: "Google Search Console: The Ultimate Guide for 2026"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "google-search-console"
url: "https://www.semrush.com/blog/google-search-console/"
canonical: "https://www.semrush.com/blog/google-search-console/"
author: "Sergei Bezdorozhev, Carlos Silva, Christine Skopec"
published: "2019-10-30T07:00:00+00:00"
updated: "2026-02-12T11:35:00+00:00"
categories:
  - "General SEO"
freshness_reasons: []
schema_genre: "General SEO"
fetched_at: "2026-06-12T15:58:08+00:00"
status_code: 200
html_hash: "64df71a7067cc4ee2e243a67f58469a7ef0fb76206fe4abc989eda5d88ccca51"
clean_word_count: 3788
clean_char_count: 26524
---
# Google Search Console: The Ultimate Guide for 2026

Google Search Console reveals whether and where your pages appear in search results. And includes some handy technical tools.

This guide explains what Google Search Console does, how to set it up, and how to use its reports to improve your search visibility.

## What Is Google Search Console?

Google Search Console (GSC) is a free [Google SEO tool](https://www.semrush.com/blog/google-seo-tools/) that helps you monitor your search performance and technical SEO health.

GSC reports on metrics across traditional search results, AI Mode, and AI Overviews. Like position in search results, clicks, and the Core Web Vitals (user experience metrics). These insights let you diagnose problems and improve how your site appears in Google’s various search experiences.

Here are some of the key things you can do with GSC:

- Review how your site is performing in Google Search, across traditional listings, AI Overviews, and AI Mode
- See which pages Google can crawl and index
- Submit sitemaps and individual URLs for discovery
- Identify and troubleshoot technical SEO issues

## How to Set Up Google Search Console

To access Google Search Console, [sign in to Search Console](https://search.google.com/search-console) with your Google account and add a property—the website you want to monitor.

You have two options when setting up Google Search Console: add a domain property or a URL prefix property.

### Add a Domain Property

Adding a domain property gives you the most comprehensive view of your site in GSC because it includes all protocols, subdomains, and paths under the domain.

When you add a domain property to Google Search Console, you have to verify ownership through your domain name system (DNS) provider. This confirms you control the domain and allows Google to collect data across the entire site.

To add a domain property, choose the “**Domain**” option in the property setup screen and enter your root domain (without http, https, or www). For example, if your domain URL is “https://www.yoursite.com,” enter “yoursite.com.” Then click “**Continue**.”

![Domain property entry form highlighted, domain entered, and arrow pointing to Continue button.](https://static.semrush.com/blog/uploads/media/ed/f4/edf4ee72aaa2d5a51fce48bda73794fe/e58602b7846ef8066b57d3c5852bedf0/image.png)

Copy the TXT record provided by GSC to add to your DNS configuration.

![Google Search Console screen showing a TXT record for DNS domain verification and arrow pointing to Copy button.](https://static.semrush.com/blog/uploads/media/f0/c6/f0c6d3a2afb9d2a32c588a4899bbbb22/a94910e8f06b5a6d80be656e33e1e109/image.png)

Open a new tab, go to your domain registrar, and locate your DNS settings. For this example, we'll use GoDaddy as our domain registrar.

Access your DNS settings in GoDaddy by clicking on the nine dots beside “My Account” in the navigation bar, and clicking “**Domains**.”

![GoDaddy account menu highlighting the Domains option under My Account.](https://static.semrush.com/blog/uploads/media/b1/af/b1af82ee108d8236e7608ef40ca86e3e/9999a5ca97fa082e0d0c4207c629e5da/image.png)

In your GoDaddy Domain Portfolio dashboard, select the three dots beside your domain name and click “**Edit****DNS**.”

![GoDaddy domain portfolio menu with the Edit DNS option selected for a domain.](https://static.semrush.com/blog/uploads/media/0f/a1/0fa14aa1d18daecbd3d2cd7ac58437ab/3d53136ebd85e5cf205b709e23b06285/image.png)

You should now be in the “DNS Management” window. Add a new TXT record by clicking “**Add New Record**” in the “DNS Records” section.

![GoDaddy DNS management page highlighting the Add New Record button.](https://static.semrush.com/blog/uploads/media/b7/f0/b7f08f18b066803a75c1b902df2f0e54/3fefcbe494bb74a42593168a0796f21f/image.png)

A “New Records” form will pop up. Add your TXT record using the values supplied by Google:

- **Type**: TXT
- **Host/Name**: @
- **Value**: [Paste the TXT record from Search Console]
- **TTL**: Default or 1 hour

When you’re done, click “**Save**.”

![TXT DNS record form showing Google site verification value and TTL settings and arrow pointing to Save button.](https://static.semrush.com/blog/uploads/media/b4/8b/b48bfd79327dc9b7febbdbe8507895bc/4eb9887d0b3dbb0d7161b8253a0c5b93/image.png)

After adding the record to your DNS configuration, return to Search Console and click “**Verify**.”

![Google Search Console DNS verification screen with the Verify button highlighted.](https://static.semrush.com/blog/uploads/media/13/1b/131b05f4ad6474ef9099e965c91fd8fc/6597fbfd09980c085f5447d7556aab10/image.png)

DNS changes can take anywhere from a few minutes to up to 48 hours to update. If verification fails at first, wait at least an hour and try again by selecting the property from your GSC dashboard.

![Google Search Console property selector showing verified and unverified domain properties.](https://static.semrush.com/blog/uploads/media/f6/01/f60134bbe666b41170aa76ffe10d206a/d0a22cd2907eb39ebdf9323d16ed4423/image.png)

Once you’ve successfully verified domain ownership, you’ll see a confirmation message and your property will begin collecting data.

![confirmation message](https://static.semrush.com/blog/uploads/media/70/47/70478550717dd26eee82e0497f3f04ca/7cc586131c81b8aa5db87972e692ef39/image.png)

### Add a URL Prefix Property

Adding a URL prefix property is useful when you want to track data for a specific section of your site, such as a blog subfolder.

To add a URL prefix property to GSC, click the “**URL prefix**” option, enter the full URL (including protocol and path) into the field, and click “**Continue**.”

In this example, we’ll use “https://www.yoursite.com/blog/.”

![URL prefix property card in Google Search Console showing a specific folder URL entered.](https://static.semrush.com/blog/uploads/media/06/32/0632f2923b1625a12311b1e98c580e04/f599daae117a7cf541afab7f83a3f77e/image.png)

Google supports multiple verification methods for URL prefix properties:

- HTML file (recommended)
- HTML tag
- [Google Analytics](https://www.semrush.com/blog/google-analytics-keywords/)
- [Google Tag Manager](https://www.semrush.com/blog/google-tag-manager/)
- Domain name provider

In this example, we’ll use the “HTML file” verification method. To do this, download the provided file.

![download button](https://static.semrush.com/blog/uploads/media/04/7d/047def731b3e89b27a31bcba6098fe43/66c6d1a8699462a942539f02a56a1386/image.png)

Upload the HTML verification file to the root directory of the website you’re verifying. The root directory depends on the URL prefix you entered. For example, the root directory is “/blog/” if you’re verifying “<https://www.yoursite.com/blog/>.”

Once the verification file is uploaded to your root directory, return to GSC and click “**Verify**.”

![verify button highlighted](https://static.semrush.com/blog/uploads/media/78/9a/789a30a761f944198bc01c96c087d93d/83df3e8d33cee5761afd0aa877a379dc/image.png)

As with domain verification, you may need to wait a bit. If you aren’t able to verify your site right away, try again later—Search Console will try to automatically verify the property.

![Google Search Console property selector with unverified URL property highlighted.](https://static.semrush.com/blog/uploads/media/75/d1/75d18b820e9f654352e5a81eede452c3/b001c394b59489db4dcff1ca52e4bf56/image.png)

## Owners, Users, and Permissions

Your permissions in Google Search Console determine what you can control and depend on whether you're an owner or a user.

Owners have full control over a property in GSC and can view all data, configure settings, use every Search Console tool, and manage other users.

There are two types of owners in Google Search Console, both with the same permissions:

- **Verified owner**: This owner is the person who verified ownership of the property
- **Delegated owner**: This owner was granted access by a verified owner

Users can access Search Console data, but their permissions are more limited than an owner’s.

Google Search Console user roles are:

- **Full user**: This user can view all data and take certain actions
- **Restricted user**: This user can view most data but is otherwise limited
- **Associate**: This user can’t access Search Console directly but can perform specific tasks depending on the association

### How to Add a User and Grant Permissions

If you’re a property owner and want to add a new user, go to “**Settings**” > “**Users and permissions**.”

![Users and permissions](https://static.semrush.com/blog/uploads/media/30/53/30539c00d38e3d92b6fe7f0856f0b6f7/c8c113b77ec754eea377083e0bf877bf/image.png)

From the “Users and permissions” menu, click “**Add****User**.”

![Google Search Console Users and permissions page with the Add User button highlighted.](https://static.semrush.com/blog/uploads/media/18/37/18374e619a02039e649789e7247c60f5/b2b279d8fb8810e67536e056658a00bf/image.png)

Enter the new user’s email address, choose an access level, and click “**Add**.”

![add new user’s email address](https://static.semrush.com/blog/uploads/media/bb/ac/bbac6e7c372af21f50e732b195dbda2b/1b3537b28358431641598244a4a5e25d/image.png)

Once added to Google Search Console, the user can access your property.

## How to Add a Sitemap to Google Search Console

To add a [sitemap](https://www.semrush.com/blog/website-sitemap/) listing the pages you want in search results that Google can use to more efficiently crawl and index (find and store) your pages, go to “**Sitemaps**” in GSC, enter your [XML sitemap](https://www.semrush.com/blog/xml-sitemap/) URL, and click “**Submit**.”

![Google Search Console Sitemaps page showing a sitemap URL entered and arrow pointing to Submit button.](https://static.semrush.com/blog/uploads/media/23/19/231929c2aa29408804b8c50041d0d51b/54af99cbb0ff5ab5b4eae987d57c52d5/image.png)

Once Google processes your sitemap, GSC shows a status message indicating whether the sitemap was submitted successfully or contains [errors](https://www.semrush.com/blog/google-search-console-errors/).

![sitemap submitted successfully message](https://static.semrush.com/blog/uploads/media/a3/8f/a38ffbd93b24a767c6b30939ebab0de2/4480de65f0d9ceafe5449581775111c4/image.png)

To make sure your sitemap is properly set up, run a crawl-based audit of your site using a dedicated SEO checker like Semrush’s [Site Audit](https://www.semrush.com/siteaudit/).

After Site Audit has crawled your site, open the “**Issues**” tab and search “sitemap” to see if any errors or warnings appear. If so, work to fix them.

![Semrush Site Audit Issues tab showing sitemap errors and warnings.](https://static.semrush.com/blog/uploads/media/8b/66/8b66430b6d631299f65880464834f79c/893388490b90460ca9d58a2b4d6649bd/image.png)

## Google Search Console Reports and Features

Google Search Console reports show how your site performs in Google Search, which pages are indexed, and where technical or experience issues can affect visibility.

### Performance Report

The Performance report shows how your site appears in Google’s traditional search results, AI Overviews, and AI Mode as well as how users interact with those results.

Just know that GSC doesn’t report on metrics for AI Overviews or AI Mode separately.

Click “**Search results**” in the left-hand navigation in GSC to view the Performance report. The report shows four metrics:

1. **Total clicks**: How many times users clicked your search results
2. **Total impressions**: How often your results were displayed to users
3. **Average** [**click-through rate**](https://www.semrush.com/blog/click-through-rate/) **(CTR)**: The percentage of impressions that resulted in a click
4. **Average position**: Your average position in search results

![GSC performance report](https://static.semrush.com/blog/uploads/media/78/4a/784a78f7bea0f100adc4660a057ff037/faf838c224abb069e49bd327b8ae15c3/image.png)

Below the chart at the top of the Performance report, a table breaks down performance by queries, pages, countries, and devices. And you can review trends over time to identify visibility issues worth exploring.

![queries, pages, countries, and devices](https://static.semrush.com/blog/uploads/media/43/88/4388600508b2e3f08cf7edf6494712bf/9bb317bbb0bf2632c484255595a5c294/image.png)

When analyzing the Performance report, look for the following:

- **Low CTR**: Pages with strong rankings but low click-through rates may benefit from clearer title tags and meta descriptions. That said, CTR may also be lower among AI-powered results.
- [**Missing keywords**](https://www.semrush.com/blog/google-search-console-keywords/): If important queries are absent from the report, you may be missing out on opportunities to drive more visibility

If your site appears in Google Discover or Google News, you’ll see separate reports for those surfaces within the Performance section.

### URL Inspection Tool

The URL inspection tool lets you check whether a specific page is indexed by Google and diagnose issues that may prevent it from appearing in search results.

Access the URL inspection tool from the top bar or by clicking “**URL inspection**” in the left-hand navigation.

![inspect any url](https://static.semrush.com/blog/uploads/media/98/ba/98ba74f3f6bf5269a004e7e62763d06c/e94c2c28315dae79103c44bca4224e58/image.png)

Paste the full URL of the page you want to analyze into the search box and press “enter” or “return” on your keyboard.The Page indexing tool shows key information about the page, including:

- **Index status**: Whether Google has indexed the page
- **Last crawl date**: When Google last crawled the URL
- **Structured data**: Whether structured data is present and error-free

![Google Search Console URL Inspection showing the page indexed and available on Google.](https://static.semrush.com/blog/uploads/media/25/a0/25a0d9f3290f2a2bcacb1bb8a0755512/8a6990498159a1a86231b758cf165385/image.png)

The tool also lets you test a live version of a page to see how [Googlebot](https://chatgpt.com/g/g-p-67a60f924c9c819185ba0729cad9b307/c/69777ec8-4f38-8330-adf7-9f385fcef0e0#:~:text=5.-,https%3A//www.semrush.com/blog/googlebot/,-Best%20placement%3A) views it.Just click “**Test Live URL**” in the top-right corner of the screen.

![test live URL](https://static.semrush.com/blog/uploads/media/74/ff/74ffffee780b168ea7665d6aa1ae4197/04a88e7d3539c32d91a1f86432d23520/image.png)

From the results page, click “**View Tested Page**” > “**Screenshot**” to see how Google renders the page.

![Google Search Console live URL test showing a rendered mobile screenshot of the About Us page.](https://static.semrush.com/blog/uploads/media/41/65/4165b2cb4b9c9e9d908a664f7bb6ee34/8acc6ecef270d1a9ae9eef228d71ac74/image.png)

If you’ve published a new page or made significant updates, you can even request indexing directly by entering the full URL in the inspect search box and clicking “**Request****Indexing**.” This prompts Google to re-crawl the page sooner, but you should know that indexing isn’t guaranteed.

### Page Indexing Report

The Page indexing report shows which pages on your site Google has and hasn’t indexed and provides details about issues preventing pages from being indexed.

Pages must be indexed to appear in search results, so it’s important to avoid any indexation problems.

You can find the Page indexing report under “**Indexing**” > “**Pages**” in the left-hand navigation. The report separates URLs into indexed and non-indexed pages, helping you spot coverage issues quickly.

![indexed and non-indexed pages](https://static.semrush.com/blog/uploads/media/a3/82/a382168e8309eae633a696a7dbc3dcd1/3620a70220b89789d531e5a846f59231/image.png)

If you see a sudden drop in indexed pages, it could be a sign that something is wrong and needs to be addressed.

![drop in the number of indexed pages](https://static.semrush.com/blog/uploads/media/11/30/11308e0243c526d5b713645fd0f099c0/eeaac474b58463a5c7ac2930d0fe7516/image.png)

Scroll down to review the reasons why some pages weren’t indexed. For example, pages returning 404 (Not Found) errors.

Click any entry in the “Reason” column to see a list of affected URLs and a description of the issue.

![Reason column](https://static.semrush.com/blog/uploads/media/c7/79/c779039c7703f9cc414989c14b2f63ab/9238f6f9dafb6d53e8b8f428ef979e4b/image.png)

At the very top of the page listing URLs affected by a given issue, you’ll see the option to get guidance on how to fix the problem.

![learn more on how to fix the issue](https://static.semrush.com/blog/uploads/media/66/8b/668b661ab44d4348d78a7308cb53c1ad/b1a51a4ef11161b34241525b2cea5680/image.png)

After you’ve addressed any issues you discovered in the Page indexing report, click “**Validate****Fix**” to notify Google of the change. And hopefully get the affected pages indexed.

### Sitemaps Report

The Sitemaps report shows whether Google can read your submitted sitemaps and how many pages it discovers from them.

Access the Sitemaps report by selecting “**Sitemaps**” from the left-hand sidebar.

![navigate to Sitemaps](https://static.semrush.com/blog/uploads/media/81/8d/818d9528703021b63e34331c55d148f5/fb31b508fd1192b87e62f60a93f24bb3/image.png)

For each submitted sitemap, the report includes:

- **URL**: The sitemap URL you submitted
- **Type**: [Sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap#sitemapformat) format (e.g., sitemap, sitemap index, etc.)
- **Submitted**: When the sitemap was added
- **Last****read**: The most recent crawl date
- **Status**: Whether Google processed the sitemap successfully
- **Discovered pages**: The number of URLs Google found in the sitemap
- **Discovered videos**: The number of videos Google found in the sitemap

![Google Search Console Submitted sitemaps report showing a successful sitemap index.](https://static.semrush.com/blog/uploads/media/20/b8/20b814de751677dc22790f5aa7c0d011/605b761a187bfdac342e28b7614d78e2/image.png)

Note the “Status” column. “Success” means Google was able to process your sitemap without issues.

Here’s an overview of what unsuccessful statuses in the Sitemaps report mean, plus how you should approach them:

- **Has errors**: Google detected issues in your sitemap. Review the listed errors and follow [Google’s guidance](https://support.google.com/webmasters/answer/7451001#error_list&zippy=%2Cerror-list) to correct them.
- **Couldn’t fetch**:Google was unable to access the sitemap. Use the URL Inspection tool to run a live test to investigate issues.

Click a sitemap entry to open a detailed report. From there, select “**See page indexing**” to see whether all the pages in your sitemap are indexed.

![see page indexing](https://static.semrush.com/blog/uploads/media/1e/a8/1ea8648a4a5f8c6ef72228b3ced22a84/8a3611597c1d625398e6888fb5636f15/image.png)

### Core Web Vitals Report

The [Core Web Vitals](https://www.semrush.com/blog/core-web-vitals/) report shows whether your pages meet Google’s performance and usability standards.

Google evaluates pages using three Core Web Vitals (CWV) metrics:

1. **Largest Contentful Paint (LCP)**: How quickly the main content loads
2. **Interaction to Next Paint (INP)**: How responsive the page is to user interactions
3. **Cumulative Layout Shift (CLS)**: How stable the page layout is as it loads

The Core Web Vitals report groups pages by “Good,” “Needs improvement,” and “Poor.”

Clicking on an issue shows the affected URLs. After fixing the issue, use “**Validate Fix**” to ask Google to re-evaluate the affected pages.

![Core Web Vitals LCP issue report showing affected mobile URLs and validation status.](https://static.semrush.com/blog/uploads/media/47/ff/47fff3bc9dc3d069f93d63743d0fb0d9/1aca796ce98677607d312c44a86bb535/image.png)

Because Core Web Vitals data is based on real user interactions, changes may take time to appear in the report.

### Enhancements Section

The Enhancements section includes reports related to your website’s structured data—markup that provides more information about your pages and makes you eligible to show for [rich results](https://www.semrush.com/blog/rich-snippets/) that may entice more clicks from searchers.

Google lists the structured data types it detects—such as Breadcrumbs—under the “**Enhancements**” section in the sidebar.

![Enhancements section](https://static.semrush.com/blog/uploads/media/1f/31/1f3119a25832d3f4d2a5f0c7bc5384ce/95217f9a81ca60aae340c470311b2104/image.png)

Click a specific structured data type to open a detailed report about any invalid items that need to be fixed.

![Breadcrumbs](https://static.semrush.com/blog/uploads/media/9c/fb/9cfbb1d95f82f534758506a892c996e0/40c62801b6fe463711c61ab70930eccd/image.png)

To resolve issues with your structured data, follow [Google’s guidance](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) for the specific markup type.

### Manual Actions Report

The Manual actions report shows whether your site has received any penalties for violating [Google’s spam policies](https://developers.google.com/search/docs/essentials/spam-policies).

Websites with manual actions (penalties) may rank much lower in Google search results—or may not rank at all. And that means less traffic and visibility.

Check for penalties by opening the “**Manual actions**” report in Search Console and note what you see:

- “No issues detected” means no action is required
- “Issues detected” means you’ve received at least one manual action to address

![Manual actions report](https://static.semrush.com/blog/uploads/media/69/11/6911020d216681f3fe7171513c9d3955/c5b42dddf9183662d73f24560b9a3614/image.png)

For detailed advice on recovering from Google penalties, review [Google’s manual action documentation](https://support.google.com/webmasters/answer/9044175?hl=en#).

### Links Report

The Links report shows details about your external links (also called backlinks) and internal links.

Backlinks are links from other websites to your site that help Google recognize your site is authoritative and deserves good search visibility.

Reviewing this [GSC’s Links report](https://www.semrush.com/blog/google-search-console-links/) helps you understand where backlinks are coming from and which pages attract them.To access the report, select “**Links**” from the sidebar.

![Links on the sidebar.](https://static.semrush.com/blog/uploads/media/83/cf/83cf2ebbc229317efdae11c2b42476d1/791669e83e543cd68028390a3fe8c388/image.png)

You’ll see your site’s total number of backlinks (“External links”) at the top.

![total number of backlinks](https://static.semrush.com/blog/uploads/media/4e/ef/4eef6b14bb23c574e32ebf80ffe7486f/96b08591f6bfd0a96b8e1cde236dd0bd/image.png)

The report also includes these sections under “External links”:

- **Top linked pages**: Pages on your site that receive the most external links
- **Top linking sites**: Domains that link to your site most often
- **Top linking text**: Common [anchor text](https://www.semrush.com/blog/anchor-text/) used in external links

![Google Search Console Links report showing top linking pages, sites, and text.](https://static.semrush.com/blog/uploads/media/8a/ce/8ace641f9585cf745c0064ec42e5bc75/094f389976773830835af9896853bd86/image.png)

The Links report also includes information about [internal links](https://www.semrush.com/blog/internal-links/)—links from pages on your own domain.

Internal links are important for SEO because they:

1. Help users and crawlers navigate your site more efficiently
2. Distribute authority across pages, which can support visibility in search results

You’ll find internal link totals and your most-linked pages within the same report.

![internal links and top linked pages](https://static.semrush.com/blog/uploads/media/79/f0/79f0286d5e930a78f02a863a25a434bd/cc5afe92f82e999f305c92a3903d361a/image.png)

### Shopping Section

The Shopping section in GSC appears for online stores and product review sites that use [product structured data](https://developers.google.com/search/docs/appearance/structured-data/product) and shows whether there are issues with product-related markup.

Depending on the structured data on your site, you might see these Shopping reports:

- **Product snippets**: Shows issues affecting product rich results in search
- **Merchant listings**: Shows issues impacting free product listings across Google
- **Shopping tab listings**: Shows issues preventing products from appearing in the Shopping tab

![Navigate to the specific report from the sidebar](https://static.semrush.com/blog/uploads/media/0a/e3/0ae3926a1507b2f7c26804f85918ba86/1a5f533f3db3042a3618aa5619f3175c/image.png)

Each Shopping report highlights any invalid items that prevent the pages from showing as rich results on Google.

![Invalid and valid items](https://static.semrush.com/blog/uploads/media/59/72/5972bd44a264d02d4d9dc7594d9fc3b7/82a04708653694b0fd8dbb3d52f5690d/image.png)

After fixing any markup errors, use [Google’s Rich Results Test](https://search.google.com/test/rich-results) to confirm whether the markup was implemented correctly.

## Connect Your Google Search Console Account to Semrush

Connecting your Google Search Console account to Semrush lets you access comprehensive search performance information in one place.

For example, [Position Tracking](https://www.semrush.com/position-tracking) allows you to import keywords directly from GSC. This lets you track rankings for search terms your site already appears for. You can easily spot trends and do competitor comparisons.

![Semrush Position Tracking overview showing keyword visibility trend for a domain.](https://static.semrush.com/blog/uploads/media/94/e1/94e1b39b286eeeb8961751e9ab59f828/5f4b2b3c760b02e09b3d47b0fbe53bd3/image.png)

Search Console data can also support tools like Semrush’s [On Page SEO Checker](https://www.semrush.com/on-page-seo-checker/), which turns performance insights into optimization ideas related to content relevance, internal links, and other on-page elements.

![Semrush On Page SEO Checker Optimization Ideas table showing pages, target keywords, and idea counts.](https://static.semrush.com/blog/uploads/media/c2/98/c2989eafeceaa78e5b395bd4db55d0b7/ed6f8708be68631ae858c0a08ed13c80/image.png)

Check out our full list of [Semrush tools that integrate with GSC](https://www.semrush.com/kb/857-google-analytics-and-search-console) for more ideas. Test all of these tools and more with a Semrush One trial.
