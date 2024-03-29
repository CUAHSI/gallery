# Example Configuration

Every example in the CUAHSI Gallery contains a customized configuration YAML
file that's used to specify the content. To learn more about the YAML format,
see the [https://yaml.org](https://yaml.org/). The required and optional
arguments contained in this file are listed below.


## Required Fields

The following fields are required in the `conf.yaml` file. In some cases, if a
field is not provided a placeholder will be added.



#### Description (required)

A long-form description of the example. If, `hs` element is provided, this will
be overridden with the HydroShare resource abstract.

``` yaml
description: | This notebook provides a very brief introduction to
...................................................
....................................................
....................................................  
............... as a batch job for the entire CONUS.
```

#### Thumbnail (required)

Relative path to the image that will be displayed on the example card. It's
recommended that the image represents the work or outcome of the example.

``` yaml
thumbnail: ./thumbnail-image.png
```

#### Title (required)

The title that will be displayed on the example landing page.

``` yaml
title: Hurricane Harvey NWM Subsetting Exercise - Given at the 2018 CUAHSI Summer Innovators Program.
```

## Optional Fields

The following fields are optional but highly recommended.

#### Short Description (optional)

An abbreviated description (<150 characters) to display below the thumbnail
image. Long descriptions are truncated at 150 characters often making the text
meaningless. This provides a mechanism for defining alternate description.

``` yaml
short_description: An introduction to using OpenDAP and Python to subset
NWM simulation forecasts.
```

#### Short Title (optional)

An abbreviated title (<50 characters) to display above the thumbnail image.

``` yaml
short_title: Subsetting NWM Forcasts
```

#### Code Path (optional)

Relative path to the code, data, and/or notebooks associated with the
example.

``` yaml
code_path: ./example-code
```

#### Launch Options (optional)

Launch options appear as badges at the top of the example landing page. These
can be any related link such as a HydroShare resource landing page, a compute
service such as JupyterHub, or a separate website such as R Shiny. An example
may have multiple launch options.

``` yaml
launch_options:
  - name: Open In HydroShare
    url: https://hydroshare.org/resource/[my-resource-id]
  - name: Run Application
    url: https://url-where-example-runs.html
```

#### HydroShare ID (optional)

A HydroShare resource identifier to use for gathering example metadata. If a
HydroShare resource identifier is provided, it will be used to collect, format,
and display metadata on the example landing page. Note, YAML elements `title`,
`description`, `author`, etc. will override any data obtained from HydroShare.

``` yaml
hydroshare:
    id: 3db192783bcb4599bab36d43fc3413db
```

### Authors (optional)

Authorship is typically obtained directly from HydroShare using the
`hydroshare id` parameter above. However, these data can be manually specified
within the configuration file following the pattern:

``` yaml
authors:
  - name: Tony Castronova
    url: https://hydroshare.org/user/11
    organization: CUAHSI email: my-email@cuahsi.org
  - name: Author 2
    url: https://personal-webpage/author2
    organization: some organization
    email: author2@some-organization.com
```

## Examples

### Referencing a HydroShare Resource

In the following example, most of the page metadata is obtained from HydroShare
using `hydroshare id`. Short titles and descriptions are provided to improve
the appearance of this example on the gallery page. Authorship is obtained
directly from HydroShare so there's no need to explicitly provide it here.

``` yaml
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
