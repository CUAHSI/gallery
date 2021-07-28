# Introduction to Time Series Analysis for Hydrologic Data

This lesson was adapted from educational material written by Dr. Kateri Salk for her Fall 2019 Hydrologic Data Analysis course at Duke University. This is the first part of a two-part exercise focusing on time series analysis. 

## Introduction
Time series are a special class of dataset, where a response variable is tracked over time. The frequency of measurement and the timespan of the dataset can vary widely. At its most simple, a time series model includes an explanatory time component and a response variable. Mixed models can include additional explanatory variables (check out the `nlme` and `lme4` R packages). We will be covering a few simple applications of time series analysis in these lessons.

### Opportunities

Analysis of time series presents several opportunities. In aquatic sciences, some of the most common questions we can answer with time series modeling are:

* Has there been an increasing or decreasing **trend** in the response variable over time?
* Can we **forecast** conditions in the future?


### Challenges

Time series datasets come with several caveats, which need to be addressed in order to effectively model the system. A few common challenges that arise (and can occur together within a single dataset) are: 

* **Autocorrelation**: Data points are not independent from one another (i.e., the measurement at a given time point is dependent on previous time point(s)).

* **Data gaps**: Data are not collected at regular intervals, necessitating *interpolation* between measurements. There are often gaps between monitoring periods. For many time series analyses, we need equally spaced points. 

* **Seasonality**: Cyclic patterns in variables occur at regular intervals, impeding clear interpretation of a monotonic (unidirectional) trend. Ex. We can assume that summer temperatures are higher.

* **Heteroscedasticity**: The variance of the time series is not constant over time.

* **Covariance**: the covariance of the time series is not constant over time.
Many of these models assume that the variance and covariance are similar over the time, which is known as heteroschedasticity. 

## Learning Objectives

After successfully completing this notebook, you will be able to:

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

### Data and Code 

This lesson will import daily discharge data for Clear Creek near Denver, Colorado for the entire period of record using the `dataRetrieval` package. The package was created to make querying and downloading hydrologic data from the USGS National Water Information System (NWIS) and the multi-agency database, Water Quality Portal (WQP) easier. NWIS contains streamflow, peak flow, rating curves, groundwater, and water quality data data collected by or for the USGS. WQP only contains water quality data.

It should be noted that the databases are not static as data is constantly being added.  For more in-depth information on the `dataRetrieval` package, please visit https://cran.r-project.org/web/packages/dataRetrieval/vignettes/dataRetrieval.html. 

The code provided in this resource was developed using R version 3.6.1. 

