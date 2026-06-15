---
title: "Send your recipes to the Google Assistant"
source: google-search-central-blog
content_type: "blog_article"
freshness_risk: "historical"
slug: "2018-05-send-your-recipes-to-google-assistant"
url: "https://developers.google.com/search/blog/2018/05/send-your-recipes-to-google-assistant"
canonical: "https://developers.google.com/search/blog/2018/05/send-your-recipes-to-google-assistant"
author: "Earl J. Wagner"
published: "2018-05-03T00:00:00+00:00"
updated: "2018-05-03T00:00:00+00:00"
categories:
  - "Google Search Central Blog"
freshness_reasons:
  - "date_2018_very_old"
  - "news_or_research"
fetched_at: "2026-06-14T13:32:20+00:00"
status_code: 200
html_hash: "329f2307ff7546177273e90ff0a4c50c58c2c9de1da3efcbe2867acb0f89d8f9"
clean_word_count: 386
clean_char_count: 2695
---
# Send your recipes to the Google Assistant

[Last year](https://www.blog.google/products/assistant/cooking-with-the-assistant-google-home-your-secret-ingredient/),
we launched Google Home with recipe guidance, providing users with step-by-step instructions for
cooking recipes. With more people using Google Home every day, we're publishing new guidelines so
your recipes can support this voice guided experience. You may receive traffic from more sources,
since users can now discover your recipes through the Google Assistant on Google Home. The
[updated structured data properties](/search/docs/appearance/structured-data/recipe#recipe_properties)
provide users with more information about your recipe, resulting in higher quality traffic to your
site.

## Updated recipe properties to help users find your recipes

We updated our
[recipe developer documentation](/search/docs/appearance/structured-data/recipe) to help
users find your recipes and experience them with Google Search and the Google Assistant on Google
Home. This will enable more potential traffic to your site. To ensure that users can access your
recipe in more ways, we need more information about your recipe. We now recommend the following
properties:

- **Videos:** Show users how to make the dish by adding a `video` array
- **Category**: Tell users the type of meal or course of the dish (for example,
  "dinner", "dessert", "entree")
- **Cuisine:** Specify the region associated with your recipe (for example,
  "Mediterranean", "American", "Cantonese")
- **Keywords**: Add other terms for your recipe such as the season ("summer"), the
  holiday ("Halloween", "Diwali"), the special event ("wedding", "birthday"), or other descriptors
  ("quick", "budget", "authentic")

We also added more guidance for `recipeInstructions`. You can specify each step of the
recipe with the `HowToStep` property, and sections of steps with the
`HowToSection` property.

## Add recipe instructions and ingredients for the Google Assistant

We now require the `recipeIngredient` and `recipeInstructions` properties if
you want to support the Google Assistant on Google Home. Adding these properties can make your
recipe eligible for integration with the Google Assistant, enabling more users to discover your
recipes. If your recipe doesn't have these properties, it won't be eligible for guidance with the
Google Assistant, but it can still be eligible to appear in Search results.

For more information, visit our
[Recipe developer documentation](/search/docs/appearance/structured-data/recipe). If you
have questions about the feature, please ask us in the
[Webmaster Help Forum](https://support.google.com/webmasters/community/).
