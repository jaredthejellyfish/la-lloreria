from flask import render_template, url_for, redirect
from flask_login import login_required, current_user
from flask import Blueprint, send_from_directory

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    return render_template("home.html", title='Home')

@main.route('/sw.js')
def sw():
    return send_from_directory('static', 'sw.js')


@main.route('/manifest.json')
def manifest():
    return send_from_directory('static', 'manifest.json')


@main.route('/app/static/js')
def app_js():
    return send_from_directory('static', 'javascript/app.js')


@main.route('/l-coin-logo.png')
def logo():
    return send_from_directory('static', 'images/l-coin-logo.png')
