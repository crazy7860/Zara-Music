## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
API_ID = int(getenv("API_ID", "18158594"))
API_HASH = getenv("API_HASH", "568e61f29c602a32da4c44997143fc54")
OWNER_NAME = getenv("OWNER_NAME", "The_Death_Soul")
ALIVE_NAME = getenv("ALIVE_NAME", "Null")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "Zain_Assistant")
BOT_USERNAME = getenv("BOT_USERNAME", "Zara_Vcbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "null")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Love_Dear_Comrades")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ZaraSupport")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/be5169a49ee37ed42e718.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/0701358b0434a508af77c.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/0701358b0434a508af77c.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/0701358b0434a508af77c.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/0701358b0434a508af77c.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/0701358b0434a508af77c.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/0701358b0434a508af77c.jpg")
