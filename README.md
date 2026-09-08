# Purpose
Sample dummy app to build a first container

# How to
> docker build -t python-dummy-app .
check the image has been created successfully
> docker images
run it
> docker run -d --name python-app -p 8000:8000 python-dummy-app
check container is running
> docker ps
check web server is running by browsing http://localhost:8000
stop it
> docker stop python-app
remove it
> docker rm python-app
