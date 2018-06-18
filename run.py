# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from str_validation import check_is_alphabet

#create a object of type Flask to access this framework
app = Flask(__name__)

# #create a object of type HTTPBasicAuth to access this framework
auth = HTTPBasicAuth()

#following are user/pass for access to http://localhost:xxxx/
users={"sundeep": "secret"}

#Check user password is valid
@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

#login is required to access /
@app.route('/app/val/v1.0', methods = ['GET', 'POST'])
@auth.login_required
def result():
    if request.method == 'POST':
        user_input = request.form.get('text')       #for Browser
        #user_input = request.data                 #for curl

        return jsonify({"user_string": user_input, "String_is_aplhabet":check_is_alphabet(user_input)})

    return '''<form method="POST">
                 string: <input type="text" name="text"><br>
                  <input type="submit" value="Submit"><br>
            </form>'''                                       #form data for Browser



if __name__ == '__main__':
    app.run(debug=True)
