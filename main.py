import os
import argparse
import shutil

from sys import argv

parser = argparse.ArgumentParser(description="Sync two directories")


origin = 'C:/Users/ionut/Desktop/programare/sync directory/source/'
target = 'C:/Users/ionut/Desktop/programare/sync directory/replica/'


for file_name in os.listdir(origin):
    if os.path.isfile((file_name)):
        shutil.copy2(src=origin+file_name, dst=target+file_name)
        print(f"{file_name} succesfully synced!" )


