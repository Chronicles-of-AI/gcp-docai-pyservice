# Copyright (c) 2021 Nikhil Akki
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from pydantic import BaseModel


class Msg(BaseModel):
    msg: str
