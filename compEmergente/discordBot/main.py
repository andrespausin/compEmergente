import discord
from discord import Intents
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True

# Se crea el cliente del bot. Se le asigna el prefijo de comandos
# Ejemplo: ?hola, ?adios, ?ping
client = commands.Bot(command_prefix = '?', intents=intents)

@client.event
#Función de incio, donde se imprime un mensaje en la consola para saber que el bot está listo
async def on_ready():
    print('El bot está listo.')
    print('----------------------------------')
    
@client.command()
# Función que se ejecuta cuando se escribe ?hola. El bot responde con un mensaje
async def hola(ctx):
    await ctx.send('Hola, {} soy un bot de prueba. ¿Cómo estás? {}'.format(ctx.author.name, ctx.author.mention))
    
@client.command()
# Función que se ejecuta cuando se escribe ?adios. El bot responde con un mensaje
async def adios(ctx):
    await ctx.send('Adiós, {} espero verte pronto. {}'.format(ctx.author.name, ctx.author.mention))

@client.command()    
# Función que se ejecuta cuando se escribe ?ping. El bot responde con un mensaje
async def ping(ctx):
    if(round(client.latency * 1000) > 100):
        await ctx.send('Tienes una latencia muy alta, deberías checkear tu internet no crack :( {}ms'.format(round(client.latency * 1000)) + ' {}'.format(ctx.author.mention))
    else:
        await ctx.send('Tienes una excelente latencia hermano, que crack! {}ms'.format(round(client.latency * 1000)) + ' {}'.format(ctx.author.mention))
        
@client.command()
# Función que se ejecuta cuando se escribe ?info. El bot responde con un mensaje
async def info(ctx):
    await ctx.send('Soy un bot de prueba. Estoy en desarrollo. Gracias por usarme de todos modos. :) {}'.format(ctx.author.mention))
    
@client.command()
# Función que se ejecuta cuando se escribe ?comandos. El bot responde con un mensaje
async def comandos(ctx):
    await ctx.send('Los comandos disponibles son: ?hola, ?adios, ?ping, ?info, ?comandos, ?clear')
            
@client.command()
# Función que se ejecuta cuando se escribe ?clear. El bot borra mensajes del chat
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    
#Se ejecuta el código del bot. Se le asigna el token del bot
client.run('MTE5NDc5MTc2MTgxMDI5Njg3Mw.GbI2jV.3GSmcYPvLo_kHHrEmUgB4_Y8lrYnMEH5wuxfsA') 