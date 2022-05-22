from minebot import instance

@instance.command(name="ping")
async def ping(ctx):
	await ctx.channel.send("pong")