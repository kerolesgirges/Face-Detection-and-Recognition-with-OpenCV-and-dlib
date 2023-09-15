import cv2
import os
import face_recognition

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Create a directory to save the captured faces
if not os.path.exists('captured_faces'):
    os.makedirs('captured_faces')

known_face_encodings = []
known_face_names = []

def save_unique_face(face_img):
    # Generate a face encoding for the captured face
    face_encoding = face_recognition.face_encodings(face_img)[0]

    # Compare the captured face encoding with known face encodings
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    # If the captured face is not a match to any known faces, save it
    if not any(matches):
        # global known_face_encodings, known_face_names
        known_face_encodings.append(face_encoding)
        known_face_names.append(f'face_{len(known_face_encodings) - 1}.jpg')
        face_filename = f'captured_faces/{known_face_names[-1]}'
        cv2.imwrite(face_filename, face_img)
        print(f"Saved a new face as {face_filename}")

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Expand the region of interest to capture a larger face image
        expansion_factor = 1.5
        x_start = max(0, int(x - w * (expansion_factor - 1) / 2))
        y_start = max(0, int(y - h * (expansion_factor - 1) / 2))
        x_end = min(frame.shape[1], int(x + w * expansion_factor))
        y_end = min(frame.shape[0], int(y + h * expansion_factor))

        # Save the detected face as an image if it is unique
        face_img = frame[y_start:y_end, x_start:x_end]
        save_unique_face(face_img)

    # Display the frame with detected faces
    cv2.imshow('Face Detection', frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
