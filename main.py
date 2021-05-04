import os
import random
import requests
import json
import csv
import pandas

from keep_alive import keep_alive
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='--')

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command(name='98', help='Antos')
async def antos(ctx):

    await ctx.send("I think Antos is really cool")

@bot.command(name='17', help='Clears Chat')
async def one_seven(ctx):

    message = "Conor is Unique ```\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r```"
    await ctx.send(message)

@bot.command(name='66', help='Nerd Call')
async def six_six(ctx):

    await ctx.send("@here ``` It is time for video games ```")

@bot.command(name='7', help='Billy')
async def zero_seven(ctx):

    await ctx.send("``` If A is for Apple and B is for Banana, what is C for? ```" + "```Plastic Explosives```")

@bot.command(name='21', help='Jack')
async def jack(ctx):

    await ctx.send("https://tenor.com/view/team-america-team-america-world-police-world-police-trey-parker-gary-gif-14802263")

@bot.command(name='69', help='Dirty')
async def six_nine(ctx):

    await ctx.send("``` Конор перестанет быть возбужденным```")

@bot.command(name='14', help="I'm not sure")
async def one_four(ctx):

    await ctx.send("https://www.youtube.com/watch?v=twjINA8dc4o")

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int):
    dice = [
        str(random.choice(range(1, 7)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(' '.join(dice))
    # @bot.command(name="rand", help="Picks a random number")
    # async def random

@bot.command(name='pick', help="Help's you decide what game to play")
async def pick_game(ctx):
    games = [
        "```League of Legends``` https://tenor.com/view/teemo-league-of-legends-trumpet-kick-gif-16332190",
        "```Counter Strike: Global Offensive``` https://tenor.com/view/counter-strike-counter_strike-counter_strike_source-cs_s-css-gif-14614580",
        "```Apex Legends``` https://tenor.com/view/wraith-apexdance-octane-dance-blood-gif-17961190",
        "```Bloons TDM6``` https://tenor.com/view/bloons-monkey-ninja-kiwi-bloons-tower-defense6-btd-gif-18355981",
        "```Minecraft``` https://tenor.com/view/default-dance-minecraft-steve-fortnite-herobrine-gif-16446396",
        "```Among Us (Lol No, Get fcked, try again)``` https://tenor.com/view/among-us-discord-gif-18555996",
        "```Puzzle Together``` https://tenor.com/view/simpsons-homer-jigsaw-puzzle-smash-gif-16752652",
        "```Tom Clancy's Rainbow Six Siege``` https://tenor.com/view/r6-rainbow6gamers-hysterical-movements-gif-16556373",
        "```Overwatch``` https://tenor.com/view/idk-mccree-overwatch-anime-cute-gif-8016115",
        "Valheim"
    ]

    myinte = random.choice(games)
    await ctx.send(myinte)

# Attempting to use API's
# def jprint(obj):
#   # create a formatted string of the Python JSON object
#   text = json.dumps(obj, sort_keys=True, indent=4)
#   print(text)

#     # with open("data_file.csv", "w") as write_file:
#     #     json.dump(text, write_file)


# response = requests.get("https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/fB3pzQG2Q5vNNdty9eIsxeLDKk58qNxNBVDCFyrA9j-GUOOL?api_key=***")
# #jprint(response.json())

# dic = response.json()
# df = pandas.DataFrame(dic)
# df.to_csv('data_file.csv', index=False)


# with open('data_file.csv', 'r') as f:
#   data = csv.reader(f)
#   for row in data:
#     wins = row[7]
#     losses = row[8]

# losses1 = int(losses)
# losses2 = int(losses) # when called the second time this is executed

# @bot.command(name='test', help='test')
# async def test(ctx):
#     response = requests.get("https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/fB3pzQG2Q5vNNdty9eIsxeLDKk58qNxNBVDCFyrA9j-GUOOL?api_key=****")
#     dic = response.json()
#     df = pandas.DataFrame(dic)
#     df.to_csv('data_file.csv', index=False)
    
#     # messagetoprompt = ("Conor has lost " + losses + " games")
#     messagetoprompt = ("API TOKEN EXPIRED")
#     await ctx.send(messagetoprompt)
    

# # When pinged request API and then VV
# if losses2 > losses1:
#   losses1 = losses
#   print("LOL Conor just lost a game")
#   print(losses2 + " losses... sheessshh")

keep_alive()
bot.run(TOKEN)


  