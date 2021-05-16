import os
import time 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegram import Update
from telegram.ext import CallbackContext


@Client.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(text=f"""Hello {message.from_user.first_name}
                             I am image2url bot.
            made by ~ [ʍǟֆȶɛʀʍɨռɖ ʋʀȶӼ™](https://telegra.ph/file/83d7a5c7158f429dcb72e.jpg)
                             """),
    time.sleep(2)   
    
    await message.reply_text(text=f"""Send me any image and i will send u it's telegra.ph link""")                  
                             


