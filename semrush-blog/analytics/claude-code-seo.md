---
title: "How to turn Claude Code into your SEO analyst (with Semrush data)"
source: semrush-blog
content_type: "product_or_tool"
freshness_risk: "low"
slug: "claude-code-seo"
url: "https://www.semrush.com/blog/claude-code-seo/"
canonical: "https://www.semrush.com/blog/claude-code-seo/"
author: "Chris Hanna, Faizan Ali, Cecilia Meis"
published: "2026-04-30T08:53:00+00:00"
updated: "2026-04-30T08:53:00+00:00"
categories:
  - "Analytics"
freshness_reasons:
  - "product_or_tool_content"
schema_genre: "Analytics"
fetched_at: "2026-06-12T14:24:00+00:00"
status_code: 200
html_hash: "dfe9488cb15bf2580b0d753db8a0cbef3e7e7be8f45bee36a942d78eca3a6b79"
clean_word_count: 5961
clean_char_count: 38260
---
# How to turn Claude Code into your SEO analyst (with Semrush data)

Getting more data is rarely the problem in SEO. The issue is that it lives in too many places, and turning it into useful insights involves a lot of jumping between tools, exporting CSVs, and piecing it all together manually.

Claude Code and the Semrush MCP let you see the full picture in one place, and in a way that lets you interact with the data in plain English. Here’s an example of what you can do:

![Claude Code analyzes GSC and Semrush data to find low-KD, high-impression SEO keyword opportunities for trafficthinktank.com](https://static.semrush.com/blog/uploads/media/d0/88/d088acd66d98b56f84baad697f7dc6b2/8481f70062134eec07933a8f7b149b59/image.jpeg)

In this guide, I’ll show you how to connect your first-party Google data and Semrush’s competitive intelligence to Claude Code. I’ll then show you how to build a live dashboard that brings it all together in one place.

I'll use one of our portfolio sites (**TrafficThinkTank.com**) as the running example. Traffic Think Tank is an SEO education community and blog that competes for keywords like “how to learn SEO,” “best SEO books,” and “SEO communities.”

Every prompt and analysis in this guide was run against the live site, so you're seeing exactly how these workflows play out for a real use case.

Let’s build it.

*Prefer to watch first? Here's a full walkthrough of the build before you dive into the steps:*

![Youtube video thumbnail](https://i.ytimg.com/vi/quYneNBX4ck/hq720.jpg)

## Step 1: Set up your project

In this step, you’ll install Claude Code and set up the project files. This article will show you what it looks like in the desktop app, but you’ll still be able to follow every step within the terminal/command line.

### Install Claude Code

If you're using the Claude desktop app, switch to the "**Code**" tab and you're good to go:

![Claude sidebar menu with Code option highlighted to start a new coding session for SEO automation tasks](https://static.semrush.com/blog/uploads/media/ed/85/ed859c20eea98a51012b00a2db89f603/1a04c46a81026e2ff8954f2d44517f09/image.png)

If you prefer the CLI, here are the install commands for Mac, Windows PowerShell, and Windows CMD:

If you’re using Mac, type in:

`curl -fsSL https://claude.ai/install.sh | bash`

If you’re using Windows PowerShell, type in:

`irm https://claude.ai/install.ps1 | iex`

If you’re using Windows CMD, enter:

`curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd`

You’ll need an Anthropic account with a Claude plan. [Anthropic’s getting started guide](https://docs.anthropic.com/en/docs/claude-code/overview) covers the basics, but all you have to do here is type “claude” and hit enter. Then follow the instructions to link your Claude account.

### Create the project directory

Set up the file structure Claude Code will use to organize your data. Tell Claude Code to do it directly, pasting in your desired structure. Like this:

![Claude Code creates SEO Dashboard project folder structure with data, fetchers, dashboard, and reports directories](https://static.semrush.com/blog/uploads/media/b9/94/b9941e4de63e424243ea981f7866a8f0/ffd62680549aea360281b121d2f6dcf0/image.png)

Store it wherever makes most sense for you, and give the folder a suitable name. I created this in a folder called “experiments” and labeled the new subfolder “SEO Dashboard v1.”

This might look a bit complex at first, but here's everything we're setting up:

- **claude.md**: A file that gives Claude Code automatic context about your site, competitors, and goals so you don't have to repeat yourself every session
- **Fetchers**: Scripts that pull live data from your Google APIs and save it locally (we’ll create these in the next step)
- **Data**: This is where all your fetched data lives, organized by source
- **Exports**: These are the live dashboard we’ll build and reports we’ll generate

If you want to copy ours, here’s what to paste into Claude Code:

*Create the following file structure:*

- *claude.md*
- *fetchers/*
- *data/*
  - *gsc/*
  - *ga4/*
  - *ads/*
  - *semrush/*
- *dashboard/*
- *reports/*

### Create your claude.md file

Claude Code reads your claude.md file automatically and uses it as context for every session. This means you never have to repeat who you are, what site you’re working on, or who your competitors are. You can ask Claude Code to create one for you, based on information about your business.

For Traffic Think Tank, the claude.md file looks like this:

![Markdown project brief for Traffic Think Tank SEO analysis with site goals, competitors, data sources, and strategy context](https://static.semrush.com/blog/uploads/media/fb/ec/fbecfcf4ceda22784e0e199f4ab1148a/eac7fe7fe15ce0efd9190d3e557f6c5a/image.png)

Here’s what to include (although you can give as much context as you want):

- What your site is for
- Who your main competitors are
- The main topics your blog content targets
- Any gated content/sections you have
- The data sources you plan to connect

## Step 2: Connect Google Search Console and Google Analytics

Google Search Console (GSC) and Google Analytics 4 (GA4) are your first-party data. These sources serve as the ground truth of what’s actually happening on your site.

You have two options for connecting these data sources:

### Option A: CSV exports

If you want to get up and running in five minutes, export and add these reports to your Claude Code setup:

- **GSC**: Go to Search Console, then "**Performance**" > "**Export**." Upload to Claude and tell it to save to data/gsc/.
- **GA4**: Go to "**Reports**" > [any report you want to use] > "**Share**" > "**Download**." Upload to Claude and tell it to save to data/ga4/.

This is enough to run every analysis in this guide, but connecting live APIs gives you real-time data and makes the dashboards and reports more robust.

### Option B: Live API connections

For live, up-to-date data that refreshes on demand, connect to Google’s APIs using a service account. One service account covers both GSC and GA4.

There are quite a few steps involved in setting up a service account correctly. [Google has documentation](https://docs.cloud.google.com/iam/docs/service-accounts-create) on the setup, but we’ve covered the most important steps below.

Claude Code can help you troubleshoot in real time. If you’re unsure of what to do at any point, paste a screenshot of where you are directly into Claude Code and ask it what to do next. It can read the screen and walk you through the next step.

Just be aware that you’ll be creating and sharing private keys here, and giving it access to your GSC and GA4 data. So if you’re not sure, or if you’re setting this up for clients, you may want to consult a developer.

Here’s how to set up the API connections:

1. Create a project in [Google Cloud Console](https://console.cloud.google.com/)
2. Enable the Search Console API and Google Analytics **Data** API (**not** the “Google Analytics API”). You can find this screen by searching for “enable APIs and services” at the top.

![Google Cloud APIs dashboard showing Search Console and Analytics Data APIs enabled for SEO data collection](https://static.semrush.com/blog/uploads/media/e7/d3/e7d37a0f040f6208f3e0955441e6cfaf/3c69a141306dcf2836cf3ca8f194fd2f/image.png)

3. Go to “**IAM & Admin**” > “**Service Accounts**” and create a new service account (you can choose “viewer” as the role here to limit permissions)

![Google Cloud IAM Service Accounts page with Create Service Account button highlighted for API authentication setup](https://static.semrush.com/blog/uploads/media/d9/f6/d9f6f5328ba55150431a1267e9d69d7f/5de4dcfde18bbd852bfc47642b198076/image.png)

4. Create and download the JSON key file via “**Actions**” > “**Manage Keys**” > “**Add key**” > “**Create new key**”
5. Add the service account email (it looks like your-project@your-project-id.iam.gserviceaccount.com) as a user in your GSC property with read access
6. Add the same email as a Viewer in your GA4 property
7. Save the key file as service-account-key.json in your project root

### Install Python dependencies

Python is the programming language that’ll power a lot of what we’re doing with this setup within Claude Code. You don’t need to know anything about how it works or how to use it. Just paste this line into your command line interface (CLI) or Claude desktop app:

pip install google-api-python-client google-auth google-analytics-data

This is the manual way to do it, but Claude Code may install this automatically.

This installs files Claude Code can then use to build the scripts we need to extract the data from our sources. These are called fetcher scripts, and we’ll create them soon.

### Create a config file

Create a config file Claude Code will use when running the fetcher scripts. This is where you'll add your brand name, domain, and IDs for each data source.

Do this for yourself if applicable, and create one for each client:

`{
"name": "Client Name",
"domain": "example.com",
"gsc_property": "https://www.example.com/",
"ga4_property_id": "1234567890",
"google_ads_customer_id": "1234567890",
"industry": "Example Industry",
"competitors": [
"https://competitor1.com/",
"https://competitor2.com/"
]
}`

### Build the fetcher scripts

Fetcher scripts use the service account you created in Google Cloud to pull information from sources like Google Search Console and Google Analytics.

Just paste in the below script that’s ready to use:

`from google.oauth2 import service_account
from googleapiclient.discovery import build
SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']
def get_gsc_service():
credentials = service_account.Credentials.from_service_account_file(
'service-account-key.json', scopes=SCOPES
)
return build('searchconsole', 'v1', credentials=credentials)
def fetch_queries(service, site_url, start_date, end_date):
response = service.searchanalytics().query(
siteUrl=site_url,
body={
'startDate': start_date,
'endDate': end_date,
'dimensions': ['query'],
'rowLimit': 1000
}
).execute()
return response.get('rows', [])`

You can increase “rowLimit” for larger sites, but the GSC API has a **daily limit of 50,000 rows** per search type. Each time you call the API in this workflow, you’re using up a portion of that limit.

I recommend keeping the row limit to 1-5K. This will give you a reasonable amount of data while still letting you perform multiple powerful analyses per day.

Claude Code reads, runs, and iterates on this script for you. It already knows the GSC API, so you don't need to read a line of documentation.

Do the same for GA4 by pasting in this fetcher:

`from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
RunReportRequest, DateRange, Metric, Dimension
)
def get_ga4_client():
credentials = service_account.Credentials.from_service_account_file(
'service-account-key.json',
scopes=['https://www.googleapis.com/auth/analytics.readonly']
)
return BetaAnalyticsDataClient(credentials=credentials)
def fetch_traffic_by_channel(client, property_id, start_date, end_date):
request = RunReportRequest(
property=f"properties/{property_id}",
date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
dimensions=[Dimension(name="sessionDefaultChannelGroup")],
metrics=[
Metric(name="sessions"),
Metric(name="totalUsers"),
Metric(name="bounceRate"),
]
)
return client.run_report(request)`

Shout out to Will Scott for the code we used here, which we took from [this Search Engine Land article](https://searchengineland.com/claude-code-seo-work-470668).

Ask Claude Code to wrap the fetchers in a single “run\_fetch.py” orchestrator. This will allow you to easily update the data for any dashboards or reports you create.

### Run the scripts and verify your data

Ask Claude Code to run the fetcher scripts. Then perform a quick sanity check on the data by asking Claude Code to:

*Read the GSC and GA4 data in the data/ directory. Summarize what we have: how many queries, how many pages, what date range, and what metrics are available.*

![Claude Code summarizes imported GSC and GA4 data, showing query counts, landing pages, metrics, and SEO dataset coverage](https://static.semrush.com/blog/uploads/media/9f/10/9f10cbf70b92a3ef3dfce723e631299c/dc73fd5a12c56d795e205173d6a842d0/image.png)

If Claude Code can read and summarize the data, you’re set. If you run into issues, quote the inconsistencies and ask Claude to explain and/or troubleshoot the discrepancies.

We'll cover how to verify findings before sharing them with clients in Step 7.

## Step 3: Connect Google Ads (if applicable)

If you run Google Ads to your website, connecting the Google Ads interface to your Claude Code setup allows you to perform some powerful analyses across both paid and organic data.

### What you need

Google Ads uses a different authentication flow than GSC and GA4. Instead of a service account, you need OAuth 2.0 credentials and a developer token, which you can only get if you have a manager account.

To set up the Google Ads API connection:

- **Developer token**: From the Google Ads API Center (“**Tools & Settings**” > “**Setup**” > “**API Center**”). For agency use, describe it as “automated reporting for marketing clients.” Approval may not be instant.
- **OAuth 2.0 client**: Create this in Google Cloud Console. It’s a separate credential from your service account. See the [Google documentation](https://support.google.com/cloud/answer/15549257) for more on the setup.
- **Refresh token**: Generate this through a one-time browser authentication flow

If you have a Manager Account (MCC), for example if you run an agency, one developer token and one refresh token cover all your sub-accounts. You change the customer ID per client.

### Install the dependency

As you did with the Python dependencies for Google Search Console and Analytics, paste the following into Claude Code to install the dependency for Google Ads:

`pip install google-ads`

### Build the fetcher

Here's the code to paste in for the Google Ads fetcher (tell Claude Code to add it to fetchers/):

`from google.ads.googleads.client import GoogleAdsClient

client = GoogleAdsClient.load_from_storage("google-ads.yaml")
ga_service = client.get_service("GoogleAdsService")

query = """
SELECT
search_term_view.search_term,
metrics.impressions,
metrics.clicks,
metrics.cost_micros,
metrics.conversions
FROM search_term_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.impressions DESC
"""

response = ga_service.search(customer_id="1234567890", query=query)`

Like with the first two fetchers, ask Claude Code to wrap this fetcher in the “run\_fetch.py” orchestrator so you can easily request updated data when you need it.

If you’re still getting API access set up or waiting on approval, download 90 days of search terms data as a CSV directly from the Google Ads UI and tell Claude to add it to the data/ads/ folder. You can upgrade to live API connections later, but this lets you start using this setup immediately.

## Step 4: Add Semrush’s competitive intelligence

Google’s APIs tell you what’s happening on *your* site. Semrush tells you what’s happening across the *entire market*. This includes:

- Competitor keywords
- Backlink profiles
- Keyword search volumes
- Keyword difficulty scores
- Traffic estimates

The connection uses MCP (Model Context Protocol), an open standard for connecting AI tools to external data sources. Essentially, this lets Claude Code and Semrush talk to each other and share data. This makes the kinds of reports and analyses you can perform far more powerful.

Here’s how to connect [Semrush MCP](https://www.semrush.com/blog/what-is-mcp-connector/) to Claude Code:

### Check your eligibility

Semrush MCP is available on Semrush One (Starter and Pro+) and SEO Classic (Pro and Guru) plans, with 50,000 API units included each month. SEO Classic Business and Semrush One Advanced can also use Semrush MCP, but you'll need to add an API units package.

Check your plan and remaining API units in the “Subscription info” tab of your profile.

![Semrush subscription dashboard highlighting API units balance and available credits for MCP-powered SEO data access](https://static.semrush.com/blog/uploads/media/da/b8/dab8c5deb9f545b3d9e0e18b1460684c/68e33f685a7c844799e66476c6d34841/image.png)

### Connect Semrush via MCP

To connect the Semrush MCP if you’re using the desktop app, click the “**+**” > “**Connectors**” > “**Manage connectors**” > “**+**” > “**Add custom connector**.”

Name it something like “Semrush MCP” and paste “https://mcp.semrush.com/v1/mcp” into the “Remote MCP Server URL” box:

![Claude custom connector setup for Semrush MCP with server URL entered before adding the integration](https://static.semrush.com/blog/uploads/media/51/f6/51f6a217dc9403683b6f49b21d73133e/97cc5508c6fb99c91c4287ee731e9470/image.png)

To connect Semrush to your Claude Code setup in the terminal, paste in the following command:

`claude mcp add semrush https://mcp.semrush.com/v1/mcp -t http`

You might need to approve the connection.

![Claude Code terminal command adding Semrush MCP server and requesting approval to connect Semrush tools](https://static.semrush.com/blog/uploads/media/e1/a4/e1a40894b5c8839cdea1edfbeb110c42/479f4e5de5107074d41fde260c5dfdc4/image.jpeg)

Once the connection is added, authenticate using the steps below.

![Claude MCP server manager showing Semrush MCP successfully connected and authenticated](https://static.semrush.com/blog/uploads/media/7a/ac/7aac6202250169d640a160282333cf4f/622e4ea278716074685eae44ce1552cc/image.jpeg)

### Authenticate your account

Like you did when you authenticated your Anthropic account at the start, you need to connect your Semrush account. To do this, type “/mcp” into Claude Code, select Semrush from the list, click “**Authenticate**,” and follow the login instructions.

If you're using the desktop app, the authentication process should start automatically. Follow the on-screen instructions.

Semrush data is now accessible in every Claude Code session.

![Claude Code confirms Semrush MCP server added to config and prompts restart to enable live Semrush access](https://static.semrush.com/blog/uploads/media/8b/16/8b16c54cc06c28c9cf64336418295b7a/80556607fa1caaeab18401f3a87c5c1a/image.png)

### Test it

Test your Semrush connection is working by pasting in a prompt like:

*Show me the top 10 organic keywords for [yourdomain.com] in the US. Include position, volume, keyword difficulty, and the ranking URL.*

If you see a data table, the connection is working.

### What’s available through Semrush MCP

You can access the following data through the Semrush MCP:

- **Analytics API**: Organic/paid keywords, keyword research (volume, KD, SERP features, intent), backlinks (referring domains, anchors, Authority Score), domain comparisons, and competitor analysis
- **Trends API**: Traffic estimates, traffic sources, top pages, audience demographics (requires a Trends API subscription)
- **Projects API (read-only)**: Position Tracking and Site Audit results from your existing Semrush projects

For more on setting this up, check out the [Semrush MCP documentation](https://developer.semrush.com/api/introduction/semrush-mcp/).

## Step 5: Cache your Semrush data for the dashboard

Before we build the dashboard, we need to save Semrush data locally alongside the Google data. MCP pulls data live, which is great for ad hoc analysis. But a dashboard needs a stable dataset to render from.

Ask Claude Code to:

*Run the following Semrush reports for [yourdomain.com] and save each as a JSON file in data/semrush/:*

*1. Top 200 organic keywords (US) with position, volume, KD, URL, and traffic estimate into organic\_keywords.json*

*2. Top 50 referring domains by Authority Score into referring\_domains.json*

*3. Top 20 organic pages by estimated traffic with keyword count into top\_pages.json*

*4. Domain overview (organic traffic, keyword count, Authority Score) for [yourdomain.com] plus competitors [list 3-5 competitor domains] into competitive\_overview.json*

Claude Code will make multiple Semrush MCP calls and save structured JSON files. Now you have all four data sources—GSC, GA4, Ads (if applicable), and Semrush—sitting in your data/ directory, ready to power a dashboard.

### Add AI visibility data to go a step further

Semrush's [AI Visibility Toolkit](https://www.semrush.com/ai-seo/overview/) isn't currently available via the MCP, but you can still add data from it to your Claude Code setup. Cross-checking your SEO metrics against your AI performance gives you a more complete picture of your overall online visibility.

Export whatever data you need from within Semrush and add it to your Claude Code setup, asking Claude to include it in /data/semrush as a new CSV file.

For example, you could export your top performing prompts and your topic opportunities from the “**Visibility Overview**” tool.

![Semrush Topics and Sources dashboard with top-performing prompts export option for AI visibility research](https://static.semrush.com/blog/uploads/media/61/aa/61aa310ed18b47da4389f230d4eec77d/da057cde2221cb6f3011dccd6686a6c6/image.png)

When you're performing analyses or building your dashboard, ask Claude to identify easy-win prompt optimization opportunities that align with your keyword opportunities. You'll improve your SEO and your [AI search optimization](https://www.semrush.com/blog/ai-search-optimization/) at the same time.

## Step 6: Build the dashboard

Build an interactive dashboard based on the data and connections you've set up. Instead of a terminal output you read once and forget, you're getting a live dashboard that visualizes all your data sources in one place. You can open it in a browser, share it with your team, and update the data monthly.

### What the dashboard will include

You’ll see five panels in the dashboard, each pulling from different data sources:

1. **Organic Overview** (GSC + Semrush): Total impressions, clicks, and top queries from GSC alongside organic keyword count, traffic estimate, and Authority Score from Semrush. Use this to baseline your overall organic performance against competitors.
2. **Striking Distance Keywords** (GSC + Semrush): Keywords at positions 5–20 from GSC, enriched with KD and volume from Semrush, all sortable and filterable. These are keywords you may want to start optimizing for first to see the quickest results.
3. **Competitive Gap Map** (Semrush): Keyword overlap visualization showing your domain versus your top competitors. Highlights clusters where your domain has no presence—i.e., clear competitive gaps.
4. **Content Performance** (GA4 + Semrush): Top pages by sessions from GA4, enriched with ranking keyword count and referring domains from Semrush. This flags potentially thin content that only ranks for a few terms.
5. **Backlink Intelligence** (Semrush): Top referring domains, Authority Score distribution, and competitor comparison. Use this to inform your [link building](https://www.semrush.com/blog/link-building/) efforts.

![Custom SEO dashboard for Traffic Think Tank showing GSC, Semrush, and competitor traffic comparison metrics](https://static.semrush.com/blog/uploads/media/3e/2e/3e2e0b1e9a37b7fe5f81306f7935ac50/d5ab349ef5a1ce46707c1be5d26bc3c2/image.png)

(I asked Claude to add some extra functionality like a light/dark mode selector, a sixth tab for paid versus organic performance, and a date selector.)

Claude Code can build the entire dashboard as a single-page web app. Here’s the prompt to build yours:

*Build a dashboard web app in dashboard/index.html that reads JSON data from our data/ directory. Use Tailwind CSS for styling and Chart.js for visualizations. The dashboard should have 5 panels:*

*1. ORGANIC OVERVIEW: Show total GSC impressions, clicks, and average position for the period. Next to it, show Semrush’s organic keyword count, estimated traffic, and Authority Score from competitive\_overview.json. Include a comparison bar chart of estimated organic traffic for [yourdomain.com] vs. competitors.*

*2. STRIKING DISTANCE KEYWORDS: A sortable table of keywords from GSC where position is 5-20, enriched with volume and KD from Semrush organic\_keywords.json. Color-code KD (green <30, yellow 30–50, red >50). Add a filter for KD range.*

*3. COMPETITIVE GAP MAP: A bar chart showing keyword count by topic cluster where competitors rank but [yourdomain.com] doesn’t. Use the cached competitive data. Show top 10 gap clusters by total volume.*

*4. CONTENT PERFORMANCE: A table of top blog pages from GA4, showing sessions, bounce rate, plus Semrush’s ranking keyword count and referring domains per page. Highlight pages with <5 ranking keywords as “thin content.”*

*5. BACKLINK INTELLIGENCE: A horizontal bar chart of top 20 referring domains by Authority Score. Show total referring domains count and comparison to competitors. Make it responsive. Use a dark sidebar with navigation. Include a header showing “[Your Brand] — SEO Dashboard” and the data freshness date. The dashboard should load data from relative paths to the data/ directory.*

Claude Code will generate the complete HTML file with embedded JavaScript. It reads your actual JSON data files and builds charts from them.

### Launch and iterate

Type this into Claude Code to launch your dashboard locally:

`cd dashboard
python3 -m http.server 8080

From here, you can iterate on the layout and specific functionalities you need. Just ask Claude Code to refine the dashboard to your needs with prompts like:

- *“Add a date picker to the header that filters the GSC data by date range.”*
- *“Add a sixth panel that shows the paid-organic overlap data from data/ads/.”*
- *“Make the striking distance table exportable as CSV.”*
- *“Add sparklines showing position trends for each keyword.”*
- *“Add month-over-month comparisons and other long-term tracking views.”*

Claude Code edits the existing dashboard file. Refresh your browser to see the result immediately.

You can ask Claude Code to make almost any change to the dashboard. If something doesn't work, keep iterating or simply say "revert to the previous version."

Treat the dashboard as yours to shape.

### Share the dashboard

You can share the dashboard with colleagues or clients by deploying the single HTML file to a hosting service like [Vercel](https://vercel.com/docs/deployments). You can ask Claude Code for help here, or consult a developer.

### Regularly update the data

Update the data in your dashboard regularly and/or each time you want to build a report.

Do this by entering this prompt into Claude Code at the time you want to update the data (don’t include “ads” if you don’t have that data source linked yet):

`python3 run_fetch.py --sources gsc,ga4,ads,semrush`

You can ask Claude Code to set up a scheduled task to refresh the data automatically (your computer will need to be on and awake). Anthropic also introduced [Claude Code Routines](https://code.claude.com/docs/en/routines), which run on Anthropic's cloud infrastructure and don't require your local machine to be on. Routines are currently in research preview.

Alternatively, you could set up automatic refreshes yourself using cron jobs if you’re more technical. But a quick manual refresh will work for most people at this stage.

## Step 7: Download your first report

You can use Claude Code to generate client-ready reports based on the data and connections you’ve set up.

Either ask Claude for reports based on specific data or actions you want to highlight, or use this prompt to instantly generate a report that covers some of the most important areas:

*Generate a full SEO opportunity report for [yourdomain.com] as a Word doc. Use all data sources available: GSC (queries.csv), GA4 (traffic\_by\_channel.csv), Semrush keywords/pages/domains/competitive overview. Structure it as follows:*

***1. Executive Summary:*** *3-5 bullet "state of the site" findings backed by numbers*

***2. Quick Wins (next 30 days):*** *GSC keywords pos 5-20 enriched with Semrush KD/volume. For each, estimate the monthly click uplift if it moved to position 3 (use GSC average position and CTR data to estimate this). Prioritize by (uplift multiplied by the inverse of KD).*

***3. Content Gap Analysis:*** *Topic clusters from Semrush keywords vs actual GSC clicks. Which clusters have high search volume but low click capture? What content is missing or thin?*

***4. Top Pages Audit:*** *Cross-reference Semrush top pages with GSC. Flag pages with high Semrush-estimated traffic but low GSC clicks (potential ranking drops or cannibalization). Flag thin content pages (< 5 ranking keywords).*

***5. Competitive Benchmarking:*** *Compare [yourdomain.com] vs all 4 competitors across keywords, traffic, and domain metrics. Where is the biggest gap and what type of content closes it?*

***6. Backlink Opportunities:*** *Given the referring domain profile (Authority Scores, sources), what's the link acquisition strategy? Where are competitors getting links that [yourdomain.com] isn't?*

***7. Prioritized Action Plan:*** *A scored table of all recommended actions: effort (Low/Med/High), impact (Low/Med/High), and suggested owner (writer / developer / outreach).*

Claude Code can generate a bunch of different file types to suit your needs, including:

- PDFs
- Word docs
- CSVs
- PowerPoints
- Plain text

But you might have to install extra dependencies within Claude Code for it to work. I’ve found it’s best to first ask Claude Code what it needs to generate the specific format you require.

When generating a docx, Claude Code asked for several permissions and folder accesses I didn't expect. Stopping the process and asking "what will you need to generate a docx file?" gave me two clear options. I chose one, and the report generated cleanly.

![Claude Code generates SEO report document after analyzing GSC, GA4, and Semrush data with Python docx setup](https://static.semrush.com/blog/uploads/media/a0/fe/a0feff6da64ce1476ec54f9fa8d3f636/22048cddc55b6c510c0a285efc289c82/image.png)

Iterating with Claude Code is normal. Expect to ask follow-ups to land where you want.

### Verify the data

The dashboard and reports Claude Code can generate are impressive, but they’re not client-ready without you first checking everything over. LLMs can occasionally misread data or generate a chart that doesn’t match the underlying numbers.

Claude can also confidently combine numbers in ways that are mathematically correct but analytically wrong. This could be misattributing channel data, for example, which could impact decisions you or your clients make.

Before you share the dashboard or act on anything, make sure you:

- Cross-reference dashboard numbers against the raw JSON files (and even the raw data within the tools themselves)
- If a finding looks too dramatic, open Claude Code and ask it to show you the raw data behind it

## Step 8: Perform cross-source analyses

Running cross-source analyses is where you can leverage the connection between first-party data (from GSC, GA4, and Google Ads) and Semrush competitive data. This lets you interact with the data at any time and for pretty much any purpose you can imagine.

The conversational nature of working with an LLM allows for deep, iterative conversations. You ask Claude Code to perform an analysis, it performs it, you push back or ask for further clarification, and you get more insights than static numbers can give you.

Below are my five favorite ways to interact with Claude Code for SEO. For each analysis, I’ll tell you the sources it pulls from, why the analysis is useful, and a prompt you can copy and paste to perform the analysis yourself, right now.

### Analysis #1: Prioritize GSC queries with competitive difficulty

**First-party source**: GSC (real impressions and positions)

**Third-party source**: Semrush (keyword difficulty)

**Prompt**: *Read the GSC data in data/gsc/. Find queries for [yourdomain.com] where position is between 5 and 15 with more than 500 impressions. For each, pull keyword difficulty and search volume from Semrush. Show only queries where KD is below 35. Sort by impressions descending. These are [yourdomain.com’s] easiest wins.*

**Why this is useful**: GSC tells you which queries are real (actual impressions from actual searchers). Semrush tells you how hard each one is to rank for. Together, these give you a prioritized optimization list neither source can produce on its own.

### Analysis #2: Competitive keyword gap

**First-party source**: GSC (what TTT actually ranks for)

**Third-party source**: Semrush (competitor keyword data)

**Prompt**: *Read [yourdomain.com’s] GSC query data. Then pull the top organic keywords for [competitor 1] and [competitor 2] from Semrush in the US. Find keywords where either [competitor 1] or [competitor 2] rank in the top 10 but [yourdomain.com] has no GSC impressions at all—meaning we’re completely invisible. Filter to volume above 300. Group results by topic cluster and rank clusters by total volume.*

**Why this is useful**: Using GSC data instead of Semrush data means we’re working with ground truth, not estimates. If a keyword has zero impressions in GSC, our website truly isn’t showing up. But combining this with Semrush’s data for competitors means we can still perform an effective keyword gap analysis.

**Follow-up prompt**: *For the top 3 gap clusters by volume, show all keywords in each cluster with volume, KD, and who ranks #1. Then check—does [yourdomain.com] have any existing blog content that could be expanded to target these?*

The follow-up prompt takes it from keyword gap analysis to content optimization planning.

### Analysis #3: Content performance audit with authority data

**First-party source**: GA4 (sessions, bounce rate, engagement)

**Third-party source**: Semrush (ranking keywords, backlink profile per page)

**Prompt**: *Read the GA4 top pages data in data/ga4/. For [yourdomain.com’s] top 20 blog pages by sessions, pull from Semrush: number of ranking keywords, estimated organic traffic, and number of referring domains for each URL. Flag pages where the ratio of sessions to ranking keywords is low—these are pages with traffic but thin topical coverage that could be expanded.*

**Why this is useful**: GA4 shows you which pages actually drive engagement. Semrush shows the competitive strength of each page (using keyword count and backlink data). A page with high sessions but only three ranking keywords and few backlinks is fragile—one algorithm update could tank it. These are pages you should prioritize optimizing for more related keywords and building backlinks to.

### Analysis #4: High-impression, low-CTR title tag opportunities

**First-party source**: GSC (impressions, CTR, positions)

**Third-party source**: Semrush (SERP analysis, competitor title tags)

**Prompt**: *From the GSC data, find [yourdomain.com’s] pages with more than 2,000 impressions but CTR below 2%. For each, pull the Semrush keyword data to find the primary keyword driving impressions, and use web search to see what the SERP results look like for that keyword. Generate 3 improved title tag options for each page based on what’s working for competitors.*

**Why this is useful**: High impressions but low CTR means Google thinks your page is relevant, but searchers aren’t clicking. This is usually a [title tag](https://www.semrush.com/blog/title-tag/) or [meta description](https://www.semrush.com/blog/meta-description/) problem. Your GSC data identifies the pages, while Semrush shows which pages are winning for relevant keywords. Claude then uses web search to find the corresponding titles. Then, Claude will give you recommendations based on all of these data sources.

### Analysis #5: Paid vs. organic overlap (for sites running Google Ads)

***Note****: This analysis requires Google Ads data, which isn’t applicable to Traffic Think Tank. But for businesses that* ***do*** *run ads, this is one of the highest-value analyses in the entire setup.*

**First-party source**: Google Ads (search terms, spend, CPC)

**Third-party source**: Semrush (organic rankings)

**Prompt**: *Read the Google Ads search terms data in data/ads/. Cross-reference with Semrush organic keyword data for [yourdomain.com]. Find keywords where we’re paying for clicks but already rank in the top 3 organically. Show keyword, organic position, ad spend, CPC, and monthly paid clicks. Calculate total potential savings if we paused ads on terms where we rank in the top 3.*

**Why this is useful**: Your Ads data shows what you’re spending, and Semrush confirms where you already rank. The overlap is wasted budget. This kind of analysis can lead to thousands of dollars in monthly savings for clients—money that can be reallocated to keywords where you (or they) have no organic presence.

## Start using Claude Code for SEO today

Here’s how to use this Claude Code setup in your regular SEO workflows:

1. **Once a month, open the dashboard**. Ask Claude to refresh the data, then check the five panels. What has changed since last month?
2. **Regularly ask cross-source questions**. Open Claude Code and ask questions about anything that looks interesting—the dashboard shows you *what*, Claude Code tells you *why*.
3. **Take action**. Update title tags for low-CTR pages. Plan content for gap clusters. Brief your link building team on referring domain targets.

This process doesn’t replace:

- **The Semrush UI**: You still need to use Semrush for configuring Position Tracking, Site Audit, keyword lists, or client dashboards. MCP is read-only for project data.
- **Strategic judgment**: The dashboard and Claude Code surface insights fast. Whether you should act on them—by investing in content, shifting ad budget, consolidating pages—is your call.
- **Ongoing monitoring**: For automated alerts and daily tracking, you still want the Semrush platform. This setup is for monthly analysis and on-demand deep dives.

To start using the Semrush MCP within Claude Code today, sign up for a Semrush One subscription.
