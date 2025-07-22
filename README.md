# vigdis-heimdall-v1

This repository contains a small prototype for controlling an ILDA laser scanner using a Helios DAC.
It currently provides a simple curses-based demo that renders a filled square which can be moved around
with the arrow keys.  The code is written for Python 3.



## Structure

- `Helios.py` – wrapper around the Helios DAC USB interface.  Provides the `HeliosDAC` class
  and `HeliosPoint` utility used to send frames to the DAC.
- `hershey.py` – lightweight Hershey font definitions used for text rendering and example shapes.
- `main.py` – demo application that uses `curses` to move a square on the laser projector.

## Requirements

- Python 3.10+
- `pyusb` for USB access to the DAC
- `numpy` and `matplotlib` for drawing utilities
- `curses` (built in on Linux/macOS)

Install the Python dependencies with:

```bash
pip install pyusb numpy matplotlib
```

## Usage

Connect the Helios DAC to your computer and run:

```bash
python3 main.py
```

Use the arrow keys to move the square, and press `q` to quit.

## Development

The project is still in an early prototype phase.  Source files can be edited directly and
reloaded by restarting the demo.  The repository now ignores compiled Python bytecode in
`__pycache__/`.

## TODO: Camera Tracking and Masking with YOLOv8

Future work will integrate a camera and object detection pipeline to allow the laser to track
objects in real time.  Planned tasks include:

1. **Camera capture** – grab frames from a webcam using `opencv-python`.
2. **YOLOv8 inference** – run detection on each frame using the Ultralytics `yolov8` model.
3. **Masking** – convert detected bounding boxes to masks in the projector's coordinate space.
4. **Calibration** – map camera coordinates to ILDA/Helios coordinates for accurate projection.
5. **Real-time control** – update the Helios frame queue to follow moving targets.
6. **Performance** – profile latency and optimise for smooth tracking.
7. **Testing** – unit tests and integration tests for the tracking pipeline.

