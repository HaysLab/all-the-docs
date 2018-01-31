# Minsky Tutorial

This document illustrates different ways you can use the Minsky cluster to run deep learning algorithms (or anything that uses a GPU).

## Python

Most deep learning frameworks have support for the Python programming language, especially the more popular ones such as TensorFlow and PyTorch.

This guide will use PyTorch as an illustrative example.

#### Preparing The Environment

We use [virtualenv](https://virtualenv.pypa.io/en/stable/) to create virtual environments (venv) in your project directory. With a venv, you can directly install packages to the venv without needing admin access, thus enabling much greater control over your project environment.

> If you are familiar with [Pipenv](pipenv.org), it is recommended to use that over `virtualenv`.

To create the venv, you can run 

```shell
virtualenv -p python3.6 venv
```

The `-p` flag specifies which version of Python to use, and the last argument `venv` specifies the name of the directory to which to install the venv.

> Using Python3 is HIGHLY RECOMMENDED.

Once the venv is set up, you can run the following to activate it

```shell
source venv/bin/activate
```

To exit the venv, run

```shell
deactivate
```

#### Installing Packages

Once you have set up and activated your venv, installing packages is very easy. For example, you can install `numpy` like this

```shell
pip install numpy
```

All the packages are installed to your venv and are directly accessible from the Python runtime installed in the venv.

Be sure to use a `requirements.txt` file to keep track of your installed packages. To generate one, you can run

```shell
pip freeze -l > requirements.txt
```

#### Development

Now that you have your venv setup, once you activate it as detailed above, you can develop your project just like any regular Python project.


## Docker

> We assume you are comfortable with docker concepts and with  nvidia-docker commands.

In some cases, the tools you are using may have dependencies that are not supported in Python (such as Torch7). In this case, managing your workspace can be difficult without `sudo` access. 

The best way to tackle this problem is with [Docker](https://www.docker.com).

#### Generating a Dockerfile

#### Getting Started

#### Running The Container
