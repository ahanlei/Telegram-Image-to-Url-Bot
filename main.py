import os
import uuid
import shutil
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from auth import Vauth
from telegraph import upload_file


"""
.vscode/
Get the config vars for the Client
"""

BOT_TOKEN = Vauth.BOT_TOKEN
API_ID = Vauth.API_ID
API_HASH = Vauth.API_HASH


"""
.vscode/
Get the Plugins 
"""

plugins= dict(
    root="workers",
)


Client(
    "ʍǟֆȶɛʀʍɨռɖ ʋʀȶӼ™",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=plugins,
    workers=50
).run()