# Loading Caffe Models in [Py]Torch

## Torch

1. Install `loadcaffe`
    
```shell
luarocks install loadcaffe
```

2. Read the model into Torch. The `loadcaffe` library is smart enough to translate the caffe model to a valid torch model.

```lua
require 'loadcaffe'

model = loadcaffe.load('net.prototxt', 'weights.caffemodel')
```

3. Optionally save the model as a torch model for future use. 

```lua
torch.save("caffe_model.t7", model)
```


## PyTorch

1. Convert Caffe model to a Torch model as illustrated above and load it into pytorch

```python
from torch.utils.serialization import load_lua

caffe = load_lua('caffe_model.t7')
```

2. Get the corresponding model in Pytorch

```python
import torchvision.models as models
vgg19 = models.vgg19()
```

3. Get the state dictionary of the pytorch model. This is where we perform all the updates.

```python
state = vgg19.state_dict()
```

4. Get the Caffe model modules 

```python
caffe_modules = caffe.modules
```

5. Use the below script to get only the weight layers in the caffe model and load them accordingly into the state dictionary:

```python
weight_layers = [m for m in caffe_modules if 'weight' in dir(m)]

layer_count = 0

for idx, s in enumerate(state):
    if idx % 2 == 0:  # this is a weight key
        state[s] = weight_layers[layer_count].weight
    elif idx % 2 == 1:  # this is a bias key
        state[s] = weight_layers[layer_count].bias
        layer_count += 1
```

6. Load back the state dictionary into the model and you're good to go!

```python
vgg19.load_state_dict(state)
```
