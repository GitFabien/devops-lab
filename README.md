# Python Dummy App — Docker Exercise

## Purpose

This exercise introduces the basic Docker workflow by containerising a small Python web application.

You will learn how to:

* Build a Docker image from a `Dockerfile`
* List and inspect Docker images
* Create and run a container
* Map a container port to your local machine
* Check container status and logs
* Stop and remove a container

---

## Project Structure

Your project should contain:

```text
python-docker-app/
├── app.py
├── requirements.txt
└── Dockerfile
```

---

## 1. Build the Docker Image

From the project directory, build the image:

```bash
docker build -t python-dummy-app .
```

### What does this mean?

* `docker build` → build an image
* `-t python-dummy-app` → give the image a name
* `.` → use the current directory as the build context

Check that the image was created:

```bash
docker images
```

You should see something similar to:

```text
REPOSITORY         TAG       IMAGE ID       CREATED          SIZE
python-dummy-app   latest    abc123...      moments ago      ...
```

---

## 2. Run the Container

Create and start a container from the image:

```bash
docker run -d \
  --name python-app \
  -p 8000:8000 \
  python-dummy-app
```

### What does this mean?

| Option              | Meaning                                       |
| ------------------- | --------------------------------------------- |
| `-d`                | Run the container in the background           |
| `--name python-app` | Give the container a name                     |
| `-p 8000:8000`      | Map host port `8000` to container port `8000` |
| `python-dummy-app`  | Image used to create the container            |

The port mapping is:

```text
Your computer                 Container
localhost:8000  ────────────>  :8000
```

---

## 3. Check the Container

Check currently running containers:

```bash
docker ps
```

You should see:

```text
CONTAINER ID   IMAGE              STATUS          PORTS
abc123...      python-dummy-app   Up ...          0.0.0.0:8000->8000/tcp
```

To see **all** containers, including stopped ones:

```bash
docker ps -a
```

---

## 4. Test the Web Application

Open a browser and visit:

```text
http://localhost:8000
```

You should see a message from the Python application.

You can also test it from the command line:

```bash
curl http://localhost:8000
```

---

## 5. Check the Container Logs

If the application is not working, the first thing to check is the container logs:

```bash
docker logs python-app
```

To continuously follow the logs:

```bash
docker logs -f python-app
```

Press `Ctrl+C` to stop following the logs.

---

## 6. Stop the Container

Stop the running container:

```bash
docker stop python-app
```

Check its status:

```bash
docker ps
```

The container should no longer appear because `docker ps` only shows running containers.

To see it:

```bash
docker ps -a
```

You should see the container with a status similar to:

```text
Exited (0)
```

---

## 7. Start the Container Again

Stopping a container does **not** delete it.

Start it again:

```bash
docker start python-app
```

Check:

```bash
docker ps
```

The application should be running again.

Try:

```text
http://localhost:8000
```

---

## 8. Remove the Container

Once you are finished, stop the container if it is running:

```bash
docker stop python-app
```

Then remove it:

```bash
docker rm python-app
```

Check:

```bash
docker ps -a
```

The `python-app` container should no longer exist.

> **Important:** Removing a container does not remove the Docker image.

Check your image:

```bash
docker images
```

You should still see:

```text
python-dummy-app
```

---

## 9. Complete Cleanup

If you also want to remove the image:

```bash
docker rmi python-dummy-app
```

Check:

```bash
docker images
```

---

# Docker Workflow

The exercise demonstrates the basic Docker lifecycle:

```text
Dockerfile
    │
    ▼
docker build
    │
    ▼
Docker Image
    │
    │ docker run
    ▼
Docker Container
    │
    ├── docker ps
    ├── docker logs
    ├── docker stop
    │
    ▼
Stopped Container
    │
    │ docker rm
    ▼
Removed Container
```

Remember:

**Image → Container**

A Docker image is the template used to create a container.

A container is a running (or stopped) instance created from an image.

---

# Useful Commands

| Task                    | Command                                                         |
| ----------------------- | --------------------------------------------------------------- |
| Build image             | `docker build -t python-dummy-app .`                            |
| List images             | `docker images`                                                 |
| Run container           | `docker run -d --name python-app -p 8000:8000 python-dummy-app` |
| List running containers | `docker ps`                                                     |
| List all containers     | `docker ps -a`                                                  |
| View logs               | `docker logs python-app`                                        |
| Follow logs             | `docker logs -f python-app`                                     |
| Stop container          | `docker stop python-app`                                        |
| Start container         | `docker start python-app`                                       |
| Remove container        | `docker rm python-app`                                          |
| Remove image            | `docker rmi python-dummy-app`                                   |

---

# Troubleshooting

### Port 8000 is already in use

You may see an error saying that port `8000` is already allocated.

Use another port on your computer:

```bash
docker run -d \
  --name python-app \
  -p 8080:8000 \
  python-dummy-app
```

Then browse to:

```text
http://localhost:8080
```

Notice that the application is still listening on **port 8000 inside the container**.

---

### Container immediately stops

Check the logs:

```bash
docker logs python-app
```

Then check its status:

```bash
docker ps -a
```

---

### I changed `app.py`

Changing your source code does not automatically change the Docker image.

Rebuild the image:

```bash
docker build -t python-dummy-app .
```

Then remove the old container and create a new one:

```bash
docker rm -f python-app
```

```bash
docker run -d \
  --name python-app \
  -p 8000:8000 \
  python-dummy-app
```

---

# Challenge

Once the basic exercise works, try the following:

1. Change the message displayed by the Python application.
2. Rebuild the Docker image.
3. Stop and remove the old container.
4. Start a new container.
5. Verify that your changes are visible in the browser.
6. Try running two containers from the same image using different host ports.

For example:

```text
localhost:8000  → Container 1
localhost:8001  → Container 2
```

This demonstrates an important Docker concept:

> **One image can be used to create multiple containers.**

