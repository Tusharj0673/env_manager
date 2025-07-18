from flask import render_template, request, redirect, url_for, flash, session, Blueprint
from models.env_info_dao import EnvInfo 
from notify.teams import TeamsNotifier
dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.before_request
def require_login():
    if not session.get('logged_in'):
        return redirect('/')

@dashboard_bp.route('/dashboard')
def dashboard():
    records = EnvInfo.get_dashboard_records()
    print("Loaded environments:", records)
    return render_template('dashboard.html', username=session.get('username'), environments=records)

@dashboard_bp.route('/checkout', methods=['POST'])
def checkout():
    env_name = request.form['env_name']
    comment = request.form['comment']
    time = request.form['hours']
    username = session.get('username')  # Get username from session

    EnvInfo.checkout_env(env_name, username, comment, time)
    return redirect(url_for('dashboard.dashboard'))

@dashboard_bp.route('/return/<env_name>', methods=['POST'])
def return_env_route(env_name):
    EnvInfo.return_env(env_name)
    return redirect(url_for('dashboard.dashboard'))

@dashboard_bp.route('/add', methods=['POST'])
def add_env_route():
    env_name = request.form['env_name']
    EnvInfo.add_env(env_name)
    return redirect(url_for('dashboard.dashboard'))
