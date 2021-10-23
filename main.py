import discord
import requests
import random
import os
from keep_alive import keep_alive

client = discord.Client()
"""listes me keywords"""

#otan leei o xrhsths leksh apo no_u_triggers mesa se hey brown entolh, apantaei me no_u_responses
no_u_triggers = [
    "fuck u", "fu", "fuck you", "γαμησου", "γαμιεσε", "πεθανεις", "μαλακα",
    "εισαι μαλακας", "u suck", "πεθανεις", "πουστη", "εισαι πουστης",
    "είσαι πουστης", "you die", "kys", "kill your self", "kill ur self", "cunt"
]

no_u_responses = [
    "no u", "fu", "stfu", "ok <:pepecrylaptop:891714887624065045>",
    "<:doom:890646102330732574>", "||*no you*||"
]

#otan leei o xrhsths leksh apo sus_triggers apantaei me sus_responses
sus_triggers = [
    "pousths", "gay", "γκει", "αδερφή", "νεράιδα", "νεραιδα", "neraida",
    "dick", "peos", "πεος", "μπουτσα", "πουτσο", "penis", "anal", "butt",
    "poutsa", "mpoutso", "πουτσα"
]

sus_responses = ["||sus||", "<:y_gay:890646222157779075> "]

#apanthseis brown se hey brown entolh
questions = [
    "<:perhaps:890648088442699846> ",
    "profanws",
    "no",
    "bruh ||fuck no||",
    "bruh ||fuck yes||",
    "yess <:pepeblush:890638472036114473> ",
    "<:um:891714963259928637> ",
    "heh ||...yeah||",
    "**NO**",
    "im busy",
    "<:kek1:884139110980284426> ",
    "<:idk:890646139441930261> ",
    "cant talk rn",
    "shh",
]
"""sunarthseis"""


#sunarthsh gia office quote api
def get_quote():
    response = requests.get("https://officeapi.dev/api/quotes/random")
    quote = response.json()
    return (quote['data']['content'] + "\n - " +
            quote['data']['character']['firstname'] + " " +
            quote['data']['character']['lastname'])


#sunarthsh gia cat photos api
def get_cat():
    response = requests.get(
        "https://api.thecatapi.com/v1/images/search?api_key=e2dec158-0a3c-4f01-a7a5-fd29ea207b92"
    )
    cat = response.json()[0]['url']
    return (cat)


@client.event
async def on_ready():
    print('{0.user}'.format(client) + ' is online')


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    msg = message.content
    #entoles gia brown
    if msg.startswith('help brown'):
        await message.channel.send(
            '**BROWN USER GUIDE**\n \n-**hi brown**: brown will say hi back\n-**bye brown**: brown will say bye back\n-**office brown**: brown will send u office quote\n-**cat brown**: brown will send u cat image/gif\n-**hey brown** *[your question]*: brown will answer'
        )

    if msg.startswith('hi brown'):
        await message.channel.send('henlo')

    if msg.startswith('bye brown'):
        await message.channel.send('bye <:nightWorld:891424681247248464> ')

    if msg.startswith('brown'):
        await message.channel.send('wtf')

    if msg.startswith('sus'):
        await message.channel.send('||no im not||')

    if msg.startswith('office brown'):
        quote = get_quote()
        await message.channel.send(quote)

    if msg.startswith('cat brown'):
        cat = get_cat()
        await message.channel.send(cat)

    if any(word in msg for word in sus_triggers):
        await message.channel.send(random.choice(sus_responses))

    if msg.startswith('hey brown'):
        if any(word in msg for word in no_u_triggers):
            await message.channel.send(random.choice(no_u_responses))
        else:
            await message.channel.send(random.choice(questions))


#sunarthsh pou krataei server anoixto
keep_alive()
#to key tou bot mas, dont share it tha mas xakaroun to server
client.run(os.getenv('TOKEN'))
