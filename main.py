import discord
from discord.ext import commands
from botlogic import pass_gen

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'HI! I am a bot{bot.user}')

@bot.command()
async def heh(ctx, count_heh = 5  ):
    await ctx.send('he' * count_heh)

@bot.command()
async def passgen(ctx):
    await ctx.send('halo, berikut password kamu:')
    await ctx.send(pass_gen(8))

@bot.command()
async def pangkatdua(ctx):
    await ctx.send ('masukan angka bebas, nanti aku hitung pangkat 2 nya')
    message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    await ctx.send(f'pangkat 2 dari angka yang kamu kirimkan adalah{(int(message.content)**2)}')

@bot.command()
async def meme(ctx):
    import random, os
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}','rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def octavia(ctx):
    with open('images/octavia.jpeg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def octavia_another_ver(ctx):
    with open('images/oct.jpeg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    import requests
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

daur_ulang = [
    'kertas bekas',
    'kardus',
    'kertas koran',
    'botol plastik',
    'kantong plastik',
    'mainan plastik',
    'tutup botol',
    'kawat',
    'botol kaca',
    'kaca',
    'kotak bekas',
    'karton',
    'piring plastik',
    'majalah',
    'kaleng besi',
    'kemasan minuman',
    'tas belanja',
    'pakaian bekas',
    'sisa makanan',
    'botol susu',
    'botol deterjen',
    'bungkus makanan',
    'wadah yogurt',
    'botol saus',
    'kotak sereal',
    'kertas kado',
    'kertas',
    'brosur'
]

@bot.command()
async def cek_sampah(ctx):
    await ctx.send('Apa sampah yang ingin kamu periksa?')
    message = await bot.wait_for('message', check=lambda m: m.author ==  ctx.author and m.channel == ctx.channel)
    message = str(message.content)

    #proses pemeriksaan
    if message.lower() in daur_ulang:
        await ctx.send('sampah tersebut harus di daur ulang, berikut tips daur ulang sampah tersebut')
        await ctx.send('https://zerowaste.id/zero-waste-lifestyle/proses-daur-ulang-plastik/')
    else:
        await ctx.send('sampah tersebut tidak dapat di daur ulang dan harus di kelola dengan bijak')
        await ctx.send('https://www.goodnewsfromindonesia.id/2023/10/31/gerakan-cegah-pilah-dan-olah-cara-bijak-kelola-sampah')
