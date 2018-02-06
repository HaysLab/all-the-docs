# Python

Most deep learning frameworks have support for the Python programming language, especially the more popular ones such as TensorFlow and PyTorch.

In this tutorial, we will show you how to use virtual environments (venvs) to get started with your project. As an illustrative example, we use CIFAR-10 classification with PyTorch.

## Preparing The Environment

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

## Installing Packages

Once you have set up and activated your venv, installing packages is very easy. For example, you can install `numpy` like this

```shell
pip install numpy
```

All the packages are installed to your venv and are directly accessible from the Python runtime installed in the venv.

Be sure to use a `requirements.txt` file to keep track of your installed packages. To generate one, you can run

```shell
pip freeze -l > requirements.txt
```

Let's install all the packages we need for running our code:

```shell
pip3 install http://download.pytorch.org/whl/cu80/torch-0.3.0.post4-cp36-cp36m-linux_x86_64.whl 
pip3 install torchvision
pip install tqdm  # note how you can use pip or pip3!
```

## Getting the Data

`torchvision` has utilities to download popular datasets automatically. The `main.py` file has a function `get_dataset()` that downloads both the training and test sets of the CIFAR-10 dataset.

## Development

Now that you have your venv setup, once you activate it as detailed above, you can develop your project just like any regular Python project.

Let us run our program and see what we get:

```
python main.py
```

The result should be the test loss and the accuracy of the model on the CIFAR-10 test set.


## Conclusion

At this point, you have nearly everything you need to get started with Minsky. Since you have full control over the venv, you can install and remove packages as you please without afffecting other's environments, and easier maintenance.
