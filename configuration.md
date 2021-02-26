# Example Configuration

Every example in the CUAHSI Gallery contains a customized configuration YAML file that's used to specify the content. To learn more about the YAML format, see the [https://yaml.org}(https://yaml.org/). The required and optional arguments contained in this file are listed below.

## Configuration Elements

### description (required)

A long-form description of the example. If, `hs` element is provided, this will be overridden with the HydroShare resource abstract.

```
description: |
	This notebook provides a very brief introduction to 
	...................................................
   ....................................................
   ....................................................
   ............... as a batch job for the entire CONUS. 
```


### thumbnail (required)

Relative path to the image that will be displayed on the example card. It's recommended that the image represents the work or outcome of the example.

```
thumbnail: ./thumbnail-image.png
```

### code\_path

Relativate path to the code, data, and/or notebooks associated with the example.

```
code_path: ./example-code
```

### title

The title that will be displayed on the example landing page.

```
title: Hurricane Harvey NWM Subsetting Exercise - Given at the 2018 CUAHSI Summer Innovators Program.
```

### short_description (optional)

An abbreviated description (<150 characters) to display below the thumbnail image. Long descriptions are truncated at 150 characters often making the text meaningless. This provides a mechanism for defining alternate description.

```
short_description: An introduction to using OpenDAP and Python to subset NWM simulation forecasts.
```

### short_title (optional)

An abbreviated title (<50 characters) to display above the thumbnail image.

```
short_title: Subsetting NWM Forcasts
```

### launch\_options

### hydroshare Id

A HydroShare resource identifer to use for gathering example metadata. If a HydroShare resource identifier is provided, it will be used to collect, format, and display metadata on the example landing page. Note, YAML elements `title`, `description`, `author`, etc. will override any data obtained from HydroShare.

```
hydroshare:
  id: 3db192783bcb4599bab36d43fc3413db
```

## Full Example

```
hydroshare:
  id: 3db192783bcb4599bab36d43fc3413db
code_path: ./notebooks
thumbnail: ./thumbnail.png
short_title: Subsetting NWM Forcasts
short_description: An introduction to collecting and processing National Water Model operational forecast data using THREDDs and OpenDAP.
launch_options:
  - name: Open In HydroShare
    url: https://hydroshare.org/resource/3db192783bcb4599bab36d43fc3413db


```
