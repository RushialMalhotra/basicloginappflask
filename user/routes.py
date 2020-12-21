from __main__ import app

from flask import Flask , request
from user.modules import User

@app.route('/user/signup', methods=['POST'])
def signup():
  signup_data = request.get_json()
  form_data = request.form.get('name')
  print('signUp data', signup_data, form_data)
  # return User().signup()

  if True:
    return {
      "Success" : True,
      "message" : "User Created successfully",
      "UserId" : "thisIs  user id" 
      }
  else:
    return 'Error creating User'
  return signup_data
  