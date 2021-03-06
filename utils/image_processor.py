import os
from PIL import Image
from .utils import truncate


def process_images(output_file, percentage):
    os.chdir("images")
    output_count = 0
    for filename in os.listdir(os.getcwd()):
        image = Image.open(filename)
        width, height = image.size
        bg_count = next(n for n, c in image.getcolors(width * height) if c == (255, 255, 255))
        img_count = width * height - bg_count
        img_percent = truncate(100 - (img_count * 100.0 / width / height), 0)
        if img_percent >= percentage:
            output_file.write(f"{filename}, {img_percent}%")
            output_file.write("\n")
            output_count = output_count + 1
    return output_count
