# Nvidia CUDA

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
