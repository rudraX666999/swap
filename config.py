import os

API_ID = API_ID = 26484988

API_HASH = os.environ.get("API_HASH", "8d6e625fe3e296b4b6bd4817aca39ec5")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7468556574:AAHSrlHtt1KwqKw0LcI4sasdGws5L17muRQ")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6888054311))

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6888054311").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


