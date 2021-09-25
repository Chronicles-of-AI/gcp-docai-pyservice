<!--
 Copyright (c) 2021 Nikhil Akki
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->

## Python based RESTful service for GCP Document AI

put this file in ./service directory with file name as '.env' 
```.env
DOMAIN=localhost
DOCKER_IMAGE_BACKEND=docai-pyservice

; # Backend
BACKEND_CORS_ORIGINS=["http://localhost:3000"]
PROJECT_NAME=docai-pyservice
SECRET_KEY=changethis
FIRST_SUPERUSER=admin@docai.com
FIRST_SUPERUSER_PASSWORD=changethis

USERS_OPEN_REGISTRATION=False

; # Postgres
POSTGRES_SERVER=0.0.0.0
POSTGRES_USER=postgres
POSTGRES_PASSWORD=changethis
POSTGRES_DB=postgres

SERVER_NAME=docai-service
SERVER_HOST=http://0.0.0.0
PROJECT_NAME=docai-service

; # Document AI GCP configuration
PROJECT_ID=<gcp project id>
LOCATION='us' # Format is 'us' or 'eu'
PROCESSOR_ID=<find process id from cloud console> # Create processor in Cloud Console
STORAGE=./storage
```

> Author - Nikhil Akki

