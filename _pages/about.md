---
layout: notebook
permalink: /
title: About
description: Xiyu Ke is an M.S. student at Rutgers interested in robotic manipulation and robot learning. Explore three robotics projects and a little about life beyond research.
home: true
redirect_from:
  - /about/
  - /about.html
---
<section class="home-intro" aria-labelledby="intro-title">
  <h1 id="intro-title">Xiyu Ke</h1>
  <div class="home-bio">
    <p>I'm an M.S. student in <strong>Electrical and Computer Engineering</strong> at <strong>Rutgers University</strong>. I received my B.S. in Intelligent Science and Technology from Dalian Maritime University.</p>
    <p>My research focuses on <strong>robotic manipulation and robot learning</strong>. I'm particularly interested in world models for predicting action outcomes and enabling more generalizable robotic planning and manipulation.</p>
    <div class="intro-links"><a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a><a href="{{ '/CV/Academic_CV.pdf' | relative_url }}?v={{ site.time | date: '%s' }}">CV <span class="file-type">[PDF]</span></a></div>
  </div>
  {% assign portrait = site.static_files | where: 'path', site.data.profile.photo | first %}
  <div class="portrait">
    {% if portrait %}
    <img src="{{ site.data.profile.photo | relative_url }}" alt="{{ site.data.profile.photo_alt | escape }}" width="360" height="440" fetchpriority="high">
    {% else %}
    <div class="portrait-placeholder" role="img" aria-label="Space reserved for a photo of Xiyu Ke"><svg width="36" height="36" viewBox="0 0 36 36" fill="none" stroke="currentColor" stroke-width="1.25" aria-hidden="true"><rect x="5" y="5" width="26" height="26" rx="3"/><circle cx="14" cy="13" r="2.5"/><path d="m6 26 8-8 6 6 4-4 7 7"/></svg><span>Photo coming soon</span></div>
    {% endif %}
  </div>
</section>

<section class="home-projects" id="projects" aria-labelledby="projects-title">
  <h2 id="projects-title">Projects</h2>
  <div class="demo-list">
    {% for project in site.data.projects %}
    <article class="demo-row" aria-labelledby="project-{{ project.id }}">
      <div class="demo-copy">
        <h3 id="project-{{ project.id }}">{{ project.name }}</h3>
        <p class="demo-title">{{ project.title }}</p>
      </div>
      {% include project-media.html project=project compact=true %}
      <p class="demo-summary">{{ project.home_summary }}</p>
    </article>
    {% endfor %}
  </div>
</section>

{% include home-publications.html %}

<section class="home-hobbies" aria-labelledby="hobbies-title">
  <h2 id="hobbies-title">Beyond research</h2>
  <ul class="hobby-list">
    <li><svg width="32" height="32" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M11 16h10M4 13v6m24-6v6"/><rect x="7" y="9" width="4" height="14" rx="1"/><rect x="21" y="9" width="4" height="14" rx="1"/></svg><span>Fitness</span></li>
    <li><svg width="32" height="32" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m11 5-5 3-3 10 5 2 3-7v14h10V13l3 7 5-2-3-10-5-3M11 5l8 13M21 5 11 22M10 22h12m-5 0 4 6m-4-6-3 7"/></svg><span>Brazilian jiu-jitsu</span></li>
    <li><svg width="32" height="32" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m2 26 10-18 10 18H2Zm17-5 4-8 7 13h-8M9 14l3 3 3-3"/><circle cx="24" cy="7" r="2.5"/></svg><span>The outdoors</span></li>
  </ul>
</section>
