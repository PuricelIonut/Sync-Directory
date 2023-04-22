import os
import argparse
import shutil

from sys import argv

parser = argparse.ArgumentParser(description="Sync two directories")


origin = "C:/Users/ionut/Desktop/programare/sync directory/source"
target = "C:/Users/ionut/Desktop/programare/sync directory/replica"
logs = "C:/Users/ionut/Desktop/programare/sync directory/logs"


# Sync target to match src
def start_sync(source, replica):
    print("Sync in progress...")
    directories, files = replace_data(source, replica)
    for i in directories:
        if not os.path.exists(i):
            os.mkdir(i)
            print("Creating directory: " + os.path.normpath(i))
    for j, k in zip(files, get_files(source)):
        if not os.path.exists(j) or os.path.getmtime(j) != os.path.getmtime(k):
            shutil.copy2(dst=j, src=k)
            print("Copying file: " + os.path.normpath(j))
    remove_files(source, replica)
    print("Sync completed!")


# Remove files and dirs to match source
def remove_files(source, replica):
    directories, files = replace_data(source, replica)
    for i in get_files(replica):
        if i not in files:
            os.remove(i)
            print("Deleting file: " + os.path.normpath(i))
    
    while len(get_directories(origin)) != len(get_directories(replica)):
        for j in reversed(get_directories(replica)):
            if j not in directories:
                try:
                    os.rmdir(j)
                    print("Deleting directory: " + os.path.normpath(j))
                except OSError:
                    continue
   
        

# Get all files in every subdir inside given path
def get_files(path):
    return [
        p[0] + "/" + file
        for p in os.walk(path)
        for file in os.listdir(p[0])
        if not os.path.isdir(p[0] + "/" + file)
    ]


# Get all subdirs based on path
def get_directories(path):
    return [i[0] for i in os.walk(path)]


# Replace src dir name with target dir name - takes origin and target paths
def replace_data(source, replica):
    if not os.path.exists(replica):
        os.mkdir(replica)

    # Replace dir name
    return [
        x.replace(os.path.basename(source), os.path.basename(replica))
        for x in get_directories(source)
    ], [
        x.replace(os.path.basename(source), os.path.basename(replica))
        for x in get_files(source)
    ]



def logs():
    ...

start_sync(origin, target)
