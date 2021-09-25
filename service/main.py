# Copyright (c) 2021 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os
from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from docai.core.config import settings

# admin routes
from docai.admin.router import user_router, login_router

# api routes
from docai.api.v1 import upload_router, gcp_docai_router

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(user_router, prefix=f"{settings.API_V1_STR}/users", tags=["Admin"])
app.include_router(login_router, prefix=settings.API_V1_STR, tags=["Login"])
app.include_router(upload_router, prefix=settings.API_V1_STR, tags=["Upload"])
app.include_router(gcp_docai_router, prefix=settings.API_V1_STR, tags=["GCP Doc AI"])


os.makedirs(settings.STORAGE_DIR, exist_ok=True)


@app.get("/")
def health_check():
    return {"response": "Health check successful!"}
