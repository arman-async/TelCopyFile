from app.bot import get_bot
from app.logger import logger

if __name__ == "__main__":
    logger.info("Starting bot...")
    get_bot().run()
