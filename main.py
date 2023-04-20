import os
import argparse
import shutil

from sys import argv

parser = argparse.ArgumentParser(description="Sync two directories")


origin = 'C:/Users/ionut/Desktop/programare/sync directory/source/'
target = 'C:/Users/ionut/Desktop/programare/sync directory/replica/'


def sync_files():
    print('Sync in progress...')
    source_files, replica_files = get_files()
    for i in get_directories():
        if not os.path.exists(i):
            os.mkdir(i)
            print('Created directory: '+i)
    for s, r in zip(source_files, replica_files):
        if not os.path.exists(r) or os.path.getmtime(s) != os.path.getmtime(r):
            shutil.copy2(src=s, dst=r)
            print('Creating file: '+r)
    remove_files()
    print('Sync completed!')

# FILES NOT IN SOURCE SO CANT COMPARE
def remove_files():
    source_files, replica_files = get_files()
    for s, r in zip(source_files, replica_files):
        if not os.path.exists(s):
            if os.path.isdir(r):
                shutil.rmtree(r)
                print('Removing directory: '+r)
            else:
                os.remove(r)
                print('Removing file: '+r)


def get_files(path):
    files = []
    for p in os.walk(path):
        for file in os.listdir(p[0]):
            if not os.path.isdir(p[0]+'/'+file):
                files.append(p[0]+'/'+file)
    return files


def get_directories(path):
    directories = []
    for f in os.walk(origin):
        directories.append(f[0])
    return directories


def replace_data():
    directories = [x.replace(os.path.basename(os.path.dirname(origin)), os.path.basename(os.path.dirname(target))) for x in get_directories(origin) ]
    files = [x.replace(os.path.basename(os.path.dirname(origin)), os.path.basename(os.path.dirname(target))) for x in get_files(origin) ]
    return directories, files


