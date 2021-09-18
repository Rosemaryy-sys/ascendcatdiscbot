import discord
import random	
from discord.ext import commands


client = commands.Bot(command_prefix="-", case_insensitive=True)



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





# still make command_prefix = "-"

#Commands = 5 as of "CURRENT" 
#CURRENTLY = 5 Commands


