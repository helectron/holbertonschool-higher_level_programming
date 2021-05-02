# Python - Hello, World
Playing with Python. Taking advantage of the fact that in this high-level language there are ten different ways to do the same thing


## General concepts
The Zen of Python
How to print text and variables using print
How to use strings
What are indexing and slicing in Python

## PEP 8 -- Style Guide for Python Code
The code use the PEP 8 style (version 1.7.*)

## Python Scripts
All the files are interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)

```python
#!/usr/bin/python3
```

```bash
#!/bin/bash
```

## Some precisions
I used emacs as an editor.

All programs and functions are compiled with gcc 4.8.4 using the flags -Wall -Werror -Wextra and -pedantic

The code used the Betty style. It will be checked using betty-style.pl and betty-doc.pl

There is no use of global variables

The prototypes of all the functions are included in your header file called lists.h

## Install PEP8
Pycodestyle is now the new standard of Python style code, but at school we will use PEP8, version 1.7.* Pycodestyle is based on pep8. The hardest part now is to install it for Python 3:

## Regular Ubuntu 14.04 install
```bash
$ sudo apt-get install python3-pep8
```

## Using Pip3
Install Pip3
```bash
$ sudo apt-get install python3-pip
```

## Install Pep8
```bash
$ sudo apt-get install python3-pip
$ sudo pip3 install -Iv pep8==1.7.0
```

-> Make sure you have the right version

```bash
$ pep8 --version
1.7.0
$
```

Finally, if you can’t make it work, please use the “container-on-demand” tool to “PEP8” your files in a pre-configured container.

:+1: :sparkles: :camel: :tada:
:rocket: :metal: :octocat: 