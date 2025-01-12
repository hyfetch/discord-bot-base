import discord
from discord.ext import commands
import os
import logging
from dotenv import load_dotenv

load_dotenv()

intent = discord.Intents.all() # You can really adjust it up to your liking, i always tend to use Intents.all() for sake of simplicity where i don't need to toggle them dynamically depending on what i do.

logging.basicConfig(level=logging.INFO)

async def load_cogs():
    """Load all cogs in the 'cogs' directory."""
    for dirpath, _, filenames in os.walk('./cogs'):
        for filename in filenames:
            if not filename.endswith('.py'):
                continue

            cog_path = os.path.join(dirpath, filename)
            module_name = os.path.relpath(cog_path, start='./cogs').replace(os.path.sep, '.')[:-3]

            try:
                await bot.load_extension(f'cogs.{module_name}')
            except commands.ExtensionAlreadyLoaded:
                logging.info(f"Skipped loading cog: {module_name}")
            except Exception as e:
                logging.error(f"Error loading cog {module_name}: {e}")


@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
    await load_cogs()
    await bot.tree.sync()


if __name__ == '__main__':
    bot = commands.Bot(command_prefix='!', intents=intent)
    bot.run(os.getenv('BOT_TOKEN'))