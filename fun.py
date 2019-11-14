import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import random
import asyncio


def get_text():
    phrase = []

    session = requests.session()
    req = session.get('https://randstuff.ru/saying/')
    doc = BeautifulSoup(req.content, features="html.parser")
    mydivs = doc.findAll("div", {"id": "saying"})

    return f"{mydivs[0].text[:-10]}"


class Fun_Class(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def quote(self, ctx):  # команда -мысля
        await ctx.send(get_text())  # бот отвечает случайной мыслью (не обязательно умной)

    @commands.command()
    async def биба(self, ctx):  # команда -биба
        if str(ctx.author.id) == '295608939481923604':
            await ctx.send('Биба фартука 100 см')
        else:
            await ctx.send('Такая биба имеет размер {} см'.format(random.randint(1, 30)))  # команда покажет вам размер бибы от 1 до 30 см

    @commands.command()
    async def avatar(self, ctx, member):
        id = member[2:-1]
        guild = ctx.guild
        for member in guild.members:
            if str(member.id) == str(id):
                embed = discord.Embed(color=0xeee657)
                image_url = member.avatar_url._url
                embed.set_image(url=image_url)
                await ctx.send(embed=embed)

    @commands.command()
    async def coin(self, ctx):
        money = {
        'eagle':'https://media.discordapp.net/attachments/605075208956805131/607346505791307786/ozSVvRj.png',
        'tails':'https://media.discordapp.net/attachments/605075208956805131/607346507766562836/v5Nm5Fz.jpg?width=679&height=672',
        'edge':'https://media.discordapp.net/attachments/605075208956805131/607346511021604864/CD3WYd3.png'
        }
        await ctx.send('Иииии... Это...')
        await asyncio.sleep(3)
        chance = random.randint(0,  100)
        if chance <= 5:
            embed = discord.Embed(color=0xeee657)
            embed.set_image(url=money.pop('edge'))
            await ctx.send(embed=embed)
        else:
            chance = random.randint(1, 2)
            if chance == 1:
                embed = discord.Embed(color=0xeee657)
                embed.set_image(url=money.pop('tails'))
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(color=0xeee657)
                embed.set_image(url=money.pop('eagle'))
                await ctx.send(embed=embed)

    @commands.command()
    async def cupid(self, ctx):
        double = list()
        users = list()
        for member in ctx.guild.members:  # проход по юзерам на сервере
            if member.bot == False:
                member = member.id
                users.append(member)

        first = random.choice(users)
        double.append(first)
        second = random.choice(users)
        while first == second:
            second = double.append(random.choice(users))
        double.append(second)

        await ctx.send("Лучшая пара: <@{}> и <@{}> :cupid:".format(str(double[0]), str(double[1])))