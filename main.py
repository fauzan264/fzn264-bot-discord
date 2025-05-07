from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import os
from dotenv import load_dotenv
from utils import utils
from discord import Intents
import random

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# CHANNEL_ID
GENERAL_CHANNEL = os.getenv("GENERAL_CHANNEL")
MLBB_CHANNEL = os.getenv("MLBB_CHANNEL")

# SCHEDULER
TODAY_WORDS_SCHEDULE_HOURS = os.getenv("TODAY_WORDS_SCHEDULE_HOURS")
TODAY_WORDS_SCHEDULE_MINUTES = os.getenv("TODAY_WORDS_SCHEDULE_MINUTES")

MABAR_SCHEDULE_HOURS = os.getenv("MABAR_SCHEDULE_HOURS")
MABAR_SCHEDULE_MINUTES = os.getenv("MABAR_SCHEDULE_MINUTES")

# create object intents
intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Active bot as {bot.user.name}")

rows = utils.load_file("cmd.csv")

used_quotes = []
for row in rows:
    cmd = row["key"]
    response = row["value"]

    if cmd == "landofdawn":
        @bot.command(name=cmd)
        async def _(ctx):
            users = [
                "585964449685569557",
                "732407057084317719",
                "220589035557486592",
                "403552045677674517",
                "349509405970137108",
                "229949010318721024"
            ]

            mentions = " ".join([f"<@{user}>" for user in users])
            await ctx.send(f"{mentions}, ayo mabar!")
    elif cmd == "kata-kata":
        
        quotes = utils.load_file("quotes.csv")

        @bot.command(name=cmd)
        async def _(ctx): 
            available_quotes = [quote for quote in quotes if quote not in used_quotes]
            if not available_quotes:
                used_quotes.clear()
                available_quotes = quotes

            choice_quotes = random.choice(quotes)
            used_quotes.append(choice_quotes)

            await ctx.send(choice_quotes['quotes'])
    else:
        @bot.command(name=cmd)
        async def _(ctx, response=response): await ctx.send(response)

    # CREATE SCHEDULER
    scheduler = AsyncIOScheduler()

    @bot.event
    async def on_ready():
        # KATA-KATA HARI INI
        channel_id = GENERAL_CHANNEL
        available_quotes = [quote for quote in quotes if quote not in used_quotes]
        if not available_quotes:
            used_quotes.clear()
            available_quotes = quotes
        message = random.choice(quotes)
        used_quotes.append(message)
        
        send_message = f"kata-kata hari ini: {message['quotes']}"
        
        scheduler.add_job(
            utils.send_message,
            'cron',
            hour=TODAY_WORDS_SCHEDULE_HOURS,
            minute=TODAY_WORDS_SCHEDULE_MINUTES,
            timezone="Asia/Jakarta",
            args=[bot, channel_id, send_message]
        )
        
        # MABAR
        channel_id = MLBB_CHANNEL
        message = "Apakah tidak ada per-mabaran duniawi hari ini?"
        
        scheduler.add_job(
            utils.send_message,
            'cron',
            hour=MABAR_SCHEDULE_HOURS,
            minute=MABAR_SCHEDULE_MINUTES,
            timezone="Asia/Jakarta",
            args=[bot, channel_id, message]
        )
        scheduler.start()

bot.run(TOKEN)