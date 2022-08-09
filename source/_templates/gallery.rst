.. _{{ label }}:

.. title:: {{ gallery_title }}

.. toctree::
   :caption: Table of Contents
   :name: {{ gallery_title }}-toc
   :hidden:
   :glob:

   *


========================
{{ gallery_title }}
========================

..
  This is where we construct the homepage thumbnail panels.
  For more details, see https://sphinx-panels.readthedocs.io/en/latest/
{% for category, cat_data in categories.items() %}

.. grid:: 1

    {% for example in cat_data %}

      .. grid-item-card:: {{ example['short_title'] }}
          :link: {{ example['label'] }} 
          :link-type: ref
        
          {% if 'tags' in example %}
           {% for tag in example['tags'] -%}
            :bdg-ref-info-line:`{{ tag }} <{{ tag }}>`
           {%- endfor %}
          {% endif %}

    
          {{ example['short_description'] }}

    {% endfor %}

{% endfor %}
