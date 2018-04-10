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

    #turn on/off message spam
    global isEnabled
    isEnabled = 'dif'
    if message.content.startswith('!turnon'):
        if (message.author.id == '106814905583169536') & (isEnabled == 'off') | (message.author.id == '106814905583169536') & (isEnabled == 'dif'):
            isEnabled = 'on'
            msg = 'Message spam have been turned on'
            await client.send_message(message.channel, msg)
            return
        if (message.author.id == '106814905583169536') & (isEnabled == 'on'):
            msg = 'Message spam is already enabled'
            await client.send_message(message.channel, msg)
        else:
            msg = '{0.author.mention} you are not authorised for this command'.format(message)
            await client.send_message(message.channel, msg)
    if message.content.startswith('!turnoff'):
        if (message.author.id == '106814905583169536') & (isEnabled == 'on'):
            isEnabled = 'off'
            msg = 'Message spam have been turned off'
            await client.send_message(message.channel, msg)
        if (message.author.id == '106814905583169536') & (isEnabled == 'off'):
            msg = 'Message spam is already disabled'
            await client.send_message(message.channel, msg)
        else:
            msg = '{0.author.mention} you are not authorised for this command'.format(message)
            await client.send_message(message.channel, msg)



@client.event
async def on_typing(channel, Member, when):
    if (Member.id == '284823748371021825') & (isEnabled == 'on'):
        msg = 'V this is an impostor, execute him V'
        await client.send_message(channel, msg)

    if (Member.id == '106814905583169536') & (isEnabled == 'on'):
        msg = 'SHUT THE FUCK UP, the REAL queen is speaking'
        await client.send_message(channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
