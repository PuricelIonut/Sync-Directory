import os
import time
import datetime

from helpers import *


def main():
    args = cl_handler()

    source = args['source']
    replica = args['replica']
    logs = args['logs']
    time_to_wait = args['time']


    if not os.path.exists(source):
        raise FileNotFoundError()
    elif os.path.exists(source) and os.path.isfile(source):
        raise Warning('Given source path leads to a file!')

    if not os.path.exists(replica):
        os.mkdir(replica)
    elif os.path.exists(replica) and os.path.isfile(replica):
        raise Warning('Given replica path leads to a file!')


    if not os.path.exists(logs):
        os.mkdir(logs)
    elif os.path.exists(logs) and os.path.isfile(logs):
        raise Warning('Given logs path leads to a file!')
    
    if time_to_wait is None:
        start_sync(source, replica)
    else:
        try:
            while True:
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                sync_time = datetime.datetime.now() + datetime.timedelta(minutes=time_to_wait)
                print('--> Current time: ', current_time)
                print(f'--> Starting sync at: {sync_time.strftime("%Y-%m-%d %H:%M:%S")}')
                time.sleep(time_to_wait*60)
                start_sync(source, replica)
        except KeyboardInterrupt:
            print('Ended by keyboard interrupt.')

main()