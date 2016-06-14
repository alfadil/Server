> **Warning:** A work in progress.

[![Build](https://travis-ci.org/Sindan/Server.svg?branch=master)](https://travis-ci.org/Sindan/Server) 
[![Health](https://landscape.io/github/Sindan/Server/master/landscape.svg?style=flat)](https://landscape.io/github/Sindan/Server/master)
[![Coverage](https://codecov.io/gh/Sindan/Server/branch/master/graph/badge.svg)](https://codecov.io/gh/Sindan/Server)


# Sindan

Sindan is an Agile project management software with focus on the following:

  - Simplicity, and easy to use.
  - Easily to customize to fit your project needs.
  - Easily to integrate with the tools you already use.

### Getting Started

You will need [Python](https://python.org)>= 3.4 to work with Sindan.

Check the repository using `git` command

```
$ git clone https://github.com/Sindan/Sindan.git
$ cd Sindan
```

Create a virtualenv, it's highly recommended.

```
$ virtualenv sindenv
```

Switch to the virtualenv

```
$ source sindenv/bin/activate
```

Install the required dependencies using `pip`

```
$ pip install -r requirements/dev.txt
```

To perform testing simply run

```
$ py.test
```

### License

![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)
