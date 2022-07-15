from flask import Flask, render_template
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')


# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



# @app.route("/ar")
# def ar():
#     # Redirect user to login form
#     return redirect("/")