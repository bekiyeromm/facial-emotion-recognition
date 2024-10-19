#!/usr/bin/env python3
import cv2
import os
from PIL import Image

def detect_and_crop_faces(input_folder, output_folder, face_cascade_path):
    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    
    # Check if the output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate over all images in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)
            
            # Convert the image to grayscale for face detection
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Detect faces in the image
            faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(48, 48))
            
            # Crop and save each detected face
            for (x, y, w, h) in faces:
                cropped_face = image[y:y+h, x:x+w]
                cropped_face_pil = Image.fromarray(cv2.cvtColor(cropped_face, cv2.COLOR_BGR2RGB))
                
                # Save the cropped face image
                base_filename = os.path.splitext(filename)[0]
                output_filename = f"{base_filename}_face.jpg"
                output_path = os.path.join(output_folder, output_filename)
                cropped_face_pil.save(output_path)
                print(f"Saved cropped face to {output_path}")

# Define paths
input_folder = '/home/beki/Desktop/research/23'  # Folder containing input images
output_folder = '/home/beki/Desktop/research/25'  # Folder to save cropped face images
face_cascade_path = 'haarcascade_frontalface_default.xml'  # Path to the Haar Cascade XML file

# Detect and crop faces
detect_and_crop_faces(input_folder, output_folder, face_cascade_path)
