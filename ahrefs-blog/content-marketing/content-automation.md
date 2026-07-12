---
title: "7 Content Automations Used by Real Content Pros"
source: ahrefs-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "content-automation"
url: "https://ahrefs.com/blog/content-automation/"
canonical: "https://ahrefs.com/blog/content-automation/"
author: "Mateusz Makosiewicz"
published: "2024-06-27T13:52:57+00:00"
updated: "2024-06-27T13:53:05+00:00"
categories:
  - "Content Marketing"
freshness_reasons:
  - "date_2024_watch"
fetched_at: "2026-06-12T11:22:40+00:00"
status_code: 200
html_hash: "b6b781aeb605df0f234b3bc0792ce6b78e63cdf5b9a84072100d3ed84dfad31d"
clean_word_count: 2684
clean_char_count: 16361
---
# 7 Content Automations Used by Real Content Pros

Content marketing can become complicated and effortful very quickly.

Content teams need to manage ideation, writing, editing, proofing, publishing, promotion, analytics, and reporting across a team of writers, reviewers, and dozens of articles each month. Smart content leads find ways to automate some of these processes to let them focus on what really matters.

So, to inspire you and show you not only what’s possible but also the kind of things that are really worth automating, we asked three experts to share their favorite workflows.

- [Eric Doty](https://www.linkedin.com/in/edoty/), Content Lead at [Dock](https://www.dock.us/).
- [Tommy Walker,](https://www.linkedin.com/in/tommyismyname/) founder of [The Content Studio](https://www.thecontentstudio.com/) and host of [The Cutting Room](https://www.thecontentstudio.com/the-cutting-room/).
- [Caitlin Burns](https://www.linkedin.com/in/caitlin-burns-75a879a7/), Content and SEO Lead at [Dovetail](https://dovetail.com/).

## 1. Use Airtable to manage the entire content production workflow

You can’t automate everything, but you can automate your entire content production workflow.

My interviewees use Airtable as a “central base of operations,” as Tommy Walker puts it. A base like that controls everything:

- Topic ideas with keywords and their [SEO data](https://ahrefs.com/blog/seo-data/).
- Briefs.
- Outlines.
- Articles.
- Tasks with their statuses and different ways to view them (calendar, kanban, etc.)
- Contributors and their roles.
- Notifications.

![Sample base in Airtable.](https://ahrefs.com/blog/wp-content/uploads/2024/06/sample-base-in-airtable-.jpg)

Airtable, base view.

The general idea behind this is the use of triggers and actions. A complete set of a trigger and at least one action is often referred to as a Zap (coined by one of the automation tool providers Zapier).

All of our experts have this kind of central base, and I guess it’s hard to resist having one once you start automating things. So here’s one of those systems by Eric Doty:

Eric mentioned using Ahrefs as his source of keywords. If you’re going to do the same, here’s a quick tip for you — use automated [keyword clustering](https://ahrefs.com/blog/keyword-clustering/) right inside Ahrefs, so you won’t need to figure it out later on.

Tip

Keyword clustering allows you to group keywords with the same intent — and you’ll come across these a lot (e.g., “car insurance” and “auto insurance)”.

All you need to do is click the **Cluster by Parent Topic** tab in the **Matching terms** report in [Ahrefs’ Keywords Explorer](https://ahrefs.com/keywords-explorer). You can also export the list and use it in Airtable, Notion, or similar.

Returning to our central content base, it’s important to note that not everyone will need to visit it regularly. As Tommy pointed out, a content automation system can integrate with processes your teammates follow (and possibly even other automation).

For example, some stakeholders need real-time notifications about status changes, while others only require a weekly digest of content output. Automation handles this excellently.

You can also have people fill out forms that will feed into system. For instance, sales team could use a form like that to request new content without needing to enter your Airtable setup.

## 2. Assign articles to writers, editors, and SMEs

Caitlin showed me how she automates assigning tasks to three types of contributors based on the work progress: writers, subject matter expert reviewers, and editors. All this is to maintain the output of 20 - 30 published articles per month, without leaving Airtable.

Caitlin was very generous, so you’re about to see not only what this workflow does but also copy the [conditional logic](https://blog.airtable.com/conditional-logic-for-automations/) for Airtable and ready-made Zaps!

The whole process starts when Caitlin assigns the status of an article to “Writing”.

This triggers an Airtable automation that adds the brief to the writer’s Google Sheet. A Zap is then triggered by the new row in Google Sheets, which adds the assignment date and sends an email to the writer, notifying them of their new assignment.

Here’s what the setup of this part looks like in Airtable:

When the writer finishes their part, Caitlin gets an automated notification in Slack.

Next, the article goes to the expert for a review. This is crucial for Caitlin’s strategy because it enhances the content with unique expertise and real-life experience.

Thanks to automation, all Caitlin needs to do is change the status to “Reviewing”. This adds the article link, brief, and word count to the reviewer’s Google Sheet.

On top of that, this automation sends an email to the reviewer notifying them of the assignment. And here’s the cool part: the email will differ depending on whether article is a completely new one or a second review. Here’s how you can set this up in Zapier.

When the reviewer is finished, they check “Done” and select a field in a “Next steps” dropdown in their sheet to reflect whether the article is approved or needs changes made by the writer. Then Caitlin gets a message like this in Slack:

If the writer needs to make changes, there’s a special status for that, too. When Caitlin changes the status from “Reviewing” to “Writer is updating”, this automatically changes the status in the writer’s Google Sheet. And to make sure the writer won’t miss that status change, there’s an automated email notification, too.

Finally, we have the editing stage. Now Caitlin changes the status to “Editing,” which adds a row in the editor’s Google Sheet, just like it did for the writer and the expert.

When an article is done, the editor changes the status in their sheet, and adds any comments if they want to, Caitlin receives this message:

You can copy the exact Zaps Caitlin used here:

- [Send new article to writer](https://zapier.com/shared/63ac628fc62f6ba9d017d463b210411d5b9deb42)
- [A writer has submitted an article](https://zapier.com/shared/ea2e265fecf56e8134225e00104d9625da02a78a)
- [Send an article back to the writer for changes](https://zapier.com/shared/547958115112fa68909a3b79856eb45c0b67055d)
- [Assign articles out from Airtable to an editor](https://zapier.com/shared/editor-new-article-added/f849d2e8c0baf5bc7da0796ae29a0ca956d6d2f7)
- [Send a Slack update when the editor checks an article as edited](https://zapier.com/shared/edited-article-alert/ea1649677c4802b20fba18c0429f117caa60e9b7)

## 3. Share content internally and make it accessible

The more you publish, the more people in your organization, the more you’re going to need this type of automation.

First, Eric will show you how to set up Airtable so that whenever a new blog post is published, it triggers an email to the writer, a message on Slack, and a status change in Airtable.

Now, let’s say you’ve a big content inventory and want to help other teams access it for use in prospect calls or newsletters. You can use another of Caitlin’s workflows, which [adds an AI-generated summary of all published articles](https://zapier.com/shared/a33a471c584956a59149561b5b7b9b99702bc643) to Airtable through a Zap.

Further reading

- [Automated SEO Reporting (The Easy Way)](https://ahrefs.com/blog/automated-seo-reporting/)

## 4. Quickly save your best content ideas

If you’re like Eric (and me), you get content ideas in various, often random, situations, and it’s not always quick or easy to pull up your content dashboard to jot them down. Luckily, you can set up a Zap to handle that, too.

In this example, Eric explains how he created a nifty workflow to send content ideas noted in a Slack channel straight to Airtable.

1. Eric notes down a keyword idea in a Slack channel with a predefined hashtag.
2. A Slack bot confirms adding the keyword to Airtable, appended with a link to the Airtable base.
3. Now that the keyword is in the keyword list, Eric can add SEO data when he’s ready.

## 5. Automatically create content briefs

If you’re creating briefs for other people or outlines for yourself using the same document format, time and again, I’m sure you’ll appreciate this workflow.

1. **The trigger has two conditions**: the topic must reach the “brief needed” status and a brief must not have already been created.
2. **The action**: a Google doc is created which acts as the template for the content brief. The document already includes some information from Airtable passed down through variables such as the keyword, topic, and format.

Tip

Help make your content more relevant in Google’s eyes by including important subtopics. You can find those by identifying the keywords the top articles rank for.

Go to [Ahrefs’ Keywords Explorer](https://ahrefs.com/keywords-explorer), enter your target keyword, and scroll down to the **SERP overview**. Select a few top-ranking articles, and click **Open in Content gap**.

You’ll see a list of keywords that your selected articles rank for. Keywords with more articles rankings in the top three will likely be the most important subtopics.

If you’re optimizing an existing article, you can add topics worth expanding on using the AI **Content Grader** in Ahrefs.

Further reading

- [How to Create Content Briefs (with 6 Templates)](https://ahrefs.com/blog/content-briefs/)

## 6. Manage guests for a podcast show

Here’s inspiration from Tommy Walker, sharing how you can automate podcast production by connecting a few different tools to Airtable.

Here are the steps:

1. Tommy sends out an invitation to book a time slot for an episode via Calendly.
2. When the guest books a time, this creates a new record in Airtable with status “Booked” and their details filled.
3. This also triggers Google Drive to create a new folder and two subfolders within in (one of them is for the guest to upload their headshot).
4. Uploading a headshot into the folder notifies the designer.
5. Next, an Email goes out to book a precall with the guest.
6. Now, Tommy can click the “Create page” button right inside Airtable which creates a page and a blog post in WordPress (how cool is that!).
7. Once the broadcast is complete on YouTube, it goes into the RSS feed in Castmagic. This allows Tommy to use the tool to create a transcript and use an AI chatbot on it.

The tick sign is the button to create a page in WordPress.

## 7. Send an email when a contributor drops a new file in Google Drive

You know how there’s no notification when someone uploads a new file to Google Drive for you? You still need to manually notify that person about the file which feels *very manual*; it feels like doing the same thing twice.

Until Google fixes that, Eric will show you how to make a Zap to save you time and peace of mind. Use this when working with designers, writers, and your video team.

1. **Trigger**: a contributor drops a file in a designated folder in Google Drive.
2. **Action**: an email goes out to the Eric with the name of the contributor and the link to the file.

## FAQs

I’ve answered a handful of common questions for those just starting out with content automation.

### What’s the difference between content automation and automated (AI) content?

It’s easy to confuse these two terms because they’re quite similar, and one is a subset of the other:

- Automated content is generated mainly by AI without human input.
- Content automation uses tools to streamline content creation, management, and distribution.

Thus, you can have content automation without automated content. Moreover, it’s advisable not to fully automate your content if you want to rank well on Google.

### Is automating content good for SEO?

TLDR; if you want to fully automate content, as in not even look at it before publishing, it will most likely be bad for SEO, even though [Google is not against AI content per se](https://developers.google.com/search/blog/2023/02/google-search-and-ai-content).

Various SEO experiments and case studies have proven one thing beyond doubt: gaming the system can bring only short-term gains. Google catches up to bad content and [spam](https://developers.google.com/search/docs/essentials/spam-policies#scaled-content) sooner or later, whether that’s automated content or not. And when this happens, your traffic charts will look like this:

You could disclose making content with AI, as Google suggests. But paradoxically, trying to adhere to the guidelines can compromise the user experience (especially for [YMYL topics](https://ahrefs.com/pl/seo/glossary/ymyl-pages)). Although consumers don’t seem to be against AI content in general ([study](https://prod.ucwe.capgemini.com/wp-content/uploads/2023/05/Final-Web-Version-Report-Creative-Gen-AI.pdf)), they are likely to be cautious about it ([study](https://kpmg.com/xx/en/home/insights/2023/09/trust-in-artificial-intelligence.html#:~:text=Trust%20and%20acceptance%20depend%20on%20the%20AI%20application.,in%20healthcare%20is%20the%20most%20trusted%20and%20accepted.)).

> It’s funny how everyone wants to use AI to write content but at the same time no one wants to read content written by AI.
>
> — Andrea Bosoni (@theandreboso) [January 18, 2023](https://twitter.com/theandreboso/status/1615688300160847873?ref_src=twsrc%5Etfw)

Finally, the content automation experts I talked with don’t use AI for content generation. Given their experience, I wasn’t expecting a different answer. They might use AI for other things like generating outlines, finding content gaps (check out our [AI Content Grader](https://ahrefs.com/blog/whats-new-at-ahrefs-mar-2024/#general)), or looking for relevant subtopics, but not for actual writing.

### Is content automation for all team sizes?

Our experts agree: big, or small, every team can benefit from content automation.

> It’s honestly for everyone. I use it for every level of content creation — from 10 articles/month to 100. At HealthMatch, we published between 150-200 articles per month, so I very quickly had to figure out how to use automation to make that scale possible. Sending an email to one or two writers a week with new assignments is doable. Sending emails to 20 writers is not.
>
>
>
> Caitlin Burns, Content and SEO Lead, [Dovetail](https://dovetail.com/)

Additionally, Tommy Walker has a unique take on this:

> The value proposition for big companies is going to be different based on the size. For bigger companies, it’s more about automating information exchange so that it happens effectively and efficiently. For small companies, it’s more about time savings.
>
>
>
> Tommy Walker, Founder, [The Content Studio](https://www.thecontentstudio.com/)

If you want to use AI for SEO effectively yet safely, we’ve got [fourteen tried and tested ideas](https://ahrefs.com/blog/ai-seo/) for you.

### What are the common pitfalls of content automation?

According to our experts, you should watch out for two things.

The first pitfall is creating infinite loops. This is when a task runs over and over again until you max out your automation tool’s plan. If you’re using Zapier, [here’s how to avoid it](https://help.zapier.com/hc/en-us/articles/8496232045453-Zap-is-stuck-in-a-loop#h_01HQ8MXQ2DB2GB6RY77ZRT3CK2).

Another pitfall is automating everything just because it’s possible.

Follow Eric’s advice: automate tasks you’ve handled manually a few times. Avoid automating new processes immediately; first, do them manually to see if they’re worth automating. Otherwise, you might waste time on ineffective workflows or overwhelm yourself with too many automated tasks.

## Final thoughts

I’d like to wrap this up with the number one content automation tip for beginners from each of our experts. They all seem to agree: smart small.

> If you attack automation with a particular problem that you want to solve rather than trying to become a content automation expert, then you’ll learn by trial and error, you’ll learn much quicker, and you’ll solve problems for yourself rather than learning the abstract. So start small, and start with a manual process that you do all the time but would love to stop doing.
>
>
>
> Eric Doty, Content Lead, [Dock](https://www.dock.us/)

Got questions or comments? Let me know on [X](https://x.com/m_makosiewicz) or [LinkedIn](https://www.linkedin.com/in/mateusz-makosiewicz-38154b67/).
