
import json

from functools import wraps
from flask import request, jsonify

from modules.helpers.database import db_session
from modules.helpers.statuscode import Status
from modules.helpers.serialize import *
#from modules.model.usersmodel import *


def get_all():
    query = "CALL spGetAllColorCode()"
    data = [dict(zip(r.keys(), r)) for r in db_session.execute(query).fetchall()]
    return Status('200', 'Ok', data).status_code()

def get_single_color():
    query = "CALL spGetColorCode()"
    data = [dict(zip(r.keys(), r)) for r in db_session.execute(query).fetchall()]
    return Status('200', 'Ok', data).status_code()

def insert_color():
    formData = request.get_json()
    color = formData['colorName']
    query = "call spInserColor('"+color+"')"
    db_session.execute(query)
    status = Status('200', 'Successfully Added New Color!')
    return status.status_code()