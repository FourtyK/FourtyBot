# импортирование библиотек
import discord
from discord.ext import commands, tasks
from discord import Status
from itertools import cycle

# импортирование файлов
from embed import Embed_Class
from fun import Fun_Class
from adm import Adm_Class
from giveaway import Giveaway_Class
from tokenfile import TOKEN


bot = commands.Bot(command_prefix='-')
bot.remove_command('help')

@bot.event
async def on_member_join(ctx, member):
    channels = member.guild.channels
    channel_id = ""
    for channel in channels:
        if channel.name == "новенькие":
            channel_id = channel.id
    if channel_id:
        channel = bot.get_channel(channel_id)
        await channel.send("Приветствую тебя на сервере {}, {}.".format(member.guild.name, member.mention))
    role = discord.utils.get(member.guild.roles, name='Member')
    if role:
        await member.add_roles(role)

statuses = cycle(["-help", "Owner's tag: #8072"])

@bot.event
async def on_ready():
    change_status.start()
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print('------')

@tasks.loop(seconds=5)
async def change_status():
    await bot.change_presence(activity=discord.Game(name=next(statuses)))

@bot.event
async def on_command_error(ctx, error):
    if "You are missing" in error.args[0]:
        await ctx.send("Недостаточно прав")
    elif "is not found" in error.args[0]:
        await ctx.send("Неизвестная команда")
    else:
        await ctx.send("Error")


bot.add_cog(Giveaway_Class(bot))
bot.add_cog(Adm_Class(bot))
bot.add_cog(Fun_Class(bot))
bot.add_cog(Embed_Class(bot))
bot.run(TOKEN) # your token
