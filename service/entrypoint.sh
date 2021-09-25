# Copyright (c) 2021 Nikhil Akki
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

set -e
set -x

uvicorn main:app --host=0.0.0.0