import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass

def log_time(func):
    def wrapper():
        start_time = datetime.now()
        func()
        end_time = datetime.now()