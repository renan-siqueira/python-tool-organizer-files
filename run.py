import os
import shutil
from settings import config


def organize_images(base_path, folder_name_1, folder_name_2, identifier_1, identifier_2):
    for root, _, files in os.walk(base_path):

        points_path = os.path.join(root, folder_name_1)
        original_path = os.path.join(root, folder_name_2)

        if not os.path.exists(points_path):
            os.makedirs(points_path)
        if not os.path.exists(original_path):
            os.makedirs(original_path)

        for file in files:
            if identifier_1 in file:
                shutil.move(os.path.join(root, file), points_path)
            elif identifier_2 in file:
                shutil.move(os.path.join(root, file), original_path)


if __name__ == '__main__':
    base_path = config.APP_PATH_MAIN_FOLDER
    
    FOLDER_NAME_1 = 'original'
    FOLDER_NAME_2 = 'flipped'
    IDENTIFIER_1 = '_without_points.'
    IDENTIFIER_2 = '_flipped.'

    organize_images(base_path, FOLDER_NAME_1, FOLDER_NAME_2, IDENTIFIER_1, IDENTIFIER_2)
