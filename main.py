import os
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

def create_discord_file(file):
    return discord.File(file, description="Two anime girls kissing with the caption \"Good Morning\"")

def is_text_channel(channel):
    return type(channel) is discord.TextChannel

def get_general_channel():
    for channel in client.get_all_channels():
        if channel.name == 'general' and is_text_channel(channel):
            return channel
            
async def send_good_morning_gif():
    gif = open_gif_file()
    discord_file = create_discord_file(gif)
    general = get_general_channel()
    if general:
        await general.send(file=discord_file)
        print(f'Sent Good Morning GIF at {datetime.now()}')

async def main_message_loop():
    schedule = create_daily_message_schedule()
    for message_time in schedule:
        sleep_until(message_time)
        await send_good_morning_gif()
    await main_message_loop()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    await main_message_loop()

client.run(discord_token)