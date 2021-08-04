# API Documentation

In order to access the API documentation of Run time and FP components, need to start the `Design Centre`.
- Note that a `dc` directory is created when the below command is run.
- When a component is built, dc gets started automatically
```
swdc -c start
```
It will show the following in the console
```

INFO: Starting Design Center at /opt/kabira/users/rsettine/BUILD.


	Stopping design center...

	Starting design center ...
		Installing Registry ...
		Updating Registry ...
		Installing Components ...
		Starting Components ...
		Waiting for components to initialize ...
		Waiting for design center services to start ...
	Startup complete

	Design Center is configured to use PRODUCTION executables
	Design Center shared memory size is 512Mb
	Design Center path: /opt/kabira/users/rsettine/BUILD/dc
	Design Center host: trocadero
	
	System Coordinator Host: All Interfaces
	System Coordinator Port: 50666
	
	Web Server Host: All Interfaces
	Web Server Port: 50667
	
	Documentation System Server Port: 29134
```
In order to access documentation, open browser and type http://trocadero.kabira.ft:29134
- Port may change each time dc is started.
- To stop dc, use `swdc -c stop` command.
