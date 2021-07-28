# Trend Detection and Forecasting

This lesson was adapted from educational material written by [Dr. Kateri Salk](https://www.hydroshare.org/user/4912/) for her Fall 2019 Hydrologic Data Analysis course at Duke University. This is the second part of a two-part exercise focusing on time series analysis. 

## Introduction
Time series are a special class of dataset, where a response variable is tracked over time. Time series analysis is a powerful technique that can be used to understand the various temporal patterns in our data by decomposing data into different cyclic trends. Time series analysis can also be used to predict how levels of a variable will change in the future, taking into account what has happened in the past.

## Learning Objectives

1. Choose appropriate time series analyses for trend detection and forecasting
2. Discuss the influence of seasonality on time series analysis
3. Interpret and communicate results of time series analyses 

## Requirements to Complete Lesson 

### Packages

This lesson requires the installation of the following R packages to run the provided script:

- `ggplot2`- Version 3.3.3. Creates elegant data visualisations using the Grammar of Graphics.

- `tidyverse`- Version 1.3.0. A collection of R packages designed for data science.

- `lubridate`- Version 1.7.9. Functions for working with dates/times.

- `scales`-Version 1.1.1. Graphical scales provide methods for automatically determining breaks and labels for axes and legends.

- `dataRetrival`-Version 2.7.6. Retrieval Functions for USGS and EPA Hydrologic and Water Quality Data.

- `stats`-Version 4.0.3. This package contains functions for statistical calculations and random number generation.

- `stlplus`-Version 0.5.1. Decompose a time series into seasonal, trend, and remainder components using an implementation of Seasonal Decomposition of Time Series by Loess (STL) that provides several enhancements over the STL method in the stats package.

- `LAGOSNE`- Version 2.0.2. Client for programmatic access to the Lake Multi-scaled Geospatial and Temporal database <https://lagoslakes.org>, with functions for accessing lake water quality and ecological context data for the US.

- `trend`- Version 1.1.4.  Non-Parametric Trend Tests and Change-Point Detection.

- `forecast`- Version 8.13. Methods and tools for displaying and analysing univariate time series forecasts including exponential smoothing via state space models and automatic ARIMA modelling.

- `tseries`- Version 0.10-48. Time series analysis and computational finance.

### Data and Code 

This lesson will query data from LAGOSNE, a combination of three data modules (LAGOSlocus, LAGOSlimno, LAGOSgeo) designed to be of use for researchers and managers to facilitate further development of our basic understanding of lake water quality at broad scales using water quality data on thousands of lakes collected over the last several decades. The database includes information about lakes in a lake-rich region of 17 states in the United States, including Minnesota, Iowa, Wisconsin, Illinois, Missouri, Michigan, Indiana, Ohio, Pennsylvania, New York, New Jersey, Connecticut, New Hampshire, Rhode Island, Massachusetts, Vermont, and Maine. LAGOSNE contains a complete census of all lakes greater than 4 hectares in the region with supporting ecological context information. Additionally, for a subset of lakes, LAGOSNE contains water quality data. The LAGOSNE package was built so that future data users could easily retrieve and manipulate the data, as well as easily access metadata.

It should be noted that the databases are not static as data is constantly being added.  For more in-depth information on the `LAGOSNE` package, please visit https://github.com/cont-limno/LAGOSNE and 
https://cont-limno.github.io/LAGOSNE/articles/lagosne_structure.html.

The code provided in this resource was developed using R version 3.6.1. 
