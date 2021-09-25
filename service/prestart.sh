# Copyright (c) 2021 Nikhil Akki
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

#! /usr/bin/env bash

# Let the DB start
python prestart.py

# Run migrations
alembic upgrade head

# Create initial data in DB
python initial_data.py
