# Minsky Servers

The Minsky servers are a set of servers with GPU capabilities for running high performance computing experiments on (such as deep learning).

There are 8 servers which can be accessed by the URLs `minsky[0-7].cc.gatech.edu`. The credentials to access Minsky are your Georgia Tech username and password.

For example, to access Minsky 7, you can run something like below:

```shell
ssh varunagrawal@minsky7.cc.gatech.edu
```

>If you are part of a class that has access to Minsky, you should be able to log in directly. If you are a working on an independent research project with a professor, you will need to request Minsky access.

## Features

Each Minsky server has the following features:

1. 4 Nvidia Tesla K40m GPUs.
2. 257 GB of RAM
3. 2.2 TB Hard Drives
4. Ubuntu Linux 14.04.5 (trusty tahr)
5. Pre-configured Docker support
6. Python (2.7, 3.4, 3.5, 3.6)

## Working with Minsky

The recommended way to use Minsky is via [Docker](https://www.docker.com) containers. Since Minsky does not allow root access, installing tools, software and dependencies can be a slow (and sometimes painful) process. The best way to get around this is to use a Docker container which you have complete control over and has everything installed.

If you are unfamiliar with Docker, [this tutorial](http://training.play-with-docker.com/dev-landing/) is a great way to get started.

### Docker with GPU support

In order to access the GPU, you need to use [nvidia-docker](https://github.com/NVIDIA/nvidia-docker). The (nvidia-)docker daemons are already set up and ready to go. You need to be added to the Docker User group on Minsky in order to use docker on Minsky. Please send out a request to the Minsky admins in order to be added to the group.

> Docker already has plenty of base images with all the needed libraries and tools setup for your work. Please be sure to checkout Dockerhub for options.

#### Docker Shared Volumes
You can share a directory on your host with the docker container so that your process inside the container can write files to the host, to be used later (weight files for example). This shared directory is called a Volume in Docker parlance. 

Docker containers normally launch as root, thus any files written to the volume will be owned by root on the host and not you, making deleting or modifying them next to impossible. The way to ensure files written to volumes are owned by you is pass in the `--user=$USER` flag for the `nvidia-docker run` command. For example, the way to run a container called `sample-container` would be:

```shell
nvidia-docker run -it --user=$USER -v $(pwd):/home/src sample-container
```

When you exit the container, all the files written to the volume will be owned by `$USER` which is you.


### Python Alternative

If you are primarily using Python, you can setup a `virtualenv` and install all your dependencies and libraries to that in order to run your code. You do not need `sudo` access in order to set up a virtual environment for Python.

> NOTE: We do not support other forms of virtualization.

## Fair Usage

Since Minsky is a shared resource without any hard and fast rules and restrictions about its usage, you are requested to please be considerate of others when using Minsky. Hoarding multiple GPUs when unnecessary, occupying large HDD space for prolonged perionds or occupying GPUs on multiple Minsky servers will be highly frowned upon, unless prior notice has been provided.

For providing notice, if you are in a class, please use Piazza or whatever the notice board technology is being used for the class. If you are working with a professor on a project, please send out an email to the admins.


## Minsky Administrators

Since Minsky is owned and operated by multiple labs, below is a list of the labs and the point-of-contact from each lab. 

1. Eye Team (Dr. Irfan Essa and Dr. James Hays) - Varun Agrawal (varunagrawal@gatech.edu)
2. Computational Perception Lab (Dr. Jim Rehg) - Ahmad Humayun (ahumayun@gatech.edu)
3. Computer Vision Lab (Dr. Devi Parikh) - 
4. Machine Learning and Perception Lab (Dr. Dhruv Batra) - 

Please feel free to reach out to us in case you need any help.
