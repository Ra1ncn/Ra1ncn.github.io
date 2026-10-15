---
layout: notebook
title: CV
permalink: /cv/
description: Xiyu Ke's education, research experience, publications, and technical skills.
redirect_from:
  - /resume
---
<header class="page-intro cv-intro"><div><h1>Curriculum vitae</h1><p class="page-lead">Xiyu Ke · Robotics & robot learning</p></div><a class="button primary" href="{{ '/CV/Academic_CV.pdf' | relative_url }}?v={{ site.time | date: '%s' }}" download>Download full CV <span class="file-type">PDF ↓</span></a></header>
<section class="cv-section"><h2>Research interests</h2><div><p>Robotic manipulation and robot learning, with a focus on fine-grained grasping and contact-aware motion planning. I’m interested in combining geometric reasoning with learning-based perception and control for reliable manipulation.</p></div></section>
<section class="cv-section"><h2>Education</h2>{% include education.html %}</section>
<section class="cv-section"><h2>Research experience</h2><div>{% for project in site.data.projects %}<article class="cv-experience"><p class="eyebrow">{{ project.period }}</p><h3><a href="{{ project.url | relative_url }}">{{ project.name }}: {{ project.title }}</a></h3><p class="muted">{{ project.lab }}<br>{{ project.role }} · {{ project.status }}</p><p>{{ project.summary }}</p><a class="text-link" href="{{ project.url | relative_url }}">Contributions and project details →</a></article>{% endfor %}<article class="cv-experience"><p class="eyebrow">APR. 2023 – JUL. 2024</p><h3>Quadrotor Navigation and Obstacle Avoidance</h3><p class="muted">Dalian Maritime University · Co-author; accepted at ICRA 2026</p><p>Implemented APF obstacle avoidance in V-REP using Lua; explored ant colony and particle swarm optimization for path planning. Integrated Crazyflie, distance sensing, and ROS flight control, with NOKOV motion capture for trajectory inspection and system debugging.</p></article></div></section>
<section class="cv-section"><h2>Publications</h2><div><p>One accepted conference paper and four submitted manuscripts, with full author lists and statuses on the publications page.</p><a class="text-link" href="{{ '/publications/' | relative_url }}">View publications & manuscripts →</a></div></section>
<section class="cv-section"><h2>Technical skills</h2><dl class="skills-list">{% for skill in site.data.skills %}<div><dt>{{ skill.category }}</dt><dd>{{ skill.items }}</dd></div>{% endfor %}</dl></section>
<section class="cv-section"><h2>Contact</h2><div><p>New Brunswick, NJ, USA</p><a class="text-link" href="mailto:{{ site.author.email }}">{{ site.author.email }} ↗</a></div></section>
