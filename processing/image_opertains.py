from PIL import Image 
import numpy as np

def grayscale(image_path, output_path):
    with Image.open(image_path) as image:
        image_array = np.array(image.convert("RGB"))
    gray_array = np.mean(image_array, axis=2).astype(np.uint8)
    gray_image = Image.fromarray(gray_array) 
    gray_image.save(output_path)

def brightness(image_path, output_path, factor):
    with Image.open(image_path) as image:
        image_array = np.array(image.convert("RGB"))
    bright_array = np.clip(image_array * factor, 0, 255).astype(np.uint8)
    result = Image.fromarray(bright_array)
    result.save(output_path)

def contrast(image_path, output_path, factor):
    with Image.open(image_path) as image:
        image_array = np.array(image.convert("RGB"))
    mean = np.mean(image_array, axis=(0, 1), keepdims=True)
    contrast_array = np.clip((image_array - mean) * factor + mean, 0, 255).astype(np.uint8)
    result = Image.fromarray(contrast_array)
    result.save(output_path)

def rotate(image_path, output_path, angle):
    with Image.open(image_path) as image:
        rotated_image = image.rotate(angle, expand=True)
    rotated_image.save(output_path)

def flip(image_path, output_path, mode):
    with Image.open(image_path) as image:
        if mode == "horizontal":
            flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
        elif mode == "vertical":
            flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
        else:
            raise ValueError("Invalid flip mode. Use 'horizontal' or 'vertical'.")
    flipped_image.save(output_path)

def resize(image_path, output_path, width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be greater than zero.")
    with Image.open(image_path) as image:
        resized_image = image.resize((width, height))
    resized_image.save(output_path)

def crop(image_path, output_path, left, upper, right, lower):
    if right <= left or lower <= upper:
        raise ValueError("Crop right/bottom values must be greater than left/top values.")
    with Image.open(image_path) as image:
        width, height = image.size
        if left < 0 or upper < 0 or right > width or lower > height:
            raise ValueError(f"Crop area must be inside the image bounds ({width}x{height}).")
        cropped_image = image.crop((left, upper, right, lower))
    cropped_image.save(output_path)
