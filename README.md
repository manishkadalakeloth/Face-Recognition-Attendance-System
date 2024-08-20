# Face-Recognition-Attendance-System
The Face Recognition Attendance System is an automated solution designed to streamline the process of taking attendance in classrooms or workplaces. Using facial recognition technology, the system captures images from a webcam, identifies individuals by comparing their faces with a pre-stored database, and records their attendance in an Excel file.

# Features
1. Real-Time Face Detection: Utilizes the Haar Cascade classifier to detect faces in real-time from a live webcam feed.
2. Face Recognition: Matches detected faces with pre-stored images in a CSV file (face_names.csv) that links image filenames to corresponding names.
3. Automated Attendance Logging: Automatically logs recognized names, along with the date and time, into an Excel file (attendance.xlsx).
4. CSV Mapping: Easy updating of recognized individuals by modifying the face_names.csv file.

# Directory Structure
FaceRecognitionAttendanceSystem/
│
├── haarcascade_frontalface_default.xml  # Pre-trained XML classifier for face detection.
├── face_names.csv  # CSV file mapping image filenames to names.
├── main.py  # The main script for running the attendance system.
│
├── attendance/
│   └── attendance.xlsx  # Excel file where attendance is recorded.
│
└── images/  # Directory where captured face images are temporarily stored.

# Getting Started
Prerequisites
Python 3.x
OpenCV
Pandas
NumPy

# Installation
1. Clone the repository:
git clone https://github.com/manishkadalakeloth/FaceRecognitionAttendanceSystem.git

2. Navigate to the project directory:
cd FaceRecognitionAttendanceSystem

3. Install the required dependencies:
pip install -r requirements.txt

# Running the Project
1. Ensure that the haarcascade_frontalface_default.xml file is in the same directory as main.py.
2. Add new faces and their corresponding names to the face_names.csv file.
3. Run the project:
   python main.py
The system will start capturing images from the webcam, detect faces, and log attendance in the attendance.xlsx file.

# Usage
Updating Faces: To add a new face, save the image in the images/ directory, then add the image filename and corresponding name to the face_names.csv file.
Attendance Records: Check the attendance.xlsx file in the attendance/ directory for recorded attendance.

# Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

# License
This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
