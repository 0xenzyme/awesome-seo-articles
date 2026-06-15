---
title: "An Introduction to TF-IDF: What It Is & How to Use It"
source: semrush-blog
content_type: "blog_article"
freshness_risk: "low"
slug: "tf-idf"
url: "https://www.semrush.com/blog/tf-idf/"
canonical: "https://www.semrush.com/blog/tf-idf/"
author: "Boris Mustapic"
published: "2024-02-28T12:28:00+00:00"
updated: "2024-02-28T12:28:00+00:00"
categories:
  - "Technical SEO"
freshness_reasons:
  - "date_2024_watch"
schema_genre: "Technical SEO"
fetched_at: "2026-06-12T20:03:14+00:00"
status_code: 200
html_hash: "24a95554ae07cedf9cf3cbaa8d4f6b7ea87aa0d3fda764fcff3094e009a91f4a"
clean_word_count: 1499
clean_char_count: 11104
---
# An Introduction to TF-IDF: What It Is & How to Use It

TF-IDF is a statistical method commonly used in information retrieval and natural language processing.

It’s an important concept for understanding how search engines analyze web content and identify key terms that can be associated with search queries.

Here’s what you need to know about it.

## What Is Term Frequency-Inverse Document Frequency (TF-IDF)?

Term frequency-inverse document frequency (TF-IDF) measures the importance of a word to a specific document.

It’s the product of two statistics: **term frequency (TF)** and **inverse document frequency (IDF)**.

### Term Frequency (TF)

Term frequency (TF) can be defined as the relative frequency of a term (t) within a document (d).

It’s calculated by dividing the number of times the term occurs in the document (*f**t*,*d*) by the total number of terms in the document.

Here’s the formula:

![Term frequency (TF) formula](https://static.semrush.com/blog/uploads/media/3f/ac/3fac3a83de09055b9e4b130c88497701/710bc4256154e8955ee8f7ef41432d4f/5PIjtEdMbYuQI-uECqX3IedqV6M66h6bCuXG6qe-NEqsY0yeMlCEEtXvLkVaICKm6FqA5da1U55894l8Y_0-lhHxNZSn6DNIVwf8pxoV3LPog2MUy1i3gBK5ybaLE8B2qeFQCCj-f3eqJrTB9-Ni508.png)![TF formula in text](https://static.semrush.com/blog/uploads/media/df/6c/df6ca4dedc56226ab3d29ede47a88e78/1a0867fd5cedea1b1559079764c357dc/duIhwSqyJIkOLG5E1Ur764cDQhkf5stzSU9undr8kRK_KkAmI9GXhIog4wQUylreByn4ccahw5H4Tz-4MhWOyGrSaElkuk7hb5aXBVJxOGnvOnuTn45FHNmF0qJPqJrSTw4zaua-MmxPo-94hzVVaKI.png)

For example, say you have a document containing 10,000 terms. And a specific term appears a total of 25 times in the document.

You’d calculate the term frequency as follows:

**TF** = 25/10,000 = 0.0025

### Inverse Document Frequency (IDF)

Inverse document frequency (IDF) measures the amount of information a term provides.

It’s calculated by dividing the total number of documents (N) by the number of documents that contain the term. Then, taking the logarithm of that quotient.

Here’s the formula:

![Inverse document frequency (IDF) formula](https://static.semrush.com/blog/uploads/media/67/58/6758866540c51aebaae73be6d4f54f58/9dcdc2861404a01386961a5ec35337c9/zB44m0RPrE3y7EqKrwaVKqNiXnGfwwPqEvVz9K2U1B4yTqUZ59OHWhHC5ArXxUUQ9utnR-QJXbod6l1cAOGXhR-GKUnvOMgU6tiFKjRAzLpdpe21nDDi7853mqWmsztEXNTYVXLwCQzhQ7zCertSItQ.png)

Let's say you have a collection of 10,000 documents (N=10,000), and a term appears in 500 of these documents.

Here’s how you’d calculate the IDF:

**IDF** = log 10,000/500 = 1.30

## TF-IDF Formula

To calculate TF-IDF, we need to multiply the values of TF and IDF:

![TF-IDF formula](https://static.semrush.com/blog/uploads/media/0c/d6/0cd6d6d875e69271160f372a2a5055a2/569dbf9f28fd91d180634e447f01228b/HKgDHBvSKTjxDdFVlqPt6L0n4ApHQh_hLGSo-nc-I3sgYuWsmxj1yiWowHx5Wpd479yqUjsgSvxsG-YX7zuYG4e6hEPa5tTainPq4_ua0mszXfModZdFGUG5fhggrsPlQFEJPXvFrncu2BvtwzbO1yQ.png)

**TF-IDF** = 0.00325

The final score shows the relevance of the term, with a higher score denoting higher relevance and a lower score denoting lower relevance.

### An Example of How to Calculate TF-IDF

So, how does TF-IDF work in practice?

Simply examining the TF, IDF, and TF-IDF formulas can be a bit overwhelming. Let’s take a look at an actual example.

Let’s say that the term “car” appears 25 times in a document that contains 1,000 words.

We’d calculate the term frequency (TF) as follows:

**TF** = 25/1,000 = 0.025

Next, let’s say that a collection of related documents contains a total of 15,000 documents.

If 300 documents out of the 15,000 contain the term “car,” we would calculate the inverse document frequency as follows:

**IDF** = log 15,000/300 = 1.69

Now, we can calculate the TF-IDF score by multiplying these two numbers:

**TF-IDF** = TF x IDF = 0.025 x 1.69 = 0.04225

## How to Use TF-IDF

TF-IDF has a number of applications. It can be used as a weighting factor for:

- **Information retrieval**: Variations of TF-IDF are used as a weighting factor by search engines to help understand the relevance of a page to a user’s search query
- **Text mining**: TF-IDF can help quantify what a document is about, which is a central question in text mining
- **User modeling**: Another application of TF-IDF involves assisting in the creation of models for user behavior and interests, which can then be used by product and content recommendation engines

### Use Semrush’s On Page SEO Tool for TF-IDF

Looking to do a bit of TF-IDF analysis for your own website? This is where Semrush’s [On Page SEO Tool](https://www.semrush.com/on-page-seo-checker/) can help.

You can use it to compare TF-IDF scores between your website content and competing pages.

Here’s how:

Enter your domain on the On Page SEO Tool page and hit the “**Get ideas**” button.

![On Page SEO Checker tool](https://static.semrush.com/blog/uploads/media/94/28/9428dd29a50f601a722119da12e12a87/0c3bf9077f4ee554739becc1aa4260a2/H1DgSoazJihjqE3MjI8VZaE4hWe3inPKOlaofL8DPEUc_aRgcfIKqZrw6Nnzkw5GL00ugn72bOGTJQG-64tsdtGg-8Llu1XIQHuTXn6gVr7fyUb0G2TXXoGecC_s0oD4nL1RNUPanB3rVMVG3BwY1eM.png)

The tool will then analyze your website. And present you with a report containing a list of ideas for optimizing your website for search engines.

To see TF-IDF scores for a specific page, visit the “**Optimization Ideas**” tab.

!["Optimization Ideas" tab in On Page SEO Checker tool](https://static.semrush.com/blog/uploads/media/60/70/6070d5bfba346dabe7a8119698112c0d/0919087c6ea28e57a1ac10e5a7163476/i1LpUfpZLKge_rFOyD2RzBJIukAcFFLYUDosySyEybIRa1s6BHLqz3oih_seAJP3WM4ejhud7x04p-jVBVe08oIFUSXb7VWRN6BKdKa_7X85gRbqFJ6dbVPQ_JCeqDn2ky5BmFde0kmB08Ub6-_gppo.png)

Find your desired page in the list, and click the blue button showing the total number of ideas for that page.

![Total number of ideas for a selected page in On Page SEO Checker](https://static.semrush.com/blog/uploads/media/eb/25/eb25c1684360996380c0a14a4fd10183/5ebb9c5c09a9ab9de2b7c89c386616c0/j65hwKmH2T0uSdZnnU9Nf9X98pd4WC0QTmZll6P_XCId8WqMC7mMyi3dRjoIDuv5oJRgfs__nn6Nnm_93AS_VgZz0xgB9WhKXJVwAX5tHSWgaTfHqq8r49C5TZj8AbR-cVxajppq9l6EkTQ1qbUa_BY.png)

Here, you’ll be presented with a list of ideas for that specific page.

![A list of page optimization ideas provided by On Page SEO Checker](https://static.semrush.com/blog/uploads/media/0b/fc/0bfcfb8e816d23118634dea384257cab/02714f31958561682a22cf5b1a8d8fa1/1bnIoH3Jp4Rl3ST6MKPvgvME4bZQMKxTjA8sUty6A4Uak4-9eEWTRv1KWXfHfPczp2o_fCs1U1p8yx6AWYOCPXlhuWhBKdEjFMBKH4VGYPx7KQlxLOhNTLOvVKRqiDQ5i4sBIMlb0A3vm1PNZXMqCpw.png)

Click on the “**See detailed analysis**” link under any of the ideas listed in the report.

![“See detailed analysis” link button in On Page SEO Checker](https://static.semrush.com/blog/uploads/media/6f/e2/6fe2f63b03a364c097cfe3d615a02841/38e1b87a0e619ecfa6cd64eb3fb8e702/PBbBOHnwXoo0kODLJMTH0Cb1xXduWTxLpFEQL1bUTOQHPWY0Utg2M_DR5v3bzy5qKgJS00biya41FyxfE-fnvwCRE1E8OGv8_kzOgdFrxBVYMsaeUkIDVJH7sBtzimVPf_zWZh5ZM5nMQXBOksZeTuM.png)

Go to the “**Keyword Usage**” tab.

![“Keyword Usage” table in On Page SEO Checker](https://static.semrush.com/blog/uploads/media/ee/7f/ee7f67701bcbf376cb110d816fe9b95f/7ea41f714905bda4558029959a5580da/WMHdLByvWe195h8vSz6zRdSljMMchgxZZWwffSKG6lOtxPdqIaALLXM1hHZ-aPVgXBJovAsSnYTZXur6V3e5Bo8ikmDhu6mKzBDYq5MbU6XFs3A6rNkdNQWcFJD6OAVVKVc7c201XVih_PXukAAlY3Y.png)

You’ll be able to compare TF-IDF scores in the “TF-IDF” section, as shown below.

![“TF-IDF” section in On Page SEO Checker](https://static.semrush.com/blog/uploads/media/85/8d/858d26a64a48b5d655b1bdd502669a64/9b51afc279c5b740c77d0a28b2bd0067/e5PweYSNwh69srJAoTCMPoekk6IkbcxctvPJUHb2M797kC1jdOkG1V7UKLXDrgxUIhpmDaKvqUohvmqcD4uf7iAnp1prDmiAN4Q4w8JlgKJM6nc18RHa1e3sjYn9cPH69f7eK_efcUaSfWbvyigF0Wo.png)

## Benefits of Using TF-IDF

Here are the main advantages of TF-IDF:

- **Easy to calculate**: Perhaps the biggest benefit of using TF-IDF is that it’s fairly simple to calculate and can serve as a starting point for more advanced analysis
- **Identifies important terms**: It can help identify important terms in a document, which is very useful for understanding what a document is about
- **Differentiates between common and rare terms**: Since TF-IDF looks at both the number of occurrences of a term in a single document—as well as the number of occurrences of the same term in a collection of documents—it helps to differentiate between common and rare terms
- **Language-independent**: TF-IDF works across all languages and is not limited by the language of a document
- **Scalable**: It’s capable of handling very big datasets containing a large number of documents

## Disadvantages of Using TF-IDF

TF-IDF also comes with its set of limitations:

- **Very rare terms can be problematic**: IDF scores can be misleadingly high for very rare terms, making them seem more important than they really are
- **No understanding of meaning or context**: TF-IDF only measures term frequency—it doesn’t understand the meaning behind the terms or the context in which they’re used
- **Ignores word order**: TF-IDF doesn’t care about word order so it can’t comprehend compound nouns or phrases as single-unit terms
- **Difficulties interpreting synonyms and similar words**: Since TF-IDF treats each term independently, it can have difficulties recognizing synonyms and similar words, which can lead to misleading scores

## The Evolving Role of TF-IDF in AI and Machine Learning

TF-IDF has numerous applications for [artificial intelligence (AI)](https://www.semrush.com/blog/ai-models/) and machine learning algorithms, including information retrieval, text mining, and more.

It keeps evolving alongside AI, with domain-specific TF-IDF models being developed at the moment. These models take into account the characteristics and nuances of specific industries they’re intended for.

Some examples include TF-IDF models aimed at the healthcare industry, which are capable of analyzing [clinical notes](https://arxiv.org/pdf/2105.09632.pdf) and [medical records](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7036927/) to retrieve valuable information for diagnosing and treating diseases.

TF-IDF is now being combined with transformer machine learning models (which learn context by tracking relationships between terms).

It’s also being utilized along with word embeddings.In this approach, terms are mapped to vectors, and the relationships between them are determined based on the distance in vector space.

In other words, these methods improve text analysis and information retrieval.

## Stay on Top of TF-IDF with Semrush

You can stay conscious of your content’s TF-IDF scores and compare them with those of your competitors by using Semrush’s [On Page SEO Tool](https://www.semrush.com/on-page-seo-checker/).

Apart from showing TF-IDF scores, the On Page SEO Tool can also help you identify dozens of ways to improve your website’s [on-page SEO](https://www.semrush.com/blog/on-page-seo/).

And improve your likelihood of ranking your content higher in search engine results.

*This post was updated in 2024. Excerpts from the original article by Christina Sanders may remain.*
