import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        text=f"Hello {message.from_user.first_name},\nIm telegram to telegra.ph image uploader bot by @W4RR10R",
        disable_web_page_preview=True
    )         





