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
from database import DataBase


bot = commands.Bot(command_prefix='-')
bot.remove_command('help')

@bot.event
<<<<<<< HEAD
async def on_member_join(member:discord.Member=None):
=======
async def on_member_join(ctx, member):
>>>>>>> f21be032b4cb54c28aa43d43bbf43dda03ffee4f
    channel = bot.get_channel(638793865633202177)
    await channel.send("Приветствую тебя на сервере {}, {}.".format(member.guild.name, member.mention))
    role = discord.utils.get(member.guild.roles, name='Member')
    await member.add_roles(role)
    DataBase().add_user(member.id, member.discriminator, member.guild.id)
<<<<<<< HEAD

@bot.event
async def on_member_remove(member:discord.Member=None):
    DataBase().delete_user(member.id, member.guild.id)
=======
>>>>>>> f21be032b4cb54c28aa43d43bbf43dda03ffee4f

statuses = cycle(["-help", "Owner: FourtyK"])

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
