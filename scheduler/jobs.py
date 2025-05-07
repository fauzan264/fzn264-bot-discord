import os
import random
from utils import utils
from dotenv import load_dotenv
load_dotenv()

# CHANNEL_ID
GENERAL_CHANNEL = os.getenv("GENERAL_CHANNEL")
MLBB_CHANNEL = os.getenv("MLBB_CHANNEL")

# SCHEDULER
TODAY_WORDS_SCHEDULE_HOURS = os.getenv("TODAY_WORDS_SCHEDULE_HOURS")
TODAY_WORDS_SCHEDULE_MINUTES = os.getenv("TODAY_WORDS_SCHEDULE_MINUTES")
MABAR_SCHEDULE_HOURS = os.getenv("MABAR_SCHEDULE_HOURS")
MABAR_SCHEDULE_MINUTES = os.getenv("MABAR_SCHEDULE_MINUTES")

quotes = utils.load_file("/quotes.csv")
used_quotes = []

def setup_scheduler(bot, scheduler, logger):
    logger.info("Setting up scheduler...")

    # Jadwal kata-kata harian
    def daily_quote():
        available = [q for q in quotes if q not in used_quotes]
        if not available:
            used_quotes.clear()
            available = quotes
        
        selected = random.choice(available)
        used_quotes.append(selected)
        message = f"kata-kata hari ini: {selected['quotes']}"

        logger.info("Scheduling daily quote message")
        scheduler.add_job(
            utils.send_message,
            'cron',
            hour=TODAY_WORDS_SCHEDULE_HOURS,
            minute=TODAY_WORDS_SCHEDULE_MINUTES,
            timezone="Asia/Jakarta",
            args=[bot, GENERAL_CHANNEL, message]
        )

    # Jadwal mabar
    def daily_mabar():
        logger.info("Scheduling daily mabar message")
        scheduler.add_job(
            utils.send_message,
            'cron',
            hour=MABAR_SCHEDULE_HOURS,
            minute=MABAR_SCHEDULE_MINUTES,
            timezone="Asia/Jakarta",
            args=[bot, MLBB_CHANNEL, "Apakah tidak ada per-mabaran duniawi hari ini?"]
        )

    daily_quote()
    daily_mabar()