# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from .data import doctors


class Dentists(Resource):

    def get(self):
        reply = doctors

        return reply, 200, None