import os

from helpers import *


def main():
    args = cl_handler()

    source = args['source']
    replica = args['replica']
    logs = args['logs']


    if not os.path.exists(source):
        raise Warning('Invalid source path!')
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
    

    start_sync(source, replica)


main()