from functools import lru_cache
from http import server

from pyrogram.client import Client

from app.config import BOT as CNF_BOT


@lru_cache()
def get_bot(cnf: CNF_BOT = CNF_BOT()) -> Client:
    return Client(
        cnf.SESSION_NAME, # type: ignore
        cnf.API_ID,
        cnf.API_HASH, # type: ignore
        bot_token=cnf.BOT_TOKEN,  # type: ignore
        #  proxy = {
        #     "scheme": "socks5",  # "socks4", "socks5" and "http" are supported
        #     "hostname": "localhost",
        #     "port": 9092
        # }
    )  # type: ignore

__all__ = ["get_bot"]
