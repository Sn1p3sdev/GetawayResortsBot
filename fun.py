import discord
from discord.ext import commands

class Fun:
    def __init__(self, self.client):
        self.self.client = self.client

    @self.client.command()
    async def ping():
    	await self.client.say('Pong!:ping_pong: ')
    	print('Command "ping" has been run.')

    @self.client.command()
    async def pong():
    	await self.client.say(':ping_pong: Ping!')
    	print('Command "pong" has been run.')

    @self.client.command()
    async def echo(*args):
    	output = ''
    	for word in args:
    		output +- word
    		output +- ' '
    	await self.client.say(output)
