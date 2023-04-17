import os
import argparse
import shutil

from sys import argv

parser = argparse.ArgumentParser(description="Sync two directories")


origin = 'C:/Users/ionut/OneDrive/Desktop/programare/learning/sync directory/source/'
target = 'C:/Users/ionut/OneDrive/Desktop/programare/learning/sync directory/replica/'

files_to_sync = os.listdir(origin)

shutil.copytree(src=origin, dst=target, dirs_exist_ok=True)

#for file_name in files_to_sync:
   #     shutil.copy2(src=origin+file_name, dst=target+file_name)
  #      print(f"{file_name} succesfully synced!" )


"""def cl_handler(parser):
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-eAll", help="Encrypt all files inside root directory", action="store_true"
    )
    args = parser.parse_args()

    # Check for existing argv
    if len(argv) < 2:
        parser.print_help()
    return vars(args)

"""