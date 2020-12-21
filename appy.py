from flask import Flask,render_template , request
import pymongo

app = Flask(__name__)

# Routes
# from user import routes

# Database
client = pymongo.MongoClient('localhost',27017)
db = client.user_login_system


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/user/signup', methods=['POST'])
def signup():
  signup_data = request.get_json()
  form_data = request.form.get('name')
  print('signUp data', signup_data['password'], form_data)
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

if __name__ == '__main__':
    app.run(debug=True)