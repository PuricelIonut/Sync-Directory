import os
import argparse
import shutil

from sys import argv

parser = argparse.ArgumentParser(description="Sync two directories")


origin = 'C:/Users/ionut/Desktop/programare/sync directory/source/'
target = 'C:/Users/ionut/Desktop/programare/sync directory/replica/'


for file in os.listdir(origin):
    if os.path.isfile((file)):
        shutil.copy2(src=origin+file, dst=target+file)
        print(f"{file} succesfully synced!" )


