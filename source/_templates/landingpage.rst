.. _{{ label }}:

{{ title }}
-------


**Description**

{{ description }}

{# ############# #}
{# COMPUTE BLOCK #}
{# ############# #}

.. container:: launch-container pb-1
    {% for option in launch_options %}
        {% if 'tooltip' in option %}
            :link-badge:`{{ option['url'] }},"{{ option['name'] }}",cls=badge-primary text-white launch-badge, tooltip={{ option['tooltip'] }}`
        {% else %} 
            :link-badge:`{{ option['url'] }},"{{ option['name'] }}",cls=badge-primary text-white launch-badge`
        {% endif %}
    {% endfor %}

.. raw:: html
   
   <br />&nbsp;

{# ############ #}
{# AUTHOR BLOCK #}
{# ############ #}

{% if authors %}
.. panels::
    :container: container pb-2
    :card: shadow
    :column: col-lg-12 col-md-6 col-sm-6 col-xs-12 p-2
    :body: text-left


    ---
      **Authors**
      ^^^^^
    {% for author in authors %}
        {% if 'url' in author -%}
            :link-badge:`{{ author['url'] }},"{{ author['name'] }}",cls=badge-primary text-white`
        {% else -%}
            :badge:`{{ author['name'] }},badge-secondary`
        {% endif -%}
            - {{ author['organization'] }} 
        {% if 'email' in author -%}
            (`contact <{{ author['email'] }}>`_)
        {% endif -%}
     {% endfor %}
{% endif %}

.. panels::
    :container: container pb-2
    :card: shadow
    :column: col-lg-12 col-md-6 col-sm-6 col-xs-12 p-2
    :body: text-left

    :column: col-lg-12 p-2
       **Code Examples**
       ^^^^^^^^^^^
     .. toctree::
        :maxdepth: 2
        :titlesonly:
        :glob:
        
        {% if code_path %}
        {{ code_path }}/**
        {% else %}
        data/**
        {% endif %}
