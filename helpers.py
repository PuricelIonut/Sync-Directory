import os
import argparse
import shutil
import datetime
import sys


# Handle all command line logic
def cl_handler():
    parser = argparse.ArgumentParser(description="Sync two directories")
    parser.add_argument('-s', '--source',type=str, help='Path to source directory(required)', required=True)
    parser.add_argument('-r', '--replica',type=str, help='Path to replica directory(required)', required=True)
    parser.add_argument('-l', '--logs',type=str, help='Path to logs directory(required)', required=True)
    parser.add_argument('-t', '--time', type=int, help='Time interval for syncing, in minutes')

    if len(sys.argv) < 2:
       parser.print_help()
    return vars(parser.parse_args())


args = cl_handler()
logs = args['logs']


# Sync target to match src
def start_sync(source, replica):
    print("Starting sync!")
    start_log('---> Starting log at: '+datetime.datetime.now().strftime("%H:%M:%S").__str__()+' <---'+'\n\n')
    directories, files = replace_data(source, replica)
    for i in directories:
        if not os.path.exists(i):
            os.mkdir(i)
            print(start_log("Creating directory: " + os.path.normpath(i)))
    for j, k in zip(files, get_files(source)):
        if not os.path.exists(j) or os.path.getmtime(j) != os.path.getmtime(k):
            shutil.copy2(dst=j, src=k)
            print(start_log("Copying file: " + os.path.normpath(j)))
    remove_files(source, replica)
    print(start_log("Sync complete!\n"))
    start_log('\n\n'+'---> Ending log at: '+datetime.datetime.now().strftime("%H:%M:%S").__str__()+' <---')


# Remove files and dirs to match source
def remove_files(source, replica):
    directories, files = replace_data(source, replica)
    for i in get_files(replica):
        if i not in files:
            os.remove(i)
            print(start_log("Deleting file: " + os.path.normpath(i)))
    
    # Make sure the directories are empty before delete else error
    while len(get_directories(source)) != len(get_directories(replica)):
        for j in reversed(get_directories(replica)):
            if j not in directories:
                try:
                    os.rmdir(j)
                    print(start_log("Deleting directory: " + os.path.normpath(j)))
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
    # Replace dir name
    return [
        x.replace(os.path.basename(source), os.path.basename(replica))
        for x in get_directories(source)
    ], [
        x.replace(os.path.basename(source), os.path.basename(replica))
        for x in get_files(source)
    ]


# Log the given parameter to a file and return the same parameter for printing
def start_log(line_to_log):
    current_date = datetime.date.today().__str__()
    
    with open(logs+'/'+current_date+'.txt', 'a') as log_file:
        log_file.write(line_to_log+'\n\n')
    return line_to_log

