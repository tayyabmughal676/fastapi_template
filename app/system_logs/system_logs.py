import logging

logging.basicConfig(filename='app_level.log', filemode='w', format='%(asctime)s %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')


class checkSystemLogs:
    @staticmethod
    def passLogs(self: str, logLevel: int):
        """
        :param self:
        :param logLevel:
        :return:
        """
        match logLevel:
            case 0:
                logging.debug(self)
            case 1:
                logging.info(self)
            case 2:
                logging.warning(self)
            case 3:
                logging.error(self)
            case 4:
                logging.critical(self)
