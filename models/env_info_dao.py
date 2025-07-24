<<<<<<< HEAD
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.sql import text
from models.db import db
from models.user_dao import UserManager
import os
import json
import requests
from flask import flash, session
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from flask import session
from flask import render_template, request, redirect, url_for, flash, session, Blueprint
from sqlalchemy.sql import text
from sqlalchemy import text
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from sqlalchemy import text
=======
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.interval import IntervalTrigger
from flask import flash
from models.db import db
from models.user_dao import UserManager
>>>>>>> 02185a2 (updated)
from notify.teams import TeamsNotifier

ASSIGNED_STATUS = 'Assigned'
UNASSIGNED_STATUS = 'Unassigned'
<<<<<<< HEAD
=======

>>>>>>> 02185a2 (updated)
class EnvInfo(db.Model):
    __tablename__ = 'env_info'

    id = db.Column(db.Integer, primary_key=True)
    env_name = db.Column(db.String(45), unique=True, nullable=False)
    assign_to = db.Column(db.String(45), nullable=True)
    status = db.Column(db.String(45), nullable=False)
    comment = db.Column(db.String(45), nullable=True)
    time = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    
    def to_dict(self):
     return {
        "id": self.id,
        "env_name": self.env_name,
        "assign_to": self.assign_to,
        "status": self.status,
        "comment": self.comment,
        "time": self.time,
        "created_at": self.created_at,
        "updated_at": self.updated_at
    }

    @property
    def is_assigned(self):
        return self.status == ASSIGNED_STATUS
    
    @classmethod
    def get_dashboard_records(cls):
<<<<<<< HEAD
     return [record.to_dict() for record in cls.query.all()]
    
=======
        return [ {k: v for k, v in record.to_dict().items() if v is not None} for record in cls.query.all() ]

>>>>>>> 02185a2 (updated)
    @staticmethod
    def update_env_status(env_name, username, time, comment, status=ASSIGNED_STATUS):
     env = EnvInfo.query.filter_by(env_name=env_name).first()

     if env:
        env.status = status
        env.assign_to = username
        env.comment = comment
        env.time = time
        env.updated_at = datetime.utcnow()

        db.session.commit()
        return env.to_dict()
     else:
        raise ValueError(f"Environment '{env_name}' not found.")

    @staticmethod
    def update_env_status_as_unassigned(env_name):
     return EnvInfo.update_env_status(
        env_name=env_name,
        username='',
        time='',
        comment='',
        status=UNASSIGNED_STATUS
    )

    @staticmethod
    def get_assigned_envs():
     assigned_envs = EnvInfo.query.filter_by(status=ASSIGNED_STATUS).all()
     return [env.to_dict() for env in assigned_envs]

    @staticmethod
    def create_env_info(env_name):
     new_env = EnvInfo(
        env_name=env_name,
        status=UNASSIGNED_STATUS,
        assign_to='',
        comment='',
        time=''
    )
     db.session.add(new_env)
     db.session.commit()
     return new_env.to_dict()

        
    @classmethod
    def checkout_env(cls, env_name, username, comment, time):    
        env = cls.query.filter_by(env_name=env_name).first()
        if env:
         if env.is_assigned:
          flash(f'Environment {env_name} is already checked out.', 'warning')
         else:
            EnvInfo.update_env_status(env_name, username, time, comment)
            flash(f'Checked out environment: {env_name.upper()}', 'success')
            TeamsNotifier.env_checked_out(env_name, username, time, comment)
        else:
            flash(f'Environment {env_name} not found.', 'danger')

    @classmethod
    def return_env(cls, env_name):
        env = cls.query.filter_by(env_name=env_name).first()
        if env:
            if not env.is_assigned:
                flash(f'Environment {env_name} is already available.', 'warning')
            else:
                EnvInfo.update_env_status_as_unassigned(env_name)
                flash(f'Released environment: {env_name.upper()}', 'success')
                TeamsNotifier.env_released(env_name)
        else:
            flash(f'Environment {env_name} not found.', 'danger')

    @classmethod
    def add_env(cls, env_name):
        env = cls.query.filter_by(env_name=env_name).first()
        if env:
            flash(f'Environment {env_name} already exists.', 'warning')
        else:
            EnvInfo.create_env_info(env_name)
            flash(f'Added environment: {env_name}', 'success')
