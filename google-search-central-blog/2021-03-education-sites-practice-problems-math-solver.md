---
title: "New for education sites: Practice problems and Math solvers structured data"
source: google-search-central-blog
content_type: "search_update"
freshness_risk: "historical"
slug: "2021-03-education-sites-practice-problems-math-solver"
url: "https://developers.google.com/search/blog/2021/03/education-sites-practice-problems-math-solver"
canonical: "https://developers.google.com/search/blog/2021/03/education-sites-practice-problems-math-solver"
author: "Michael Le"
published: "2021-03-25T00:00:00+00:00"
updated: "2021-03-25T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2021_very_old"
  - "news_or_research"
  - "official_update_or_announcement"
fetched_at: "2026-06-14T13:38:26+00:00"
status_code: 200
html_hash: "55e6ec840666fd33fb60d489c0bb7261bd97adc37090df565d51a9ee6bbc3953"
clean_word_count: 894
clean_char_count: 5804
---
# New for education sites: Practice problems and Math solvers structured data

According to [Unesco](https://en.unesco.org/covid19/educationresponse), nearly 1.5 billion learners had their education
disrupted due to COVID-19. Almost overnight, students, parents, and educators had to adapt to new learning norms. Many folks turned to Google for
help finding educational and learning resources and we are committed to supporting ways to help people find what they're looking for.

In this post, we provide details to help you implement structured data on your [practice problem](/search/docs/appearance/structured-data/practice-problems) and [math solver](/search/docs/appearance/structured-data/math-solvers) pages to make
your pages eligible to feature on Google Search as rich results (please note that being eligible does not guarantee that your site will show up
in search results). We also provide [rich results status reports](https://support.google.com/webmasters/answer/7552505)
to help you make sure that your implementation is correct.

Practice content and math assistance have been some of the most requested information from learners. Practice material helps users gauge their mastery
of a concept while a solver provides explanations to help a user get unstuck while doing math problems. Both features present an opportunity for sites
with either material to increase brand awareness on the Google Search results page and may increase traffic as a result of an enhanced appearance.

If you have eligible content on your website, you can take advantage of these new schemas by following the best practices in this post.

## Practice problems markup

Practice problems on Google provides users with rich results that give them a preview of the learning content on your site. Check the full list
of [guidelines](/search/docs/appearance/structured-data/practice-problems#guidelines)
in our documentation. Specifically, we recommend that you focus on these guidelines:

- Add a `Quiz` property for each practice problem that you want to be featured. The structured data must appear
  on the same page as the practice problem a user can interact with on your web page.
- Your web page must include all required structured data properties as described under [required `Quiz` properties](/search/docs/appearance/structured-data/practice-problems#structured-data-type-definitions).
- You must mark up a minimum of two practice problems per concept (for example, two practice problems for the concept "quadratic equation").
  Focus on marking up the concepts and problems that you want to be eligible to appear in the Practice problems rich result.
  They can be on separate pages.

![Practice problems rich result on Google Search](/static/search/blog/images/practice-problems-rich-result.png "Practice problems rich result on Google Search")

Relevance to the user, including topicality, grade level and curriculum standards, can be key considerations for users when they're deciding on what learning
material to use. In our studies, we've heard that users look for these signals to determine if learning content online matches what they are
learning in school. That's why we encourage you to add all of the recommended properties that are relevant for your content.

## Math solvers markup

A math solver page provides a tool to help users input their math equations and find explanations for how to solve a math problem. For example,
a user would be able to enter an equation, like x^4 - 3x = 0, to see websites that have an explanation with steps for how to arrive
at the solution. By using Math solvers structured data, you can make your site eligible to be featured on Google Search when users enter a math
equation into the Google Search bar.

![Math solvers rich result on Google Search](/static/search/blog/images/math-solver-rich-result.png "Math solvers rich result on Google Search")

Math solvers structured data is only for official math solvers; don't add this structured data to pages where users cannot submit math equations
for a step-by-step solution. You can learn more about implementation details in the [developer documentation](/search/docs/appearance/structured-data/math-solvers).

## Debugging and monitoring Practice problems and Math solvers markup with Search Console

To help you monitor markup issues, we are also launching [reports in
Search Console](https://support.google.com/webmasters/answer/7552505) for both Practice problems and Math solvers that show all errors, warnings, and valid items for pages with structured data.

Use the report to understand what Google can or cannot read from your site, and troubleshoot rich result errors. In addition, once you fix an issue,
you can use the report to validate it, which will trigger a process where Google recrawls your affected pages. Learn more about how to use the
report to [monitor your rich results](https://www.youtube.com/watch?v=Vmfvf8nG09k).

![Practice problems report on Search Console](/static/search/blog/images/practice-problems-search-console.png "Practice problems report on Search Console")

You can also test your structured data using the [Rich Results Test](https://search.google.com/test/rich-results) by submitting
a code snippet or the URL of a page. The test shows any errors or suggestions for your structured data.

![Practice problems on Rich Results test](/static/search/blog/images/practice-problems-rich-results-test.png "Practice problems on Rich Results test")

We would love to hear your thoughts on how Practice problems or Math solvers structured data works for you. Send us any feedback either through
[Twitter](https://twitter.com/googlesearchc) or the [Search Central Help Community](https://support.google.com/webmasters/threads?thread_filter=(category:structured_data)).
