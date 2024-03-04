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


## Experiments:

For each class, I take the first 10000 images, and then split them to training and test sets with ratio 8:2. The training/test loss/accuracy curves for the experiment are shown below:

<img src="demo/loss_accuracy_curves.png" width="800"> 

## Requirements

* **python 3.6**
* **cv2**
* **pytorch** 
* **numpy**
