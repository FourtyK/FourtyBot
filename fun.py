import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import random
import asyncio

from database import DataBase

def get_text():
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
        id = member[3:-1]
        guild = ctx.guild
        for member in guild.members:
            if str(member.id) == str(id):
                embed = discord.Embed(color=0xeee657)
                image_url = member.avatar_url._url
                embed.set_image(url="https://cdn.discordapp.com" + image_url)
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
        chance = random.randint(0, 100)
        embed = discord.Embed(color=0xeee657)
        if chance <= 5:
            embed.set_image(url=money.pop('edge'))
            await ctx.send(embed=embed)
        else:
            chance = random.randint(1, 2)
            if chance == 1:
                embed.set_image(url=money.pop('tails'))
                await ctx.send(embed=embed)
            else:
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

    @commands.command()
    async def duel(self, ctx, member:discord.Member=None):
        if ctx.author.id == member.id:
            await ctx.send("Вы не можете бросить самому себе дуэль! :clown:")
        else:
            self.answer = False
            players = [ctx.author.name, member.name]

            await ctx.send(f"**{member.name}** имеет 7 секунд для ответа.")
            await asyncio.sleep(7)

            if self.answer:
                await ctx.send(f"Дуэль между **{ctx.author.name}** и **{member.name}** начата!")
            else:
                await ctx.send(f"**{member.name}** испугался и не принял дуэль в отведённое время! 🐓")

            if self.answer:
                first_shot = random.choice([0, 1])
                await ctx.send(f"Первым стрелять будет **{players[first_shot]}**")
                if random.randint(0,100) < 5:
                    await asyncio.sleep(3)
                    await ctx.send(f"""Вот это невезение! Пистолет **{players[first_shot]}** дал осечку!
    Теперь очередь **{players[1 - first_shot]}** делать выстрел.""")
                    await asyncio.sleep(3)
                else:
                    if random.randint(0,100) < 50:
                        await asyncio.sleep(3)
                        await ctx.send(f"Попадание! **{players[first_shot]}** побеждает в дуэли!")
                        if players[first_shot] == ctx.author.name:
                            duel_result = '10'
                        else:
                            duel_result = '01'
                    else:
                        await asyncio.sleep(3)
                        await ctx.send(f"**{players[first_shot]}** стреляет, но не попадает! Теперь очередь **{players[1 - first_shot]}**")
                        if random.randint(0,100) < 5:
                            await asyncio.sleep(3)
                            await ctx.send("Пистолет второго игрока дает осечку! Оба игрока живы, дуэль окончена.")
                        elif random.randint(0,100) < 50:
                            await asyncio.sleep(3)
                            await ctx.send(f"Попадание! **{players[1 - first_shot]}** побеждает в дуэли!")
                            if players[first_shot] == ctx.author.name:
                                duel_result = '01'
                            else:
                                duel_result = '10'
                        else:
                            await asyncio.sleep(3)
                            await ctx.send(f"**{players[1 - first_shot]}** промахивается!")
                            await ctx.send("Оба игрока промахнулись, дуэль окончена вничью!")
                            duel_result = '00'
                DataBase().insert_duel_info(ctx.author.id, member.id, duel_result)

    @commands.command()
    async def accept(self, ctx):
        self.answer = True
        await ctx.send(f"**{ctx.author.name}** принял приглашение на дуэль!")
