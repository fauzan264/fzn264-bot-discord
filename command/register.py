from .csv_command import register_csv_command
from .kata_kata import register_kata_kata
from .land_of_dawn import register_land_of_dawn

def register_all_commands(bot, logger=None):
    register_csv_command(bot, logger)
    register_kata_kata(bot, logger)
    register_land_of_dawn(bot, logger)