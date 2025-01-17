import uuid
from pathlib import Path
from random import randint
from tempfile import TemporaryDirectory

from pyrogram import filters
from pyrogram.client import Client
from pyrogram.enums import ChatAction
from pyrogram.types import Message

from app.config import STATIC_MESSAGE
from app.opration import change_hash

from .. import get_bot

client = get_bot()


@client.on_message(filters.command("start"))
async def start(client: Client, message: Message):
    await message.reply_text(STATIC_MESSAGE.start)


@client.on_message(filters.command("help"))
async def help(client: Client, message: Message):
    await message.reply_text(STATIC_MESSAGE.help)


@client.on_message(filters.command("ping"))
async def ping(client: Client, message: Message):
    await message.reply_text(STATIC_MESSAGE.ping)


@client.on_message(filters.media)
async def copy_media(client: Client, message: Message):
    temp_dir = TemporaryDirectory()
    filename = uuid.uuid1().hex
    filepath = Path(temp_dir.name) / filename
    
    status_msg = await message.reply_text("Status: Downloading...", reply_to_message_id=message.id)
    await message.download(str(filepath.resolve()))
    
    await status_msg.edit_text("Status: Processing...")
    change_hash.Binary(file_path=filepath).add_to_end(randint(16, 128))

    if filepath.exists():
        await status_msg.edit_text("Status: Uploading...")
        await client.send_chat_action(message.chat.id, ChatAction.UPLOAD_DOCUMENT)
        caption = message.text if message.text else ""
        caption += STATIC_MESSAGE.suffix
        await client.send_document(
            message.chat.id,
            str(filepath.resolve()),
            caption=caption,
        )
    else:
        await status_msg.edit_text("File Not Found - again try again.")
    
    await status_msg.delete()
    temp_dir.cleanup()
