.. _{{ label }}:

.. toctree::
   :caption: Table of Contents
   :name: mastertoc
   :hidden:
   :glob:

   index


========================
{{ gallery_title }}
========================



..
  This is where we construct the homepage thumbnail panels.
  For more details, see https://sphinx-panels.readthedocs.io/en/latest/
{% for category, cat_data in categories.items() %}

{{ category }} Examples
******************************

.. panels::
    :card: shadow
    :img-top-cls: pl-5 pr-5
    :column: col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2

    {% for example in cat_data %}
    ---
    :img-top: /_static/{{ example['thumbnail'] }}
    
    **{{ example['title']|truncate(50, True) }}**

    {% if 'card_description' in example %}
        {{ example['card_description']|truncate(150, True) }}
    {% else %}
        {{ example['description']|truncate(150, True) }}
    {% endif %}

    .. link-button:: {{ example['label'] }}
        :type: ref
        :text: Open Example
        :classes: btn-outline-primary btn-block stretched-link
    
     {% endfor %}

{% endfor %}






..
    This is an example of a subgallery panel
    ---
    :img-top: _static/r-logo.jpeg


    .. link-button:: examples/r
        :type: ref
        :text: Spatial Plotting with RGdal
        :classes: btn-block stretched-link


