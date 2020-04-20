"""
Class that extends flask config and can be extended itself
"""

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'yikes'


