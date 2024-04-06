import discord
from discord.ext import commands
import filter

config = {
    'token': 'MTIxNTkzMjQ4OTQyNDU3MjQzNw.GDI8p0.cJ4JUBJVlbTj9qnk-YOnTEuNdPHp8CmEbZsT7Q',
    'prefix': 'prefix',
}

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


#asdadasdasdasdasd



@bot.event
async def on_message(ctx):
    if ctx.author != bot.user:
        print(ctx.author)
        print(ctx)
        print(ctx.content, type(ctx.content))
        forbidden_word=filter.filter(ctx.content)
        if forbidden_word:
            await ctx.reply("ай ай ай плохо так выражатся я от тебя такого не ожидал "+f'@{ctx.author.global_name}')
        else:
            await ctx.reply(ctx.content)
bot.run(config['token'])
