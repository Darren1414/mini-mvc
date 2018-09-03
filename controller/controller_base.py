#coding=utf-8

from dbs.models import db

class ControllerBase(object):
    def __init__(self):
        self.db = db