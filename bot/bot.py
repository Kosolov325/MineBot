import discord
from resources.socket import Botquery
from resources.config import botconfig
from asyncio import TimeoutError
from discord.ext import commands

bot = commands.Bot(command_prefix=botconfig.prefix)

@bot.command(name="ping")
async def ping(ctx):
	await ctx.channel.send("boa noite bruno")

@bot.command(name="addserver")
async def setip(ctx):
    def check(message: discord.Message):
         return isinstance(message.channel, discord.DMChannel) and message.author == ctx.author

    await ctx.message.delete()
    try:
        await ctx.author.send("Digite o endereço IP!")
        ip = await bot.wait_for("message", timeout=30.0, check=check)
        
        await ctx.author.send("Digite a Porta!")
        port = await bot.wait_for("message", timeout=30.0, check=check)

        query = Botquery(ip.content, port.content)
        await ctx.author.send("Feito!")
    except:
        query = Botquery(ip.content)
        await ctx.author.send("Feito!")

@bot.command(name="changeapi")
async def changeapi(ctx):
    def check(message: discord.Message):
         return isinstance(message.channel, discord.DMChannel) and message.author == ctx.author

    await ctx.message.delete()

    try:
        await ctx.author.send("Digite o endpoint da API!")
        api = await bot.wait_for("message", timeout=30.0, check=check)

        botconfig.api = api.content
        await ctx.author.send("Feito!")
    except:
        pass

@bot.event
async def on_ready():
    print('Running.....')

bot.run(botconfig.token)