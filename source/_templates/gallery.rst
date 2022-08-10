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


.. grid:: 1

    {% for category, cat_data in categories.items() %}

    {% for example in cat_data %}

      .. grid-item-card:: {{ example['short_title'] }}
          :img-top: /_static/{{ example['thumbnail'] }}
          :link: {{ example['label'] }} 
          :link-type: ref
          :class-card: gallery-example
        
          {% if 'tags' in example %}
           {% for tag in example['tags'] -%}
            :bdg-ref-info-line:`{{ tag }} <{{ tag }}>`
           {%- endfor %}
          {% endif %}

    
          {{ example['short_description'] }}

    {% endfor %}

    {% endfor %}
