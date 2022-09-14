from __future__ import print_function

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import discord
from discord.ext import commands
import time

TOKEN =""

client = discord.Client()

cred = credentials.Certificate('firebase.json')


databaseurl = ""

firebase_admin.initialize_app(cred, {'databaseURL': databaseurl})


# def update():
    

#     ref = db.reference(f"/")
#     x='user'
#     ref.update({x:{'color':'poop', 'balance': 170}})

#     return

# #update()
def wl(user, name, timestamp, address):
    ref = db.reference(f"/")
    ref.update({user:{'name':name, 'timestamp': timestamp, 'address': address}})
    return

# def startfire(user):
#     ref = db.reference(f"/")
#     ref.update({user:{'balance':100, 'twitter': 'false'}})
#     return

# def updatebalance(user,balance):
#     ref = db.reference(f"/")
#     ref.update({user:{'balance':balance}})
#     return

# def updatetwitter(user,balance):
#     b = readbalance(user)
#     b += balance
#     ref = db.reference(user)
#     ref.update({user:{'balance':b , 'twitter' : 'true'}})
#     return(b)

# def readbalance(user):
#     ref = db.reference(user)
#     x = ref.get()
#     b = int(x['balance'])
#     return(b)


def readfire(user):
    ref = db.reference(user)
    x = ref.get()
    #print(x)
    return(x)


#print(readfire)
#readfire()

client = discord.Client()



@client.event
async def on_message(message):

    if message.content.startswith('!whitelist'):
        personid = str(message.author.id)
        person= str(message.author.name)
        timestamp = str(message.created_at)


        addy=str(message.content).split(" ",1)[1]


        resp = readfire(user=personid)
        print(resp)

        if resp == None:
            wl(user=personid, name=person, timestamp=timestamp, address=addy)
            print('wl success')
            await message.channel.send(str(person) + ': ' +' You have been whitelisted!')


        if resp != None:
          print('already registered')
          await message.channel.send(str(person)+': Already whitelisted!')

# @client.event
# async def on_message(message):

#     if message.content.startswith('!wallet'):
#         personid = str(message.author.id)
#         person=str(message.author.name)

#         resp = readfire(user=person)

#         if resp == None:
#             startfire(personid)
#             await message.channel.send(str(person) + ': ' +' Your wallet has been created!')


#         if resp != None:
#           print('already registered')
#           await message.channel.send(str(person)+': already has a wallet!')
#         #await message.channel.send("hello!")


#     if message.content.startswith('!balance'):
#         personid = str(message.author.id)
#         person=str(message.author.name)

#         resp=readfire(personid)

#         if resp != None:

#             balance = readbalance(personid)
#             await message.channel.send(str(person) + ': ' +' Your balance is: '+str(balance))

#         if resp == None:
#             await message.channel.send(str(person) + ': ' +' Use !wallet to create your wallet!')



#     if message.content.startswith('!spin'):
#         personid = str(message.author.id)
#         person=str(message.author.name)
#         mes=str(message.content).split(" ",1)[1]
#         guess = int(mes)

#         answer = random.randint(1,3)

#         resp=readfire(personid)

#         if resp != None:

#             balance = readbalance(personid)
#             if balance >=5:
#                 if guess == answer:
#                     balance += 5
#                     updatebalance(personid,balance)
#                     await message.channel.send(str(person) + ': ' +' Congrats you won 5 points!')

#                 else:
#                     await message.channel.send(str(person) + ': ' +' Wrong answer, better luck next time!')
#             else:
#                 await message.channel.send(str(person) + ': ' +' not enough money!')

#         if resp == None:
#             await message.channel.send(str(person) + ': ' +' Use !wallet to create your wallet!')
        




@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client.run(TOKEN)
