# Minsky Tutorial

This document illustrates different ways you can use the Minsky cluster to run deep learning algorithms (or anything that uses a GPU).

## Prerequisites

This tutorial assumes a few things.

1. You are familiar and comfortable using the terminal in a Unix-like environment. Minsky does not offer GUI or Windows support.
2. Your project is under source control (such as git) that you can use to push changes to the minsky cluster in a clean way.
3. You are familiar with Python at a level more than beginner.
4. You are comfortable with using Docker if you intend to use Docker containers.

## Python

Most deep learning frameworks have support for the Python programming language, especially the more popular ones such as TensorFlow and PyTorch.

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
e mean to learn one network with multiple outputs for detection at diffeGPU
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

> We assume you are comfortable with docker concepts and with docker commands.

In some cases, the tools you are using may have dependencies that are not supported in Python (such as Torch7). In this case, managing your workspace can be difficult without `sudo` access. 

The best way to tackle this problem is with [Docker](https://www.docker.com).

> NOTE you need to be added to the Docker group on Minsky so that you can use Docker without `sudo` privileges. Please contact the admins of Minsky (given in the README) in order to be added.

In order to use the GPU(s) in Minsky, we will be using [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) to run our docker commands. `nvidia-docker` is Nvidia's wrapper over Docker that allows docker containers to use the GPU as if it were just another resource available to it.

There is no learning curve to `nvidia-docker`, all you need to do is replace `docker` in the shell command with `nvidia-docker` where needed.

#### Generating a Dockerfile

To get started with a docker container, you need the blueprint of the container, also known as the Dockerfile.

The Dockerfile is like any other Dockerfile that is used for the task you wish to undertake. For instance, a Deep Learning oriented Dockerfile will specify a Deep Learning framework be installed. You may wish to add some extra commands in the Dockerfile to customize it for your objective.

#### Getting Started

`nvidia-docker` has already been installed on each server of the Minsky cluster.

All you need to do is clone your code repository to a directory in your home path. The code repo should have the Dockerfile with it as well.

Assuming you are in the code directory for your project, you can run the following commands to set up your container image. We assume the container name is `project`.

```shell
# Build the container
nvidia-docker build -t project:latest .
```

At this point, if you run `docker images`, you should see your docker image in the list.

#### Running The Container

Now that we have built the container image, we can run the container very easily.

If you aren't, you should use Docker Volumes in order to share disk space between the server and your container. This way, any data you save to your container (such as models or results) will be synced to the server and you won't lose them accidentally. Note that you need to pass the `--user` flag to your container so that the saved data are owned by you and not by root. Passing in your UID also makes container monitoring easier.

```shell
# Run the container with a shared volume
nvidia-docker run -it --user=$(id -u) -v $(pwd):/home/src project
```

The `-it` flags tells docker to open up an interactive terminal prompt for you. The `-v` flag specifies a Docker Volume so that your project directory is loaded onto the container, and the `--user` flag ensures any files created within the container and saved to a Volume is owned by you.

A new terminal prompt should appear before you. You can now run your code like normal as if you had your own desktop.

You can quit the container by typing `exit` or hitting `Ctrl+d`. Once your code has finished running and you're done with the container, be sure to clean it up with

```shell
# stop the container if needed
docker stop project

docker rm project
```

# Conclusion
At this point, you should be ready to go with your project on Minsky, either via Python venv or Docker! Please feel free to contact us in case you have issues or questions.
