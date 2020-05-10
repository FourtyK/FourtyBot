import discord
from discord.ext import commands
import random
from database import DataBase


class Embed_Class(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def help(self, ctx):
        embed = discord.Embed(title="Бот Фартука", description="Я - крутейший бот на свете, созданный людьми для дискорда. "
                                                               "Я владею множеством функций, а главное - я написан на языке программирования python.\n"
                                                               "Source: [GitHub](https://github.com/FourtyK/FourtyBot)\n"
                                                               "Contacts: [VKontakte](https://vk.com/idroasss), [Telegram](https://t.me/fourtyk)", 
                                                               color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/570664367947907078/0a9ea2db037bad1191e16891ff869e0a.png?size=2048")
        embed.set_footer(text="Все права защищены Котолицией (с) 2019")
        embed.set_author(name=f"Hello {ctx.author.name}", icon_url="https://cdn.discordapp.com" + ctx.author.avatar_url._url)
        embed.set_image(url="https://media.discordapp.net/attachments/605075208956805131/607346534601719819/maxresdefault.jpg?width=1195&height=673")
        embed.add_field(name="Развлечения", value="-fun", inline=False)
        embed.add_field(name="Управление юзерами", value="-adm", inline=False)
        embed.add_field(name="Розыгрыши", value="-gws", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def fun(self, ctx):
        embed = discord.Embed(title='Развлечения :tada:', color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.add_field(name="-coin", value="Бот подкинет монетку и скажет результат.", inline=False)
        embed.add_field(name="-cupid", value="Бот покажет голубков.", inline=False)
        embed.add_field(name="-quote", value="Бот скажет вам умную мыслю.", inline=False)
        embed.add_field(name="-биба", value="Бот скажет вам размер вашей бибы.", inline=False)
        embed.add_field(name="-avatar [@User#1234]", value="Бот покажет вам аватарку пользователя в полном размере.", inline=False)
        embed.add_field(name="-duel [@User#1234]", value="Предложите кому-нибудь дуэль.", inline=False)
        embed.add_field(name="-duel_stats", value="Узнать вашу статистику по дуэлям.", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def adm(self, ctx):
        embed = discord.Embed(title='Админские команды', color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.add_field(name="-kick [@User#1234] reason", value="Кикнуть человека с сервера.", inline=False)
        embed.add_field(name="-ban [@User#1234] reason", value="Забанить человека на сервере.", inline=False)
        embed.add_field(name="-clear N", value="Очистит чат от N последних сообщений. (По умолчанию 10)", inline=False)
        embed.add_field(name="-mute/unmute [@User#1234]", value="Заблокировать/Разблокировать юзеру чат", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def gws(self, ctx):
        embed = discord.Embed(title="Розыгрыши", color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.add_field(name="-gwstart [Time] [Winners] [Prizes]", value="Начать розыгрыш.", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def duel_stats(self, ctx):
        stats = DataBase().get_duel_info(ctx.author.id)
        embed = discord.Embed(title=f"Статистика игрока **{ctx.author.name}** по дуэлям.",
                              description=f"""Количество побед: {stats[0]}\n
                                              Количество поражений: {stats[1]}\n
                                              Количество ничьих: {stats[2]}""",
                              color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_footer(text="Предложите кому-нибудь сыграть дуэль: -duel [@Player#1234]")
        await ctx.send(embed=embed)