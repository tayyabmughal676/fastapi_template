"""
    Logging
    Enum

"""
import logging
from enum import Enum

file_name: str = "app.log"
file_mode: str = 'w'
message_format: str = '%(asctime)s %(name)s - %(levelname)s - %(message)s'
message_dateformat: str = '%d-%b-%y %H:%M:%S'

logging.basicConfig(filename=file_name, filemode=file_mode, format=message_format,
                    datefmt=message_dateformat)


class Levels(Enum):
    """
    Enums
    """
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4


class CheckSystemLogs:
    """
    pass_logs
    :param self
    :param log_level
    """

    @staticmethod
    def pass_logs(self: str, log_level: int):
        """
        :param self:
        :param log_level:
        :return:
        """
        match log_level:
            case Levels.DEBUG:
                logging.debug(self)
            case Levels.INFO:
                logging.info(self)
            case Levels.WARNING:
                logging.warning(self)
            case Levels.ERROR:
                logging.error(self)
            case Levels.CRITICAL:
                logging.critical(self)
