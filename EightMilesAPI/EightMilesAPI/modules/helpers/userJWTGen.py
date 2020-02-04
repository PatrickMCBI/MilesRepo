from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

class UserJWT(object):
    
    def __init__(self, arg):
        
        self.arg = arg
        self.email = self.arg["email"]
        self.pwd = self.arg["pwd"]
      

    # def UserJWTData(self):