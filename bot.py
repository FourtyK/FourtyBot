import discord
from discord.ext import commands
from discord import Status
import random
import inspect
import asyncio
import requests
from bs4 import BeautifulSoup
# ИМПОРТ НУЖНЫХ БИБЛИОТЕК


def get_text():
    session = requests.session()
    req = session.get('http://cpsy.ru/cit1.htm')
    doc = BeautifulSoup(req.content, features="html.parser")
    mydivs = doc.findAll("div", {"class": "ctext"})
    quote = random.choice(mydivs).text

    return quote
    

"==================================================================="


bot = commands.Bot(command_prefix='-')  # префикс бота

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    game = discord.Game('РАБОТАЮ')
    await bot.change_presence(status=discord.Status.dnd, activity=game)  # установка статуса бота на Не беспокоить и игровая активность - Работ

@bot.event  # следующая команда будет работать постоянно
async def on_command_error(ctx, error):  # если бот видит неизвестную команду, то возникает ошибка. При её возникновении включается эта функция
    await ctx.send('Я тебя не понимаю...')  # и вывод сообщения

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Бот Фартука", description="Я - крутейший бот на свете, созданный людьми для дискорда. Я владею множеством функций, а главное - я написан на языке программирования python. Для того, чтобы найти мои исходники - обратитесь к моему создателю.\nНа любые неизвестные ему команды отвечает, что таких не видывал.", color=0xeee657)
    embed.add_field(name="-help", value="Бот выведет информацию о себе и о функциях, которые он имеет", inline=False)
    embed.add_field(name="-префикс", value='Бот сообщит свой префикс', inline=False)
    embed.add_field(name="-мысля", value="Бот скажет вам умную мыслю", inline=False)
    embed.add_field(name="-шпион", value="Бот найдёт крысу", inline=False)
    embed.add_field(name="-биба", value="Бот скажет вам размер вашей бибы", inline=False)
    embed.add_field(name="-members_list", value="Бот выведет количество офлайн и онлайн пользователей", inline=False)
    embed.add_field(name="-аватарка [id_пользователя]", value="Бот покажет вам аватарку пользователя в полном размере", inline=False)
    embed.add_field(name="-монетка", value="Бот подкинет монетку и скажет результат", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def мысля(ctx):  # команда -мысля
    await ctx.send(get_text())  # бот отвечает случайной мыслью (не обязательно умной)

@bot.command()
async def префикс(ctx):  # команда -префикс 
    await ctx.send('Префикс бота: /')  # бот покажет префикс

@bot.command()
async def биба(ctx):  # команда -биба
    if str(ctx.author.id) == '295608939481923604':
        await ctx.send('Биба фартука 100 см')
    else:
        await ctx.send('Такая биба имеет размер {} см'.format(random.randint(1, 30)))  # команда покажет вам размер бибы от 1 до 30 см

@bot.command()
async def members_list(ctx):  # команда список участников
    users_list = list()  # создание списка для юзеров
    users_online_list = list()  # создание списка всех онлайн юзеров
    guild = ctx.guild  # поиск сервера, откуда была вызвана команда
    for member in guild.members:  # проход по юзерам на сервере
        users_list.append(member)  # добавление юзера в список участников сервака
        if member.status != discord.Status.offline:  # проверка юзера на онлайн 
            users_online_list.append(member)  # если он онлайн - добавляется в список онлайн_пользователей
    await ctx.send('''Пользователей на сервере: {}\n'''
'''Пользователей на сервере онлайн: {}'''.format(len(users_list), len(users_online_list))) # вывод итога

@bot.command()
async def шпион(ctx):
    users = []
    for member in ctx.guild.members:  # проход по юзерам на сервере
        if member.bot is False:
            users.append(member.id)

    await ctx.send('<@{}> шпион!'.format(random.choice(users)))  # вывод 1 рандомного человека 

@bot.command()
async def аватарка(ctx, memb):
    id = memb[2:-1]
    guild = ctx.guild
    for member in guild.members:
        if str(member.id) == str(id):
            await ctx.send('Аватарка игрока {}: {}'.format(member.name, member.avatar_url))

@bot.command()
async def монетка(ctx):
    answers_list = ['Орёл!', 'Решка!']
    await ctx.send('Иииии... Это...')
    await asyncio.sleep(3)
    chance = random.randint(0,  100)
    if chance <= 5:
        await ctx.send('Ребро!')
        await ctx.send("https://imgur.com/CD3WYd3")
    else:
        chance = random.randint(1, 2)
        if chance == 1:
            await ctx.send('Решка!')
            await ctx.send("https://imgur.com/v5Nm5Fz")
        else:
            await ctx.send('Орёл!')
            await ctx.send("https://imgur.com/ozSVvRj") 

@bot.command()
async def лучшая_пара(ctx):
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


bot.run('NTcwNjY0MzY3OTQ3OTA3MDc4.XMChxw.gLll-JonRcOVY-T3AgpXBpDYIb4')
