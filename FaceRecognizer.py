# import cv2 as cv
# import numpy as np
# import mediapipe as mp
#
# # Initialize drawing and face detection specifications
# mp_drawing = mp.solutions.drawing_utils
# mp_face_detection = mp.solutions.face_detection
#
# # Load the trained face recognition model (replace with your model path)
# face_recognizer = cv.face.LBPHFaceRecognizer_create()
# face_recognizer.read('face_trained.yml')
#
# # Define labels (replace with your actual labels)
# people = ['100','101']
# # Start video capture from webcam
# cap = cv.VideoCapture(0)
#
# with mp_face_detection.FaceDetection(
#     min_detection_confidence=0.5, model_selection=0
# ) as face_detection:
#     while True:
#         success, image = cap.read()
#         if not success:
#             print("Ignoring empty camera frame.")
#             # If loading image fails, exit the loop
#             continue
#
#         # Flip the image horizontally to correct the mirroring effect
#         image = cv.flip(image, 1)
#
#         # Convert BGR image to RGB for MediaPipe processing
#         image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
#
#         # Perform face detection on the frame
#         results = face_detection.process(image_rgb)
#
#         # Process detected faces
#         if results.detections:
#             for detection in results.detections:
#                 # Extract face landmarks (bounding box)
#                 xmin = int(detection.location_data.relative_bounding_box.xmin * image.shape[1])
#                 ymin = int(detection.location_data.relative_bounding_box.ymin * image.shape[0])
#                 width = int(detection.location_data.relative_bounding_box.width * image.shape[1])
#                 height = int(detection.location_data.relative_bounding_box.height * image.shape[0])
#
#                 # Extract the face ROI (Region of Interest)
#                 face_roi = image[ymin:ymin + height, xmin:xmin + width]
#                 gray = cv.cvtColor(face_roi, cv.COLOR_BGR2GRAY)
#
#                 # Predict label and confidence
#                 label, confidence = face_recognizer.predict(gray)
#
#                 # Display results
#                 print(f'Label = {people[label]} with a confidence of {confidence}')
#                 cv.putText(image, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0),
#                            thickness=2)
#                 cv.rectangle(image, (xmin, ymin), (xmin + width, ymin + height), (0, 255, 0), thickness=2)
#
#         # Display the processed frame
#         cv.imshow('Real-time Face Recognition', image)
#
#         # Exit on 'q' key press
#         if cv.waitKey(5) & 0xFF == ord('q'):
#             break
#
# # Release resources
# cap.release()
# cv.destroyAllWindows()
#
# import cv2 as cv
# import numpy as np
# import mediapipe as mp
#
# # Initialize drawing and face detection specifications
# mp_drawing = mp.solutions.drawing_utils
# mp_face_detection = mp.solutions.face_detection
#
# # Load the trained face recognition model (replace with your model path)
# face_recognizer = cv.face.LBPHFaceRecognizer_create()
# face_recognizer.read('face_trained.yml')
#
# # Define labels (replace with your actual labels)
# people = ['100', '101']
# # Start video capture from webcam
# cap = cv.VideoCapture(0)
#
# with mp_face_detection.FaceDetection(
#     min_detection_confidence=0.5, model_selection=0
# ) as face_detection:
#     while True:
#         success, image = cap.read()
#         if not success:
#             print("Ignoring empty camera frame.")
#             # If loading image fails, exit the loop
#             continue
#
#         # Flip the image horizontally to correct the mirroring effect
#         image = cv.flip(image, 1)
#
#         # Convert BGR image to RGB for MediaPipe processing
#         image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
#
#         # Perform face detection on the frame
#         results = face_detection.process(image_rgb)
#
#         # Process detected faces
#         if results.detections:
#             for detection in results.detections:
#                 # Extract face landmarks (bounding box)
#                 xmin = int(detection.location_data.relative_bounding_box.xmin * image.shape[1])
#                 ymin = int(detection.location_data.relative_bounding_box.ymin * image.shape[0])
#                 width = int(detection.location_data.relative_bounding_box.width * image.shape[1])
#                 height = int(detection.location_data.relative_bounding_box.height * image.shape[0])
#
#                 # Extract the face ROI (Region of Interest)
#                 face_roi = image[ymin:ymin + height, xmin:xmin + width]
#                 gray = cv.cvtColor(face_roi, cv.COLOR_BGR2GRAY)
#
#                 # Predict label and confidence
#                 label, confidence = face_recognizer.predict(gray)
#
#                 # Display results
#                 print(f'Label = {people[label]} with a confidence of {confidence}')
#
#                 # Draw rectangle with desired thickness
#                 cv.rectangle(image, (xmin, ymin), (xmin + width, ymin + height), (0, 255, 0), thickness=2)
#
#                 # Calculate text position within the rectangle (adjust padding as needed)
#                 text_x = xmin + 10
#                 text_y = ymin + height - 10
#
#                 # Display label name above the rectangle with adjusted font size
#                 cv.putText(image, str(people[label]), (text_x, text_y), cv.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0),
#                            thickness=1)
#
#         # Display the processed frame
#         cv.imshow('Real-time Face Recognition', image)
#
#         # Exit on 'q' key press
#         if cv.waitKey(5) & 0xFF == ord('q'):
#             break
#
# # Release resources
# cap.release()
# cv.destroyAllWindows()
#
# import cv2 as cv
# import numpy as np
# import mediapipe as mp
#
# # Initialize drawing and face detection specifications
# mp_drawing = mp.solutions.drawing_utils
# mp_face_detection = mp.solutions.face_detection
#
# # Load the trained face recognition model (replace with your model path)
# face_recognizer = cv.face.LBPHFaceRecognizer_create()
# face_recognizer.read('face_trained.yml')
#
# # Define labels (replace with your actual labels)
# people = ['100', '101']
# # Start video capture from webcam
# cap = cv.VideoCapture(0)
#
# with mp_face_detection.FaceDetection(
#         min_detection_confidence=0.5, model_selection=0
# ) as face_detection:
#     while True:
#         success, image = cap.read()
#         if not success:
#             print("Ignoring empty camera frame.")
#             # If loading image fails, exit the loop
#             continue
#
#         # Flip the image horizontally to correct the mirroring effect
#         image = cv.flip(image, 1)
#
#         # Convert BGR image to RGB for MediaPipe processing
#         image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
#
#         # Perform face detection on the frame
#         results = face_detection.process(image_rgb)
#
#         # Process detected faces
#         if results.detections:
#             for detection in results.detections:
#                 # Extract face landmarks (bounding box)
#                 xmin = int(detection.location_data.relative_bounding_box.xmin * image.shape[1])
#                 ymin = int(detection.location_data.relative_bounding_box.ymin * image.shape[0])
#                 width = int(detection.location_data.relative_bounding_box.width * image.shape[1])
#                 height = int(detection.location_data.relative_bounding_box.height * image.shape[0])
#
#                 # Extract the face ROI (Region of Interest)
#                 face_roi = image[ymin:ymin + height, xmin:xmin + width]
#
#                 # Check if face ROI is empty
#                 if face_roi.size == 0:
#                     print("Empty face ROI. Skipping...")
#                     continue
#
#                 gray = cv.cvtColor(face_roi, cv.COLOR_BGR2GRAY)
#
#                 # Predict label and confidence
#                 label, confidence = face_recognizer.predict(gray)
#
#                 # Display results
#                 print(f'Label = {people[label]} with a confidence of {confidence}')
#
#                 # Draw rectangle with desired thickness
#                 cv.rectangle(image, (xmin, ymin), (xmin + width, ymin + height), (0, 255, 0), thickness=2)
#
#                 # Calculate text position within the rectangle (adjust padding as needed)
#                 text_x = xmin + 10
#                 text_y = ymin + height - 10
#
#                 # Display label name above the rectangle with adjusted font size
#                 cv.putText(image, str(people[label]), (text_x, text_y), cv.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0),
#                            thickness=1)
#
#         # Display the processed frame
#         cv.imshow('Real-time Face Recognition', image)
#
#         # Exit on 'q' key press
#         if cv.waitKey(5) & 0xFF == ord('q'):
#             break
#
# # Release resources
# cap.release()
# cv.destroyAllWindows()
#
# import cv2 as cv
# import numpy as np
# import mediapipe as mp
# import sqlite3
# import datetime
#
# def update_attendance(recognized_face_id):
#     # Connect to the SQLite database
#     conn = sqlite3.connect('students.db')
#     cursor = conn.cursor()
#
#     # Get the current date
#     current_date = datetime.date.today()
#
#     # Check if the recognized face ID exists in the Attendance table
#     cursor.execute("SELECT date FROM Attendance WHERE student_id = ? ORDER BY date DESC LIMIT 1", (recognized_face_id,))
#     result = cursor.fetchone()
#
#     if result:
#         last_attendance_date = datetime.datetime.strptime(result[0], "%Y-%m-%d").date()
#
#         # Compare the retrieved date with the current date
#         if last_attendance_date != current_date:
#             # Update the records in the Attendance table
#             cursor.execute("UPDATE Attendance SET date = ? WHERE student_id = ? AND date = ?", (current_date, recognized_face_id, result[0]))
#
#             # Update the Attendance_count in the Students table
#             cursor.execute("UPDATE Students SET attendance_count = attendance_count + 1 WHERE id = ?", (recognized_face_id,))
#         else:
#             print("Attendance for today already marked.")
#     else:
#         # Insert a new row for the recognized face ID
#         cursor.execute("INSERT INTO Attendance (student_id, date) VALUES (?, ?)", (recognized_face_id, current_date))
#
#         # Update the Attendance_count in the Students table
#         cursor.execute("UPDATE Students SET attendance_count = attendance_count + 1 WHERE id = ?", (recognized_face_id,))
#
#     # Commit the changes to the database
#     conn.commit()
#     print("Attendance updated successfully.")
#
#     # Close the connection
#     conn.close()
#
# # Initialize drawing and face detection specifications
# mp_drawing = mp.solutions.drawing_utils
# mp_face_detection = mp.solutions.face_detection
#
# # Load the trained face recognition model (replace with your model path)
# face_recognizer = cv.face.LBPHFaceRecognizer_create()
# face_recognizer.read('face_trained.yml')
#
# # Define labels (replace with your actual labels)
# people = ['100', '101']
# # Start video capture from webcam
# cap = cv.VideoCapture(0)
#
# with mp_face_detection.FaceDetection(
#         min_detection_confidence=0.5, model_selection=0
# ) as face_detection:
#     while True:
#         success, image = cap.read()
#         if not success:
#             print("Ignoring empty camera frame.")
#             # If loading image fails, exit the loop
#             continue
#
#         # Flip the image horizontally to correct the mirroring effect
#         image = cv.flip(image, 1)
#
#         # Convert BGR image to RGB for MediaPipe processing
#         image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
#
#         # Perform face detection on the frame
#         results = face_detection.process(image_rgb)
#
#         # Process detected faces
#         if results.detections:
#             for detection in results.detections:
#                 # Extract face landmarks (bounding box)
#                 xmin = int(detection.location_data.relative_bounding_box.xmin * image.shape[1])
#                 ymin = int(detection.location_data.relative_bounding_box.ymin * image.shape[0])
#                 width = int(detection.location_data.relative_bounding_box.width * image.shape[1])
#                 height = int(detection.location_data.relative_bounding_box.height * image.shape[0])
#
#                 # Extract the face ROI (Region of Interest)
#                 face_roi = image[ymin:ymin + height, xmin:xmin + width]
#
#                 # Check if face ROI is empty
#                 if face_roi.size == 0:
#                     print("Empty face ROI. Skipping...")
#                     continue
#
#                 gray = cv.cvtColor(face_roi, cv.COLOR_BGR2GRAY)
#
#                 # Predict label and confidence
#                 label, confidence = face_recognizer.predict(gray)
#                 recognized_face_id = int(people[label]);
#                 conn = sqlite3.connect('students.db')
#                 cursor = conn.cursor()
#                 cursor.execute("SELECT name FROM Students WHERE id = ? ",
#                                (recognized_face_id,))
#                 name = cursor.fetchone()
#                 conn.close()
#                 # Display results
#                 print(f'Label = {name[0]} with a confidence of {confidence}')
#
#                 # Draw rectangle with desired thickness
#                 if confidence >= 60:
#
#                     update_attendance(recognized_face_id)
#
#                     cv.rectangle(image, (xmin, ymin), (xmin + width, ymin + height), (0, 255, 0), thickness=2)
#                     # Calculate text position within the rectangle (adjust padding as needed)
#                     text_x = xmin + 10
#                     text_y = ymin + height - 10
#
#                     # Display label name above the rectangle with adjusted font size
#                     cv.putText(image, str(name[0]), (text_x, text_y), cv.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0),
#                                thickness=1)
#                 else:
#                     cv.rectangle(image, (xmin, ymin), (xmin + width, ymin + height), (0, 0, 255), thickness=2)
#                     # Calculate text position within the rectangle (adjust padding as needed)
#                     text_x = xmin + 10
#                     text_y = ymin + height - 10
#
#                     # Display "unknown" text above the rectangle with adjusted font size
#                     cv.putText(image, "Unknown", (text_x, text_y), cv.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255),
#                                thickness=1)
#
#         # Display the processed frame
#         cv.imshow('Real-time Face Recognition', image)
#
#         # Exit on 'q' key press
#         if cv.waitKey(5) & 0xFF == ord('q'):
#             break
#
#
#
# # Release resources
# cap.release()
# cv.destroyAllWindows()


import cv2 as cv
import numpy as np
import mediapipe as mp
import sqlite3
import datetime
import tkinter as tk
from PIL import Image, ImageTk

class FaceRecognitionAttendance:
    def __init__(self, model_path, labels, database_path='students.db'):
        self.face_recognizer = cv.face.LBPHFaceRecognizer_create()
        self.face_recognizer.read(model_path)
        self.labels = labels
        self.database_path = database_path
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_face_detection = mp.solutions.face_detection

    def update_attendance(self, recognized_face_id):
        # Connect to the SQLite database
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()

        # Get the current date
        current_date = datetime.date.today()

        # Check if the recognized face ID exists in the Attendance table
        cursor.execute("SELECT date FROM Attendance WHERE student_id = ? ORDER BY date DESC LIMIT 1", (recognized_face_id,))
        result = cursor.fetchone()

        if result:
            last_attendance_date = datetime.datetime.strptime(result[0], "%Y-%m-%d").date()

            # Compare the retrieved date with the current date
            if last_attendance_date != current_date:
                # Update the records in the Attendance table
                cursor.execute("UPDATE Attendance SET date = ? WHERE student_id = ? AND date = ?", (current_date, recognized_face_id, result[0]))

                # Update the Attendance_count in the Students table
                cursor.execute("UPDATE Students SET attendance_count = attendance_count + 1 WHERE id = ?", (recognized_face_id,))
            else:
                print("Attendance for today already marked.")
        else:
            # Insert a new row for the recognized face ID
            cursor.execute("INSERT INTO Attendance (student_id, date) VALUES (?, ?)", (recognized_face_id, current_date))

            # Update the Attendance_count in the Students table
            cursor.execute("UPDATE Students SET attendance_count = attendance_count + 1 WHERE id = ?", (recognized_face_id,))

        # Commit the changes to the database
        conn.commit()
        print("Attendance updated successfully.")

        # Close the connection
        conn.close()

    def recognize_and_update(self,frame2):
        # Start video capture from webcam
        cap = cv.VideoCapture(0)

        # Create a label within frame2 to display the video
        video_label = tk.Label(frame2)
        video_label.pack(fill=tk.BOTH, expand=True)
        with self.mp_face_detection.FaceDetection(min_detection_confidence=0.5, model_selection=0) as face_detection:
            while True:
                success, image = cap.read()
                if not success:
                    print("Ignoring empty camera frame.")
                    # If loading image fails, exit the loop
                    continue

                # Flip the image horizontally to correct the mirroring effect
                image = cv.flip(image, 1)

                # Convert BGR image to RGB for MediaPipe processing
                image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)

                # Perform face detection on the frame
                results = face_detection.process(image_rgb)
                # Process detected faces
                if results.detections:
                    for detection in results.detections:
                        # Extract face landmarks (bounding box)
                        xmin = int(detection.location_data.relative_bounding_box.xmin * image.shape[1])
                        ymin = int(detection.location_data.relative_bounding_box.ymin * image.shape[0])
                        width = int(detection.location_data.relative_bounding_box.width * image.shape[1])
                        height = int(detection.location_data.relative_bounding_box.height * image.shape[0])

                        # Extract the face ROI (Region of Interest)
                        face_roi = image[ymin:ymin + height, xmin:xmin + width]

                        # Check if face ROI is empty
                        if face_roi.size == 0:
                            print("Empty face ROI. Skipping...")
                            continue

                        gray = cv.cvtColor(face_roi, cv.COLOR_BGR2GRAY)

                        # Predict label and confidence
                        label, confidence = self.face_recognizer.predict(gray)
                        recognized_face_id = int(self.labels[label])
                        conn = sqlite3.connect(self.database_path)
                        cursor = conn.cursor()
                        cursor.execute("SELECT name FROM Students WHERE id = ?", (recognized_face_id,))
                        name = cursor.fetchone()
                        conn.close()

                        # Display results
                        print(f'Label = {name[0]} with a confidence of {confidence}')

                        # Draw rectangle with desired thickness
                        if confidence >= 60:
                            self.update_attendance(recognized_face_id)

                            cv.rectangle(image, (xmin, ymin), (xmin + width, ymin + height), (0, 255, 0), thickness=2)
                            # Calculate text position within the rectangle (adjust padding as needed)
                            text_x = xmin + 10
                            text_y = ymin + height - 10

                            # Display label name above the rectangle with adjusted font size
                            cv.putText(image, str(name[0]), (text_x, text_y), cv.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), thickness=1)
                        else:
                            cv.rectangle(image, (xmin, ymin), (xmin + width, ymin + height), (0, 0, 255), thickness=2)
                            # Calculate text position within the rectangle (adjust padding as needed)
                            text_x = xmin + 10
                            text_y = ymin + height - 10

                            # Display "unknown" text above the rectangle with adjusted font size
                            cv.putText(image, "Unknown", (text_x, text_y), cv.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), thickness=1)

                # Display the processed frame
                # Resize the image efficiently for Tkinter (outside the loop)
                image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
                resized_image = cv.resize(image, (550, 400))

                # Convert to PIL Image for Tkinter
                img = Image.fromarray(resized_image)
                img = ImageTk.PhotoImage(image=img)

                # Update the video label
                video_label.config(image=img)
                video_label.image = img  # Keep a reference
                #cv.imshow('Real-time Face Recognition', image)
                # Update the Tkinter mainloop
                frame2.update()
                # Exit on 'q' key press
                if cv.waitKey(5) & 0xFF == ord('q'):
                    break

        # Release resources
        cap.release()
        cv.destroyAllWindows()

# Usage
# model_path = 'face_trained.yml'
# labels = ['100', '101']  # Replace with your actual labels
# attendance_system = FaceRecognitionAttendance(model_path, labels)
# attendance_system.recognize_and_update()
