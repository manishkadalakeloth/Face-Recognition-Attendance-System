import cv2
import pandas as pd
import os
from datetime import datetime

# Create directories if they don't exist
os.makedirs('images', exist_ok=True)
os.makedirs('attendance', exist_ok=True)

# Load the Excel sheet or create one with headers if it doesn't exist
attendance_file = 'attendance/attendance.xlsx'

if not os.path.exists(attendance_file) or os.path.getsize(attendance_file) == 0:
    df_attendance = pd.DataFrame(columns=['Name', 'Date', 'Time'])
    df_attendance.to_excel(attendance_file, index=False)

# Function to mark attendance
def mark_attendance(name):
    df_attendance = pd.read_excel(attendance_file)
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    new_entry = pd.DataFrame({'Name': [name], 'Date': [date], 'Time': [time]})
    df_attendance = pd.concat([df_attendance, new_entry], ignore_index=True)
    df_attendance.to_excel(attendance_file, index=False)

# Initialize webcam
video_capture = cv2.VideoCapture(0)

# Provide absolute path to the Haar cascade
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

# Count for image capturing
count = 0

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangle around the faces and save images
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = frame[y:y + h, x:x + w]
        count += 1
        cv2.imwrite(f'images/user_{count}.jpg', face)
        mark_attendance(f"User_{count}")

    # Display the output
    cv2.imshow('Video', frame)

    # Break the loop on 'q' key press or after capturing 50 images
    if cv2.waitKey(1) & 0xFF == ord('q') or count >= 50:
        break

# Release the capture and close the window
video_capture.release()
cv2.destroyAllWindows()
