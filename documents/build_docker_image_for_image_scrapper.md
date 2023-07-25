## How to build the Docker Image for the Image Scrapper project in local system

## Steps:

1. Make sure the `Docker` is running. Otherwise, open the docker app to make sure that the Docker Daemon(The Docker daemon handles Docker objects like images, containers, networks, and volumes while listening for Docker API calls. To manage Docker services, a daemon can also talk to other daemons.)

2. Run the following commands to build the docker image

```bash
docker build -t image_scrapper .
```

this will create the docker images. 

3. Run the following command to run the docker container
```bash 
docker run -d -p 5000:5000 --name image_scrapper image_scrapper:latest
```