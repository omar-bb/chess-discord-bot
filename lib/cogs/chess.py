from discord.ext import commands

class Chess(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def puzzle(self, rating):
        pass

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("chess")


def setup(bot):
    bot.add_cog(Chess(bot))
