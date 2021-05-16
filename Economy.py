import discord
from discord import client
from discord.ext import commands
import random
import json
import requests
import os
import json

class Economy(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):

        print('Economy Cog is online')


# Economy stuff
    mainshop = [{"name": "Watch", "price":100, "description": "Time"}, {"name": "Laptop", "price":750, "description": "Epic Gaming"}, {"name": "PC", "price":4500, "description": "Pro Gaming"}]   

# Balance
    @commands.command()
    async def bal(self, ctx):
        await open_account(ctx.author)
        user = ctx.author
        users = await get_bank_data()

        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"] 

        em = discord.Embed(title = f"{ctx.author.name}'s balance", color = discord.Color.dark_gold())
        em.add_field(name = 'Wallet Balance', value = wallet_amt)
        em.add_field(name = 'Bank Balance', value = bank_amt)
        await ctx.send(embed = em)

# Beg

    @commands.command()
    @commands.cooldown(1,60,commands.BucketType.user)
    async def beg(self, ctx):
        await open_account(ctx.author)
        user = ctx.author
        users = await get_bank_data()

        earning = random.randrange(101)

        await ctx.send(f"Someone gave you {earning} coins!!")

        users[str(user.id)]["wallet"] += earning

        with open("mainbank.json", "w") as f:
            json.dump(users,f)

# Withdraw
    @commands.command()
    async def withd(self, ctx, amount = None):
        await open_account(ctx.author)
        if amount == None:
            await ctx.send("Please enter the amount you want to withdraw - ``~withd <number>``")
            return

        bal = await update_bank(ctx.author)

        amount = int(amount)
        if amount>bal[1]:
            await ctx.send("You to poor for that")  
            return
        if amount<0:
            await ctx.send("Mate, how tf do you have negative money")
            return
        await update_bank(ctx.author, amount)
        await update_bank(ctx.author,-1*amount,"bank")

        await ctx.send(f"You withdrew {amount} coins!")
    
# Deposit
    @commands.command()
    async def dep(self, ctx, amount = None):
        await open_account(ctx.author)
        if amount == None:
            await ctx.send("Please enter the amount you want to deposit - ``~dep <number>``")
            return

        bal = await update_bank(ctx.author)

        amount = int(amount)
        if amount>bal[0]:
            await ctx.send("You to poor for that")  
            return
        if amount<0:
            await ctx.send("Mate, how tf do you have negative money")
            return
        await update_bank(ctx.author, -1*amount)
        await update_bank(ctx.author,amount,"bank")

        await ctx.send(f"You deposited {amount} coins!")

# Send Money
    @commands.command()
    async def send(self, ctx,member:discord.Member,amount = None):
        await open_account(ctx.author)
        await open_account(member)
        if amount == None:
            await ctx.send("Please enter the amount you want to send - ``~send <number>``")
            return

        bal = await update_bank(ctx.author)

        amount = int(amount)
        if amount>bal[1]:
            await ctx.send("You to poor for that")  
            return
        if amount<0:
            await ctx.send("Mate, how tf do you have negative money")
            return
        await update_bank(ctx.author, -1*amount,"bank")
        await update_bank(member,amount,"bank")

        await ctx.send(f"You gave {amount} coins!")

# Gambling (slots)
    @commands.command()
    async def slots(self,ctx,amount = None):
        await open_account(ctx.author)
        if amount == None:
            await ctx.send("Please enter the amount you want to gamble - ``~slots <number>``")
            return

        bal = await update_bank(ctx.author)

        amount = int(amount)
        if amount>bal[0]:
            await ctx.send("You to poor for that")  
            return
        if amount<0:
            await ctx.send("Mate, how tf do you have negative money")
            return

        final = []
        for i in range(3):
            a= random.choice(["X","O", 'Q'])

            final.append(a)
        await ctx.send(str(final))

        if final[0] == final[1] or final[0] == final[2] or final[2] == final[1]:
            await update_bank(ctx.author, 2*amount)
            await ctx.send(f'you won!!')
        else:
            await update_bank(ctx.author, -1*amount)
            await ctx.send(f'you lost.')

    @commands.command(aliases = ["lb"])
    async def leaderboard(self, ctx,x = 1):
        users = await get_bank_data()
        leader_board = {}
        total = []
        for user in users:
            name = int(user)
            total_amount = users[user]["wallet"] + users[user]["bank"]
            leader_board[total_amount] = name
            total.append(total_amount)

        total = sorted(total,reverse=True)    

        em = discord.Embed(title = f"Top {x} Richest People" , description = "This is decided on the basis of raw money in the bank and wallet",color = discord.Color(0xfa43ee))
        index = 1
        for amt in total:
            id_ = leader_board[amt]
            member = client.get_user(id_)
            name = member.name
            em.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = False)
            if index == x:
                break
            else:
                index += 1

        await ctx.send(embed = em)
      

        


# Helper functions

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






# DO NOT TOUCH
def setup(client):
    client.add_cog(Economy(client))