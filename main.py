#Import Packages
import discord
from discord.ext import commands
import random
import json
import requests
import os
import json

# open json file

os.chdir('C:\\Users\\skyar\\Desktop\\EvoBot')

# Client
client = commands.Bot(command_prefix='~')
client.remove_command("help")

#quotes from website

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return(quote)

# variables

randomfacts = [
"```It is impossible for most people to lick their own elbow. (try it!)```",
"```A crocodile cannot stick its tongue out.```",
"```A shrimp's heart is in its head.```",
"```It is physically impossible for pigs to look up into the sky.```",
"```If you sneeze too hard, you could fracture a rib.```",
"```Wearing headphones for just an hour could increase the bacteria in your ear by 700 times.```",
"```In the course of an average lifetime, while sleeping you might eat around 70 assorted insects and 10 spiders, or more.```",
"```Some lipsticks contain fish scales.```",
"```There are 293 ways to make change for a dollar.```",
"```The average person's left hand does 56 percent of the typing (when using the proper position of the hands on the keyboard; Hunting and pecking doesn't count!).```",
"```A shark is the only known fish that can blink with both eyes.```",
'```The longest one-syllable words in the English language are "scraunched" and "strengthed"```',
'```Some suggest that "squirreled" could be included, but squirrel is intended to be pronounced as two syllables (squir-rel) according to most dictionaries```', 
'```"Screeched" and "strengths" are two other long one-syllable words, but they only have 9 letters.```',
"```Almonds are a member of the peach family.```",
"```Maine is the only state that has a one-syllable name.```",
'```There are only four words in the English language which end in "dous": tremendous, horrendous, stupendous, and hazardous.```',
'```Los Angeles full name is "El Pueblo de Nuestra Senora la Reina de los Angeles de Porciuncula"```',
"```A cat has 32 muscles in each ear.```",
"```An ostrich's eye is bigger than its brain.```",
"```Tigers have striped skin, not just striped fur.",
"```In many advertisements, the time displayed on a watch is 10:10.```",
"```The characters Bert and Ernie on Sesame Street were named after Bert the cop and Ernie the taxi driver in Frank Capra's It's a Wonderful Life.```",
"```A dime has 118 ridges around the edge.```",
"```The giant squid has the largest eyes in the world.```",
"```Most people fall asleep in seven minutes.```",
"```Stewardesses is the longest word that is typed with only the left hand```"
]

# Colors
colors= [0x000000, 0xffffff, 0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0x00FFFF, 0xFF00FF]

# Tips

tipsEvo = [
    'Use a **Ravager Horn** to call an ally raid into a village',
    '**Tigers** are stealthy hunters, be careful when traversing the jungle',
    '**Myrmex** have a reputation system going from -100 to 100, you can befriend them and even create new coloies',
    '**Lightning Dragons**, unlike Ice and Fire dragons, are nocturnal and sleep during the day',
    'Using **Acacia Blossoms**, you can tame tuskless Elephants',
    '**Guard Villagers** can be created by shift right clicking a villager with a sword or crossbow',
    'Using a **Heavy Workbench**, you can upgrade your weapons and armor at the cost of levels',
    'With the **Raid Hero** effect, you can barter emeralds with pillagers to acquire items such as Crossbows, Horse Armor, Saddles, and the Heavy Workbench',
    '**Mantis Shrimp** can be tamed and ordered to break blocks they are holding',
    'The deeper you go the more **drowning** damage you will take',
    'The **Undergarden** is accessed using a Catalyst on stone bricks arranged like a nether portal',
    '1 block in the **Undergarden** is 4 blocks in the Overworld'
]
nsfwpic= [
    "https://cdn.discordapp.com/attachments/833130130741526539/842521765247057940/image0.jpg",
    "https://cdn.discordapp.com/attachments/842120710805782578/842241959388250112/image0.png",
    "https://cdn.discordapp.com/attachments/833130130741526539/842524327048118282/image0.jpg",
    "https://media.discordapp.net/attachments/833130130741526539/842534052207525898/E1KlEc8VcAAcwOM.jpg"

]
expt = [
    "expects",
    'expect',
    'expecting',
    'expected',
    "Expects",
    'Expect',
    'Expecting',
    'Expected'

]
# Shop
mainshop = [{"name": "Watch", "price":100, "description": "Time"}, {"name": "Laptop", "price":750, "description": "Epic Gaming"}, {"name": "PC", "price":4500, "description": "Pro Gaming"}]
# start client
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=".... . .-.. .--. / -- . | ~help"))
    print('We have logged in as {0.user}'.format(client))

# Cogs
@client.command()
async def load(ctx, extension):
    client.load_extention(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extention(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# Error

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("***Still on cooldown***, please try again in {:.2f}s".format(error.retry_after))

# Commands
@client.command()
async def version(ctx):
    Myembed = discord.Embed(title="Current Version", description = "The bot is in Version 1.0", color = (random.choice(colors)))
    Myembed.add_field(name="Version Code", value="v1.0.0", inline=False)
    Myembed.add_field(name="Date Relased", value="May 5th, 2021")
    Myembed.set_author(name='Evo')
        
    await ctx.send(embed=Myembed)

@client.command()
async def ping(ctx):

    await ctx.send(f'```\nPong! {round(client.latency*1000)}ms\n```')

@client.command()
async def help(ctx):
    help_embed = discord.Embed(title='Help', description = "All the bot commands", color = (random.choice(colors)))
    help_embed.add_field(name='~tips', value='Get tips for the upcoming season of Monke Craft', inline=False)
    help_embed.add_field(name='~quote', value='Get a random quote', inline=False)
    help_embed.add_field(name= '~help', value= 'Help command for the bot', inline=False)
    help_embed.add_field(name='~fact', value='get a random fact', inline=False)
    help_embed.add_field(name="~ping", value='Pong, also get bot latency', inline=False)
    help_embed.add_field(name= '~sexy', value = 'NSFW', inline=False)
    help_embed.add_field(name= '~sendinv', value = 'Get bot inv', inline=False)
    help_embed.add_field(name='~sus', value='Amongus', inline=False)
    help_embed.add_field(name = '~balance', value = 'Shows your bank and wallet balance', inline=False)
    help_embed.add_field(name='~beg', value = "you get money", inline=False)
    help_embed.add_field(name = '~withd', value = 'You can take money out of ur bank', inline=False)
    help_embed.add_field(name='~dep', value='Deposit money in ur bank', inline=False)
    help_embed.set_footer(text='all this is still wip')
        
    await ctx.send(embed=help_embed)

@client.command()
async def fact(ctx):

    await ctx.send(random.choice(randomfacts))

@client.command()
async def quote(ctx):

    quote=get_quote()

    await ctx.send(f'```{quote}```')

@client.command()
async def sexy(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(random.choice(nsfwpic))

@client.command()
@commands.cooldown(1,15,commands.BucketType.user)
async def tips(ctx):
    await ctx.send(random.choice(tipsEvo))

@client.command()
async def sendinv(ctx):
    await ctx.send('https://discord.com/api/oauth2/authorize?client_id=691463184095248415&permissions=2889350214&scope=bot')

@client.command()
async def sus(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send('https://cdn.discordapp.com/attachments/833784979406061569/842159929666043924/among-us-player-red-512.png')
    await ctx.send('sus')


#Economy stuff

# Shop command

@client.command()
async def shop(ctx):
    em = discord.Embed(title = "Shop")
    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item['description']
        em.add_field(name = name, value = f'${price} | {desc}')

    await ctx.send(embed = em)

# Buy command

async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
            return


    await ctx.send(f"You just bought {amount} {item}")

@client.command()
async def bag(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []


    em = discord.Embed(title = "Bag")
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name = name, value = amount)    

    await ctx.send(embed = em) 




# Helper Functions
async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users: 
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open("mainbank.json", "w") as f:
        json.dump(users,f)
    return True

async def get_bank_data():
    with open('mainbank.json','r') as f:
        users = json.load(f)
    return users

async def update_bank(user, change = 0, mode = 'wallet'):
    users = await get_bank_data()

    users[str(user.id)][mode] += change
    
    with open('mainbank.json', 'w') as f:
        json.dump(users, f)

    bal = [users[str(user.id)]['wallet'], users[str(user.id)]['bank']]
    return bal 

async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None

    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]        

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]



    




# Run the client on the server
client.run('TOKEN')
