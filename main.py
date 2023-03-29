from utils.logger import loggerInit
from utils.Base import ReadConfig
from loguru import logger
import pathlib


loggerInit()

CONFIG_FILE = str(pathlib.Path.cwd()) + "/configs/apps.toml"
if not pathlib.Path(CONFIG_FILE).exists():
    raise FileNotFoundError("Cant find configs/apps.toml")

config = ReadConfig().parseFile(CONFIG_FILE)


def start():
    ctrlConfig = config.Controller
    try:
        pass
    except KeyboardInterrupt:
        logger.info('Caught Ctrl-C, Exiting.')
        exit()


if __name__ == '__main__':
    start()

