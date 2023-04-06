from pyrogram import Client, filters
from requests import post
from os import getenv, remove

API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = getenv("OWNER_ID")
URL = getenv("URL")
UPLOAD_FILE_KEY = getenv("UPLOAD_FILE_KEY")
SECRET_KEY = getenv("SECRET_KEY")
SECRET_VALUE = getenv("SECRET_VALUE")
BOT_USERNAME = getenv("BOT_USERNAME")

app = Client(
    BOT_USERNAME,
    api_id=API_ID, api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


def is_owner(client, message):
    if message.from_user.id == int(OWNER_ID):
        return True
    return False


@app.on_message(filters.command("start"))
async def start_command(client, message):
    if is_owner(client, message):
        await message.reply_text("Hello!")
    else:
        await message.reply_text("You are not the owner.")


@app.on_message(filters.document)
async def handle_file_upload(client, message):
    if is_owner(client, message):
        try:
            await message.reply_text("Downloading the file now.")
            FILE_PATH = await client.download_media(message.document)
            await message.reply_text("File downloaded successfully. Now uploading to server.")
            r = post(URL, files={"upload_file_key": open(FILE_PATH, "rb")}, data={"secret_key": SECRET_VALUE})
            remove(FILE_PATH)
            await message.reply_text("File uploaded successfully.")
        except Exception as e:
            await message.reply_text(f"Something went wrong:\n{e}")
            await message.reply_text(f"Backtrace:\n{traceback.format_exc()}")
    else:
        await message.reply_text("You are not the owner.")

app.run()
