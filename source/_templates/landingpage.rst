.. _{{ label }}:

.. title:: {{ title }}

.. raw:: html

    <div class=example-title>
        <h1> {{ title }} </h1>
    </div>

{# ############### #}
{# COMPUTE OPTIONS #}
{# ############### #}


.. container:: container-lg launch-container pb-1

    {% for option in launch_options %}
        {% if 'tooltip' in option %}
            :link-badge:`{{ option['url'] }},"{{ option['name'] }}",cls=badge-primary text-white launch-badge, tooltip={{ option['tooltip'] }}`
        {% else %} 
            :link-badge:`{{ option['url'] }},"{{ option['name'] }}",cls=badge-primary text-white launch-badge`
        {% endif %}
    {% endfor %}



.. container:: container-lg launch-container pb-1 author-div
    
    .. raw:: html

        <br />&nbsp;
        <hr>
        <br />&nbsp;
        <h2> Authors </h2>

        {% for i in range(0, authors|length) %}    

            <span class="NameHighlights">
                <a href="javascript:;">{{ authors[i]['name'] }}</a>
                {% if i < authors|length - 1 %}
                    , 
                {% endif %}
                <div>

                    {{ authors[i]['organization'] }} 

                    <hr>

                    {% if 'email' in authors[i] %}

                        <a class="sphinx-bs badge badge-primary text-white reference external" href=mailto:{{ authors[i]['email'] }}>
                            <span>Email</span>
                        </a>

                    {% endif %}


                    {% if 'url' in authors[i] %}

                        <a class="sphinx-bs badge badge-primary text-white reference external" href={{ authors[i]['url'] }}>
                            <span>Webpage</span>
                        </a>

                    {% endif %}

                </div>
            </span>

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


.. raw:: html

    <h2> Code </h2>


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

