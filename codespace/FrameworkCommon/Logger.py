import logging


def InitialDebugLog():

    ##Create logger
    logger = logging.getLogger('')
    logger.setLevel(logging.DEBUG)

    return logger