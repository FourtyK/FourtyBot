import discord
from discord.ext import commands, tasks
from discord import Status
from itertools import cycle
# import youtube_dl
from embed import Embed_Class
from fun import Fun_Class
from adm import Adm_Class
# from music import Music_Class
# ИМПОРТ НУЖНЫХ БИБЛИОТЕК

bot = commands.Bot(command_prefix='-')  # префикс бота
bot.remove_command('help')

@bot.event
async def on_member_join(member):
    channels = member.guild.channels
    channel_id = ""
    for channel in channels:
        if channel.name == "новенькие":
            channel_id = channel.id
    if channel_id:
        channel = bot.get_channel(channel_id)
        await channel.send("Приветствую тебя на сервере {}, {}.".format(member.guild.name, member.mention))
    role = discord.utils.get(member.guild.roles, name='Member')
    await member.add_roles(role)

@bot.event
async def on_reaction_add(member):
    pass

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
        await ctx.send('Ошибка')

# bot.add_cog(Music_Class(bot))
bot.add_cog(Adm_Class(bot))
bot.add_cog(Fun_Class(bot))
bot.add_cog(Embed_Class(bot))
bot.run('token')
