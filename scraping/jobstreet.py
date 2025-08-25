from discord import Embed
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

job_schedulers = [
    {
        "hour": 9,
        "minute": 00
    },
    {
        "hour": 15,
        "minute": 00
    },
    {
        "hour": 17,
        "minute": 40
    },
]

def jobstreet_scheduler(bot, scheduler, logger, channel_id, position, city):
    async def get_jobs(channel_id):
        # Setup headless browser
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        logger.info("Opening JobStreet page")
        position_job = position.lower().replace(" ", "-")
        city_job = city.lower().replace(" ", "-")
        driver.get(f"https://id.jobstreet.com/id/{position_job}-jobs/in-{city_job}")

        time.sleep(2)

        positions = driver.find_elements(By.CSS_SELECTOR, "a[data-testid='job-card-title']")
        companies = driver.find_elements(By.CSS_SELECTOR, "a[data-automation='jobCompany']")

        logger.info(f"Found {len(positions)} positions and {len(companies)} companies")

        if not positions or not companies:
            logger.warning("No job data found!")
            driver.quit()
            return

        try:
            channel = await bot.fetch_channel(channel_id)
            if not channel:
                logger.warning("Channel not found")
                driver.quit()
                return

            jobs_count = min(len(positions), len(companies))
            fields_per_embed = 10

            for batch in range(0, jobs_count, fields_per_embed):
                embed = Embed(
                    title=f"📢 Info Lowongan {position} di {city}",
                    description=f"Lowongan {position} di {city} #{batch + 1} - #{min(batch + fields_per_embed, jobs_count)}",
                    color=0x3498db
                )

                for i in range(batch, min(batch + fields_per_embed, jobs_count)):
                    title = positions[i].text[:256]
                    company = companies[i].text[:256]
                    url = positions[i].get_attribute('href')
                    embed.add_field(
                        name=f"{title} - {company}",
                        value=f"[Lihat detail]({url})"[:1024],
                        inline=False
                    )

                await channel.send(embed=embed)
                logger.info(f"Sent embed batch {batch // fields_per_embed + 1}")

        except Exception as e:
            logger.error(f"Failed to send embed: {e}")

        driver.quit()

    for job_scheduler in job_schedulers:
        logger.info(f"Scheduling daily jobstreet message")
        scheduler.add_job(
            lambda: bot.loop.create_task(get_jobs(channel_id)),
            'cron',
            hour=job_scheduler['hour'],
            minute=job_scheduler['minute'],
            timezone="Asia/Jakarta"
        )
