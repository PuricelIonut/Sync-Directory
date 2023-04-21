import os
import argparse
import shutil

from sys import argv

parser = argparse.ArgumentParser(description="Sync two directories")


origin = 'C:/Users/ionut/OneDrive/Desktop/programare/learning/sync directory/source'
target = 'C:/Users/ionut/OneDrive/Desktop/programare/learning/sync directory/replica'


# Sync target to match src
def start_sync(path_origin, path_target):
    print('Sync in progress...')
    directories, files = replace_data(path_origin, path_target)
    for i in directories:
        if not os.path.exists(i):
            os.mkdir(i)
            print('Creating directory: '+os.path.normpath(i))
    for j, k in zip(files, get_files(path_origin)):
        if not os.path.exists(j) or os.path.getmtime(j) != os.path.getmtime(k):
            shutil.copy2(dst=j, src=k)
            print('Copying file: '+os.path.normpath(j))
    remove_files(path_origin=path_origin, path_target=path_target)
    print('Sync completed!')


# Remove files and dirs to match src
def remove_files(path_origin, path_target):
    directories, files = replace_data(path_origin, path_target)
    for i in get_files(path_target):
        if i not in files:
            os.remove(i)
            print('Deleting file: '+os.path.normpath(i))
    for j in get_directories(path_target):
        if j not in directories:
            os.rmdir(j)
            print('Deleting directory: '+os.path.normpath(j))


# Get all files in every subdir inside given path
def get_files(path):
    files = []
    for p in os.walk(path):
        for file in os.listdir(p[0]):
            if not os.path.isdir(p[0]+'/'+file):
                files.append(p[0]+'/'+file)
    return files


# Get all subdirs based on path
def get_directories(path):
    directories = []
    for f in os.walk(path):
        directories.append(f[0])
    return directories


# Replace src dir name with target dir name - takes origin and target paths
def replace_data(path_origin, path_target):
    if not os.path.exists(path_target):
        os.mkdir(path_target)

    # Replace dir name 
    directories = [x.replace(os.path.basename(path_origin), os.path.basename(path_target)) for x in get_directories(path_origin) ]
    files = [x.replace(os.path.basename(path_origin), os.path.basename(path_target)) for x in get_files(path_origin) ]
    return directories, files
    

start_sync(path_origin=origin, path_target=target)


