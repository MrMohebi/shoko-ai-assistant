import uvicorn
from loguru import logger


class Main:
    def __init__(self, _config):
        self.app = None
        self.config = _config

    def start(self):
        logger.info("Api Server Start")
        uvicorn.run('apps.Api.server:app',
                    host=self.config.host,
                    reload_delay=5,
                    port=self.config.port,
                    reload=False,
                    log_level="debug",
                    workers=1
                    )

