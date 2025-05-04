from discord.ext import commands
import os
from dotenv import load_dotenv
from utils import utils
from discord import Intents
import random

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# create object intents
intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Active bot as {bot.user.name}")

rows = utils.load_file("cmd.csv")

for row in rows:
    cmd = row["key"]
    response = row["value"]

    if cmd == "landofdawn":
        @bot.command(name=cmd)
        async def _(ctx):
            users = [
                ""
            ]

            mentions = " ".join([f"<@{user}>" for user in users])
            await ctx.send(f"{mentions}, ayo mabar!")
    elif cmd == "kata-kata":
        
        quotes = utils.load_file("quotes.csv")
        used_quotes = []

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

bot.run(TOKEN)