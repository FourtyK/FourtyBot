import discord
from discord.ext import commands
import asyncio
import random


class Giveaway_Class(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def calc_time(self, time):
        intervals = (
            ('weeks', 604800),
            ('days', 86400),
            ('hours', 3600),
            ('minutes', 60),
            ('seconds', 1))

        def display_time(seconds, granularity=2):
            result = []

            for name, count in intervals:
                value = seconds // count
                if value:
                    seconds -= value * count
                    if value == 1:
                        name = name.rstrip('s')
                    result.append("{} {}".format(value, name))
            return ', '.join(result[:granularity])
        
        return display_time(int(time))

    def make_embed(self, time, winners, prizes):
        time = self.calc_time(time)
        embed = discord.Embed(title=prizes,
                              color=discord.Color.blue())
        embed.add_field(name="Click the reaction below to enter!", value=f"Ends in: {time}", inline=False)
        return embed

    @commands.command()
    @commands.has_role("Giveaway")
    async def gwstart(self, ctx, time, winners, *args):
        prizes = " ".join(args)
        embed = self.make_embed(time, winners, prizes)
        message = await ctx.send(embed=embed)
        await message.add_reaction("🎉")
        await asyncio.sleep(int(time))
        message = await ctx.channel.fetch_message(message.id)
        users = await message.reactions[0].users().flatten()
        winner = (random.choice(users))
        await ctx.send(f"{winner.mention} won {prizes}")
