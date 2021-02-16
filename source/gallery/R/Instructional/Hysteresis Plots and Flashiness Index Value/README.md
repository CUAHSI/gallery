# High Frequency Flow Data: Flashiness Index Value and Hysteresis Plots

This lesson was adapted from educational material written by Dr. Kateri Salk for her Fall 2019 Hydrologic Data Analysis course at Duke University. This is the second part of a two-part exercise focusing on high frequency flow data. 

## Introduction 
**Flashiness** is how responsive a stream is to precipitation. Flashiness is an important characteristic of the stream hydrologic regime. A "flashy" stream is one that experiences a rapid increase in flow shortly after onset of a precipitation event, and an equally rapid return to base conditions shortly after the end of the precipitation event. A "flashy" stream will thus increase in stormflow much faster following a precipitation event.

## Learning Objectives

After successfully completing this notebook, you will be able to:

1. Calculate the Flashiness Index Value of a river

2. Use a hysteresis plot to understand watershed dynamics

3. Communicate findings with peers through oral, visual, and written modes

## Requirements to Complete Lesson 

### Packages

This lesson requires the installation of the following R packages to run the provided script:

- `ggplot2`- Version 3.3.3. Creates elegant data visualisations using the Grammar of Graphics.

- `tidyverse`- Version 1.3.0. A collection of R packages designed for data science.

- `lubridate`- Version 1.7.9. Functions for working with dates/times.

- `scales`- Version 1.1.1. Graphical scales provide methods for automatically determining breaks and labels for axes and legends.

- `dataRetrival`- Version 2.7.6. Retrieval Functions for USGS and EPA Hydrologic and Water Quality Data.

- `xts`- Version 0.12.1. Provides for uniform handling of R's different time-based data classes by extending zoo, maximizing native format information preservation and allowing for user level customization and extension, while simplifying cross-class interoperability.

- `dygraphs`- Version 1.1.1.6. R interface for the dygraphs Javascript charting library. Provides rich facilities for charting time-series data in R, including highly configurable series- and axis-display and interactive features like zoom/pan and series/point highlighting.

- `Cairo` - Version 1.5-12.2. R graphics device using cairographics library that can be used to create high-quality vector (PDF, PostScript and SVG) and bitmap output (PNG,JPEG,TIFF), and high-quality rendering in displays (X11 and Win32).

### Data and Code 

This lesson will import instantaneous value data from the National Water Information System for Third Fork Creek and Ellerbe Creek in North Carolina for the entire period of record using the `dataRetrieval` package. The package was created to make querying and downloading hydrologic data from the USGS National Water Information System (NWIS) and the multi-agency database, Water Quality Portal (WQP) easier. NWIS contains streamflow, peak flow, rating curves, groundwater, and water quality data data collected by or for the USGS. WQP only contains water quality data.

It should be noted that the databases are not static as data is constantly being added.  For more in-depth information on the `dataRetrieval` package, please visit https://cran.r-project.org/web/packages/dataRetrieval/vignettes/dataRetrieval.html. 

The code provided in this resource was developed using R version 3.6.1. 
