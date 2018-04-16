# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
from discord import Game
import asyncio

TOKEN = open('TOKEN.txt', 'r').read()
bot = discord.Client()


@bot.event
async def on_message(message):
    # global
    global checkIfEnabled
    checkIfEnabled = 'off'

    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await bot.send_message(message.channel, msg)

    # turn on/off message spam
    elif message.content.startswith('!turnon'):
        if message.author.id == '106814905583169536':
            msg = 'Message spam is enabled'
            checkifenabled = 'on'
            await bot.send_message(message.channel, msg)
        else:
            msg = '{0.author.mention} you are not authorised for this command'.format(message)
            await bot.send_message(message.channel, msg)
    elif message.content.startswith('!turnoff'):
        if message.author.id == '106814905583169536':
            msg = 'Message spam is disabled'
            checkifenabled = 'off'
            await bot.send_message(message.channel, msg)
        else:
            msg = '{0.author.mention} you are not authorised for this command'.format(message)
            await bot.send_message(message.channel, msg)


@bot.event
async def on_typing(channel, Member, when):
    if Member.id == '284823748371021825':
        msg = 'Fun fact: {0.author.mention} is mildly retarded'.format(discord.message)
        await bot.send_message(channel, msg)

    elif Member.id == '106814905583169536' & checkIfEnabled == 'on':
        msg = 'SHUT THE FUCK UP, the REAL queen is speaking'
        await bot.send_message(channel, msg)


@bot.event
async def on_ready():
    await bot.change_presence(game=Game(name='with humans!'))
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


async def list_servers():
    await bot.wait_until_ready()
    while not bot.is_closed:
        print('Current servers: ')
        for server in bot.servers:
            print(server.name)
        await asyncio.sleep(600)

bot.loop.create_task(list_servers())
bot.run(TOKEN)
