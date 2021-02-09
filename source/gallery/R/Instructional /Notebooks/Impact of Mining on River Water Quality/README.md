# Chemical Properties of Rivers: Impacts of Mining on Specific Conductance and pH 
 
 This lesson was adapted from educational material written by Dr. Kateri Salk for her Fall 2019 Hydrologic Data Analysis course at Duke University. 
 
## Introduction
 
The hydrologic impacts on mining can cause cause damage to a landscape in an area much larger than the mining site itself. Water-pollution problems caused by mining include acid mine drainage, metal contamination, and increased sediment levels. The devastating effects of mining impact fisheries, swimming, domestic water supply, irrigation, and other uses of streams. For more information on the environmental impacts of mining, please visit:

http://www.pollutionissues.com/Li-Na/Mining.html#ixzz6jGlfrX9m
 
## Learning Objectives 

After successfully completing this exercise, you will be able to:

1. Execute queries to pull a variety of National Water Information System (NWIS) and Water Quality Portal (WQP) data into R.

2. Analyze inorganic aspects of water quality following a watershed disturbance such as mining.

## Requirements to Complete Lesson 

### Packages 

This lesson requires the installation of the following R packages to run the provided script:

- `tidyverse`- Version 1.3.0. A collection of R packages designed for data science. 

- `lubridate`- Version 1.7.9. Functions for working with dates/times. 

- `ggplot2`- Version 3.3.3. Creates elegant data visualisations using the Grammar of Graphics.

- `scales`- Version 1.1.1. Graphical scales provide methods for automatically determining breaks and labels for axes and legends.

- `dataRetrieval`- Version 2.7.6. Retrieval Functions for USGS and EPA Hydrologic and Water Quality Data.

- `cowplot`- Version 1.1.1. Provides various features that help with creating publication-quality figures with 'ggplot2', such as a set of themes, functions to align plots and arrange them into complex compound figures, and functions that make it easy to annotate plots and or mix plots with images.

### Data and Code 

This lesson will import water quality data for two rivers in West Virginia, Twelvepole Creek and Kanawha River, for the entire period of record using the `dataRetrieval` package. The package was created to make querying and downloading hydrologic data from the USGS National Water Information System (NWIS) and the multi-agency database, Water Quality Portal (WQP) easier. NWIS contains streamflow, peak flow, rating curves, groundwater, and water quality data data collected by or for the USGS. WQP only contains water quality data.

It should be noted that the databases are not static as data is constantly being added.  For more in-depth information on the `dataRetrieval` package, please visit https://cran.r-project.org/web/packages/dataRetrieval/vignettes/dataRetrieval.html. 

The code provided in this resource was developed using R version 3.6.1. 
