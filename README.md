# Telegram File Uploader Bot (Pyrogram)

This is a telegram bot that accepts files from users and uploads them to a configured URL. It uses the pyrogram library to interact with the telegram API.

## Setup

To set up the bot, you need to have python 3.6 or higher installed on your system. You also need to install the pyrogram library using pip:

`pip install pyrogram`

Then, you need to create a bot account on telegram using [@BotFather](https://t.me/BotFather) and get its token. You also need to get your own api_id and api_hash from [https://my.telegram.org](https://my.telegram.org).

Next, you need to edit the config.py file and fill in the following variables:

- api_id: Your telegram api_id
- api_hash: Your telegram api_hash
- bot_token: Your bot token from [@BotFather](https://t.me/BotFather)
- owner_id: Your telegram user id (optional, for logging purposes)
- url: The URL where you want to upload the files
- upload_file_key: The key name for the file parameter in the upload request
- secret_key: The key name for a secret parameter in the upload request (optional, for security purposes)
- secret_value: The value for the secret parameter in the upload request (optional, for security purposes)
- bot_username: Your bot username

Finally, you can run the bot.py file using python:

`python main.py`

The bot will start listening for messages from users. To use the bot, users need to send a file to it and wait for a response with the uploaded URL.

`--Thanks to Bing ChatGPT for generating this accurate README File`
