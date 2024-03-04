<p align="center">
 <h1 align="center">AI MOUSE</h1>
</p>

## Introduction

Here is my python source code for AI MOUSE, with my code, you could: 
* **Run an app which you could control the computer mouse with your fingers (If you use laptop, your webcam will be used by default)**

## Camera app
In order to use this app, you need a pen (or any object) with blue, red or green color. When the pen (object) appears in front of camera, it will be catched and highlighted by an yellow circle. When you are ready for drawing, you need to press **space** button. When you want to stop drawing, press **space** again
Below is the demo by running the sript **camera_app.py**:
<p align="center">
  <img src="demo/quickdraw.gif" width=600><br/>
  <i>Camera app demo</i>
</p>

## Docker

For being convenient, I provide Dockerfile which could be used for running training as well as test phases

Assume that docker image's name is **ssd**. You already created an empty folder name **trained_models** for storing trained weights. Then you clone this repository and cd into it.

Build:

`docker build --network=host -t ssd .`

Run:

`docker run --rm -it -v path/to/your/coco:/coco -v path/to/trained_models:/trained_models --ipc=host --network=host ssd`
## How to use my code

Assume that at this step, you either already installed necessary libraries or you are inside docker container

Now, with my code, you can:

* **Train your model** by running `python -m torch.distributed.launch --nproc_per_node=NUM_GPUS_YOU_HAVE train.py --model [ssd|ssdlite] --batch-size [int] [--amp]`. You could stop or resume your training process whenever you want. For example, if you stop your training process after 10 epochs, the next time you run the training script, your training process will continue from epoch 10. mAP evaluation, by default, will be run at the end of each epoch. **Note**: By specifying **--amp** flag, your model will be trained with mixed precision (FP32 and FP16) instead of full precision (FP32) by default. Mixed precision training reduces gpu usage and therefore allows you train your model with bigger batch size while sacrificing negligible accuracy. More infomation could be found at [apex](https://github.com/NVIDIA/apex) and [pytorch](https://pytorch.org/docs/stable/notes/amp_examples.html).
* **Test your model for COCO dataset** by running `python test_dataset.py --pretrained_model path/to/trained_model`
* **Test your model for image** by running `python test_image.py --pretrained_model path/to/trained_model --input path/to/input/file --output path/to/output/file`
* **Test your model for video** by running `python test_video.py --pretrained_model path/to/trained_model --input path/to/input/file --output path/to/output/file`

