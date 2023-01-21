import logging

def get_logs(level, format):

    logger= logging.getLogger()
    logger.setLevel(level)

    ch = logging.StreamHandler()
    ch.setLevel(level)

    formatter = logging.Formatter(format)
    
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    return logger


logger = get_logs(logging.WARNING, "%(asctime)s- " "%(levelname)s: %(message)s")
logger.debug("debug message")
logger.info("info message")
logger.warning("Warning message")