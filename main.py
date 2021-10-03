import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefx = "//", intents = nextcord.Intents.all())

@bot.event
async def on_ready():
  print('Bot is online')
  
bot.run(TOKEN)
