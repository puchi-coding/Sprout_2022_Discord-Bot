import discord
from discord.ext import commands
import os  
from dotenv import load_dotenv


load_dotenv()
bot = commands.Bot(command_prefix ="$")

@bot.event
async def on_ready():
    print(">>Bot is Online<<")


for FileName in os.listdir('./cmds'):
    if FileName.endswith('.py'):
        bot.load_extension(f'cmds.{FileName[:-3]}')


if  __name__ == "__main__":
    bot.run(os.getenv('TOKEN'))
