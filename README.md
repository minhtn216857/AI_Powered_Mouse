<p align="center">
 <h1 align="center">AI MOUSE</h1>
</p>

## Introduction

Here is my python source code for AI MOUSE, with my code, you could: 
* **Run an app which you could control the computer mouse with your fingers (If you use laptop, your webcam will be used by default)**

## AI Mouse app
In order to use this app, you must raise a hand (object) appears in front of camera:
- Using a index finger to move the computer mouse around the screen
- Using a thumb touches a middle finger to represent a button click
When you want to stop my app, press **space** 
Below is the demo by running the sript **AI_MOUSE.py**:
(Because when recording video the mouse has an error of staying still, I will fix the video demo soon)
<p align="center">
  <img src="demo/quickdraw.gif" width=600><br/>
  <i>AI Mouse app demo</i>
</p>

## Docker

For being convenient, I provide Dockerfile which could be used for running my python code

Build:

`docker build -t ai-mouse .`

Run:

`docker run --rm -it ai-mouse bash`

## How to use my code

Assume that at this step, you either already installed necessary libraries or you are inside docker container
And now, you can run my app

