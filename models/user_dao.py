
from models.db import db
from sqlalchemy.sql import text
import os
import json
import requests
from flask import flash, session
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from flask import session # Move this to user dao or rename it.
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from flask import session
from models.db import db


class UserManager(db.Model):
    __tablename__ = 'user_info'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), unique=True, nullable=False)
    email = db.Column(db.String(45), nullable=False)
    status = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(45), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime(1970, 1, 1, 0, 0, 1))
    updated_at = db.Column(db.String(45), default='1970-01-01 00:00:01')

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
    @staticmethod
    def Fetch_seper_class():
     from models.env_info_dao import EnvInfo
     return EnvInfo 
    
    @staticmethod
    def get_envs_by_status(status):
        EnvInfo=UserManager.Fetch_seper_class()
        try:
            return EnvInfo.query.filter_by(status=status).all() 
        except Exception as e:
            print(f"Error fetching environments: {e}")
            return []
    
    @staticmethod
    def update_user_status(username, status):
        EnvInfo=UserManager.Fetch_seper_class()

    @staticmethod
    def update_user_status(username, status):
        try:
            user = UserManager.query.filter_by(username=username).first()
            if user:
                user.status = status
                db.session.commit()
            else:
                print(f"[Warning] User '{username}' not found.")
        except Exception as e:
            print(f"Error updating user status: {e}")

    @staticmethod
    def authenticate_user(username, password):
        EnvInfo=UserManager.Fetch_seper_class()
        try:
         return UserManager.query.filter_by(username=username, password=password).first()
        except Exception as e:
            print(f"Error during authentication: {e}")
            return None
    
    @staticmethod
    def session_timeout_manager():
        if 'username' in session:
            session.permanent = True  # This will reset the timeout countdown on each request

    # Initialize the scheduler
    scheduler = BackgroundScheduler()

    @staticmethod
    def login_user(user, pwd):
        # Authenticate the user
        result = UserManager.authenticate_user(user, pwd)
        
        if result:
            # Successful login, set session data and update database
            session['logged_in'] = True
            session['username'] = user
            UserManager.update_user_status(user, 'logged_in')
            return True
        else:
            return False

    # Function to handle user logout
    @staticmethod
    def logout_user(user):
        # Clear session data and update the user's status to 'logged_out'
        session.clear()
        UserManager.update_user_status(user, 'logged_out')
