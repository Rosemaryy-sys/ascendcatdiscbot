import discord
import random	
from discord.ext import commands


client = commands.Bot(command_prefix="a!", case_insensitive=True)



@client.event
async def on_ready():
    print("ITS READY")




@client.event
async def on_ready():
     	print("Commands are set and ready to go.. o_o")




@client.command()
async def hello(ctx):
	await ctx.send("hello person")


     


@client.command()
async def rules(ctx):
	await ctx.send("there might be rules")


@client.command()
async def history(ctx):
	await ctx.send("this isnt history class")

@client.command()
async def mmm(ctx):
	await ctx.send("u having a stroke?")

@client.command()
async def math(ctx):
	await ctx.send("i am not smart at math")
		
@client.command()
async def faggot(ctx):
	await ctx.send("huh? what u say?")

@client.command()
async def fruity(ctx):
	await ctx.send("not me, its you.")

@client.command()
async def ascend(ctx):
	await ctx.send("ascended into the deeplands")

@client.command()
async def pineapple(ctx):
	await ctx.send("pineapple, pen, apple.")

@client.command()
async def kaeyaballs(ctx):
	await ctx.send("police, this is the person.")

@client.command()
async def kaeyaballcheese(ctx):
	await ctx.send("sir come with me your goin to hatsune miku prison")

@client.command()
async def vampirecookie(ctx):
	await ctx.send("thinking bout that man always ")

@client.command()
async def dont(ctx):
	await ctx.send("dont shue me i need a family to raise :cryingemo:")

@client.command()
async def floppa(ctx):
	await ctx.send("No flop no flopsta, just flpppaaa. Flopaa no flop no flopsta.")






# still make command_prefix = "a!"

#Commands = 14 as of "CURRENT" 
#CURRENTLY = 14 Commands
