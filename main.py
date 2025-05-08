from discord.ext import commands
from discord import Intents
import os
from dotenv import load_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from scheduler.jobs import setup_scheduler
from command.register import register_all_commands
from utils.logger import setup_logger

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Logger, Scheduler, Bot
logger = setup_logger()
scheduler = AsyncIOScheduler()

# create object intents
intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    logger.info(f"Active bot as {bot.user.name}")
    setup_scheduler(bot, scheduler, logger)
    scheduler.start()

register_all_commands(bot, logger)

bot.run(TOKEN)