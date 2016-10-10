import os
import sys

import shutil


class BLFile(object):
    def __init__(self, path, filename, key):
        self.path = path
        self.filename = filename
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

if __name__ == "__main__":

    start_dir = sys.argv[1]
    subj_files = sys.argv[2]


    if len(sys.argv) > 4:
        print "\nusage:  $: python scatterbl.py  folder_with_all_bl_files  path_to_subject_files  [--audio] [--video]\n\ncan't have more than 3 arguments"
        sys.exit(0)

    audio_bl = False
    if "--audio" in sys.argv:
        audio_bl = True
    video_bl = False
    if "--video" in sys.argv:
        video_bl = True

    bl_files = []

    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file.endswith(".csv"):
                key = file[:5]
                bl_file = BLFile(os.path.join(root, file), file, key)
                bl_files.append(bl_file)

    for root, dirs, files in os.walk(subj_files):
        if audio_bl:
            if "Audio_Annotation" in root:
                key = root.split("Subject_Files/")[1].split("/")[1]
                for bl_file in bl_files:
                    if bl_file.key == key:
                        shutil.copy(bl_file.path, os.path.join(root, bl_file.filename))

        if video_bl:
            if "Video_Annotation" in root:
                key = root.split("Subject_Files/")[1].split("/")[1]
                for bl_file in bl_files:
                    if bl_file.key == key:
                        shutil.copy(bl_file.path, os.path.join(root, bl_file.filename))

    print
