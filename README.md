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

# Backend
BACKEND_CORS_ORIGINS=["http://localhost:3000"]
PROJECT_NAME=docai-pyservice
SECRET_KEY=changethis
FIRST_SUPERUSER=admin@docai.com
FIRST_SUPERUSER_PASSWORD=changethis

USERS_OPEN_REGISTRATION=False

TEST_PDF=<file path>
# Postgres
POSTGRES_SERVER=0.0.0.0
POSTGRES_USER=postgres
POSTGRES_PASSWORD=changethis
POSTGRES_DB=postgres

SERVER_NAME=docai-service
SERVER_HOST=http://0.0.0.0
PROJECT_NAME=docai-service

# Document AI GCP configuration
PROJECT_ID=<gcp project id>
LOCATION='us' # Format is 'us' or 'eu'
PROCESSOR_ID=<find process id from cloud console> # Create processor in Cloud Console
STORAGE=./storage
```

### How to run?

Tested on Linux (Fedora 34) & WSL2 (Ubuntu 20.04).

```bash
# BELOW ACTION -> required only for first time setup
git clone https://github.com/Chronicles-of-AI/gcp-docai-pyservice.git

# REGULAR ACTION
cd gcp-docai-pyservice
docker-compose up -d

# BELOW ACTION -> required only for first time setup
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - # install poetry 
cd service
poetry install # install dependencies
poetry run bash prestart.sh # to setup DB schemas
poetry run bash tests.sh # to run tests
```

Features -

- [x] Document AI integration Sync
- [x] Docker support
- [x] Docker compose for local dev
- [x] User Login, registeration
- [x] Authentication with JWT
- [x] DB migrations setup using Alembic
- [x] Tests suite using Pytest
- [ ] Helper scripts to setup db and run migrations
- [ ] Document AI Async implementation
- [ ] gcloud deployment templates for cloud run/functions/bucket

> Author - Nikhil Akki

> License -
> [MIT](https://github.com/Chronicles-of-AI/gcp-docai-pyservice/blob/main/LICENSE)
