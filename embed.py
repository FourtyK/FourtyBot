import discord
from discord.ext import commands
import random


class Embed_Class(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def help(self, ctx):
        embed = discord.Embed(title="Бот Фартука", description="Я - крутейший бот на свете, созданный людьми для дискорда. "
                                                                  "Я владею множеством функций, а главное - я написан на языке программирования python. "
                                                                  "Для того, чтобы найти мои исходники - обратитесь к моему создателю.\nНа любые неизвестные ему команды отвечает, что таких не видывал.\n "
                                                                  "За помощью обращаться в личку [ВКонтакте](https://vk.com/idroasss)", color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/570664367947907078/0a9ea2db037bad1191e16891ff869e0a.png?size=2048")
        embed.set_footer(text="Все права защищены Котолицией (с) 2019")
        embed.set_author(name="Author: FourtyK", icon_url="https://cdn.discordapp.com/avatars/295608939481923604/d23702f744c6a6355494709b318f4b9a.png?size=2048")
        embed.set_image(url="https://media.discordapp.net/attachments/605075208956805131/607346534601719819/maxresdefault.jpg?width=1195&height=673")
        embed.add_field(name="Развлечения", value="-fun", inline=False)
        embed.add_field(name="Управление юзерами", value="-adm", inline=False)
        # embed.add_field(name="Музыка", value="-music", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def fun(self, ctx):
        embed = discord.Embed(title='Развлечения :tada:', color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.add_field(name="-coin", value="Бот подкинет монетку и скажет результат.", inline=False)
        embed.add_field(name="-cupid", value="Бот покажет голубков.", inline=False)
        embed.add_field(name="-quote", value="Бот скажет вам умную мыслю.", inline=False)
        embed.add_field(name="-биба", value="Бот скажет вам размер вашей бибы.", inline=False)
        embed.add_field(name="-avatar [@User#1234]", value="Бот покажет вам аватарку пользователя в полном размере.", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def adm(self, ctx):
            embed = discord.Embed(title='Админские команды', color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
            embed.add_field(name="-kick [@User#1234] reason", value="Кикнуть человека с сервера.", inline=False)
            embed.add_field(name="-ban [@User#1234] reason", value="Забанить человека на сервере.", inline=False)
            embed.add_field(name="-clear", value="Очистит чат от 10 последних сообщений.", inline=False)
            embed.add_field(name="-mute/unmute [@User#1234]", value="Заблокировать/Разблокировать юзеру чат", inline=False)
            await ctx.send(embed=embed)

    # @commands.command()
    # async def music(self, ctx):
    #         embed = discord.Embed(title='Музыка', color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
    #         embed.add_field(name="-play [url_youtube_video]", value="Бот подключится к голосовому чату, где вы находитесь\n и начнёт проигрывать выбранное видео.", inline=False)
    #         embed.add_field(name="-volume [1-100]", value="Изменяет громкость проигрывания видео.", inline=False)
    #         embed.add_field(name="-leave", value="Бот выйдёт из голосового чата", inline=False)
    #         await ctx.send(embed=embed)
