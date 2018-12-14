import discord
import asyncio
import json
from discord.ext import commands
from itertools import cycle

#settings or values

TOKEN = 'NTE5NjU2NTM4MDM0NDA1Mzk3.Duifaw.Peoy1GOMWO9SCW_yQfiGKxNyWio'
client = commands.Bot(command_prefix = '>')
status = ['at Getaway Resorts', 'with iifluxi', 'with zultra500', 'with manslo', 'with iiPokiesi']
client.remove_command('help')

#cool loopy stuff

async def change_playing_status():
	await client.wait_until_ready()
	msgs = cycle(status)
	while not client.is_closed:
		current_status = next(msgs)
		await self.client.change_presence(game=discord.Game(name=current_status, type = 3))
		await asyncio.sleep(5)
#E V E N T S ! ! !

#ON_events
@client.event
async def on_ready():
	print('The bot is now live.')
	print('The bot is being hosted on Heroku.')

@client.event
async def on_message(message):
	print('A user has sent a message.')
	await self.client.process_commands(message)

@client.event
async def on_member_join():
	role = discord.utils.get(member.server.roles, name='Member')
	await self.client.add_roles(member, role)

@client.event
async def on_reaction_add():
	channel = reaction.message.channel
	await self.client.send_

#LvL System
#@self.client.event
#async def on_member_join():
#	with open ('users.json', 'r') as f:
#		users = json.load(f)
#
#		await update_data(users, message.author)
#
#	with open('users.json', 'w') as f:
#		users = json.load(f)
#
#@self.client.event
#async def on_message(message):
#	with open('users.json', 'r') as f:
#		users = json.load(f)
#
#	await update_data(users, message.author)
#	await add_experience(users, message.author, 5)
#	await level_up(users, message.author, message.channel)
#
#	with open('users.json', 'w') as f:
#		json.dump(users, f)
#
#async def update_data(users, user):
#	if not user.id in users:
#		users[user.id] = {}
#		users[user.id]['experience'] = 0
#		users[user.id]['level'] = 1
#
#async def add_experience(users, user, exp):
#	users[user.id]['experience'] += exp
#
#async def level_up(users, user, channel):
#	experience = users[user.id]['experience']
#	lvl_start = users[user.id]['level']
#	lvl_end = int(experience ** (1/4))
#
#	if lvl_start < lvl_end:
#		await self.client.send_message(channel, '{} has leveled up to level {}!!! Congrats {}!!!'.format(user.mention, lvl_end, user.mention))
#		users[user.id]['level'] = lvl_end


#C O M M A N D S ! ! !

#Cogs
def setup(client):
	client.add_cog(Fun(client))

def setup(client):
	client.add_cog(Moderation(client))

def setup(client):
	client.add_cog(Music(client))

def setup(client):
	client.add_cog(Other(client))

#moderation commands
#misc. commands
self.client.loop.create_task(change_playing_status())
self.client.run(TOKEN)
