import logging



class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(
            filename="automation.log",
            format="%(asctime)s - %(levelname)s - %(message)s",
            level=logging.INFO
        )

        logger = logging.getLogger()
        return logger