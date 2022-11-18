# Flask Login System Overview

## Setup & Installation

Make sure you have the latest version of Python installed.

Clone repo to server
```bash
git clone <repo-url>
```

Installing the required modules for python
```bash
pip install -r requirements.txt
```

# Starting The App

````bash
gunicorn main:app
````

Syntax: gunicorn <filename>:<application_name>
- filename without extensions
- server runs on <a href="http://127.0.0.1:8000/" target="_blank">Server</a>

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

