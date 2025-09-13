import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import logging
from datetime import datetime, timedelta
import os
import json

# load token from .env file
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

# handles log outputting rather than the terminal
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# set intents both in the dev UI and here
intents = discord.Intents.default()
intents.message_content = True


# Creates bot with '!' prefix -> !command
bot = commands.Bot(command_prefix="!", intents=intents)

# make a folder to store the chores data
# each file in the folder will be associated with a person
CHORES_DIR = "chores_data"
# create directory if it doesn't exist
os.makedirs(CHORES_DIR, exist_ok=True)


# runs the bot and tells it to use handler as the log handler
bot.run(token, log_handler=handler, log_level=logging.DEBUG)