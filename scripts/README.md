# README

### [ktsprof](https://github.com/rsettine-tibco/fp-notes/blob/main/fp39/scripts/ktsprof)
This script is used to set the development environment profile so that you are ready to build the FP components. 

It uses `ksh` shell.

This script requires 4 aruments. For more details, please refer [here](https://github.com/rsettine-tibco/fp-notes/blob/main/fp39/presentations/How%20to%20build%20FP%20components.pdf).
### [setenv3.9_dev](https://github.com/rsettine-tibco/fp-notes/blob/main/fp39/scripts/setenv3.9_dev)
Use this script to set the development envrionment profile. However, use this profile only to run the examples as this uses `bash` shell. 

### [importfpsrc.ksh](https://github.com/rsettine-tibco/fp-notes/blob/main/fp39/scripts/importfpsrc.ksh)
This script is used to download the source code from svn. During the download, it also does additional things such as creates the soft links that required, linking to 3rdparty etc., (which otherwsie will not happen if we use `svn` command to download the source)

### [addlog.py](https://github.com/rsettine-tibco/fp-notes/blob/main/fp39/scripts/addlog.py)
This script can be used to add the logging to `.act` file when needed.
