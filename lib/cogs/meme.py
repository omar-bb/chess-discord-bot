import aiohttp
import logging
import random

import discord
from discord.ext import commands

logging.basicConfig(level=logging.INFO)


class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["chessmeme"])
    async def meme(self, ctx):
        chess_subreddits = ["chessmemes", "AnarchyChess", "HikaruNakamura"]
        async with aiohttp.request("GET", f"https://meme-api.herokuapp.com/gimme/{random.choice(chess_subreddits)}") as response:
            if response.status == 200:
                data = await response.json()

                embed = discord.Embed(
                    title=data["title"], url=data["postLink"], color=ctx.author.color)

                embed.set_image(url=data["url"])

                await ctx.send(embed=embed)
            else:
                logging.warning(
                    f"Request failed. Status code: {response.status}")
                await ctx.send("Subreddit not found! Please enter a valid one.")


def setup(bot):
    bot.add_cog(Meme(bot))
