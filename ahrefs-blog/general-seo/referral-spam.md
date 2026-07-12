---
title: "How To Stop Referral Spam In Google Analytics"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "high"
slug: "referral-spam"
url: "https://ahrefs.com/blog/referral-spam/"
canonical: "https://ahrefs.com/blog/referral-spam/"
author: "Alex Dealy"
published: "2015-11-12T21:06:53+00:00"
updated: "2021-06-29T21:05:10+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "date_2021_very_old"
  - "time_sensitive_title"
fetched_at: "2026-06-12T11:58:58+00:00"
status_code: 200
html_hash: "1244f874c8accbaf3c62296bb1f7daa5f45bd0457429138900ee174fed70d2ac"
clean_word_count: 2203
clean_char_count: 12811
---
# An Actionable Guide To Stopping Referral Spam In Google Analytics

Is ghost referral spam screwing up your Google analytics data?

Fed up seeing spammy sites like darodar, semalt, floating-share-buttons.com and www.event-tracking.com in your list of referrers?

Well, you’re not alone.

Referral spam is the bain of most webmasters at the moment and has been getting steadily worse over the past year *(obviously making money for someone somewhere)*.

But fear not, Alex Dealy of loganix.net has the complete solution to your referral spam nightmare - ensuring none of those annoying spammers slip through the net and that your stats remain clean and accurate.

Over to Alex…

## What’s Ghost and Referral Spam Traffic and Why Does it Suck?

Spam has evolved. It’s not just an inbox & search engine problem anymore. It’s found its way into your Google Analytics account. Just like how spammers will bend to the lowest denominator to try to squeeze into your email inbox, they’ve picked up on flaws in the system to show up in data reports.

*Why*?

With the dimmest glimmer of hope that you’ll wonder what the hell they’re doing in your report and visit their website out of curiosity.

*Lame, right*?

Tell me about it! It makes data a mess—for both my personal sites and client’s sites that I work with at [The Magistrate](http://magistrateinc.com/).

*But, moar web traffic*?

The thing is, these bots never actually visit your site.

They manage to only just tickle the javascript that Google Analytics uses to notify you when a visitor normally views a page.

![ghost and referral spam](https://ahrefs.com/blog/wp-content/uploads/2015/11/image03.jpg)

They can still really skew your analytics numbers, including key stats like [bounce rate](https://ahrefs.com/blog/bounce-rate/) and other engagement metrics.

If you’re making big content marketing investments based on these numbers, it’s important that they’re as accurate as they can be.

This has made ghost and referral spam traffic a big problem for:

- Small businesses and solopreneurs
- Medium businesses with no dedicated marketer
- Marketing Agencies small and large

And the kicker? These agents of Voldemort work fast. Real fast.

Not only are the numbers of hits from spam increasing everyday, but so are the sources that have to be blacklisted and eliminated.

We’ve even seen referral spammers try such nonsensical techniques as trying to disguise themselves as Google. Why? Who knows?

Here is what we see on our side:

It’s particularly troubling if your site is relatively new and is not yet getting much legitimate web traffic. The spam percentages are much higher, and will skew your data much more than if your site has thousands of hits a day.

Here’s an example of a personal site of mine. I haven’t paid much attention to it, so it doesn’t get a lot of hits. But with a quick look at the orange segment, you can see that only 80% of the traffic recorded in Analytics is legitimate. 20% is spam traffic!

The bottom line is that you need clean data to make informed decisions about your website. And to do that, you need to address and clean up this mess.

Start now, because they are only going to improve their game.

## Ever Wonder How Easy It Is?

A single referrer record in analytics is a single “page load”

Under normal circumstances, that’s someone loading your page and all the other assets your page contains including images, css, javascript libraries & tracking. Ghost spammers avoid all the mess and just fire off a single javascript tracking code to google thereby forging a visit that never actually shows up.

That tracking “page load” took 0.001 seconds on a server somewhere. At the same time, that server was also loading 100 other “page loads” for different sites to muscle their way into everyone’s GA account.

When you consider how easy it is to buy another *(twenty)* $5 host, you’ll really grasp the how easy it is for this system to get way out of hand.

If the ROI is there, this problem gets far worse before it gets any better.

## Coming Up Short: Tactics that Don’t Take it All the Way

This issue first became known to the public a few years ago when a mysterious online service called Semalt *(hate these jerks)* started to use the technique to appear on Analytics reports.

And, as always, social media reacted.

If you don’t believe them, believe me. It was everywhere--It’s still rampant.

But with a big problem comes an innovative solution, or so we thought.

As it turns out, these spammers are so active, and their technique is so good, that many techniques pitched as being a “solution” did **not** work.

Hell, you’ve probably tried a few of them yourself.

In preparation for this article, I went through my considerable amount of browser bookmarks and my Pocket archive to find all of the guides I had used before prioritizing this in-house fix for our team.

Techniques that do not actually solve this problem include:

- Changing your .htcaccess file - This method will not work with advanced tactics.  Ghost spam never touches your site therefore renders this method useless.
- Using the referral exclusion/blocking list *([read more](http://www.clairwyant.com/google-analytics-domain-filtering-spam-bots-ghost-visitors-bad-data/))* - Good setup but no updates.
- Sourcing exclusion lists into exclusion filters - Only excludes and blocks future spam & does nothing about the referrers from yesteryear.

The only one that really came close was the exclusion filter. The real problem there was that it was very difficult to find current and consistently-updated lists. Many of the founders/creators of such lists just weren’t actually invested in keeping a solution updated.

The constant maintenance required to keep a list like that up is prohibitive to it being an **effective** solution to the problem, especially when there is no profit in doing so.

## The Missing Puzzle Piece

To be reasonable and effective, a solution to identify and weed out ghost and referral spam traffic would need to be:

- **Very** regularly updated
- Retroactive to past data
- Sourced from a large base of data

Using those principles as guidelines, we crafted the process that works so well for us now.

## Step 1: Using Segments to Filter and Block Spam

Just in case you need a refresher:

- Filters allow you to include or block data from your reporting data set. Keep in mind that filters are **destructive**. Anything you filter and block, accidentally or otherwise is gone forever. They also cannot edit past data.

- Segments, on the other hand, are a subset of users or sessions. You can turn segments on and off, as they are not destructive, and can be applied to past data.

First, I personally *(and professionally)* always prefer to play with segments instead of adding a new filter since segments do not permanently alter your data.

If you mess up while playing with a filter and accidentally filter out real referrers, then that data is never coming back.

Segments also allow to build upon previously used data, and you can apply them **retroactively** as well. No matter how long you’ve left that bad data idling around in your account, you can get it all now with a well-constructed segment.

## Step 2: Maintaining The Exclusion List

Thanks to the innovative team we’ve got here at the Magistrate, *(in particular, our Programmer Josh, who championed building this tool)*, we took advantage of a tool we use every day, anyways: Slack

The result? A custom integration into our Slack channel that posts every new campaign source from all of our client’s sites every hour. When it arrives, we give it a quick look and either whitelist it or add it the exclusion segment.

It works like this:

1. 1. **Referrals received**: For all properties we have control over in GA.
   2. **Results sorted by count**: We use PHP to sort, then loop and check if we recognize each. If not…
   3. **Suspected spam sent to slack channel for judgementafter clicking either *Blacklist* or *Whitelist* you’re taken to…**
   4. **Verdict verified**: A PHP page contains a confirmation for each classification
   5. **Spammers Stored**: verified spammers are locked up in our database until…
   6. **Data output in regex format**: We transfer the data and paste it to our analytics account.

We’re super proud of this, and it lets us update our list *at least* five times per day.

## Facing Reality: There is No One Solution

Despite our success—our analytics data is pretty damn clean—we’ve learned along the way that our method and tool should still be supplemented with other techniques, to cover your bases more than anything.

In the end, there is so much spam that we’re only just past the tip of the iceberg. Our data collection is relatively small and young.

Plus, thanks to some friends on inbound, we got some great pointers about solid techniques that also help suppress unwanted spam. The [comments and exchange](http://inbound.org/articles/view/referral-spam-solved-give-your-analytics-an-enema) that we had here are well worth a look at for additional context into solving Analytics Spam.

The rest of the steps are relatively easy.

1. Be sure to turn on the option within Google Analytics to exclude known bots and spiders.
2. Consider adding an [inclusive hostname filter](https://moz.com/blog/stop-ghost-spam-in-google-analytics-with-one-filter)
3. You could even [add a cookie to your site](http://www.lunametrics.com/blog/2015/03/19/eliminating-dumb-ghost-referral-traffic/) to cover your bases even more

Together, you’d get a very clean analytics profile.

Like, “your house while the in-laws are over” clean.

One contention we’ve gotten during our time creating and promoting our tool, is that many have had success with the inclusive hostname filter, listed above. Though the technique is currently proving **mostly effective**, we’ve found that it’s not the best long-term solution to keeping data clean:

- Analytics spam is increasingly spoofing hostnames. It’s not that difficult to do, and is an open window into your data
- Setup this option incorrectly, and you’re potentially filtering out real data *(see filters vs. segments)*

We’ve never quite seen hostname filters work 100% because of this vulnerability. We feel like our tool is finally the complete solution since it doesn’t discriminate by what means the spam referrer ended up in our GA account, it just stops it dead in its tracks.

**Editor’s note:** I asked Alex why the exclusion list was required in addition to the inclusive hostname filter *(which I have personally implemented on my sites)*. His answer was as above - while the inclusive hostname filter is pretty effective, there are sites that slip through the net *(and the spammers are getting smarter)*. When I checked my own analytics he was absolutely right as you can see below:

So as Alex says, a combination of both methods will be most effective in eliminating all ghost referrals and keeping your analytics clean.

At this point, an honest person would admit, setting up all of these solutions together is also a lot of work. I know about all the solutions, have documented them thoroughly and still don’t implement them all on sites I control.  A solution that never gets implemented is no solution at all.

And that is why we feel like this is finally a **complete** solution.

## Moving Forward

Again, it’s hard to stay 100% ahead of the curve.

But, if you need a robust and QUICK tool *(done in a minute, literally)* that is well-maintained, we’ve put an easy to use tool for you. It’ll only cost an email address, and we’re invested in keeping it updated.

Here is our [referral spam cleanup tool](https://loganix.net/rst-lander/), and let me quickly walk you through it.

After going through the double opt-in, you’ll arrive at the form below. Select any view to apply to all of your Analytics accounts and views.

Then, apply the segment in any of your reporting views. It’s useful to compare it with all sessions, depending on what you’re reporting on.

When that’s done, simply view the graph to get an idea of how much you were able to clean up your data. In this case, spam constituted over 20% of the data collected in Analytics. Blue is data as collected previously, and orange is the data once adjusted to remove spammy visits.

And hey, if you’re finding a bad guy that hasn’t quite reached us yet, you can suggest that the spammers be added to the segment’s blacklist.

Again, this is an ever-evolving problem for us. If it is for you too, we want your input.

This would have never been possible without our team, and we think it can be even better with you too.

If you have any tips and tricks we’ve missed, I hope you’ll let us know. In the meantime, [enjoy our tool](https://loganix.net/rst-lander) and cheers!
