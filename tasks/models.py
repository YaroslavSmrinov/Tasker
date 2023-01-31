from database.base import base
from sqlalchemy import Column, Integer, String


class Task(base):
    __tab_name = 'tasks'
    id = Column(Integer, primary_key=True)
    text = Column(String)
