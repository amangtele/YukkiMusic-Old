##Config

import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
SESSION_NAME = getenv("SESSION_NAME", "BQBfLYOF7h0ac7MHEJG2Bfjbd6bTXVMMoRpEn-gKIIxcAx-ggLdRwuGxVLdHAH9FXFsg7bVsq_HNShpou-OwiCJoUQCHJpv-ubhgPWKvZS_bwh9_CvbST5fVmivd_VFMi_S6wAptJFQPH2khE17lKr3DenCe1ohikXEmxAJiw_uH9Uk7WSJzQ8VxcHCGGog0tX8wu2W7ENBHEJEj_gD7N7QGuiAVgzHEw1IUh5xkRDVtOLEK9bsnMxGP_D4x6Ad9_oCx4vZAe7JJWotNC8iq2sC4XVlaf6E856_7HTK5jGPtbYwNRwWHju_nsFL4W-k6LHXU-S1gM5duw70ytfYDPv2SbZ0THwA")
BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "54000"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
MONGO_DB_URI = getenv("MONGO_DB_URI")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001306851903"))
ASS_ID = int(getenv("ASS_ID", ""))
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
