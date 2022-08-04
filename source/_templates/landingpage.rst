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

    .. raw:: html

        {% for option in launch_options %}
        {% if 'tooltip' in option %}
        <a class="badge launch" target='_blank' href={{ option['url'] }} title={{ option['tooltip'] }}>
            <span>{{ option['name'] }}</span>
        </a>
        {% else %} 
        <a class="badge launch" target='_blank' href={{ option['url']  }}>
            <span>{{ option['name'] }}</span>
        </a>
        {% endif %}
        {% endfor %}


.. raw:: html
    
    <br />&nbsp;
    <hr>


    
.. container:: container-lg launch-container pb-1 author-div


    .. container:: landing-page-header

        **Keywords:**
        
        {% for tag in tags -%}    

           :bdg-ref-info-line:`{{ tag }} <{{ tag }}>`

        {%- endfor %}


    .. raw:: html
    
        <br />

    .. container:: landing-page-header

        **Authors:**  

    .. raw:: html

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


                    {% if 'hs-profile' in authors[i] %}

                        <a class="sphinx-bs badge badge-primary text-white reference external" target='_blank' href={{ authors[i]['hs-profile'] }}>
                            <span>Profile</span>
                        </a>

                    {% endif %}
                    <!-- TODO: Include personal webpages from conf.yaml -->

                </div>
            </span>

        {% endfor %}


.. raw:: html

    <br />&nbsp;
    <br />&nbsp;


.. container:: container-lg example-content

    .. tabs::

        .. tab:: Description

            {% if description['type'] == 'markdown' %}
            
            .. mdinclude:: {{ description['value'] }}

            {% elif description['type'] == 'text' %}

            .. raw:: html

                {{ description['value'] }}

            {% else %}

                description format is not supported.

            {% endif %}

        {% if code_path or notebooks %}
        .. tab:: Code 

            The following code files are included in this example: 

            {% if code_path %}
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
                .. toctree::
                   :titlesonly:
                   :maxdepth: 1

                   {% for item in notebooks %}
                   {{ item['label'] }} <{{ item['name'] }}>
                   {% endfor %}

            {% endif %}
        {% endif %}

        
        {% for tab in additional_tabs %}
        .. tab:: {{ tab['name'] }}
            {% if tab['type'] == 'markdown' %}
            
            .. mdinclude:: {{ tab['value'] }}

            {% elif tab['type'] == 'text' %}

            .. raw:: html

                {{ tab['value'] }}

            {% elif tab['type'] == 'youtube' %}

            .. youtube:: {{ tab['value'] }}

            {% endif %}



        {% endfor %}
