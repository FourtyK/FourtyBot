import discord
from discord.ext import commands
from discord import Status
from discord.voice_client import VoiceClient
import random
import inspect
import asyncio
import requests
from bs4 import BeautifulSoup
import youtube_dl
# ИМПОРТ НУЖНЫХ БИБЛИОТЕК

times = ['секунду', 'час', 'день', 'неделю', 'месяц', 'год', '10 лет', 'столетие', 'никогда']


def get_text():
    session = requests.session()
    req = session.get('http://cpsy.ru/cit1.htm')
    doc = BeautifulSoup(req.content, features="html.parser")
    mydivs = doc.findAll("div", {"class": "ctext"})
    quote = random.choice(mydivs).text

    return quote
    

"=============================EMBED================================="


bot = commands.Bot(command_prefix='-')  # префикс бота
bot.remove_command('help')

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

@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Бот Фартука", description="Я - крутейший бот на свете, созданный людьми для дискорда. Я владею множеством функций, а главное - я написан на языке программирования python. Для того, чтобы найти мои исходники - обратитесь к моему создателю.\nНа любые неизвестные ему команды отвечает, что таких не видывал.", color=0xeee657)
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/570664367947907078/0a9ea2db037bad1191e16891ff869e0a.png?size=2048')
    embed.set_footer(text='Все права защищены Котолицией (с) 2019')
    embed.set_author(name='Author: FourtyK', icon_url='https://cdn.discordapp.com/avatars/295608939481923604/899fc51ebe661cc9dd8e21a92db51789.png?size=2048')
    embed.set_image(url='https://media.discordapp.net/attachments/605075208956805131/607346534601719819/maxresdefault.jpg?width=1195&height=673')
    embed.add_field(name="Развлечения", value="-развлечения")
    embed.add_field(name="Управление юзерами", value="-control")
    await ctx.send(embed=embed)

@bot.command()
async def развлечения(ctx):
    embed = discord.Embed(title='Развлечения :tada:', color=0xeee657)
    embed.add_field(name="-монетка", value="Бот подкинет монетку и скажет результат", inline=False)
    embed.add_field(name="-купидон", value='Бот покажет голубков', inline=False)
    embed.add_field(name="-мысля", value="Бот скажет вам умную мыслю", inline=False)
    embed.add_field(name="-шпион", value="Бот найдёт крысу", inline=False)
    embed.add_field(name="-биба", value="Бот скажет вам размер вашей бибы", inline=False)
    embed.add_field(name="-аватарка [id_пользователя]", value="Бот покажет вам аватарку пользователя в полном размере", inline=False)
    embed.add_field(name="-когда", value='Бот скажет когда вы ...', inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def control(ctx):
        embed = discord.Embed(title='Админские команды', color=0xeee657)
        embed.add_field(name="-kick (reason)", value='-kick [@Player#1234] reason', inline=False)
        embed.add_field(name="-ban (reason)", value='-ban [@Player#1234] reason', inline=False)
        await ctx.send(embed=embed)


"==============================FUN================================="


@bot.command()
async def когда(ctx):
    answer = random.choice(times)
    if answer == 'никогда':
        await ctx.send(answer.capitalazie())
    else:
        await ctx.send('Через ' + answer)

@bot.command()
async def мысля(ctx):  # команда -мысля
    await ctx.send(get_text())  # бот отвечает случайной мыслью (не обязательно умной)

@bot.command()
async def биба(ctx):  # команда -биба
    if str(ctx.author.id) == '295608939481923604':
        await ctx.send('Биба фартука 100 см')
    else:
        await ctx.send('Такая биба имеет размер {} см'.format(random.randint(1, 30)))  # команда покажет вам размер бибы от 1 до 30 см

@bot.command()
async def шпион(ctx):
    users = []
    for member in ctx.guild.members:  # проход по юзерам на сервере
        if member.bot is False:
            users.append(member.id)

    await ctx.send('<@{}> крыса!'.format(random.choice(users)))  # вывод 1 рандомного человека 

@bot.command()
async def аватарка(ctx, memb):
    id = memb[2:-1]
    guild = ctx.guild
    for member in guild.members:
        if str(member.id) == str(id):
            embed = discord.Embed(color=0xeee657)
            image_url = member.avatar_url._url
            embed.set_image(url=image_url)
            await ctx.send(embed=embed)

@bot.command()
async def монетка(ctx):
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

@bot.command()
async def купидон(ctx):
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


"==============================ADM=================================="


@bot.command()
async def kick(ctx, member : discord.Member=None, *, reason=None):
    if ctx.author.guild_permissions.administrator is True:
        if not member:
            await ctx.send('А кикать кого?')
            return
        await member.kick(reason=reason)
        await ctx.send('Юзер был кикнут с сервера')
    else:
        await ctx.send('Недостаточно прав')

@bot.command()
async def ban(ctx, member : discord.Member=None, *, reason=None):
    if ctx.author.guild_permissions.administrator is True:
        if not member:
            await ctx.send('А банить кого?')
            return
        await member.ban(reason=reason)
        await ctx.send('Юзер был забанен на сервере')
    else:
        await ctx.send('Недостаточно прав')

    
"=============================MUSIC================================"

@bot.command(pass_context=True)
async def join(ctx):
    if ctx.voice_client is None:
        if ctx.author.voice:
            await ctx.author.voice.channel.connect()

@bot.command(pass_context=True)
async def disconnect(ctx):
    await ctx.voice_client.disconnect()

@bot.command(pass_context=True)
async def play(ctx, url):
    

bot.run('NTcwNjY0MzY3OTQ3OTA3MDc4.XUMkGw.ViGkN4AAwROqxXnI_933JJ2ye2g')
