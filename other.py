import discord
from discord.ext import commands

class Other:
    def __init__(self, self.client):
        self.self.client = self.client

@self.client.command()
async def logout(ctx):
    if ctx.message.author == "Sn1p3sdev" or "manslo":
        await self.client.logout()
        client.say("Shutting down...")
        print("{} has initiated a complete shut down of the bot. Shutting down now.".format(ctx.message.author))
    else:
        client.say("You do not have the perms to preform a shutdown.")
        print("{} has insufficient perms to preform a shutdown.".format(ctx.message.author))

@self.client.command()
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

	await self.client.say(embed=embed)

@self.client.command(pass_context=True)
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

	await self.client.say(embed=embed)

@self.client.command(pass_context=True)
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

	await self.client.say( 'Check your DMs.')
	await self.client.send_message(author, embed=embed)

#announcing commands
@self.client.command()
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

	await self.client.say(embed=embed)


@self.client.command(pass_context=True)
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

	await self.client.say(embed=embed)

@self.client.command(pass_context=True)
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

	await self.client.say(embed=embed)

@self.client.event
async def on_message_delete():
	author = message.author
	content = message.content
	channel = message.channel
	await self.client.send_message(channel, '{}: {}'.format(author, content))
