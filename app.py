import discord
from discord.ext import commands
from Addons import *


import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('TOKEN')

bot = commands.Bot(command_prefix = ";",help_command = None)

bot.add_cog(Status(bot))
bot.add_cog(Listen(bot))

bot.run(token)