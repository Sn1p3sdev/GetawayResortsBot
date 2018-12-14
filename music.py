import discord
from discord.ext import commands

class Music:
    def __init__(self, self.client):
        self.self.client = self.client

@self.client.command(pass_context=True)
async def join(ctx):
		channel = ctx.message.author.voice.voice_channel
		await self.client.join_voice_channel(channel)
		print('Joined voice channel: {}'.format(channel))

@self.client.command(pass_context=True)
async def leave(ctx):
	server = ctx.message.server
	voice_self.client = self.client.voice_self.client_in(server)
	await voice_self.client.disconnect()
	print('Left voice channel: {}'.format(voice_self.client))

#@self.client.command(pass_context=True)
#async def play(ctx, url):
#	server = ctx.message.server
#	voice_self.client = self.client.voice_self.client_in(server)
#	player = await voice_self.client.create_ytdl_player(url)
#	players[server.id] = player
#	player.start()
