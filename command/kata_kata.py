from discord.ext import commands
import random
from utils import utils

used_quotes = []

def register_kata_kata(bot, logger=None):
    quotes = utils.load_file("quotes.csv")
    
    @bot.command(name="kata-kata")
    async def _(ctx): 
        available_quotes = [quote for quote in quotes if quote not in used_quotes]
        if not available_quotes:
            used_quotes.clear()
            available_quotes = quotes
        choice_quotes = random.choice(quotes)
        used_quotes.append(choice_quotes)

        if logger: logger.info(f"'kata-kata' used by {ctx.author}")
        await ctx.send(choice_quotes['quotes'])