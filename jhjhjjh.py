from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def lmaolol(ctx, count_lmaolol = 8):
    await ctx.send("lmaolol" * count_lmaolol )
@bot.command()
async def pswd(ctx, longitud = 9):
    await ctx.send(f"Tu contraseña es : {gen_pass(longitud)}")
bot.run("")
