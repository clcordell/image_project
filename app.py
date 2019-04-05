import time
import configparser

from utils.utils import truncate
from utils.image_processor import process_images


class App:
    config = configparser.ConfigParser()
    config.read('settings.ini')
    config.sections()
    percentage = int(config['SETTINGS']['PERCENTAGE'])
    print(f"Image - Write Space Checker\nDeveloped by Connor Cordell - 2019")
    print("Processing...")

    start_time = time.time()
    output_file = open("output-file.csv", "a+")
    output_count = process_images(output_file, percentage)
    time_taken = truncate(time.time() - start_time, 3)
    output_file.close()

    print(f"""
    There are {output_count} image(s) which have more than {percentage}% white space.
    The file name(s) have been added to \"{output_file.name}\"

    Process completed in {time_taken}ms.
    """)
