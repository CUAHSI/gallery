.. toctree::
   :maxdepth: 2
   :hidden:
   :glob:
   :caption: Galleries

   gallery/Python/index
   gallery/R/index
   gallery/RShiny/index


CUAHSI Compute and Modeling Gallery
=============================================


..
  This is where we construct the homepage thumbnail panels.
  For more details, see https://sphinx-panels.readthedocs.io/en/latest/ 

.. grid:: 1 2 2 3

{% for gallery in galleries %}

    {% if 'label' in gallery %}

        .. grid-item-card:: {{ gallery['display_name'] }}
            :img-top: {{ gallery['thumbnail'] }}
            :link: {{ gallery['label'] }}
            :link-type: ref
            :shadow: lg
            :padding: 2
            :columns: 12 6 5 3

            {{ gallery['description']|e }}


     {% endif %}

{% endfor %}



