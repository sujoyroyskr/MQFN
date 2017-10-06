import logging
import os

PORT = 15333
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# LOG_FILEPATH = "/srv/webapps/BBMQ/logs/bbmq.log"
LOG_FILEPATH = os.path.join(BASE_DIR, "logs", "bbmq.log")
LOG_LEVEL = logging.DEBUG
SERVER_MAX_QUEUED_CON = 5
TOPICS = ["PR_PAYLOADS"]
CLIENT_PUBLISHER = "PRODUCER"
CLIENT_SUBSCRIBER = "CONSUMER"
MAX_MESSAGE_SIZE = 65536
SERVER_ACKNOWLEDGEMENT = "ROGER"
CLIENT_SHUTDOWN_SIGNAL = "SHUTDOWN"
CONSUMER_REQUEST_WORD = "FETCH"
INVALID_PROTOCOL = "UNKNOWN_WORD"
EMPTY_QUEUE_MESSAGE = "QUEUE EMPTY"
PRODUCER_ACK_MESSAGE = "ACKNOWLEDGED"
CLOSE_CONNECTION_SIGNAL = "CLOSE_CON"
HELP_INSTRUCTIONS = os.path.join(BASE_DIR, "help_instructions.txt")
PID_FILEPATH = os.path.join(BASE_DIR, "tmp")


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOG_FILEPATH,
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'server_daemon': {
            'handlers': ['file'],
            'propagate': False
        },
        'server_daemon_console_logger': {
            'handlers': ['console'],
            'propagate': False
        }
    }
}