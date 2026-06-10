## Imports

import discord
from discord.ext import commands

import dotenv
import os
import asyncio
from server import keep_alive
from pathlib import Path

## Bot Settings

description = """your_bot_description_here"""

# Intents are required for certain features, you can adjust them as needed.
intents = discord.Intents.default()

## Startup

bot = commands.Bot(command_prefix='your_prefix', description=description, intents=intents)

# .env should contain the bot token as DISCORD_TOKEN
# loads env variable for local hosting, on Render these are set in the dashboard and accessed as env variables as well
dotenv.load_dotenv(Path(__file__).parent / 'cfg/.env', verbose=True)

# to add a cog, use bot.load_extension('cogs.your_cog_name') in the main() function below.
async def main():
    async with bot:
        # bot startup, must be the last line of main()
        await bot.start(os.getenv('DISCORD_TOKEN'))

@bot.event
async def on_ready():
    assert bot.user is not None
    # startup message, can be customized or removed
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('Bot Launched!')
    
keep_alive()
asyncio.run(main())