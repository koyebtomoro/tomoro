#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>ᴢᴇʙʀᴀ</a>\n○ sᴀʟᴜʀᴀɴ : <a href='https://t.me/zonabisa'>ғɪʟᴍ sᴜʙ ɪɴᴅᴏ | ᴢᴏɴᴀʙɪsᴀ</a>\n○ ɢʀᴏᴜᴘ : <a href='https://t.me/zonabisaroom'>ɢʀᴏᴜᴘ ᴄʜᴀᴛ | ᴢᴏɴᴀʙɪsᴀ</a>\n○ ʟɪsᴛ ʙᴏᴛ : <a href='https://t.me/zonabisabot'>ᴢᴏɴᴀʙɪsᴀ ʙᴏᴛ</a>\n○ ʜᴜʙᴜɴɢɪ ᴀᴅᴍɪɴ : <a href='https://t.me/zonabisacontactbot'>ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ | ᴢᴏɴᴀʙɪsᴀ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴛᴜᴛᴜᴘ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ᴢᴏɴᴀʙɪsᴀ', url='https://t.me/zonabisa')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
