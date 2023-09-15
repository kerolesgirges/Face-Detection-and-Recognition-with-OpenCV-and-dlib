# Face Detection and Recognition with OpenCV and dlib

## Overview

This Python script demonstrates real-time face detection, expansion, and recognition using OpenCV and the dlib library. It captures faces from a webcam feed, expands the detected face region, and saves unique faces to a specified directory.

## Dependencies

Make sure you have the following libraries installed:

- OpenCV (opencv-python)
- dlib
- face_recognition

You can install them using pip:

```shell
pip install opencv-python dlib face_recognition
```

## Usage

1. Clone this repository to your local machine.

2. Open a terminal and navigate to the directory containing the code.

3. Run the script using the following command:

```shell
python face_detection_recognition.py
```

4. A window will open, displaying the webcam feed. When a face is detected, it will be outlined with a green rectangle.

5. The script will expand the detected face region and save unique faces in the "captured_faces" directory. Each unique face will have a unique filename in the format `face_0.jpg`, `face_1.jpg`, and so on.

6. Press the 'q' key to exit the application.

## Configuration

You can configure the following parameters in the script:

- **expansion_factor**: Controls how much to expand the detected face region. Adjust this value to capture larger or smaller face regions.

- **minNeighbors**: Adjust this value for face detection sensitivity. Higher values result in fewer detections, while lower values may detect more faces but with potential false positives.

## License

This code is provided under the [MIT License](LICENSE).

## Author

keroles girges

## Acknowledgments

This script was inspired by various OpenCV and dlib face detection and recognition tutorials and examples.

