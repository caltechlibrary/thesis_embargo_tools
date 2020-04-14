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
These tools are used to marshal those requests among committee 
members and complete the review process.


Installation
------------

You need Python 3.8 available to run the tools. Additionally
you will need to be familair with create folders and files on your
own computer, how to work in your email environment including
downloading email messages as plain text files,
work with Excel spreadsheets, use a web browser and how to "unzip"
the tools in this project to make them available on your computer.
Finally you'll need to have [Box](https://www.imss.caltech.edu/box) 
installed and available on your machine.

If you don't have Python 3.8 and `pip` on your system the recommended
way to get it installed is to install [Miniconda](https://docs.conda.io/en/latest/miniconda.html). If that
is not available see [INSTALL-Python3.md](INSTALL-Python3.md) 

### Installing additional Python packages

This project depends the following pacakges which may need
to be installed on your computer.

+ [xlsxwriter](https://xlsxwriter.readthedocs.io/)

```
    python3 -m pip install XlsxWrite
```


Usage
-----

+ Use the stacks form to generate the request
+ When you receive the request in email, download the email message
+ Create an appropriate folder structure for the students request
+ Use [generate_committee_form.py](docs/generate_committee_form.md) to generate the Excel file that will be placed in the Box folder for the student's request.
    + this program will generate two documents
        + an Excel file the committee will complete for the review process
        + a plain text file with an example email message to be sent to the committee members
+ Forward link to the Excel file used for the committee form using the plain text committee email message


License
-------

Software produced by the Caltech Library is Copyright (C) 2020, Caltech.  This software is freely distributed under a BSD/MIT type license.  Please see the [LICENSE](LICENSE) file for more information.


Acknowledgments
---------------

This work was funded by the California Institute of Technology Library.

(If this work was also supported by other organizations, acknowledge them here.  In addition, if your work relies on software libraries, or was inspired by looking at other work, it is appropriate to acknowledge this intellectual debt too.)

<div align="center">
  <br>
  <a href="https://www.caltech.edu">
    <img width="100" height="100" src=".graphics/caltech-round.png">
  </a>
</div>
