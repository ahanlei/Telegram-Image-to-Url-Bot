import os
import uuid
import shutil
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from auth import Vauth
from telegraph import upload_file


@Client.on_message(filters.photo)
async def getimage(client, message):
    tmp = os.path.join("_Hacked_", str(message.chat.id))
    if not os.path.isdir(tmp):
        os.makedirs(tmp)
    img_path = os.path.join(tmp, str(uuid.uuid4()) + ".jpg")
    dwn = await message.reply_text("Uploading to my server and analyzing...", True)
    img_path = await client.download_media(message=message, file_name=img_path)
    await dwn.edit_text("ETA: > sec[░░░░░░              ]")
    await dwn.edit_text("ETA: > sec[░░░░░░░░░░░░        ]")
    await dwn.edit_text("ETA: > sec[░░░░░░░░░░░░░░░░░░░░]")
    await dwn.edit_text("Sending...")
    
    

    try:
        response = upload_file(img_path)
    except Exception as e:
        await dwn.edit_text(f"Oops something went wrong\n{error}")
        return
    await dwn.edit_text(
        text=f"<b>Link :-</b> <code>https://telegra.ph{response[0]}</code>",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Open Link", url=f"https://telegra.ph{response[0]}"),
                                            InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}"),
                                            InlineKeyboardButton(text="Group Link", url=f"https://t.me/vrtxmusic")
                                            ]])
    )
    shutil.rmtree(tmp, ignore_errors=True)
    
