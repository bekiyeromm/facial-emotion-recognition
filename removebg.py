import cv2
import numpy as np
import os
# Define the input and output directories
input_folder = os.path.expanduser('/home/beki/Desktop/new/unannotated/happy/')
output_folder = os.path.expanduser('/home/beki/Desktop/new/unannotated/grayscale image/happy/')




if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Define the background color (e.g., white)
bg_color = np.array([255, 255, 255])  # RGB for white

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        # Load the image
        img = cv2.imread(image_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Create a mask where the background color is detected
        mask = np.all(img_rgb == bg_color, axis=-1)
        img_rgb[mask] = [0, 0, 0, 0]  # Replace background with transparent
        
        # Save the result
        img_rgba = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2RGBA)
        cv2.imwrite(output_path, img_rgba)
        
        print(f"Processed and saved image: {output_path}")

print("Background removal completed for all images.")




