import os

API_ID = API_ID = 26368249

API_HASH = os.environ.get("API_HASH", "6cc3cfdeae65b6ae7f47fb828edf38f4")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6970138044:AAFZqpB32j0gFRTqtRtR6mL7fjngHsEDH5Q")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5684410709))

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5684410709").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


