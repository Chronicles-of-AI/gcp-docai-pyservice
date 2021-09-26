# Copyright (c) 2021 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import json
from dotenv import load_dotenv

load_dotenv()

from fastapi.testclient import TestClient
from docai import app
from docai.core.config import settings


client = TestClient(app)


def get_access_token():
    login_data = {
        "username": settings.FIRST_SUPERUSER,
        "password": settings.FIRST_SUPERUSER_PASSWORD,
    }
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    return tokens


def test_upload_file() -> None:
    url = f"{settings.API_V1_STR}/upload/pdf"
    print(f"{url=}")
    files = {"file": open(settings.TEST_PDF, "rb")}
    tokens = get_access_token()
    headers = {
        "Authorization": "Bearer {}".format(tokens["access_token"]),
    }
    print(f"{files=}, {tokens=}, {headers=}")
    response = client.post(url, files=files, headers=headers)
    response_dict = json.loads(response.text)
    check_dict = response_dict
    check_dict.update(dict(upload_id=response_dict.get("upload_id")))
    assert response.status_code == 200
    assert response_dict == check_dict
