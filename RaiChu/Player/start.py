
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from RaiChu.config import BOT_NAME as bn
from Process.filters import other_filters2
from time import time
from datetime import datetime
from Process.decorators import authorized_users_only
from RaiChu.config import BOT_USERNAME, ASSISTANT_USERNAME

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 ** 2 * 24),
    ("hour", 60 ** 2),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(other_filters2)
async def start(_, message: Message):
        await message.reply_text(
        f"""**I ᴀᴍ 𝒁𝒂𝒓𝒂 𝑽𝒄 𝑷𝒍𝒂𝒚𝒆𝒓   
ʙᴏᴛ 𝙾𝚆𝙽𝙴𝙳 ʙʏ [𝑯𝒖𝒔𝒔𝒂𝒊𝒏](https://t.me/The_Death_Soul)
Thanks to add me 😜**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍹𝐎𝐰𝐧𝐞𝐫🍹", url="https://t.me/The_Death_Soul"
                    ),
                    InlineKeyboardButton(
                        "🛡️𝐅𝐞𝐝𝐞𝐫𝐚𝐭𝐢𝐨𝐧🛡️", url="https://t.me/Death_Soul_Federation"
                    )
                  ],[
                    InlineKeyboardButton(
                       "🥂𝐒𝐮𝐩𝐩𝐨𝐫𝐭🥂", url="https://t.me/Love_Dear_Comrades"
                    ),
                    InlineKeyboardButton(
                        "🍸𝐔𝐩𝐝𝐚𝐭𝐞𝐬🍸", url="https://t.me/ZaraSupport"
                    )
                ],[
                    InlineKeyboardButton(
                        "➕𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )
