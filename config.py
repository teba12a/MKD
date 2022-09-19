from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "11632645"))
API_HASH = getenv("API_HASH", "274995c77d98520c6be79828b22b743f")
BOT_TOKEN = getenv("BOT_TOKEN","5337470376:AAFiLxWpXJft4MGKn5lUIW_vbtYIvkjt9xQ")
BOT_NAME = getenv("BOT_NAME","𝑴𝒖𝒔𝒊𝒄 ♪ سنوو")
BOT_USERNAME = getenv("BOT_USERNAME", "HYJJp_bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "BOYKA_50")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "TeaMember")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/b0aefd5c3b634687f011f.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/2378384a1c3f7b4e4213e.jpg")
SESSION_NAME = getenv("SESSION_NAME", "--AgArFutt1z_SyOapN0V5b-Wo7uMxLWeQrTnKjYeBIefy9NoSNR0JfVtDrbC54QgdIjiOeUcQGcH9qPYU2ZkJWGw7LKiSbnWSkxuHh3bNyDrHr69WWv00O1s_hmDcctPmIlN4ZX4eUHlG1UYuoFcEoHob5eN4MRp921aewEvRxc6mCn_MIFfVJdYiKfD8gNIpoQLi55GgUbga2Q_5mEwkjVH9E_EQNpKesoxbPVPtR6fKrZlZ6VAwX880CC3Y_Rz8SQfGOsVw2DoLffwgc2v82mo2UamCi1dQ9zQRdHN8PquRzxGevufBTj3hs4Yot-SHBqjDKeMxq8Fvk0MKlOIZ9LUeAAAAASxokk8A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2139870419").split()))+ [5490392130]