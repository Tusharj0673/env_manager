from flask import render_template, request, redirect, url_for, flash, session, Blueprint
from models.env_info_dao import EnvInfo
from models.user_dao import UserManager

# Create a Blueprint for main routes
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def start():
    return redirect(url_for('main.login'))

# Route to display the login form
@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        pwd = request.form.get('password')
        
        # Call the login function from models.py
        if UserManager.login_user(user, pwd):
            return redirect(url_for('dashboard.dashboard'))
        else:
            flash("Invalid username or password!")
            return redirect(url_for('main.login'))
    
    return render_template('login.html')

@main_bp.route('/logout', methods=['POST'])
def logout():
    user = session.get('username')  # Get the current logged-in user's username
    if user:
        # Call the logout function from models.py
        UserManager.logout_user(user)
    return redirect("/")
