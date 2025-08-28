from discord import Embed
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import asyncio

job_schedulers = [
    {
        "hour": 9,
        "minute": 0
    },
    {
        "hour": 13,
        "minute": 0
    },
    {
        "hour": 16,
        "minute": 0
    },
    {
        "hour": 20,
        "minute": 0
    },
]

def jobstreet_scheduler(bot, scheduler, logger, channel_id, position, city):
    async def get_jobs(channel_id):
        position_job = position.lower().replace(" ", "-")
        city_job = city.lower().replace(" ", "-")
        response = requests.get(f"https://id.jobstreet.com/id/{position_job}-jobs/in-{city_job}", "html")
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, "html.parser")
            
            positions = soup.select("a[data-testid='job-card-title']")
            companies = soup.select("a[data-automation='jobCompany']")

            if not positions or not companies:
                logger.warning("No job data found!")
            else:
                try:
                    channel = await bot.fetch_channel(channel_id)

                    job_count = min(len(positions), len(companies))
                    print(job_count)
                    fields_per_embed = 10

                    for batch in range(0, job_count, fields_per_embed):
                        embed = Embed(
                            title=f"📢 Info Lowongan {position} di {city}",
                            description=f"Lowongan {position} di {city} #{batch + 1} - #{min(batch + fields_per_embed, job_count)}",
                            color=0x3498db
                        )

                        for i in range(batch, min(batch + fields_per_embed, job_count)):
                            title = positions[i].get_text(strip=True)
                            company = companies[i].get_text(strip=True)
                            url = f"https://id.jobstreet.com{positions[i].get("href")}"

                            embed.add_field(
                                name=f"{title} - {company}",
                                value=f"[Lihat detail]({url})"[:1024],
                                inline=False
                            )

                        await channel.send(embed=embed)
                        logger.info(f"Sent embed batch {batch // fields_per_embed + 1}")
                except Exception as e:
                    logger.error(f"Failed to send embed: {e}")
        else:
            print(f"Failed get page: {response.status_code}")
        await asyncio.sleep(120)
    

    for job_scheduler in job_schedulers:
        logger.info(f"Scheduling daily jobstreet message")
        scheduler.add_job(
            lambda: bot.loop.create_task(get_jobs(channel_id)),
            'cron',
            hour=job_scheduler['hour'],
            minute=job_scheduler['minute'],
            timezone="Asia/Jakarta"
        )
