import discord
from discord.ext import commands

class Moderation:
    def __init__(self, self.client):
        self.self.client = self.client

    @self.client.command(pass_context=True)
    async def clear(ctx, amount=1000):
    	channel = ctx.message.channel
    	messages = []
    	async for message in self.client.logs_from(channel, limit=int(amount) + 1):
    		messages.append(message)
    	await self.client.delete_messages(messages)
    	await self.client.say('Messages deleted.')
    	print('Command "clear" has been run. Messages have been deleted.')

    @self.client.command(pass_context=True)
    async def mute(ctx, member: discord.Member):
         if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '194151340090327041':
            role = discord.utils.get(member.server.roles, name='Muted')
            await bot.add_roles(member, role)
            embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
            await bot.say(embed=embed)
         else:
            embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
            await bot.say(embed=embed)

@self.client.command()
async def kick(ctx, member: discord.Member=None):
	if not member:
		await ctx.send('{} Please specify a member.'.format(ctx.message.author.mention))
		return
	await member.kick()
	await ctx.send(f'{member.mention} has been kicked.')

@self.client.command()
async def ban(ctx, member: discord.Member=None):
	if not member:
		await ctx.send('{} Please specify a member.'.format(ctx.message.author.mention))
		return
	await member.ban()
	await ctx.send(f'{member.mention} has been banned.')
