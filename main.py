import discord
import random
from keep_alive import keep_alive
import time
from discord.ext import commands
from lists import no_u_triggers, no_u_responses, questions, dies_responses, sus_triggers, sus_responses, wellbeing_responses, wellbeing_triggers, options, help_brown, competition, greetings, ids, whos_right1, whos_right2, goodbyes, wtf, doYouLikeMe, doYouLikeMeResponses
from sunarthseis import get_cat, get_episode, get_name, get_quote
#to send url images
import io
import aiohttp

client = commands.Bot = commands.Bot(command_prefix="@")


@client.event
async def on_ready():
    print('{0.user}'.format(client) + ' is online')


#brown sets a timer
@client.command()
async def timer(ctx, timeneeded):
    if timeneeded.isdigit() == True:
        if (int(timeneeded) < 61):
            await ctx.send('a timer has been set for ' + timeneeded +
                           ' minutes')
            time.sleep(int(timeneeded) * 60)
            await ctx.send(
                '**Timer is up! tsekare puretoulh sou andrea :rotating_light:** '
                + ctx.message.author.mention)
            await ctx.send(
                'https://tenor.com/view/hot-temperature-thermometer-raspberry-rpi-raspberry-pi-gif-17436134'
            )
        else:
            await ctx.send('timers cant be more than an hour long :/')
    else:
        await ctx.send(
            'wrong input! try asking for a timer again \n||eg. *@timer 5*  for a 5 minute timer||'
        )


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content

    say = message.channel.send

    #help brown
    if msg.startswith('help brown'):
        await say(help_brown)
        time.sleep(3)

    #hi brown
    if msg.startswith('hi brown'):
        time.sleep(1)
        await say(random.choice(greetings) + ' ' + get_name(message.author))

    #bye brown
    if msg.startswith('bye brown'):
        time.sleep(1)
        await say(random.choice(goodbyes))

    #brown/brown please kill/brown say
    if msg.startswith('brown'):
        shouldsaywtf = True
        if any(word in msg for word in no_u_triggers):
            shouldsaywtf = False
            await say(random.choice(no_u_responses))
        if msg.startswith("brown please kill"):
            shouldsaywtf = False
            time.sleep(1)
            await say('as you wish')
            time.sleep(2)
            async with aiohttp.ClientSession() as session:
                async with session.get(
                        'https://static.wikia.nocookie.net/c5b9c51d-7240-4f13-9b9d-994ff77dbb91'
                ) as resp:
                    if resp.status != 200:
                        return await message.send('Could not download file...')
                    data = io.BytesIO(await resp.read())
                    await say(file=discord.File(data, 'gun.png'))
        if msg.startswith('brown say') or msg.startswith('brown, say'):
            shouldsaywtf = False
            time.sleep(1)
            await say('no')
            time.sleep(1)
            await say('i dont think i will')
        if any(word in msg for word in doYouLikeMe):
            shouldsaywtf = False
            time.sleep(1)
            await say('ngl')
            time.sleep(2)
            await say(random.choice(doYouLikeMeResponses))
        if shouldsaywtf == True:
            time.sleep(2)
            await say(random.choice(wtf))
        else:
            return ()
    #birthday commmands
    if msg.startswith('its michaels birthday'):
        time.sleep(2)
        await say('happy birthday michael<:pepeblush:890638472036114473> ')

    if msg.startswith('its andrews birthday'):
        time.sleep(2)
        await say('happy birthday andrew<:pepeblush:890638472036114473> ')
    if msg.startswith('its my birthday'):
        time.sleep(2)
        await say('happy birthday man<:pepeblush:890638472036114473> ')

    #if u call brown sus
    if msg.startswith('sus'):
        time.sleep(2)
        await say('||no im not||')

    #office api commands
    if msg.startswith('office quote brown'):
        time.sleep(2)
        quote = get_quote()
        await say(quote)
    if msg.startswith('office episode brown'):
        await say('rewatching entire office library...')
        time.sleep(2)
        await say('...fuck theyre all awesome...')
        time.sleep(2)
        await say('...ok watch this one')
        time.sleep(1)
        episode = get_episode()
        await say(episode)

    #cat api command
    if msg.startswith('cat brown'):
        time.sleep(2)
        await say('scanning for best kitten <:cat:903757470399340584>...')
        time.sleep(3)
        cat = get_cat()
        await say(cat)

    #if u say smth sus
    if any(word in msg for word in sus_triggers):
        await say(random.choice(sus_responses))

    #hey brown [your question]
    if msg.startswith('hey brown'):
        time.sleep(2)
        if any(word in msg for word in no_u_triggers):
            await say(random.choice(no_u_responses))
        elif any(word in msg for word in wellbeing_triggers):
            await say(random.choice(wellbeing_responses))
        else:
            await say(random.choice(questions))

    #kills brown, sends url image of his dead body
    if msg.startswith('System.override.kill_brown'):
        time.sleep(2)
        await say(
            random.choice(dies_responses) +
            '**Brown cannot overide user instructions.**')
        await say('**Chasing brown...**')
        time.sleep(3)
        time.sleep(2)
        await say('**Brown tried hiding in his vent...**')
        time.sleep(1)
        await say('**Firing F-2000 Assault Rifle...**')
        time.sleep(5)
        await say('**Successfully shot brown...**')
        time.sleep(2)
        await say('**Brown is trying to call his son...**')
        time.sleep(3)

        async with aiohttp.ClientSession() as session:
            async with session.get(
                    'https://preview.redd.it/n7acnf9lwbo51.png?width=440&format=png&auto=webp&s=34e6cd219339fa6a2e2d9882ba62c7ac04d69c9e'
            ) as resp:
                if resp.status != 200:
                    return await message.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await say(file=discord.File(data, 'n7acnf9lwbo51.png'))
        await say('**Brown has been terminated.**')
        time.sleep(2 * 60)
        await say('*Brown has respawned*')
    #brown decides what we do
    if msg.startswith('what should we do brown'):
        await say('using advanced algorithms...')
        time.sleep(1)
        await say('...to figure out optimal activity...')
        time.sleep(1)
        await say('...results are in:')
        time.sleep(1)
        await say(random.choice(options))

    #if alexa,siri...are mentioned
    if any(word in msg for word in competition):
        await say("fuck that bitch")

    #whos right brown, brown will decide who is right in an argument
    if msg.startswith('whos right brown'):
        time.sleep(1)
        await say(random.choice(whos_right1))
        time.sleep(3)
        myid = '<@' + random.choice(ids) + '>'
        await say(myid + ' ' + random.choice(whos_right2))

    #leave the server brown command
    if msg.startswith('leave the server brown'):
        time.sleep(4)
        await say('oh')
        time.sleep(2)
        await say('okay')
        time.sleep(2)
        await say('ill see myself out then')
        time.sleep(4)
        await say('System.override.kill_brown')
        time.sleep(2)
        await say('System.override.kill_brown')
        time.sleep(1)
        await say('doesnt work when i say it haha :sweat_smile:')

    #if tell brown happy new year
    if msg.startswith('happy new year'):
        time.sleep(2)
        await say('happy new year yall :))')

    #end of @client.event, line bellow makes sure client.command() stil works
    await client.process_commands(message)


#sunarthsh pou krataei server anoixto
keep_alive()
#to key tou bot mas, dont share it tha mas xakaroun to server
client.run('OTAxMjg5MTYzNzQyMTQyNDc0.YXNs8Q.SisEixfAv1WMocZRe-nnKyxCD-o')
