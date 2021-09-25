# Copyright (c) 2021 Nikhil Akki
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: Optional[int] = None
