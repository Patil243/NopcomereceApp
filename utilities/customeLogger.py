# import logging
#
# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename=".\\Logs\\automation.log" ,
#                         format='%(asctime)s :%(levelname)s: %(message)s', datefmt='%m/%d/%y %I:%M:%S %P')
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger

import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        if not os.path.exists(".\\Logs"):
            os.makedirs(".\\Logs")

        logger = logging.getLogger("nopCommerceLogger")  # Named logger
        logger.setLevel(logging.INFO)

        # To avoid adding multiple handlers if already added
        if not logger.handlers:
            file_handler = logging.FileHandler(".\\Logs\\automation.log")
            formatter = logging.Formatter('%(asctime)s :%(levelname)s: %(message)s', datefmt='%m/%d/%y %I:%M:%S %p')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger
