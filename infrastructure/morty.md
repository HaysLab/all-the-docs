# Morty Server

Below you will find all the documentation regarding the server named `Morty` used by HaysLab.

<a href="https://en.wikipedia.org/wiki/Rick_and_Morty" target="_blank"><img src="https://github.com/HaysLab/all-the-docs/blob/master/images/Morty.png" width="100px" height="100px" /></a>

## Table of Contents
- [Getting Access](#getting-access)
- [Remote Login](#remote-login)
- [Configuration](#configuration)
- [Available Software](#available-software)

## Getting Access

In order to get access to Morty and use its Rick-powered capabilities, please contact [Dr. James Hays](http://www.cc.gatech.edu/~hays/) for permission. He will also be able to direct you to the sysadmin for Morty who can get you setup.

## Remote Login

To log in to Morty remotely, you can `ssh` in using the DNS: `morty.cc.gt.atl.ga.us`

Be sure to prepend your username to the DNS, e.g. `hayslab@morty.cc.gt.atl.ga.us` 

## Configuration

Morty has the following configuration:

- CPU: i7-6900K
- Motherboard: ASUS X99-A II (4 PCI express slots)
- Memory: 64GB
- SSD: 480GB
- Hard Drive: 3TB
- Power supply: 850W
- GPUs in SLI:
  1. Nvidia Titan XP
  2. Nvidia Titan X

## Available Software

Below is a list of all the available software on Morty. If you need something installed, please contact the sysadmin before installing it, and please submit a Pull Request to update this doc.

Docker is HIGHLY RECOMMENDED!

- Python 2.7
- Python 3.5
- CUDA 8.0
- cuDNN 5.1
- Docker 1.13.0
- Caffe
- Torch
- Tensorflow 0.12.1
