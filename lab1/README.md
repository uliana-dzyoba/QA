As an official base image was used python:3 for both images

The server app was developed with Flask

Checksum is calculated using md5 algorith and is send in http header called checksum

To get into the client container shell execute:
```
$ sudo docker exec -it client sh
\# ls ../../../clientdata
```
and there must be a file called textfile.txt

_Note that for this to work the container must be running_

Volumes were created with a -v flag when running the containers using docker run
