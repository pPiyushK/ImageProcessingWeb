from PIL import Image 
import numpy as np

def grayscale(image_path, output_path):
    image = Image.open(image_path).convert("RGB") 
    image_array = np.array(image)
    gray_array = np.mean(image_array, axis=2).astype(np.uint8)
    gray_image = Image.fromarray(gray_array) 
    gray_image.save(output_path)

