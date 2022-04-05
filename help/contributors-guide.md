# Guide for Contributors

This page explains how to add an example to the CUAHSI Gallery. The sections
below provide a step-by-step guide.

## 1. Fork this repository

## 2. Create a directory for your example

All gallery content follows a consistent directory structure;
`Root/Sub-Gallery/Category/Example`, where

- `Root` is the root directory of the gallery, i.e. `source/gallery`
- `Sub-Gallery` is a grouping categories around a programming language or
  technology, e.g. `Python`, `R`, `ShinyR`.
- `Category` is a grouping of examples around a similar theme or topic, e.g.
  `Instructional`, `Research`.
- `Example` is a directory containing the configuration and supporting files
  for a single example. The name of the example folder should be lowercase,
  self-descriptive, and contain no spaces.

All content within the Gallery must must follow the pattern. The category and
sub-gallery that you choose is dependent on the example together define where
the example is displayed on the webpage. While, new sub-galleries and
categories can be created, contributors are encouraged to use existing ones
wherever possible. For example, a instructional notebook that demonstrates
using the Python Pandas library for a data science application would be located
in:

``` text
- source
  - gallery
    - Python
      - Instructional
        - <title-of-my-example>
```

### Directory Structure

After creating the directory which will hold your example, populated it with
the following files.

1. `conf.yaml`: a yaml configuration file that is used to populate the metadata
   for your example on the website. The contents of this file are described in
   detail HERE.

2. A thumbnail image that will be displayed in the gallery, e.g.
   `thumbnail.png`. Use a eye-catching and visually appeal (but relevant) image
   that gives a preview of example results.

3. A directory for code, data, and/or notebooks that will be rendered on the
   page, e.g. `/notebooks`. Place any relevant content for your example in this
   directory, it will be referenced in the configuration file.

### Build the Gallery

Build the gallery on your local machine by following the instructions HERE.
Once everything is appearing as expected, proceed to the next step.

### Merge your Example

Create a Pull Request to merge your code into the CUAHSI/Gallery repository.
Once your contributions have been reviewed they will be merged and be made
publicly available on the gallery website. Note, you may be asked to make
changes prior to your work being merged.

