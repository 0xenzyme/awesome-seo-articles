---
title: "Video Schema: What It Is & How to Implement It"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "video-schema"
url: "https://www.semrush.com/blog/video-schema/"
canonical: "https://www.semrush.com/blog/video-schema/"
author: "Vishal Dave"
published: "2023-11-03T10:46:00+00:00"
updated: "2023-11-03T10:46:00+00:00"
categories:
  - "General SEO"
freshness_reasons:
  - "date_2023_aging"
schema_genre: "General SEO"
fetched_at: "2026-06-12T20:26:30+00:00"
status_code: 200
html_hash: "ca53d174b26b8960ef7bd53df59865840c7d534ad1773f130c2e3b9c937f41aa"
clean_word_count: 2470
clean_char_count: 21146
---
# Video Schema: What It Is & How to Implement It

## What Is Video Schema?

Video schema markup is code that helps search engines understand and display your video content in search results.

Adding video schema markup to your webpages supplies additional details about your videos. For example, the title, description, thumbnail, video duration, and upload date.

Google uses this information to generate rich results. Here is an example:

![An example of video result on Google SERP from Shutterstock](https://static.semrush.com/blog/uploads/media/8e/03/8e032993bb24e3e6e8ace9bd9778b301/f020f9602de588632a301afcb456bb90/AD_4nXec6cnznMcb0PRNonCTSzsdXGqCAXv1MwEWtGphb9d1iezYTlCBPdLg9_SmiZGC5_fUWf-Upe-fUDBaFbUI7qp0pqGRaTU5pj4VmhCIe7iyr71RihNNLTaHmyvFHUApJDGOW_eVnw.png)

In this example, Google shows the thumbnail, title, description, upload date, and uploader information.

This feature makes the video result stand out on search engine results pages (SERPs) and often generates more clicks.

In this post, you’ll learn everything you need to know about using video schema markup.

Let’s get started.

## What Are the Benefits of Using Video Schema?

Using video schema is not a direct ranking factor. But it provides indirect SEO benefits.

Video schema markup makes your video eligible for an immersive, rich snippet format. This often includes a thumbnail, the video duration, and other relevant information. It stands out more than standard search results.

When users see these rich snippets, they are more likely to click. This can improve your overall click-through rate (CTR).

For example, see this video in a rich snippet format:

![Indian Premiere League's "Highlights - Men & Women | IPLT20" rich snippet result on Google](https://static.semrush.com/blog/uploads/media/c0/de/c0de690a03da54f411aeabb5dacf5ff8/0fd03a952827f9ceeb2b4b230f281423/AD_4nXeVPzrkYc-5vdyfGkbuRI8cIgp_EE5twHUex6OsCGEZu_FQHbEvfnykwB5Lr4A-DLikxFZ7sPq2J3FqtQdaZOPPTWFhTlBA8VIN_PdjvvMFALtVV_SiVQJx4hgGCGxu_bR5vC4F.png)

Compare it to the plain blue link result:

![JioCinema's "Tata Ipl 2023 Highlights" plain Google result](https://static.semrush.com/blog/uploads/media/de/3c/de3ce4027fbc600721ac259fe1b718db/857dd931b61d1a22c4ef160df3c8e82c/AD_4nXctGf0TpRlLS22sF7kduiA3_dDE9Mbbgbz3FpNMVyNKEMQGv_wB7bqqm5JuoN-it2ybHs58RqgCOhXphnuWp7QUAzzvpTT9r1guwbw71rW8jB24dIefIfjsPjdNVin1B5QB9W_KDQ.png)

Which would you click? Probably the first one.

Another benefit of video schema is that it helps Google understand your video’s content. This may make it more likely that Google will rank your video for relevant search queries.

## Examples of Schema Markup for Videos

Video schema markup comes in different forms. But they all use VideoObject schema as the foundation.

VideoObject schema marks up your video and defines its properties. It can appear as JSON-LD or Microdata. JSON-LD is placed inside a <script> element that can go anywhere on the webpage. Microdata relies on specific HTML tags to embed structured data in the code.

Google supports both formats but prefers JSON-LD, so that’s what we’ll focus on here.

Below are examples showing how different properties change your video’s appearance in search results.

### Standard Video

This screenshot shows a video result that uses standard VideoObject schema:

![Hotstar's video rich snippet that uses standard VideoObject schema on Google SERP](https://static.semrush.com/blog/uploads/media/61/89/61897f0cf16a186cfcf897e7b066611b/11d26149b43ea01ab5ec7acb41e9385b/AD_4nXe3xWU75Czih7ua8gYSVOvt87wOC_2OzuY7OswBFQZUXabAXK_Z_Fk9cqoeXhFowH2CfO7oMh194UoMvgpsEll2UNvWTZqYrft8vwok1_PVwCrZJUSCWzQTRR-I4HHdFUx5wlcA2Q.png)

Here is the markup code powering this snippet:

`<script type = "application/ld+json" >
{
"@context": "https://schema.org",
"@type": "VideoObject",
"name": "Action Recap: Pakistan vs India",
"description": "Watch the best moments from the Asia Cup 2023 match between Pakistan and India",
"thumbnailUrl": ["https://img1.hotstarext.com/image/upload/f_auto,t_hcdl/sources/r1/cms/prod/9889/1589889-h-655968c7423d"],
"uploadDate": "2023-09-10T15:13:40.000Z",
"duration": "PT0H9M51S",
"embedUrl": "https://www.hotstar.com/in/sports/cricket/asia-cup-2023/708507/match-clips/action-recap-pakistan-vs-india/1540024271",
"regionsAllowed": [{
"@type": "Place",
"name": "IN"
}],
"publication": {
"@type": "BroadcastEvent",
"isLiveBroadcast": false,
"startDate": "2023-09-10T15:13:40.000Z"
}
</script>`

This markup helps Google display the video in a rich snippet and makes the result stand out.

### Live-Streamed Video

For livestream videos, you can add BroadcastEvent properties to show when a live event is happening. Google then displays a LIVE badge on the video snippet.

Here’s how a snippet using BroadcastEvent properties appears:

![Hotstar's video rich snippet that uses BroadcastEvent properties on Google SERP](https://static.semrush.com/blog/uploads/media/5f/2a/5f2ae8f5d03ee05d8bfa326430816c01/e1ac2dec2b21a13fd643b545954479ff/AD_4nXcxOPB8szKHB4LqzMgM5fj5MlZn6EtOUbMANkFeOvTNb7A7LPqlOh0jaMR4zhMutJmWU62wLPujWfAj8phiQBp5ddmRtZ-LQZLQS3np72K9GLfNTMmE5oxd-Fm-ATP7CI0CKklc.png)

Here is sample code:

`<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "Super 4s: PAK vs IND",
  "description": "Watch live stream of Asia Cup 2023 Super 4s match between Pakistan and India.",
  "thumbnailUrl": ["https://img1.hotstarext.com/image/upload/f_auto,t_hcdl/sources/r1/cms/prod/8563/1588563-h-364f2ca5f332"],
  "uploadDate": "2023-09-11T07:30:00.000Z",
  "embedUrl": "https://www.hotstar.com/in/sports/cricket/super-4s-pakistan-vs-india/1540025325",
  "contentUrl": "https://www.hotstar.com/stream/super-4s-pakistan-vs-india",
  "regionsAllowed": ["IN"],
  "publication": {
    "@type": "BroadcastEvent",
    "isLiveBroadcast": true,
    "startDate": "2023-09-11T07:40:10.000Z"
  }
</script>`

Use this markup for live events such as news programs, award shows, or sports events.

Google recommends calling its indexing API to request crawling when the live video starts and ends. This ensures the LIVE badge appears promptly.

### Video Clips

You can also add Clip properties to indicate important moments in your video. Google can use them to display timestamps and labels.

Here is a snippet example that uses Clip properties:

![YouTube's video result that uses Clip properties on Google SERP](https://static.semrush.com/blog/uploads/media/21/2a/212a56e5b2f6cab4e4e2ff58d03c72a6/10e900524c1ab0f2e2c223ac34687229/AD_4nXeHYtSKn79uaVO3JzDu8ePwUySn2He-E8ruxgLn9NuvpF8rTbbwgHdZzntUftvGrP2jWVgDIvj7KY7mP0d52GTqLHO6R4LBF234WfppcHj37UyShCdG9TmvfSNeEUnnNo75fb2X.png)

And here is a sample code:

`<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "How to Meditate 🙏🏼",
  "description": "Meditation is a practice that can benefit your health and wellness in so many ways.",
  "thumbnailUrl": ["https://i.ytimg.com/vi/oq6j9uWrcfg/maxresdefault.jpg"],
  "uploadDate": "2016-09-21",
  "duration": "PT4M10S",
  "embedUrl": "https://www.youtube.com/embed/oq6j9uWrcfg",
  "genre": "Howto & Style",
  "author": {
    "@type": "Person",
    "name": "Lavendaire"
  },
  "interactionStatistic": {
    "@type": "InteractionCounter",
    "interactionType": { "@type": "WatchAction" },
    "userInteractionCount": 2054538
  },
  "hasPart": [
    {
      "@type": "Clip",
      "name": "Purpose of Meditation",
      "startOffset": 30,
      "endOffset": 45,
      "url": "https://www.youtube.com/watch?v=oq6j9uWrcfg&t=30"
    },
    {
      "@type": "Clip",
      "name": "Benefits of Meditation",
      "startOffset": 50,
      "endOffset": 120,
      "url": "https://www.youtube.com/watch?v=oq6j9uWrcfg&t=50"
    }
  ]
}
</script>`

This helps users jump to a specific moment in the video directly from Google.

## Recommended and Required Properties for Video Schema

Properties are video attributes you define in markup (e.g., name, thumbnail image source, etc.).

VideoObject supports [many properties](https://schema.org/VideoObject), but not all are necessary. Google says three properties are required for a rich snippet:

- **name**: The title or name of the video
- **thumbnailUrl**: The source of the thumbnail image
- **uploadDate**: The date when you uploaded the video

Google can’t extract the video’s information if any of these are missing.

Depending on the video type, you may need other properties. This table summarizes all video schema properties. (Properties marked with \* are required.)

|  |  |
| --- | --- |
| **Standard Video Schema Properties** | |
| **Properties** | **Descriptions** |
| name\* | Name or title of the video |
| thumbnailUrl\* | URL of the video thumbnail image |
| uploadDate\* | Publish date of the video |
| contentUrl | URL of the actual video file |
| description | Video description |
| duration | Video duration in ISO 8601 format |
| embedUrl | URL of the video player where the video is embedded |
| expires | Expiration date of the video |
| hasPart | Used to nest the Clip properties |
| interactionStatistic | Number of total views the video has |
| regionsAllowed | Places where the video is allowed |
| **Broadcast Event (Live Badge)** | |
| publication\* | Used to nest BroadcastEvent properties when the video is live |
| publication.endDate\* | Date/time when the live stream ends |
| publication.isLiveBroadcast\* | Boolean value that defines if the video is live or has ended |
| publication.startDate\* | Date/time when the live stream starts |
| **Clip** | |
| name\* | Name of the clip |
| startOffset\* | Start time for the clip |
| endOffset | End time for the clip |
| url\* | URL of the video that points to the starting of the clip |

Learn more from [Google’s documentation on schema markup for videos](https://developers.google.com/search/docs/appearance/structured-data/video#video-object).

## How to Implement Video Schema

Implementing video schema markup is straightforward.

There are multiple ways to do it. The simplest approach is to write the code manually and add it to the webpage.

Here’s how:

### 1. Create the Video Schema Markup Code

Create your video schema markup code in JSON-LD format.

Use a text editor and start with this template:

`<script type="application/ld+json">
{
"@context": "https://schema.org/",
"@type": "VideoObject",
"name": "Name of the Video",
"thumbnailUrl": "https://example.com/thumbnail.jpg",
"uploadDate": "2024-01-28"
}
</script>`

Change the video name, thumbnail image URL, and upload date to fit your content. Then copy the code.

### 2. Validate Your Schema Markup Code

Visit [Google’s Rich Results Test](https://search.google.com/test/rich-results).

Switch to the "**Code**" mode on the main screen and paste your markup code.

![Rich Results Test showing a code snippet.](https://static.semrush.com/blog/uploads/media/35/ed/35edc610e9c26cb1a4c4cf64192c6147/b32d636ae561134a4015c70c7eb90029/AD_4nXeg-8Q5xXhQXS63_1V__KXAAlf6RT_buWop3yMgzJdrWoH1S7ruZ_rsHMZGd6fbRT7FTVJeRhE_2cMP8QS5Ue3QZ0i22N3BIOezQLHypu-rT6xQVq_TQIsXvMAxlGdK_x9BwIfQEQ.png)

Click the "**Test Code**" button.

After validation, the results will appear:

![Test results section in Google’s Rich Results Test](https://static.semrush.com/blog/uploads/media/59/e2/59e2252a8082e7216f3917911e21f8d1/f0e7e639a7be2e0f757281b0bbffd82e/AD_4nXfWC-W2GVlsHEcAUzS-MKZu0iaLYbwlWj8IIhHPOyiEnE0sWshLPurw1A85_5x4jncukzw5BLWY7rcDa03NwLtWmqQ7ABZdsR1t3UT9b0Do7KaNHQ9m5Jki3mX_XvV32FNCkU59OA.png)

If there are no errors, the markup is ready for implementation.

### 3. Add the Video Schema Markup Code to the Webpage

Open your content management system (CMS) and find the webpage where you want to add schema markup.

In WordPress, you can follow these steps:

From your WordPress admin dashboard, go to "**Posts**."

![WordPress dashboard with posts menu open.](https://static.semrush.com/blog/uploads/media/8e/6b/8e6be1767de14ce37c9462101943e7da/b77028dcb76293579a9f1aab7d06f613/AD_4nXcYjvQxXddWdvMtl4szdqCCVJ8ylUacm7LKOWzt1fxseFuTf7VqzxrQIshdeLG6UXIctXH9yYQRlNzgV1vITa1cMoam0fjJzuNwaIGZyuh7XG-hD_TSZJQ9vhEg-mpsHfKgftfLTw.png)

Locate the post you want to add schema to.

Then click "**Edit**."

![WordPress dashboard with example post and edit button](https://static.semrush.com/blog/uploads/media/dc/53/dc5332fcc26cc7564002d5a925e2a0ce/b51e971c4c90bf7915d60ac7a53d1f2b/AD_4nXfglWj3hKnaFOyyUVADAn3dm7hUTwgf6J3ETBqYZ0B04acA76UzOsT87xxbRzF4nH6kTHW3dlxcTE1xRYY8cgObyuUZNMqcUK91ll9NRVt8ZFyw-vtPSyrqwxt18pIyVA5-adnU.png)

The WordPress block editor will open up.

In the editor, click the "**+**" sign (anywhere in the page) and create a new "**Custom HTML**" block.

![Custom HTML option in WordPress block editor](https://static.semrush.com/blog/uploads/media/fc/5b/fc5b68980b707ff1715bcef8000d5259/3a0228a39b49d427bc11a2fe767d1999/AD_4nXdyix63tr0NB48O_z_KtBt3Ke0YbeAd2Zxmw3sQZdDBX4K3hkyV2snWLrEh9SE_Nwam4n-u6aNUTMx7ZWhORrkCXqjJg1gpn12SpWS0N0s1Y5-SOnT-8d0HvJIr_DYMbmfN5OfUMA.png)

Now, paste the code in the HTML box as shown below. And click "**Update**."

![Custom HTML added to a WordPress post](https://static.semrush.com/blog/uploads/media/8b/d8/8bd8a169a19db75bb0aba70cc8079dab/793c6a226773f95f14f1a281e07d0d99/AD_4nXd66UcHjZnlz68mXh8RrANIlI6_3KzXhKTK1h0RlTVcqxUOtUGqNbTdKw8SzFq0j1tPzXvClOyfhyQbxX4M8j7vSfzSwZQffp9NFCes7TtUwGSLP15KzOVMonLVX8L_Kh9LtjH2qg.png)

### 4. Perform a Rich Results Test

After implementing your markup, test it with the [Rich Results Test](https://search.google.com/test/rich-results). Or you can use [Site Audit](https://www.semrush.com/siteaudit/) to scan for multiple schema types, including video schema.

Create a new project in Site Audit:

!["Create project" button highlighted under Site Audit tool](https://static.semrush.com/blog/uploads/media/91/8f/918fad0e95eef5d9fd178cbb8759aa72/fce8c357d8f4000fcab9db5586a846dd/AD_4nXc_zThIeuGnW96gCgVMbCtCw0lytrXVm0vDRTksMx2UFkgFDgWv3s8jmaiZ4lI0GGPp1VAuq5IJ4dafk2WJGC02qQ_I125ZoXiu7InFRZW_Xy4scjTICcml7ZsvZnVQ0jHlX9Np3g.png)

Enter your domain and project name, then click "**Create project**."

!["Create project" pop up window in Site Audit tool](https://static.semrush.com/blog/uploads/media/c7/3a/c73a73839c6f26ffd7bc3809df3e5db2/3fd3ab92753b75e8c92e151481acf5e0/AD_4nXcem_IcQciCjtRDjfkDVxNgwpYEJg7t9Yety4KPGom4IMfPz8d4Sd0kzjSYwr4iFOaLfLE5r_IFn79cyzz8Gg2jzkSYPzgMmac2su4v_wj1FyFxQLt0IR6OY-IshWDT2mMgsLJGCA.png)

Follow the setup instructions.

In the last configuration step, you can set a schedule for recurring audits.

Then, click "**Start Site Audit**."

![Site Audit settings configuration screen with schedule option.](https://static.semrush.com/blog/uploads/media/38/22/382242cca9b9e716998ac6bfa6103274/12f2a779d733c179402e6275c500873d/AD_4nXc3dQ1g4FAnWB3kWD8T_2t-AjYmNDLXfLr7LUr2yXPxSez7cQhoXN16cR0Bfp3KlHd8c25_3cA9YyGLxRaQDrXQqmmR2rr9gFr4Ef5FIP24tlGZv4kyvrPZW8GvP8jUmVe-IiS3.png)

When the audit is complete, go to the "**Issues**" tab and type "structured data" into the search bar.

!["structured data" entered into the search bar under the "Issues" tab](https://static.semrush.com/blog/uploads/media/5e/11/5e1134c7734a01082a61c861b6fef9c5/0d175d49d0138c55bd5a2052971a2899/AD_4nXcWxPG4i440IKkAF2eVyuoA-qyN-63-moGbJCpkKXGqv7XDcSKRGa07WH-5UUOVPhvhJAwlmCtrU2XUFVxhEmr3DAI97OSqrnoepUmXPZamRpuW0MPmoeqUHSHVcALq5lQ2hCvGzA.png)

You’ll then be able to see any problems with your structured data, and you’ll get advice for fixing them.

![Structured data issues identified in Site Audit](https://static.semrush.com/blog/uploads/media/f7/dd/f7dd0c9f2da3bf4808afb1c7fde9857c/dcc3695b3328c678ec4755ffb0dc75c2/AD_4nXe_dfOsYF35-rp_jIYWJP-Jdy4caxPX2xBJbzPGjntpH4OF3Ryif75trpOmASJruW8fflPq8RIcU_ESoac4PFrwRsTWwkdx5bQgFdvpSM2ex7J06a7l4bJYlHIxcsp0SOFpttla0A.png)

## Best Practices for Video Schema Markup

Using schema for videos can boost your organic marketing strategy if you implement it correctly.

Here are some best practices for successful video schema implementation:

- Insert keywords naturally in properties like the name and description
- Ensure you have all required properties from Google
- Update the markup code whenever the video changes
- Validate your markup before implementing it
- Audit your site regularly to spot new schema issues
- Verify the thumbnail image link is accessible to Google
- Track the performance of your video rich snippets

## Measuring the Impact of Video Schema on SEO

Video schema can expand your organic reach. But measuring your performance is essential.

Use [Google Search Console](https://search.google.com/search-console) to see how your site’s video results perform.

Go to the "**Performance**" section and click "**Search results**."

!["Performance on Search results" graph in Google Search Console](https://static.semrush.com/blog/uploads/media/69/fd/69fdd1eca9afaf060a38396607e6d49f/ab2661afd48b04eb62c069b3dce652c8/AD_4nXeb9f5GfXuzqwniKR8h15-8rFhIftm8v39TJ8VvqSNaJ_ZK2EDHEoVzqgrHpyZwNm6SVrLZZ3Mbxgo_1lep-1R9CobD86J4W5bmAH3Pzj9YgcJKnL9P-0XKKnMYcp_WnxisXv_LOw.png)

Scroll to the table and select “**SEARCH APPEARANCE**.”

The "Videos" row shows how many clicks and impressions you get from video results.

!["Videos" row highlighted under “SEARCH APPEARANCE” table](https://static.semrush.com/blog/uploads/media/ce/e9/cee9234e317d63f7cade5fb640422e96/4c627e51cc2def9d14989ae9fd67eabd/AD_4nXfCbNJ0zWXe8t6KMVfEbDScn3KL0oH9oZBTdYxA-cLPJGrrCSHXFuzcoFbaqG2MIHKq-BYRUtj-RhRIBC1qBG-FzOYWrWPW3QHsGtIfPC9S3HluvHb3fhVxXuMiLVrjnU9y4LX0QQ.png)

Click "**Videos**" to filter the performance report for video results.

!["Performance on Search results" report in GSC with video results filtered](https://static.semrush.com/blog/uploads/media/06/9f/069f0fa0ae633f8cd4a64d8b79d9a129/ddeb658d8d66691d4c40f64d7da9cec4/AD_4nXcaLuX8EzX8_Z6SNgBZbiQT9cHRvazP17tClKSoCGvRYc5I_Q_x4Bznq_lsp6eggfJe3kORjxM4xStx4FeaSIhQ8aQsRfcjgujthsaPzXer9DZuLy38WaSTo2YmQA6qmZD22zMssQ.png)

Adjust the date range to see how your video schema implementation performs over time.

Another way to track the impact of video schema is to use [Position Tracking](https://www.semrush.com/position-tracking/).

Go to the Position Tracking tool and click “**Create project**.”

!["Create project" button highlighted under Position Tracking tool](https://static.semrush.com/blog/uploads/media/46/3a/463a629687730c2d4c92d845124c0904/928fb816d4d05e11d9de230295ddc179/AD_4nXeZAVBkHKiSXryaFcW7X3qstla5rc-Do4Fs3I4ibDX3Wd-5CwXcj7lajDLFAc-NaxHoolaVE3v1K8d4NRBegdFkw068bF8aarV5iCgEYMnriFc6AJDBYvhx6irKIDTBFctlwZeSrA.png)

Enter your website domain and click "**Create Project**."

!["Create project" pop up window in Position Tracking tool](https://static.semrush.com/blog/uploads/media/84/08/84084a005578e018c209b00f897190f6/24e76915f62148865942b870d0e5000e/AD_4nXfUzFPJEG5JdHgu6qe69mZaGeig-pK2rNg6h9WWDc8mKSxznl5KG2j_8jPmqOzvjnUyI_4ZTZfumxhJZKsxrBW0yXojOBxBDS2WeCQOu8KgJhVxHh-oiwi3kP1cGGKvdLsAv1t8cA.png)

In the "**Targeting**" section, select "**Google**," then choose your device, location, and language. Click "**Continue To Keywords**."

!["Targeting" window in Position Tracking settings](https://static.semrush.com/blog/uploads/media/b1/b1/b1b1c81173b4e7a1bcd7450a2ac6fafd/df9f7829c83526c8a261cd57616575cd/AD_4nXdGG1_eosa3mVbhls9HUp4LeOnnkbcoOczJWWrGEsY9TE7kDTrJUTUUleJMaMjnz86DTiZqNPUZkz3zSNnn2f_zLKOYFNmaq4-DVq7w6Zbb8u8vP9NIJyjoYlxfmsgw4gSeOSOFSQ.png)

Add the keywords you want to track and click "**Start Tracking**."

!["dog food," "pet treats," and "flea treatment for cats" entered under "Keywords" window in Position Tracking settings](https://static.semrush.com/blog/uploads/media/26/58/26589a87cb39d0388f4ac38ccfc431d0/645660deb8842a8ca0106da144150aa7/AD_4nXcAXvp9AeSq9HWs57nX01yrK5c6Gva7p9et7Lv5HtrAlXMf_XpBoTXPYE-1PtNY0U6peHInpJz5kcWKe8Y86TlRS_yKR95MFso4xp_tUdcqOJcYfvt3za3sjA0KaX93Pos3Kwwu.png)

After setup, go to the "**Overview**" tab, click "**SERP Features**," and choose "**Video**."

!["Video" selected from the "SERP Features" drop-down menu in Position Tracking](https://static.semrush.com/blog/uploads/media/9f/40/9f403131d74479f9dc0f8b0853098f44/1e3f92eca95e22bf21bdd25116a37f57/AD_4nXcqLfaUmXdRDtyz_EM5CMDSOrQ3QGX3d10kTw7N_zqVR5CeRX50_TmvQVkHURr_02bKjL0gNGlfiCgJFVTIHbmVQ0fAP_IH7_VhqG0f5zIR9pWsA8RDsaA0XKS-C1MmQLc1zzJ61Q.png)

Then select "**SERP Features**" again and set it to "**your-domain.com ranks**."

!["chewy.com ranks" selected under "SERP Features" menu](https://static.semrush.com/blog/uploads/media/81/ed/81ed0caf6237f753dbfdee52083be223/115f6abe71d69b169ec4efde1a580614/AD_4nXd-yVpbPSUTAHtZt6bg80aZmRrrB_bqLJUxzb0kO6fTAwmS3QWp9nOYTeD57c4hJdpjLWUAmQR9UgRxcOVQfoj-MYZ4V0zpnve0ukHJwy0c5fay0vj2tm2IiwtisF8RbsMmL81FRw.png)

This view shows all keywords for which your site ranks with a video result.

!["Rankings Overview" report in Position Tracking tool](https://static.semrush.com/blog/uploads/media/c0/e6/c0e60d72e111f2151c1814258a0bb543/afe355e4c10d036ca0b5243f56f3f3cd/AD_4nXethtBqk676mjILuI3pTA4yANoSQqNDkln-mjJJppfOpKwjlSJGgJAzX5CT6b2CW3-pY5poaMi2dE3QgSx8kc1ilpQv9H3__EZLlsinvVHAxjHzmsn8HaszmEcPlfPpu_uj6k5kYQ.png)

That's how easy it is to track video schema results using the Position Tracking tool.
