import discord
import random as r
from discord.ext import commands

client = commands.Bot(command_prefix = '!')
client.remove_command('help')


sizel = [1,2,3,4,5,6,7,8]
lolhaha = ["nice", "not nice"]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def nice(ctx):
    await ctx.send(f"{ctx.author.mention} is {r.choice(lolhaha)}")


@client.command()
@commands.has_role('MOD')
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason),await ctx.send(f'{member.mention} kicked for {reason}.')


@client.command()
@commands.has_role('MOD')
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason), await ctx.send(f'{member.mention} has been banned for {reason}.')


@client.command()
@commands.has_role('MOD')
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')


    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


@client.command()
async def size(ctx, member : discord.Member):
    await ctx.send(f"{member.mention}'s brain is {r.choice(sizel)} inches long.")


@client.command()
async def hello(ctx):
    await ctx.send('Hello!')


@client.command()
async def help(ctx):
    await ctx.send('`!help, !kick, !ban, !size, !hello`')


@client.command()
async def channel(ctx):
    await ctx.create_text_channel(ctx)


client.run('TOKEN')
