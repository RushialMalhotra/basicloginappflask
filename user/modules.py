from flask import Flask, jsonify, request
from passlib.hash import pbkdf2_sha256
import uuid

class User:

    def signup(self):
        print(request.form)

        user = {
            "_id": str(uuid.uuid4().hex),
            "name": 'FFFFFFF',
            "email": 'FFFFF',
            "password": 'FFFFFFFF'
        }

        ## Encrypt the password
        # user['password'] = pbkdf2_sha256.encrypt(user['password'])


        return jsonify(user), 200