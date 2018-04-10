# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
from discord import Member, message

TOKEN = 'NDA0OTkzNjYxMDU5ODU4NDMz.DazwaQ.P9e8ajUAaVo6dwb-z7tymyjKn9o'

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)


@client.event
async def on_typing(channel, Member, when):
    if Member.id == '284823748371021825':
        msg = 'V this is an impostor, execute him V'
        await client.send_message(channel, msg)

    if Member.id == '106814905583169536':
        msg = 'SHUT THE FUCK UP, the REAL queen is speaking'
        await client.send_message(channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
