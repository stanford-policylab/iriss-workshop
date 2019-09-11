IRiSS 2019 Summer Workshop: Introduction to R
===

This guide will help you get oriented before attending the R workshop.
After reading, you should have some idea of what `JupyterLab`, `R`, and `tidyverse` are, why you are learning them, and have them installed and working on your computer.

# 0. Python

In order to use `JupyerLab`, you need to have Python installed on your computer.
You will not be learning anything about how to use Python during this workshop.

## Checking installation

You might have Python installed already.
First, open up a terminal on your computer.
On OSX and Linux open the `terminal` application.
On Windows, run `Command Prompt`.

Now you should check both that you have Python installed, and that it is
version 3. In your terminal, type the following command and press return:

```
python --version
```

You should see something like:

```
jnu@dagmar:~> python --version
Python 3.7.1
```

### Wrong version

If you see any version of Python 3, (whether 3.7.1 or 3.6.0 or whatever), you
will be fine for this tutorial.

If that command showed you Python2 instead of Python3, try running:

```
python3 --version
```

If that works, just substitute `python3` for `python` when you are running
commands in this guide.

### Missing Python

If you don't have Python3 installed, you can download and install the latest release here:
https://www.python.org/downloads/

# 1. JupyterLab

Throughout this workshop we will be writing and running code in a tool called
[JupyterLab](https://jupyterlab.readthedocs.io/en/stable/index.html).

The Jupyter Project provides software to run Python and R in a visual, interactive environment.
Contrast this approach with the main alternative paradigm, which is to write code in text files and run all of it through the command line.
That approach works well for developing complete standalone applications.
For most scientific work, it's more convenient to run lines of code individually (or in small batches); to tweak parameters, adjust plots, etc.

Jupyter is designed around the concept of a "notebook."
A notebook lets you write code in small chunks called cells, and run the cells to see the output.
Jupyter displays the output of these commands conveniently, whether as plots or tables or something else.
You can also write plain text (and not code) in cells, which is convenient for writing notes or instructions in a notebook you will share with collaborators, students, etc.

You will learn more about how to interact with the Jupyter notebook throughout the day.

## Installation

The easiest way to install JupyterLab is using Python's built-in package
manager, `pip`.

Try running:

```
python -m pip install jupyterlab
```

If that fails, try following more detailed instructions here:
https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html#pip

## Running

Now in your terminal run the following command by typing it and pressing return:

```
jupyter lab
```

This will start running a web server that serves the JupyterLab application.
This command should automatically open your default web browser to the JupyterLab page.

If you do not see JupyterLab open, read the output of the command you ran in the terminal.
If Jupyter started correctly, it should have printed to the screen the URL you can use to access Jupyter.

**NOTE** Jupyter is now running locally on your computer; it is only visible to you. Nobody else can see your copy of Jupyter.

# 2. R

## Installation

To install the latest version of `R` on your computer, go to https://cloud.r-project.org/ and follow the instructions to download and install `R` for your platform.

## Using R with JupyterLab

In order to use `R` with JupyterLab, you need to install the `IRkernel` package.

In a terminal (either `Command Prompt` on Windows or `terminal` on OSX/Linux), type `R` and press enter to enter the interactive `R` shell.

Follow the instructions here to install the `IRkernel`: https://irkernel.github.io/installation/

**NOTE** When you run the install command, you may be asked to choose a mirror. You should choose a location that is geographically close to you (such as CA-1, which is in Berkeley).

Now when you start JupyterLab with the `jupyter lab` command, you should see the option to create a notebook with the `R` kernel.

## Installing tidyverse

The tidyverse is a collection of powerful libraries for working with data.
These tools make common data manipulation and visualization tasks easy.

To install, open the interactive `R` shell again and run:

```
install.packages("tidyverse")
```
