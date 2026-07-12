---
title: "Download search queries data using Python"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2011-12-download-search-queries-data-using"
url: "https://developers.google.com/search/blog/2011/12/download-search-queries-data-using"
canonical: "https://developers.google.com/search/blog/2011/12/download-search-queries-data-using"
author: "Jonathan Simon"
published: "2011-12-22T00:00:00+00:00"
updated: "2011-12-22T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2011_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:16:44+00:00"
status_code: 200
html_hash: "35516f277ea86197a36616ee07f436e01be3fc29d327c4fed450bcb6ca25f67f"
clean_word_count: 525
clean_char_count: 3357
---
# Download search queries data using Python

For all the developers who have expressed interest in getting programmatic access to the search
queries data for their sites in Webmaster Tools, we've got some good news. You can now get access
to your search queries data in
[CSV format](https://en.wikipedia.org/wiki/Comma-separated_values)
using a open source Python script from the
[webmaster-tools-downloads](https://code.google.com/p/webmaster-tools-downloads/)
project. Search queries data is not currently available via the Webmaster Tools API, which has
been a common API user request that we're considering for the next API update. For those of you
who need access to search queries data right now, let's look at an example of how the search
queries downloader Python script can be used to download your search queries data and upload it
to a Google Spreadsheet in Google Docs.

## Example usage of the search queries downloader Python script

1. If Python is not already installed on your machine, download and install
   [Python](https://python.org/download/).
2. Download and install the
   [Google Data APIs Python Client Library](https://code.google.com/apis/gdata/articles/python_client_lib).
3. Create a folder and add the
   [`downloader.py`](https://code.google.com/p/webmaster-tools-downloads/source/browse/downloader.py)
   script to the newly created folder.
4. Copy the
   [`example-create-spreadsheet.py`](https://code.google.com/p/webmaster-tools-downloads/source/browse/example-create-spreadsheet.py)
   script to the same folder as `downloader.py` and edit it to replace the example
   values for `website`, `email` and `password` with valid values
   for your Webmaster Tools verified site.
5. Open a Terminal window and run the `example-create-spreadsheet.py` script by entering
   `python example-create-spreadsheet.py` at the terminal window command line.
6. Visit Google Docs to see a new spreadsheet containing your search queries data.

![Top Search Queries data exported to Google Sheets](/static/search/blog/images/import/7cffcac259e99e915fb0abf52d1c9368.png)

If you just want to download your search queries data in a .csv file without uploading the data to
a Google spreadsheet use
[`example-simple-download.py`](https://code.google.com/p/webmaster-tools-downloads/source/browse/example-simple-download.py)
instead of `example-create-spreadsheet.py` in the example above.

You could easily configure these scripts to be run daily or monthly to archive and view your
search queries data across larger date ranges than the current one month of data that is available
in Webmaster Tools, for example, by setting up a cron job or using Windows Task Scheduler.

An important point to note is that this script example includes user name and password credentials
within the script itself. If you plan to run this in a production environment you should follow
security best practices like using encrypted user credentials retrieved from a secure data storage
source. The script itself uses HTTPS to communicate with the API to protect these credentials.

Take a look at the search queries downloader script and start using search queries data in your
own scripts or tools. Let us know if you have questions or feedback in the
[Webmaster Help Forum](https://support.google.com/webmasters/community/label?lid=462896acb3879639&hl=en).
