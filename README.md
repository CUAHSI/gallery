# CUAHSI Compute Gallery
A community gallery of code and web applications that run in the CUAHSI Cloud.


## Conda environment

```
$ conda env create -f environment.yml
```

## Build Instructions

To list all options: 

```
$ make help
```

Build in development mode: 

```
$ make html 
```

Build for publishing to GitHub pages:

```
$ make github
```

Cleaning

```
$ make clean
```

## How to add an Example to the Gallery

### 1. Fork this repository

### 2. Create a directory

Your directory should be created within a subdirectory of `source/gallery`. The subdirectory you choose is dependent on the example and will define where it is displayed within the category. For example, a instructional example that demonstrates using the Python Pandas library for data science application would be located in:

```
- source
  - gallery
    - Python
      - Instructional
        - <My Example>
```

### 3. Add a Thumbnail

Add a thumbnail for your example which will be displayed in the gallery, e.g. `thumbnail.png`.

### 4. Add code

Create a directory for your code and/or notebooks (e.g. notebooks) and add all of your code here.

### 5. Create the configuration file

Create a file called `conf.yaml` to define the metadata associated with your example. Note, `code_path` and `thumbnail` must match the path/name defined in previous steps.  An example is shown below:

`conf.yaml`
```
hydroshare:
  id: 3db192783bcb4599bab36d43fc3413db
code_path: ./notebooks
thumbnail: ./thumbnail.png
launch_options:
  - name: Open In HydroShare
    url: https://hydroshare.org/resource/3db192783bcb4599bab36d43fc3413d
```

### 6. Create a Pull Request

Create a PR to merge your example into the Gallery. 

