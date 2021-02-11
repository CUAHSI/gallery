# Exploratory Data Visualization for the Physical Properties of Lakes

This lesson was adapted from educational material written by Dr. Kateri Salk for her Fall 2019 Hydrologic Data Analysis course at Duke University. This is the first part of a two-part exercise focusing on the physical properties of rivers.

## Introduction

The field of **limnology**, the study of inland waters, uses a unique graph format to display relationships of variables by depth in a lake (the field of oceanography uses the same convention). Depth is placed on the y-axis in reverse order and the other variable(s) are placed on the x-axis. In this manner, the graph appears as if a cross section were taken from that point in the lake, with the surface at the top of the graph. This lesson introduces physical properties of lakes, namely stratification, and its visualization using the package `ggplot2`.

## Learning Objectives

After successfully completing this exercise, you will be able to:

1. Investigate the concepts of lake stratification and mixing by analyzing monitoring data

2. Apply data analytics skills to applied questions about physical properties of lakes

3. Communicate findings with peers through oral, visual, and written modes

## Requirements to Complete Lesson

### Packages

This lesson requires the installation of the following R packages to run the provided script:

`tidyverse`- Version 1.3.0. A collection of R packages designed for data science.

`lubridate`- Version 1.7.9. Functions for working with dates/times.

`ggplot2`- Version 3.3.3. Creates elegant data visualisations using the Grammar of Graphics.

`scales`- Version 1.1.1. Graphical scales provide methods for automatically determining breaks and labels for axes and legends.

`dataRetrieval`- Version 2.7.6. Retrieval Functions for USGS and EPA Hydrologic and Water Quality Data.

## Data and Code

This lesson will import daily discharge data for the Eno River near Durham, North Carolina for the entire period of record using the dataRetrieval package. The package was created to make querying and downloading hydrologic data from the USGS National Water Information System (NWIS) and the multi-agency database, Water Quality Portal (WQP). NWIS only contains data collected by or for the USGS. It should be noted that the databases are not static as data is constantly being added. For more in-depth information on the dataRetrieval package, please visit:

https://cran.r-project.org/web/packages/dataRetrieval/vignettes/dataRetrieval.html.

The code provided in this resource was developed using R version 3.6.1.
