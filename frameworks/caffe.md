# Caffe
[Official Installation Instructions](https://github.com/BVLC/caffe/)

## Ubuntu Installation

Follow all the instructions given [here](http://caffe.berkeleyvision.org/install_apt.html).

### Installing with Anaconda

- Install Anaconda Python
- `conda install` the required libraries
    - libgcc
- You will have to install OpenCV [2|3] independently since Caffe has trouble with finding OpenCV via Anaconda.
    - Be sure to turn the flags for TIFF and JPEG on during the cmake build.
- Update the Makefile.config to point to Anaconda
- Compile Caffe as usual 
    
        make all -j`nproc`

### HDF5

If you're using HDF5 layers, you need to perform some operations to allow Caffe to find the required header files and shared libraries:

- Modify `INCLUDE_DIRS` in `Makefile.config`

    
        INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial/

- Create the following symlinks to the shared object files:


        cd /usr/lib/x86_64-linux-gnu
        sudo ln -s libhdf5_serial.so.8.0.2 libhdf5.so
        sudo ln -s libhdf5_serial_hl.so.8.0.2 libhdf5_hl.so

