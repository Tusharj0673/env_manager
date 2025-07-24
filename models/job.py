from datetime import datetime, timedelta
<<<<<<< HEAD
from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.sql import text
import os
from models.env_info_dao import EnvInfo
from models.user_dao import UserManager
import json
import requests
from flask import flash, session
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from flask import session
from models.user_dao import UserManager
from flask import render_template, request, redirect, url_for, flash, session, Blueprint
from sqlalchemy.sql import text
from sqlalchemy import text
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from sqlalchemy import text
from models.env_info_dao import EnvInfo
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from notify.teams import TeamsNotifier

=======

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from models.env_info_dao import EnvInfo
from models.user_dao import UserManager
from notify.teams import TeamsNotifier


>>>>>>> 02185a2 (updated)
class EnvJob:
    def __init__(self):
        self.scheduler = None

    def auto_release_env(self, app):
     with app.app_context():
        assigned_envs = EnvInfo.get_assigned_envs()

        for env in assigned_envs:
            env_name = env.get("env_name")
            updated_date = env.get("updated_at")
            
            try:
                hours = int(env.get("time", 0))
            except (ValueError, TypeError):
                hours = 0

            if not updated_date:
                continue

            expiration_time = updated_date + timedelta(hours=hours)
            now = datetime.utcnow()

            if now >= expiration_time:
                EnvInfo.update_env_status_as_unassigned(env_name)

    def start_scheduler(self, app):
        if self.scheduler and self.scheduler.running:
            print("Scheduler is already running.")
            return

        self.scheduler = BackgroundScheduler()
        self.scheduler.add_job(
            func=lambda: self.auto_release_env(app),
            trigger=IntervalTrigger(seconds=60),
            id='env_scheduler_task',
            replace_existing=True
        )
        self.scheduler.start()
        print("Scheduler started with a recurring task.")

    def stop_scheduler(self):
        if self.scheduler:
            self.scheduler.shutdown(wait=False)
            print("Scheduler stopped.")
            self.scheduler = None
        else:
            print("Scheduler was not running.")
