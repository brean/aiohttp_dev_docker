# aiohttp-devtools + Docker
Docker container running a simple [aiohttp-devtools](https://github.com/aio-libs/aiohttp-devtools) app in a volume for easy development.

It also installs the dependencies in a volume so they can easily be reinstalled without creating a new container. 

# Build and run
Start `docker-compose up` to build and run the docker container. Once its running you can access http://localhost:4000 in your web browser. It shows a simple welcome page reading 'Welcome User!'. You can make changes in the files in the `volumes/web/` folder and it will reload the page automatically.

If you make changes in `docker/Dockerfile` just run `docker-compose build` to re-build the docker image.

If you like to add additional requirements just add them to the `requirements.txt`-file and restart the container. This works because the [entrypoint-script](https://github.com/brean/aiohttp_dev_docker/blob/master/docker/entrypoint.sh) executes `pip install` for the `requirements.txt` at startup.

To reinstall the dependencies just stop the container, delete the `volumes/virtualenv`-folder and restart the container. During the container startup the virtualenv will be recreated.
