from discord.ext import commands

def register_land_of_dawn(bot, logger=None):
        @bot.command(name="landofdawn")
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

            if logger: logger.info(f"'landofdawn' used by {ctx.author}")
            await ctx.send(f"{mentions}, ayo mabar!")