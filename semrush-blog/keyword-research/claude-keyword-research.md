---
title: "How to do keyword research with Claude and Semrush"
source: "semrush-blog"
content_type: "blog_article"
freshness_risk: "low"
slug: "claude-keyword-research"
url: "https://www.semrush.com/blog/claude-keyword-research/"
canonical: "https://www.semrush.com/blog/claude-keyword-research/"
author: "Chris Hanna"
published: "2026-09-10T17:12:00+00:00"
updated: "2026-09-10T17:12:00+00:00"
categories:
  - "Keyword Research"
  - "SEO"
freshness_reasons: []
fetched_at: "2026-10-12T10:04:11.522445+00:00"
status_code: 200
html_hash: "a6c08cfd6998f34172a4926b0c8c39be1f63344d4c1197856414808b274a4ae1"
clean_word_count: 3784
clean_char_count: 24316
---
# How to do keyword research with Claude and Semrush

Keyword research is an important stage in creating content that meets your audience's needs and provides value for your own business. But basic keyword research often gives you the same list of keywords that everyone in your category is getting when they run their own process.

Performing keyword research with Claude and Semrush solves this issue by building your business context into the keyword research process itself. And by looking at what real customers are saying online and in your sales calls.

The keyword research workflow I'll show you below is repeatable, and you can use it any time you need to create new content or update existing pages. Here's how to do it:

## Part 1: Set up your Claude project

Set up a Claude project for your keyword research to keep it organized and provide project-specific context.

Projects let you add files and instructions Claude will reference for each chat in the project. This leads to better outputs and less back and forth with Claude, making the whole process more efficient.

### Create the project

To create a project in Claude, click the “**Projects**” option in the left-hand sidebar. Then click “**New project**.”

![Claude Projects page with the Projects menu highlighted and an arrow pointing to the New project button](https://static.semrush.com/blog/uploads/media/f7/9e/f79e7b428f19a1ab1299b1896d78a348/14af49808b9446d8f0528ea61f1752c2/image.png)

Give your project a name, like “Keyword Research Workflow,” and a description. Then click the “**Create project**” button.

![Claude project setup with the Keyword Research Workflow name, project goal, and Create project button highlighted](https://static.semrush.com/blog/uploads/media/40/62/40627e9d22c088f6b25dd4941e4cddfa/a874aa441ac21e659f5cb5a2daff7785/image.png)

### Add project instructions

Add project instructions to outline what you want Claude to do in your newly created project by clicking the “**+**” button next to “Instructions” within your project.

![Claude Keyword Research Workflow project with an arrow pointing to the button for adding project instructions](https://static.semrush.com/blog/uploads/media/86/0e/860ebdb0da063c76c575e5f017cc767c/6f28acbcfaf64567c0665239daa36290/image.png)

In the “Set project instructions” window, you’ll define the rough process Claude will follow, the data sources it should use, and your expected inputs and outputs.

Here’s an example set of instructions you can use for this process:

*For chats in this project, perform keyword research using the Semrush MCP, uploaded Google Search Console query CSVs, a list of existing page URLs uploaded by the user, and any uploaded competitor reviews, Reddit threads, or sales call transcripts, combined with the business context file added to this project.*

*Run the following processes when prompted:*

- *Keyword gap analysis (Semrush MCP)*
- *Easy win analysis from uploaded Google Search Console data (plus Semrush MCP if prompted by the user)*
- *Competitor review analysis*
- *Reddit thread analysis*
- *Sales call transcript analysis*

*For the competitor review, Reddit thread, and sales call analyses, generate keyword ideas first, then validate them in Semrush for volume and keyword difficulty. Output results as CSV files unless told otherwise.*

*When a user asks for a specific number of keywords to return using the Semrush MCP, return only that number. Do not fetch more than 10 rows if they only ask for 10 rows of data, as this can affect API unit usage. If you run into issues, or don’t see data where you expect to, flag it to the user instead of running your own diagnostic or exploratory queries.*

Once you’ve added your instructions, click “**Save instructions**.”

![Claude project instructions for keyword research with Semrush, GSC, reviews, Reddit, and sales calls, with Save instructions highlighted](https://static.semrush.com/blog/uploads/media/85/6a/856a01c1c26d3adde1c86f00fca23fe0/a21f9b06cddf24286f55c83993a3ff0e/image.png)

### Give Claude your business context

Give Claude your business context to improve the output quality and keywords that Claude identifies as relevant to your business.

To add business context, click the “**+**” button in the “Context” window and then click “**Add text content**.”

![Claude project Context menu with Add text content selected for adding business information to the keyword research workflow](https://static.semrush.com/blog/uploads/media/12/05/1205373f8eef28a1f6c5e8e4efa1701e/bcf6306fe87ee59200427bf66e2507e2/image.png)

Add a title like "Business Context" and then paste in content that answers the following five questions:

- What do you sell?
- Who buys it?
- What problems do you solve?
- Who are your competitors?
- Do you have any specific rules you want Claude to follow?

By adding this context, Claude can make decisions while identifying keywords.

For example, it can run related searches for product features that you specify, or it can add modifiers to its search terms based on your target market.

Adding business context now will also help in part 3 when we’ll ask Claude to analyze reviews, Reddit threads, and sales call transcripts to come up with its own keyword ideas.

Use our [business context template](https://docs.google.com/document/d/107uDHJKr5IoCDhIu79d_QaSCbMDG48kma6RO7JTZSrY/template/preview) to create a document that you can upload for this process:

![Business Context Template with sections for products or services, target buyers, and customer problems](https://static.semrush.com/blog/uploads/media/75/36/753633ea2652835892713a745ffb20e8/04844c77e14c355bbdfef033ca819f4a/image.png)

I also recommend uploading a list of your website's URLs for additional context to help Claude see what pages you already have on your site. While it's not perfect, since it relies on interpreting your URLs, it’s a fairly quick and easy way to give Claude context on pages you already have. This allows Claude to suggest pages you may want to optimize rather than creating new pages.

Do this by adding the list the same way you added the business context. Click the “**Add Content**” button when you’re finished:

![Claude Add text content window containing a list of existing website URLs, with the Add Content button highlighted](https://static.semrush.com/blog/uploads/media/f0/39/f03968d5f9c65390fb9d03a032f0d700/15a9fa400281a6a7df003773502805b0/image.png)

### Connect Semrush and Search Console

Connect Semrush via the MCP and upload Google Search Console (GSC) data to provide Claude with sources of truth for each keyword research process you’ll carry out.

To connect the Semrush MCP, click the “**+**” button in any chat, then go to “**Connectors**” > “**Add connector**” > “**Browse connectors**.”

![Claude Connectors menu showing the steps to add a connector and browse available connectors](https://static.semrush.com/blog/uploads/media/a1/b3/a1b3cbdb8dd0207e5d84cb3e1da26b38/da1c22eea1a0c79ca4fc2c31a4511812/image.png)

Then search for Semrush and click the “**+**” button next to “Semrush.”

![Claude connector directory search results for Semrush, with the button to add the Semrush connector highlighted](https://static.semrush.com/blog/uploads/media/50/48/5048ec2153444dade70da1b2c22cbb7c/2e7540985695f105e810deb1558b57ce/image.png)

There’s no official MCP available for Google Search Console, but there are still ways you can connect Google Search Console directly to Claude. We covered how to do this in our article about [turning Claude code into your own SEO analyst](https://www.semrush.com/blog/claude-code-seo/).

For this workflow though, all you need to do is upload a CSV file of exported Google Search Console query data. You can get this by navigating to  “**Performance**” > “**Search results**” within Google Search Console and clicking the “**Export**” button.

![Google Search Console Search results performance report for three months, with the Export button highlighted](https://static.semrush.com/blog/uploads/media/be/cf/becf9c5bf967611ab5371f13241b4b58/f72fc91949bc94c504def36747e9b4c7/image.png)

This will download a zip file. Open it, select the “Queries.csv” file, and upload that to your Claude chat.

Download a new CSV using this method each time you perform the analyses below (e.g., monthly), so Claude has up-to-date data.

## Part 2: Find keyword opportunities

In this part, we'll show you how to uncover keyword opportunities based on your competitors and find easy win opportunities.

By default, Claude will output all the ideas for each of the methods below as individual CSV files. I recommend performing each of them within the same chat, so Claude can easily combine and sort these CSV files without you having to share files between chats.

### Find keywords competitors have that you don't

Find keywords your competitors appear for that you might be missing by performing a [keyword gap analysis](https://www.semrush.com/blog/keyword-gap-analysis/).

If one competitor ranks for terms you don’t and they have a similar target audience to you, then these terms may be worth targeting yourself.

If multiple competitors rank for a term that you don't, that's a strong signal the topic is relevant for your target audience and one that you may want to cover.

Find your keyword gaps using the prompt below:

*Perform a keyword gap analysis between the competitors listed in the business context file and my domain, one at a time. Apply the following filters:*

- *Minimum search volume: [e.g., 100]*
- *Keyword difficulty range: [e.g., 0-49]*
- *Search intent(s): [e.g., commercial and transactional]*

*First list the top 10 keywords for each competitor individually. Then find up to 10 keywords that all competitors rank for but my domain doesn't (if there are none, just flag that and don't perform any further analyses).*

*Prioritize keywords relevant to my business per the business context file. Exclude branded keywords and navigational intent (e.g., “[competitor name] login”). Combine all the results into a CSV.*

Note that you can ask Claude to find more than 10 keywords at a time, but this will increase API unit use.

Here’s an example output from this process:

![Claude keyword gap analysis CSV listing competitor keywords with positions, search volume, difficulty, CPC, and top URLs](https://static.semrush.com/blog/uploads/media/cd/2d/cd2d9f49e5084d740e307179312364a3/382e7b4f05362a26e5c411a94f5864cb/image.png)

Because Claude has context about your business, it can perform a keyword gap analysis with business relevance filtering built in. That prevents it from surfacing keywords that may not be relevant to your business.

### Find the easy wins in Search Console

You'll now find queries you rank for but not well (e.g., in positions 8 to 20), or that you get few clicks for based on your Google Search Console data.

Because Google is already ranking you somewhere for these terms, your content is already deemed relevant. That’s why they could be easy wins.

Further optimizing your content for relevant keywords you’re already ranking for improves your chances of ranking better with less effort than trying to create completely new pieces from scratch.

Use this prompt to identify easy win opportunities (make sure you’ve uploaded the Google Search Console queries CSV from part 1):

*Analyze my uploaded Google Search Console query CSV and identify three types of keyword opportunities:*

- *Keywords ranking in positions 8 to 20*
- *Keywords with high impressions but low CTR*
- *Keywords with impressions but no clear page covering the topic*

*Use my uploaded URL list to spot coverage gaps. Output a CSV with columns for the keyword, the type of opportunity, why it’s worth prioritizing, and whether it should be a new page or optimization of an existing page (with the corresponding URL).*

Claude will output the CSV, but it may also summarize the most important opportunities. Like this:

![Claude summary of keyword opportunities grouped into positions 8–20, high-impression low-CTR terms, and content gaps](https://static.semrush.com/blog/uploads/media/ef/23/ef23d642ef2a486af1d2c6ccdd44a6fa/3941c96ceac8683c46f980a292c02ef7/image.jpeg)

Since this step is based on your own Google Search Console data, you don't need to validate these keywords with Semrush to know that there’s real demand for them.

## Part 3: Find what customers actually say

This part involves finding what your potential customers and existing customers are saying and turning those comments into keyword ideas that you can create content around.

### Mine competitor reviews

Mine your competitors’ reviews to identify words and phrases that their customers use to describe their products and services and the kinds of features customers value.

The language you find in competitors’ reviews helps you identify opportunities that traditional keyword research might not.

For example, if a customer leaves a review for your competitor and mentions features that they wish the competitor's product had, you could create a piece of content that highlights the fact that your product or service **does** have those features. And that could lead to appearing in relevant search results or AI responses.

For example, several G2 reviews for project management tool Trello note that it doesn’t support task dependencies.

![G2 Trello customer review highlighting a complaint about the lack of native support for task dependencies](https://static.semrush.com/blog/uploads/media/21/a9/21a9f3e1768993940ce5b4d7b96802ad/32b267046315f5cd38127b6fea4226c7/image.png)

SmartSuite, another project management tool, has content specifically about dependencies in project management. One of its articles highlights how SmartSuite helps manage dependencies.

![SmartSuite article about dependencies in project management, including definitions, types, and examples](https://static.semrush.com/blog/uploads/media/b4/ef/b4ef7eb15ac85863f35e024a35916f3b/b6b6f4da1b856ee797c6172735eaf0c0/image.jpeg)

This piece of content is cited in the AI Overview for related search terms:

![Google AI Overview explaining four types of task dependencies, with SmartSuite cited as a source](https://static.semrush.com/blog/uploads/media/a9/49/a949c6097b9932b8638eab1fc6bcd28a/0fcd70e5303e7634bfc7562d77df148a/image.jpeg)

Where you look for competitor reviews will depend on your product or service and industry. If you’re in B2B software, websites like G2 and Capterra are good places to start.

If you sell B2C products, then your competitors' Amazon reviews are worth looking at. So are reviews on their website or any other sites where they sell their products.

To turn your competitors' reviews into usable context within Claude, simply copy reviews and paste them into Claude.

![Competitor customer reviews pasted into Claude for analysis, including positive and negative feedback](https://static.semrush.com/blog/uploads/media/7e/fc/7efcf8449b3509cefa7dfba99fe3a5cd/791f3936c27424056802aac1fbb841a5/image.jpeg)

Then, add the prompt below:

*Group the attached reviews into recurring themes, summarizing each one. For each theme, pull direct phrases or quotes showing how customers describe their problems, or features they like or wish the product had. Turn these into realistic search queries someone with that pain point might type into Google. Output as a CSV with columns for keyword, theme, and source review summary.*

Because this prompt is designed to link each suggested keyword idea to the review that it came from, you can verify why Claude has suggested each keyword idea.

You'll validate whether these keywords are worth targeting using Semrush shortly.

### Mine Reddit threads

Mine Reddit threads to identify the language that customers use when describing products or services like yours.

To find Reddit threads related to your offering or business, use the Google site search operator “site:reddit.com ‘keyword’” or browse relevant subreddits directly.

![Google search results for product marketing discussions on Reddit using the site:reddit.com search operator](https://static.semrush.com/blog/uploads/media/c1/69/c169e1d19f88d9661cddc668cc4b96a3/a303502f0fcf4f5395598501a9937cf9/image.png)

A quick way to perform keyword research for these Reddit threads directly in Claude is to use a prompt like the one below that simply searches Semrush for the keywords a given thread ranks for:

*Use Semrush to find the top [number] keywords that [thread URL] ranks for and include search volume, keyword difficulty, and intent for each one. Exclude any keywords that contain “Reddit” or common misspellings, as they have navigational intent.*

This works because, if the thread ranks for a given term, the term is likely relevant to what your target audience was talking about or asking about in the Reddit thread.

However, the method of seeing what terms a thread ranks for requires the thread to rank well in Google, so you can miss out on a lot of potential keyword ideas. That's why I also recommend leaning on Claude to perform keyword analysis in a similar way to how we did it for the competitor reviews above.

To do this, copy and paste entire Reddit threads along with comments into Claude and run the prompt below to get Claude to analyze the threads for potential keyword ideas:

*Using the attached Reddit thread and comments, and the business context file for reference, identify words and phrases users might type into Google or AI search tools related to my products or services. Focus on pain points raised in the thread. Output as a CSV with two columns: one for the keyword and one for the thread or comment snippet it came from.*

***Further reading****:* [*Reddit keyword research: How to find hidden SEO opportunities*](https://www.semrush.com/blog/reddit-keyword-research/)

### Pull topics from your sales calls

Pull topics from your sales calls using the exact words and phrases prospects and customers use that you may not currently have content optimized for.

Simply upload your sales call transcripts to Claude and use the following prompt to extract keyword ideas:

*Using the attached sales call transcript(s), identify keyword ideas based on pain points, complaints, and features prospects praised or wished the product had. Output as a CSV with columns for keyword and the exact transcript snippet it's based on.*

### Validate search demand

Validate the keyword ideas Claude generated based on competitor reviews, Reddit threads, and sales calls with Semrush to get metrics like search volume and keyword difficulty to help with prioritization.

Use this prompt to get Claude to validate search demand using the Semrush MCP:

*Combine the keyword ideas from the competitor reviews, Reddit threads, and sales call transcript into one CSV with columns for keyword, search volume, intent, keyword difficulty, and source, including the snippet each keyword came from. Use the Semrush MCP to find volume, difficulty, and intent for each keyword. If no volume data exists, enter 0 for volume, N/A for keyword difficulty, and estimate intent based on context.*

You'll probably find that a lot of the keyword ideas suggested by Claude have zero search volume or no data returned by Semrush. This doesn't mean there’s no search demand for that term. It could just mean that that exact wording currently shows no search volume.

Because these keyword ideas came from things potential or existing customers said, they may still be worth targeting in your content. In these cases, use your judgment to decide whether it's worth creating a piece of content around that term or optimizing an existing piece. Or come up with your own variations and check for search demand on those instead.

For example, Claude suggested the keyword idea of "best community for new freelancers," but Semrush returned zero search volume for this term.

![Claude keyword ideas from competitor reviews, including “best community for new freelancers” and other freelance topics](https://static.semrush.com/blog/uploads/media/82/24/822440810d598c4997de67afefcf79ac/071c566237e95ec3d03b4c7399495a3c/image.png)

I quickly brainstormed that there may be a keyword related to this: "best communities for freelancers." I ran this idea through Semrush, and found that it does get 20 monthly searches. This isn't a huge amount of search volume, but it's an example of where Claude's initial keyword ideas can generate more of your own ideas with fairly little effort.

![Semrush Keyword Overview for “best communities for freelancers,” showing US search volume of 20 and unavailable difficulty data](https://static.semrush.com/blog/uploads/media/89/99/899918459950f21d7d7926c829ed1e73/a48b3fa4981c2b99a5b2b9004a9b4aec/image.png)

## Part 4: Prioritize the right terms

Choose the right terms to target by asking Claude to consolidate all of the keyword lists it identified in each stage of the keyword research process, then ask Claude to prioritize them based on what matters most to your business.

Get a prioritized list from Claude by entering a prompt like the one below:

*Combine the keywords from the individual keyword gap analyses, the keyword gap analysis vs. all competitors at once, Search Console easy-win analysis, competitor review analysis, Reddit thread analysis, and sales call analysis, using only validated keywords for the latter three, into one CSV with columns for keyword, search volume, intent, keyword difficulty, topic cluster, new/existing page, and reasoning.*

*Cluster keywords by topic, since several may fit one piece of content. For the new/existing page column, check my uploaded URL list, and if unsure, note this in the reasoning column. Prioritize primarily by business relevance, then by search volume and keyword difficulty. In the reasoning column, explain why each keyword or cluster was prioritized.*

*Then create a separate CSV for keywords you couldn’t validate any Semrush data for. Cluster these keywords too, and note where each keyword idea came from.*

Here’s an example output with the validated keywords:

![Keyword list validated with search volume, difficulty, intent, source, and snippets from competitor reviews and Reddit threads](https://static.semrush.com/blog/uploads/media/f7/dd/f7dde817a3ef700c6818bf995857acff/762bee69999dd0d5c5f2e4c565d626b5/image.jpeg)

How you choose to prioritize the terms that Claude has found depends on your goals. Prioritization is an important part of keyword research, but the main things you should take into account when prioritizing keywords to target are:

- How relevant the keyword is to what your business does
- The likelihood that targeting that keyword could lead to a conversion

Search volume, keyword difficulty, and [search intent](https://www.semrush.com/blog/search-intent/) can be useful for gauging search demand and for rough prioritization. But just because a term has a high search volume doesn't mean it's likely to convert many users. And just because a term has no search volume doesn’t mean it’s worthless.

That’s why we asked Claude to generate a separate CSV for keywords it was unable to find any Semrush data for. These are terms you’ll have to manually assess to decide whether they’re worth creating or optimizing content for.

I recommend looking at the snippet or thread that led to that keyword idea from Claude and determining from that how useful a piece of content on that keyword would be for your target audience.

For example, one of the keywords Claude suggested from the sales call transcripts that had zero search volume was "how to find freelance clients consistently." If my business sold coaching services, a promise to help you find more clients consistently would likely be compelling. And I could target that keyword with a blog post or landing page with a CTA for my services.

## Turn your keyword ideas into high-quality content

You should now have a CSV of topic clusters you can use to create content.

Many of the keywords Claude identified will likely require new pages. Find out how to create optimized pages for these keywords in our guide to [creating SEO content](https://www.semrush.com/blog/seo-content/).

If you want to try the workflows in this article for yourself, sign up for a [free trial of Semrush](https://www.semrush.com/semrush-free-trial/) to get access to the MCP.
