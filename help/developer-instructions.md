# Developer Instructions

## Install and Prepare the Python Environment

*These development instructions consist of commands that should be executed in a
bash terminal.*

While there are several options for creating a Python environment, we recommend
using Anaconda. To install anaconda on MacOS, follow the instructions
[here](https://docs.anaconda.com/anaconda/install/mac-os/).

After installing and configuring Anaconda, create a new environment for the
gallery project. This environment will encapsulate all software dependencies.
We can create a new environment and install dependencies simultaneously using
the following command:

``` bash
conda env create -f environment.yml
```

After this command completes, you should have a Python environment with all the
Gallery dependencies installed in it. Before proceeding with the local build
steps (below), activate the environment with the following command.

``` bash
conda activate gallery
```

This will modify your terminal to look something like this:

``` bash
(gallery): ~$ 
```

## Local Development Instructions

### QuickStart
To assist with building the Gallery in a local setting, this project makes use
of a `Makefile`. Simply put, this enables us to run a series of build
commands/options using the `make` keyword.

To list all available options:

``` text
$ make help

Please use `make <target>' where <target> is one of
  html       builds standalone HTML files
  cache      builds standalone HTML files from cache whenever possible
  github     builds website ready to be pushed to GitHub
  rebuild    rebuilds the website in-place, without querying data from HydroShare
  clean      cleans all local build files

```

To build the gallery website for local development, run the following command:

``` text
$ make html 

...
...
The HTML pages are in source/_build/html.
Copying contentui stylesheet/javascript... done

Build finished. The HTML pages are in source/_build/html
```

This command requires an internet connection because it queries metadata from
HydroShare for some of the resources in the gallery. Once this command
completes, the website files are written to `source/_build/html`. To view the
gallery website you will need to start an http server using the following
command:

``` text
python -m http.server --directory source/_build/html 9000
```

Now you can navigate to `127.0.0.1:9000` in the web browser of your choice.

### Additional Development Functions

Since the Gallery is deployed on `github.io`, we need to put the production
files in a specific folder, i.e. `./docs`. The Makefile contains a helper
function to move these files into the correct location for you.

The following command will build the Gallery and then move files into the
correct location for publishing to GitHub pages:

``` text
make github
```

After this command completes, the Gallery can be redeployed to github.io by
invoking a `git push`.

To speed up compilation, metadata is cached locally between builds. To remove
these cached files run:

``` text
make clean
```
