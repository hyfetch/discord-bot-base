import discord
from discord import app_commands
from discord.ext import commands

class ExampleModule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name="example", description="An example command")
    async def example(self, interaction: discord.Interaction):
        await interaction.response.send_message("Example command to showcase how to even use cogs / modules \n For additional info refer to [Discord.py documentation](https://discordpy.readthedocs.io/en/stable/) ")

async def setup(bot):
    await bot.add_cog(ExampleModule(bot))