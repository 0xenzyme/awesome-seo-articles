---
title: "How to Start a Link Building Campaign Fast (and Systematize Everything)"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "fast-link-building"
url: "https://ahrefs.com/blog/fast-link-building/"
canonical: "https://ahrefs.com/blog/fast-link-building/"
author: "Joshua Hardwick"
published: "2020-04-16T13:26:24+00:00"
updated: "2025-12-18T13:56:23+00:00"
categories:
  - "Link Building"
freshness_reasons: []
fetched_at: "2026-06-12T11:30:23+00:00"
status_code: 200
html_hash: "64df5781f75e2b3c2c4d772c71c90f819a67323ddcb6988370d1a57a59ae5b3e"
clean_word_count: 2780
clean_char_count: 15573
---
# How to Start a Link Building Campaign Fast (and Systematize Everything)

Do you know the basics of [link building](https://ahrefs.com/seo/link-building), but struggle to get a campaign off the ground? This advanced guide will show you how to do that—fast.

Link building outreach can be broken down into three tasks:

1. Finding prospects
2. Finding contact information
3. Sending emails

Most of the information you read online is focused on that last part: sending emails. But if you’ve ever done [blogger outreach](https://ahrefs.com/blog/blogger-outreach/) before, you’ll know that the real bottlenecks occur when finding prospects and contact information.

Get those right, and sending emails is easy.

In this actionable tutorial, we’ll focus on how to make the first two parts of the process more efficient. And we’ll also talk about how to systematize, automate, and scale your outreach.

Let’s dive straight in.

New to link building? Check out our

[Beginner’s guide to link building](https://ahrefs.com/blog/link-building/)

## The process

Before we do anything, we first need to choose a type of campaign to run.

To keep things simple, let’s opt for a [guest posting](https://ahrefs.com/blog/guest-blogging/) campaign.

Before I lose you, let me just say that I know guest posting is far from exciting. It’s boring, and it’s old news. The reason I’m using it to demonstrate this process is because it’s a straightforward example. I’ll explain how you can apply it to other [link building strategies](https://ahrefs.com/blog/link-building-strategies/) later.

Ready? Let’s go.

### Step 1. Finding prospects

The first piece of the puzzle is to abandon the usual approach of using Google to find prospects.

Don’t get me wrong, Google is excellent for finding prospects for all types of campaigns, but it’s a massive bottleneck when speed is the aim. You have to extract results, bulk-check SEO metrics with a third-party tool, and, well, it just takes too long.

So instead, we’ll use [Ahrefs’ Content Explorer](https://ahrefs.com/content-explorer).

Content Explorer is a searchable, filterable database of around a billion web pages.

Now, what we’re **not** going to do here is use search operators to find “write for us pages”—even though it’s possible with Content Explorer.

Instead, we’re going to use it to find sites that are writing about relevant topics.

There are three reasons for this:

1. Most people are open to guest posts—even if they don’t have a “write for us” page.
2. If websites have already published content about relevant topics, then we know they’re suitable prospects.
3. It gives us two key pieces of data (post URL and author) to make finding contact information easier.

To get started, we’ll go to Content Explorer and run an “In title” search like this to find blog posts about relevant topics:

`(How OR why) AND ([keyword 1] OR [keyword 2])`

For example, if we have a site that sells health supplements, we can search for something like this:

Just to explain how this search works:

- The brackets group words together.
- The OR operator says to return results containing either of the words in the brackets (e.g., how or why).
- The AND operator says to return results with at least one of the words from the first group (how or why) and from the second group (muscle or gym).

Put this all together, and what we’re effectively searching for are pages with the words “how” or “why,” and “muscle” or “gym” in their [title tags](https://ahrefs.com/blog/title-tag-seo/).

Most of these will be blog posts related to building muscle or going to the gym.

For example, here are just a few of the results from our search:

From here, we need to filter the results for only pages that are:

- **English.** Content Explorer stores pages in many languages, but we only want English pages because we’re doing outreach in English. People who’ve written content in another language might not be able to read our outreach email.
- **Live.** Content Explorer stores live and dead pages. It doesn’t make sense for us to reach out to the authors of dead pages because they’ll question how we found that page, and why they’re receiving an email from us.
- **On DR 20-95 websites.** [Domain Rating (DR)](https://ahrefs.com/blog/domain-rating/) is an Ahrefs SEO metric that measures a site’s “link authority.” It probably isn’t worth spending a lot of time and effort writing guest posts for most low DR websites. And domains with super high DR scores are almost always websites like Facebook, Google, etc. We want to filter both of these out to avoid wasting time.

Here’s how to apply these filters in Content Explorer:

We also need to filter out multiple pages from the same domain as we only want to contact each website once.

To do that, we can use the “one page per domain” checkbox.

2,685 prospects. Not bad for two minutes of work.

All that’s left to do is export the results to CSV, and import everything into a Google Sheet. Don’t use Excel for this. The reason why will become clear in the next step.

Sidenote.

 You can export up to 2,000 results from Content Explorer when using the “One page per domain” toggle. If there are more than 2,000 results for your search, adjust the DR filter, and export the results in batches. For example, if you have 3,500 results when filtering for pages on DR 20-95 sites, you could instead filter for pages from DR 20-50 sites, export the results, then repeat the process for pages from DR 51-95 sites. All you then need to do then is merge them in Google Sheets.

### Step 2. Finding contact information

Before we can reach out to any of these sites, we need to find some contact information—namely, the first name, last name, and email address of an appropriate person.

This is usually a huge bottleneck for two reasons:

1. **It’s a manual process.** You have to visit the sites, find the name of the person to contact, and [hunt down their email address](https://ahrefs.com/blog/find-email-address/).
2. **It’s easier to find some sites’ contact information than others.** Sometimes you can easily spend 15+ minutes looking for just one email address.

So here’s the solution:

Instead of finding emails manually, we’re going to let [Hunter](https://hunter.io/)—an email lookup tool—do the hard work for us. We just need to feed it a first name, last name, and domain name.

For example, if we put my full name and “ahrefs.com” into Hunter, it finds my email address:

But how do we get names and domains of our prospects?

Well, if we look at the export from Content Explorer, we see that there are already author names for some prospects.

Sidenote.

 I replaced all the names in the export with fake names for privacy reasons.

If we feed these to Hunter, along with the “Content URL,” it’ll pull out the domain and try to find that person’s email address. If it finds it, we know that they’re somehow associated with the site. If it doesn’t, we can just assume that they’re a guest blogger and ignore them for now.

So here’s the process:

First, we’ll filter out the pages without author names.

Second, we’ll get rid of all the columns except for Content Title, Content URL, and Author.

Third, we’ll add two more columns (D and E):

In cell D1, we’ll enter this formula:

`=IFERROR(ARRAYFORMULA(IF(C1:C="Author","First name",IFERROR(IF(search(" ",C1:C),LEFT(C1:C,FIND(" ",C1:C)-1),C1:C),C1:C))),"")`

In cell E1, we’ll enter this formula:

`=IFERROR(ARRAYFORMULA(IF(C1:C="Author","Last name",IF(LEN(D1:D) < 1,"",IFERROR(IF(search(" ",C1:C),TRIM(RIGHT(SUBSTITUTE(C1:C," ",REPT(" ",100)),100)),""),"unknown")))),"")`

This splits the first and last names.

This is important because we’re not going to use Hunter’s web tool to find email addresses; we’re going to use [their Google Sheets add-on](https://hunter.io/sheets) to check them in bulk.

If you’re following along, then you need to sign up and get an API key for this, which gives you 50 free searches a month. Once you’re ready to go, load it up in Sheets and use the email finder option.

Tell it where to find the first name, last name, and URL. Leave the company name blank.

Hit find email addresses, and it’ll start working its magic.

Note that this won’t find email addresses for everyone. The name has to be from someone associated with the website (meaning they have a personal @domain email), and it has to be in Hunter’s database.

The final step is to verify the emails Hunter finds using a tool like [Neverbounce](https://neverbounce.com/).

To do this, we’ll go to Neverbounce’s bulk tool, upload the list, then clean the list.

Sidenote.

 You will get 1,000 free credits when you sign up for Neverbounce. If you need more after that, it’s quite cheap—between $3-$8 per 1,000 emails.

Finally, we’ll export the valid emails and use [a VLOOKUP formula](https://ahrefs.com/blog/google-sheets-formulas-seo/) to bring them into our sheet.

Now we have a bunch of prospects pretty much ready to pitch.

Let’s export these to CSV, and we’re ready for the final part of the process.

### Step 3. Sending emails

Good news: Most of the hard work is done. All that’s left is to upload the prospects to an outreach tool like Mailshake, Buzzstream, or Pitchbox.

It’s then just a case of writing an outreach template using merge fields.

Sidenote.

Please write a better outreach email than the example above. I kept that intentionally simple for demonstration purposes. It’s not a good pitch.

Now, at this stage, you could start blasting out emails left, right, and center with no personalization—but we really wouldn’t recommend that. Personalizing your emails is pretty much the only differentiating factor between a spammy and a non-spammy approach here. Just because we’re automating things doesn’t mean that [the rules of good outreach](https://ahrefs.com/blog/outreach/) no longer apply.

Here’s the way I see it: we’re automating the boring stuff so we can spend more time on the things that matter, like personalizing emails and double-checking that our prospects are sound.

Does this slow things down? Of course, but even if it takes five minutes to personalize each email, that’s still 12 emails an hour.

If we assume a low 8% conversion rate, that’s still one link per hour of work.

But, if that still sounds like a lot of work for one link, the next section might interest you.

## How to systematize, automate, and scale this process

Finding someone to send outreach emails for you is simple enough: just post a [job listing](https://ahrefs.com/blog/seo-job-description/) on a freelancing website like Upwork.

But why stop there? It’s entirely possible to:

- **Systematize** and delegate almost every part of the process.
- **Automate** things to reduce moving parts.
- **Scale** and reach out to more prospects.

Here’s how to do each of these things:

### Systematizing

What we have above is a process for link building, but processes aren’t the same as systems. A process is a series of steps to achieve an end goal, whereas a system joins those steps together.

Basically, with systems, once you set the wheels in motion, everything takes care of itself.

Here’s a simple way to turn the process above into a system:

First, set up a Trello board with lists for each part of the process.

Second, create documentation for each step.

I find [Google Docs](https://www.google.co.uk/docs/about/) best for this because you can easily share them with other members of your team. So for the process above, you’d create three documents: one for prospecting, one for finding contact information, and one for sending emails.

Third, create a new list on the Trello board and add links to the documentation there.

Now, whenever you start a campaign, you just need to create a new card, tag the person responsible for carrying out the first task, and point them to the documentation.

However, you might be wondering what happens when the person completes this task? Don’t you have to keep an eye on things and keep assigning steps to the next person?

Nope. Just make assigning the next step part of your documentation.

### Automating

Having a system where all the cogs keep turning is fantastic, but wouldn’t it be even better if you could reduce the number of cogs that need turning?

This is where automation comes into play.

Watch [this video](https://www.youtube.com/watch?v=HyIXvIaUlLk) to learn how to automate the bulk of the process above with Zapier:

### Scaling

Reading through this guide, you might have noticed that although this process is fast, systematized, and can even be semi-automated, it leaves a lot of prospects on the table.

After all, Content Explorer only finds names for **some** pages, Hunter only finds email addresses for **some** prospects, and Neverbounce only verifies **some** emails.

If you start out with 1,000 prospects, then you might only have 100 ready to go at the end of this process.

As there are only a finite number of prospects for any campaign, it doesn’t make sense to leave 90% of them on the table.

But here’s the thing: I’m not telling you to.

The point of this process is to get a link building campaign off the ground as quickly as possible—not execute it to perfection.

Doing things this way lets you quickly get a sense of whether a campaign has legs or not.

**If it doesn’t have legs**, knock it on the head.

**If it does have legs**, then it’s time to scale.

You’ve already got a system in place, so scaling things is as easy as creating an additional piece of documentation for finding names and email addresses manually.

However, this isn’t the only way to scale. You can also:

1. Run more campaigns.
2. Apply these principles to more link building tactics.

Let’s talk more about option B.

## Using this process for other link building tactics

Everything we’ve talked about above can be applied to pretty much any link building tactic—as long as your prospecting process gives you first and last names.

But here’s the thing: most prospecting processes don’t give you this.

For example, let’s say that you find a [broken link building](https://ahrefs.com/blog/broken-link-building/) opportunity in Site Explorer.

If you export the backlinks report for this opportunity, you won’t see author names.

This isn’t a big issue. As long as your list of prospects is a list of web pages (not websites), you just need to add one additional step to the process: use [URL Profiler](https://urlprofiler.com/) to pull names.

How? Just paste the prospects into URL Profiler and check the “Readability” checkbox.

This will pull author names from the pages where possible.

Sidenote.

 URL Profiler isn’t free, but there’s a free 14-day trial.

Does it find as many as Content Explorer? In my experience, not quite—but it’s not a million miles off.

Merge this with your existing data using VLOOKUPS in Google Sheets.

Using Google to find prospects?

You can also pull Ahrefs’ SEO metrics like DR, UR, and organic traffic with URL Profiler.

Just check the appropriate boxes for the data points you want to pull.

From there, we pretty much run through the same process as before: find emails, verify them, do outreach.

## Final thoughts

Getting a link building campaign off the ground doesn’t have to take days—or even hours.

Using the process outlined in this guide, it should be possible to at least pitch a few guest posts within 30 minutes or so—even if you don’t have a lot of link building experience.

Got questions? Didn’t understand something? [Ping me on Twitter](https://twitter.com/joshuachardwick?lang=en).
