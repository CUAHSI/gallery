.. _{{ label }}:

.. title:: {{ title }}

.. raw:: html

    <div class=example-title>
        <h1> {{ title }} </h1>
    </div>

{# ############### #}
{# COMPUTE OPTIONS #}
{# ############### #}

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
    <hr>
    <br />&nbsp;

.. raw:: html

    <div class=example-description>
        <h2> Description </h2>
        <p>{{ description }}</p>
    </div>


{# ############ #}
{# AUTHOR BLOCK #}
{# ############ #}

{% if authors %}
.. panels::
    :container: container pb-2 example-panels
    :card: shadow
    :column: col-lg-6 col-md-6 col-sm-12 col-xs-12 p-2
    :body: text-left


    ---
      **Authors**
      ^^^^^
    {% for author in authors %}
        {% if 'url' in author -%}
            :link-badge:`{{ author['url'] }},"{{ author['name'] }}",cls=badge-primary text-white`
        {% else -%}
            :badge:`"{{ author['name'] }}", badge-secondary`
        {% endif -%}
            - {{ author['organization'] }} 
        {% if 'email' in author -%}
            (`contact <{{ author['email'] }}>`_)
        {% endif -%}
     {% endfor %}
{% endif %}

    ---
    {% if code_path %}

       **Source Code**
       ^^^^^^^^^^^
     .. toctree::
        :maxdepth: 1
        :titlesonly:
        :glob:
        
        {% if code_path %}
        {{ code_path }}/**
        {% else %}
        data/**
        {% endif %}
     {% endif %}
     {% if notebooks %}
       **Source Code**
       ^^^^^^^^^^^
     .. toctree::
        :titlesonly:
        :maxdepth: 1

        {% for item in notebooks %}
        {{ item['label'] }} <{{ item['name'] }}>
        {% endfor %}
     {% endif %}

