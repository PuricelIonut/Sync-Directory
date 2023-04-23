# Sync-Directory

### A python script made for syncing two directories

## Usage:

    Takes command-line arguments:
    - Source directory path: '-s --source'
    - Replica directory path: '-r --replica'
    - Logs directory path: '-l --logs'
    - Time to wait before starting to sync: '-t --time'

    Source, replica and logs are required but if time is omitted the script will run instantly.
    Time takes an integer indicating how many minutes to wait before sync.