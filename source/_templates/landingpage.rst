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



{% for author in authors %}

.. dropdown:: {{ author['name'] }}
    :container: + shadow btn-author
    :animate: fade-in-slide-down
    :body: bg-light text-left
    
    {{ author['organization'] }} 

    {% if 'email' in author %}
    :link-badge:`{{ author['email'] }},"Email",cls=badge-primary text-white`
    {% endif %}

    {% if 'url' in author %}
    :link-badge:`{{ author['url'] }},"Webpage",cls=badge-primary text-white`
    {% endif %}

{% endfor %}


.. raw:: html

    <br />&nbsp;
    <br />&nbsp;

    <div class=example-description>
    
    <h2> Description </h2>

    {% if markdown %}
    
    .. mdinclude:: {{ markdown }}
    
    {% else %}
    
    <p>{{ description }}</p>
    
    {% endif %}
    
    </div>

.. panels::
    :container: container pb-1 example-panels
    :card: shadow
    :column: col-lg-6 col-md-6 col-sm-12 col-xs-12 p-2
    :body: text-left

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

