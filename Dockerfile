FROM dockerkawa0620/mediapipe:latest

RUN pip install pyautogui mouseinfo python-xlib

COPY AI_MOUSE.py /AI_MOUSE.py
