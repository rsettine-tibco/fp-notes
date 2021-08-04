# Build & Test FTP

## Build source
### Build _include_
```
cd $SW_HOME/ftp/paftp/linux/include
dmake BUILD=ALL
```
The above will copy the files (header or cpp?) from _`$SW_HOME/ftp/paftp/linux/include`_ to _`$SW_HOME/distrib/kabira/include`_
### Build _libsrc_
```
cd $SW_HOME/ftp/paftp/linux/libsrc
dmake BUILD=ALL
```
### Build _src_
```
cd $SW_HOME/ftp/paftp/linux/src
dmakeBUILD=ALL
```

In case, any intermediate error in any of the above steps, and like to clean and re-run? 
```
dmake clobber
```
or 
```
dmake clobberdc
```
The above stop clean and stop _Design Center_.
When there is error for missing header file, then check for the same under below directories
```
ls $SW_HOME/distrib/kabira/include
ls $SW_HOME/distrib/kabira/lib
```
#### Trouble shooting error:
Was getting below error on first time building _FTP_.

```
In file included from ./paftp_priv.h:20,
                 from paftp_dimpl.cpp:15:
./paftp.h:21:25: error: globbuiltin.h: No such file or directory
[Info]    : dmake:  Error code 1, while making 'devobj/paftp_dimpl.o'
dmake:  Error code 255, while making 'recursive'
[Fatal]   : dmake failed.
Build failed
dmake:  Error code 250, while making '/opt/kabira/users/rsettine/BUILD/paftp/paftpALL.bldtype'
```

The above got addressed when build from `$SW_HOMEftp/paftp/linux/include`; this has copied the `globbuiltin.h` under `$SW_HOME/distrib/kabira/include` directory.

## Testing FTP:
In order to test ftp connectivity, have to build test source first.
### Build _test_
```
cd $SW_HOME/ftp/paftp/linux/test
dmake BUILD=ALL
```
### Run _tests_
```
./runtest.ksh
```

However, it is running into different issue
```
runtest.ksh: missing required -d option
Usage, one of the following :

runtest.ksh [-b buildType][-i][-v][-x] -d deploySpec [-d deploySpec] -e engName
	  [-m memorySize] [-a application] [-C company]
runtest.ksh [-b buildType][-v][-x] [-a application] [-C company] -c
runtest.ksh [-b buildType][-v][-x] [-a application] [-C company] -i
runtest.ksh [-b buildType][-v][-x] [-a application] [-C company] -s

	-a		Application name
	-b buildType	DEVELOPMENT|PRODUCTION. Default: DEVELOPMENT
	-c		cleanup now
	-C		Company name
	-d deploySpec	deploy specification file (relative or absolute path)
			to be loaded. This argument may appear multiple times.
	-e engName	Test engine name.
	-m memorySize	Shared memory size in MB
	-i		install only - do not start components.
	-s		stop the test node
	-v		verbose; enable script debug printing.
	-x		enable set -x ksh script output.
```
The above says, deploy specification is mandatory; but learnt that test script will create that automatically. Yet to figure it out.

Noticed that runtest.ksh calling the script => _$SW_HOME/ftp/paftp/linux/include/testenv.ksh_
_$SW_HOME/ftp/paftp/linux/include/testenv.ksh => $SW_HOME/distrib/kabira/include/runtest.env_
_$SW_HOME/distrib/kabira/include/runtest.env => $SW_HOME/distrib/kabira/include/swenv.sh_
also using _$SW_HOME/distrib/kabira/bin/swregistry_

Learnt that, user have to modify below data in runtest.ksh; at least ftp connection,  directory name credentials
```
TESTDIR=/var/tmp/ftptest/
KSHUSER=`whoami`
#HOSTNAME=angel.kabira.com
HOSTNAME=mars.kabira.fr
PWDEXE=`which pwd`
CPEXE=`which cp`

#FTPUSER=appsfwx
#FTPUSER=support
FTPUSER=fcm
#FTPPASS=one12two
#FTPPASS=Support2012
FTPPASS=1typo+FULFI
UPLDDIR=upload
DWLDDIR=download
FTPTSTDIR=ftptest
```
