# aiohttp-devtools + Docker
Docker-Environment running [aiohttp-devtools](https://github.com/aio-libs/aiohttp-devtools) for easy development.

Installs dependencies in a volume so they can easily be reinstalled without creating a new container. The easiest way to do this is to just stop the container, delete the `volumes/virtualenv`-folder and restart the container. During the container startup the virtualenv will be recreated.

# Build and run
Start `docker-compose up` to build and run the docker container. Once its running you can access http://localhost:4000 in your web browser. It shows a simple welcome page reading 'Welcome User!'. You can make changes in the files in the `volumes/web/` folder and it will reload the page automatically.

If you make changes to the Dockerfile just run `docker-compose build` to re-build the docker image.

Because the [entrypoint-script](https://github.com/brean/aiohttp_dev_docker/blob/master/docker/entrypoint.sh) executes `pip install` for the `requirements.txt` you only need to add your dependencies to that requirements file and restart the docker container.
