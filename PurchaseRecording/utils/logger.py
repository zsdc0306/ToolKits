# import logging
#
#
# class Logger(object):
#     def __init__(self, logger_name):
#         formatter = logging.Formatter(fmt='%(asctime)s [%(levelname)s] %(module)s - %(message)s')
#         handler = logging.StreamHandler()
#         handler.setFormatter(formatter)
#         self.logger = logging.getLogger(logger_name).addHandler(handler)
#         self.logger.setLevel(logging.INFO)
#
#     def get_logger(self):
#         return self.logger
#
#
# my_logger = Logger("mylogger").get_logger()
