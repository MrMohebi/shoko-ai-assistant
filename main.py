import importlib

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
        from concurrent.futures import ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=len(ctrlConfig)) as p:
            for starter in ctrlConfig:
                if not pathlib.Path(f"apps/{starter}/main.py").exists():
                    logger.warning(f"Skip Controller {starter} ,Do Not Exist.")
                    continue
                else:
                    logger.success(f"Set Controller {starter}.")
                module = importlib.import_module('apps.' + starter + ".main")
                # Use the submit method of ThreadPoolExecutor
                task = p.submit(module.Main(ctrlConfig.get(starter)).start)
                print(task.exception())
    except KeyboardInterrupt:
        logger.info('Caught Ctrl-C, Exiting.')
        exit()


if __name__ == '__main__':
    start()

