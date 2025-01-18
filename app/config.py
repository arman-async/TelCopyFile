from dotenv import load_dotenv
from os import getenv

load_dotenv()

class BOT:
    API_ID = int(getenv("API_ID")) # type: ignore
    API_HASH = getenv("API_HASH")
    BOT_TOKEN = getenv("BOT_TOKEN")
    OWNER_ID = int(getenv("OWNER_ID")) # type: ignore
    SESSION_NAME = getenv("SESSION_NAME")
    WORKERS = int(getenv("WORKERS", 256))


class STATIC_MESSAGE:
    start = "Hi i willing to serve"
    ping = "Pong 👌 - I wake up"
    help = "Send me the files. I copy the files and send it again | the benefit of this is that eight files are changed"
    suffix = "\n"*2 + "It was copied 🫡"