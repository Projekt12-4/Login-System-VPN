# Flask Login System Overview
ee
## Setup & Installation

Make sure you have the latest version of Python installed.

<span>**Note: This repo has only been tested under Linux!**</span>


Clone repo to server
```bash
git clone <repo-url>
```

Quick Setup
```bash
python setup.py
```

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

