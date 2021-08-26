import discord
from discord.utils import get
from discord.ext import commands
import pyautogui
import time
import pydirectinput

print(pyautogui.size())



client = commands.Bot(command_prefix = '.')


@client.command()
async def right(ctx):
    pydirectinput.keyDown('right')
    time.sleep(1.5)
    pydirectinput.keyUp('right')
#    await ctx.send('presssed right!') 
    print('pressed right')
    
@client.command()
async def holdright(ctx):
    pydirectinput.keyDown('right')
#    await ctx.send('holding right') 
    print('holding right')
    
@client.command()
async def let(ctx):
    pydirectinput.keyUp('right')
    pydirectinput.keyUp('left')
#    await ctx.send('let go of both shit') 
    print('let got of right and left')
    
@client.command()
async def left(ctx):
    pydirectinput.keyDown('left')
    time.sleep(1.5)
    pydirectinput.keyUp('left')
#    await ctx.send('presssed left!') 
    print('pressed left')
    
@client.command()
async def up(ctx):
    pydirectinput.keyDown('up')
    time.sleep(0.5)
    pydirectinput.keyUp('up')
#   await ctx.send('presssed up!') 
    print('pressed up')
    
@client.command()
async def holdleft(ctx):
    pydirectinput.keyDown('left')
#    await ctx.send('holding left') 
    print('holding left')
    
@client.command()
async def down(ctx):
    pydirectinput.keyDown('down')
    time.sleep(0.5)
    pydirectinput.keyUp('down')
#    await ctx.send('presssed down!') 
    print('pressed down')

@client.event
async def on_ready():	
    print('Bot is connected.')
    
@client.command()
async def how(ctx):
    await ctx.send('.up, .right, .left, .down, .holdright, .holdleft, .let (hold means it will keep holding them down until you type .let') 
    print('showed help instructions')
	


     


client.run('bot token')