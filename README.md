# aiohttp-devtools + Docker
Docker-Environment running [aiohttp](https://github.com/aio-libs/aiohttp-devtools) for easy development.

Installs dependencies in a volume so they can easily be reinstalled without creating a new Container.

# Build and run
Start `docker-compose up` to build and run the docker container. Once its running you can access http://localhost:4000 in your web browser to see a simple welcome page. You can make changes in the files in the `volumes/web/` folder and it will the page reload automatically.

If you make changes to the Dockerfile just run `docker-compose build` to re-build the docker image.
