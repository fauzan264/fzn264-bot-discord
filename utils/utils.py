import csv

dir = "./data/"
def load_file(csv_file):
    print(csv_file)

    with open(dir+csv_file, "r") as file:
        csv_reader = csv.DictReader(file)
        rows = [row for row in csv_reader]
        return rows
    
async def send_message(bot, channel_id, message):
    try:
        channel = await bot.fetch_channel(channel_id)
        await channel.send(message)
    except Exception as e:
        print(f"Error: {e}, channel {channel_id} not found!")