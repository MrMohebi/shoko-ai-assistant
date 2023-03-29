from loguru import logger
import sys


def loggerInit():
    logger.remove()
    handler_id = logger.add(sys.stderr, level="INFO")
    logger.add(sink='run.log',
               format="{time} - {level} - {message}",
               level="INFO",
               rotation="200 MB",
               enqueue=True)

    logger.debug("Debug Mode On")
    logger.info("Hay, Let's start...")
