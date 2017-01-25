# Caffe
[Official Installation Instructions](https://github.com/BVLC/caffe/)

## Ubuntu Installation

Follow all the instructions given [here](http://caffe.berkeleyvision.org/install_apt.html).

### HDF5

If you're using HDF5 layers, you need to perform some operations to allow Caffe to find the required header files and shared libraries:

- Modify `INCLUDE_DIRS` in `Makefile.config`

    
            INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial/

- Create the following symlinks to the shared object files:


            cd /usr/lib/x86_64-linux-gnu
            sudo ln -s libhdf5_serial.so.8.0.2 libhdf5.so
            sudo ln -s libhdf5_serial_hl.so.8.0.2 libhdf5_hl.so


### cuDNN

To install cuDNN, go to the [Nvidia CuDNN page](https://developer.nvidia.com/cudnn), register yourself and download the linux library (e.g. cuDNN v5.1 Library for Linux) for the appropriate CUDA version.

Now follow the below instructions:

1. Find the location of your CUDA install `which nvcc`.
2. Unzip the cuDNN tarball you downloaded above.
3. `cd` into the extracted folder.
4. Run the following commands:

        $ sudo cp -P include/cudnn.h /usr/local/cuda-8.0/include  # assuming you got /usr/local/cuda-8.0 from step 1
        $ sudo cp -P lib64/libcudnn* /usr/lib/x86_64-linux-gnu/
        $ sudo chmod a+r /usr/lib/x86_64-linux-gnu/libcudnn*

You should now be able to run `make` or `cmake` and see the cuDNN installation being picked up.
