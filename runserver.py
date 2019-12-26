"""
This script runs the BellRPi application using a development server.
"""

from os import environ
from RPiBellsScheduler import app


if __name__ == '__main__':
    # Specify the server host.
    HOST = environ.get('SERVER_HOST', 'localhost')
    
    # Specify the server port.
    try:
        PORT = int(environ.get('SERVER_PORT', '7007'))
    except ValueError:
        PORT = 7007
    
    # Run the application on local development server.
    app.run(HOST, PORT, True)
