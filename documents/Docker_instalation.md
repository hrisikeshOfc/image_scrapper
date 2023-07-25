# Docker Installation and Basic Functionalities Guide

## Table of Contents
1. **Introduction**
2. **Installing Docker**
    -  *Windows*
    -  *Linux (Ubuntu)*
    - *Mac*
3. **Basic Docker Functionalities**
    - *Running a Container*
    - *Listing Containers*
    - *Stopping a Container*
    - *Removing a Container*
    - *Pulling Docker Images*
    - *Building Docker Images*
    - *Managing Docker Images*
    - *Port Mapping*
    - *Viewing Logs*

---

## 1. Introduction

Docker is an open-source platform that allows you to develop, deploy, and run applications inside containers. Containers are lightweight, portable, and isolated environments that contain all the necessary dependencies to run your applications. In this guide, we will walk you through the installation process for Docker on different operating systems and cover some of the basic Docker functionalities.

---

## 2. Installing Docker




### 2.1 Docker Installation on Windows with WSL 2 and Ubuntu

Docker on Windows can be installed using WSL 2 (Windows Subsystem for Linux) along with Ubuntu. WSL 2 allows you to run a Linux kernel directly on Windows, providing better performance and improved compatibility for Docker. Let's go through the step-by-step installation process:



### 2.1.1 Install WSL 2

1. Open PowerShell as an administrator by right-clicking the Start button, selecting "Windows PowerShell (Admin)."

2. Run the following command to enable the WSL feature:
   ```powershell
   wsl --install
   ```
   This command will install WSL 2, the latest WSL Linux kernel, and set WSL 2 as the default version.

### 2.1.2 Install Ubuntu from Microsoft Store

1. Open the Microsoft Store from the Start menu.

2. Search for "Ubuntu" and select "Ubuntu" from the search results.

3. Click the "Install" button to download and install Ubuntu.

4. Launch Ubuntu from the Start menu. The first time you open it, it will take a few moments to set up.

### 2.1.3 Install Docker

1. Visit the official Docker website: https://www.docker.com/products/docker-desktop
2. Download the Docker Desktop installer.
3. Double-click the installer and follow the on-screen instructions.
4. After installation, Docker Desktop will run automatically, and you'll see the Docker icon in the system tray when it's running.

### 2.1.4 Verify Docker Installation

To verify that Docker is installed correctly and running, run the following command in the Ubuntu terminal:
```bash
docker --version
```

You should see the installed Docker version printed on the screen.

## 2.3. Basic Docker Functionalities

Now that you have Docker installed successfully, let's explore some basic Docker functionalities.

### [The list of basic Docker functionalities and commands generated in the previous content]

---

With Docker successfully installed on your Windows machine using WSL 2 and Ubuntu, you can now enjoy the benefits of containerization. Docker simplifies the process of managing and deploying applications, making it an essential tool for modern software development. Happy containerizing!### 2.2 Linux (Ubuntu)

1. Update your system's package index by running:
   ```
   sudo apt update
   ```
2. Install necessary dependencies:
   ```
   sudo apt install apt-transport-https ca-certificates curl software-properties-common
   ```
3. Add the Docker GPG key to your system:
   ```
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
   ```
4. Add the Docker repository to APT sources:
   ```
   echo "deb [signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list
   ```
5. Update APT index again:
   ```
   sudo apt update
   ```
6. Install Docker:
   ```
   sudo apt install docker-ce
   ```
7. Start and enable Docker service:
   ```
   sudo systemctl start docker
   sudo systemctl enable docker
   ```

### 2.3 Mac

1. Visit the official Docker website: https://www.docker.com/products/docker-desktop
2. Download the Docker Desktop installer.
3. Double-click the installer and follow the on-screen instructions.
4. After installation, Docker Desktop will run automatically, and you'll see the Docker icon in the menu bar when it's running.

---

## 3. Basic Docker Functionalities

### 3.1 Running a Container

To run a Docker container, use the following command:

```bash
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
```

*Example:*
```bash
docker run -d --name my_container nginx
```

### 3.2 Listing Containers

To list all running containers, use the following command:

```bash
docker ps
```

To list all containers (including stopped ones), add the `-a` flag:

```bash
docker ps -a
```

### 3.3 Stopping a Container

To stop a running container, use the following command:

```bash
docker stop CONTAINER_ID
```

### 3.4 Removing a Container

To remove a container, it must be stopped first. Use the following command to remove a stopped container:

```bash
docker rm CONTAINER_ID
```

### 3.5 Pulling Docker Images

To download a Docker image from Docker Hub, use the following command:

```bash
docker pull IMAGE_NAME:TAG
```

*Example:*
```bash
docker pull ubuntu:latest
```

### 3.6 Building Docker Images

To build a Docker image from a Dockerfile, use the following command:

```bash
docker build -t IMAGE_NAME:TAG PATH_TO_DOCKERFILE
```

*Example:*
```bash
docker build -t my_custom_image:latest .
```

### 3.7 Managing Docker Images

To list all Docker images on your system, use the following command:

```bash
docker images
```

To remove a Docker image, use the following command:

```bash
docker rmi IMAGE_NAME:TAG
```

### 3.8 Port Mapping

To map a container's port to a host port, use the `-p` flag with the `docker run` command:

```bash
docker run -p HOST_PORT:CONTAINER_PORT IMAGE
```

*Example:*
```bash
docker run -p 8080:80 nginx
```

### 3.9 Viewing Logs

To view the logs of a running container, use the following command:

```bash
docker logs CONTAINER_ID
```

---

This guide covered the installation of Docker on Windows, Linux (Ubuntu), and Mac, as well as some basic Docker functionalities. Docker is a powerful tool that can greatly simplify the development and deployment process of applications. Explore more advanced Docker features and configurations to unleash the full potential of containerization!