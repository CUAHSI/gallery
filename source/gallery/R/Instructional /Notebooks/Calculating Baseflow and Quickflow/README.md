# High Frequency Flow Data: Introduction to Dygraphs

This lesson was adapted from educational material written by Dr. Kateri Salk and teaching assistant Cathy Chamberlin for her Fall 2019 Hydrologic Data Analysis course at Duke University. This is the first part of a two-part exercise focusing on high frequency flow data. 

## Introduction
High frequency data is usually defined as frequencies significantly lower than daily (e.g. 5-minute, 15-minute, 1 hr etc). The large amount of data allows us to distinguish between different models (model validation) with a higher statistical precision. Baseflow is a portion of streamflow that is not directly generated from the excess rainfall during a storm event. In other words, this is the flow that would exist in the stream without the contribution of direct runoff from the rainfall. It should not be confused with groundwater flow. Quickflow is the part of a storm rainfall which moves quickly to a stream channel via surface runoff or overland flow, and forms a flood wave in the channel.  What types of hydrological and biological processes happen on this timescale that we might want to investigate?

## Learning Objectives

After successfully completing this notebook, you will be able to:
1. Determine stormflow and baseflow from high frequency flow data
2. Communicate findings with peers through oral, visual, and written modes

## Requirements to Complete Lesson 

### Packages
This lesson requires the installation of the following R packages to run the provided script:

- `ggplot2`- Version 3.3.3. Creates elegant data visualisations using the Grammar of Graphics.

- `tidyverse`- Version 1.3.0. A collection of R packages designed for data science.

- `lubridate`- Version 1.7.9. Functions for working with dates/times.

- `scales`- Version 1.1.1. Graphical scales provide methods for automatically determining breaks and labels for axes and legends.

- `dataRetrival`- Version 2.7.6. Retrieval Functions for USGS and EPA Hydrologic and Water Quality Data.

- `cowplot`- Version 1.1.1. Provides various features that help with creating publication-quality figures with 'ggplot2'.

- `EcoHydRology`- Version 0.4.12.1. This package provides a flexible foundation for scientists, engineers, and policy makers to base teaching exercises as well as for more applied use to model complex eco-hydrological interactions.

- `xts`- Version 0.12.1. Provides for uniform handling of R's different time-based data classes by extending zoo, maximizing native format information preservation and allowing for user level customization and extension, while simplifying cross-class interoperability.

- `dygraphs`- Version 1.1.1.6. R interface for the dygraphs Javascript charting library. Provides rich facilities for charting time-series data in R, including highly configurable series- and axis-display and interactive features like zoom/pan and series/point highlighting.

### Data and Code 

This lesson will import instantaneous value data from the National Water Information System for Third Fork Creek and Ellerbe Creek in North Carolina for the entire period of record using the `dataRetrieval` package. The package was created to make querying and downloading hydrologic data from the USGS National Water Information System (NWIS) and the multi-agency database, Water Quality Portal (WQP) easier. NWIS contains streamflow, peak flow, rating curves, groundwater, and water quality data data collected by or for the USGS. WQP only contains water quality data.

It should be noted that the databases are not static as data is constantly being added.  For more in-depth information on the `dataRetrieval` package, please visit https://cran.r-project.org/web/packages/dataRetrieval/vignettes/dataRetrieval.html. 

The code provided in this resource was developed using R version 3.6.1. 
