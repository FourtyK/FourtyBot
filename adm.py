import discord
from discord.ext import commands
import asyncio
import datetime
from funcs import uptime_com


class Adm_Class(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channels_names_list = ['инфо', 'новости', 'info', 'news', 'info-eng', 'info-ru']
        self.start_time = datetime.datetime.utcnow()

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, n=None):
        n = int(n)
        await ctx.message.delete()
        if not n:
            await ctx.channel.purge(limit=10)
            msg = await ctx.send('{} messages was cleared by {}'.format("10", ctx.author.mention))
        else:
            await ctx.channel.purge(limit=n)
            msg = await ctx.send('{} messages was cleared by {}'.format(n, ctx.author.mention))
        await asyncio.sleep(5)
        await msg.delete()


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.Member=None, *, reason=None):
        if not member:
            await ctx.send('Не был указан пользователь.')
            return
        await member.kick(reason=reason)
        await ctx.send('Юзер был кикнут с сервера.')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.Member=None, *, reason=None):
        if not member:
            await ctx.send('Не был указан пользователь.')
            return
        await member.ban(reason=reason)
        await ctx.send('Юзер был забанен на сервере.')

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member:discord.Member=None):
        for categor in ctx.guild.categories:
            for chan in categor.channels:
                if chan.type.name == "text":
                    if chan.name not in self.channels_names_list:
                        await chan.set_permissions(member, send_messages=False)
        await ctx.send(f"{member.name} был замучен!")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member:discord.Member=None):
        for categor in ctx.guild.categories:
            for chan in categor.channels:
                if chan.type.name == "text":
                    if chan.name not in self.channels_names_list:
                        await chan.set_permissions(member, send_messages=True)
        await ctx.send(f"{member.name} был размучен!")

    @commands.command()
    async def uptime(self, ctx):
        await ctx.send(uptime_com(self.start_time))