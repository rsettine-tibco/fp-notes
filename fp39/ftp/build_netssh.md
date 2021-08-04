# Build & Test **netssh**

## Build source
### Build _palibssh_
```
cd $SW_HOME/netssh/palibssh/linux/src
dmake BUILD=ALL
```
The above is resulting the following error now; **Yet to figure it out to proceed**.
```
->	palibssh.cpp:1005: warning: unused variable ‘status’
->
dmake:  Error code 1, while making 'devobj/palibssh.o'
dmake:  Error code 255, while making 'recursive'
[Fatal]   : dmake failed.
Build failed
dmake:  Error code 250, while making '/opt/kabira/users/rsettine/netssh/palibssh/linux/src/palibsshALL.bldtype'
trocadero:/opt/kabira/users/rsettine/netssh/palibssh/linux/src -> 
```
