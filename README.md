# Flask Login System Overview

## Setup & Installation

<span>**Note: This repo has only been tested under Linux!**</span>


1. Clone this repository to your Development environment assuming you have git already installed (clone using your ssh-keys)
```bash
git clone <repo-url>
```
\\
2. Install Docker Desktop under Windows 10 (with WSL Extension/Integration!!)\\
3. Install VSCode on Windows 10 \\
4. Start VSCode under Linux (assuming you're in the root dir of your git repo)\\
```bash
code .
```
... this will open Visual Studio Code from Windows (even though it was called out of a WSL2-Instance)
the main difference: your VSCode will connect to your WSL2-Linux Machine\\
5. Press CTRL + SHIFT + P - and select reopen in container (uses the devcontainer.json config)\\
6. Wait for it to setup everything you need (the postCreateCommand will install all requirements that youneed to use the application correctly)\\
7. Start your project using the instructions below  

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
# If you can't run gunicorn by itself
python3 -m gunicorn main:app
````

or 

````bash
# This script also checks if the environment variables are set
python3 start.py

````

- filename without extensions
- server runs on http://127.0.0.1:8000/

## Deploying the Server

Forward all traffic from nginx to gunicorn.
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

