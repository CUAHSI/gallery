# Physical Properties of Rivers: Calculating Recurrence Interval and Exceedance Probability

This lesson was adapted from educational material written by Dr. Kateri Salk for her Fall 2019 Hydrologic Data Analysis course at Duke University. This is the first part of a two-part exercise focusing on the physical properties of rivers. 

## Introduction

Rivers are bodies of freshwater flowing from higher elevations to lower elevations due to the force of gravity. One of the most important physical characteristics of a stream or river is **discharge**, the volume of water moving through the river or stream over a given amount of time. This exercise will introduce the concepts of **Recurrence Intervals** and **Exceedance Probability** for the prediction of streamflow discharge. 

## Learning Objectives 

After successfully completing this exercise, you will be able to:

1. Execute queries to pull a variety of National Water Information System (NWIS) and Water Quality Portal (WQP) data into R.

2. Calculate recurrence interval and exceedance probability from daily discharge data. 

## Requirements to Complete Lesson 

### Packages 

This lesson requires the installation of the following R packages to run the provided script:

- `tidyverse`- Version 1.3.0. A collection of R packages designed for data science. 

- `lubridate`- Version 1.7.9. Functions for working with dates/times. 

- `ggplot2`- Version 3.3.3. Creates elegant data visualisations using the Grammar of Graphics.

- `scales`- Version 1.1.1. Graphical scales provide methods for automatically determining breaks and labels for axes and legends.

- `dataRetrieval`- Version 2.7.6. Retrieval Functions for USGS and EPA Hydrologic and Water Quality Data.

### Data and Code 

This lesson will import daily discharge data for the Eno River near Durham, North Carolina for the entire period of record using the `dataRetrieval` package. The package was created to make querying and downloading hydrologic data from the USGS National Water Information System (NWIS) and the multi-agency database, Water Quality Portal (WQP) easier. NWIS contains streamflow, peak flow, rating curves, groundwater, and water quality data data collected by or for the USGS. WQP only contains water quality data.

It should be noted that the databases are not static as data is constantly being added.  For more in-depth information on the `dataRetrieval` package, please visit https://cran.r-project.org/web/packages/dataRetrieval/vignettes/dataRetrieval.html. 

The code provided in this resource was developed using R version 3.6.1. 
