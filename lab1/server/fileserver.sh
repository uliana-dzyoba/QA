#!/bin/bash

# build the flask container
sudo docker build -t meiring/server .

# create the network
sudo docker network create client-server-net

# start the flask app container
sudo docker run -d --net client-server-net -p 5000:5000 --name server -v servervol:/serverdata meiring/server
