#!/bin/bash

# build the container
sudo docker build -t meiring/client .

#find server ip
SERVER_IP=$(sudo docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' server)

# start the container
sudo docker run -dit --net client-server-net --name client -v clientvol:/clientdata meiring/client $SERVER_IP 5000
