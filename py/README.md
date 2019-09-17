IRiSS 2019 Summer Workshop: Introduction to Python
===

This guide will help you get oriented before attending the Python workshop.
After reading, you should have some idea of what both `Python` and `JupyterLab` are, why you are learning them, and have them installed and working on your computer.

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
 * `pandas` - data manipulation and analysis
 * `nltk` - natural language processing algorithms, models, etc.
 * `spacy` - high-performance NLP
 * `tensorflow` and `torch` - deep learning
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
If you are using Windows, please ensure that when you install Python3, you check
the box to include Python in your path.

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

### Installing Python3 kernel

Ensure that the Python3 kernel is available by running the following in a terminal:

```
python3 -m pip install ipykernel
python3 -m ipykernel install --user
```

This lets you use Python3 when running JupyterLab.

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

# 2. Running JupyterLab on the cloud

__NOTE:__ It is only necessary to follow these instructions if you were unable
to install Python locally on your computer.

## Get set up on GitHub

Begin by creating a GitHub account (if you do not already have one) by clicking
[here](https://github.com). (Be sure to click through _all the way_ to the end
of the account creation process.)

Then, have one of the instructors add you to the `@iriss-workshop` organization.
There are two ways to do this:
1. Log into the Stanford Computational Social Science workspace on Slack by
   clicking [here](https://stanford-css.slack.com). Then, once Slack has opened
   up, press <kbd>ctrl</kbd> + <kbd>k</kbd> and type `#r-py-workshop`. Click on
   the (only) result to join the `#r-py-workshop` channel, and then post your
   _GitHub_ username.
  * __NOTE:__ If you do not have a SUNet ID, this option will not work.
2. Flag one of the instructors walking around and have them add you to the
   `@iriss-workshop` organization manually.

Lastly, once you've been added to `@iriss-workshop`, you should receive an email
at the email address you used to register for your GitHub account. This email
will be an invitation to join `@iriss-workshop`. Click through the links all the
way to the end to ensure that you've accepted the invitation.

## Logging into the cloud

Once you've been added to the `@iriss-workshop`, visit
[scpl-jupyter.org](https://scpl-jupyter.org), and click `Sign in with GitHub`. 

## Troubleshooting

If you get error `403 - Forbidden` when you try to log into the cloud, one of
two things has probably happened:
1. The instructors haven't added you to the `@iriss-workshop` group. If you
   haven't received an email from GitHub asking you to join the
   `@iriss-workshop` group, this is almost certainly what happened. Just be
   patient, and, if necessary, repost your username in the Slack channel.
2. You haven't accepted an invitation to join the `@iriss-workshop` group. Make
   sure you click through the link contained in the invitation email _all the
   way_ to the end.
