import os
import argparse
import shutil

from sys import argv

parser = argparse.ArgumentParser(description="Sync two directories")


origin = 'C:/Users/ionut/Desktop/programare/sync directory/source/'
target = 'C:/Users/ionut/Desktop/programare/sync directory/replica/'


def copy_files():
    print('Sync in progress...')
    for file in os.listdir(origin):
        if os.path.isdir(origin+file) and not os.path.exists(target+file):
            os.mkdir(target+file)
            print('Creating directory:'+target+file)
        elif os.path.isfile(origin+file) and file in os.listdir(target) and os.path.getmtime(origin+file) != os.path.getmtime(target+file):
            shutil.copy2(src=origin+file, dst=target+file)
            print('Syncing: '+origin+file)
        elif os.path.isfile(origin+file) and file not in os.listdir(target):
            shutil.copy2(src=origin+file, dst=target+file)
            print('Creating file: '+target+file)
    remove_files()
    print('Sync completed!')


def remove_files():
    source, replica = get_files()
    for f in replica:
        if f not in source:
            if os.path.isdir(f):
                shutil.rmtree(target+f)
                print('Removing directory: '+target+f)
            else:
                os.remove(target + f)
                print('Removing: ' + target + f)


def get_files():
    source = os.listdir(origin)
    replica = os.listdir(target)
    return source, replica

copy_files()

#  os.path.getmtime(path)¶ ( get date when last modified )