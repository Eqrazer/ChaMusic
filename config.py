from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
SESSION_NAME = getenv("SESSION_NAME", "session")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "ChaHaeInBot")
ALIVE_NAME = getenv("ALIVE_NAME", "Cha Hae-In")
BOT_USERNAME = getenv("BOT_USERNAME")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/eqrazer/CHamusic")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "45"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "AnimeFunChat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "AinCradNetwork")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $ +").split())
OWNER_ID = list(map(int, getenv("OWNER_ID").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/9ed109ac540d36fbd44e0.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/dff230db49b1340590b71.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/5ef0c2e786365709ae1dd.png")

IMG_4 = getenv("IMG_4", "https://i.imgur.com/NNIlUG2.mp4")
IMG_5 = getenv("IMG_5", "https://i.imgur.com/ZVW6JMA.mp4")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/1daa11f5c22f9bac4d60a.jpg")
