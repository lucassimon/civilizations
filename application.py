# -*- coding: utf-8 -*-

# Third

# Python
from os import getenv
from os.path import dirname, isfile, join
import logging
# Third
from dotenv import load_dotenv

# Apps

_ENV_FILE = join(dirname(__file__), '.env')

if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)


from apps import create_app

app = create_app(getenv('ENV') or 'default')

def log_handler(msg, level):
    # Redirecting the msg and level to logging library.
    getattr(logging, level)(msg)
    print(f'Msg: {msg} / Level: {level}')
    
if __name__ == '__main__':
    ip = '0.0.0.0'
    app.debug = True
    app.run(host=ip, port=8000, debug=True)
