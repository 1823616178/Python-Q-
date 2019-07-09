"""
This script runs the GetBelleWomenIage application using a development server.
"""

from os import environ
from GetBelleWomenIage import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

# import sys
#
# activate_this = '/var/www/test/venv/bin/activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))
# sys.path.insert(0, '/var/www/test')
# from hello import app as application
