import cv2 as cv
import os
import numpy as np
import mediapipe as mp

# Initialize drawing and face detection specifications
mp_drawing = mp.solutions.drawing_utils
mp_face_detection = mp.solutions.face_detection


people = ['100','101']
DIR = '//images/train'
features = []
labels = []


def create_train():
  with mp_face_detection.FaceDetection(
      min_detection_confidence=0.5, model_selection=0
  ) as face_detection:
    for person in people:
      path = os.path.join(DIR, person)
      label = people.index(person)

      for img in os.listdir(path):
        img_path = os.path.join(path, img)
        img_array = cv.imread(img_path)

        # Handle empty image reading
        if img_array is None:
          print("Error reading image:", img_path)
          continue

        # Convert BGR image to RGB for MediaPipe processing
        image = cv.cvtColor(img_array, cv.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Perform face detection on the frame
        results = face_detection.process(image)

        # Convert image back to BGR for further processing
        image.flags.writeable = True
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

        # Extract and process detected faces
        if results.detections:
          for detection in results.detections:
            # Get face landmarks (bounding box)
            xmin = int(detection.location_data.relative_bounding_box.xmin * image.shape[1])
            ymin = int(detection.location_data.relative_bounding_box.ymin * image.shape[0])
            width = int(detection.location_data.relative_bounding_box.width * image.shape[1])
            height = int(detection.location_data.relative_bounding_box.height * image.shape[0])

            # Extract the face ROI (Region of Interest)
            face_roi = image[ymin:ymin + height, xmin:xmin + width]

            # Handle empty face ROI
            if face_roi.shape[0] == 0 or face_roi.shape[1] == 0:
              print("No face detected in image:", img_path)
              continue

            gray = cv.cvtColor(face_roi, cv.COLOR_BGR2GRAY)

            # Add the face and its label to the data
            features.append(gray)
            labels.append(label)


create_train()
print('Training done---------')
features = np.array(features, dtype='object')
labels = np.array(labels)
face_recognizer = cv.face.LBPHFaceRecognizer.create()
#Train the Recognizer on the features list and the labels list

face_recognizer.train(features,labels)

# Save the trained model and data (replace with your desired saving methods)
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
