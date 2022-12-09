# Stops and removes containers
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

# Removes all images
docker rmi $(docker images -a -q)

# Copies ssh_keys into container

## Copy both private and public key:
docker cp ~/.ssh/id_ed25519 <container-name>://.ssh/
docker cp ~/.ssh/id_ed25519.pub <container-name>:/<user>/.ssh/

docker cp $HOME/.ssh/id_ed25519 6b9d18c3de7f:/home/appuser/.ssh/
docker cp $HOME/.ssh/id_ed25519.pub 6b9d18c3de7f:/home/appuser/.ssh/
Note: The user is specified in the IDE e.g. vscode 
 
## change the permission of private key so that you can do git operations


