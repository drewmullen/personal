docker network

docker network ls

docker network inspect <name>

network types:
single host networking:
user defined bridge (vswitch) network on a clean docker host

docker network create -d bridge --subnet 10.0.0.1/24 <name>

docker run -dt --name <> --network <bridge name> ubuntu

## multi-host overlay networking
