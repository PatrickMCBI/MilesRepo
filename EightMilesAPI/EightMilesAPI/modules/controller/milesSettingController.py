
import json

from functools import wraps
from flask import request, jsonify

from modules.helpers.database import db_session
from modules.helpers.statuscode import Status
from modules.helpers.serialize import *
from modules.model.usersmodel import *

"""
Create API function here
"""

def get_all_setting():

    query = "CALL spSelect8milesdetails()"
    data = [dict(zip(r.keys(), r)) for r in db_session.execute(query).fetchall()]
    print("---xxxx ", data)
    return Status('200', 'Ok', data).status_code()


