import discord
import asyncio
import json
from discord.ext import commands
from itertools import cycle

#settings or values

TOKEN = 'NTE5NjU2NTM4MDM0NDA1Mzk3.Duifaw.Peoy1GOMWO9SCW_yQfiGKxNyWio'
client = commands.Bot(command_prefix = 'GR!')
status = ['to what the people want.']
#status = ['at Getaway Resorts', 'with iifluxi', 'with zultra500', 'with manslo', 'with BabySage']
client.remove_command('help')

#cool loopy stuff

async def change_playing_status():
	await client.wait_until_ready()
	msgs = cycle(status)
	while not client.is_closed:
		current_status = next(msgs)
		await client.change_presence(game=discord.Game(name=current_status, url="https://www.twitch.tv/Sn1p3sdev" ,type = 2))#1 for streaming. I think...
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
	await client.process_commands(message)

@client.event
async def on_member_join():
	role = discord.utils.get(member.server.roles, name='Member')
	await client.add_roles(member, role)

@client.event
async def on_reaction_add():
	channel = reaction.message.channel
	await client.send_

#LvL System
#@client.event
#async def on_member_join():
#	with open ('users.json', 'r') as f:
#		users = json.load(f)
#
#		await update_data(users, message.author)
#
#	with open('users.json', 'w') as f:
#		users = json.load(f)
#
#@client.event
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
#		await client.send_message(channel, '{} has leveled up to level {}!!! Congrats {}!!!'.format(user.mention, lvl_end, user.mention))
#		users[user.id]['level'] = lvl_end


#C O M M A N D S ! ! !

#fun commands
@client.command()
async def ping():
	await client.say('Pong!:ping_pong: ')
	print('Command "ping" has been run.')

@client.command()
async def pong():
	await client.say(':ping_pong: Ping!')
	print('Command "pong" has been run.')

@client.command()
async def echo(*args):
	output = ''
	for word in args:
		output +- word
		output +- ' '
	await client.say(output)

#moderation commands
@client.command(pass_context=True)
async def clear(ctx, amount=1000):
	channel = ctx.message.channel
	messages = []
	async for message in client.logs_from(channel, limit=int(amount) + 1):
		messages.append(message)
	await client.delete_messages(messages)
	await client.say('Messages deleted.')
	print('Command "clear" has been run. Messages have been deleted.')

@client.command()
async def kick(ctx, member: discord.Member=None):
	if not member:
		await client.send("Please specify a member.")
		return
	await member.kick()
	await client.send(f"{member.mention} has been kicked.")

@client.command()
async def ban(ctx, member: discord.Member=None):
	if not member:
		await client.send("Please specify a member.")
		return
	await member.ban()
	await client.send(f"{member.mention} has been banned.")

@client.command()
async def mute(ctx, member: discord.Member=None):
	role = discord.utils.get(ctx.guild.roles, name="G.R Muted")
	if not member:
		await client.send("Please specify a member.")
		return
	await member.add_roles(role)
	await client.send(f"{member.mention} has been muted!")

@client.command()
async def unmute(ctx, member: discord.Member=None):
	role = discord.utils.get(ctx.guild.roles, name="G.R Muted")
	if not member:
		await client.send("Please specify a member.")
		return
	await member.remove_roles(role)
	await client.send(f"{member.mention} has been unmuted.")
	await client.send("Make sure to watch out for them though!!!")

#music commands
@client.command(pass_context=True)
async def join(ctx):
	channel = ctx.message.author.voice.voice_channel
	await client.join_voice_channel(channel)
	print('Joined voice channel: {}'.format(channel))

@client.command(pass_context=True)
async def leave(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	await voice_client.disconnect()
	print('Left voice channel: {}'.format(voice_client))
#other commands
@client.command()
async def logout(ctx):
    if ctx.message.author == "Sn1p3sdev" or "manslo":
        await client.logout()
        client.say("Shutting down...")
        print("{} has initiated a complete shut down of the bot. Shutting down now.".format(ctx.message.author))
    else:
        client.say("You do not have the perms to preform a shutdown.")
        print("{} has insufficient perms to preform a shutdown.".format(ctx.message.author))

@client.command()
async def info():
	embed = discord.Embed(
		title = 'Info about the Getaway Resorts bot',
		colour = discord.Colour.red()
	)

	embed.set_footer(text='no u')
	embed.set_thumbnail(url='https://cdn.discordapp.com/app-icons/519656538034405397/cc0c1d9876df2948228391f3ea1f8167.png')
	embed.set_author(name='Getaway Resorts', icon_url='https://cdn.discordapp.com/icons/465869379675095051/683e02a5c32c314693ea95d663358766.png')
	embed.add_field(name='Name:', value='Getaway Resorts')
	embed.add_field(name='Description:', value='This bot was made for one purpose and one purpose only. \nIt was to help people. It is a gift from manslo to the group.')
	embed.add_field(name='Version:', value='v0.0.1 alpha')
	embed.add_field(name='Released On:', value='12/6/2018')

	await client.say(embed=embed)

@client.command(pass_context=True)
async def gift():
	embed = discord.Embed(
	title = "If you didn't know that this bot is a gift, well now you know. :P",
	colour = discord.Color.blue()
	)

	embed.set_footer(text='Made by manslo.'),
	embed.set_thumbnail(url='https://cdn.discordapp.com/app-icons/519656538034405397/cc0c1d9876df2948228391f3ea1f8167.png')
	embed.set_author(name='Getaway Resorts', icon_url='https://cdn.discordapp.com/icons/465869379675095051/683e02a5c32c314693ea95d663358766.png')
	embed.add_field(name='From:', value='manslo (SHR | 13 | Overseer)')
	embed.add_field(name='To:', value='To all of Getaway Resorts. All staff and guests.')
	embed.add_field(name='Purpose:', value='To ease the lives of all Getaway Resorts Discord Members.')

	await client.say(embed=embed)

@client.command(pass_context=True)
async def help(ctx):
	author = ctx.message.author

	embed = discord.Embed(
	title = 'Commands for Getaway Resorts',
	colour = discord.Color.blue(),
	#channel = message.channel
	)

	embed.set_author(name='Getaway Resorts')
	embed.set_thumbnail(url='https://cdn.discordapp.com/app-icons/519656538034405397/cc0c1d9876df2948228391f3ea1f8167.png')
	embed.add_field(name='**PREFIX:**', value='**>**', inline=True)
	embed.add_field(name='ping', value='Classic.', inline=True)
	embed.add_field(name='pong', value='Also a Classic.', inline=True)
	embed.add_field(name='clear', value='Clears messages.', inline=True)
	embed.add_field(name='logout', value='Makes the bot logout and shutdown.', inline=True)
	embed.add_field(name='info', value='Tells you all about the bot.', inline=True)
	embed.add_field(name='help', value='Shows all the commands that you are able to use.', inline=True)
	embed.add_field(name='gift', value='Shows the information about this gift.', inline=True)
	embed.set_footer(text='Made by manslo.')

	await client.say( 'Check your DMs.')
	await client.send_message(author, embed=embed)

#announcing commands
@client.command()
async def test(arg1, arg2):
	embed = discord.Embed(
	title = 'This is a test command!',
	colour = discord.Color.orange(),
	)

	embed.set_author(name='Getaway Resorts')
	embed.set_thumbnail(url='https://cdn.discordapp.com/app-icons/519656538034405397/cc0c1d9876df2948228391f3ea1f8167.png')
	embed.add_field(name='Below is the 1st argument!', value=(arg1))
	embed.add_field(name='Below is the 2nd argument!', value=(arg2))
	embed.set_footer(text='Made by manslo.')

	await client.say(embed=embed)


@client.command(pass_context=True)
async def training(ctx, arg1, arg2, arg3):
	author = ctx.message.author
	embed = discord.Embed(
	colour = discord.Color.green()
	)
	embed.set_author(name='Getaway Resorts')
	embed.set_thumbnail(url='https://cdn.discordapp.com/app-icons/519656538034405397/cc0c1d9876df2948228391f3ea1f8167.png')
	embed.add_field(name='Host:', value=(author))
	embed.add_field(name='Co-host:', value=(arg1))
	embed.add_field(name='When:', value=((arg2, arg3)))
	embed.add_field(name='Where:', value='[The Training Center](https://web.roblox.com/games/1905439067/Training-Facility-V2-Getaway-Resort)')
	embed.set_footer(text='Made by manslo.')

	await client.say(embed=embed)

@client.command(pass_context=True)
async def interviews(ctx, arg1, arg2, arg3):
	author = ctx.message.author
	embed = discord.Embed(
	colour = discord.Color.green()
	)
	embed.set_author(name='Getaway Resorts')
	embed.set_thumbnail(url='https://cdn.discordapp.com/app-icons/519656538034405397/cc0c1d9876df2948228391f3ea1f8167.png')
	embed.add_field(name='Host:', value=(author))
	embed.add_field(name='Co-host:', value=(arg1))
	embed.add_field(name='When:', value=((arg2, arg3)))
	embed.add_field(name='Where:', value='[The Interviews Center](https://web.roblox.com/games/1932127304/Interview-Centre-V2-Getaway-Resort)')
	embed.set_footer(text='Made by manslo.')

	await client.say(embed=embed)

@client.command(pass_context=True)
async def apply(ctx, arg1, arg2):
	author = ctx.message.author
	embed = discord.Embed(
	colour = discord.Color.blue()
	)
	embed.set_author(name='Getaway Resorts')
	embed.set_thumbnail(url='https://cdn.discordapp.com/app-icons/519656538034405397/cc0c1d9876df2948228391f3ea1f8167.png')
	embed.add_field(name='ROBLOX username:', value=(arg1))
	if arg2 == 'security' or 'Security' or 'Security Guard' or 'security guard':
		embed.add_field(name='Job being applied for:', value=(arg2))
	if arg2 == 'receptionist' or 'Receptionist' or 'front desk' or 'Front Desk':
		embed.add_field(name='Job being applied for:', value=(arg2))
	else:
		embed.add_field(name='Job being applied for:', value='The job you applied for is invalid. Please apply for either Security or Receptionist.')
	embed.set_footer(text='Made by manslo.')

	await client.say(embed=embed)

@client.command()
@client.event
async def on_message_delete():
	author = message.author
	content = message.content
	channel = message.channel
	await client.send_message(channel, '{}: {}'.format(author, content))
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
client.loop.create_task(change_playing_status())
client.run(TOKEN)
