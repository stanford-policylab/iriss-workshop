IRiSS 2019 Summer Workshop: Introduction to Python
===

# 0. Python

Python is one of the most widely used programming languages in the world.
Some of the world's most widely-used websites and applications are built
largely in Python, such as Instagram, Reddit, Dropbox, and YouTube.
Python is also widely used in scientific circles for numerical computing and
data visualization.

## Why Python?

Python hits a sweetspot balancing power and ease-of-use.
Python code is more similar to a human language (viz., English) than other programming languages,
so it's easy for beginners to be productive without stumbling too much over the syntax.
At the same time, Python is still a fully-featured language, providing the tools to access lower-level system interfaces and build complex applications.

But what makes Python a uniquely powerful tool in so many circumstances is the ecosystem of modules that exist to extend the core language.
First, the standard libary (included when you install Python) contains tools to solve all sorts of common tasks: sorting algorithms, combinations, regular expressions, text encoding, cryptography, and lots more.
But also, across both science and industry, developers have built state-of-the-art libraries and frameworks for a variety of problem domains. To name just a few:

 * `numpy` - high-performance numerical computing
 * `scipy` - builds on `numpy` to implement a number of algorithms and techniques
 * `nltk` - natural language processing algorithms, models, etc.
 * `spacy` - high-performance NLP
 * `tensorflow` - machine learning
 * `flask` - build websites and APIs
 * `scrapy` - scrape websites

In general, most services you will want to integrate with---be it Facebook's API to pull data, Twilio's API to send text messages, Google's Cloud APIs to do pretty much anything---will provide a library to do this in Python.

## How do I ... Python?

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
