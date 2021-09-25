# Copyright (c) 2021 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os
from fastapi import APIRouter

from docai.gcp.extraction import process_document_sample
from docai.core.config import settings

project_id = settings.PROJECT_ID
location = settings.LOCATION
processor_id = settings.PROCESSOR_ID

router = APIRouter()


@router.post("/docai/form-parser")
def form_parser_sync(upload_id: str):
    file_path = os.path.join(settings.STORAGE_DIR, upload_id, "pdf")
    if os.path.exists(file_path):
        output = process_document_sample(project_id, location, processor_id, file_path)
        response = {"Result": "OK", "output": output}
    else:
        response = {"Result": "Not OK", "Reason": "Invalid upload_id!"}
    return response
