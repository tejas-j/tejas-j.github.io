---
title: CV
description: Curriculum vitae of Tejas R. Jammihal, bioinformatics scientist at the Children's Hospital of Philadelphia.
permalink: /cv/
---
{%- assign cv = site.data.cv -%}

<div class="section-head">
  <h1>Curriculum vitae</h1>
  <a class="button" href="{{ site.author.cv | relative_url }}">Download PDF</a>
</div>

<h2>Experience</h2>
{%- for e in cv.experience %}
<div class="cv-item">
  <div class="cv-dates">{{ e.dates }}</div>
  <div>
    <h3>{{ e.title }}</h3>
    <p class="cv-org">{{ e.org }}{% if e.unit %} · {{ e.unit }}{% endif %} · {{ e.location }}</p>
    <ul>
      {%- for b in e.bullets %}<li>{{ b }}</li>{% endfor %}
    </ul>
  </div>
</div>
{%- endfor %}

<h2>Education</h2>
{%- for e in cv.education %}
<div class="cv-item">
  <div class="cv-dates">{{ e.dates }}</div>
  <div>
    <h3>{{ e.degree }}</h3>
    <p class="cv-org" style="margin-bottom:0">{{ e.org }}</p>
  </div>
</div>
{%- endfor %}

<h2>Skills</h2>
<ul class="skills">
  {%- for s in cv.skills %}
  <li><span class="k">{{ s.group }}</span><span>{{ s.items }}</span></li>
  {%- endfor %}
</ul>

<h2>Honors</h2>
<ul class="plain">
  {%- for h in cv.honors %}<li>{{ h }}</li>{% endfor %}
</ul>

<h2>Service and mentoring</h2>
<ul class="plain">
  {%- for s in cv.service %}<li>{{ s }}</li>{% endfor %}
</ul>

<p class="pub-note">Publications are listed on the <a href="{{ '/publications/' | relative_url }}">publications page</a>.</p>
