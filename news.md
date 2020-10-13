---
layout: page
title: News
description: Checkout the latest changes!
---

{% for item in site.data.news %}
# {{ item.date }}
 {% for entries in item.changes %}
- {{ entries.entry }}
 {% endfor %}
{% endfor %}
