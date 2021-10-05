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

            {% if markdown %}

            .. mdinclude:: {{ markdown }}

            {% else %}

            .. raw:: html

                {{ description }}


            {% endif %}

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

        {% if additional_info %}
        .. tab:: Additional Information

            {{ additional_info }}

        {% endif %}
