---
layout: notebook
title: Sitemap
permalink: /sitemap/
sitemap: false
---
<header class="page-intro"><h1>Sitemap</h1></header>
<section class="index-links"><h2>Main pages</h2><ul>{% for link in site.data.navigation.main %}<li><a href="{{ link.url | relative_url }}">{{ link.title }}</a></li>{% endfor %}</ul><h2>Research projects</h2><ul>{% for project in site.data.projects %}<li><a href="{{ project.url | relative_url }}">{{ project.name }}: {{ project.title }}</a></li>{% endfor %}</ul><a href="{{ '/sitemap.xml' | relative_url }}">XML sitemap</a></section>
