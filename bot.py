from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!')

@bot.command(name="idea", help="Get a side project idea")
async def idea(ctx):
    await ctx.send("Ideas are hard")
    await ctx.send("Worry not, I think you should...")

    topics = ['chat bot', 'cli', 'game', 'web bot', 'browser extension', 'api', 'web interface']
    areas = ['note taking', 'social life', 'physical fitness', 'mental health', 'pet care']
    language = ['python', 'java']

    idea = f'Create a new {random.choice(topics)} in {random.choice(language)} that helps with {random.choice(areas)}! :slight_smile:'
    await ctx.send(idea)

@bot.command(name="calc", help="Perform a calculation where fn is either +,-,*, or /")
async def calc(ctx, x, fn, y):
    x = float(x)
    y = float(y)
    if fn == '+':
        await ctx.send(x + y)
    elif fn == '-':
        await ctx.send(x - y)
    elif fn == '*':
        await ctx.send(x * y)
    elif fn == '/':
        await ctx.send(x / y)
    elif fn == '**':
        await ctx.send(x ** y)
    else:
        await ctx.send("We only support 5 function operations")

# make sure to create a token file (in real life use env variables)
with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)

