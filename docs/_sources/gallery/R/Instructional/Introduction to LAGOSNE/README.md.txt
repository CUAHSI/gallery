# Chemical Properties of Lakes: Introduction to the Lake Multi-Scaled Geospatial and Temporal Database (LAGOSNE)

This lesson was adapted from educational material written by Dr. Kateri Salk for her Fall 2019 Hydrologic Data Analysis course at Duke University. 

## Introduction

Trophic states are based on lake fertility.  The root “trophy” means nutrients; therefore, lakes are classified based on the amount of available nutrients for organisms.  More fertile lakes have more nutrients and therefore more plants and algae. There are four lake trophic states:

“Oligo” means very little; therefore, oligotrophic means very little nutrients (Phosphorus and Nitrogen). In oligotrophic lakes, oxygen is found at high levels throughout the water column. Cold water can hold more dissolved oxygen than warm water, and the deep region of oligotrophic lakes stays very cold. In addition, low algal concentration allows deeper light penetration and less decomposition.

“Meso” means middle or mid; therefore, mesotrophic means a medium amount of nutrients (Phosphorus and Nitrogen). Mesotrophic lakes behave differently than oligotrophic lakes in that they stratify, meaning they separate into layers in the summer (more on lake stratification). The top layer of water becomes warm from the sun and contains algae. Since the by-product of photosynthesis is oxygen, oxygen concentration remains high at the surface of the lake. The bottom layer remains cooler and can become anoxic in mid-summer. 

“Eu” means true; therefore, eutrophic literally means true nutrients or truly nutrient rich (Phosphorus and Nitrogen). Eutrophic lakes are found in southern Minnesota where the soils are more fertile and where there is a lot of farmland. Eutrophic lakes are shallow and have murky water and mucky, soft bottoms.

Hypereutrophic lakes are at the extreme end of the eutrophic range with exceedingly
high nutrient concentrations and associated biomass production. In temperate regions
the fish communities are dominated by roach and bream. Anoxia or complete loss of oxygen often occurs in the hypolimnion during summer stratification. 

For more information on lake trophic states, please visit:

http://www.lake.wateratlas.usf.edu/library/learn-more/learnmore.aspx?toolsection=lm_tsi and http://www.manitowoccountylakesassociation.org/oligotrophic-vs-mesotrophic-vs-eutrophic/. 

## Learning Objectives 

After successfully completing this exercise, you will be able to:

1. Navigate and explore the LAGOSNE database and R package

2. Evaluate lake water quality using the trophic state index

3. Analyze spatial and temporal patterns of water quality across the northeast U.S.

# Requirements to Complete Lesson 

### Packages 

This lesson requires the installation of the following R packages to run the provided script:

- `tidyverse`- Version 1.3.0. A collection of R packages designed for data science. 

- `lubridate`- Version 1.7.9. Functions for working with dates/times. 

- `ggplot2`- Version 3.3.3. Creates elegant data visualisations using the Grammar of Graphics.

- `scales`- Version 1.1.1. Graphical scales provide methods for automatically determining breaks and labels for axes and legends.

- `repr`- Version 1.1.0. String and binary representations of objects for several formats / mime types.

- `LAGOSNE`- Version 2.0.2. Client for programmatic access to the Lake Multi-scaled Geospatial and Temporal database <https://lagoslakes.org>, with functions for accessing lake water quality and ecological context data for the US.

### Data and Code 

This lesson will query data from LAGOSNE, a combination of three data modules (LAGOSlocus, LAGOSlimno, LAGOSgeo) designed to be of use for researchers and managers to facilitate further development of our basic understanding of lake water quality at broad scales using water quality data on thousands of lakes collected over the last several decades. The database includes information about lakes in a lake-rich region of 17 states in the United States, including Minnesota, Iowa, Wisconsin, Illinois, Missouri, Michigan, Indiana, Ohio, Pennsylvania, New York, New Jersey, Connecticut, New Hampshire, Rhode Island, Massachusetts, Vermont, and Maine. LAGOSNE contains a complete census of all lakes greater than 4 hectares in the region with supporting ecological context information. Additionally, for a subset of lakes, LAGOSNE contains water quality data. The LAGOSNE package was built so that future data users could easily retrieve and manipulate the data, as well as easily access metadata.

It should be noted that the databases are not static as data is constantly being added.  For more in-depth information on the `LAGOSNE` package, please visit https://github.com/cont-limno/LAGOSNE and 
https://cont-limno.github.io/LAGOSNE/articles/lagosne_structure.html.

The code provided in this resource was developed using R version 3.6.1. 
