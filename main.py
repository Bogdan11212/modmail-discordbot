import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user.name}")

@bot.command()
async def modmail(ctx, *, message):
    channel = discord.utils.get(ctx.guild.channels, name="mod-mail")
    if channel is None:
        category = discord.utils.get(ctx.guild.categories, name="Mod Mail")
        if category is None:
            category = await ctx.guild.create_category("Mod Mail")
        channel = await ctx.guild.create_text_channel("mod-mail", category=category)
    else:
        await channel.send(f"New Mod Mail from {ctx.author}: {message}")

@bot.command()
async def close(ctx):
    if ctx.channel.category.name == "Mod Mail":
        await ctx.channel.delete()

bot.run("YOUR_DISCORD_TOKEN")