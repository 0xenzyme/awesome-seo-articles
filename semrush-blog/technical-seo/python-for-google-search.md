---
title: "How to Scrape & Analyze Google Search Results with Python"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "python-for-google-search"
url: "https://www.semrush.com/blog/python-for-google-search/"
canonical: "https://www.semrush.com/blog/python-for-google-search/"
author: "Yannick Weiler"
published: "2023-09-06T11:06:00+00:00"
updated: "2023-09-06T11:06:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2023_aging"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T18:45:35+00:00"
status_code: 200
html_hash: "c55cfc74a0c127fc273c5469747eda679fd91f200c7a1c1848f5f1a768c41180"
clean_word_count: 3095
clean_char_count: 21274
---
# How to Scrape & Analyze Google Search Results with Python

Ever spent hours analyzing Google search results and ended up more frustrated and confused than before?

Python hasn’t.

In this article, we’ll explore why Python is an ideal choice for Google search analysis and how it simplifies and automates an otherwise time-consuming task.

We’ll also perform an SEO analysis in Python from start to finish. And provide code for you to copy and use.

But first, some background.

## Why to Use Python for Google Search and Analysis

Python is known as a versatile, easy-to-learn programming language. And it really shines at working with Google search data.

Why?

Here are a few key reasons that point to Python as a top choice for scraping and analyzing Google search results:

### Python Is Easy to Read and Use

Python is designed with simplicity in mind. So you can focus on analyzing Google search results instead of getting tangled up in complicated coding syntax.

It follows an easy to grasp syntax and style. Which allows developers to write fewer lines of code compared to other languages.

![an infographic showing the same example using Python, Java and C++](https://static.semrush.com/blog/uploads/media/d1/ac/d1ac13a1dfff276ac15672efc3723b49/A4-zKy98QqZM1vSZTjfIEjvXsX91OGrNLZjjlVCW8vLXuz3ZNTPyBLQas1UDpTffNAFzmmwCof4Xtv7VSctSElkZ6FEfxIP1lkrLiya9MgGRS4OxYk2DSHw2DwWfgtHKZsibFLSy2thCSQtUbzU3iGQ.png)

### Python Has Well-Equipped Libraries

A Python library is a reusable chunk of code created by developers that you can reference in your scripts to provide extra functionality without having to write it from scratch.

And Python now has a wealth of libraries like:

- Googlesearch, Requests, and Beautiful Soup for web scraping
- Pandas and Matplotlib for data analysis

These libraries are powerful tools that make scraping and analyzing data from Google searches efficient.

### Python Offers Support from a Large Community and ChatGPT

You’ll be well-supported in any Python project you undertake, including Google search analysis.

Because Python's popularity has led to a large, active community of developers. And a wealth of tutorials, forums, guides, and third-party tools.

And when you can’t find pre-existing Python code for your search analysis project, chances are that ChatGPT will be able to help.

When using ChatGPT, we recommend prompting it to:

- Act as a Python expert and
- Help with a problem

Then, state:

- The goal (“to query Google”) and
- The desired output (“the simplest version of a query”)

![an example of Python-based query in ChatGPT](https://static.semrush.com/blog/uploads/media/fc/23/fc23ff8ab1a70fd63f8deb33bcc95a55/c10F3m_k-Ysy7yCqiS1BSva_AKLBPUqE_3rW05oyVP1DO5IpN_U_j4NOL1ZlxZUObrFB5lbQnVpBzvfSdZndDthlUIiHlLHCYLkmL-wnaTxfMNWMOwi6OVM8e0O0qmMT4_MSQt24UTajD5H0ICPyO4A.jpeg)

## Setting Up Your Python Environment

You'll need to set up your Python environment before you can scrape and analyze Google search results using Python.

There are many ways to get Python up and running. But one of the quickest ways to start analyzing Google search engine results pages ([SERPs](https://www.semrush.com/blog/serp/)) with Python is Google’s own notebook environment: [Google Colab](https://research.google.com/colaboratory/).

Here’s how easy it is to get started with Google Colab:

1. **Access Google Colab**: Open your web browser and go to [Google Colab](https://colab.research.google.com/). If you have a Google account, sign in. If not, create a new account.

2. **Create a new notebook**: In Google Colab, click on “**File**” > “**New** **Notebook**” to create a new Python notebook.

![open new notebook in Google Colab](https://static.semrush.com/blog/uploads/media/34/6b/346b582b12c5b433c6f2f4908842cf45/cCD1IgUkvCRcPuAkryyhZxiXGJk9plBnkFCICU6oYlx8C8i7gylDGXodaskQXXuVX0x88EuIMUP6kyTA3x2T6pu3NzotZ7BQGnfCdmRs2deMp1tfECdTAg3_j5aZB0ytz_YSxPnm0l1tctdvQYTbfNo.jpeg)

3. **Check installation**: To ensure that Python is working correctly, run a simple test by entering and executing the code below. And Google Colab will show you the Python version that’s currently installed:

`import sys
sys.version`

Wasn’t that simple?

There’s just one more step before you can perform an actual Google search.

### Importing the Python Googlesearch Module

Use the googlesearch-python package to scrape and analyze Google search results with Python. It provides a convenient way to perform Google searches programmatically.

Just run the following code in a code cell to access this Python Google search module:

`from googlesearch import search
print("Googlesearch package installed successfully!")`

One benefit of using Google Colab is that the googlesearch-python package is pre-installed. So, no need to do that first.

It’s ready to go once you see the message "Googlesearch package installed successfully!"

Now, we'll explore how to use the module to perform Google searches. And extract valuable information from the search results.

## How to Perform a Google Search with Python

To perform a Google search, write and run a few lines of code that specify your search query, how many results to display, and a few other details (more on this in the next section).

`# set query to search for in Google
query = "long winter coat"
results = search(query, tld="com", lang="en", stop=3, pause=2)
for result in results:
print(result)`

You’ll then see the top three Google search results for the query "long winter coat."

Here’s what it looks like in the notebook:

![top three Google search results for the query "long winter coat" in the notebook](https://static.semrush.com/blog/uploads/media/38/08/3808b38f27c04ea48c00182df9d7d1d1/YAg6VcKS-CT7fQEvO_u5ZaBWeT-55d4sbThjjPBwJhgOBCOJkZkmhFp3foJ2b3l_mhldnGrnE9aD2UjF5TmR_Fua8DVAiGqoEZqV2C5q5yp51-io4x-SiynlXWzPW39R9Tn2oqm8LbvQT89rKQ_tJec.jpeg)

To verify that the results are accurate, you can use [Keyword Overview](https://www.semrush.com/analytics/keywordoverview/).

Open the tool, enter "long winter coat" into the search box, and make sure the location is set to "U.S." And click "**Search**."

![search for "long winter coat" in the US in Keyword Overview tool](https://static.semrush.com/blog/uploads/media/57/25/5725d92787ce31b75fc566846c33617e/1WGcboOWaekF5-K8qL-n2sUXrpGjsmhNVn6cO_lX7WU-ayM19yLnDM5TK59ug7oGDuUfgwaM-d9_U6eBY9cHhUtfBu7vlD-BtENUBsM2MEYpj6bva6I5Q-RHTzuby5ar8iKHfM4BUyIjXW8Tyjb6ncQ.jpeg)

Scroll down to the "SERP Analysis" table. And you should see the same (or very similar) URLs in the top three spots.

!["SERP Analysis" table](https://static.semrush.com/blog/uploads/media/bb/0b/bb0b09961a427089f7380b0776412108/EHLMdUeojfxy9jyVfpnE3MJaIQ9gFIIwaBBvpGgQDbGBlLEQLXCbHqFS2eMt5nG0dz02mrOLjlABOYqqDyVuUT6TDs33fR3CYzBML175oVkuHQUSFHrR9ajtRA1P3DgGUMFsW3q6U97FNTKAYJrQQdI.jpeg)

Keyword Overview also shows you a lot of helpful data that Python has no access to. Like monthly search volume (globally and in your chosen location), [Keyword Difficulty](https://www.semrush.com/blog/keyword-difficulty/) (a score that indicates how difficult it is to rank in the top 10 results for a given term), [search intent](https://www.semrush.com/blog/search-intent/) (the reason behind a user’s query), and much more.

### Understanding Your Google Search with Python

Let's go through the code we just ran. So you can understand what each part means and how to make adjustments for your needs.

We'll go over each part highlighted in the image below:

![an image of the code ran above in Keyword Overview](https://static.semrush.com/blog/uploads/media/fd/e0/fde051e10b155f662b0bcccf2ed7cc79/XbHiu1gIhUYp4RkdKH1fEVgSxu68Jrt09aNRleodT2AEh-u2XPJVlGRW36ZCNFtkYzvHhlQz2g9LXPzE-UBhh98A1zoP3pemz4Fow-f3RnuMC8lzyOu7gZyIb9-Cm2coKnokCRRA8h3ukuaoPoPpTbA.jpeg)

1. **Query variable**: The query variable stores the search query you want to execute on Google
2. **Search function**: The search function provides various parametersthat allow you to customize your search and retrieve specific results:
   1. **Query**: Tells the search function what phrase or word to search for. This is the only required parameter, so the search function will return an error without it. This is the only required parameter; all following ones are optional.
   2. **Tld (short for top-level domain)**: Lets you determine which version of Google’s website you want to execute a search in. Setting this to "com" will search google.com; setting it to "fr" will search google.fr.
   3. **Lang**: Allows you to specify the language of the search results. And accepts a two-letter language code (e.g., "en" for English).
   4. **Stop**: Sets the number of the search results for the search function. We’ve limited our search to the top three results, but you might want to set the value to “10.”
   5. **Pause**: Specifies the time delay (in seconds) between consecutive requests sent to Google. Setting an appropriate pause value (we recommend at least 10) can help avoid being blocked by Google for sending too many requests too quickly.
3. **For loop sequence**: This line of code tells the loop to iterate through each search result in the "results" collection one by one, assigning each search result URL to the variable "result"
4. **For loop action**: This code block follows the for loop sequence (it’s indented) and contains the actions to be performed on each search result URL. In this case, they’re printed into the output area in Google Colab.

## How to Analyze Google Search Results with Python

Once you’ve scraped Google search results using Python, you can use Python to analyze the data to extract valuable insights.

For example, you can determine which keywords’ SERPs are similar enough to be targeted with a single page. Meaning Python is doing the heavy lifting involved in [keyword clustering](https://www.semrush.com/blog/keyword-clustering/).

Let’s stick to our query "long winter coat" as a starting point. Plugging that into [Keyword Overview](https://www.semrush.com/analytics/keywordoverview/) reveals over 3,000 keyword variations.

!["Keyword Variations" table for "long winter coat" query shows 3.0K results](https://static.semrush.com/blog/uploads/media/53/cf/53cf5236d4706764507281134fd5f353/_N1-4VWrqHFpDkMyWkhBAp9kNXCRtjMoUPC4Kq5UX0AsspcnQJhSVM0tNtJsII44CJrbTNWoWklEPh1sEX6ezgNGIJWAm1SVdPxhkGQjb6BNS3ryFHmB-sq-BmOTikB6GPw27jM-nTBar9VCRpAZ_8A.jpeg)

For the sake of simplicity, we’ll stick to the five keywords visible above. And have Python analyze and cluster them by creating and executing this code in a new code cell in our Google Colab notebook:

`import pandas as pd
main_query = "long winter coat"
secondary_queries = ["long winter coat women", "womens long winter coats", "long winter coats for women", "long winter coats"]
main_results = search(main_query, tld="com", lang="en", stop=3, pause=2)
main_urls = set(main_results)
url_percentages = {}
for secondary_query in secondary_queries:
 secondary_results = search(secondary_query, tld="com", lang="en", stop=3, pause=2)
 secondary_urls = set(secondary_results)
 percentage = (len(main_urls.intersection(secondary_urls)) / len(main_urls)) * 100
 url_percentages[secondary_query] = percentage
df_url_percentages = pd.DataFrame(url_percentages.items(), columns=['Secondary Query', 'Percentage'])
df_url_percentages = df_url_percentages.sort_values(by='Percentage', ascending=False)
df_url_percentages`

With 14 lines of code and a dozen or so seconds of waiting for it to execute, we can now see that the top three results are the same for these queries:

- “long winter coat”
- “long winter coat women”
- “womens long winter coats”
- “long winter coats for women”
- “long winter coats”

So, those queries can be targeted with the same page.

Also, you shouldn’t try to rank for “long winter coat” or “long winter coats” with a page offering coats for men.

### Understanding Your Google Search Analysis with Python

Once again, let’s go through the code we’ve just executed. It’s a little more complex this time, but the insights we’ve just generated are much more useful, too.

![an image of the code ran above in Keyword Overview](https://static.semrush.com/blog/uploads/media/38/39/3839b6191db376612a7677ce4c00e70c/3xp2rv7yIcaT3ZsrUVeY44_n5FLaEisc5LwZyJK7rHaMbsWiwu6A-WBSYri1e11KFVqDQwwH6sGhVQiO_vG2HtaVB16EZmQu3GTUUKnmQbXfxredBLgf4-fJ-t5M_CwI2-jAlpUHVDn7VMDXtBifIlE.jpeg)

1. **Import pandas as pd**: Imports the Pandas library and makes it callable by the abbreviation "pd." We’ll use the Pandas library to create a "DataFrame," which is essentially a table inside the Python output area.

2. **Main\_query = "python google search"**: Defines the main query to search for on Google

3. **Secondary\_queries = ["google search python", "google search api python", "python search google", "how to scrape google search results python"]**: Creates a list of queries to be executed on Google. You can paste many more queries and have Python cluster hundreds of them for you.

4. **Main\_results = search(main\_query, tld="com", lang="en", stop=3, pause=2**): Executes the main query and stores the search results in main\_results. We limited the number of results to three (stop=3), because the top three URLs in Google’s search results often do the best job in terms of satisfying users’ search intent.

5. **Main\_urls = set(main\_results)**: Converts the search results of the main query into a set of URLs and stores them in main\_urls

6. **Url\_percentages = {}**: Initializes an empty dictionary (a list with fixed value pairs) to store the URL percentages for each query

![an image of the code described in this section](https://static.semrush.com/blog/uploads/media/49/52/4952158efcef99aee76e6e62fa38350f/c8WeZkZlzHSls1SzjVimRpOJ1eJ3jCNl7buO8LsWh043kOgHVxe2zyoK_7EFUKW6jnvlHEDQr4uzhj5R1YHd5TirF56K_Ji-aMllGATqPp103CBZGwwqTvJXUWfnHiXHKpGVWdvVCrh8hNdbywGIekk.jpeg)

7. **For secondary\_query in secondary\_queries :**: Starts a loop that iterates over each secondary query in the secondary queries list

8. **Secondary\_results = search(secondary\_query, tld="com", lang="en", stop=3, pause=2)**: Executes the current secondary query and stores the search results in secondary\_results. We limited the number of results to three (stop=3) for the same reason we mentioned earlier.

9. **Secondary\_urls = set(secondary\_results)**: Converts the search results of the current secondary query into a set of URLs and stores them in secondary\_urls

10. **Percentage = (len(main\_urls.intersection(urls)) / len(main\_urls)) \* 100**: Calculates the percentage of URLs that appear in both the main query results and the current secondary query results. The result is stored in the variable percentage.

11. **Url\_percentages[secondary\_query] = percentage**: Stores the computed URL percentage in the url\_percentages dictionary, with the current secondary query as the key

![an image of the code described in this section](https://static.semrush.com/blog/uploads/media/b1/a4/b1a44ce5f23b35a3db9d01c6b9b09f9a/7Hkr9yZbVcp55jKC1Q3z2-QdQPNhXw7qUnn8FgjM48nZ417XPIx3rLUNdjEf066Ay_CyBZjbrgAq2RRY5rqOldZXeR6RgZfQmgA0_JK5w7ECaw6sq1uOjgsi19rHzs_6xSlyfv3XVuz_sTiedPosFwE.jpeg)

12. **Df\_url\_percentages = pd.DataFrame(url\_percentages.items(), columns=['Secondary Query', 'Percentage'])**: Creates a Pandas DataFrame that holds the secondary queries in the first column and their overlap with the main query in the second column. The columns argument (which has three labels for the table added) is used to specify the column names for the DataFrame.

13. **Df\_url\_percentages = df\_url\_percentages.sort\_values(by='Percentage', ascending=False)**: Sorts the DataFrame df\_url\_percentages based on the values in the Percentage column. By setting ascending=False, the dataframe is sorted from the highest to the lowest values.

14. **Df\_url\_percentages**: Shows the sorted DataFrame in the Google Colab output area. In most other Python environments you would have to use the print() function to display the DataFrame. But not in Google Colab— plus the table is interactive.

In short, this code performs a series of Google searches and shows the overlap between the top three search results for each secondary query and the main query.

The larger the overlap is, the more likely you can rank for a primary and secondary query with the same page.

### Visualizing Your Google Search Analysis Results

Visualizing the results of a Google search analysis can provide a clear and intuitive representation of the data. And enable you to easily interpret and communicate the findings.

Visualization comes in handy when we apply our code for keyword clustering to no more than 20 or 30 queries.

***Note**: For larger query samples, the query labels in the bar chart we’re about to create will bleed into each other. Which makes the DataFrame created above more useful for clustering.*

You can visualize your URL percentages as a bar chart using Python and Matplotlib with this code:

`import matplotlib.pyplot as plt
sorted_percentages = sorted(url_percentages.items(), key=lambda x: x[1], reverse=True)
sorted_queries, sorted_percentages = zip(*sorted_percentages)
plt.bar(sorted_queries, sorted_percentages)
plt.xlabel("Queries")
plt.ylabel("URL Percentage")
plt.title("URL Percentage in Search Results")
plt.xticks(rotation=45)
plt.ylim(0, 100)
plt.tight_layout()
plt.show()`

We’ll quickly run through the code again:

![an image of the code described in this section](https://static.semrush.com/blog/uploads/media/e3/7f/e37fecf945c029e1a7f4367e9654a230/6_4MxqUg-V_3rR4r_hrfkohK_ncVw1tPeup5NZBFaiK12RacYNscdYnEwUuADED4nsde20KUIb5gC-5_JJaPiOG-jj66uE7qXF7Iwi74uyjIvhS62UH8WpXKGXgoUCPvjsX9nK-5yVhxQkXXJF4cpjM.jpeg)

1. **Sorted\_percentages = sorted(url\_percentages.items(), key=lambda x: x[1], reverse=True)**: This specifies that the URL percentages dictionary (url\_percentages) is sorted by value in descending order using the sorted() function. It creates a list of tuples (value pairs) sorted by the URL percentages.

2. **Sorted\_queries, sorted\_percentages = zip(\*sorted\_percentages)**: This indicates the sorted list of tuples is unpacked into two separate lists (sorted\_queries and sorted\_percentages) using the zip() function and the \* operator. The \* operator in Python is a tool that lets you break down collections into their individual items

![an image of the code section described above](https://static.semrush.com/blog/uploads/media/6c/3d/6c3d1b2833aa3a5cb2fa73dd6a63ce34/CQMUkBEqw63321uG7cx0oJakkHP-gmbWg-pkwff-99ZIqNH2eCWmgp-e6jA6x_AOPJgiueQx0UARUpK99dOd_c3gj-SXTmzB_SnyE_p5fvu9wbiPTHWPR5dHXGUO6Nqh6jmVBNGkWMFY0XMf2VFisQk.jpeg)

3. **Plt.bar(sorted\_queries, sorted\_percentages)**: This creates a bar chart using plt.bar() from Matplotlib. The sorted queries are assigned to the x-axis (sorted\_queries). And the corresponding URL percentages are assigned to the y-axis (sorted\_percentages).

4. **Plt.xlabel("Queries")**: This sets the label "Queries" for the x-axis

5. **Plt.ylabel("URL Percentage")**: This sets the label "URL Percentage" for the y-axis

6. **Plt.title("URL Percentage in Search Results")**: This sets the title of the chart to "URL Percentage in Search Results"

7. **Plt.xticks(rotation=45)**: This rotates the x-axis tick labels by 45 degrees using plt.xticks() for better readability

8. **Plt.ylim(0, 100)**: This sets the y-axis limits from 0 to 100 using plt.ylim() to ensure the chart displays the URL percentages appropriately

9. **Plt.tight\_layout()**: This function adjusts the padding and spacing between subplots to improve the chart’s layout

10. **Plt.show()**: This function is used to display the bar chart that visualizes your Google search results analysis

And here’s what the output looks like:

!["URL percentage in search results" graph](https://static.semrush.com/blog/uploads/media/61/a3/61a33ebff934015cec1289cf64244fcf/dr9GBzZNbaND4UyhFLDufZ3q0g7gxEuQ9k3izIVBcop5-PE1SKzBj_c8RlL4OA8ioA7r8XT7k4DifyNO721Hs8O3LoN2tZ6Z0kzjEarGZ1NnRoNNzqXc6Nw3E1uTKU9nU-QXWVg8qWC_9394fXN-El4.jpeg)

## Master Google Search Using Python's Analytical Power

Python offers incredible analytical capabilities that can be harnessed to effectively scrape and analyze Google search results.

We’ve looked at how to cluster keywords, but there are virtually limitless applications for Google search analysis using Python.

But even just to extend the keyword clustering we’ve just conducted, you could:

- Scrape the SERPs for all queries you plan to target with one page and extract all the [featured snippet](https://www.semrush.com/blog/featured-snippet/) text to optimize for them
- Scrape the questions and answers inside the [People also ask](https://www.semrush.com/blog/how-to-maximize-people-also-ask-seo-opportunities-study/) box to adjust your content to show up in there

You’d need something more robust than the Googlesearch module. There are some great SERP application programming interfaces (APIs) out there that provide virtually all the information you find on a Google SERP itself, but you might find it simpler to get started using [Keyword Overview](https://www.semrush.com/analytics/keywordoverview/).

This tool shows you all the SERP features for your target keywords. So you can study them and start optimizing your content.
