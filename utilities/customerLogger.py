import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s:PID- %(process)d: TID-%(thread)d: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p', force=True)

        logger=logging.getLogger()
        # filehandler=logging.FileHandler('.\\Logs\\automation.log',mode='a')
        # formatter=logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        # filehandler.setFormatter(formatter)
        # logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger
