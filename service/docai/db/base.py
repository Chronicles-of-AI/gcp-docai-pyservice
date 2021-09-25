# Copyright (c) 2021 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT


# Import all the models, so that Base has them before being
# imported by Alembic
from docai.db.base_class import Base  # noqa
from docai.admin.models.user import User  # noqa
