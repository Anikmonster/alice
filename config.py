import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 22431683
API_HASH = "6ab71bcb282fdf6ac3198399e8a2e2ae"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "8129555741:AAG2Hdp2ZUaVz1jrQS3ApVHNaofnRR8lbhs"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://Shadow12:Shadow12@cluster0.ddkep.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002292555984

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 6993303142

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/all_anime_in_offcial_hindi"
SUPPORT_GROUP = "https://t.me/OTAKU_ANIME_GC"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQFNtIsASqX09sXO5pfcY21W0gh9aZ0Gd2WQ3a8p5ryzVwNwikoTW_ocJ1BxL6oUD22ZHkjQLhU7x9FS_LIG0U2uWB2IowJsHNbH9VT8P5vlo_FMTlcY5IFTg9ltROVuLUuEcH3ZUwmfTEWE6t20M6MskJwN59LfixqN1nkbKX-iOXTM3Y3PTE5GYPmdjZHK0JSxIl4aGEkR2TklCXVgeakXWp95ZcVBlB-6h_jCqYfmWfwT6WPyYcc-ELXCco-SwwXfBSZPglxMDX8IGmKDCPF_gXcMOe81CENNmWeksOy8yrcr3IT7Kh9ghLCYlrhPCeOuT2K0UikTXYScJTc9WbpVV7ey5gAAAAG5nyIVAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/642493e5920e285cce40f-60df85227dd104b78d.jpg"

PING_IMG_URL = "https://graph.org/file/642493e5920e285cce40f-60df85227dd104b78d.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/642493e5920e285cce40f-60df85227dd104b78d.jpg"
STATS_IMG_URL = "https://graph.org/file/642493e5920e285cce40f-60df85227dd104b78d.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/642493e5920e285cce40f-60df85227dd104b78d.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/642493e5920e285cce40f-60df85227dd104b78d.jpg"
STREAM_IMG_URL = "https://graph.org/file/642493e5920e285cce40f-60df85227dd104b78d.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/642493e5920e285cce40f-60df85227dd104b78d.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/642493e5920e285cce40f-60df85227dd104b78d.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/642493e5920e285cce40f-60df85227dd104b78d.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/642493e5920e285cce40f-60df85227dd104b78d.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/642493e5920e285cce40f-60df85227dd104b78d.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
