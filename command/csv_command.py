from utils import utils

def register_csv_command(bot, logger=None):
    rows = utils.load_file("cmd.csv")
    for row in rows:
        cmd = row["key"]
        response = row["value"]

        @bot.command(name=cmd)
        async def _(ctx, response=response):
            if logger: logger.info(f"'{cmd}' used by {ctx.author}")
            await ctx.send(response)