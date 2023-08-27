import os
import discord
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

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

client.run(discord_token)