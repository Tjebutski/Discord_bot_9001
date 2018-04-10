# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord

TOKEN = 'NDA0OTkzNjYxMDU5ODU4NDMz.DazwaQ.P9e8ajUAaVo6dwb-z7tymyjKn9o'


bot = discord.Client()


@bot.event
async def on_message(message):
    # Global
    global isEnabled
    isEnabled = 'dif'

    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await bot.send_message(message.channel, msg)

    #turn on/off message spam
    if message.content.startswith('!turnon'):
        if message.author.id == '106814905583169536':
            isEnabled = 'on'
            msg = 'Message spam is enabled'
            await bot.send_message(message.channel, msg)
            return
        if (message.author.id == '106814905583169536') & (isEnabled == 'on'):
            msg = 'Message spam is already enabled'
            await bot.send_message(message.channel, msg)
            return
        else:
            msg = '{0.author.mention} you are not authorised for this command'.format(message)
            await bot.send_message(message.channel, msg)
            return
    if message.content.startswith('!turnoff'):
        if (message.author.id == '106814905583169536') & (isEnabled == 'on'):
            isEnabled = 'off'
            msg = 'Message spam is disabled'
            await bot.send_message(message.channel, msg)
            return
        if (message.author.id == '106814905583169536') & (isEnabled == 'off') | (message.author.id == '106814905583169536') & (isEnabled == 'dif'):
            msg = 'Message spam is already disabled'
            await bot.send_message(message.channel, msg)
            return
        else:
            msg = '{0.author.mention} you are not authorised for this command'.format(message)
            await bot.send_message(message.channel, msg)
            return



@bot.event
async def on_typing(channel, Member, when):
    if (Member.id == '284823748371021825') & (isEnabled == 'on'):
        msg = 'V this is an impostor, execute him V'
        await bot.send_message(channel, msg)

    if (Member.id == '106814905583169536') & (isEnabled == 'on'):
        msg = 'SHUT THE FUCK UP, the REAL queen is speaking'
        await bot.send_message(channel, msg)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN)
