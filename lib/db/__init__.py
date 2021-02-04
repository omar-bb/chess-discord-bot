import os
import mysql.connector
from mysql.connector import errorcode

import typing
from apscheduler.triggers.cron import CronTrigger

class Database:
    def __init__(self, db_user, db_pass, db_host, db_name):
        self._cnx = mysql.connector.connect(user=db_user, password=db_pass,
                            host=db_host,
                            database=db_name)
        self._cur = self._cnx.cursor()

    def commit(self):
        print("commiting...")
        self._cnx.commit()

    def autosave(self, sched):
        sched.add_job(self.commit, CronTrigger(second=0))

    def execute(self, query, values: tuple = None):
        self._cur.execute(query, values or ())

    def fetchall(self) -> tuple:
        return self._cur.fetchall()

    def fetchone(self) -> tuple:
        return self._cur.fetchone()

    def __del__(self):
        self._cnx.close()
