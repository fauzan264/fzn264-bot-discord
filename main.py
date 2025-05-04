from discord.ext import commands
import os
from dotenv import load_dotenv
from utils import utils
from discord import Intents

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# create object intents
intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot aktif sebagai {bot.user.name}")

@bot.command(name="ping")
async def hello(ctx):
    await ctx.send("Pong!")

@bot.command(name="landofdawn")
async def mobile_legends_team(ctx):

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


@bot.command(name="indonesia")
async def indonesian(ctx):
    await ctx.send("Indonesia besar, Indonesia kuat, Indonesia cerah")
    
@bot.command(name="pelayan")
async def _(ctx): await ctx.send("Siap, tuan!")
    
@bot.command(name="kata-kata")
async def _(ctx): await ctx.send(utils.load_file())

# async def main():
#     # load all file command from folder "cmd"
#     for filename in os.listdir("./cmd"):
#         if filename.endswith(".py") and filename != "__init__.py":
#             try:
#                 await bot.load_extension(f"cmd.{filename[:-3]}")
#                 print(f"Memuat extension {filename[:-3]}")
#             except Exception as e:
#                 print(f"Gagal memuat extension {filename[:-3]}: {e}")

# @bot.event
# async def on_ready():
#     print(f"Bot aktif sebagai {bot.user.name}")
#     main()

bot.run(TOKEN)