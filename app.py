<<<<<<< HEAD
from flask import Flask, session, redirect, url_for
from models.db import db
from routes import main_bp, dashboard_bp
import config # Importing session timeout manager
from models.env_info_dao import EnvInfo # Importing session timeout manager
from models.user_dao import UserManager
import atexit
from datetime import datetime, timedelta
from models.job import EnvJob
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
=======
from datetime import timedelta

import config
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from flask import Flask
from models.db import db
from models.env_info_dao import EnvInfo
from models.job import EnvJob
from models.user_dao import UserManager
from routes import main_bp, dashboard_bp
>>>>>>> 02185a2 (updated)

# Initialize the Flask app
app = Flask(__name__, static_folder='static')
app.config.from_object(config)
app.secret_key = 'karamazov'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10080)

# Initialize DB
db.init_app(app)

# Register blueprints
app.register_blueprint(main_bp)
app.register_blueprint(dashboard_bp)

# Set up the job scheduler
env_job = EnvJob()
env_job.start_scheduler(app)

# Stop scheduler on app exit
import atexit
atexit.register(env_job.stop_scheduler)

@app.before_request
def before_request():
    UserManager.session_timeout_manager()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

<<<<<<< HEAD

=======
>>>>>>> 02185a2 (updated)
