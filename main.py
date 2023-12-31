import os, asyncio
import discord
from datetime import datetime
from schedule import create_daily_message_schedule, sleep_until
from dotenv import load_dotenv

load_dotenv()
discord_token = os.environ['DISCORD_BOT_TOKEN'] 

intents = discord.Intents.default()
client = discord.Client(intents=intents)

def open_gif_file():
    file = open("yuri-good-morning.gif", "rb")
    return file

def close_gif_file(file):
    file.close()

def is_text_channel(channel):
    return type(channel) is discord.TextChannel

def get_lizcord_general_channel():
    for channel in client.get_all_channels():
        if channel.id == 1037773076747784194 and is_text_channel(channel):
            return channel
            
async def send_good_morning_gif():
    gif = open_gif_file()
    general_channel = get_lizcord_general_channel()
    await general_channel.send(file=discord.File(gif, description="Two anime girls kissing with the caption \"Good Morning\""))
    print(f'Sent Good Morning GIF at {datetime.now()}')

async def sleep_and_send_gif(message_time):
    await sleep_until(message_time)
    await send_good_morning_gif()

# routine finishes when all scheduled tasks have been completed
async def run_scheduled_tasks(schedule):
    async with asyncio.TaskGroup() as tg:
        for message_time in schedule:
            tg.create_task(sleep_and_send_gif(message_time))

async def main_message_loop():
    schedule = create_daily_message_schedule()
    await run_scheduled_tasks(schedule)
    await main_message_loop()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    await send_good_morning_gif()
    await main_message_loop()

client.run(discord_token)