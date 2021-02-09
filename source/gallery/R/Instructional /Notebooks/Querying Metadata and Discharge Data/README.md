# Physical Properties of Rivers: Querying Metadata and Discharge Data

This lesson was adapted from educational material written by Dr. Kateri Salk for her Fall 2019 Hydrologic Data Analysis course at Duke University. This is the second part of a two-part exercise focusing on the physical properties of rivers. 

## Introduction

Rivers are bodies of freshwater flowing from higher elevations to lower elevations due to the force of gravity. One of the most important physical characteristics of a stream or river is **discharge**, the volume of water moving through the river or stream over a given amount of time. Discharge can be measured directly by measuring the velocity of flow in several spots in a stream and multiplying the flow velocity over the cross-sectional area of the stream. However, this method is effort-intensive. This exercise will demonstrate how to approximate discharge by developing a **rating curve** for a stream at a given sampling point.You will also learn to query metadata from and compare discharge patterns in climatically different regions of the United States. 

## Learning Objectives 

After successfully completing this exercise, you will be able to:

1. Execute queries to pull a variety of National Water Information System (NWIS) and Water Quality Portal (WQP) data into R.

2. Analyze seasonal and interannual characteristics of stream discharge and compare discharge patterns in different regions of the United States 

## Requirements to Complete Lesson 

### Packages 

This lesson requires the installation of the following R packages to run the provided script:

- `tidyverse`- Version 1.3.0. A collection of R packages designed for data science. 

- `lubridate`- Version 1.7.9. Functions for working with dates/times. 

- `ggplot2`- Version 3.3.3. Creates elegant data visualisations using the Grammar of Graphics.

- `scales`- Version 1.1.1. Graphical scales provide methods for automatically determining breaks and labels for axes and legends.

- `repr`- Version 1.1.0. String and binary representations of objects for several formats/mime types.

- `cowplot`- Version 1.1.1. Provides various features that help with creating publication-quality figures with 'ggplot2', such as a set of themes, functions to align plots and arrange them into complex compound figures, and functions that make it easy to annotate plots and or mix plots with images.

- `dataRetrieval`- Version 2.7.6. Retrieval Functions for USGS and EPA Hydrologic and Water Quality Data.

### Data and Code 

This lesson will import metadata and discharge data using the `dataRetrieval` package. The package was created to make querying and downloading hydrologic data from the USGS National Water Information System (NWIS) and the multi-agency database, Water Quality Portal (WQP). NWIS only contains data collected by or for the USGS. It should be noted that the databases are not static as data is constantly being added.  For more in-depth information on the `dataRetrieval` package, please visit:

https://cran.r-project.org/web/packages/dataRetrieval/vignettes/dataRetrieval.html. 

This exercise will analyze data from the following rivers/streams: 

* Haw River in North Carolina

* Verde River in Arizona 

* Bitterroot River in Montana

* Sauk River in Minnesota 

* Nehalem River in Oregon

The code provided in this resource was developed using R version 3.6.1. 
