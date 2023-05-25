import argparse
import logging
from colorlog import ColoredFormatter

logger = logging.getLogger(name=__name__)
logger.setLevel(logging.INFO)
formatter = ColoredFormatter(
         "%(white)s%(asctime)10s | %(log_color)s%(levelname)6s | %(log_color)s%(message)6s",
        reset=True,
        log_colors={
            'DEBUG':    'cyan',
            'INFO':     'yellow',
            'WARNING':  'green',
            'ERROR':    'red',
            'CRITICAL': 'red,bg_white',
        },
    )
formatter = logging.Formatter(formatter)

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)
# def init_logger(level:int) ->None :
#     formatter = ColoredFormatter(
#          "%(white)s%(asctime)10s | %(log_color)s%(levelname)6s | %(log_color)s%(message)6s",
#         reset=True,
#         log_colors={
#             'DEBUG':    'cyan',
#             'INFO':     'yellow',
#             'WARNING':  'green',
#             'ERROR':    'red',
#             'CRITICAL': 'red,bg_white',
#         },
#     )
#     handler = logging.StreamHandler()
#     handler.setFormatter(formatter)
#     logger.addHandler(handler)
#     logger.setLevel(level)
