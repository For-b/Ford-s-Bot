import discord
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(game=discord.Game(name="Making a bot"))

@client.event
async def on_message_delete(message):
    author = message.author
    message = message.content
    print('{}: {}'.format(author, message))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "+help":
        await client.send_message(message.channel, "piss off i aint finished!")

client.run('NTQ3MTY3MDkzOTkzMzczNzA2.D0y0ng.AAM18D03m1Uw7BX4f_I1sSCygRQ')