# ![Eye of Sauron logo](https://github.com/playtunes100/Eye-of-sauron/blob/3762373b65b6a3956c26a11b5842bdc9469fdca8/eye%20of%20sauron%20logo.png)

## What is it
Eye of sauron is a script used for sorting/organizing files in a directory

## How does it work
It uses [Watchdog](https://pypi.org/project/watchdog/) which monitors filesystem events
to lookout for new files added to the directory.
These files will then be moved to a corresponding subdirectory depending on their filetype.

## Why?
I needed something to automate cleaning up my Downloads folder

## Install
place `eye.py` file in the desired folder
create a virtual environment
`python -m venv nameofvirtualenvironment`
Activate the virtual environment
`cd \nameofvirtualenvironment\Scripts\ & activate & ..\..`

using [PIP Package installer](https://pypi.org/project/pip/) run
`pip install -r requirements.txt`

## Next?
Make it a user friendly GUI 




