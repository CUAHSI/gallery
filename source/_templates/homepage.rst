.. toctree::
   :maxdepth: 2
   :hidden:
   :glob:
   :caption: Galleries

   gallery/Python/index
   gallery/R/index
   gallery/RShiny/index
   gallery/Matlab/index


CUAHSI Compute and Modeling Gallery
=============================================


..
  This is where we construct the homepage thumbnail panels.
  For more details, see https://sphinx-panels.readthedocs.io/en/latest/ 

.. panels::
    :card: shadow
    :img-top-cls: pl-3 pr-3 panel-img
    :column: col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2 gallery-card

{% for gallery in galleries %}

    {% if 'label' in gallery %}
    ---
    :img-top: {{ gallery['thumbnail'] }}

    {{ gallery['description']|e }}

    .. link-button:: {{ gallery['label'] }}
        :type: ref
        :text: {{ gallery['display_name'] }} Gallery
        :classes: btn-outline-primary btn-block stretched-link

     {% endif %}

{% endfor %}



