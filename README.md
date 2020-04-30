Thesis Embargo Tools
=====================================================

This is a small collection of tools for internal review and processing 
of Thesis embargo requests.

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg?style=flat-square)](https://choosealicense.com/licenses/bsd-3-clause)
[![Latest release](https://img.shields.io/github/v/release/caltechlibrary/template.svg?style=flat-square&color=b44e88)](https://github.com/caltechlibrary/thesis_embargo_tools/releases)


Table of contents
-----------------

* [Introduction](#introduction)
* [Installation](#installation)
* [Usage](#usage)
* [License](#license)
* [Acknowledgments](#authors-and-acknowledgments)


Introduction
------------

There is a committee review process for embargoing Caltech Thesis.
These tools generate the forms needed for the approval process.


Installation
------------

### Python Install

You need to have Python 3.7 on your machine
([Miniconda](https://docs.conda.io/en/latest/miniconda.html) is a great
installation option).  Test whether you have python installed by opening a terminal or
anaconda prompt window and typing `python -V`, which should print version 3.7
or greater.

### Clone thesis_embargo_tools

It's best to download this software using git.  To install git, type
`conda install git` in your terminal or anaconda prompt window.  Then find where you
want the thesis_embargo_tools folder to live on your computer in File Explorer or Finder
(This could be the Desktop or Documents folder, for example).  Type `cd `
in anaconda prompt or terminal and drag the location from the file browser into
the terminal window.  The path to the location
will show up, so your terminal will show a command like
`cd /Users/tmorrell/Desktop`.  Hit enter.  Then type
`git clone https://github.com/caltechlibrary/thesis_embargo_tools.git`. Once you
hit enter you'll see an thesis_embargo_tools folder.  Type `cd thesis_embargo_tools`

### Install

Now that you're in the thesis_embargo_tools folder, type `pip install .`

### Updates

To update the script, type `git pull`

Usage
-----

+ Use the stacks form to generate the request
+ When you receive the request in email, download the email message and save it
to the thesis_embargo_tools folder
+ Type `python generate_committee_docs.py stacks_email.eml xlsx_filename.xlsx`,
providing the name of the email message you saved earlier and the desired
output file name


License
-------

Software produced by the Caltech Library is Copyright (C) 2020, Caltech.  This software is freely distributed under a BSD/MIT type license.  Please see the [LICENSE](LICENSE) file for more information.


Acknowledgments
---------------

This work was funded by the California Institute of Technology Library.

<div align="center">
  <br>
  <a href="https://www.caltech.edu">
    <img width="100" height="100" src=".graphics/caltech-round.png">
  </a>
</div>
