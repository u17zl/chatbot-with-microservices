# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from .data import doctors


class DentistsName(Resource):

    def get(self, name):
        reply = {}
        print(name)
        for doctor in doctors:
            if name == doctor["name"]:
                reply = doctor
                return reply, 200, None
        return {"code": 404, "message": "Not Found"}, 404
        