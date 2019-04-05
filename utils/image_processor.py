import os
from PIL import Image


def process_images(output_file):
    os.chdir("images")
    output_count = 0
    for filename in os.listdir(os.getcwd()):
        image = Image.open(filename)
        width, height = image.size
        bg_count = next(n for n, c in image.getcolors(width * height) if c == (255, 255, 255))
        img_count = width * height - bg_count
        img_percent = 100 - (img_count * 100.0 / width / height)
        if img_percent >= 60:
            output_file.write(f"{filename}, {img_percent}%")
            output_file.write("\n")
            output_count = output_count + 1
    return output_count
