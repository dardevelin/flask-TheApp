from flask import Flask
from flask_login import login_user, logout_user

from . import app
from . database import session, User

# solves most responses you need
from flask import render_template, request, Response, redirect, url_for, flash

# if authentication is needed, this is where you start
from flask_login import login_required, login_user, current_user
from werkzeug.security import check_password_hash

import json
from . import decorators


@app.route("/api/search/<name>", methods=['GET'])
@decorators.accept("application/json")
def api_search(name):
    results = session.query(User).filter(User.name.ilike("%{}%".format(name))).all()
    data = json.dumps([user.as_dictionary() for user in results])
    
    return Response(data, 200, mimetype="application/json")
