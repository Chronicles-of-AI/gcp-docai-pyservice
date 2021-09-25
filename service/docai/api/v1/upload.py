# Copyright (c) 2021 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os
from uuid import uuid4
from fastapi import APIRouter, File, UploadFile, Depends
import aiofiles
from docai.admin.controllers import user
from docai.admin import models
from docai.core.config import settings
from starlette import responses


router = APIRouter()


@router.post("/upload/pdf")
async def post_endpoint(
    file: UploadFile = File(...),
    current_user: models.User = Depends(user.get_current_active_superuser),
):
    filename = file.filename.lower().split(".")
    uid = str(uuid4())[-8:]
    save_file_name = os.path.join(settings.STORAGE_DIR, f"{uid}.pdf")
    if filename[-1] == "pdf":
        async with aiofiles.open(
            save_file_name,
            "wb",
        ) as out_file:
            content = await file.read()  # async read
            await out_file.write(content)  # async write
        response = {"Result": "OK", "upload_id": uid}
    else:
        response = {"Result": "Not OK", "Reason": "Please upload a PDF file!"}
    return response
