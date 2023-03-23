from pyrogram import Client, filters
# from pyrogram.handlers import MessageHandler, CommandHandler
import requests
import os

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

owner_id = os.getenv("OWNER_ID")
url = os.getenv("URL")
upload_file_key = os.getenv("UPLOAD_FILE_KEY")
secret_key = os.getenv("SECRET_KEY")
secret_value = os.getenv("SECRET_VALUE")
bot_username = os.getenv("BOT_USERNAME")

app = Client(
    bot_username,
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

# @app.on_message()
# async def my_handler(client, message):
#     await client.send_message(messacd /mge.chat.id, "Your message has been forwarded to me.")
#     await message.reply_text("Hello")

def is_owner(client, message):
    allowed = False
    user = message.from_user
    if user.id == int(owner_id):
        allowed = True
    return allowed

@app.on_message(filters.command("start"))
async def start_command(client, message):
    if(is_owner(client, message)):
        await message.reply_text("Hello!")
    else:
        await message.reply_text("You are not the owner.")

@app.on_message(filters.document)
async def handle_file_upload(client, message):
    if(is_owner(client, message)):
        try:
            file_path = await client.download_media(message.document)
            files = {upload_file_key: open(file_path, 'rb')}
            data = {secret_key: secret_value}
            r = requests.post(url, files=files, data=data)
            os.remove(file_path)
            await message.reply_text("File uploaded successfully.")
        except Exception as e:
            await message.reply_text("Something went wrong:\n"+str(e))
            await message.reply_text("Backtrace:\n"+str(traceback.format_exc()))
    else:
        await message.reply_text("You are not the owner.")


# app.add_handler(MessageHandler(handle_file_upload, filters=filters.document))
# app.add_handler(MessageHandler(is_owner))
# app.add_handler(CommandHandler("start", start_command))
app.run()
