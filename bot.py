import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import requests
import os

client = commands.Bot(command_prefix="--")
client.remove_command("help")

@client.event
async def on_member_join(member):
    server = client.get_server("502625088722436096")
    channel = client.get_channel("502626654598856704")
    await client.send_message(channel, f"Welcome {member.mention} to {server}!")



@client.event
async def on_ready():
    print("The bot is ready!")
    
bot_token:client.run(str(os.environ.get('BOT_TOKEN')))
