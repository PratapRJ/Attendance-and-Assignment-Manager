#
# import cv2
# import os
# import mediapipe as mp
#
# # Initialize drawing and face detection specifications
# mp_drawing = mp.solutions.drawing_utils
# mp_face_detection = mp.solutions.face_detection
#
# # Create video capture object
# cap = cv2.VideoCapture(0)
#
# # Define model selection options (0 - short-range, 1 - longer range)
# model_selection = 0
#
# # Get folder name from user
# while True:
#     folder_name = input("Enter a folder name to save images (or 'q' to quit): ")
#     if folder_name.lower() == 'q':
#         break
#
#     # Check if folder exists
#     if os.path.exists(folder_name):
#         print(f"Folder '{folder_name}' already exists. Images will be saved with incremented names.")
#     else:
#         # Create the folder if it doesn't exist
#         os.makedirs(folder_name)
#
#     # Specify the maximum number of faces to detect and save
#     max_faces_to_save = int(input(
#         f"Enter Maximum faces to save in that '{folder_name}' folder: "))  # Change this value as needed
#
#     # Face counter with initial value based on existing files (if any)
#     face_count = len(os.listdir(folder_name))  # Assuming filenames start with "face_"
#     print(face_count)
#     with mp_face_detection.FaceDetection(
#             min_detection_confidence=0.5, model_selection=model_selection
#     ) as face_detection:
#         while True:
#             # Capture frame-by-frame
#             success, image = cap.read()
#             if not success:
#                 print("Ignoring empty camera frame.")
#                 continue
#
#             # Flip the image horizontally to correct the mirroring effect
#             image = cv2.flip(image, 1)
#
#             # Convert the BGR image to RGB for processing
#             image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#             image.flags.writeable = False
#
#             # Perform face detection on the frame
#             results = face_detection.process(image)
#
#             # Convert image back to BGR for drawing
#             image.flags.writeable = True
#             image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#
#             # Draw bounding boxes and save faces
#             if results.detections:
#                 for detection in results.detections:
#                     if face_count < max_faces_to_save:
#                         # Extract the face ROI (Region of Interest)
#                         xmin = int(detection.location_data.relative_bounding_box.xmin * image.shape[1])
#                         ymin = int(detection.location_data.relative_bounding_box.ymin * image.shape[0])
#                         width = int(detection.location_data.relative_bounding_box.width * image.shape[1])
#                         height = int(detection.location_data.relative_bounding_box.height * image.shape[0])
#                         face_image = image[ymin:ymin + height, xmin:xmin + width]
#
#                         # Generate incremented filename
#                         filename = f"{folder_name}/{face_count + 1}.jpg"
#                         cv2.imwrite(filename, face_image)
#                         face_count += 1
#
#                         # Draw bounding box (optional)
#                         mp_drawing.draw_detection(image, detection,
#                                                    mp_drawing.DrawingSpec(thickness=2, color=(0, 255, 0)))
#
#             # Display the resulting frame
#             cv2.imshow('MediaPipe Face Detection', image)
#
#             # Exit on 'q' key press or after saving n faces
#             if cv2.waitKey(5) & 0xFF == ord('q') or face_count >= max_faces_to_save:
#                 break
#
#     # Exit loop if user entered 'q'
#     break
#
# # Release capture object and close all windows
# cap.release()
# cv2.destroyAllWindows()

import cv2
import os
import mediapipe as mp
# Define model selection options (0 - short-range, 1 - longer range)
model_selection = 0

# Get folder name from user (replace with desired path)
folder = input("Enter folder Name :");
folder_name = os.path.join("images", "train", folder)

# Check if the complete path exists
if not os.path.exists(folder_name):
    # Create all necessary subfolders if they don't exist
    os.makedirs(folder_name)
    print(f"Created folder: {folder_name}")
else:
    print(f"Folder '{folder_name}' already exists. Images will be saved with incremented names.")

# Specify the maximum number of faces to detect and save
max_faces_to_save = int(input("Enter Maximum faces to save: "))

# Face counter with initial value based on existing files (if any)
face_count = len(os.listdir(folder_name))  # Assuming filenames start with "face_"
print(f"Current face count in '{folder_name}': {face_count}")

with mp.solutions.face_detection.FaceDetection(
        min_detection_confidence=0.5, model_selection=model_selection
) as face_detection:
    # Create video capture object
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # Flip the image horizontally to correct the mirroring effect
        image = cv2.flip(image, 1)

        # Convert the BGR image to RGB for processing
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Perform face detection on the frame
        results = face_detection.process(image)

        # Convert image back to BGR for drawing
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Draw bounding boxes and save faces
        if results.detections:
            for detection in results.detections:
                if face_count < max_faces_to_save:
                    # Extract the face ROI (Region of Interest)
                    xmin = int(detection.location_data.relative_bounding_box.xmin * image.shape[1]-50)
                    ymin = int(detection.location_data.relative_bounding_box.ymin * image.shape[0]-80)
                    width = int(detection.location_data.relative_bounding_box.width * image.shape[1])
                    height = int(detection.location_data.relative_bounding_box.height * image.shape[0])
                    face_image = image[ymin:ymin + height+120, xmin:xmin + width+120]

                    # Generate incremented filename with path
                    filename = os.path.join(folder_name, f"{face_count + 1}.jpg")
                    cv2.imwrite(filename, face_image)
                    face_count += 1

                    # Draw bounding box (optional)
                    mp.solutions.drawing_utils.draw_detection(image, detection,
                                                                 mp.solutions.drawing_utils.DrawingSpec(thickness=2, color=(0, 255, 0)))

        # Display the resulting frame
        cv2.imshow('MediaPipe Face Detection', image)

        # Exit on 'q' key press or after saving n faces
        if cv2.waitKey(5) & 0xFF == ord('q') or face_count >= max_faces_to_save:
            break

    # Release capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()
