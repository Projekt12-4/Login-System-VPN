# Flask Login System Overview

## Setup & Installation

<span>**Note: This repo has only been tested under Linux!**</span>


1. Clone this repository to your Development environment assuming you have git already installed (clone using your ssh-keys) &nbsp;
```bash
git clone <repo-url>
```
2. Install Docker Desktop under Windows 10 (with WSL Extension/Integration!!) &nbsp;
3. Install VSCode on Windows 10 &nbsp;
4. Start VSCode under Linux (assuming you're in the root dir of your git repo) &nbsp;
```bash
code .
```
... this will open Visual Studio Code from Windows (even though it was called out of a WSL2-Instance)
the main difference: your VSCode will connect to your WSL2-Linux Machine &nbsp;

5. Press CTRL + SHIFT + P - and select reopen in container (uses the devcontainer.json config) (assuming you've installed the RemoteContainerExtension) &nbsp;

6. Wait for it to setup everything you need (the postCreateCommand will install all dependencies that come with the project) &nbsp;

7. Start your project using the instructions below  &nbsp;

# Starting The App

````bash
# Simplest option of all
gunicorn main:app
````
Syntax: gunicorn <file>:<application_name>
- filename without extensions
- application name / the main instance in main 
  (*app - by default*)

or 

````bash
# If you can't run gunicorn as a standalone application
python3 -m gunicorn main:app
````

- syntax asforementioned
- server runs on http://127.0.0.1:8000/

## Setting up a reverse proxy

### NGINX Reverse Proxy Configuration
Forwards all traffic from nginx to gunicorn.
Nginx will act as a reverse proxy

````bash
 server {
    listen 80;
    server_name example.org;
    access_log  /var/log/nginx/example.log;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
  }
````
More information can be found here:

- https://hub.docker.com/_/nginx
- https://gunicorn.org/#deployment

## Deploying the application using Docker

- https://hub.docker.com/r/xqly/login-system

Pull image from the official docker registry
````bash
docker pull xqly/login-system:latest
````
Start the image
````bash
docker run login-system
````
the name can be replaced with the **image-id**
... the same can be achieved on a GUI-Level using [Portainer][1].

Since the app doesn't rely on a persistent data storage *(not yet)* and due to security precautions, it is strongly advised to deploy the application as a temporary container that removes itself after being stopped.










[1]: https://www.portainer.io/
