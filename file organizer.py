# organize a cluttered desktop & hdd by automatically moving it to dated folders (year, month) according to 'date created'

import os
import shutil
import datetime

def organize_files(source_folder, target_folder):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for root, _, files in os.walk(source_folder):
        for filename in files:
            if filename.startswith("._"):
                continue  # Skip hidden system files
            source_path = os.path.join(root, filename)

            try:
                file_creation_time = os.path.getctime(source_path)
            except FileNotFoundError:
                continue  # Skip files that can't be accessed

            creation_date = datetime.datetime.fromtimestamp(file_creation_time)
            target_subfolder = os.path.join(target_folder, str(creation_date.year),
                                            f"{creation_date.month:02d}")

            if not os.path.exists(target_subfolder):
                os.makedirs(target_subfolder)

            target_file = os.path.join(target_subfolder, filename)
            shutil.move(source_path, target_file)
            print(f"Moved {filename} to {target_subfolder}")

source_folder = "//"  # Update this path
target_folder = "//"  # Update this path

organize_files(source_folder, target_folder)












